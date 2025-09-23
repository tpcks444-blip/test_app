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

st.title("인적사항을 알려주세요")
st.write("인적사항 입력")
st.write("이름, 나이, 성별, 주소를 입력하셔야 합니다.")

name = st.text_input("이름을 입력하세요:")
# 나이는 0에서 부터 120사이의 숫자를 입력하도록 제한 
# 초기값을 25로 설정
age = st.number_input("나이를 입력하세요:", min_value=0, max_value=120, value=25)
address = st.text_input("주소를 입력하세요:")
# radio는 선택할 수 있도록 하는 것으로  ["여자", "남자"] 이게 선택지 
# 여, 남으로 선택 가능
gender = st.radio("성별", ["여", "남"])


# 입력완료라는 버튼을 만듦과 동시에 만약 버튼이 눌렸을때 아래 코드가 실행되도록 함 
if st.button("입력완료"): 
    st.write(f"당신의 이름은 {name}이고, 성별은 {gender}자이고, 나이는 {age}세 입니다. 주소는 {address}입니다. ")
    st.success("데이터가 저장되었습니다.")
