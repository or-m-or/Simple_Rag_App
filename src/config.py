config = {
    "llm_predict": 
    {
        "openai_model"  : "gpt-3.5-turbo-0125", # # gpt-4
    },
    "embed_model": 
    {
        "model_name" : "intfloat/e5-small", # "intfloat/e5-small" # sentence-transformers/all-MiniLM-l6-v2
        "cache_dir"  : "",
    },
    "input_directory"   : "./documents",
    "output_directory" : "./storage",
}