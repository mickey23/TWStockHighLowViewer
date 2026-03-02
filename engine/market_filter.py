# -*- coding: utf-8 -*-
def filter_top_volume(stock_data, top_n=500):
    """依成交量篩選前 top_n 股票"""
    volume_list = []
    for stock, df in stock_data.items():
        avg_vol = df["Volume"].tail(20).mean()
        volume_list.append((stock, avg_vol))
    volume_list.sort(key=lambda x: x[1], reverse=True)
    top_stocks = [s for s, v in volume_list[:top_n]]
    return {s: stock_data[s] for s in top_stocks}
