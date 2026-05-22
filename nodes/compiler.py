import shutil

def compiler_node(state: dict):
    print("\n--- NODE: COMPILER (Building Outputs) ---")
    history = state.get("history", [])
    if not history:
        print("[Compiler Error] No execution history to summarize.")
        return state
    best_run = max(reversed(history), key=lambda x: x["rating"])
    shutil.copy(best_run["image_path"], f"{state['output_dir']}/final.png")
    print(f"[Compiler] SUCCESS! Saved true refined asset to: outputs/final.png")
    print(f"[Compiler] Chosen: Iteration {best_run['iteration']} (Score: {best_run['rating']}/10)")
    report_md = f"# Thumbnail Agent Framework Report\n\n"
    report_md += f"**Core Video Topic:** {state['video_topic']}\n"
    report_md += f"**Total Loops Evaluated:** {len(history)}\n"
    report_md += f"**Winning Configuration:** Iteration {best_run['iteration']} (Score: {best_run['rating']}/10)\n\n"
    report_md += "---\n\n## Iteration Diagnostic History\n\n"
    
    for run in history:
        report_md += f"### Iteration {run['iteration']}\n"
        report_md += f"- **Vision Engine Rating:** {run['rating']}/10\n"
        report_md += f"- **Local Source Path:** `{run['image_path']}`\n"
        report_md += f"- **Visual Prompt Delivered:**\n  > {run['prompt']}\n"
        report_md += f"- **Critic Review Feedback:**\n  > *{run['critique']}*\n\n"
        report_md += "---\n"
        
    with open("outputs/report.md", "w") as f:
        f.write(report_md)
        
    print("[Compiler] Generated updated history report inside: outputs/report.md")
    return state