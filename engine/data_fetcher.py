import os
import pandas as pd
import yfinance as yf
from concurrent.futures import ThreadPoolExecutor, as_completed

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)


def clean_columns(df):
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    return df


def fetch_one(stock):

    path = os.path.join(DATA_DIR, f"{stock}.csv")

    try:

        # =========================
        # 如果已有資料 → 只更新新資料
        # =========================
        if os.path.exists(path):

            old_df = pd.read_csv(path)

            if "Date" not in old_df.columns:
                return stock, None

            # 🔥 修正關鍵在這裡
            last_date = pd.to_datetime(old_df["Date"].iloc[-1])
            last_date_str = last_date.strftime("%Y-%m-%d")

            new_df = yf.download(
                f"{stock}.TW",
                start=last_date_str,
                progress=False,
                auto_adjust=False
            )

            if new_df.empty:
                return stock, old_df

            new_df = clean_columns(new_df)
            new_df.reset_index(inplace=True)

            df = pd.concat([old_df, new_df])
            df.drop_duplicates(subset=["Date"], inplace=True)
            df.sort_values("Date", inplace=True)

            df.to_csv(path, index=False)
            return stock, df

        # =========================
        # 第一次下載
        # =========================
        df = yf.download(
            f"{stock}.TW",
            period="1y",
            progress=False,
            auto_adjust=False
        )

        if df.empty:
            return stock, None

        df = clean_columns(df)
        df.reset_index(inplace=True)
        df.to_csv(path, index=False)

        return stock, df

    except Exception as e:
        return stock, None


def fetch_all(stocks, max_workers=10):

    results = {}

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(fetch_one, s) for s in stocks]

        for future in as_completed(futures):
            stock, df = future.result()
            if df is not None:
                results[stock] = df

    return results
