#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builder for Level B1: 15 Lessons x 70 words = 1050 Words.
Merges b1_part1, b1_part2, b1_part3 and generates curriculum_b1.json.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.ipa_helper import get_ipa
from data.b1_part1 import LESSONS_B1_PART1
from data.b1_part2 import LESSONS_B1_PART2
from data.b1_part3 import LESSONS_B1_PART3

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

def get_level_b1():
    all_raw_lessons = LESSONS_B1_PART1 + LESSONS_B1_PART2 + LESSONS_B1_PART3
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
        "id": "B1",
        "name": "B1 中级独立运用",
        "goetheLevel": "Goethe-Zertifikat B1",
        "description": "系统精通被动态、关系从句全格位、第一第二分词、间接引语、目的结果连词及数字化、职场4.0、环保转型、德语区历史国情与歌德B1高分核心词汇！",
        "lessons": lessons
    }

def main():
    b1_data = get_level_b1()
    total_words = sum(len(l["words"]) for l in b1_data["lessons"])
    print(f"[OK] Level B1 compiled: {len(b1_data['lessons'])} lessons, {total_words} words.")
    for i, l in enumerate(b1_data['lessons']):
        print(f"  Lesson {i+1}: {l['id']} - {len(l['words'])} words - {l['title']}")
    
    out_path = os.path.join(os.path.dirname(__file__), "curriculum_b1.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(b1_data, f, ensure_ascii=False, indent=2)
    print(f"[OK] Saved {out_path} ({os.path.getsize(out_path):,} bytes)")

if __name__ == "__main__":
    main()
