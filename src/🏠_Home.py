import streamlit as st
import random
import time


def main_page():
    st.set_page_config(
        page_icon=":heart:",
        page_title="Build a RAGs bot - Main",
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