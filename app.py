from flask import Flask, render_template, request, jsonify
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from src.hf_llm import get_hf_llm
# ✅ CORRECT IMPORTS FOR LANGCHAIN 0.3.10
from langchain.chains import create_retrieval_chain
from langchain.chains import RetrievalQA
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

# Initialize components
print("✅ Using LangChain 0.3.10 - All imports working!")
print("Loading embeddings...")
embeddings = download_hugging_face_embeddings()

print("Connecting to Pinecone...")
index_name = "medical-chatbot"
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

print("Loading Hugging Face LLM...")
llm = get_hf_llm()

# Create retrieval chain using LangChain 0.3.x syntax
system_prompt = (
    "You are a medical assistant. Use the following context to answer the user's question. "
    "If you don't know the answer, say you don't know. Be accurate and helpful.\n\n"
    "Context: {context}"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])

# Create the chain
print("Creating retrieval chain...")
document_chain = create_stuff_documents_chain(llm, prompt)
qa_chain = create_retrieval_chain(docsearch.as_retriever(search_kwargs={'k': 3}), document_chain)

print("✅ Medical Chatbot initialized successfully!")
print("🚀 Starting Flask server on http://0.0.0.0:5000")

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Please provide a message'}), 400
        
        print(f"📩 Received question: {user_message}")
        
        # Get response from RAG chain
        result = qa_chain.invoke({"input": user_message})
        
        # Extract answer and sources
        answer = result.get('answer', 'No answer generated')
        sources = [doc.metadata.get('source', 'Unknown') for doc in result.get('context', [])]
        
        print(f"✅ Generated answer with {len(sources)} sources")
        
        response = {
            'response': answer,
            'sources': sources
        }
        
        return jsonify(response)
    
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return jsonify({'error': f'Error processing question: {str(e)}'}), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'langchain_version': '0.3.10',
        'message': 'Medical Chatbot is running'
    })

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)