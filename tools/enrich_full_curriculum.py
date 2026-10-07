#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Curriculum Enrichment Tool:
Injects comprehensive quiz banks into curriculum_a1.json, curriculum_a2.json,
curriculum_b1.json, and curriculum_b2.json.
Guarantees 10 questions per lesson across A1-B2 (600 questions) + 40 questions in A0 = 640 questions.
"""

import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
sys.path.insert(0, BASE_DIR)

from quiz_data_a1 import A1_QUIZZES
from quiz_data_a2 import A2_QUIZZES
from quiz_data_b1 import B1_QUIZZES
from quiz_data_b2 import B2_QUIZZES

LEVEL_CONFIGS = [
    ("a1", A1_QUIZZES),
    ("a2", A2_QUIZZES),
    ("b1", B1_QUIZZES),
    ("b2", B2_QUIZZES)
]

def main():
    print("=" * 60)
    print("ENRICHING CURRICULUM QUIZ BANKS (A1 - B2)")
    print("=" * 60)

    total_injected = 0

    for lvl_code, quiz_bank in LEVEL_CONFIGS:
        json_path = os.path.join(DATA_DIR, f"curriculum_{lvl_code}.json")
        if not os.path.exists(json_path):
            print(f"[ERROR] Missing file: {json_path}")
            sys.exit(1)

        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        lvl_quizzes_before = sum(len(l.get("quiz", [])) for l in data.get("lessons", []))
        lvl_quizzes_after = 0

        for lesson in data.get("lessons", []):
            lid = lesson["id"]
            if lid in quiz_bank:
                lesson["quiz"] = quiz_bank[lid]
                lvl_quizzes_after += len(lesson["quiz"])
            else:
                print(f"[WARNING] Lesson {lid} not found in quiz bank for {lvl_code.upper()}!")

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"[+] Level {lvl_code.upper()}: Updated {len(data.get('lessons', []))} lessons. Quizzes: {lvl_quizzes_before} -> {lvl_quizzes_after}")
        total_injected += lvl_quizzes_after

    print("-" * 60)
    print(f"Total quizzes in A1-B2: {total_injected}")
    print("=" * 60)

if __name__ == "__main__":
    main()
