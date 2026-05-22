def should_continue(state):
    history = state.get("history", [])
    if not history:
        return "continue"

    latest_run = history[-1]
    current_rating = latest_run["rating"]
    current_iteration = state["iteration"]
    target_rating = state.get("target_rating", 8)
    max_iterations = state.get("max_iterations", 3)

    print("\n--- ROUTER DECISION ---")
    print(f"Iteration : {current_iteration}")
    print(f"Rating    : {current_rating}/10")

    if current_rating >= target_rating:
        print("Decision  : FINISH (target reached)")
        return "finish"

    if current_iteration >= max_iterations:
        print("Decision  : FINISH (max iteration reached)")
        return "finish"

    print("Decision  : CONTINUE")

    return "continue"