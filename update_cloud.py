from notify_telegram import send_message

if result["NewHigh_60"] and result["MA_Bullish"] and result["Volume_Break"]:
    msg = f"🚀 {result['Stock']} 創60日新高\n收盤:{result['Close']}"
    send_message(msg)
