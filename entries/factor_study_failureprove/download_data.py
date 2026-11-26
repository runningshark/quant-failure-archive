# -*- coding: utf-8 -*-
"""
下载并整理本档案用到的数据。全部是公开数据，不需要任何账号或密钥。

  py download_data.py --yahoo     只下载跨资产趋势（第 22 条）要用的 ETF 日线，约 1 分钟。
                                  这份数据来自 Yahoo 财经，不随仓库分发，复现第 22 条之前要先跑这一步。
  py download_data.py             重新下载全部数据（可选，约 15 到 25 分钟）。
                                  仓库里已经带了一份截至 2026-11-25 的币安数据快照（data/），不下载也能复现其余 10 条。
                                  中断了可以直接重跑，已经下载的会跳过；想更新到最新数据，先把 raw 文件夹删掉。
                                  注意：数据更新之后，结果不会再和归档时的数字逐项一致。

数据来源：币安现货和 U 本位合约的公开接口、币安官方数据归档（data.binance.vision）、Yahoo 财经。
"""
import io
import json
import os
import re
import sys
import threading
import time
import urllib.parse
import urllib.request
import zipfile
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
OUT = os.path.join(HERE, "data")
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"}
SPOT = ["https://data-api.binance.vision", "https://api.binance.com", "https://api1.binance.com"]
FAPI = "https://fapi.binance.com"
S3 = "https://s3-ap-northeast-1.amazonaws.com/data.binance.vision"
FUND_PRE = "data/futures/um/monthly/fundingRate/"
YAHOO = ["SPY", "QQQ", "EWJ", "EWY", "EWZ", "EWT", "INDA", "GLD", "SLV", "PPLT", "PALL", "USO", "BNO", "UNG", "CPER", "CORN", "WEAT", "URA", "XLE",
         "FXE", "FXY", "FXB", "UUP", "BTC-USD", "ETH-USD", "^IRX", "TLT", "IEF", "DBC", "EEM", "FXI"]
STABLE = set("USDC BUSD TUSD PAX USDP DAI FDUSD USDS USDSB SUSD UST EUR GBP AUD EURI AEUR USD1 XUSD BFUSD USDE PYUSD RLUSD FRAX VAI USDD BKRW IDRT BIDR "
             "BVND NGN RUB TRY UAH BRL ZAR PLN RON ARS JPY MXN COP CZK USDSOLD U USDF USDX EURC FRXUSD USDG USD0 USDTB USDQ EURQ USDR GUSD LUSD".split())
WRAP = set("WBTC WBETH BETH WETH BNSOL PAXG XAUT STETH WSTETH CBBTC BBTC LBTC SOLVBTC".split())
lock = threading.Lock()
pause = [0.0]


def raw(u, tries=5, timeout=30):
    err = None
    for k in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=timeout).read()
        except Exception as e:
            err = e
            time.sleep(0.5 + k)
    raise err


def api(bases, path, weight_cap):
    """币安接口：留意限速（返回头里有已用权重），被限了就等一会儿；400 表示这个品种没有数据。"""
    err = None
    for k in range(6):
        w = pause[0] - time.time()
        if w > 0:
            time.sleep(min(w, 45))
        base = bases[k % len(bases)] if k >= 2 else bases[0]
        try:
            r = urllib.request.urlopen(urllib.request.Request(base + path, headers=UA), timeout=20)
            if int(r.headers.get("x-mbx-used-weight-1m") or 0) > weight_cap:
                with lock:
                    pause[0] = time.time() + 20
            return json.loads(r.read())
        except urllib.error.HTTPError as e:
            err = "HTTP %s" % e.code
            if e.code in (418, 429):
                with lock:
                    pause[0] = time.time() + 45
            elif e.code == 400:
                return None
            time.sleep(1 + k)
        except Exception as e:
            err = str(e)[:80]
            time.sleep(1 + k)
    raise RuntimeError(err)


