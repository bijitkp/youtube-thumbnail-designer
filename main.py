from core.graph import build_graph
from dotenv import load_dotenv
from tools.output_manager import create_output_dir

load_dotenv()

def main():
    #topic = "Agentic AI is the future of AI"
    topic = "Why Python is the best language for AI"

    output_dir = create_output_dir(topic)
    graph = build_graph()

    initial_state = {
        "video_topic": topic,
        "search_summary": "",
        "current_prompt": "",
        "current_image_path": "",
        "iteration": 1,
        "max_iterations": 3,
        "target_rating": 8,
        "output_dir": output_dir,
        "history": [],
        "final_rating": 0
    }

    final_state = graph.invoke(initial_state)

    print("\n================================")
    print("PIPELINE COMPLETED")
    print("================================")
    print(f"\nFinal Rating: {final_state.get('final_rating')}")
    print(f"\nOutputs saved in:")
    print(output_dir)

if __name__ == "__main__":
    main()