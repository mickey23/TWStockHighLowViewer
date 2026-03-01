def volume_break(df):
    df["VolMA20"] = df["Volume"].rolling(20).mean()
    return df["Volume"] > df["VolMA20"] * 1.5
