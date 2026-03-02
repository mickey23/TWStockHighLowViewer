def breakout_factor(df):

    df["H60"] = df["High"].rolling(60).max()

    if df["Close"].iloc[-1] >= df["H60"].iloc[-2]:
        return 100

    return 0
