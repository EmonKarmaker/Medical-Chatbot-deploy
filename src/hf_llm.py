from langchain_community.llms import HuggingFaceHub
import os

def get_hf_llm():
    """
    Initialize Hugging Face LLM for medical chatbot
    """
    # Using a good medical-focused model that's free
    repo_id = "microsoft/DialoGPT-medium"  # Good for conversations
    
    llm = HuggingFaceHub(
        repo_id=repo_id,
        model_kwargs={
            "temperature": 0.3,  # Lower for more focused medical responses
            "max_new_tokens": 500,
            "do_sample": True,
            "top_p": 0.95
        },
        huggingfacehub_api_token=os.getenv('HUGGINGFACEHUB_API_TOKEN')
    )
    
    return llm

# Alternative medical-focused model (uncomment if you want to try):
# "microsoft/BioGPT-Large" - specifically trained on biomedical literature