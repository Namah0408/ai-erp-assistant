from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.rag.config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP
)


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
    length_function=len
)


def split_documents(documents):
    """
    Split documents into smaller chunks for embedding and retrieval.
    """

    return text_splitter.split_documents(documents)