# -*- coding: utf-8 -*-
import pandas as pd

def add_industry_rank(df):
    """加入產業分類排名"""
    df = df.copy()
    if "產業" not in df.columns:
        df["產業"] = "未分類"
    df["產業排名"] = df.groupby("產業")["短期均線"].rank(ascending=False)
    return df
