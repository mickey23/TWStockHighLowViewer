def volatility_factor(df):
    return df["Close"].pct_change().std()
