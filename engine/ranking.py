def score_stock(factors):

    score = (
        factors["Momentum"] * 0.3 +
        factors["Breakout"] * 0.2 +
        factors["Trend"] * 0.2 +
        factors["Volume"] * 0.2 -
        factors["Volatility"] * 0.1
    )

    return score
