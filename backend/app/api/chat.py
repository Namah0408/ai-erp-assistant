from fastapi import APIRouter
from pydantic import BaseModel

from langchain_core.messages import (
    HumanMessage
)

from app.graph.workflow import (
    erp_graph
)


router = APIRouter(
    prefix="/chat",
    tags=["AI Chat"]
)


class ChatRequest(BaseModel):

    question: str

    thread_id: str


@router.post("/")
def chat(
    request: ChatRequest
):

    config = {
        "configurable": {
            "thread_id":
            request.thread_id
        }
    }

    result = erp_graph.invoke(
        {
            "messages": [
                HumanMessage(
                    content=request.question
                )
            ]
        },
        config=config
    )

    final_message = (
        result["messages"][-1]
    )

    return {
        "thread_id":
        request.thread_id,

        "question":
        request.question,

        "answer":
        final_message.content
    }


@router.get(
    "/history/{thread_id}"
)
def get_chat_history(
    thread_id: str
):

    config = {
        "configurable": {
            "thread_id":
            thread_id
        }
    }

    state = erp_graph.get_state(
        config
    )

    messages = state.values.get(
        "messages",
        []
    )

    history = []

    for message in messages:

        if message.type not in [
            "human",
            "ai"
        ]:
            continue

        history.append({
            "role": message.type,
            "content": message.content
        })

    return {
        "thread_id": thread_id,
        "history": history
    }