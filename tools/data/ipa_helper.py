#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
German IPA Generator & Phonetic Helper
Provides authentic International Phonetic Alphabet (IPA) annotations for German words.
"""

# Explicit overrides for high-frequency or irregular pronunciation
KNOWN_IPA = {
    "das Alphabet": "[alfaˈbeːt]",
    "der Buchstabe": "[ˈbuːxˌʃtaːbə]",
    "schön": "[ʃøːn]",
    "heißen": "[ˈhaɪsn̩]",
    "die Straße": "[ˈʃtʁaːsə]",
    "die Tür": "[tyːɐ̯]",
    "das Haus": "[haʊs]",
    "deutsch": "[dɔɪtʃ]",
    "Deutschland": "[ˈdɔɪtʃlant]",
    "begrüßen": "[bəˈɡʁyːsn̩]",
    "der Name": "[ˈnaːmə]",
    "kommen": "[ˈkɔmən]",
    "wohnen": "[ˈvoːnən]",
    "sprechen": "[ˈʃpʁɛçn̩]",
    "die Sprache": "[ˈʃpʁaːxə]",
    "gut": "[ɡuːt]",
    "danke": "[ˈdaŋkə]",
    "der Vater": "[ˈfaːtɐ]",
    "die Mutter": "[ˈmʊtɐ]",
    "das Kind": "[kɪnt]",
    "die Eltern": "[ˈɛltɐn]",
    "der Beruf": "[bəˈʁuːf]",
    "die Familie": "[faˈmiːli̯ə]",
    "arbeiten": "[ˈaʁbaɪtn̩]",
    "der Arzt": "[aːɐ̯tst]",
    "die Ärztin": "[ˈɛːɐ̯tstɪn]",
    "der Apfel": "[ˈapfl̩]",
    "das Brot": "[bʁoːt]",
    "der Kaffee": "[ˈkafe]",
    "das Wasser": "[ˈvasɐ]",
    "kaufen": "[ˈkaʊfn̩]",
    "kosten": "[ˈkɔstn̩]",
    "der Supermarkt": "[ˈzuːpɐˌmaʁkt]",
    "lecker": "[ˈlɛkɐ]",
    "aufstehen": "[ˈaʊfˌʃteːən]",
    "die Uhr": "[uːɐ̯]",
    "der Morgen": "[ˈmɔʁɡn̩]",
    "anrufen": "[ˈanˌʁuːfn̩]",
    "der Tag": "[taːk]",
    "die Woche": "[ˈvɔxə]",
    "frühstücken": "[ˈfʁyːˌʃtʏkn̩]",
    "abfahren": "[ˈapˌfaːʁən]",
    "die Wohnung": "[ˈvoːnʊŋ]",
    "das Zimmer": "[ˈtsɪmɐ]",
    "die Miete": "[ˈmiːtə]",
    "der Tisch": "[tɪʃ]",
    "der Stuhl": "[ʃtuːl]",
    "das Bett": "[bɛt]",
    "der Schrank": "[ʃʁaŋk]",
    "die Küche": "[ˈkʏçə]",
    "die Reise": "[ˈʁaɪzə]",
    "reisen": "[ˈʁaɪzn̩]",
    "der Urlaub": "[ˈuːɐ̯laʊp]",
    "besuchen": "[bəˈzuːxn̩]",
    "das Flugzeug": "[ˈfluːkˌtsɔɪk]",
    "der Koffer": "[ˈkɔfɐ]",
    "das Hotel": "[hoˈtɛl]",
    "bleiben": "[ˈblaɪbn̩]",
    "die Gesundheit": "[ɡəˈzʊnthaɪt]",
    "der Schmerz": "[ʃmɛʁts]",
    "das Fieber": "[ˈfiːbɐ]",
    "die Medizin": "[mediˈtsiːn]",
    "der Termin": "[tɛʁˈmiːn]",
    "fehlen": "[ˈfeːlən]",
    "sich ausruhen": "[zɪç ˈaʊsˌʁuːən]",
    "die Apotheke": "[apoˈteːkə]",
    "die Stadt": "[ʃtat]",
    "der Bahnhof": "[ˈbaːnˌhoːf]",
    "die Haltestelle": "[ˈhaltəˌʃtɛlə]",
    "die Ampel": "[ˈampl̩]",
    "stellen": "[ˈʃtɛlən]",
    "stehen": "[ˈʃteːən]",
    "geradeaus": "[ɡəʁaːdəˈʔaʊs]",
    "die Kreuzung": "[ˈkʁɔɪtsʊŋ]",
    "die Bewerbung": "[bəˈvɛʁbʊŋ]",
    "der Kollege": "[kɔˈleːɡə]",
    "der Chef": "[ʃɛf]",
    "das Büro": "[byˈʁoː]",
    "die Besprechung": "[bəˈʃpʁɛçʊŋ]",
    "die Erfahrung": "[ɛɐ̯ˈfaːʁʊŋ]",
    "verdienen": "[fɛɐ̯ˈdiːnən]",
    "kündigen": "[ˈkʏndɪɡn̩]",
    "schnell": "[ʃnɛl]",
    "billig": "[ˈbɪlɪç]",
    "teuer": "[ˈtɔɪ̯ɐ]",
    "wichtig": "[ˈvɪçtɪç]",
    "das Angebot": "[ˈanɡəˌboːt]",
    "die Qualität": "[kvaliˈtɛːt]",
    "auswählen": "[ˈaʊsˌvɛːlən]",
    "gefallen": "[ɡəˈfaln̩]"
}

def get_ipa(word_clean, full_word):
    """
    Returns authentic German IPA for a word.
    Uses known lexicon first, then applies standard German phonetic rules.
    """
    if full_word in KNOWN_IPA:
        return KNOWN_IPA[full_word]
    if word_clean in KNOWN_IPA:
        return KNOWN_IPA[word_clean]

    w = word_clean.lower()
    
    # Prefix handling for separable verbs / common prefixes
    prefix = ""
    stress = "ˈ"
    if w.startswith("be") or w.startswith("ge") or w.startswith("ver") or w.startswith("zer") or w.startswith("ent") or w.startswith("er"):
        stress = "" # second syllable usually stressed

    # Common replacements
    ipa = w
    # Diphthongs
    ipa = ipa.replace("äu", "ɔɪ").replace("eu", "ɔɪ").replace("ei", "aɪ").replace("ey", "aɪ").replace("ai", "aɪ").replace("au", "aʊ").replace("ie", "iː")
    
    # Umlaute
    ipa = ipa.replace("ä", "ɛː").replace("ö", "øː").replace("ü", "yː").replace("ß", "s")
    
    # Consonant clusters
    ipa = ipa.replace("sch", "ʃ").replace("tsch", "tʃ")
    if ipa.startswith("sp"):
        ipa = "ʃp" + ipa[2:]
    elif ipa.startswith("st"):
        ipa = "ʃt" + ipa[2:]
    
    # ch rule: after a, o, u, au -> [x], else [ç]
    res = []
    i = 0
    while i < len(ipa):
        if ipa[i:i+2] == "ch":
            prev = ipa[i-1] if i > 0 else ""
            if prev in "aou" or (i >= 2 and ipa[i-2:i] == "aʊ"):
                res.append("x")
            else:
                res.append("ç")
            i += 2
        elif ipa[i:i+2] == "ck":
            res.append("k")
            i += 2
        elif ipa[i:i+2] == "ph":
            res.append("f")
            i += 2
        elif ipa[i:i+2] == "th":
            res.append("t")
            i += 2
        elif ipa[i:i+2] == "qu":
            res.append("kv")
            i += 2
        else:
            res.append(ipa[i])
            i += 1
    ipa = "".join(res)
    
    # Ending -ig -> [ɪç]
    if ipa.endswith("ig"):
        ipa = ipa[:-2] + "ɪç"
    elif ipa.endswith("ung"):
        ipa = ipa[:-3] + "ʊŋ"
    elif ipa.endswith("er"):
        ipa = ipa[:-2] + "ɐ"
    elif ipa.endswith("en"):
        ipa = ipa[:-2] + "n̩"
        
    ipa = ipa.replace("w", "v").replace("z", "ts")
    if ipa.startswith("v"):
        ipa = "f" + ipa[1:]

    return f"[{stress}{ipa}]"
