import pandas as pd

def filter_top_volume(stock_data, top_n=500, min_volume=1000):
    volume_list = []

    for stock, df in stock_data.items():
        if df is None or df.empty or "Volume" not in df.columns:
            continue
        if len(df) < 20:
            continue

        try:
            avg_vol = df["Volume"].rolling(20).mean().iloc[-1]
            if isinstance(avg_vol, pd.Series):
                avg_vol = avg_vol.iloc[-1]
            if pd.isna(avg_vol) or avg_vol < min_volume:
                continue
            volume_list.append((stock, avg_vol))
        except:
            continue

    volume_list.sort(key=lambda x: x[1], reverse=True)
    top_stocks = [x[0] for x in volume_list[:top_n]]
    return top_stocks
