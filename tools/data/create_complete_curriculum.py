#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Full Goethe German Curriculum Dataset Generator (CEFR A0-B2)
Generates 65 Lessons, 4250+ Vocabulary Items (1050+ words per level for A1, A2, B1, B2).
Each word contains authentic German spelling, article (der/die/das), word type,
IPA phonetic notation, plural/conjugation forms, Chinese definition, and authentic German examples with translations.
"""

import json
import os
import sys

# Ensure import works
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.ipa_helper import get_ipa
from data.level_a0 import get_level_a0

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
