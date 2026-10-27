# Kaala Mithra — App Development webpage

This folder contains the complete App Development webpage and its editable source project.

## Open the webpage

Open `index.html` in a modern browser. The built page is self-contained, with its CSS, fonts, logo, and illustrations embedded.

## Included project files

- `index.html` — current ready-to-view webpage
- `index.src.html` — editable HTML source
- `theme.css` and `fonts.css` — page styling and embedded fonts
- `assets/` — logo and original app/service concept images
- `build.py` — rebuilds the standalone `index.html` from the source and assets
- `qa.py` — static checks for page content and links

## Rebuild and check

From this directory, run:

```bash
python3 build.py
python3 qa.py
```

The build script uses Pillow (`PIL`). Install it with `python3 -m pip install Pillow` if it is not already available.

## Contact and visuals

The page is branded as **Kaala Mithra — AI Tech Solution**. WhatsApp and phone links use `+91 63618 42299`. App visuals are illustrative concepts, not client work.
