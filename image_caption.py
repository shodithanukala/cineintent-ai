from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

# ----------------------------
# Device Setup
# ----------------------------
device = "cuda" if torch.cuda.is_available() else "cpu"

# ----------------------------
# Load Model Once
# ----------------------------
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
).to(device)


# ----------------------------
# Caption Generator
# ----------------------------
def generate_caption(image):
    """
    Generate a scene description from an image.
    """
    if isinstance(image, str):
        image = Image.open(image)

    inputs = processor(image, return_tensors="pt").to(device)

    with torch.no_grad():
        output = model.generate(**inputs)

    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption
