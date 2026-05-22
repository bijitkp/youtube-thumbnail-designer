from datetime import datetime
import os

def create_output_dir(topic: str):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    safe_topic = (
        topic.lower()
        .replace(" ", "_")
        .replace("/", "_")
    )

    output_dir = f"outputs/{timestamp}_{safe_topic}"
    os.makedirs(output_dir, exist_ok=True)

    return output_dir