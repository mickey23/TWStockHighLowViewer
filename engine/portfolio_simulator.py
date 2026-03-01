import numpy as np

def simulate_portfolio(returns):

    returns = np.array(returns)

    cumulative = (1 + returns).cumprod()

    max_drawdown = (cumulative / cumulative.cummax() - 1).min()

    sharpe = returns.mean() / returns.std() * (252 ** 0.5)

    return {
        "TotalReturn": cumulative[-1] - 1,
        "Sharpe": sharpe,
        "MaxDrawdown": max_drawdown
    }
