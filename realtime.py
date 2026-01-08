import pandas as pd

def get_realtime(symbol="BTC-USD", period="5d", interval="5m"):
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
        # ⭐ 打包或沒網路時用「假資料」撐住
        return mock_data()
