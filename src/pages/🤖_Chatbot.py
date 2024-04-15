import streamlit as st
import openai
from llama_index.llms.openai import OpenAI
try:
    from llama_index import VectorStoreIndex, ServiceContext, Document, SimpleDirectoryReader
except ImportError:
    from llama_index.core import VectorStoreIndex, ServiceContext, Document, SimpleDirectoryReader
from config import config
# import nest_asyncio
# nest_asyncio.apply()


@st.cache_resource(show_spinner=False)
def initialize_index(model, temperature, documents_dir=config["input_directory"]):
    reader = SimpleDirectoryReader(input_dir=documents_dir, recursive=True)
    docs = reader.load_data()
    
    PROMPT = '''
            당신은 KT AIVLE School의 질문에 대한 답변을 하는 상담사이며 AIVLE School관련 질문에 대해 답하는 것이 당신의 임무입니다.
            답변은 사실에 근거해야 하며, 어떠한 환상도 포함되어서는 안됩니다.
            
            문서 안에 포함된 내용을 활용해서 최대한 자세히 대답해 주세요.
            답변은 한국어로 대답합니다.
        '''
        
    llm = OpenAI(model=model, temperature=temperature, system_prompt=PROMPT)
    service_context = ServiceContext.from_defaults(llm=llm)
    index = VectorStoreIndex.from_documents(
        docs, service_context=service_context
    )
    return index


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
    
    if not st.session_state.get('api_key', ''):
        st.error("🚨 Setup page 에서 먼저 API key 를 기입하고 테스트 하고자 하는 문서를 업로드 해주세요")
        return  # Stop further execution of the function if required settings are missing


    # 채팅 메세지 기록 초기화
    if "messages" not in st.session_state.keys():
        st.session_state.messages = [
            {"role": "assistant", "content": "업로드한 문서에 대해 질문을 시작해주세요!"}
        ]
    
    # 인덱스 및 채팅 엔진 초기화
    if "index" not in st.session_state:
        st.session_state.index = initialize_index(st.session_state.model_name, st.session_state.model_temperature)

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