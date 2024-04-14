import streamlit as st
import random
import time


# 테스트용 임시 응답 설정 
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


def main_page():
    st.set_page_config(
        page_icon="🤖",
        page_title="Build a RAGs bot",
        layout="centered",
        initial_sidebar_state="expanded",
        menu_items=None,
    )
    st.title("Simple RAGs Chatbot")
    st.info(
        "RAG(검색 증강 생성)를 활용하여 개인이 소유한 데이터에 기반한 맞춤형 챗봇 구축하기",
        icon="🚀",
    )


    with st.sidebar:
        ...
    

if __name__=="__main__":
    main_page()