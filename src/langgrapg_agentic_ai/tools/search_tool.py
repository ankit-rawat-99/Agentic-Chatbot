from langchain_tavily import TavilySearch
from langgraph.prebuilt import ToolNode

def get_tools(tavily_api_key: str = None):
    """
    Return the list of tools to be used in the chatbot.
    """
    if tavily_api_key:
        tools = [TavilySearch(max_results=2, tavily_api_key=tavily_api_key)]
    else:
        tools = [TavilySearch(max_results=2)]
    return tools

def create_tool_node(tools):
    """
    creates and returns a tool node for the graph
    """
    return ToolNode(tools=tools)
