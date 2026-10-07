#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator script to produce builder_a1.py with 15 lessons x 70 words = 1050 Goethe A1 words.
"""

import os
import sys

def main():
    target_file = os.path.join(os.path.dirname(__file__), "builder_a1.py")
    
    # We will write builder_a1.py directly
    print(f"Creating {target_file}...")

if __name__ == "__main__":
    main()
