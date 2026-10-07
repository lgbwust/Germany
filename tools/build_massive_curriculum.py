#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DeutschMeister Massive Curriculum Generator (CEFR A0 - B2)
Generates 65 lessons, 4250+ vocabulary words (1050+ words per level for A1, A2, B1, B2).
Every single word contains authentic IPA, German articles (der/die/das), plurals,
Chinese definitions, and realistic Goethe exam examples with translations.
"""

import json
import os
import sys

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
