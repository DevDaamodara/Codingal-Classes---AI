from huggingface_hub import InferenceClient
from PIL import Image, ImageEnhance, ImageFilter
from config import HF_API_KEY

client = InferenceClient(
    provider="hf-inference",
    api_key=HF_API_KEY,
)

MODEL = "black-forest-labs/FLUX.1-schnell"

def generate_image_from_text(prompt):
    print("🎨 Generating image using FLUX model...\n")
    image = client.text_to_image(prompt, model=MODEL)
    return image.convert("RGB")

def apply_daylight(image):
    image = ImageEnhance.Brightness(image).enhance(1.3)   # +30% brightness
    image = ImageEnhance.Contrast(image).enhance(1.1)     # +10% contrast
    image = image.filter(ImageFilter.GaussianBlur(radius=1))
    return image

def apply_night(image):
    image = ImageEnhance.Contrast(image).enhance(1.4)     # +40% contrast
    image = ImageEnhance.Brightness(image).enhance(0.9)   # -10% brightness
    image = image.filter(ImageFilter.GaussianBlur(radius=0.5))
    return image

def main():
    print("Welcome to the Post-Processing Magic Workshop!")
    print("This program generates AI images with two mood editions.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input('Enter image prompt (e.g., "a magical forest at sunrise"):\n').strip()

        if user_input.lower() == "exit":
            print("Goodbye!"); break

        if not user_input:
            print("Please enter a valid prompt.\n"); continue

        try:
            image = generate_image_from_text(user_input)

            print("☀️  Applying Daylight Edition...")
            daylight = apply_daylight(image)

            print("🌙 Applying Night Mood...")
            night = apply_night(image)

            # Build filenames from the prompt
            slug = user_input.lower().replace(" ", "_")[:30]
            daylight_file = f"{slug}_daylight.png"
            night_file    = f"{slug}_night.png"

            daylight.save(daylight_file)
            night.save(night_file)
            print(f"\n✅ Saved: {daylight_file}")
            print(f"✅ Saved: {night_file}")

            print("\n🖼️  Displaying Daylight Edition...")
            daylight.show()

            print("🖼️  Displaying Night Mood...")
            night.show()

            print("\n" + "-" * 80)

        except Exception as e:
            print(f"\n❌ Error: {e}\n")

if __name__ == "__main__":
    main()