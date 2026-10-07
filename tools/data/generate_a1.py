#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator for Level A1: 15 Lessons x 70 words = 1050 Words
Outputs tools/data/level_a1.json
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.ipa_helper import get_ipa

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

def format_lesson(les_id, title, summary, g_title, g_sections, quiz, raw_words):
    words = [make_word(w[0], w[1], w[2], w[3], w[4], w[5], w[6]) for w in raw_words]
    return {
        "id": les_id,
        "title": title,
        "summary": summary,
        "grammar": {
            "title": g_title,
            "sections": g_sections
        },
        "words": words,
        "quiz": quiz
    }
