from langchain_huggingface import HuggingFaceEndpoint
import os

def get_hf_llm():
    """
    Initialize Hugging Face Inference API for medical chatbot
    Using a free, fast model
    """
    # Using a good medical model that's available for free
    repo_id = "microsoft/DialoGPT-medium"  # Good for conversations
    
    llm = HuggingFaceEndpoint(
        repo_id=repo_id,
        task="text-generation",
        huggingfacehub_api_token=os.getenv('HUGGINGFACEHUB_API_TOKEN'),
        model_kwargs={
            "temperature": 0.3,
            "max_new_tokens": 500,
            "do_sample": True
        }
    )
    
    return llm