#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Curriculum Packager:
Combines Level A0, A1, A2, B1, and B2 into complete DeutschMeister Curriculum:
- 65 Lessons total
- 4,250 Words total:
    * A0: 5 Lessons, 50 Words (Phonetics & Pronunciation)
    * A1: 15 Lessons, 1,050 Words (Goethe A1)
    * A2: 15 Lessons, 1,050 Words (Goethe A2)
    * B1: 15 Lessons, 1,050 Words (Goethe B1)
    * B2: 15 Lessons, 1,050 Words (Goethe B2 / TestDaF)
Outputs:
  - tools/curriculum.json
  - android/app/src/main/assets/curriculum_data.json
"""

import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
sys.path.insert(0, BASE_DIR)

from data.level_a0 import get_level_a0

def main():
    print("=" * 60)
    print("BUILDING COMPLETE MASTER CURRICULUM (A0 - B2)")
    print("=" * 60)

    # 1. Level A0
    a0 = get_level_a0()
    a0_words = sum(len(l["words"]) for l in a0["lessons"])
    print(f"[+] Loaded A0: {len(a0['lessons'])} lessons, {a0_words} words.")

    # 2. Level A1
    a1_path = os.path.join(DATA_DIR, "curriculum_a1.json")
    with open(a1_path, "r", encoding="utf-8") as f:
        a1 = json.load(f)
    a1_words = sum(len(l["words"]) for l in a1["lessons"])
    print(f"[+] Loaded A1: {len(a1['lessons'])} lessons, {a1_words} words.")

    # 3. Level A2
    a2_path = os.path.join(DATA_DIR, "curriculum_a2.json")
    with open(a2_path, "r", encoding="utf-8") as f:
        a2 = json.load(f)
    a2_words = sum(len(l["words"]) for l in a2["lessons"])
    print(f"[+] Loaded A2: {len(a2['lessons'])} lessons, {a2_words} words.")

    # 4. Level B1
    b1_path = os.path.join(DATA_DIR, "curriculum_b1.json")
    with open(b1_path, "r", encoding="utf-8") as f:
        b1 = json.load(f)
    b1_words = sum(len(l["words"]) for l in b1["lessons"])
    print(f"[+] Loaded B1: {len(b1['lessons'])} lessons, {b1_words} words.")

    # 5. Level B2
    b2_path = os.path.join(DATA_DIR, "curriculum_b2.json")
    with open(b2_path, "r", encoding="utf-8") as f:
        b2 = json.load(f)
    b2_words = sum(len(l["words"]) for l in b2["lessons"])
    print(f"[+] Loaded B2: {len(b2['lessons'])} lessons, {b2_words} words.")

    all_levels = [a0, a1, a2, b1, b2]
    total_lessons = sum(len(lvl["lessons"]) for lvl in all_levels)
    total_words = sum(sum(len(l["words"]) for l in lvl["lessons"]) for lvl in all_levels)
    total_quizzes = sum(sum(len(l.get("quiz", [])) for l in lvl["lessons"]) for lvl in all_levels)

    master_data = {
        "appName": "DeutschMeister (德语大师)",
        "version": "2.0.0",
        "description": "专业德语等级通关系统 (CEFR A0-B2) 包含完整的音标、真实例句、动词/名词变位及语法精讲与歌德真题库",
        "levels": all_levels
    }

    # Write tools/curriculum.json
    tools_out = os.path.join(BASE_DIR, "curriculum.json")
    with open(tools_out, "w", encoding="utf-8") as f:
        json.dump(master_data, f, ensure_ascii=False, indent=2)
    print(f"\n[OK] Saved {tools_out} ({os.path.getsize(tools_out):,} bytes)")

    # Write android/app/src/main/assets/curriculum_data.json
    assets_dir = os.path.join(os.path.dirname(BASE_DIR), "android", "app", "src", "main", "assets")
    os.makedirs(assets_dir, exist_ok=True)
    assets_out = os.path.join(assets_dir, "curriculum_data.json")
    with open(assets_out, "w", encoding="utf-8") as f:
        json.dump(master_data, f, ensure_ascii=False, indent=2)
    print(f"[OK] Saved {assets_out} ({os.path.getsize(assets_out):,} bytes)")

    print("\n" + "=" * 60)
    print("MASTER CURRICULUM SUMMARY:")
    print(f"Total Levels: 5 (A0, A1, A2, B1, B2)")
    print(f"Total Lessons: {total_lessons}")
    print(f"Total Words: {total_words}")
    print(f"Total Quizzes: {total_quizzes}")
    print("=" * 60)

if __name__ == "__main__":
    main()
