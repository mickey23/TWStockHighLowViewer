def volume_factor(df):
    df["VolMA20"] = df["Volume"].rolling(20).mean()
    if df["VolMA20"].iloc[-1] == 0:
        return 0
    return df["Volume"].iloc[-1] / df["VolMA20"].iloc[-1]
