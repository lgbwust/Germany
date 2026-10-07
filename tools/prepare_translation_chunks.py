#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prepare Translation Chunks:
Selects exact Goethe candidates for A2 (+43), B1 (+1350), B2 (+1350) and splits
untranslated example sentences into parallel chunks for fast subagent translation.
"""

import json
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
CACHE_FILE = os.path.join(BASE_DIR, "vocab_sentence_cache.json")

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
    print("[*] Loading HanDeDict...")
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
    print(f"[*] HanDeDict terms: {len(de2zh)}")
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
    return plurals

def infer_plural(word, art, pos, plurals_dict):
    w_clean = word.lower().strip()
    if art:
        w_clean = re.sub(r"^(der|die|das)\s+", "", w_clean).strip()
    if w_clean in plurals_dict:
        return plurals_dict[w_clean]
    if pos != "n." and not art:
        return "-"
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

def main():
    de2zh = load_handedict()
    plurals_dict = load_plurals()

    # Existing words
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

    print(f"[*] Existing words in curriculum: {len(existing_words)}")

    # Load candidate pools
    with open(os.path.join(BASE_DIR, "german_decks.json"), "r", encoding="utf-8") as f:
        decks = json.load(f)

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

    print(f"[*] Candidate selection: A2={len(a2_cands)}, B1={len(b1_cands)}, B2={len(b2_cands)}")
    assert len(a2_cands) == 43
    assert len(b1_cands) == 1350
    assert len(b2_cands) == 1350

    all_data = {
        "a2": a2_cands,
        "b1": b1_cands,
        "b2": b2_cands
    }
    with open(os.path.join(DATA_DIR, "candidates_all.json"), "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)

    # Check cache
    cache = {}
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            cache = json.load(f)

    all_cands = a2_cands + b1_cands + b2_cands
    needed_sents = []
    for c in all_cands:
        ex = c["example"]
        if ex not in cache:
            needed_sents.append(ex)

    unique_sents = list(dict.fromkeys(needed_sents))
    print(f"[*] Total unique sentences needing translation: {len(unique_sents)} (already cached: {len(all_cands) - len(unique_sents)})")

    # Split into chunks of ~250
    chunk_size = 250
    chunks = [unique_sents[i:i + chunk_size] for i in range(0, len(unique_sents), chunk_size)]
    print(f"[*] Splitting into {len(chunks)} chunks of ~{chunk_size} sentences each.")

    for idx, ch in enumerate(chunks):
        chunk_data = [{"id": i, "de": s} for i, s in enumerate(ch)]
        out_path = os.path.join(DATA_DIR, f"trans_chunk_{idx}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(chunk_data, f, ensure_ascii=False, indent=2)
        print(f"  [+] Wrote {out_path} ({len(chunk_data)} sentences)")

if __name__ == "__main__":
    main()
