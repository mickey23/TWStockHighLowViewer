# -*- coding: utf-8 -*-
import pandas as pd

def calculate_score(df):
    if df.empty:
        return df
    df['總分'] = df['突破分數']  # 可加權重或其他因子
    return df.sort_values('總分', ascending=False)
