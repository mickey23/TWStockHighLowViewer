import pandas as pd
from engine.stock_list_fetcher import get_all_taiwan_stocks
from engine.data_fetcher import fetch_all
from engine.market_filter import filter_top_volume

# 假設你已經有這些模組
from engine.factor_engine_long import calculate_factors_long
from engine.factor_engine_short import calculate_factors_short
from engine.scoring_engine import calculate_score
from engine.backtest_engine import backtest_simple
from engine.ai_engine import predict_price

def main():
    print("🚀 取得全市場股票清單...")
    stocks = get_all_taiwan_stocks()

    print("⚡ 多線程下載中...")
    stock_data = fetch_all(stocks, max_workers=10)

    print("📊 篩選成交量前500名...")
    top_stocks = filter_top_volume(stock_data, top_n=500)

    long_results = []
    short_results = []

    for stock in top_stocks:
        df = stock_data[stock]
        if df is None or len(df) < 200:
            continue

        # 長期
        f_long = calculate_factors_long(df)
        score_long = calculate_score(f_long)
        back_long = backtest_simple(df, 50, 200)
        pred = predict_price(df)

        long_results.append({
            "Stock": stock,
            **f_long,
            "Score": score_long,
            "Backtest(%)": back_long,
            "PredictedPrice": pred
        })

        # 短期
        f_short = calculate_factors_short(df)
        score_short = calculate_score(f_short)
        back_short = backtest_simple(df, 5, 20)

        short_results.append({
            "Stock": stock,
            **f_short,
            "Score": score_short,
            "Backtest(%)": back_short,
            "PredictedPrice": pred
        })

    df_long = pd.DataFrame(long_results)

    if not df_long.empty and "Score" in df_long.columns:
        df_long = df_long.sort_values("Score", ascending=False)
        df_long.to_csv("master_long_term.csv", index=False)
        print("✅ 已產生 master_long_term.csv")
    else:
        print("⚠ 長期結果為空，未產生檔案")

    df_short = pd.DataFrame(short_results)

    if not df_short.empty and "Score" in df_short.columns:
        df_short = df_short.sort_values("Score", ascending=False)
        df_short.to_csv("master_short_term.csv", index=False)
        print("✅ 已產生 master_short_term.csv")
    else:
        print("⚠ 短期結果為空，未產生檔案")


    print("\n🔥 完成！已產生長短期排行榜")

if __name__ == "__main__":
    main()
