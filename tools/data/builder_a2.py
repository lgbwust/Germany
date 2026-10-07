#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builder for Level A2: 15 Lessons x 70 words = 1050 Words.
Merges a2_part1, a2_part2, a2_part3 and generates curriculum_a2.json.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.ipa_helper import get_ipa
from data.a2_part1 import LESSONS_A2_PART1
from data.a2_part2 import LESSONS_A2_PART2
from data.a2_part3 import LESSONS_A2_PART3

def make_word(word, article, wtype, plural, meaning, example, example_cn):
    clean = word
    if word.startswith("der ") or word.startswith("die ") or word.startswith("das "):
        clean = word[4:]
    ipa = get_ipa(clean, word)
    return {
        "word": word,
        "article": article,
        "type": wtype,
        "ipa": ipa,
        "plural": plural,
        "meaning": meaning,
        "example": example,
        "exampleCn": example_cn
    }

def get_level_a2():
    all_raw_lessons = LESSONS_A2_PART1 + LESSONS_A2_PART2 + LESSONS_A2_PART3
    lessons = []
    for raw in all_raw_lessons:
        words = [make_word(w[0], w[1], w[2], w[3], w[4], w[5], w[6]) for w in raw["words"]]
        lessons.append({
            "id": raw["id"],
            "title": raw["title"],
            "summary": raw["summary"],
            "grammar": raw["grammar"],
            "words": words,
            "quiz": raw["quiz"]
        })
    return {
        "id": "A2",
        "name": "A2 进阶突破通关",
        "goetheLevel": "Goethe-Zertifikat A2",
        "description": "深入掌握过去时、第二虚拟式、从句连词、比较级最高级、双向介词及双元制、职场、医疗、环保与歌德A2真题核心大纲词汇！",
        "lessons": lessons
    }

def main():
    a2_data = get_level_a2()
    total_words = sum(len(l["words"]) for l in a2_data["lessons"])
    print(f"[OK] Level A2 compiled: {len(a2_data['lessons'])} lessons, {total_words} words.")
    out_path = os.path.join(os.path.dirname(__file__), "curriculum_a2.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(a2_data, f, ensure_ascii=False, indent=2)
    print(f"[OK] Saved {out_path}")

if __name__ == "__main__":
    main()