def save(fn, obj):
    with open(fn + ".tmp", "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False)
    os.replace(fn + ".tmp", fn)


def pool(fn, items, workers, label):
    done = [0]

    def wrap(x):
        try:
            fn(x)
        except Exception as e:
            print("   失败", str(x).encode("unicode_escape").decode(), str(e)[:80])
        with lock:
            done[0] += 1
            if done[0] % 100 == 0:
                print("   %s %d / %d" % (label, done[0], len(items)))
    with ThreadPoolExecutor(workers) as p:
        list(p.map(wrap, items))


# ---------- 1. 现货日线（含已下架） ----------
def step_spot():
    os.makedirs(os.path.join(RAW, "spot"), exist_ok=True)
    ex = api(SPOT, "/api/v3/exchangeInfo", 4500)
    save(os.path.join(RAW, "spot_ex.json"), ex)
    syms = sorted(s["symbol"] for s in ex["symbols"] if s["quoteAsset"] == "USDT")

    def one(sym):
        fn = os.path.join(RAW, "spot", sym + ".json")
        if os.path.exists(fn):
            return
        rows, start = [], 1483228800000
        while True:
            k = api(SPOT, "/api/v3/klines?symbol=%s&interval=1d&startTime=%d&limit=1000" % (urllib.parse.quote(sym), start), 4500)
            if not k:
                break
            rows += [[x[0], float(x[1]), float(x[2]), float(x[3]), float(x[4]), float(x[7]), x[6]] for x in k]
            if len(k) < 1000:
                break
            start = k[-1][0] + 86400000
        save(fn, rows)
    print("1/6 现货日线：%d 个 USDT 交易对（含已下架）" % len(syms))
    pool(one, syms, 6, "现货")
    return ex


def step_panel(ex):
    info = {s["symbol"]: s for s in ex["symbols"] if s["quoteAsset"] == "USDT"}
    now_ms = time.time() * 1000
    C, H, L, V = {}, {}, {}, {}
    for sym in sorted(info):
        fn = os.path.join(RAW, "spot", sym + ".json")
        if not os.path.exists(fn):
            continue
        rows = [r for r in json.load(open(fn, encoding="utf-8")) if r[6] < now_ms]        # 只要已经走完的日线
        if not rows:
            continue
        idx = pd.to_datetime([r[0] for r in rows], unit="ms")
        C[sym] = pd.Series([r[4] for r in rows], index=idx)
        H[sym] = pd.Series([r[2] for r in rows], index=idx)
        L[sym] = pd.Series([r[3] for r in rows], index=idx)
        V[sym] = pd.Series([r[5] for r in rows], index=idx)
    cal = pd.date_range(min(s.index[0] for s in C.values()), max(s.index[-1] for s in C.values()), freq="D")
    wide = lambda d: pd.DataFrame({k: v[~v.index.duplicated()].reindex(cal) for k, v in d.items()})
    close, high, low, qvol = wide(C), wide(H), wide(L), wide(V)
    dead = qvol.fillna(0) <= 0                                   # 成交额为 0 的日子（停牌）当作没有数据
    close, high, low, qvol = close.mask(dead), high.mask(dead), low.mask(dead), qvol.mask(dead)
    bases = {s: info[s]["baseAsset"] for s in close.columns}
    allb = set(bases.values())
    first = close.apply(lambda s: s.first_valid_index())

    def why(sym):
        b = bases[sym]
        if b in STABLE:
            return "稳定币/法币"
        if b in WRAP:
            return "包装资产/黄金"
        if (b.endswith("UP") and b[:-2] + "DOWN" in allb) or (b.endswith("DOWN") and b[:-4] + "UP" in allb):
            return "杠杆代币"
        if (b.endswith("BULL") and b[:-4] + "BEAR" in allb) or (b.endswith("BEAR") and b[:-4] + "BULL" in allb):
            return "杠杆代币"
        if b.endswith("B") and first[sym] is not None and first[sym] >= pd.Timestamp("2026-06-01"):
            return "代币化股票"                                  # 币安 2026 年 6 月起上线的美股代币，名字都以 B 结尾
        return ""
    meta = pd.DataFrame({"base": pd.Series(bases), "status": pd.Series({s: info[s]["status"] for s in close.columns})})
    meta["first"] = first
    meta["last"] = close.apply(lambda s: s.last_valid_index())
    meta["days"] = close.notna().sum()
    meta["excluded"] = [why(s) for s in meta.index]
    vol = (close / close.shift(1) - 1).std()
    peg = ((close.min() > 0.85) & (close.max() < 1.15) & (vol < 0.01)).reindex(meta.index).fillna(False)
    meta.loc[peg & (meta["excluded"] == ""), "excluded"] = "稳定币（按价格判断）"
    os.makedirs(OUT, exist_ok=True)
    for name, df in (("close", close), ("high", high), ("low", low), ("qvol", qvol)):
        df.to_csv(os.path.join(OUT, name + ".csv.gz"), float_format="%.10g", compression="gzip")
    meta.to_csv(os.path.join(OUT, "spot_meta.csv"), encoding="utf-8")
    print("   现货宽表：%s 到 %s，%d 个品种，排除 %d 个，可用 %d 个（其中已下架 %d 个）" % (
        cal[0].date(), cal[-1].date(), close.shape[1], (meta.excluded != "").sum(), (meta.excluded == "").sum(),
        ((meta.excluded == "") & (meta.status != "TRADING")).sum()))
    return close, qvol, meta


# ---------- 2. 哪些币需要资金费和合约日线 ----------
def step_mapping(close, qvol, meta):
    ok = meta.index[meta.excluded == ""]
    hist = close[ok].notna().cumsum()
    liq = qvol[ok].rolling(30, min_periods=20).median().shift(1).where(hist.shift(1) >= 90)
    ever = (liq.rank(axis=1, ascending=False) <= 60).any()
    names = list(ever.index[ever])                               # 曾经进过成交额前 60 的币
    syms, marker = [], ""
    while True:
        x = raw(S3 + "?delimiter=/&prefix=" + FUND_PRE + ("&marker=" + urllib.parse.quote(marker) if marker else "")).decode()
        syms += re.findall(r"<Prefix>" + re.escape(FUND_PRE) + r"([^<]+)/</Prefix>", x)
        nm = re.search(r"<NextMarker>([^<]+)</NextMarker>", x)
        if "<IsTruncated>true</IsTruncated>" not in x or not nm:
            break
        marker = nm.group(1)
    fs = set(syms)
    mp = {}
    for s in names:
        b = meta.loc[s, "base"]
        c = [x for x in (b + "USDT", "1000" + b + "USDT", "1000000" + b + "USDT", "1M" + b + "USDT") if x in fs]
        if b == "LUNA":
            c = [x for x in ("LUNAUSDT", "LUNA2USDT") if x in fs]    # 2022 年 5 月前后是两个不同的币
        if c:
            mp[s] = c
    mp.setdefault("BTCUSDT", ["BTCUSDT"])
    mp.setdefault("ETHUSDT", ["ETHUSDT"])
    save(os.path.join(OUT, "spot2perp.json"), mp)
    print("2/6 曾进过成交额前 60 的币 %d 个，其中有永续合约的 %d 个" % (len(names), len(mp)))
    return mp


# ---------- 3. 资金费率 ----------
def step_funding(mp):
    os.makedirs(os.path.join(RAW, "fund"), exist_ok=True)
    need = sorted({x for v in mp.values() for x in v})

    def one(sym):
        fn = os.path.join(RAW, "fund", sym + ".json")
        if os.path.exists(fn):
            return
        x = raw(S3 + "?delimiter=/&prefix=" + urllib.parse.quote(FUND_PRE + sym + "/")).decode()
        rows = []
        for k in sorted(re.findall(r"<Key>([^<]+\.zip)</Key>", x)):
            z = zipfile.ZipFile(io.BytesIO(raw("https://data.binance.vision/" + urllib.parse.quote(k))))
            for line in z.read(z.namelist()[0]).decode().splitlines()[1:]:
                p = line.split(",")
                if len(p) >= 3 and p[0].strip().isdigit():
                    rows.append([int(p[0]), float(p[2])])
        rows.sort()
        save(fn, rows)
    print("3/6 资金费率（官方归档，按月）：%d 个合约" % len(need))
    pool(one, need, 12, "资金费")
    fx = api([FAPI], "/fapi/v1/exchangeInfo", 1800)
    save(os.path.join(RAW, "fut_ex.json"), fx)
    trading = {s["symbol"] for s in fx["symbols"] if s["status"] == "TRADING"}
    tfn = os.path.join(RAW, "fund_tail.json")
    tail = json.load(open(tfn, encoding="utf-8")) if os.path.exists(tfn) else {}
    start = int((time.time() - 45 * 86400) * 1000)
    todo = [s for s in need if s in trading and s not in tail]
    print("   归档只到上个月，最近 45 天用接口补：%d 个（这个接口限 5 分钟 500 次，所以要等几分钟）" % len(todo))
    for i, s in enumerate(todo):
        j = api([FAPI], "/fapi/v1/fundingRate?symbol=%s&startTime=%d&limit=1000" % (urllib.parse.quote(s), start), 1800)
        tail[s] = [[int(x["fundingTime"]), float(x["fundingRate"])] for x in (j or [])]
        time.sleep(0.62)
        if i % 50 == 49:
            save(tfn, tail)
            print("   补当月 %d / %d" % (i + 1, len(todo)))
    save(tfn, tail)
    return need, tail


# ---------- 4. 合约日线 ----------
def step_perp(need):
    os.makedirs(os.path.join(RAW, "perp"), exist_ok=True)

    def one(sym):
        fn = os.path.join(RAW, "perp", sym + ".json")
        if os.path.exists(fn):
            return
        rows, start = [], 1567296000000
        while True:
            k = api([FAPI], "/fapi/v1/klines?symbol=%s&interval=1d&startTime=%d&limit=1500" % (urllib.parse.quote(sym), start), 1800)
            if not k:
                break
            rows += [[x[0], float(x[4]), float(x[7]), x[6]] for x in k]
            if len(k) < 1500:
                break
            start = k[-1][0] + 86400000
        save(fn, rows)
    print("4/6 永续合约日线：%d 个" % len(need))
    pool(one, need, 4, "合约")


# ---------- 5. 合成资金费和合约价格的宽表 ----------
def step_build(mp, need, tail):
    now_ms = time.time() * 1000
    cal = pd.date_range("2019-09-01", pd.Timestamp.now("UTC").normalize().tz_localize(None) - pd.Timedelta(days=1), freq="D")
    daily = {}
    for p in need:
        fn = os.path.join(RAW, "fund", p + ".json")
        rows = json.load(open(fn, encoding="utf-8")) if os.path.exists(fn) else []
        ev = {int(round(r[0] / 60000.0)): r[1] for r in rows}
        for t, r in tail.get(p, []):
            ev[int(round(t / 60000.0))] = r
        if not ev:
            continue
        s = pd.Series(ev).sort_index()
        day = pd.to_datetime(((s.index.values - 1) // 1440) * 86400, unit="s")       # 00:00 结算的那一笔算在前一天
        daily[p] = s.groupby(day).sum()

    def perp_close(p):
        fn = os.path.join(RAW, "perp", p + ".json")
        if not os.path.exists(fn):
            return None
        rows = [r for r in json.load(open(fn, encoding="utf-8")) if r[3] < now_ms and r[2] > 0]
        if not rows:
            return None
        s = pd.Series([r[1] for r in rows], index=pd.to_datetime([r[0] for r in rows], unit="ms"))
        return s[~s.index.duplicated()]
    F, C = {}, {}
    for spot, perps in mp.items():
        ser = [daily[p].reindex(cal) for p in perps if p in daily]
        if ser:
            if spot == "LUNAUSDT" and len(ser) == 2:
                F[spot] = ser[0].where(cal < pd.Timestamp("2022-05-28"), ser[1])
            else:
                x = ser[0]
                for y in ser[1:]:
                    x = x.fillna(y)
                F[spot] = x
        x = None
        for p in perps:
            s = perp_close(p)
            if s is None:
                continue
            s = s.reindex(cal)
            if x is None:
                x = s
                continue
            add = s.where(x.isna())
            first = add.first_valid_index()
            x = x.fillna(add)
            if first is not None:
                i = x.index.get_loc(first)
                if i > 0 and not np.isnan(x.iloc[i - 1]):
                    x.iloc[i] = np.nan                                               # 换合约的那一天不连着算收益
        if x is not None:
            C[spot] = x
    F, C = pd.DataFrame(F), pd.DataFrame(C)
    F.to_csv(os.path.join(OUT, "funding_daily.csv.gz"), float_format="%.8g", compression="gzip")
    C.to_csv(os.path.join(OUT, "perp_close.csv.gz"), float_format="%.10g", compression="gzip")
    print("5/6 资金费宽表 %d 天 × %d 个币（到 %s）；合约价格宽表 %d 个币" % (F.shape[0], F.shape[1], F.index[-1].date(), C.shape[1]))


# ---------- 6. 跨资产（Yahoo） ----------
def step_yahoo():
    os.makedirs(os.path.join(RAW, "yahoo"), exist_ok=True)
    Y = {}
    for s in YAHOO:
        fn = os.path.join(RAW, "yahoo", s.replace("^", "_") + ".json")
        if not os.path.exists(fn):
            for host in ("query1", "query2", "query1"):
                try:
                    u = "https://%s.finance.yahoo.com/v8/finance/chart/%s?period1=0&period2=9999999999&interval=1d&events=div%%2Csplit" % (host, urllib.parse.quote(s))
                    r = json.loads(raw(u, tries=2))["chart"]["result"][0]
                    q = r["indicators"]["quote"][0]["close"]
                    ac = (r["indicators"].get("adjclose") or [{}])[0].get("adjclose") or q
                    save(fn, [[t, c, a] for t, c, a in zip(r["timestamp"], q, ac) if c is not None and a is not None])
                    break
                except Exception as e:
                    print("   Yahoo 失败", s, str(e)[:60])
                    time.sleep(2)
            time.sleep(0.6)
        if os.path.exists(fn):
            rows = json.load(open(fn, encoding="utf-8"))
            ser = pd.Series([r[2] for r in rows], index=pd.to_datetime([r[0] for r in rows], unit="s").normalize())
            Y[s.replace("^", "_")] = ser[~ser.index.duplicated(keep="last")]
    Y = pd.DataFrame(Y).sort_index()
    os.makedirs(OUT, exist_ok=True)
    Y.to_csv(os.path.join(OUT, "yahoo_adjclose.csv.gz"), float_format="%.8g", compression="gzip")
    if not os.path.exists(os.path.join(OUT, "tbill_13w.csv.gz")) and "_IRX" in Y:      # 美国 13 周国债收益率，资金费篮子（第 23 条）用
        t = Y["_IRX"].dropna().loc["2019-01-01":].rename("yield_pct")
        t.index.name = "date"
        t.to_csv(os.path.join(OUT, "tbill_13w.csv.gz"), float_format="%.4f", compression="gzip")
    print("6/6 跨资产日线 %d 个品种，到 %s" % (Y.shape[1], Y.index[-1].date()))


def main():
    os.makedirs(RAW, exist_ok=True)
    t0 = time.time()
    if "--yahoo" in sys.argv:
        step_yahoo()
        print("完成。接下来可以运行  py verify.py T5")
        return
    ex = step_spot()
    close, qvol, meta = step_panel(ex)
    mp = step_mapping(close, qvol, meta)
    need, tail = step_funding(mp)
    step_perp(need)
    step_build(mp, need, tail)
    step_yahoo()
    print("全部完成，用时 %.0f 分钟。数据在 data 文件夹，接下来运行 verify.py。" % ((time.time() - t0) / 60))


if __name__ == "__main__":
    main()
