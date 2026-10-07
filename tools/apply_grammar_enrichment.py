#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Applies Enriched Grammar to all 65 lessons across Levels A0, A1, A2, B1, and B2.
"""

import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
sys.path.insert(0, BASE_DIR)

from grammar_data_a0 import A0_GRAMMAR
from grammar_data_a1 import A1_GRAMMAR
from grammar_data_a2 import A2_GRAMMAR
from grammar_data_b1 import B1_GRAMMAR
from grammar_data_b2 import B2_GRAMMAR

def update_json_curriculum(file_name, grammar_dict, level_id):
    path = os.path.join(DATA_DIR, file_name)
    print(f"[*] Updating {level_id} grammar in {path}...")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    updated_count = 0
    for lesson in data.get("lessons", []):
        lid = lesson.get("id")
        if lid in grammar_dict:
            lesson["grammar"] = grammar_dict[lid]
            updated_count += 1
        else:
            print(f"[!] Warning: lesson {lid} not found in grammar dictionary!")

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"[+] Updated {updated_count} lessons in {file_name}.")

def update_level_a0_file():
    a0_py_path = os.path.join(DATA_DIR, "level_a0.py")
    print(f"[*] Updating level_a0.py at {a0_py_path}...")
    
    # We can rewrite get_level_a0() in level_a0.py to inject A0_GRAMMAR
    with open(a0_py_path, "r", encoding="utf-8") as f:
        content = f.read()

    # If grammar_data_a0 is not imported, import it and apply before return
    if "from grammar_data_a0 import A0_GRAMMAR" not in content:
        # Add import at the top
        new_content = "import os\nimport sys\nsys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\nfrom grammar_data_a0 import A0_GRAMMAR\n\n" + content
        # In get_level_a0, before returning, apply A0_GRAMMAR to all lessons
        needle = "def get_level_a0():\n    return {"
        replacement = """def get_level_a0():
    data = {"""
        new_content = new_content.replace(needle, replacement)
        
        # At end of get_level_a0():
        new_content += """
    for l in data["lessons"]:
        if l["id"] in A0_GRAMMAR:
            l["grammar"] = A0_GRAMMAR[l["id"]]
    return data
"""
        with open(a0_py_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("[+] level_a0.py updated with A0_GRAMMAR injection.")
    else:
        print("[=] level_a0.py already configured.")

def main():
    print("=" * 60)
    print("APPLYING ENRICHED GRAMMAR TO ALL LEVELS")
    print("=" * 60)

    # 1. Update A0
    update_level_a0_file()

    # 2. Update A1
    update_json_curriculum("curriculum_a1.json", A1_GRAMMAR, "A1")

    # 3. Update A2
    update_json_curriculum("curriculum_a2.json", A2_GRAMMAR, "A2")

    # 4. Update B1
    update_json_curriculum("curriculum_b1.json", B1_GRAMMAR, "B1")

    # 5. Update B2
    update_json_curriculum("curriculum_b2.json", B2_GRAMMAR, "B2")

    print("\n[+] Triggering build_master_curriculum.py...")
    import build_master_curriculum
    build_master_curriculum.main()

    print("\n[+] Triggering validate_data.py...")
    import validate_data
    val_res = validate_data.validate_curriculum(os.path.join(BASE_DIR, "curriculum.json"))
    if not val_res:
        print("[ERROR] Validation failed!")
        sys.exit(1)

    print("\n" + "=" * 60)
    print("ALL GRAMMAR ENRICHMENT APPLIED AND VALIDATED SUCCESSFULLY!")
    print("=" * 60)

if __name__ == "__main__":
    main()
