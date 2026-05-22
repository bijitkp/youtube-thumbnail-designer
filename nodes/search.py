from tools.tavily_search import run_web_search

def web_search_node(state: dict) -> dict:
    print("\n--- NODE: WEB SEARCH ---")
    summary = run_web_search(state["video_topic"])
    return {"search_summary": summary, "history": [], "iteration": 0}