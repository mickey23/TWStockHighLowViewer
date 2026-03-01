import os
import pandas as pd
import requests
import json
from datetime import datetime
from engine.factor_engine import calculate_factors
from engine.ranking import score_stock
from engine.walkforward import walk_forward
from engine.portfolio_simulator import simulate_portfolio

DATA_DIR = "data"
OUTPUT_DIR = "output"

def load_stock_list():
    with open("stock_list.txt") as f:
        return [x.strip() for x in f if x.strip()]

def download_data(stock):
    url = f"https://query1.finance.yahoo.com/v7/finance/download/{stock}.TW?period1=0&period2=9999999999&interval=1d&events=history"
    r = requests.get(url)
    path = f"{DATA_DIR}/{stock}.csv"
    with open(path, "wb") as f:
        f.write(r.content)
    return path

def main():

    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    stocks = load_stock_list()

    all_scores = {}
    ranking = []

    for s in stocks:

        path = download_data(s)
        df = pd.read_csv(path)

        factors = calculate_factors(df)
        score = score_stock(factors)

        all_scores[s] = factors
        ranking.append((s, score))

    ranking.sort(key=lambda x: x[1], reverse=True)
    top10 = ranking[:10]

    with open(f"{OUTPUT_DIR}/factor_scores.json", "w") as f:
        json.dump(all_scores, f, indent=4)

    with open(f"{OUTPUT_DIR}/ranking.json", "w") as f:
        json.dump(top10, f, indent=4)

    # 模擬前10組合
    returns = []

    for stock, _ in top10:
        df = pd.read_csv(f"{DATA_DIR}/{stock}.csv")
        wf = walk_forward(df)
        returns.extend(wf)

    stats = simulate_portfolio(returns)

    with open(f"{OUTPUT_DIR}/portfolio_stats.json", "w") as f:
        json.dump(stats, f, indent=4)

if __name__ == "__main__":
    main()
