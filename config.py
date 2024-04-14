config = {
    "llm_predict": 
    {
        "model_name"  : "gpt-3.5-turbo-0125", # # gpt-4
        "temperature" : 0
    },

    "embed_model": 
    {
        "model_name" : "text-embedding-3-small", # "intfloat/e5-small"
        "cache_dir"  : "",
    },

    "input_directory"   : "./documents",
    "persist_directory" : "./storage",
}