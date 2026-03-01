def breakout_60(df):
    df["H60"] = df["High"].rolling(60).max()
    return df["High"] >= df["H60"]
