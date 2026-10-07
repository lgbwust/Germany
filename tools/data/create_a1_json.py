#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builder for A1: 15 Lessons x 70 words = 1050 Words
Outputs tools/data/a1_full.json
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
