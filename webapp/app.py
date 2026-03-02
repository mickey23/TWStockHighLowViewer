import os
import streamlit as st
import pandas as pd

st.title("📈 雙策略量化選股系統")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "..", "master_long_term.csv")

long_df=pd.read_csv(file_path)

file_path = os.path.join(BASE_DIR, "..", "master_short_term.csv")
short_df=pd.read_csv(file_path)

st.header("🅰 長期投資排行")
st.dataframe(long_df.head(10))

st.header("🅱 短線強勢排行")
st.dataframe(short_df.head(10))
