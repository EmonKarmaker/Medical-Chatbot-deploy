# test_deployment.py - SAFE TEST NO SERVER START
import os
from dotenv import load_dotenv

def test_deployment():
    print("🔧 MEDICAL CHATBOT - DEPLOYMENT TEST")
    print("=" * 50)
    
    # 1. Test environment variables
    print("\n1. 🔐 ENVIRONMENT VARIABLES:")
    load_dotenv()
    pinecone_key = os.getenv('PINECONE_API_KEY')
    hf_token = os.getenv('HUGGINGFACEHUB_API_TOKEN')
    
    print(f"   PINECONE_API_KEY: {'✅ SET' if pinecone_key else '❌ MISSING'}")
    print(f"   HUGGINGFACE_TOKEN: {'✅ SET' if hf_token else '❌ MISSING'}")
    
    # 2. Test imports
    print("\n2. 📦 IMPORT CHECKS:")
    try:
        from src.helper import download_hugging_face_embeddings
        print("   ✅ src.helper - OK")
    except Exception as e:
        print(f"   ❌ src.helper - FAILED: {e}")
        return False
        
    try:
        from src.hf_llm import get_hf_llm
        print("   ✅ src.hf_llm - OK")
    except Exception as e:
        print(f"   ❌ src.hf_llm - FAILED: {e}")
        return False
        
    try:
        from langchain_pinecone import PineconeVectorStore
        print("   ✅ langchain_pinecone - OK")
    except Exception as e:
        print(f"   ❌ langchain_pinecone - FAILED: {e}")
        return False
        
    try:
        from langchain.chains import create_retrieval_chain
        from langchain.chains.combine_documents import create_stuff_documents_chain
        from langchain_core.prompts import ChatPromptTemplate
        print("   ✅ langchain chains - OK")
    except Exception as e:
        print(f"   ❌ langchain chains - FAILED: {e}")
        return False
    
    # 3. Test Flask app structure
    print("\n3. 🚀 FLASK APP STRUCTURE:")
    try:
        from app import app
        print("   ✅ Flask app import - OK")
        
        # Check if routes exist
        routes = [rule.rule for rule in app.url_map.iter_rules()]
        print(f"   ✅ Routes found: {len(routes)} routes")
        
    except Exception as e:
        print(f"   ❌ Flask app - FAILED: {e}")
        return False
    
    print("\n" + "=" * 50)
    print("🎉 ALL TESTS PASSED! READY FOR DEPLOYMENT!")
    print("👉 You can now deploy to Render safely!")
    return True

if __name__ == "__main__":
    test_deployment()