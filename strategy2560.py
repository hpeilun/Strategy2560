def strategy_2560(df):
    signals = []
    for i in range(2, len(df)):
        if (
            df["close"][i-2] > df["ema25"][i-2] and
            df["close"][i-1] > df["ema25"][i-1] and
            df["ema5"][i] > df["ema60"][i]
        ):
            signals.append(("BUY", i, df["close"][i]))

        if df["ema5"][i] < df["ema60"][i]:
            signals.append(("SELL", i, df["close"][i]))
    return signals
