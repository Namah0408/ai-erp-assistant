from langchain_chroma import Chroma

from app.rag.config import (
    VECTOR_DB_DIR,
    COLLECTION_NAME
)

from app.rag.embeddings import embedding_model


def get_vectorstore():
    """
    Return the persistent local Chroma vector store.
    """

    VECTOR_DB_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    vectorstore = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embedding_model,
        persist_directory=str(VECTOR_DB_DIR)
    )

    return vectorstore