from llama_index.llms.openai import OpenAI
from llama_index.core import (
    VectorStoreIndex, 
    ServiceContext, 
    SimpleDirectoryReader,
    Settings
)
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from config import config
import logging
import sys
import torch


logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


def initialize_index(model, temperature, provider):
    documents_dir = config["input_directory"]
    reader = SimpleDirectoryReader(input_dir=documents_dir, recursive=True)
    docs = reader.load_data()

    PROMPT = '''
        당신은 사용자가 업로드한 문서에 대한 질문에 대한 답변을 하는 상담사입니다.
        답변은 사실에 근거해야 하며, 어떠한 환상도 포함되어서는 안됩니다.
        
        문서 안에 포함된 내용을 활용해서 최대한 자세히 대답해 주세요.
        답변은 항상 한국어로 대답합니다.
    '''
    
    embed_model = HuggingFaceEmbedding(
        model_name=config["embed_model"]["model_name"]
    )
    
    if provider == "OpenAI":
        llm = OpenAI(
            model=model, 
            temperature=temperature, 
            system_prompt=PROMPT
        )
    else:
        llm = HuggingFaceLLM(
            model_name=model,
            context_window=2048,
            max_new_tokens=256,
            generate_kwargs= {"temperature" : temperature},
            query_wrapper_prompt= PROMPT,
            tokenizer_kwargs={"max_length": 2048},
            model_kwargs={"torch_dtype": torch.float16}
        )

    # 전역 설정
    Settings.llm = llm
    Settings.embed_model = embed_model
    Settings.chunk_size = 1024
    # Settings.node_parser = SentenceSplitter(chunk_size = 512, chunk_overlap=20)
    # Settings.context_window =
    # Settings.chunk_overlap = 
    # service_context = ServiceContext(llm=llm, embed_model=embed_model) # 더 이상 쓰지 않음
    index = VectorStoreIndex.from_documents(docs)
    
    return index
