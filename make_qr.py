"""
Генератор QR-кода для ресепшена.
Использование:  python make_qr.py https://artsmile-demo.pages.dev
Результат:      qr_artsmile.png  (брендированный QR с логотипом-цветами клиники)
"""
import sys
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from PIL import Image, ImageDraw, ImageFont
import os

url = sys.argv[1] if len(sys.argv) > 1 else "https://artsmile-demo.pages.dev"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "qr_artsmile.png")

NAVY = (13, 27, 78)
GOLD = (244, 196, 48)
WHITE = (255, 255, 255)

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=14, border=2)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),
    color_mask=SolidFillColorMask(back_color=WHITE, front_color=NAVY),
).convert("RGB")

qw, qh = img.size
# Card with header + caption
pad = 60
header_h = 150
footer_h = 90
canvas = Image.new("RGB", (qw + pad * 2, qh + header_h + footer_h + pad), WHITE)
d = ImageDraw.Draw(canvas)
d.rounded_rectangle([0, 0, canvas.size[0] - 1, canvas.size[1] - 1], radius=40, outline=NAVY, width=6)
d.rounded_rectangle([0, 0, canvas.size[0] - 1, header_h], radius=40, fill=NAVY)
d.rectangle([0, header_h - 40, canvas.size[0], header_h], fill=NAVY)

def font(px, bold=True):
    for n in (["arialbd.ttf", "segoeuib.ttf"] if bold else ["arial.ttf", "segoeui.ttf"]):
        try:
            return ImageFont.truetype(n, px)
        except Exception:
            continue
    return ImageFont.load_default()

def centered(text, y, f, fill):
    bb = d.textbbox((0, 0), text, font=f)
    d.text(((canvas.size[0] - (bb[2] - bb[0])) // 2, y), text, font=f, fill=fill)

centered("🦷 ArtSmile", 30, font(54), GOLD)
centered("Online randevu / Online booking", 100, font(26, False), WHITE)
canvas.paste(img, (pad, header_h + 25))
centered("Tara & uygulamayı yükle", qh + header_h + 40, font(30), NAVY)
centered("Scan & install the app", qh + header_h + 78, font(24, False), (107, 114, 128))

canvas.save(OUT, quality=95)
print("QR saved:", OUT)
print("URL encoded:", url)
