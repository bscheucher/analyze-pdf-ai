import os
from pinecone import Pinecone as PineconeClient
from langchain_community.vectorstores import Pinecone as LangchainPinecone
from app.chat.embeddings.openai import embeddings

# Initialize Pinecone client
pinecone_client = PineconeClient(api_key=os.getenv("PINECONE_API_KEY"))

# Connect to existing Pinecone index with LangChain
vector_store = LangchainPinecone.from_existing_index(
    os.getenv("PINECONE_INDEX_NAME"), embeddings
)


def build_retriever(chat_args):
    search_kwargs = {"filter": {
        "pdf_id": chat_args.pdf_id
    }}
    return vector_store.as_retriever(
        search_kwargs=search_kwargs
    )
