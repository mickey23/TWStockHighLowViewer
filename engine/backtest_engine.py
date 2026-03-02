import numpy as np

def backtest_strategy(df):

    df = df.copy()
    df["信號"] = (df["MA20"] > df["MA50"]).astype(int)

    df["策略報酬"] = df["信號"].shift(1) * df["Close"].pct_change()

    total_return = (1 + df["策略報酬"]).prod() - 1
    win_rate = (df["策略報酬"] > 0).mean()

    return total_return, win_rate
