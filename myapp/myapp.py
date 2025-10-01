# 실행방법 : 터미널 창에서 아래 명령어 실행 
# python -m streamlit run c:/Users/user/Desktop/coding_lesson/myapp.py

# 수정이 되면, git에다가 내 컴퓨터에 있는 코드를 올려야 한다
# git에 코드를 업로드 하는 방법 
# 1) vs code의 밑의 창에서 TERMINAL 탭을 클릭!
# 2) git add .  입력 하면, 현재 수정된 파일을 반영할 준비를 한다는 뜻 
# 3) git commit -m "메세지 내용" 수정한 사항을 기록함
# 4) git push origin main 하면 git에다가 수정한 사항을 push 하는 것 

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
st.image("https://i.ibb.co/tMG6Rp0Q/image.jpg",caption="senior")
# 내가 좋아하는 Youtube 채널
st.header("내가 좋아하는 유튜브")


