import yfinance as yf

TICKERS = ["VWCE.MI", "JEDI.MI", "EMIM.L", "VVSM.MI", "NUKL.L", "VVMX.MI"]

def get_data(ticker):
    df = yf.download(ticker, period="5y", interval="1d")
    df.dropna(inplace=True)
    return df
