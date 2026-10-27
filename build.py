#!/usr/bin/env python3
"""Build the self-contained Kaala Mithra app-development landing page."""
import base64
import io
import os
import re
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
IMAGES = {
    "%%IMG_HERO%%": ("app-dev-hero.png", 1240, 82),
    "%%IMG_COMMERCE%%": ("commerce-app.png", 1120, 82),
    "%%IMG_BOOKING%%": ("booking-app.png", 1120, 82),
    "%%IMG_OPERATIONS%%": ("operations-app.png", 1120, 82),
    "%%IMG_DISCOVERY%%": ("capability-discovery.png", 960, 80),
    "%%IMG_DESIGN%%": ("capability-design.png", 960, 80),
    "%%IMG_DEVELOPMENT%%": ("capability-development.png", 960, 80),
    "%%IMG_INTEGRATIONS%%": ("capability-integrations.png", 960, 80),
}


def read(name):
    with open(os.path.join(HERE, name), encoding="utf-8") as fh:
        return fh.read()


def image_data(filename, max_width, quality):
    path = os.path.join(ASSETS, filename)
    image = Image.open(path).convert("RGB")
    if image.width > max_width:
        height = round(image.height * max_width / image.width)
        image = image.resize((max_width, height), Image.Resampling.LANCZOS)
    buffer = io.BytesIO()
    image.save(buffer, "JPEG", quality=quality, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(buffer.getvalue()).decode("ascii")


def main():
    html = read("index.src.html")
    css = read("theme.css")
    fonts = read("fonts.css")
    css = css.replace("%%FONTS%%", fonts)
    html = html.replace("%%CSS%%", css)

    logo_path = os.path.join(ASSETS, "logo.png")
    with open(logo_path, "rb") as fh:
        logo = base64.b64encode(fh.read()).decode("ascii")
    html = html.replace("%%LOGO%%", "url('data:image/png;base64," + logo + "')")

    total_image_bytes = 0
    for token, (filename, width, quality) in IMAGES.items():
        data = image_data(filename, width, quality)
        total_image_bytes += len(data)
        if token not in html:
            raise ValueError(f"Expected image token not found: {token}")
        html = html.replace(token, data)

    leftovers = re.findall(r"%%[A-Z_]+%%", html)
    if leftovers:
        raise ValueError("Unresolved build tokens: " + ", ".join(sorted(set(leftovers))))

    output = os.path.join(HERE, "index.html")
    with open(output, "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"Built {output} ({os.path.getsize(output) / 1024:.0f} KB; embedded images {total_image_bytes / 1024:.0f} KB).")


if __name__ == "__main__":
    main()
