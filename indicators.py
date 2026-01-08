def EMA(series, n):
    return series.ewm(span=n).mean()
