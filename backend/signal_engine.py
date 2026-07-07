def trend_status(row):
    if row["EMA20"] > row["EMA50"] > row["EMA100"] and row["ADX"] > 25:
        return "BULL"
    if row["ADX"] < 20:
        return "SIDEWAYS"
    return "WEAK"


def entry_signal(row):
    if (
        row["EMA20"] > row["EMA50"] > row["EMA100"] and
        row["Close"] > row["EMA20"] and
        row["ADX"] > 25 and
        row["Volume"] > row["VOL_MA20"] * 1.5
    ):
        return True
    return False


def exit_signal(row):
    if row["Close"] < row["EMA50"] or row["MACD"] < 0 or row["ADX"] < 20:
        return True
    return False


def sl_tp(row):
    sl = row["Close"] - 1.5 * row["ATR"]
    tp = row["Close"] + 2 * row["ATR"]
    return sl, tp
