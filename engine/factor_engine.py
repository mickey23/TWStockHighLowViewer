# -*- coding: utf-8 -*-
def calculate_factors(df):
    """短期因子計算"""
    df = df.copy()
    f = {}
    if "Close" in df:
        f["短期均線"] = df["Close"].rolling(5).mean().iloc[-1]
        f["突破"] = 1 if df["Close"].iloc[-1] > df["Close"].max() else 0
    return f
