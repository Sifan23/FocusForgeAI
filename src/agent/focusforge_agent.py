"""FocusForge AI agent with LangGraph and tools."""

from langchain_core.tools import tool


@tool
def placeholder_tool(query: str) -> str:
    """Placeholder tool - replace with actual agent tools."""
    return f"Processed: {query}"


# Agent graph will be defined here
