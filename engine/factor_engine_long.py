import pandas as pd


def normalize_columns(df):
    """
    確保欄位為單層，且 Close 為 Series
    """
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # 如果 Close 仍是 DataFrame（極少數情況）
    if isinstance(df["Close"], pd.DataFrame):
        df["Close"] = df["Close"].iloc[:, 0]

    return df


def calculate_factors_long(df):

    df = df.copy()
    df = normalize_columns(df)

    if len(df) < 120:
        return {}

    # 均線
    df["MA50"] = df["Close"].rolling(50).mean()
    df["MA200"] = df["Close"].rolling(200).mean()

    # 突破
    df["H120"] = df["High"].rolling(120).max()

    latest = df.iloc[-1]
    prev = df.iloc[-2]

    factors = {}

    factors["GoldenCross"] = 100 if latest["MA50"] > latest["MA200"] else 0
    factors["Breakout120"] = 100 if latest["Close"] > prev["H120"] else 0

    return factors
