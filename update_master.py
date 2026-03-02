# -*- coding: utf-8 -*-
import pandas as pd
from engine.stock_list_fetcher import get_all_taiwan_stocks
from engine.data_fetcher import download_stock_data
from engine.market_filter import filter_top_volume
from engine.factor_engine_long import calculate_factors_long
from engine.industry_rank import add_industry_rank
from engine.score_engine import calculate_score

def main():
    print("🚀 啟動台股自動量化掃描機 v3.5")
    print("📡 取得全市場股票清單...")
    stocks = get_all_taiwan_stocks()
    if not stocks:
        print("⚠ 無法取得股票清單，程式結束")
        return

    print(f"⚡ 下載股票資料 ({len(stocks)} 檔)...")
    stock_data = download_stock_data(stocks)

    print("📊 篩選成交量前500名...")
    top_stocks = filter_top_volume(stock_data, top_n=500)

    print("⚡ 計算因子與排名...")
    df_result = calculate_factors_long(top_stocks)

    print("⚡ 加入產業分類排名...")
    df_result = add_industry_rank(df_result)

    print("⚡ 計算總分...")
    df_result = calculate_score(df_result)

    print("✅ 量化掃描完成")
    df_result.to_csv("scan_result.csv", encoding="utf-8-sig")
    print("📁 輸出 scan_result.csv")

if __name__ == "__main__":
    main()
