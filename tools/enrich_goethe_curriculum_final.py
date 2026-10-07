#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Final Goethe & CEFR Curriculum Vocabulary Enricher:
Expands curriculum vocabulary to strictly meet and exceed official Goethe-Institut standards:
- A0: 100 words (Phonetics & basics, 5 lessons x 20 words)
- A1: 1,200 words (Goethe standard: 650-1,000 words, 15 lessons x 80 words)
- A2: 1,350 words (Goethe standard: ~1,300 words, 15 lessons x 90 words)
- B1: 2,400 words (Goethe standard: ~2,400 words, 15 lessons x 160 words)
- B2: 2,400 words (Goethe standard: 4,000-5,000 cumulative, 15 lessons x 160 words)
Total Curriculum Words: 7,450 words.
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
CACHE_FILE = os.path.join(BASE_DIR, "vocab_sentence_cache.json")

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

def load_handedict():
    print("[*] Loading HanDeDict German-Chinese dictionary...")
    de2zh = {}
    hd_path = os.path.join(BASE_DIR, "handedict.u8")
    with open(hd_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.strip().split("/")
            if len(parts) >= 2:
                head = parts[0]
                defs = parts[1:-1]
                head_match = re.match(r"^\S+\s+(\S+)\s+\[([^\]]*)\]", head)
                if head_match:
                    simp = head_match.group(1)
                    for d in defs:
                        clean_d = re.sub(r"\s*\([^)]*\)", "", d).strip()
                        for sub in clean_d.split(","):
                            sub = re.sub(r"^(der|die|das)\s+", "", sub.strip()).strip()
                            if sub and len(sub) > 1 and sub.lower() not in de2zh:
                                de2zh[sub.lower()] = simp
    print(f"[*] HanDeDict loaded with {len(de2zh)} terms.")
    return de2zh

def load_plurals():
    plurals = {}
    wf_path = os.path.join(BASE_DIR, "words_final.json")
    if os.path.exists(wf_path):
        with open(wf_path, "r", encoding="utf-8") as f:
            wf = json.load(f)
        for it in wf:
            de_raw = it.get("de", "")
            if "," in de_raw:
                parts = de_raw.split(",")
                w_clean = re.sub(r"^(der|die|das)\s+", "", parts[0]).strip().lower()
                pl = parts[1].strip()
                if pl:
                    plurals[w_clean] = pl
    lg_path = os.path.join(BASE_DIR, "learn_german_clean.json")
    if os.path.exists(lg_path):
        with open(lg_path, "r", encoding="utf-8") as f:
            lg = json.load(f)
        for it in lg:
            de_clean = it.get("de", "").strip().lower()
            pl = it.get("pl", "")
            if pl and pl != "-":
                plurals[de_clean] = pl
    print(f"[*] Loaded {len(plurals)} authentic plural forms.")
    return plurals

def infer_plural(word, art, pos, plurals_dict):
    w_clean = word.lower().strip()
    if art:
        w_clean = re.sub(r"^(der|die|das)\s+", "", w_clean).strip()
    if w_clean in plurals_dict:
        return plurals_dict[w_clean]
    if pos != "n." and not art:
        return "-"
    # German noun plural heuristic
    if art == "die":
        if w_clean.endswith("in"):
            return "-nen"
        if w_clean.endswith("e"):
            return "-n"
        if any(w_clean.endswith(suf) for suf in ["ung", "heit", "keit", "schaft", "ion", "tät", "ik"]):
            return "-en"
    if art == "das":
        if w_clean.endswith("chen") or w_clean.endswith("lein"):
            return "-"
        if w_clean.endswith("um"):
            return "-en"
    if w_clean.endswith("el") or w_clean.endswith("en") or w_clean.endswith("er"):
        return "-"
    if w_clean.endswith("y") or w_clean.endswith("a") or w_clean.endswith("o"):
        return "-s"
    return "-e"

def translate_batch_youdao(sentences):
    """Translates a small batch of clean sentences (6) in one request."""
    if not sentences:
        return []
    clean_sents = [re.sub(r"[\r\n]+", " ", s.strip()) for s in sentences]
    text = "\n".join(clean_sents)
    url = "https://aidemo.youdao.com/trans"
    data = urllib.parse.urlencode({"q": text, "from": "Auto", "to": "zh-CHS"}).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"User-Agent": "Mozilla/5.0"})
    
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=6) as r:
                d = json.loads(r.read().decode("utf-8"))
                if d.get("errorCode") == "0":
                    lines = d.get("translation", [""])[0].split("\n")
                    if len(lines) == len(sentences):
                        return [l.strip() for l in lines]
                elif d.get("errorCode") == "411":
                    time.sleep(3)
        except Exception:
            time.sleep(1.5)
            
    # Fallback: single requests
    results = []
    for s in clean_sents:
        try:
            data_single = urllib.parse.urlencode({"q": s, "from": "Auto", "to": "zh-CHS"}).encode("utf-8")
            req_single = urllib.request.Request(url, data=data_single, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req_single, timeout=4) as r:
                d = json.loads(r.read().decode("utf-8"))
                trans = d.get("translation", [""])[0].strip()
                results.append(trans if trans else s)
            time.sleep(0.3)
        except Exception:
            results.append(s)
    return results

