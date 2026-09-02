from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.retriever import retrieve_documents


router = APIRouter(
    prefix="/knowledge",
    tags=["Knowledge Base"]
)


class KnowledgeSearchRequest(BaseModel):
    query: str


@router.post("/search")
def search_knowledge(
    request: KnowledgeSearchRequest
):

    documents = retrieve_documents(
        request.query
    )

    results = []

    for document in documents:

        results.append({
            "content": document.page_content,
            "source": document.metadata.get(
                "source"
            )
        })

    return {
        "query": request.query,
        "results": results
    }