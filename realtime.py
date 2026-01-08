import pandas as pd

def get_realtime(symbol="BTC-USD", period="1d", interval="5m"):
    try:
        import yfinance as yf
        df = yf.download(
            symbol,
            period=period,
            interval=interval,
            progress=False
        )

        if df.empty:
            raise ValueError("Empty")

        df = df.reset_index()
        df.columns = [c.lower() for c in df.columns]
        return df

    except Exception as e:
        print("⚠ 使用假資料:", e)
        return mock_data()


def mock_data():
    data = {
        "open":  [100,101,102,103,104,105],
        "high":  [101,102,103,104,105,106],
        "low":   [99,100,101,102,103,104],
        "close": [100,102,101,104,105,106],
        "volume":[10,12,11,13,15,14]
    }
    return pd.DataFrame(data)
