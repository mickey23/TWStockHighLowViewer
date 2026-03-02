import requests

def get_twse_list():
    """
    取得上市股票清單（TWSE官方API）
    """
    url = "https://openapi.twse.com.tw/v1/opendata/t187ap03_L"

    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        data = res.json()
        stocks = []

        for item in data:
            # 支援 dict 或 list
            if isinstance(item, dict):
                if "公司代號" in item:
                    stocks.append(item["公司代號"])
                elif "證券代號" in item:
                    stocks.append(item["證券代號"])
            elif isinstance(item, list):
                code = str(item[0]).strip()
                if code.isdigit():
                    stocks.append(code)

        return sorted(list(set(stocks)))

    except Exception as e:
        print("⚠ 無法下載上市股票清單：", e)
        return []

def get_all_taiwan_stocks():
    print("📡 下載台股上市股票清單…")
    stocks = get_twse_list()
    print(f"✅ 共取得 {len(stocks)} 檔股票")
    return stocks
