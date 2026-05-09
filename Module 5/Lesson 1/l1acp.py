from huggingface_hub import InferenceClient
from datetime import datetime
from PIL import Image
from config import HF_API_KEY

MODELS = [
    "skyslayer/sdl",
    "ByteDance/SDXL-Lightning",
    "stabilityai/stable-diffusion-xl-base-1.0",
    "stabilityai/sdxl-turbo",
    "runwayml/stable-diffusion-v1-5",
]

client = InferenceClient(api_key=HF_API_KEY)

print(f"Primary model: {MODELS[0]}")
print("Type 'quit' to exit\n")

while True:
    prompt = input("Enter prompt: ").strip()

    if prompt.lower() in ["quit", "exit", "q"]:
        break

    if not prompt:
        continue

    # Extra payload options
    negative_prompt = input("Enter negative prompt (optional): ").strip()
    guidance_scale = input("Enter guidance scale (optional, default 7.5): ").strip()

    if guidance_scale == "":
        guidance_scale = 7.5
    else:
        guidance_scale = float(guidance_scale)

    # Custom payload
    payload = {
        "inputs": prompt,
        "options": {
            "negative_prompt": negative_prompt,
            "guidance_scale": guidance_scale
        }
    }

    print("Generating...")
    image = None

    for model in MODELS:
        try:
            image = client.text_to_image(
                prompt,
                model=model
            )
            break

        except Exception:
            print("Executing next model...")
            continue

    if image:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"generated_{timestamp}.png"

        image.save(filename)

        print(f"Saved: {filename}")
        print("Custom settings used:")
        print(payload["options"])

        image.show()
        print()

    else:
        print("Error: All models failed.\n")

print("Goodbye!")