def momentum_factor(df):
    if len(df) < 120:
        return 0
    return (df["Close"].iloc[-1] / df["Close"].iloc[-120]) - 1
