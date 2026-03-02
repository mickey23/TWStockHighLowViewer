# -*- coding: utf-8 -*-
import os
import pandas as pd
import yfinance as yf
from concurrent.futures import ThreadPoolExecutor

CACHE_DIR = "cache"
os.makedirs(CACHE_DIR, exist_ok=True)

def get_all_taiwan_stocks():
    """回傳台股股票代號列表"""
    # 這裡使用範例清單，建議可改用 TWSE/TPEX API
    twse_list = ["2330.TW", "2317.TW", "2412.TW"]
    return twse_list

def download_stock_data(symbols):
    """多線程下載股票歷史資料"""
    stock_data = {}

    def fetch(symbol):
        try:
            ticker = yf.Ticker(symbol)
            df = ticker.history(period="1y")
            if df.empty:
                return
            stock_data[symbol] = df
        except Exception as e:
            print(f"{symbol} 下載失敗: {e}")

    with ThreadPoolExecutor(max_workers=8) as executor:
        executor.map(fetch, symbols)
    return stock_data
