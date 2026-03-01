import pandas as pd

def run_backtest(df, signal):

    results = []

    for i in range(len(df)-20):
        if signal.iloc[i]:

            entry = df.iloc[i]["Close"]
            exit_price = df.iloc[i+20]["Close"]
            ret = (exit_price - entry) / entry

            results.append(ret)

    if not results:
        return None

    s = pd.Series(results)

    return {
        "Trades": len(s),
        "WinRate": (s > 0).mean(),
        "AvgReturn": s.mean(),
        "MaxLoss": s.min()
    }
