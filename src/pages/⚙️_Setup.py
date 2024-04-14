import os
import openai
import streamlit as st
from utils import (
    get_files,
)


def setup_page():
    st.set_page_config(
        page_icon="⚙️",
        page_title="Build a RAGs bot - Setup",
        layout="centered",
        initial_sidebar_state="expanded",
        menu_items=None,
    )
    st.title("Setup")
    st.info(
        "설정 관련 설명 작성하기",
        icon="🧤",
    )

    llm_tab, docs_tab = st.tabs(["LLM 설정", "문서 업로드"])
    with llm_tab:
        api_key = st.text_input("👉🏻 OpenAI API Key 를 입력해주세요.", type="password")
        if api_key:
            openai.api_key = api_key
                
        llm_name = st.selectbox(
            "👉🏻 사용할 LLM을 선택해주세요.", ["gpt-3.5-turbo"]
        )
        model_temperature = st.slider(
            "👉🏻 LLM Temperature", min_value=0.0, max_value=1.0, step=0.1
        )
        st.write("---\n")
        if st.button("💾 변경 사항 저장 (Index 초기화)", key="init_index"):
            st.session_state["init_index"] = {
                llm_name, model_temperature, # api_key
            }
    
    with docs_tab:
        st.markdown("> **파일 선택**\n")
        
        uploaded_file = st.file_uploader("👉🏻 새로운 파일 업로드", type=["pdf", "txt", "markdown"])
        if uploaded_file:
            st.session_state['input_file'] = uploaded_file
        else:
            st.warning("파일이 업로드되지 않았습니다.")
        
        # document_text = st.text_area("👉🏻 직접 타이핑하려면 여기에 해당 내용을 작성해주세요")
        # st.session_state['file'] = st.selectbox("👉🏻 이전에 업로드 한 파일을 다시 사용하려면, 아래에서 파일을 선택해주세요.", 
        #                                         key='file_select', 
        #                                         options=get_files())
        
        # if st.session_state['file'] != '(선택)':
        #     st.session_state['input_file'] = os.path.join(os.getcwd(), 'documents', st.session_state['file'])
        # else:
        #     st.warning("파일이 선택되지 않았습니다.")
    
if __name__=="__main__":
    setup_page()