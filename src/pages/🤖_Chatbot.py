import streamlit as st
from generation import initialize_index
from config import config
# import nest_asyncio
# nest_asyncio.apply()


def main_page():
    st.set_page_config(
        page_icon="🤖",
        page_title="Build a RAGs bot - Chatbot",
        layout="centered",
        initial_sidebar_state="expanded",
        menu_items=None,
    )
    st.title("Simple RAG Chat Example")
    st.info(
        "채팅을 시작하기 전에 아래 항목을 먼저 수행해주세요! \n"
        "1. Setup 페이지의 [LLM 설정]에서 OpenAI의 api key를 먼저 기입해주세요. \n"
        "2. Setup 페이지의 [문서 업로드]에서 테스트 해보고 싶은 문서를 업로드해주세요. \n\n"
        "그런 다음, 업로드한 문서에 대한 채팅을 시작해보세요",
        icon="💬"
    )
    
    with st.sidebar:
        st.header("현재 상태")
        with st.container():
            st.markdown("> LLM 설정")
            st.write("LLM - ", st.session_state.get('model_name', '설정되지 않음'))
            st.write("Temperature - ", st.session_state.get('model_temperature', '설정되지 않음'))
            
            st.markdown("> API 키")
            api_key_status = "✅ SUCCESS" if 'api_key' in st.session_state else "❌ FAIL"
            st.text("OpenAI API Key - {}".format(api_key_status))

            if st.button('세션 초기화'):
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                st.experimental_rerun()
                
                
    if st.session_state.get('model_provider') == 'OpenAI' and \
       ('api_key' not in st.session_state or not st.session_state.api_key):
        st.error("🚨 Setup page 에서 먼저 API key 를 기입하고 테스트 하고자 하는 문서를 업로드 해주세요")
        return  


    # 채팅 메세지 기록 초기화
    if "messages" not in st.session_state.keys():
        st.session_state.messages = [
            {"role": "assistant", "content": "업로드한 문서에 대해 질문을 시작해주세요!"}
        ]
    
    # 인덱스 및 채팅 엔진 초기화
    if "index" not in st.session_state:
        st.session_state.index = initialize_index(
            st.session_state.model_name, 
            st.session_state.model_temperature,
            st.session_state.get('model_provider', 'HuggingFace')
        )

    if "chat_engine" not in st.session_state:
        st.session_state.chat_engine = st.session_state.index.as_chat_engine(chat_mode="condense_question", verbose=True)

    # 사용자 입력 프롬프트 및 채팅 기록 세션에 저장
    if prompt := st.chat_input("Your question"):
        st.session_state.messages.append({"role": "user", "content": prompt})

    # 이전 채팅 기록 출력
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # 마지막 메시지가 어시스턴트가 보낸 메시지가 아닌 경우 새 응답을 생성
    if st.session_state.messages and st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.chat_engine.chat(prompt)
                st.write(response.response)
                message = {"role": "assistant", "content": response.response}
                st.session_state.messages.append(message) # 메세지 기록에 새로운 응답 추가
    
    


if __name__=="__main__":
    main_page()