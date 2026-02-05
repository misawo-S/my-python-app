import streamlit as st
import random

# --- 背景色の設定 ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #4682B4; /* スクショにあるスチールブルー */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- 1. サイドバーの設定 ---
st.sidebar.title("⚙️ 設定・入力")
user_name = st.sidebar.text_input("あなたの名前を入力してください")

# --- 2. メイン画面の見出し ---
st.title("🌈 虹色・魔法の占いアプリ")
st.markdown("---")

# 占いデータ
fortunes = [
    {"result": "伝説の大吉", "item": "金の招き猫"},
    {"result": "そこそこの吉", "item": "使い古した消しゴム"},
    {"result": "のびしろのある凶", "item": "新しいスニーカー"},
    {"result": "ぴかぴかの末吉", "item": "お気に入りのペン"}
]

# --- 3. メインの動作 ---
if st.button("運勢を占う！"):
    if user_name:
        choice = random.choice(fortunes)
        st.balloons()
        st.success(f"✨ {user_name} さんの運勢が決まりました！")
        st.header(f"結果は... {choice['result']} !!!")
        st.info(f"🍀 ラッキーアイテム: {choice['item']}")
    else:
        st.error("左のサイドバーに名前を入力してね！")