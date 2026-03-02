# -*- coding: utf-8 -*-
import os
import pandas as pd
import yfinance as yf
from concurrent.futures import ThreadPoolExecutor

CACHE_DIR = "cache"
os.makedirs(CACHE_DIR, exist_ok=True)

def download_stock_data(stock_list):
    stock_data = {}
    def fetch(symbol):
        cache_file = os.path.join(CACHE_DIR, f"{symbol}.csv")
        try:
            if os.path.exists(cache_file):
                df = pd.read_csv(cache_file, index_col=0, parse_dates=True)
            else:
                df = yf.download(symbol, period="1y", interval="1d")
                df.to_csv(cache_file)
            stock_data[symbol] = df
        except Exception as e:
            print(f"⚠ {symbol} 下載失敗: {e}")

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(fetch, stock_list)

    return stock_data
