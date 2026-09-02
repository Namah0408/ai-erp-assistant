from fastapi import APIRouter
from pydantic import BaseModel

from app.ai.llm import llm_with_tools, tools
from app.ai.prompts import chat_prompt


router = APIRouter(
    prefix="/chat",
    tags=["AI Chat"]
)


class ChatRequest(BaseModel):
    question: str


@router.post("/")
def chat(request: ChatRequest):

    messages = chat_prompt.format_messages(
        question=request.question
    )

    # Ask the LLM what to do
    response = llm_with_tools.invoke(messages)

    # Check whether the LLM wants to use a tool
    if response.tool_calls:

        for tool_call in response.tool_calls:

            tool_name = tool_call["name"]
            tool_args = tool_call["args"]

            selected_tool = next(
                (
                    tool
                    for tool in tools
                    if tool.name == tool_name
                ),
                None
            )

            if selected_tool is None:
                continue

            tool_result = selected_tool.invoke(tool_args)

            messages.append(response)

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call["id"],
                "content": str(tool_result)
            })

        # Ask LLM to turn the database result into a useful answer
        final_response = llm_with_tools.invoke(messages)

        return {
            "question": request.question,
            "answer": final_response.content
        }

    # No tool required
    return {
        "question": request.question,
        "answer": response.content
    }