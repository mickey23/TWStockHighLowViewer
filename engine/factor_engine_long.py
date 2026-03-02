# -*- coding: utf-8 -*-
import pandas as pd

def calculate_factors_long(stock_data):
    result_list = []
    for symbol, df in stock_data.items():
        if df.empty:
            continue
        df['收盤'] = df['Close']
        df['MA20'] = df['Close'].rolling(20).mean()
        df['MA50'] = df['Close'].rolling(50).mean()
        df['突破分數'] = (df['Close'].iloc[-1] > df['MA50'].iloc[-1]) * 100
        df['股票代號'] = symbol
        result_list.append(df.tail(1))
    if result_list:
        return pd.concat(result_list)
    return pd.DataFrame()
