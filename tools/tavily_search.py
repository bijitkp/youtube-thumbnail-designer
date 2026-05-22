import os
from tavily import TavilyClient

def run_web_search(topic: str) -> str:
    tavily_key = os.getenv("TAVILY_API_KEY")
    if not tavily_key:
        return "No Tavily API key found. Defaulting to raw topic strategy."
    
    try:
        client = TavilyClient(api_key=tavily_key)
        response = client.search(query=f"{topic} youtube thumbnail ideas hooks", max_results=2)
        return "\n".join([f"- {r['title']}: {r['snippet']}" for r in response.get("results", [])])
    except Exception as e:
        return f"Search engine offline: {e}"