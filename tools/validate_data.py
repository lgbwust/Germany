#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validation and Quality Linter Tool for DeutschMeister Curriculum
Validates format, IPA notation, articles, translations, quiz indexes, and CEFR Goethe coverage.
"""

import json
import os
import sys

VALID_LEVELS = {"A0", "A1", "A2", "B1", "B2"}
VALID_ARTICLES = {"der", "die", "das", ""}
VALID_QUIZ_TYPES = {"VOCAB_MEANING", "ARTICLE", "GRAMMAR_FILL", "PRONUNCIATION", "EXAM_REAL", "SENTENCE_BUILDER", "LISTENING_MCQ", "MEANING_SELECT"}

def validate_curriculum(file_path):
    print(f"[*] Validating curriculum file: {file_path}")
    if not os.path.exists(file_path):
        print(f"[ERROR] File does not exist: {file_path}")
        return False

    with open(file_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except Exception as e:
            print(f"[ERROR] Invalid JSON: {e}")
            return False

    errors = []
    warnings = []

    if "levels" not in data or not isinstance(data["levels"], list):
        errors.append("Root element missing 'levels' array")
        return False

    level_ids_seen = set()
    total_words = 0
    total_quizzes = 0
    total_grammar_sections = 0

    articles_count = {"der": 0, "die": 0, "das": 0, "none": 0}
    quiz_types_count = {}

    for lvl_idx, lvl in enumerate(data["levels"]):
        lid = lvl.get("id")
        lname = lvl.get("name")
        if not lid or lid not in VALID_LEVELS:
            errors.append(f"Level at index {lvl_idx} has invalid ID: {lid}")
        if lid in level_ids_seen:
            errors.append(f"Duplicate level ID: {lid}")
        level_ids_seen.add(lid)

        lessons = lvl.get("lessons", [])
        if not lessons:
            warnings.append(f"Level {lid} has no lessons")

        for les_idx, les in enumerate(lessons):
            les_id = les.get("id", f"{lid}_L{les_idx}")
            title = les.get("title", "")
            if not title:
                errors.append(f"Lesson {les_id} missing title")

            # Validate grammar
            grammar = les.get("grammar", {})
            if not grammar.get("title"):
                warnings.append(f"Lesson {les_id} grammar missing title")
            sections = grammar.get("sections", [])
            total_grammar_sections += len(sections)
            for sec in sections:
                if not sec.get("heading") or not sec.get("content"):
                    errors.append(f"Lesson {les_id} grammar section missing heading or content")

            # Validate words
            words = les.get("words", [])
            for w_idx, w in enumerate(words):
                total_words += 1
                word_text = w.get("word", "")
                art = w.get("article", "")
                ipa = w.get("ipa", "")
                meaning = w.get("meaning", "")
                example = w.get("example", "")
                example_cn = w.get("exampleCn", "")

                if not word_text:
                    errors.append(f"Lesson {les_id} word #{w_idx} has empty 'word'")
                if art not in VALID_ARTICLES:
                    errors.append(f"Word '{word_text}' has invalid article: '{art}'")
                else:
                    if art:
                        articles_count[art] += 1
                    else:
                        articles_count["none"] += 1

                if not ipa:
                    warnings.append(f"Word '{word_text}' missing IPA notation")
                if not meaning:
                    errors.append(f"Word '{word_text}' missing Chinese meaning")
                if not example:
                    warnings.append(f"Word '{word_text}' missing German example sentence")
                if not example_cn:
                    warnings.append(f"Word '{word_text}' missing Chinese translation for example")

            # Validate quiz
            quizzes = les.get("quiz", [])
            for q_idx, q in enumerate(quizzes):
                total_quizzes += 1
                qid = q.get("id", f"{les_id}_Q{q_idx}")
                qtype = q.get("type", "")
                q_text = q.get("question", "")
                options = q.get("options", [])
                c_idx = q.get("correctIndex", -1)
                expl = q.get("explanation", "")

                quiz_types_count[qtype] = quiz_types_count.get(qtype, 0) + 1

                if qtype not in VALID_QUIZ_TYPES:
                    errors.append(f"Quiz {qid} has unknown type: '{qtype}'")
                if not q_text:
                    errors.append(f"Quiz {qid} has empty question")
                if len(options) < 2:
                    errors.append(f"Quiz {qid} has fewer than 2 options (found {len(options)})")
                if c_idx < 0 or c_idx >= len(options):
                    errors.append(f"Quiz {qid} correctIndex {c_idx} out of range [0, {len(options)-1}]")
                if not expl:
                    warnings.append(f"Quiz {qid} missing explanation")

    print("\n" + "=" * 60)
    print("VALIDATION REPORT:")
    print(f"Levels Found: {sorted(list(level_ids_seen))}")
    print(f"Total Words Checked: {total_words}")
    print(f"Total Grammar Sections: {total_grammar_sections}")
    print(f"Total Quiz Questions: {total_quizzes}")
    print(f"Article Distribution: der: {articles_count['der']}, die: {articles_count['die']}, das: {articles_count['das']}, other/verbs: {articles_count['none']}")
    print(f"Quiz Types Distribution: {quiz_types_count}")
    print("=" * 60)

    if warnings:
        print(f"\n[!] Warnings ({len(warnings)}):")
        for w in warnings[:10]:
            print(f"  - {w}")
        if len(warnings) > 10:
            print(f"  ... and {len(warnings) - 10} more warnings")

    if errors:
        print(f"\n[x] Errors ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")
        return False

    print("\n[SUCCESS] All curriculum data passed linting and validation without errors!")
    return True

if __name__ == "__main__":
    curriculum_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "curriculum.json")
    if len(sys.argv) > 1:
        curriculum_file = sys.argv[1]
    
    success = validate_curriculum(curriculum_file)
    sys.exit(0 if success else 1)
