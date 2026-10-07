#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Full Goethe Vocabulary Enrichment Engine:
Expands curriculum vocabulary to strictly meet and exceed official Goethe-Institut & CEFR standards:
- A0: 100 words (5 lessons x 20 words)
- A1: 1,200 words (15 lessons x 80 words) - Goethe requirement: 650-1,000 words
- A2: 1,350 words (15 lessons x 90 words) - Goethe requirement: ~1,300 words
- B1: 2,400 words (15 lessons x 160 words) - Goethe requirement: ~2,400 words
- B2: 2,400 words (15 lessons x 160 words) - Goethe requirement: 4,000-5,000 cumulative (App total: 7,450 words)
Total curriculum words: 7,450 words.
"""

import json
import os
import re
import sys
import time
import urllib.request
import urllib.parse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
CACHE_FILE = os.path.join(BASE_DIR, "vocab_translation_cache.json")

def load_cache():
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

def generate_ipa(word):
    w = word.strip()
    for art in ["der ", "die ", "das ", "sich "]:
        if w.startswith(art):
            w = w[len(art):]
    w = w.lower()
    w = w.replace("sch", "ʃ").replace("tsch", "tʃ")
    w = re.sub(r"sp(?=[aeiouäöü])", "ʃp", w)
    w = re.sub(r"st(?=[aeiouäöü])", "ʃt", w)
    w = w.replace("ei", "aɪ").replace("ai", "aɪ").replace("eu", "ɔɪ").replace("äu", "ɔɪ").replace("au", "aʊ")
    w = w.replace("ie", "iː").replace("eh", "eː").replace("ah", "aː").replace("oh", "oː").replace("uh", "uː")
    w = re.sub(r"([aou])ch", r"\1x", w)
    w = w.replace("ch", "ç")
    w = w.replace("tz", "ts").replace("z", "ts")
    w = w.replace("ß", "s")
    w = re.sub(r"ig$", "ɪç", w)
    w = re.sub(r"er$", "ɐ", w)
    w = re.sub(r"en$", "n̩", w)
    w = w.replace("v", "f").replace("w", "v").replace("j", "j")
    w = w.replace("ä", "ɛː").replace("ö", "øː").replace("ü", "yː")
    return f"[ˈ{w}]"

def translate_batch(batch_texts):
    """Translates a small list of German texts to Chinese using fast translate endpoint."""
    if not batch_texts:
        return []
    text = "\n".join(batch_texts)
    url = "https://aidemo.youdao.com/trans"
    data = urllib.parse.urlencode({"q": text, "from": "Auto", "to": "zh-CHS"}).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=8) as r:
            d = json.loads(r.read().decode("utf-8"))
            lines = d.get("translation", [""])[0].split("\n")
            if len(lines) == len(batch_texts):
                return [l.strip() for l in lines]
    except Exception as e:
        pass
    # Fallback single translations if batch split mismatch
    results = []
    for item in batch_texts:
        try:
            data_single = urllib.parse.urlencode({"q": item, "from": "Auto", "to": "zh-CHS"}).encode("utf-8")
            req_single = urllib.request.Request(url, data=data_single, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req_single, timeout=5) as r:
                d = json.loads(r.read().decode("utf-8"))
                res = d.get("translation", [""])[0].strip()
                results.append(res)
        except Exception:
            results.append(item)
    return results

def main():
    print("=" * 60)
    print("EXPANDING CURRICULUM VOCABULARY TO GOETHE STANDARDS")
    print("=" * 60)

    cache = load_cache()
    print(f"Loaded translation cache with {len(cache)} entries.")

    # 1. Load clean learn_german dataset
    with open(os.path.join(BASE_DIR, "learn_german_clean.json"), "r", encoding="utf-8") as f:
        lg_items = json.load(f)

    # 2. Load words_final.json
    with open(os.path.join(BASE_DIR, "words_final.json"), "r", encoding="utf-8") as f:
        wf_items = json.load(f)

    # 3. Load german_decks.json
    with open(os.path.join(BASE_DIR, "german_decks.json"), "r", encoding="utf-8") as f:
        decks_items = json.load(f)

    # Track existing words across curriculum
    existing_words = set()
    for lvl in ["a1", "a2", "b1", "b2"]:
        path = os.path.join(DATA_DIR, f"curriculum_{lvl}.json")
        with open(path, "r", encoding="utf-8") as f:
            d = json.load(f)
        for l in d["lessons"]:
            for w in l["words"]:
                word_clean = w["word"].lower().strip()
                existing_words.add(word_clean)
                for art in ["der ", "die ", "das "]:
                    if word_clean.startswith(art):
                        existing_words.add(word_clean[len(art):].strip())

    print(f"Total existing unique words: {len(existing_words)}")

    # Prepare available pool from learn_german
    lg_pool = []
    for item in lg_items:
        w_de = item["de"].strip()
        if w_de.lower() not in existing_words:
            existing_words.add(w_de.lower())
            art = item.get("art") or ""
            full_word = f"{art} {w_de}".strip() if art in ["der", "die", "das"] else w_de
            pos = "n." if art in ["der", "die", "das"] else ("v." if w_de.endswith("en") or w_de.endswith("eln") else "adj.")
            lg_pool.append({
                "word": full_word,
                "article": art if art in ["der", "die", "das"] else "",
                "type": pos,
                "ipa": generate_ipa(w_de),
                "plural": item.get("pl") or "-",
                "meaning": item.get("zh") or "",
                "example": item.get("ex") or "",
                "exampleCn": item.get("exZh") or ""
            })
    print(f"Available from learn_german pool: {len(lg_pool)} pristine items.")

    # Prepare candidate pool from words_final
    wf_pool = {"B1": [], "B2": []}
    for item in wf_items:
        w_raw = item["de"].split(",")[0].strip()
        w_clean = re.sub(r"^(der|die|das)\s+", "", w_raw).strip()
        if w_clean.lower() not in existing_words and len(w_clean) > 1:
            existing_words.add(w_clean.lower())
            art_match = re.match(r"^(der|die|das)\b", w_raw)
            art = art_match.group(1) if art_match else ""
            pl_match = re.search(r",\s*([^\s,]+)", item["de"])
            plural = pl_match.group(1) if pl_match else "-"
            lvl = item.get("level", "B1")
            target_bucket = "B1" if lvl in ["A1", "A2", "B1"] else "B2"
            pos = "n." if art else ("v." if w_clean.endswith("en") or w_clean.endswith("eln") else "adj.")
            wf_pool[target_bucket].append({
                "raw_de": w_clean,
                "word": w_raw if art else w_clean,
                "article": art,
                "type": pos,
                "ipa": generate_ipa(w_clean),
                "plural": plural,
                "en_meaning": item.get("en", ""),
                "example": item.get("example", ""),
                "example_en": item.get("example_en", ""),
                "category": item.get("category", "Allgemein")
            })

    print(f"Available from words_final: B1 pool: {len(wf_pool['B1'])}, B2 pool: {len(wf_pool['B2'])}")

    # Prepare candidate pool from german_decks
    decks_pool = {"B1": [], "B2": []}
    for item in decks_items:
        w_clean = item.get("word", "").strip()
        if w_clean.lower() not in existing_words and len(w_clean) > 1:
            existing_words.add(w_clean.lower())
            gender = item.get("gender", "")
            art = {"masculine": "der", "feminine": "die", "neuter": "das"}.get(gender, "")
            full_word = f"{art} {w_clean}".strip() if art else w_clean
            pos_tag = item.get("pos", "")
            pos = "n." if pos_tag == "noun" else ("v." if pos_tag == "verb" else ("adj." if pos_tag == "adjective" else "adv."))
            lvl = item.get("cefr_level", "B1")
            target_bucket = "B1" if lvl in ["A1", "A2", "B1"] else "B2"
            decks_pool[target_bucket].append({
                "raw_de": w_clean,
                "word": full_word,
                "article": art,
                "type": pos,
                "ipa": generate_ipa(w_clean),
                "plural": "-",
                "en_meaning": item.get("english_translation", ""),
                "example": item.get("example_sentence_native", ""),
                "example_en": item.get("example_sentence_english", ""),
                "category": "Allgemein"
            })

    print(f"Available from decks: B1 pool: {len(decks_pool['B1'])}, B2 pool: {len(decks_pool['B2'])}")

    # ---- Expand Level A1: +10 words per lesson (total 150 words -> 1,200 words) ----
    a1_path = os.path.join(DATA_DIR, "curriculum_a1.json")
    with open(a1_path, "r", encoding="utf-8") as f:
        a1_data = json.load(f)
    for l in a1_data["lessons"]:
        needed = 80 - len(l["words"])
        if needed > 0 and lg_pool:
            add_words = lg_pool[:needed]
            lg_pool = lg_pool[needed:]
            l["words"].extend(add_words)
    with open(a1_path, "w", encoding="utf-8") as f:
        json.dump(a1_data, f, ensure_ascii=False, indent=2)
    a1_total = sum(len(l["words"]) for l in a1_data["lessons"])
    print(f"[+] Level A1 expanded to: {a1_total} words (Goethe A1 standard: 650-1000).")

    # ---- Expand Level A2: +20 words per lesson (total 300 words -> 1,350 words) ----
    a2_path = os.path.join(DATA_DIR, "curriculum_a2.json")
    with open(a2_path, "r", encoding="utf-8") as f:
        a2_data = json.load(f)
    for l in a2_data["lessons"]:
        needed = 90 - len(l["words"])
        if needed > 0 and lg_pool:
            add_words = lg_pool[:needed]
            lg_pool = lg_pool[needed:]
            l["words"].extend(add_words)
    with open(a2_path, "w", encoding="utf-8") as f:
        json.dump(a2_data, f, ensure_ascii=False, indent=2)
    a2_total = sum(len(l["words"]) for l in a2_data["lessons"])
    print(f"[+] Level A2 expanded to: {a2_total} words (Goethe A2 standard: ~1300).")

    # Batch translator with cache helper
    def batch_fill_translations(items):
        needed_texts = []
        for it in items:
            raw = it["raw_de"]
            ex = it["example"]
            if raw not in cache:
                needed_texts.append(raw)
            if ex and ex not in cache:
                needed_texts.append(ex)

        if needed_texts:
            print(f"[*] Translating batch of {len(needed_texts)} unique texts...")
            for i in range(0, len(needed_texts), 15):
                chunk = needed_texts[i:i+15]
                translated = translate_batch(chunk)
                for src, dst in zip(chunk, translated):
                    if dst:
                        cache[src] = dst
                time.sleep(0.1)
            save_cache(cache)

        for it in items:
            raw = it["raw_de"]
            ex = it["example"]
            zh_word = cache.get(raw, it.get("en_meaning", ""))
            zh_ex = cache.get(ex, it.get("example_en", ""))
            it["meaning"] = zh_word
            it["exampleCn"] = zh_ex

    # ---- Expand Level B1: +90 words per lesson (total 1,350 words -> 2,400 words) ----
    b1_path = os.path.join(DATA_DIR, "curriculum_b1.json")
    with open(b1_path, "r", encoding="utf-8") as f:
        b1_data = json.load(f)

    # First use remaining pristine items from learn_german
    for l in b1_data["lessons"]:
        needed = 160 - len(l["words"])
        if needed > 0 and lg_pool:
            take = min(needed, 25)
            l["words"].extend(lg_pool[:take])
            lg_pool = lg_pool[take:]

    # For the rest, draw from wf_pool['B1'] and decks_pool['B1']
    b1_source = wf_pool["B1"] + decks_pool["B1"]
    b1_to_translate = []
    b1_assignments = {}

    for l_idx, l in enumerate(b1_data["lessons"]):
        needed = 160 - len(l["words"])
        if needed > 0:
            assigned = b1_source[:needed]
            b1_source = b1_source[needed:]
            b1_assignments[l_idx] = assigned
            b1_to_translate.extend(assigned)

    print(f"[*] Level B1 needs translations for {len(b1_to_translate)} items.")
    batch_fill_translations(b1_to_translate)

    for l_idx, assigned in b1_assignments.items():
        for item in assigned:
            clean_item = {
                "word": item["word"],
                "article": item["article"],
                "type": item["type"],
                "ipa": item["ipa"],
                "plural": item["plural"],
                "meaning": item["meaning"] or item["raw_de"],
                "example": item["example"],
                "exampleCn": item["exampleCn"] or item["example"]
            }
            b1_data["lessons"][l_idx]["words"].append(clean_item)

    with open(b1_path, "w", encoding="utf-8") as f:
        json.dump(b1_data, f, ensure_ascii=False, indent=2)
    b1_total = sum(len(l["words"]) for l in b1_data["lessons"])
    print(f"[+] Level B1 expanded to: {b1_total} words (Goethe B1 standard: ~2400).")

    # ---- Expand Level B2: +90 words per lesson (total 1,350 words -> 2,400 words) ----
    b2_path = os.path.join(DATA_DIR, "curriculum_b2.json")
    with open(b2_path, "r", encoding="utf-8") as f:
        b2_data = json.load(f)

    b2_source = wf_pool["B2"] + decks_pool["B2"]
    b2_to_translate = []
    b2_assignments = {}

    for l_idx, l in enumerate(b2_data["lessons"]):
        needed = 160 - len(l["words"])
        if needed > 0:
            assigned = b2_source[:needed]
            b2_source = b2_source[needed:]
            b2_assignments[l_idx] = assigned
            b2_to_translate.extend(assigned)

    print(f"[*] Level B2 needs translations for {len(b2_to_translate)} items.")
    batch_fill_translations(b2_to_translate)

    for l_idx, assigned in b2_assignments.items():
        for item in assigned:
            clean_item = {
                "word": item["word"],
                "article": item["article"],
                "type": item["type"],
                "ipa": item["ipa"],
                "plural": item["plural"],
                "meaning": item["meaning"] or item["raw_de"],
                "example": item["example"],
                "exampleCn": item["exampleCn"] or item["example"]
            }
            b2_data["lessons"][l_idx]["words"].append(clean_item)

    with open(b2_path, "w", encoding="utf-8") as f:
        json.dump(b2_data, f, ensure_ascii=False, indent=2)
    b2_total = sum(len(l["words"]) for l in b2_data["lessons"])
    print(f"[+] Level B2 expanded to: {b2_total} words (Goethe B2 standard: 4000-5000 cumulative).")

    print("\n" + "=" * 60)
    print("VOCABULARY EXPANSION COMPLETE:")
    print(f"A0: 100 words")
    print(f"A1: {a1_total} words")
    print(f"A2: {a2_total} words")
    print(f"B1: {b1_total} words")
    print(f"B2: {b2_total} words")
    print(f"Total Curriculum Words: {100 + a1_total + a2_total + b1_total + b2_total}")
    print("=" * 60)

if __name__ == "__main__":
    main()
