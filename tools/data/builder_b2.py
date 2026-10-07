#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builder for Level B2: 15 Lessons x 70 words = 1050 Words.
Merges b2_part1, b2_part2, b2_part3 and generates curriculum_b2.json.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.ipa_helper import get_ipa
from data.b2_part1 import LESSONS_B2_PART1
from data.b2_part2 import LESSONS_B2_PART2
from data.b2_part3 import LESSONS_B2_PART3

def make_word(word, article, wtype, plural, meaning, example, example_cn):
    clean = word
    if word.startswith("der ") or word.startswith("die ") or word.startswith("das "):
        clean = word[4:]
    ipa = get_ipa(clean, word)
    art = article if article in ("der", "die", "das") else ""
    return {
        "word": word,
        "article": art,
        "type": wtype,
        "ipa": ipa,
        "plural": plural,
        "meaning": meaning,
        "example": example,
        "exampleCn": example_cn
    }

def get_level_b2():
    all_raw_lessons = LESSONS_B2_PART1 + LESSONS_B2_PART2 + LESSONS_B2_PART3
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
        "id": "B2",
        "name": "B2 高阶流利突破",
        "goetheLevel": "Goethe-Zertifikat B2 / TestDaF",
        "description": "全面精通名词化风格、扩展分词定语、虚拟式推测与外交论证、被动态替代结构、第二格学术介词、主观情态动词、高阶功能动词及德福/歌德B2学术图表与议论文通关核心词汇！",
        "lessons": lessons
    }

def main():
    b2_data = get_level_b2()
    total_words = sum(len(l["words"]) for l in b2_data["lessons"])
    print(f"[OK] Level B2 compiled: {len(b2_data['lessons'])} lessons, {total_words} words.")
    for i, l in enumerate(b2_data['lessons']):
        print(f"  Lesson {i+1}: {l['id']} - {len(l['words'])} words - {l['title']}")
    
    out_path = os.path.join(os.path.dirname(__file__), "curriculum_b2.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(b2_data, f, ensure_ascii=False, indent=2)
    print(f"[OK] Saved {out_path} ({os.path.getsize(out_path):,} bytes)")

if __name__ == "__main__":
    main()
