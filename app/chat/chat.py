from app.chat.models import ChatArgs
from app.chat.vector_stores.pinecone import build_retriever

"""
:param chat_args: ChatArgs object containing
    conversation_id, pdf_id, metadata, and streaming flag.

:return: A chain

Example Usage:

    chain = build_chat(chat_args)
"""


def build_chat(chat_args: ChatArgs):
    retriever = build_retriever(chat_args)
