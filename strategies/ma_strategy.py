def ma_bullish(df):
    df["MA5"] = df["Close"].rolling(5).mean()
    df["MA20"] = df["Close"].rolling(20).mean()
    df["MA60"] = df["Close"].rolling(60).mean()
    return (df["MA5"] > df["MA20"]) & (df["MA20"] > df["MA60"])
