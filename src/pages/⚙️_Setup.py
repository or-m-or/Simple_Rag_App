import os
import openai
import streamlit as st
from utils import (
    get_files,
)
from config import config


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
        "채팅을 시작하기 전 환경 설정을 먼저 해주세요. \n"
        "1. [LLM 설정] 탭에서 사용하고자 하는 LLM과 관련된 옵션을 설정할 수 있습니다.\n"
        "2. OpenAI 모델을 사용하려면 OpenAI API Key를 입력해주세요\n"
        "3. [문서 업로드] 탭에서 질의를 하고자 하는 문서를 업로드 해주세요.\n" 
        "4. 현재는 PDF, 마크다운 파일만 업로드 가능합니다.",
        icon="🧤"
    )

    llm_tab, docs_tab = st.tabs(["LLM 설정", "문서 업로드"])
    
    with llm_tab:
        model_name = st.selectbox("👉🏻 사용할 LLM을 선택해주세요.", list(config['llm_predict'].keys()))
        st.session_state.model_provider = config['llm_predict'][model_name]
        st.session_state.model_name = model_name
        
        
        if config['llm_predict'][model_name] == "OpenAI":
            api_key = st.text_input("👉🏻 OpenAI API Key 를 입력해주세요.", type="password")
            if api_key:
                st.session_state.api_key = api_key
                os.environ["OPENAI_API_KEY"] = api_key
                openai.api_key = api_key
        
        
        st.session_state.model_temperature = st.slider(
            "👉🏻 LLM Temperature", min_value=0.0, max_value=1.0, step=0.1, 
        )
        st.write("---\n")

            
    # 현재는 PDF 만 됨 
    with docs_tab:
        st.markdown("> **파일 선택**\n")
        uploaded_file = st.file_uploader("👉🏻 새로운 파일 업로드", type=['pdf', 'md'])
        with st.spinner(text="문서 업로드 중..."):
            if uploaded_file:
                document_dir = config['input_directory']
                file_path = os.path.join(document_dir, uploaded_file.name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                st.success(f"파일이 성공적으로 업로드되어 저장되었습니다: {uploaded_file.name}")
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


if __name__=="__main__":
    setup_page()