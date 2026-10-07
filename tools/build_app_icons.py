#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates Official German Flag (Schwarz-Rot-Gold) App Icons across all Android mipmap densities:
- 3D Glass German Flag Squircle (ic_launcher.png)
- 3D Glass German Flag Circle (ic_launcher_round.png)
- Adaptive Icon Foreground (ic_launcher_foreground.png)
- Adaptive Icon XML definitions (mipmap-anydpi-v26)
"""

import os
import shutil
from PIL import Image, ImageDraw

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES_DIR = os.path.join(BASE_DIR, "android", "app", "src", "main", "res")

SRC_PATH = "/Users/pioneer/.gemini/antigravity-cli/brain/b791da9a-9ef4-4fb7-88f2-0f39cc143e3e/de_flag_full_1791035934443.jpg"
LOCAL_SRC = os.path.join(BASE_DIR, "tools", "german_flag_icon_master.jpg")

DENSITIES = {
    "mipmap-mdpi": {"fg": 108, "launcher": 48},
    "mipmap-hdpi": {"fg": 162, "launcher": 72},
    "mipmap-xhdpi": {"fg": 216, "launcher": 96},
    "mipmap-xxhdpi": {"fg": 324, "launcher": 144},
    "mipmap-xxxhdpi": {"fg": 432, "launcher": 192},
}

def main():
    print("[*] Building German Flag Android launcher icons...")
    if not os.path.exists(SRC_PATH):
        raise FileNotFoundError(f"Source icon not found at {SRC_PATH}")

    # Copy master icon locally
    shutil.copyfile(SRC_PATH, LOCAL_SRC)
    print(f"[+] Cached German flag master icon at {LOCAL_SRC}")

    img = Image.open(LOCAL_SRC).convert("RGBA")
    # Crop the exact 3D flag squircle card: (102, 90, 922, 910) -> 820x820
    crop = img.crop((102, 90, 922, 910))

    for folder_name, sizes in DENSITIES.items():
        folder_path = os.path.join(RES_DIR, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        fg_size = sizes["fg"]
        launcher_size = sizes["launcher"]

        # 1. Legacy Squircle ic_launcher.png
        sq_img = crop.resize((launcher_size, launcher_size), Image.Resampling.LANCZOS)
        sq_mask = Image.new("L", (launcher_size, launcher_size), 0)
        draw_sq = ImageDraw.Draw(sq_mask)
        draw_sq.rounded_rectangle((0, 0, launcher_size, launcher_size), radius=int(launcher_size * 0.22), fill=255)
        launcher_sq = Image.new("RGBA", (launcher_size, launcher_size), (0, 0, 0, 0))
        launcher_sq.paste(sq_img, (0, 0), sq_mask)
        launcher_sq.save(os.path.join(folder_path, "ic_launcher.png"), "PNG", optimize=True)

        # 2. Legacy Round ic_launcher_round.png
        round_mask = Image.new("L", (launcher_size, launcher_size), 0)
        draw_round = ImageDraw.Draw(round_mask)
        draw_round.ellipse((0, 0, launcher_size, launcher_size), fill=255)
        launcher_round = Image.new("RGBA", (launcher_size, launcher_size), (0, 0, 0, 0))
        launcher_round.paste(sq_img, (0, 0), round_mask)
        launcher_round.save(os.path.join(folder_path, "ic_launcher_round.png"), "PNG", optimize=True)

        # 3. Adaptive Foreground ic_launcher_foreground.png (108dp canvas)
        # The safe area is 72dp in the center (from 18dp to 90dp, which is 66.6% of canvas).
        # We size the badge to 72dp (int(fg_size * 0.666)) and center it.
        safe_dim = int(fg_size * 0.666)
        badge = crop.resize((safe_dim, safe_dim), Image.Resampling.LANCZOS)
        # Apply smooth squircle mask to the badge
        badge_mask = Image.new("L", (safe_dim, safe_dim), 0)
        draw_bm = ImageDraw.Draw(badge_mask)
        draw_bm.rounded_rectangle((0, 0, safe_dim, safe_dim), radius=int(safe_dim * 0.22), fill=255)
        badge_masked = Image.new("RGBA", (safe_dim, safe_dim), (0, 0, 0, 0))
        badge_masked.paste(badge, (0, 0), badge_mask)

        fg_canvas = Image.new("RGBA", (fg_size, fg_size), (0, 0, 0, 0))
        offset = (fg_size - safe_dim) // 2
        fg_canvas.paste(badge_masked, (offset, offset), badge_masked)
        fg_canvas.save(os.path.join(folder_path, "ic_launcher_foreground.png"), "PNG", optimize=True)

        print(f"[+] Generated {folder_name}: fg={fg_size}px, launcher={launcher_size}px")

    # 4. Create mipmap-anydpi-v26 XML definitions
    anydpi_dir = os.path.join(RES_DIR, "mipmap-anydpi-v26")
    os.makedirs(anydpi_dir, exist_ok=True)

    ic_launcher_xml = """<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@color/ic_launcher_background" />
    <foreground android:drawable="@mipmap/ic_launcher_foreground" />
</adaptive-icon>
"""
    with open(os.path.join(anydpi_dir, "ic_launcher.xml"), "w", encoding="utf-8") as f:
        f.write(ic_launcher_xml)

    with open(os.path.join(anydpi_dir, "ic_launcher_round.xml"), "w", encoding="utf-8") as f:
        f.write(ic_launcher_xml)

    print("[+] Generated German flag adaptive icon XML definitions.")

if __name__ == "__main__":
    main()
