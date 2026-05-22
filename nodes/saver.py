import os

def saver_node(state: dict) -> dict:
    print("\n--- NODE: SAVER ---")
    history = state["history"]
    best_run = max(history, key=lambda x: x["rating"])

    if os.path.exists(best_run["image_path"]):
        with open(best_run["image_path"], "rb") as src, open("outputs/final.png", "wb") as dest:
            dest.write(src.read())

    report = f"# Thumbnail Designer Run Trace\n\n**Topic:** {state['video_topic']}\n\n## Summary\n"
    report += f"- Best Score: **{best_run['rating']}/10**\n- Loops: {len(history)}\n\n## Trace History\n"
    for i, run in enumerate(history):
        report += f"### Iteration {i+1}\n- **Prompt:** {run['prompt']}\n- **Rating:** {run['rating']}/10\n- **Critique:** {run['critique']}\n\n---\n"
        
    with open("outputs/report.md", "w") as f:
        f.write(report)
    print("Execution trace locked cleanly into outputs/ directory.")
    return {}