import os
import base64
from openai import OpenAI

def generator_node(state: dict) -> dict:
    print("\n--- NODE: GENERATOR (GPT Image API) ---")
    openai_client = OpenAI()
    iteration = state["iteration"] + 1
    os.makedirs("outputs", exist_ok=True)
    image_path = f"{state['output_dir']}/iter_{state['iteration']}.png"
    refined_prompt = state["current_prompt"]
    
    try:
        print(f"[Generator] Submitting prompt to gpt-image-1-mini...")
        response = openai_client.images.generate(
            model="gpt-image-1-mini",
            prompt=f"{refined_prompt}, unique layout iteration {iteration}, high-contrast, clean corporate tech YouTube thumbnail asset, 4k vector aesthetic.",
            size="1536x1024",
            quality="medium",
            n=1
        )
        
        img_b64_data = response.data[0].b64_json
        img_binary_payload = base64.b64decode(img_b64_data)
        
        with open(image_path, "wb") as f:
            f.write(img_binary_payload)
            
        print(f"[Generator] SUCCESS! Saved iteration asset to: {image_path}")
        return {"current_image_path": image_path, "iteration": iteration}
        
    except Exception as e:
        print(f"[Generator Critical Error] Image generation failed: {e}")
        raise e