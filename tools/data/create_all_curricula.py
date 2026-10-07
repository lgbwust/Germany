#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Builder for Goethe German CEFR Levels A1, A2, B1, B2
Generates 15 lessons x 70 words = 1050 words per level.
Total vocabulary across A1-B2: 4200 words (+ A0: 50 words = 4250 words).
Outputs:
  tools/data/curriculum_a1.json
  tools/data/curriculum_a2.json
  tools/data/curriculum_b1.json
  tools/data/curriculum_b2.json
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.ipa_helper import get_ipa

def make_w(word, article, wtype, plural, meaning, example, example_cn):
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
