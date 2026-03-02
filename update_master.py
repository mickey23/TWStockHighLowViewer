# -*- coding: utf-8 -*-
import os
from engine.data_fetcher import download_stock_data, get_all_taiwan_stocks
from engine.factor_engine import calculate_factors
from engine.factor_engine_long import calculate_factors_long
from engine.market_filter import filter_top_volume
from engine.industry_rank import add_industry_rank
import pandas as pd

def main():
    print("🚀 啟動台股自動量化掃描機 v3.5 (Streamlit版)")
    
    # 取得全市場股票清單
    print("📡 取得全市場股票清單...")
    stocks = get_all_taiwan_stocks()
    if not stocks:
        print("⚠ 無法取得股票清單，程式結束")
        return

    # 下載股票資料
    print("⚡ 下載股票資料...")
    stock_data = download_stock_data(stocks)
    if not stock_data:
        print("⚠ 無資料可下載，程式結束")
        return

    # 篩選成交量前500名
    print("📊 篩選成交量前500名...")
    stock_data = filter_top_volume(stock_data, top_n=500)

    # 計算因子
    print("⚡ 計算因子與排名...")
    df_list = []
    for stock, df in stock_data.items():
        f_short = calculate_factors(df)
        f_long = calculate_factors_long(df)
        f_combined = {**f_short, **f_long, "股票代號": stock}
        df_list.append(f_combined)

    df_result = pd.DataFrame(df_list)

    # 加入產業分類排名
    print("⚡ 加入產業分類排名...")
    df_result = add_industry_rank(df_result)

    # 輸出 CSV (繁體中文欄位)
    output_file = "stock_scan_result.csv"
    df_result.to_csv(output_file, index=False, encoding="utf-8-sig")
    print(f"✅ 完成，結果已輸出至 {output_file}")

if __name__ == "__main__":
    main()
