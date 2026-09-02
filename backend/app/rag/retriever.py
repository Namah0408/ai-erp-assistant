from app.rag.config import RETRIEVAL_K
from app.rag.vectorstore import get_vectorstore


def get_retriever():

    vectorstore = get_vectorstore()

    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": RETRIEVAL_K
        }
    )

    return retriever


def retrieve_documents(query: str):

    retriever = get_retriever()

    documents = retriever.invoke(query)

    return documents


def retrieve_context(query: str) -> str:

    documents = retrieve_documents(query)

    if not documents:
        return "No relevant company information was found."

    context_parts = []

    for document in documents:

        source = document.metadata.get(
            "source",
            "Unknown"
        )

        context_parts.append(
            f"Source: {source}\n"
            f"{document.page_content}"
        )

    return "\n\n---\n\n".join(
        context_parts
    )