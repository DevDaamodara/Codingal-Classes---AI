import base64, requests, os, csv
from config import HF_API_KEY

API_URL = "https://router.huggingface.co/v1/chat/completions"
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}", "Content-Type": "application/json"}
MODELS = [
    "Qwen/Qwen2.5-VL-72B-Instruct",
]

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"}

def data_url(b: bytes) -> str:
    return "data:image/jpeg;base64," + base64.b64encode(b).decode("utf-8")

def extract_err(r: requests.Response) -> str:
    try:
        j = r.json()
        return j.get("error", {}).get("message") or str(j)
    except Exception:
        return (r.text or "").strip() or r.reason or "Request failed."

def box(title: str, lines: list[str], icon: str):
    w = max(30, len(title) + 4, *(len(x) for x in lines))
    print("\n" + "┏" + "━" * (w + 2) + "┓")
    print(f"┃ {icon} {title.ljust(w - 2)} ┃")
    print("┣" + "━" * (w + 2) + "┫")
    for x in lines:
        print(f"┃ {x.ljust(w)} ┃")
    print("┗" + "━" * (w + 2) + "┛\n")

def caption_image(image_path: str) -> str | None:
    try:
        with open(image_path, "rb") as f:
            img = f.read()
    except Exception as e:
        box("File Error", [f"Could not load: {image_path}", f"Reason: {e}"], "❌")
        return None

    base = {
        "messages": [{
            "role": "user",
            "content": [
                {"type": "text", "text": "Give a short caption for this image."},
                {"type": "image_url", "image_url": {"url": data_url(img)}},
            ],
        }],
        "max_tokens": 60,
        "temperature": 0.9,
    }

    last = None
    for model in MODELS:
        payload = dict(base, model=model)
        try:
            r = requests.post(API_URL, headers=HEADERS, json=payload, timeout=120)
        except requests.RequestException as e:
            last = f"Request failed: {e}"
            continue

        if r.status_code != 200:
            last = extract_err(r)
            continue

        try:
            d = r.json()
        except Exception:
            last = "Non-JSON response received from the API."
            continue

        cap = (d.get("choices", [{}])[0].get("message", {}).get("content") or "").strip()
        if cap:
            return cap
        last = "No caption found."

    box("Caption Failed", [f"🖼️ Image  : {image_path}", f"❌ Error : {last or 'Unknown error'}"], "⚠️")
    return None

def caption_folder():
    folder = input("📁 Enter folder path (default: images): ").strip() or "images"

    if not os.path.isdir(folder):
        box("Folder Error", [f"Folder not found: {folder}"], "❌")
        return

    images = [f for f in os.listdir(folder) if os.path.splitext(f)[1].lower() in IMAGE_EXTS]

    if not images:
        box("Folder Empty", [f"No images found in: {folder}"], "⚠️")
        return

    verbose = input("🖨️  Print each caption to console? (y/n, default: y): ").strip().lower() != "n"

    results = []
    for filename in images:
        image_path = os.path.join(folder, filename)
        cap = caption_image(image_path)

        if cap:
            results.append((filename, cap))
            if verbose:
                box("Caption Generated", [
                    f"🖼️ Image  : {filename}",
                    "📝 Caption:",
                    f"   {cap}",
                ], "🎉")
        else:
            results.append((filename, "ERROR: caption failed"))

    summary_path = os.path.join(folder, "captions_summary.txt")
    with open(summary_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["image", "caption"])
        writer.writerows(results)

    box("Done", [
        f"✅ Processed : {len(results)} image(s)",
        f"💾 Saved to  : {summary_path}",
    ], "📋")

def main():
    caption_folder()

if __name__ == "__main__":
    main()