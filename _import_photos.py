"""Импорт фото врачей: переименование + сжатие до 512x512 в images/ и public/images/."""
from PIL import Image, ImageOps
import os

SRC = r"C:\Users\shulk\Desktop\Doctors"
BASE = os.path.dirname(os.path.abspath(__file__))
DEST1 = os.path.join(BASE, "images")
DEST2 = os.path.join(BASE, "public", "images")
os.makedirs(DEST1, exist_ok=True)
os.makedirs(DEST2, exist_ok=True)

P = "Photorealistic_professional_medical_headshot_of_202606141935"
MAPPING = {
    f"{P} (4).jpeg": "dr-ahmet-yilmaz.jpg",
    f"{P} (2).jpeg": "dr-mehmet-ozturk.jpg",
    f"{P}.jpeg":     "dr-can-kaya.jpg",
    f"{P} (5).jpeg": "dr-fatma-koc.jpg",
    f"{P} (1).jpeg": "dr-zeynep-arslan.jpg",
    f"{P} (3).jpeg": "dr-elif-demir.jpg",
}

for src_name, out_name in MAPPING.items():
    src_path = os.path.join(SRC, src_name)
    if not os.path.exists(src_path):
        print("MISSING:", src_name); continue
    img = ImageOps.exif_transpose(Image.open(src_path)).convert("RGB")
    # квадрат по центру + ресайз 512
    img = ImageOps.fit(img, (512, 512), Image.LANCZOS, centering=(0.5, 0.42))
    for d in (DEST1, DEST2):
        img.save(os.path.join(d, out_name), "JPEG", quality=85, optimize=True)
    print("OK:", out_name, os.path.getsize(os.path.join(DEST1, out_name)) // 1024, "KB")

print("DONE")
