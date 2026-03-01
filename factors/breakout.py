def breakout_factor(df):
    df["H60"] = df["High"].rolling(60).max()
    if df["H60"].iloc[-1] == 0:
        return 0
    return df["High"].iloc[-1] / df["H60"].iloc[-1]
