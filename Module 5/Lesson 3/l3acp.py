import os, io, time, requests, mimetypes
from datetime import datetime
from PIL import Image
from config import HF_API_KEY

MODEL = "stabilityai/stable-diffusion-2-inpainting"
API = f"https://router.huggingface.co/hf-inference/models/{MODEL}"
ALLOWED, MAX_MB = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp", ".tiff"}, 8

def ask_image(label, default):
    print(f"\n🖼️  Enter path for {label} (default: {default})")
    while True:
        p = input(f"Path [{default}]: ").strip().strip('"').strip("'") or default
        if not os.path.isfile(p): print("⚠️  Not found."); continue
        if os.path.splitext(p)[1].lower() not in ALLOWED: print("⚠️  Unsupported type."); continue
        if os.path.getsize(p) / (1024 * 1024) > MAX_MB: print("⚠️  Too big (>8MB)."); continue
        try: Image.open(p).verify()
        except: print("⚠️  Corrupted image."); continue
        return p

def generate_inpainting_image(prompt, image_path, mask_path, tries=8):
    mime_img, _ = mimetypes.guess_type(image_path)
    mime_mask, _ = mimetypes.guess_type(mask_path)

    with open(image_path, "rb") as f: img_bytes = f.read()
    with open(mask_path, "rb") as f: mask_bytes = f.read()

    payload = {
        "inputs": prompt,
    }

    for _ in range(tries):
        r = requests.post(
            API,
            headers={"Authorization": f"Bearer {HF_API_KEY}"},
            files={
                "image": (os.path.basename(image_path), img_bytes, mime_img or "image/png"),
                "mask_image": (os.path.basename(mask_path), mask_bytes, mime_mask or "image/png"),
            },
            data={"inputs": prompt},
            timeout=120,
        )
        if r.status_code == 200:
            return Image.open(io.BytesIO(r.content)).convert("RGB")
        if r.status_code == 503:
            print("⏳ Model warming up, retrying..."); time.sleep(3); continue
        raise RuntimeError(f"API {r.status_code}: {r.text[:300]}")
    raise RuntimeError("Model warm-up timeout.")

def main():
    image_path = ask_image("original photo", "old_photo.png")
    mask_path  = ask_image("mask image", "old_photo_mask.png")

    print('\n✏️  Enter a brief restoration description.')
    print('   Example: "restore the torn edges and faded areas"')
    prompt = input("Prompt: ").strip()
    if not prompt:
        prompt = "restore the torn edges and faded areas"
        print(f"   (Using default: {prompt})")

    print("\n🔄 Sending to inpainting model...")
    try:
        result = generate_inpainting_image(prompt, image_path, mask_path)
    except Exception as e:
        return print("❌", e)

    result.show()
    print("✅ Restoration preview displayed.")

    save = input("\n💾 Save the result? (y/n, default: y): ").strip().lower()
    if save != "n":
        out = "old_photo_restored.png"
        result.save(out)
        print(f"✅ Saved: {out}")
    else:
        print("🚫 Result not saved.")

    # Extra exploration: let user try a different mask without restarting
    while True:
        again = input("\n🔁 Try a different mask path? (y/n, default: n): ").strip().lower()
        if again != "y": break
        mask_path = ask_image("new mask image", mask_path)
        print("\n🔄 Re-running with new mask...")
        try:
            result = generate_inpainting_image(prompt, image_path, mask_path)
        except Exception as e:
            print("❌", e); continue
        result.show()
        save = input("💾 Save this result? (y/n, default: y): ").strip().lower()
        if save != "n":
            out = f"old_photo_restored_{datetime.now().strftime('%H%M%S')}.png"
            result.save(out)
            print(f"✅ Saved: {out}")

if __name__ == "__main__": main()