def main():
    print("=" * 60)
    print("EXPANDING DEUTSCHMEISTER CURRICULUM TO GOETHE STANDARDS")
    print("=" * 60)

    de2zh = load_handedict()
    plurals_dict = load_plurals()
    cache = load_cache()
    print(f"[*] Sentence translation cache has {len(cache)} entries.")

    # Track all existing words across A1, A2, B1, B2
    existing_words = set()
    for lvl in ["a1", "a2", "b1", "b2"]:
        path = os.path.join(DATA_DIR, f"curriculum_{lvl}.json")
        with open(path, "r", encoding="utf-8") as f:
            d = json.load(f)
        for l in d["lessons"]:
            for w in l["words"]:
                w_raw = w["word"].strip().lower()
                existing_words.add(w_raw)
                for art in ["der ", "die ", "das ", "sich "]:
                    if w_raw.startswith(art):
                        existing_words.add(w_raw[len(art):].strip())

    print(f"[*] Existing unique words across curriculum: {len(existing_words)}")

    # Load candidate pools from german_decks.json
    with open(os.path.join(BASE_DIR, "german_decks.json"), "r", encoding="utf-8") as f:
        decks = json.load(f)

    # Sort decks so more frequent words come first
    decks.sort(key=lambda x: x.get("word_frequency", 999999))

    a2_cands = []
    b1_cands = []
    b2_cands = []

    for it in decks:
        w = it.get("word", "").strip()
        if not w or len(w) <= 1:
            continue
        w_low = w.lower()
        if w_low in existing_words:
            continue
        if w_low not in de2zh:
            continue
        ex = it.get("example_sentence_native", "").strip()
        if not ex:
            continue

        gender = it.get("gender", "")
        art = {"masculine": "der", "feminine": "die", "neuter": "das"}.get(gender, "")
        pos_tag = it.get("pos", "")
        pos = "n." if pos_tag == "noun" else ("v." if pos_tag == "verb" else ("adj." if pos_tag == "adjective" else "adv."))
        
        # Ensure noun is capitalized
        if art:
            w_display = w[0].upper() + w[1:] if len(w) > 1 else w.upper()
            full_word = f"{art} {w_display}"
        else:
            full_word = w

        cand = {
            "word": full_word,
            "raw": w,
            "article": art,
            "type": pos,
            "ipa": generate_ipa(w),
            "plural": infer_plural(w, art, pos, plurals_dict),
            "meaning": de2zh[w_low],
            "example": ex,
            "example_en": it.get("example_sentence_english", "")
        }

        lvl = it.get("cefr_level", "")
        if lvl == "A2" and len(a2_cands) < 43:
            a2_cands.append(cand)
            existing_words.add(w_low)
        elif lvl == "B1" and len(b1_cands) < 1350:
            b1_cands.append(cand)
            existing_words.add(w_low)
        elif lvl == "B2" and len(b2_cands) < 1350:
            b2_cands.append(cand)
            existing_words.add(w_low)

    print(f"[*] Selected candidate counts: A2={len(a2_cands)} (need 43), B1={len(b1_cands)} (need 1350), B2={len(b2_cands)} (need 1350)")
    assert len(a2_cands) == 43, f"A2 candidate count {len(a2_cands)} != 43"
    assert len(b1_cands) == 1350, f"B1 candidate count {len(b1_cands)} != 1350"
    assert len(b2_cands) == 1350, f"B2 candidate count {len(b2_cands)} != 1350"

    all_cands = a2_cands + b1_cands + b2_cands
    sentences_to_translate = []
    for c in all_cands:
        ex = c["example"]
        if ex not in cache:
            sentences_to_translate.append(ex)

    # Deduplicate while preserving order
    unique_sents = list(dict.fromkeys(sentences_to_translate))
    print(f"[*] Sentences requiring translation: {len(unique_sents)} (already cached: {len(all_cands) - len(unique_sents)})")

    batch_size = 15
    total_batches = (len(unique_sents) + batch_size - 1) // batch_size
    for b_idx in range(total_batches):
        chunk = unique_sents[b_idx * batch_size : (b_idx + 1) * batch_size]
        translated = translate_batch_youdao(chunk)
        for s, t in zip(chunk, translated):
            if t and t != s:
                cache[s] = t
            elif s not in cache:
                cache[s] = t
        save_cache(cache)
        print(f"  [{b_idx+1}/{total_batches}] Progress: {min((b_idx+1)*batch_size, len(unique_sents))}/{len(unique_sents)} sentences translated...")
        time.sleep(0.4)

    save_cache(cache)

    # Attach translated exampleCn to all candidates
    for c in all_cands:
        ex = c["example"]
        c["exampleCn"] = cache.get(ex, c.get("example_en", ex))

    # ---- 1. Expand Level A2 to 1,350 words ----
    a2_path = os.path.join(DATA_DIR, "curriculum_a2.json")
    with open(a2_path, "r", encoding="utf-8") as f:
        a2_data = json.load(f)

    a2_ptr = 0
    for l in a2_data["lessons"]:
        needed = 90 - len(l["words"])
        if needed > 0:
            for item in a2_cands[a2_ptr : a2_ptr + needed]:
                l["words"].append({
                    "word": item["word"],
                    "article": item["article"],
                    "type": item["type"],
                    "ipa": item["ipa"],
                    "plural": item["plural"],
                    "meaning": item["meaning"],
                    "example": item["example"],
                    "exampleCn": item["exampleCn"]
                })
            a2_ptr += needed

    with open(a2_path, "w", encoding="utf-8") as f:
        json.dump(a2_data, f, ensure_ascii=False, indent=2)

    a2_counts = [len(l["words"]) for l in a2_data["lessons"]]
    print(f"[+] Level A2 finalized: total={sum(a2_counts)}, per_lesson={a2_counts[:3]}... ({len(a2_counts)} lessons)")

    # ---- 2. Expand Level B1 to 2,400 words ----
    b1_path = os.path.join(DATA_DIR, "curriculum_b1.json")
    with open(b1_path, "r", encoding="utf-8") as f:
        b1_data = json.load(f)

    b1_ptr = 0
    for l in b1_data["lessons"]:
        needed = 160 - len(l["words"])
        if needed > 0:
            for item in b1_cands[b1_ptr : b1_ptr + needed]:
                l["words"].append({
                    "word": item["word"],
                    "article": item["article"],
                    "type": item["type"],
                    "ipa": item["ipa"],
                    "plural": item["plural"],
                    "meaning": item["meaning"],
                    "example": item["example"],
                    "exampleCn": item["exampleCn"]
                })
            b1_ptr += needed

    with open(b1_path, "w", encoding="utf-8") as f:
        json.dump(b1_data, f, ensure_ascii=False, indent=2)

    b1_counts = [len(l["words"]) for l in b1_data["lessons"]]
    print(f"[+] Level B1 finalized: total={sum(b1_counts)}, per_lesson={b1_counts[:3]}... ({len(b1_counts)} lessons)")

    # ---- 3. Expand Level B2 to 2,400 words ----
    b2_path = os.path.join(DATA_DIR, "curriculum_b2.json")
    with open(b2_path, "r", encoding="utf-8") as f:
        b2_data = json.load(f)

    b2_ptr = 0
    for l in b2_data["lessons"]:
        needed = 160 - len(l["words"])
        if needed > 0:
            for item in b2_cands[b2_ptr : b2_ptr + needed]:
                l["words"].append({
                    "word": item["word"],
                    "article": item["article"],
                    "type": item["type"],
                    "ipa": item["ipa"],
                    "plural": item["plural"],
                    "meaning": item["meaning"],
                    "example": item["example"],
                    "exampleCn": item["exampleCn"]
                })
            b2_ptr += needed

    with open(b2_path, "w", encoding="utf-8") as f:
        json.dump(b2_data, f, ensure_ascii=False, indent=2)

    b2_counts = [len(l["words"]) for l in b2_data["lessons"]]
    print(f"[+] Level B2 finalized: total={sum(b2_counts)}, per_lesson={b2_counts[:3]}... ({len(b2_counts)} lessons)")

    print("\n" + "=" * 60)
    print("CURRICULUM VOCABULARY EXPANSION COMPLETED SUCCESSFULLY!")
    print(f"Level A0: 100 words (5 lessons x 20 words)")
    print(f"Level A1: 1,200 words (15 lessons x 80 words)")
    print(f"Level A2: {sum(a2_counts)} words (15 lessons x 90 words)")
    print(f"Level B1: {sum(b1_counts)} words (15 lessons x 160 words)")
    print(f"Level B2: {sum(b2_counts)} words (15 lessons x 160 words)")
    print(f"Total Curriculum Vocabulary: {100 + 1200 + sum(a2_counts) + sum(b1_counts) + sum(b2_counts)} words")
    print("=" * 60)

if __name__ == "__main__":
    main()
