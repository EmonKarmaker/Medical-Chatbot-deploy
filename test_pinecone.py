import os
from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()

def test_pinecone():
    try:
        pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
        indexes = pc.list_indexes()
        print("✅ Pinecone connection successful!")
        print("Available indexes:", indexes)
        return True
    except Exception as e:
        print(f"❌ Pinecone error: {e}")
        return False

if __name__ == "__main__":
    test_pinecone()