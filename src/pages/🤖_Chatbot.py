import streamlit as st


def main_page():

    st.title("Chat")
    st.info(
        "채팅 ㄱㄱ",
        icon="💬",
    )
    st.write("---\n")

    # 채팅 기록 초기화
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # 앱 재실행 시 채팅 메시지 이력 표시
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 사용자와 챗봇 간의 대화 이력 관리
    if prompt := st.chat_input("What is up?"):
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