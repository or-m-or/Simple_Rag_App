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
        page_title="Build a RAGs bot - Chatbot",
        layout="centered",
        initial_sidebar_state="expanded",
        menu_items=None,
    )
    st.title("Chat")
    st.info(
        "채팅 ㄱㄱ",
        icon="💬",
    )

    # 채팅 기록 초기화
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # 앱 재실행 시 채팅 메시지 이력 표시
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 사용자와 챗봇 간의 대화 이력 관리
    if prompt := st.chat_input("여기에 질문을 작성해주세요!"):
        # 사용자 메시지를 채팅 이력에 추가
        st.session_state.messages.append({"role": "user", "content": prompt})
        # 채팅 메시지 컨테이너에 사용자 메시지 표시
        with st.chat_message("user"):
            st.markdown(prompt)
        # 채팅 메시지 컨테이너에 챗봇 응답 표시
        with st.chat_message("assistant"):
            response = st.write_stream(response_generator())
        # 챗봇 응답을 채팅 이력에 추가
        st.session_state.messages.append({"role": "assistant", "content": response})


    with st.sidebar:
        ...
    

if __name__=="__main__":
    main_page()