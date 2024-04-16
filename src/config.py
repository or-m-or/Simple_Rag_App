config = {
    "llm_predict": 
    {
        "gpt-3.5-turbo-0125": "OpenAI" ,
        "gpt-4-turbo": "OpenAI",
        "yanolja/EEVE-Korean-2.8B-v1.0": "HuggingFace",
        "KRAFTON/KORani-v3-13B": "HuggingFace",
    },
    "embed_model": 
    {
        "model_name" : "intfloat/e5-small", # "intfloat/e5-small" # sentence-transformers/all-MiniLM-l6-v2
        "cache_dir"  : "",
    },
    "input_directory"   : "./documents",
    "output_directory" : "./storage",
}