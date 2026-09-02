from langchain_huggingface import HuggingFaceEmbeddings

from app.rag.config import EMBEDDING_MODEL_NAME


embedding_model = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL_NAME,
    encode_kwargs={
        "normalize_embeddings": True
    }
)