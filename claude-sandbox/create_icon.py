#!/usr/bin/env python3
"""Create a simple menu bar icon for Claude Sandbox."""

from PIL import Image, ImageDraw
from pathlib import Path

def create_icon():
    # Menu bar icons are typically 22x22 points, @2x = 44x44 pixels
    size = 44
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Draw a simple "C" in a rounded box (Claude-like)
    margin = 4

    # Outer rounded rectangle
    draw.rounded_rectangle(
        [(margin, margin), (size - margin, size - margin)],
        radius=8,
        fill=None,
        outline=(0, 0, 0, 255),
        width=3
    )

    # Draw "C" for Claude
    c_bbox = (margin + 8, margin + 6, size - margin - 8, size - margin - 6)
    draw.arc(c_bbox, start=45, end=315, fill=(0, 0, 0, 255), width=4)

    # Save
    icon_path = Path(__file__).parent / "icon.png"
    img.save(icon_path)
    print(f"Created {icon_path}")

    # Also create @1x version
    img_1x = img.resize((22, 22), Image.Resampling.LANCZOS)
    img_1x.save(Path(__file__).parent / "icon_1x.png")

if __name__ == "__main__":
    create_icon()
