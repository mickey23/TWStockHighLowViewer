from factors.breakout import breakout_factor
from factors.ma_cross import ma_cross_factor
from factors.rsi_factor import rsi_factor

def volume_factor(df):

    df["Vol20"] = df["Volume"].rolling(20).mean()

    if df["Volume"].iloc[-1] > df["Vol20"].iloc[-1]:
        return 100

    return 30


def calculate_factors(df):

    return {
        "Breakout": breakout_factor(df),
        "MA_Cross": ma_cross_factor(df),
        "RSI": rsi_factor(df),
        "Volume": volume_factor(df)
    }
