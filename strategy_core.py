import pandas as pd
import requests

class Strategy2560:
    def __init__(self):
        self.df = pd.DataFrame()

    def fetch_crypto(self, symbol="BTCUSDT", limit=200):
        url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval=1h&limit={limit}"
        data = requests.get(url).json()
        self.df = pd.DataFrame([{
            "open": float(d[1]),
            "high": float(d[2]),
            "low": float(d[3]),
            "close": float(d[4]),
            "volume": float(d[5])
        } for d in data])

    def calc_indicators(self):
        df = self.df
        df["MA10"] = df["close"].rolling(10).mean()
        df["EMA10"] = df["close"].ewm(span=10, adjust=False).mean()
        df["RSI"] = self._rsi(df["close"])
        self.df = df

    def _rsi(self, series, period=14):
        delta = series.diff()
        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)
        avg_gain = gain.rolling(period).mean()
        avg_loss = loss.rolling(period).mean()
        rs = avg_gain / avg_loss
        return 100 - (100 / (1 + rs))

    def generate_signals(self):
        df = self.df
        df["signal"] = 0
        df.loc[(df["close"] > df["MA10"]) & (df["RSI"] < 70), "signal"] = 1
        df.loc[(df["close"] < df["MA10"]) & (df["RSI"] > 30), "signal"] = -1
        return df

    def update(self):
        try:
            self.fetch_crypto()
            self.calc_indicators()
            self.generate_signals()
            print("Strategy updated")
        except Exception as e:
            print("Error updating strategy:", e)
