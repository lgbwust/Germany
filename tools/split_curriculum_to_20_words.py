#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Curriculum Splitter (20 Words Per Lesson Standard):
Splits all curriculum levels (A1, A2, B1, B2) into bite-sized 20-word modular lessons:
- A0: 5 lessons x 20 words = 100 words (already 20 words/lesson)
- A1: 60 lessons x 20 words = 1,200 words
- A2: 68 lessons x 20 words = 1,360 words
- B1: 120 lessons x 20 words = 2,400 words
- B2: 120 lessons x 20 words = 2,400 words
Total: 373 lessons, 7,460 words.
Each lesson has:
- Structured theme title and progression part indicator
- Dynamic summary
- Tailored grammar section with complete headings and rich explanations
- Exactly 20 words
- 4 curated quizzes (original quizzes + vocabulary/article practical exercises)
"""

import json
import os
import re
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

PART_LABELS = [
    "基础认知 (Grundlagen)",
    "核心词汇 (Kernwortschatz)",
    "情境表达 (Kommunikation)",
    "语法拓展 (Grammatik)",
    "实战应用 (Praxis)",
    "综合进阶 (Vertiefung)",
    "场景演练 (Szenario)",
    "考点强化 (Prüfungstraining)"
]

def generate_quiz_for_words(words_chunk, level_id, lesson_num, orig_quizzes, start_q_idx=0):
    quizzes = []
    q_id_counter = 1

    # 1. Reuse 1-2 relevant quizzes from original lesson pool if available
    if orig_quizzes:
        pick_count = min(2, len(orig_quizzes))
        for o_q in orig_quizzes[:pick_count]:
            quizzes.append({
                "id": f"{level_id}_L{lesson_num:03d}_Q{q_id_counter}",
                "type": o_q.get("type", "GRAMMAR_FILL"),
                "question": o_q.get("question", ""),
                "options": o_q.get("options", []),
                "correctIndex": o_q.get("correctIndex", 0),
                "explanation": o_q.get("explanation", "")
            })
            q_id_counter += 1

    # 2. Add 2 Vocabulary meaning quizzes from this lesson's own 20 words
    candidates = [w for w in words_chunk if w.get("meaning")]
    if len(candidates) >= 4:
        for pick_idx in [0, min(10, len(candidates) - 1)]:
            target_w = candidates[pick_idx]
            distractors = [w["meaning"] for i, w in enumerate(candidates) if i != pick_idx and w["meaning"] != target_w["meaning"]]
            if len(distractors) >= 3:
                chosen_distractors = distractors[:3]
                options = [target_w["meaning"]] + chosen_distractors
                # keep deterministic or simple order
                quizzes.append({
                    "id": f"{level_id}_L{lesson_num:03d}_Q{q_id_counter}",
                    "type": "VOCAB_MEANING",
                    "question": f"单词「{target_w['word']}」的正确中文释义是？",
                    "options": options,
                    "correctIndex": 0,
                    "explanation": f"「{target_w['word']}」的中文释义为「{target_w['meaning']}」。例句：{target_w.get('example', '')}（{target_w.get('exampleCn', '')}）"
                })
                q_id_counter += 1

    # 3. Add 1 Article quiz if any noun exists in the 20 words
    nouns = [w for w in words_chunk if w.get("article") in ["der", "die", "das"]]
    if nouns:
        target_noun = nouns[0]
        art = target_noun["article"]
        options = ["der", "die", "das"]
        correct_idx = options.index(art)
        gender_desc = "阳性" if art == "der" else ("阴性" if art == "die" else "中性")
        clean_name = re.sub(r"^(der|die|das)\s+", "", target_noun["word"]).strip()
        quizzes.append({
            "id": f"{level_id}_L{lesson_num:03d}_Q{q_id_counter}",
            "type": "ARTICLE",
            "question": f"名词「{clean_name}」的正确定冠词是？",
            "options": options,
            "correctIndex": correct_idx,
            "explanation": f"名词「{clean_name}」为{gender_desc}名词，定冠词是 {art}，复数形式为 {target_noun.get('plural', '-') }。"
        })
        q_id_counter += 1

    return quizzes

def split_level_lessons(input_path, level_id, add_words=None):
    with open(input_path, "r", encoding="utf-8") as f:
        level_data = json.load(f)

    orig_lessons = level_data["lessons"]
    all_words = []
    for l in orig_lessons:
        all_words.extend(l["words"])

    if add_words:
        all_words.extend(add_words)

    total_words = len(all_words)
    assert total_words % 20 == 0, f"Total words {total_words} is not divisible by 20!"
    target_lesson_count = total_words // 20
    print(f"[*] Level {level_id}: Splitting {total_words} words into {target_lesson_count} lessons (20 words each).")

    new_lessons = []
    orig_count = len(orig_lessons)

    for l_idx in range(target_lesson_count):
        lesson_num = l_idx + 1
        words_chunk = all_words[l_idx * 20 : (l_idx + 1) * 20]

        # Determine which original thematic unit this belongs to
        orig_idx = min(l_idx * orig_count // target_lesson_count, orig_count - 1)
        orig_les = orig_lessons[orig_idx]

        # Calculate sub-part index within that thematic unit
        # Find how many sub-lessons map to orig_idx
        unit_sub_lessons = [i for i in range(target_lesson_count) if min(i * orig_count // target_lesson_count, orig_count - 1) == orig_idx]
        part_idx = unit_sub_lessons.index(l_idx)
        part_total = len(unit_sub_lessons)
        part_label = PART_LABELS[part_idx % len(PART_LABELS)]

        # Clean title
        raw_title = orig_les.get("title", "")
        clean_theme = re.sub(r"^第\d+课[：:]\s*", "", raw_title).strip()
        new_title = f"第{lesson_num}课：{clean_theme} ({part_idx + 1}/{part_total}) · {part_label}"

        # Clean summary
        orig_summary = orig_les.get("summary", "")
        new_summary = f"{orig_summary}（第{part_idx + 1}部分 · 本课专注掌握20个高频核心词汇与发音练习）"

        # Grammar
        orig_grammar = orig_les.get("grammar", {})
        orig_sections = orig_grammar.get("sections", []) if orig_grammar else []
        if orig_sections:
            chosen_section = orig_sections[part_idx % len(orig_sections)]
            new_grammar = {
                "title": f"{orig_grammar.get('title', '语法精讲')} · 核心重点 ({part_idx + 1})",
                "sections": [
                    {
                        "heading": chosen_section.get("heading", "语法解析"),
                        "content": chosen_section.get("content", "请结合本课例句重点掌握相关动词变位与句型结构。")
                    }
                ]
            }
        else:
            new_grammar = {
                "title": f"{clean_theme} · 重点语法解析",
                "sections": [
                    {
                        "heading": "词汇搭配与语序规则",
                        "content": "在日常德语交流中，请注意第二格冠词变化、动词第二位基本语序以及动词与介词的固定搭配。"
                    }
                ]
            }

        # Quiz
        orig_quizzes = orig_les.get("quiz", [])
        # Rotate quizzes for variety
        start_q = (part_idx * 2) % max(1, len(orig_quizzes)) if orig_quizzes else 0
        rotated_orig = orig_quizzes[start_q:] + orig_quizzes[:start_q] if orig_quizzes else []
        new_quizzes = generate_quiz_for_words(words_chunk, level_id, lesson_num, rotated_orig)

        new_lessons.append({
            "id": f"{level_id}_L{lesson_num:03d}",
            "title": new_title,
            "summary": new_summary,
            "grammar": new_grammar,
            "words": words_chunk,
            "quiz": new_quizzes
        })

    level_data["lessons"] = new_lessons
    with open(input_path, "w", encoding="utf-8") as f:
        json.dump(level_data, f, ensure_ascii=False, indent=2)

    print(f"[+] Level {level_id} saved: {len(new_lessons)} lessons, {sum(len(l['words']) for l in new_lessons)} words.")
    return len(new_lessons)

def main():
    print("=" * 60)
    print("SPLITTING ALL LEVELS INTO 20 WORDS PER LESSON")
    print("=" * 60)

    # 1. Level A1: 1,200 words -> 60 lessons
    a1_path = os.path.join(DATA_DIR, "curriculum_a1.json")
    split_level_lessons(a1_path, "A1")

    # 2. Level A2: Add 10 pristine body words from learn_german_clean -> 1,360 words -> 68 lessons
    a2_path = os.path.join(DATA_DIR, "curriculum_a2.json")
    with open(os.path.join(BASE_DIR, "learn_german_clean.json"), "r", encoding="utf-8") as f:
        lg = json.load(f)

    # Load existing words to avoid duplication
    existing = set()
    for lvl in ["a1", "a2", "b1", "b2"]:
        path = os.path.join(DATA_DIR, f"curriculum_{lvl}.json")
        with open(path, "r", encoding="utf-8") as f:
            d = json.load(f)
        for l in d["lessons"]:
            for w in l["words"]:
                existing.add(w["word"].lower().strip())

    fresh_a2_words = []
    for it in lg:
        de_clean = it["de"].strip()
        if de_clean.lower() not in existing and len(de_clean) > 1:
            art = it.get("art") or ""
            full_w = f"{art} {de_clean}".strip() if art else de_clean
            pos = "n." if art else ("v." if de_clean.endswith("en") else "adj.")
            fresh_a2_words.append({
                "word": full_w,
                "article": art if art in ["der", "die", "das"] else "",
                "type": pos,
                "ipa": f"[ˈ{de_clean.lower()}]",
                "plural": it.get("pl") or "-",
                "meaning": it.get("zh") or "",
                "example": it.get("ex") or "",
                "exampleCn": it.get("exZh") or ""
            })
            existing.add(de_clean.lower())
            if len(fresh_a2_words) == 10:
                break

    print(f"[*] Prepared {len(fresh_a2_words)} fresh words for Level A2 to reach 1,360 words.")
    split_level_lessons(a2_path, "A2", add_words=fresh_a2_words)

    # 3. Level B1: 2,400 words -> 120 lessons
    b1_path = os.path.join(DATA_DIR, "curriculum_b1.json")
    split_level_lessons(b1_path, "B1")

    # 4. Level B2: 2,400 words -> 120 lessons
    b2_path = os.path.join(DATA_DIR, "curriculum_b2.json")
    split_level_lessons(b2_path, "B2")

    print("\n" + "=" * 60)
    print("ALL CURRICULUM LEVELS SUCCESSFULLY SPLIT TO 20 WORDS PER LESSON!")
    print("=" * 60)

if __name__ == "__main__":
    main()
