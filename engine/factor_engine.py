# -*- coding: utf-8 -*-
import pandas as pd

def calculate_factors(stock_data):
    df_result = pd.DataFrame()
    for stock, df in stock_data.items():
        if df.empty: 
            continue
        df_factor = pd.DataFrame({
            "股票代號": stock,
            "MA5": df['Close'].rolling(5).mean().iloc[-1],
            "MA20": df['Close'].rolling(20).mean().iloc[-1],
            "MA60": df['Close'].rolling(60).mean().iloc[-1]
        }, index=[0])
        df_result = pd.concat([df_result, df_factor], ignore_index=True)
    return df_result
