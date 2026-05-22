from typing import TypedDict, Annotated
import operator

class FeedbackItem(TypedDict):
    iteration: int
    rating: int
    critique: str
    prompt: str
    image_path: str

class ThumbnailState(TypedDict):
    video_topic: str
    search_summary: str
    current_prompt: str
    current_image_path: str
    iteration: int
    max_iterations: int
    target_rating: int
    output_dir: str
    history: Annotated[list[FeedbackItem], operator.add]
    final_rating: int