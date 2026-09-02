import shutil
from uuid import uuid4

from langchain_chroma import Chroma

from app.rag.config import (
    VECTOR_DB_DIR,
    COLLECTION_NAME
)

from app.rag.document_loader import load_documents
from app.rag.text_splitter import split_documents
from app.rag.embeddings import embedding_model


def ingest_documents():

    print("Loading company documents...")

    documents = load_documents()

    print(
        f"Loaded {len(documents)} documents."
    )

    print("Splitting documents into chunks...")

    chunks = split_documents(documents)

    print(
        f"Created {len(chunks)} chunks."
    )

    # Remove existing vector database
    # so repeated ingestion does not create duplicates.
    if VECTOR_DB_DIR.exists():

        print(
            "Removing old Chroma database..."
        )

        shutil.rmtree(
            VECTOR_DB_DIR
        )

    VECTOR_DB_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    print(
        "Generating embeddings and storing them in Chroma..."
    )

    vectorstore = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embedding_model,
        persist_directory=str(VECTOR_DB_DIR)
    )

    ids = [
        str(uuid4())
        for _ in chunks
    ]

    vectorstore.add_documents(
        documents=chunks,
        ids=ids
    )

    print(
        "Knowledge base created successfully."
    )

    print(
        f"Stored {len(chunks)} chunks in Chroma."
    )

    print(
        f"Database location: {VECTOR_DB_DIR}"
    )


if __name__ == "__main__":
    ingest_documents()