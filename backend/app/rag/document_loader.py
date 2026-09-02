from langchain_core.documents import Document

from app.rag.config import DOCUMENTS_DIR


def load_documents():
    """
    Load all .txt documents from the company documents directory.
    """

    documents = []

    if not DOCUMENTS_DIR.exists():
        raise FileNotFoundError(
            f"Documents directory does not exist: {DOCUMENTS_DIR}"
        )

    text_files = list(DOCUMENTS_DIR.glob("*.txt"))

    if not text_files:
        raise FileNotFoundError(
            f"No .txt documents found inside: {DOCUMENTS_DIR}"
        )

    for file_path in text_files:

        content = file_path.read_text(
            encoding="utf-8"
        )

        document = Document(
            page_content=content,
            metadata={
                "source": file_path.name,
                "file_path": str(file_path)
            }
        )

        documents.append(document)

    return documents