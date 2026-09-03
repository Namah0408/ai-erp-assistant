from langchain_core.messages import (
    SystemMessage
)

from langgraph.graph import (
    StateGraph,
    MessagesState,
    START
)

from langgraph.prebuilt import (
    ToolNode,
    tools_condition
)

from app.ai.llm import (
    llm_with_tools,
    tools
)

from app.ai.prompts import (
    SYSTEM_PROMPT
)

from app.graph.memory import (
    checkpointer
)


def agent_node(
    state: MessagesState
):
    """
    Main AI reasoning node.

    The agent receives the conversation,
    decides whether a tool is required,
    and generates either a tool call or
    a final answer.
    """

    messages = [
        SystemMessage(
            content=SYSTEM_PROMPT
        )
    ] + state["messages"]

    response = llm_with_tools.invoke(
        messages
    )

    return {
        "messages": [
            response
        ]
    }


# ToolNode automatically executes
# tools requested by the LLM.
tool_node = ToolNode(
    tools,
    handle_tool_errors=True
)


# Create LangGraph workflow
workflow = StateGraph(
    MessagesState
)


# Add AI reasoning node
workflow.add_node(
    "agent",
    agent_node
)


# Add tool execution node
workflow.add_node(
    "tools",
    tool_node
)


# Graph always starts with the agent
workflow.add_edge(
    START,
    "agent"
)


# After the agent runs:
#
# If tool calls exist:
#     agent -> tools
#
# Otherwise:
#     agent -> END
workflow.add_conditional_edges(
    "agent",
    tools_condition
)


# After tool execution,
# return to the agent.
workflow.add_edge(
    "tools",
    "agent"
)


# Compile graph with persistent memory
erp_graph = workflow.compile(
    checkpointer=checkpointer
)