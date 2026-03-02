# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from update_master import main

st.set_page_config(page_title="台股自動量化掃描機", layout="wide")
st.title("📈 台股自動量化掃描機 v3.5")

if st.button("執行量化掃描"):
    st.info("開始執行量化掃描...")
    main()
    if os.path.exists("stock_scan_result.csv"):
        st.success("掃描完成！")
        df = pd.read_csv("stock_scan_result.csv", encoding="utf-8-sig")
        st.dataframe(df)
        st.download_button("下載結果 CSV", data=df.to_csv(index=False, encoding="utf-8-sig"), file_name="stock_scan_result.csv")
    else:
        st.error("掃描失敗，請檢查 log。")
