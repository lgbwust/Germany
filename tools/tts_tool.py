#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TTS Audio Tool for German Learning
Allows testing German pronunciation audio locally, checking installed German voices on macOS,
and exporting sample audio pronunciation clips for offline usage if needed.
"""

import subprocess
import sys
import os
import json

def list_german_voices():
    print("[*] Inspecting available German TTS voices on macOS...")
    try:
        res = subprocess.run(["say", "-v", "?"], capture_output=True, text=True)
        german_voices = [line for line in res.stdout.splitlines() if "de_DE" in line or "de_AT" in line or "de_CH" in line]
        if german_voices:
            print("Found German voices:")
            for v in german_voices:
                print(f"  - {v}")
        else:
            print("No dedicated German voice found; system fallback will be used.")
        return german_voices
    except Exception as e:
        print(f"Error checking voices: {e}")
        return []

def speak_german(text, voice=None):
    cmd = ["say"]
    if voice:
        cmd.extend(["-v", voice])
    cmd.append(text)
    print(f"[*] Speaking: '{text}'...")
    subprocess.run(cmd)

def main():
    voices = list_german_voices()
    voice_name = None
    if voices:
        # e.g., 'Anna                de_DE    # Hallo, ich heiße Anna...'
        voice_name = voices[0].split()[0]
        print(f"Using voice: {voice_name}")

    test_words = [
        "Guten Tag! Willkommen bei DeutschMeister.",
        "Das deutsche Alphabet hat sechsundzwanzig Buchstaben.",
        "Übung macht den Meister."
    ]

    print("\nDo you want to test TTS audio playback? Pass argument '--speak' to hear audio.")
    if "--speak" in sys.argv:
        for t in test_words:
            speak_german(t, voice_name)
    else:
        print("Run with: python3 tools/tts_tool.py --speak to hear test phrases.")

if __name__ == "__main__":
    main()
