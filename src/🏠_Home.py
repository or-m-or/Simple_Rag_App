import streamlit as st
import random
import time


def main_page():
    st.set_page_config(
        page_icon=":heart:",
        page_title="Build a RAGs bot, powered by LlamaIndex",
        layout="centered",
        initial_sidebar_state="expanded",
        menu_items=None,
    )
    st.title("Simple RAGs Chatbot")
    st.info(
        "RAG(검색 증강 생성)를 활용하여 개인이 소유한 데이터에 기반한 맞춤형 챗봇 구축하기",
        icon="🚀",
    )


    # 상세 설명 추가
    st.markdown("""            
    > LlamaIndex를 사용하여 구현된 **사용자의 데이터를 기반으로 채팅할 수 있는 간단한 맞춤형 챗봇 예제**입니다.
    
    ### 사용 방법
    아래 단계에 따라 챗봇을 설정하고 사용할 수 있습니다 :

    1. **[Setup]** 페이지의 [문서 업로드] 탭에서 질의하고자 하는 문서를 업로드합니다.
    2. **[Setup]** 페이지의 [LLM 설정] 탭에서 사용할 LLM을 선택합니다.
    3. 설정이 완료되면 **[Chatbot]** 페이지에서 챗봇과의 대화를 시작할 수 있습니다.

    """)
    
    st.write("---\n")
    
    with st.sidebar:
        ...
        # st.write("여기에 사이드바 옵션을 구성할 수 있습니다. 예를 들어 설정을 조정하거나 사용자 계정 정보를 제공하는 옵션 등이 있을 수 있습니다.")
    
    # 추가적인 사용자 인터랙션 요소
    if st.button('시작하기'):
        ...
    

if __name__=="__main__":
    main_page()