import pandas as pd


def normalize_columns(df):
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    if isinstance(df["Close"], pd.DataFrame):
        df["Close"] = df["Close"].iloc[:, 0]

    return df


def calculate_factors_short(df):

    df = df.copy()
    df = normalize_columns(df)

    if len(df) < 60:
        return {}

    df["MA5"] = df["Close"].rolling(5).mean()
    df["MA20"] = df["Close"].rolling(20).mean()

    latest = df.iloc[-1]

    factors = {}
    factors["ShortTrend"] = 100 if latest["MA5"] > latest["MA20"] else 0

    return factors
