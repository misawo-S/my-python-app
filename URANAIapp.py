import streamlit as st
import random

#web画面の見出し
st.title("魔法のmeb占い")

#ボタン設置
if st.button("運勢を占う"):
 kuji=["大吉","吉","凶"]
 result = random.choice(kuji)

#画面に大きく表示
 st.header (f"結果は...{result}!!!")
 st.balloons()

