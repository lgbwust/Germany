#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Helper to format and assemble curriculum data with authentic IPA
"""
import os
import json
from .ipa_helper import get_ipa

def build_lesson(les_id, title, summary, grammar_title, grammar_sections, quiz_items, word_tuples):
    words = []
    for item in word_tuples:
        # item: (word, article, type, plural, meaning, example, exampleCn)
        word, article, wtype, plural, meaning, example, example_cn = item
        clean = word
        if word.startswith("der ") or word.startswith("die ") or word.startswith("das "):
            clean = word[4:]
        ipa = get_ipa(clean, word)
        words.append({
            "word": word,
            "article": article,
            "type": wtype,
            "ipa": ipa,
            "plural": plural,
            "meaning": meaning,
            "example": example,
            "exampleCn": example_cn
        })
    
    return {
        "id": les_id,
        "title": title,
        "summary": summary,
        "grammar": {
            "title": grammar_title,
            "sections": grammar_sections
        },
        "words": words,
        "quiz": quiz_items
    }
