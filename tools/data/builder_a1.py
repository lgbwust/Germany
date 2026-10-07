#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builder for Level A1: 15 Lessons x 70 words = 1050 Words.
Merges a1_part1, a1_part2, a1_part3 and generates curriculum_a1.json.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.ipa_helper import get_ipa
from data.a1_part1 import LESSONS_PART1
from data.a1_part2 import LESSONS_PART2
from data.a1_part3 import LESSONS_PART3

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

def get_level_a1():
    all_raw_lessons = LESSONS_PART1 + LESSONS_PART2 + LESSONS_PART3
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
        "id": "A1",
        "name": "A1 基础入门通关",
        "goetheLevel": "Start Deutsch 1 (A1)",
        "description": "全面掌握日常生活、家庭、超市就餐、出行、职业健康与考前冲刺四大题型高频核心词汇与核心语法！",
        "lessons": lessons
    }

def main():
    a1_data = get_level_a1()
    total_words = sum(len(l["words"]) for l in a1_data["lessons"])
    print(f"[OK] Level A1 compiled: {len(a1_data['lessons'])} lessons, {total_words} words.")
    out_path = os.path.join(os.path.dirname(__file__), "curriculum_a1.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(a1_data, f, ensure_ascii=False, indent=2)
    print(f"[OK] Saved {out_path}")

if __name__ == "__main__":
    main()
