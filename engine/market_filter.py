# -*- coding: utf-8 -*-
import pandas as pd

def filter_top_volume(stock_data, top_n=500):
    avg_volumes = {}
    for stock, df in stock_data.items():
        if df.empty:
            continue
        avg_volumes[stock] = df['Volume'].tail(20).mean()
    top_stocks = sorted(avg_volumes, key=lambda x: avg_volumes[x], reverse=True)[:top_n]
    return {s: stock_data[s] for s in top_stocks}
