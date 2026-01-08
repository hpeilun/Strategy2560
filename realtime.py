import pandas as pd

def get_realtime(symbol="BTC-USD", period="1d", interval="5m"):
    try:
        import yfinance as yf

        ticker = yf.Ticker(symbol)
        df = ticker.history(period=period, interval=interval)

        if df.empty:
            raise ValueError("Empty data")

        df = df.reset_index()
        df = df.rename(columns={
            "Open": "open",
            "High": "high",
            "Low": "low",
            "Close": "close",
            "Volume": "volume"
        })

        return df

    except Exception as e:
        print("Using mock data:", e)
        return mock_data()


def mock_data():
    data = {
        "open":  [100,101,102,103,104],
        "high":  [101,102,103,104,105],
        "low":   [99,100,101,102,103],
        "close": [100,102,101,104,105],
        "volume":[10,12,11,13,15]
    }
    return pd.DataFrame(data)
