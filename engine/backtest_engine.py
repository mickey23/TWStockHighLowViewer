def backtest_simple(df, short_window=20, long_window=60):

    df["MA_S"] = df["Close"].rolling(short_window).mean()
    df["MA_L"] = df["Close"].rolling(long_window).mean()

    df["Signal"] = (df["MA_S"] > df["MA_L"]).astype(int)
    df["Return"] = df["Close"].pct_change()
    df["Strategy"] = df["Signal"].shift(1) * df["Return"]

    cumulative = (1 + df["Strategy"]).cumprod().iloc[-1]

    return round((cumulative - 1) * 100, 2)
