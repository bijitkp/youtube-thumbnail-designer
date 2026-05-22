import os
from openai import OpenAI
from tavily import TavilyClient

def prompt_writer_node(state: dict) -> dict:
    print(f"\n--- NODE: PROMPT WRITER (Iteration {state['iteration'] + 1}) ---")
    openai_client = OpenAI()
    
    topic = state["video_topic"]
    history = state.get("history", [])

    search_context = ""
    if not history:
        print(f"[Writer] Querying Tavily for topic: '{topic}'")
        try:
            tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
            search_res = tavily_client.search(query=f"{topic} youtube thumbnail concept ideas trends", max_results=3)
            search_context = "\n".join([f"- {r['title']}: {r['content']}" for r in search_res.get('results', [])])
        except Exception as e:
            print(f"[Writer Warning] Search failed, proceeding with raw topic: {e}")

    system_prompt = (
        "You are an elite YouTube thumbnail designer. Your job is to output a highly detailed, "
        "descriptive text prompt for DALL-E 3. Focus entirely on the visual composition, "
        "vibrant colors, and high-contrast elements. Avoid complex text embedding instructions since DALL-E 3 handles text best when integrated naturally."
    )
    
    user_content = f"Create a DALL-E 3 prompt for a thumbnail about: '{topic}'.\n"
    if search_context:
        user_content += f"\nUse these search insights for visual references:\n{search_context}"
        
    if history:
        last_attempt = history[-1]
        user_content += (
            f"\n\nYour previous prompt scored a {last_attempt['rating']}/10. "
            f"Fix this explicit critique from the Vision system:\n\"{last_attempt['critique']}\""
        )

    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content}
        ],
        temperature=0.7
    )
    
    new_prompt = response.choices[0].message.content.strip()
    print(f"[Writer] Drafted DALL-E Prompt: {new_prompt[:120]}...")
    return {"current_prompt": new_prompt}