from factors.momentum import momentum_factor
from factors.breakout import breakout_factor
from factors.trend import trend_factor
from factors.volume import volume_factor
from factors.volatility import volatility_factor

def calculate_factors(df):
    return {
        "Momentum": momentum_factor(df),
        "Breakout": breakout_factor(df),
        "Trend": trend_factor(df),
        "Volume": volume_factor(df),
        "Volatility": volatility_factor(df)
    }
