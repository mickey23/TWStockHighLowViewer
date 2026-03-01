def trend_factor(df):
    df["MA20"] = df["Close"].rolling(20).mean()
    df["MA60"] = df["Close"].rolling(60).mean()
    return 1 if df["MA20"].iloc[-1] > df["MA60"].iloc[-1] else 0
