# 실행방법 : 터미널 창에서 아래 명령어 실행 
# python -m streamlit run c:/Users/user/Desktop/coding_lesson/myapp.py


# streamlit은 웹사이트를 만들도록 도와주는 python의 라이브러리
import streamlit as st # streamlit을 사용할거라는 뜻 
# pandas는 표 데이터를 다룰 수 있도록 도와주는 python 라이브러리 
import pandas as pd 
# os는 파일을 경로에 만들어주거나, 파일이 있는지 확인해줄 수 있는 라이브러리 
import os 
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&display=swap" rel="stylesheet">
    <style>
    h1 {
        font-family: 'Nanum Pen Script', cursive !important ;
        font-size: 100px !important;
        color: #2a23de !important;
    }
    .korean-font {
        font-family: 'Nanum Pen Script', cursive !important;
        font-size: 36px !important;
        color: #42cc27 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("세찬의 홈페이지")
st.write("안녕하세요 박세찬입니다.")
st.write("저의 홈페이지에 오신 것을 환영합니다.")


# 내가 좋아하는 이미지 
st.header("내가 좋아하는 것들")

# 내가 좋아하는 Youtube 채널
st.header("내가 좋아하는 유튜브")


