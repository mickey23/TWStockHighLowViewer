import pandas as pd

def rsi_factor(df, period=14):

    delta = df["Close"].diff()

    gain = (delta.where(delta > 0, 0)).rolling(period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(period).mean()

    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))

    latest_rsi = rsi.iloc[-1]

    if latest_rsi > 60:
        return 100
    elif latest_rsi > 50:
        return 70
    elif latest_rsi > 40:
        return 40
    else:
        return 10
