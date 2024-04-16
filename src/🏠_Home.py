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
    아래 단계에 따라 챗봇을 설정하고 사용해 보세요:

    1. **데이터 업로드**: 사용자는 자신의 데이터를 업로드할 수 있습니다. 텍스트 파일, PDF 또는 기타 지원되는 형식을 사용할 수 있습니다.
    2. **챗봇 설정**: 업로드한 데이터에 기반하여 챗봇을 설정할 수 있습니다. 다양한 파라미터를 조정하여 챗봇의 반응을 최적화하세요.
    3. **대화 시작**: 설정이 완료되면 챗봇과의 대화를 시작할 수 있습니다. 챗봇은 업로드한 데이터를 활용하여 질문에 답변합니다.

    ### 기능 소개
    - **데이터 업로드**: 테스트 해보고자하는 문서를 업로드하여 테스트 해볼 수 있습니다.
    - **챗봇 커스터마이징**: 다양한 설정 옵션을 통해 챗봇의 동작을 사용자의 요구에 맞게 조정할 수 있습니다.
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