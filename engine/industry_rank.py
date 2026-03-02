# -*- coding: utf-8 -*-
import pandas as pd

INDUSTRY_MAP = {
    # 範例: 股票代號: 產業
    '2330.TW': '半導體',
    '2317.TW': '電子零組件',
    # 其他請自行補
}

def add_industry_rank(df):
    if df.empty:
        return df
    df['產業'] = df['股票代號'].map(lambda x: INDUSTRY_MAP.get(x, '其他'))
    df['產業排名'] = df.groupby('產業')['突破分數'].rank(ascending=False, method='min')
    return df
