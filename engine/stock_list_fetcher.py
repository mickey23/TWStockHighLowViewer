# -*- coding: utf-8 -*-
import requests
import pandas as pd
from io import StringIO

def get_twse_list():
    url = "https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=&type=ALL"
    try:
        res = requests.get(url, timeout=10)
        lines = [line for line in res.text.splitlines() if line.startswith('"') and len(line.split('","')) >= 12]
        csv_text = "\n".join(lines)
        if not csv_text:
            print("⚠ 找不到有效 TWSE 股票清單")
            return []

        df = pd.read_csv(StringIO(csv_text))
        df.columns = [c.strip() for c in df.columns]
        if '證券代號' not in df.columns:
            print("⚠ 找不到 TWSE 股票代號欄位")
            return []

        return df['證券代號'].astype(str).tolist()
    except Exception as e:
        print(f"⚠ 無法取得上市股票清單: {e}")
        return []

def get_tpex_list():
    url = "https://openapi.tpex.org.tw/v1/stock/list"
    try:
        res = requests.get(url, timeout=10)
        data = res.json()
        if not data:
            print("⚠ TPEX 股票清單為空")
            return []
        stocks = [item['stockSymbol'] for item in data if 'stockSymbol' in item]
        return stocks
    except Exception as e:
        print(f"⚠ 無法取得上櫃股票清單: {e}")
        return []

def get_all_taiwan_stocks():
    twse = get_twse_list()
    tpex = get_tpex_list()
    return twse + tpex
