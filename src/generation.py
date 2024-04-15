from llama_index.llms.openai import OpenAI
from llama_index.core import (
    VectorStoreIndex, 
    ServiceContext, 
    Document, 
    SimpleDirectoryReader,
)
import nest_asyncio


def initialize_index(model, temperature, documents_dir):
    reader = SimpleDirectoryReader(input_dir=documents_dir, recursive=True)
    docs = reader.load_data()
    
    PROMPT = '''
            당신은 KT AIVLE School의 질문에 대한 답변을 하는 상담사이며 AIVLE School관련 질문에 대해 답하는 것이 당신의 임무입니다.
            답변은 사실에 근거해야 하며, 어떠한 환상도 포함되어서는 안됩니다.
            
            문서 안에 포함된 내용을 활용해서 최대한 자세히 대답해 주세요.
        '''
        
    llm = OpenAI(model=model, temperature=temperature, system_prompt=PROMPT)
    service_context = ServiceContext.from_defaults(llm=llm)
    index = VectorStoreIndex.from_documents(
        docs, service_context=service_context
    )
    return index




nest_asyncio.apply()

