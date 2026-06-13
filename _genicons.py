from PIL import Image, ImageDraw, ImageFont
import os

OUT = os.path.dirname(os.path.abspath(__file__))

def load_font(px):
    for name in ["arialbd.ttf", "Arial Bold.ttf", "DejaVuSans-Bold.ttf", "segoeuib.ttf"]:
        try:
            return ImageFont.truetype(name, px)
        except Exception:
            continue
    return ImageFont.load_default()

def make(size):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    r = int(size * 0.22)
    d.rounded_rectangle([0, 0, size - 1, size - 1], radius=r, fill=(13, 27, 78, 255))
    cx, cy = size // 2, int(size * 0.43)
    rad = int(size * 0.21)
    d.ellipse([cx - rad, cy - rad, cx + rad, cy + rad], fill=(244, 196, 48, 255))
    # tooth glyph (navy on gold)
    tw, th = int(size * 0.12), int(size * 0.16)
    tx, ty = cx, cy - int(size * 0.015)
    d.rounded_rectangle([tx - tw, ty - th, tx + tw, ty + int(th * 0.35)], radius=int(tw * 0.85), fill=(13, 27, 78, 255))
    d.polygon([(tx - tw, ty + int(th * 0.25)), (tx - int(tw * 0.15), ty + int(th * 0.25)), (tx - int(tw * 0.5), ty + th)], fill=(13, 27, 78, 255))
    d.polygon([(tx + tw, ty + int(th * 0.25)), (tx + int(tw * 0.15), ty + int(th * 0.25)), (tx + int(tw * 0.5), ty + th)], fill=(13, 27, 78, 255))
    # wordmark
    font = load_font(int(size * 0.115))
    txt = "ArtSmile"
    bb = d.textbbox((0, 0), txt, font=font)
    d.text((cx - (bb[2] - bb[0]) // 2, int(size * 0.70)), txt, font=font, fill=(255, 255, 255, 255))
    return img

for s in [192, 512]:
    make(s).save(os.path.join(OUT, "icon-%d.png" % s))
make(180).save(os.path.join(OUT, "apple-touch-icon.png"))
make(512).save(os.path.join(OUT, "icon-maskable.png"))
make(64).save(os.path.join(OUT, "favicon.png"))
print("ICONS_OK", sorted(f for f in os.listdir(OUT) if f.endswith(".png")))
