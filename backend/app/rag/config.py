from pathlib import Path


# backend/
BACKEND_DIR = Path(__file__).resolve().parents[2]

# ai_erp_assistant/
PROJECT_DIR = BACKEND_DIR.parent

# ai_erp_assistant/data/documents/
DOCUMENTS_DIR = PROJECT_DIR / "data" / "documents"

# ai_erp_assistant/data/chroma_db/
VECTOR_DB_DIR = PROJECT_DIR / "data" / "chroma_db"


COLLECTION_NAME = "novatech_knowledge"

EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

CHUNK_SIZE = 700
CHUNK_OVERLAP = 100

RETRIEVAL_K = 4