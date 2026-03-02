import schedule
import time
import subprocess

def job():
    subprocess.run(["python", "update_master.py"])

# 每天下午 15:10 執行
schedule.every().day.at("15:10").do(job)

print("⏰ 排程啟動中...")

while True:
    schedule.run_pending()
    time.sleep(60)
