from langchain_core.tools import tool

from app.rag.retriever import retrieve_context


@tool
def search_company_knowledge(
    query: str
) -> str:
    """
    Search NovaTech Industries company policies,
    procedures, rules, and internal documentation.

    Use this tool when the user asks about company
    policies or procedures such as leave rules,
    HR policies, procurement policies, inventory
    policies, invoice policies, or finance rules.
    """

    return retrieve_context(query)