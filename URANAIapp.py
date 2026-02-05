import streamlit as st
import random

#web画面の見出し
st.title("魔法のweb占い")

# 占いデータ（運勢とアイテムのセット）
fortunes = [
    {"result": "大吉", "item": "金の招き猫"},
    {"result": "中吉", "item": "使い古した消しゴム"},
    {"result": "吉", "item": "新しいスニーカー"},
    {"result": "凶", "item": "お気に入りのペン"}
]

#ボタン設置
if st.button("運勢を占う"):
 #リストから１セットをランダムに選ぶ
 choice = random.choice(fortunes)

#画面に大きく表示
 st.header (f"結果は...{choice['result']}!!!")
 st.subheader(f"ラッキーアイテム：{choice['item']}")
 st.balloons()
 

