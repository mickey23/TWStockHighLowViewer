# -*- coding: utf-8 -*-
def calculate_factors_long(df):
    """長期因子計算"""
    df = df.copy()
    f = {}
    if "Close" in df:
        f["長期均線"] = df["Close"].rolling(50).mean().iloc[-1]
    return f
