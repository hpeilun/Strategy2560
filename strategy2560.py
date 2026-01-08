def run_strategy(df):
    df = df.copy()

    df["signal"] = 0
    df.loc[df["close"] > df["close"].shift(1), "signal"] = 1
    df.loc[df["close"] < df["close"].shift(1), "signal"] = -1

    return df


def backtest(df):
    trades = 0
    wins = 0
    entry = None

    for i in range(len(df)):
        if df["signal"].iloc[i] == 1 and entry is None:
            entry = df["close"].iloc[i]

        elif df["signal"].iloc[i] == -1 and entry is not None:
            exit_price = df["close"].iloc[i]
            trades += 1
            if exit_price > entry:
                wins += 1
            entry = None

    winrate = (wins / trades * 100) if trades > 0 else 0

    return {
        "trades": trades,
        "wins": wins,
        "winrate": round(winrate, 2)
    }
