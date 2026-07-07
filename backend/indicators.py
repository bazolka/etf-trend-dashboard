import pandas_ta as ta

def add_indicators(df):
    df["EMA20"] = ta.ema(df["Close"], length=20)
    df["EMA50"] = ta.ema(df["Close"], length=50)
    df["EMA100"] = ta.ema(df["Close"], length=100)
    df["SMA200"] = ta.sma(df["Close"], length=200)

    adx = ta.adx(df["High"], df["Low"], df["Close"], length=14)
    df["ADX"] = adx["ADX_14"]

    df["ATR"] = ta.atr(df["High"], df["Low"], df["Close"], length=14)

    macd = ta.macd(df["Close"])
    df["MACD"] = macd["MACDh_12_26_9"]

    df["VOL_MA20"] = df["Volume"].rolling(20).mean()

    return df
