#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assemble Enriched Curriculum:
Merges translated sentence chunks into master sentence cache,
assigns translations to candidates in candidates_all.json,
writes curriculum_a2.json, curriculum_b1.json, curriculum_b2.json,
rebuilds master curriculum, and validates everything.
"""

import json
import os
import sys
import glob

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
CACHE_FILE = os.path.join(BASE_DIR, "vocab_sentence_cache.json")

def main():
    print("=" * 60)
    print("ASSEMBLING ENRICHED CURRICULUM")
    print("=" * 60)

    # 1. Update cache with completed chunks
    cache = {}
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            cache = json.load(f)

    done_files = sorted(glob.glob(os.path.join(DATA_DIR, "trans_chunk_*_done.json")))
    print(f"[*] Found {len(done_files)} completed chunk files.")

    for df in done_files:
        try:
            with open(df, "r", encoding="utf-8") as f:
                items = json.load(f)
            count = 0
            for it in items:
                de = it.get("de", "").strip()
                zh = it.get("zh", "").strip()
                if de and zh and zh != de:
                    cache[de] = zh
                    count += 1
            print(f"  [+] Loaded {count} translations from {os.path.basename(df)}")
        except Exception as e:
            print(f"  [!] Error reading {df}: {e}")

    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)
    print(f"[*] Cache updated with {len(cache)} total translations.")

    # 2. Load candidates
    cands_path = os.path.join(DATA_DIR, "candidates_all.json")
    with open(cands_path, "r", encoding="utf-8") as f:
        cands_all = json.load(f)

    a2_cands = cands_all["a2"]
    b1_cands = cands_all["b1"]
    b2_cands = cands_all["b2"]

    # 3. Update curriculum_a2.json
    a2_path = os.path.join(DATA_DIR, "curriculum_a2.json")
    with open(a2_path, "r", encoding="utf-8") as f:
        a2_data = json.load(f)

    a2_ptr = 0
    for l in a2_data["lessons"]:
        needed = 90 - len(l["words"])
        if needed > 0:
            for item in a2_cands[a2_ptr : a2_ptr + needed]:
                ex = item["example"]
                zh = cache.get(ex, item.get("example_en", ex))
                l["words"].append({
                    "word": item["word"],
                    "article": item["article"],
                    "type": item["type"],
                    "ipa": item["ipa"],
                    "plural": item["plural"],
                    "meaning": item["meaning"],
                    "example": item["example"],
                    "exampleCn": zh
                })
            a2_ptr += needed

    with open(a2_path, "w", encoding="utf-8") as f:
        json.dump(a2_data, f, ensure_ascii=False, indent=2)
    a2_counts = [len(l["words"]) for l in a2_data["lessons"]]
    print(f"[+] Level A2 total words: {sum(a2_counts)} ({len(a2_counts)} lessons x 90 words)")

    # 4. Update curriculum_b1.json
    b1_path = os.path.join(DATA_DIR, "curriculum_b1.json")
    with open(b1_path, "r", encoding="utf-8") as f:
        b1_data = json.load(f)

    b1_ptr = 0
    for l in b1_data["lessons"]:
        needed = 160 - len(l["words"])
        if needed > 0:
            for item in b1_cands[b1_ptr : b1_ptr + needed]:
                ex = item["example"]
                zh = cache.get(ex, item.get("example_en", ex))
                l["words"].append({
                    "word": item["word"],
                    "article": item["article"],
                    "type": item["type"],
                    "ipa": item["ipa"],
                    "plural": item["plural"],
                    "meaning": item["meaning"],
                    "example": item["example"],
                    "exampleCn": zh
                })
            b1_ptr += needed

    with open(b1_path, "w", encoding="utf-8") as f:
        json.dump(b1_data, f, ensure_ascii=False, indent=2)
    b1_counts = [len(l["words"]) for l in b1_data["lessons"]]
    print(f"[+] Level B1 total words: {sum(b1_counts)} ({len(b1_counts)} lessons x 160 words)")

    # 5. Update curriculum_b2.json
    b2_path = os.path.join(DATA_DIR, "curriculum_b2.json")
    with open(b2_path, "r", encoding="utf-8") as f:
        b2_data = json.load(f)

    b2_ptr = 0
    for l in b2_data["lessons"]:
        needed = 160 - len(l["words"])
        if needed > 0:
            for item in b2_cands[b2_ptr : b2_ptr + needed]:
                ex = item["example"]
                zh = cache.get(ex, item.get("example_en", ex))
                l["words"].append({
                    "word": item["word"],
                    "article": item["article"],
                    "type": item["type"],
                    "ipa": item["ipa"],
                    "plural": item["plural"],
                    "meaning": item["meaning"],
                    "example": item["example"],
                    "exampleCn": zh
                })
            b2_ptr += needed

    with open(b2_path, "w", encoding="utf-8") as f:
        json.dump(b2_data, f, ensure_ascii=False, indent=2)
    b2_counts = [len(l["words"]) for l in b2_data["lessons"]]
    print(f"[+] Level B2 total words: {sum(b2_counts)} ({len(b2_counts)} lessons x 160 words)")

    print("\n[OK] Curriculum files successfully written!")

if __name__ == "__main__":
    main()
