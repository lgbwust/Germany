#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Massive Curriculum Builder for DeutschMeister
Builds 15 comprehensive lessons for A1, A2, B1, and B2 (each having 70 words, total 1050 words per level).
Combined with Level A0 (5 lessons, 50 words), total vocabulary across all levels is 4250+ words!
All words include standard IPA, articles, plurals, Chinese meanings, and authentic bilingual examples.
"""

from .ipa_helper import get_ipa
from .level_a0 import get_level_a0

def make_word_entry(word, article, wtype, plural, meaning, example, example_cn):
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
