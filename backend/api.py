from fastapi import FastAPI
from data_fetcher import get_data, TICKERS
from indicators import add_indicators
from signal_engine import trend_status, entry_signal, exit_signal, sl_tp

app = FastAPI()

@app.get("/signals")
def get_signals():
    results = {}

    for t in TICKERS:
        df = get_data(t)
        df = add_indicators(df)
        last = df.iloc[-1]

        results[t] = {
            "trend": trend_status(last),
            "entry": entry_signal(last),
            "exit": exit_signal(last),
            "sl_tp": sl_tp(last)
        }

    return results
