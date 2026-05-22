import os
from openai import OpenAI
from pydantic import BaseModel

class CriticResponse(BaseModel):
    rating: int
    critique: str

def critic_node(state):
    print(f"\n--- NODE: CRITIC (Iteration {state['iteration']}) ---")
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    prompt = f"""
You are an expert YouTube thumbnail critic.

Evaluate the thumbnail prompt below.

TOPIC:
{state['video_topic']}

PROMPT:
{state['current_prompt']}

Return:
- rating (1-10)
- critique

Be extremely critical.

A score of:
10 = viral world-class thumbnail
9 = exceptional
8 = strong professional quality
7 = average
6 or below = needs major improvement
"""

    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        response_format=CriticResponse
    )

    result = completion.choices[0].message.parsed

    print(f"\n[Critic] Rating: {result.rating}/10")
    print(f"[Critic] Feedback: {result.critique}")

    next_iteration = state["iteration"] + 1

    history_item = {
        "iteration": state["iteration"],
        "rating": result.rating,
        "critique": result.critique,
        "prompt": state["current_prompt"],
        "image_path": state["current_image_path"]
    }

    return {
        "history": [history_item],
        "final_rating": result.rating,
        "iteration": next_iteration
    }