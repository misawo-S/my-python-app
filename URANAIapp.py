import streamlit as st
import random

# Web画面の見出し
st.title("🔮 名前で占う！魔法のWebアプリ")

# 1. 名前の入力欄を作る
user_name = st.text_input("あなたの名前を入力してください")

# 占いデータ
fortunes = [
    {"result": "伝説の大吉", "item": "金の招き猫"},
    {"result": "そこそこの吉", "item": "使い古した消しゴム"},
    {"result": "のびしろのある凶", "item": "新しいスニーカー"},
    {"result": "ぴかぴかの末吉", "item": "お気に入りのペン"}
]

# 2. ボタン設置（名前が入力されている時だけ動くように工夫）
if st.button("運勢を占う！"):
    if user_name: # もし名前が入っていたら
        # ランダムに選ぶ
        choice = random.choice(fortunes)
        
        # 3. 名前入りの結果を表示
        st.header(f"{user_name} さんの結果は... {choice['result']} !!!")
        st.subheader(f"✨ ラッキーアイテム: {choice['item']}")
        
        # 演出
        st.balloons()
    else:
        # 名前が入っていない時の警告
        st.warning("名前を入力してからボタンを押してね！")