#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builder for Level A1: Goethe-Zertifikat A1
15 Lessons x 70 Words = 1050 Words
"""

import json
import os
import sys

# Ensure tools/ can be imported
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.ipa_helper import get_ipa

def make_word(word, article, wtype, plural, meaning, example, example_cn):
    clean = word
    if word.startswith("der ") or word.startswith("die ") or word.startswith("das "):
        clean = word[4:]
    ipa = get_ipa(clean, word)
    return {
        "word": word,
        "article": article,
        "type": wtype,
        "ipa": ipa,
        "plural": plural,
        "meaning": meaning,
        "example": example,
        "exampleCn": example_cn
    }

def get_a1_lessons():
    # We define 15 lessons, each with 70 high-frequency Goethe A1 words
    lessons = []
    
    # LESSON 1: 相识、寒暄与国籍 (70 words)
    l01_raw = [
        ("hallo", "", "int.", "", "你好，喂", "Hallo, wie geht es dir?", "你好，你身体好吗？"),
        ("guten Morgen", "", "phrase", "", "早上好", "Guten Morgen, Herr Schmidt!", "早上好，施密特先生！"),
        ("guten Tag", "", "phrase", "", "你好，日安", "Guten Tag, wie kann ich helfen?", "你好，我能帮什么忙？"),
        ("guten Abend", "", "phrase", "", "晚上好", "Guten Abend allerseits!", "大家晚上好！"),
        ("gute Nacht", "", "phrase", "", "晚安", "Gute Nacht, schlaf gut!", "晚安，做个好梦！"),
        ("auf Wiedersehen", "", "phrase", "", "再见（正式面谈）", "Auf Wiedersehen und schönen Tag!", "再见，祝您一天愉快！"),
        ("tschüss", "", "int.", "", "再见（口语熟人）", "Tschüss, bis morgen!", "拜拜，明天见！"),
        ("bitte", "", "adv./int.", "", "请；不客气", "Ein Wasser, bitte!", "请来一杯水！"),
        ("danke", "", "int.", "", "谢谢", "Danke für Ihre Hilfe!", "谢谢您的帮助！"),
        ("vielen Dank", "", "phrase", "", "非常感谢", "Vielen Dank für die Einladung.", "非常感谢您的邀请。"),
        ("der Name", "der", "n.", "-n", "名字，姓名", "Mein Name ist Peter.", "我的名字叫彼得。"),
        ("der Vorname", "der", "n.", "-n", "名", "Mein Vorname ist Thomas.", "我的名字是托马斯。"),
        ("der Nachname", "der", "n.", "-n", "姓氏", "Wie ist Ihr Nachname?", "您的姓氏是什么？"),
        ("heißen", "", "v.", "heißt, hieß, geheißen", "名叫，称为", "Ich heiße Anna.", "我叫安娜。"),
        ("sein", "", "v.", "ist, war, ist gewesen", "是，存在", "Wir sind Studenten.", "我们是大学生。"),
        ("haben", "", "v.", "hat, hatte, gehabt", "有，拥有", "Ich habe eine Frage.", "我有一个问题。"),
        ("kommen", "", "v.", "kommt, kam, ist gekommen", "来，来自", "Woher kommen Sie?", "您来自哪里？"),
        ("wohnen", "", "v.", "wohnt, wohnte, gewohnt", "居住", "Ich wohne in Berlin.", "我住在柏林。"),
        ("leben", "", "v.", "lebt, lebte, gelebt", "生活，活着", "Er lebt in München.", "他生活在慕尼黑。"),
        ("sprechen", "", "v.", "spricht, sprach, gesprochen", "说，讲", "Sprechen Sie Englisch?", "您讲英语吗？"),
        ("die Sprache", "die", "n.", "-n", "语言", "Deutsch ist eine schöne Sprache.", "德语是一门优美的语言。"),
        ("das Deutsch", "das", "n.", "-", "德语", "Ich lerne jetzt Deutsch.", "我现在正在学德语。"),
        ("das Chinesisch", "das", "n.", "-", "汉语，中文", "Chinesisch ist meine Muttersprache.", "汉语是我的母语。"),
        ("das Englisch", "das", "n.", "-", "英语", "Er spricht sehr gut Englisch.", "他英语说得非常好。"),
        ("das Land", "das", "n.", "Länder", "国家；乡村", "Deutschland ist ein schönes Land.", "德国是个美丽的国家。"),
        ("das Deutschland", "das", "n.", "-", "德国", "Wir fliegen nach Deutschland.", "我们乘飞机去德国。"),
        ("das China", "das", "n.", "-", "中国", "Ich komme aus China.", "我来自中国。"),
        ("das Österreich", "das", "n.", "-", "奥地利", "Wien ist die Hauptstadt von Österreich.", "维也纳是奥地利的首都。"),
        ("die Schweiz", "die", "n.", "-", "瑞士", "Er wohnt in der Schweiz.", "他住在瑞士。"),
        ("das Frankreich", "das", "n.", "-", "法国", "Paris liegt in Frankreich.", "巴黎位于法国。"),
        ("das Italien", "das", "n.", "-", "意大利", "Rom ist eine alte Stadt in Italien.", "罗马是意大利的一座古老城市。"),
        ("das Spanien", "das", "n.", "-", "西班牙", "Wir machen Urlaub in Spanien.", "我们在西班牙度假。"),
        ("das Japan", "das", "n.", "-", "日本", "Tokio liegt in Japan.", "东京在日本。"),
        ("die USA", "die", "n.pl.", "-", "美国", "Er studiert in den USA.", "他在美国留学。"),
        ("neu", "", "adj.", "neuer, am neuesten", "新的", "Das ist mein neuer Kollege.", "这是我的新同事。"),
        ("alt", "", "adj.", "älter, am ältesten", "老的，旧的", "Wie alt bist du?", "你多大了？"),
        ("groß", "", "adj.", "größer, am größten", "大的，高大的", "Berlin ist eine große Stadt.", "柏林是一座大城市。"),
        ("klein", "", "adj.", "kleiner, am kleinsten", "小的", "Mein Zimmer ist klein aber fein.", "我的房间小但精致。"),
        ("wer", "", "pron.", "", "谁", "Wer ist das?", "那是谁？"),
        ("was", "", "pron.", "", "什么", "Was machen Sie beruflich?", "您从事什么职业？"),
        ("wie", "", "adv.", "", "怎样，如何", "Wie geht es Ihnen?", "您最近好吗？"),
        ("wo", "", "adv.", "", "在哪里", "Wo wohnen Sie jetzt?", "您现在住在哪里？"),
        ("woher", "", "adv.", "", "从哪里来", "Woher kommst du?", "你从哪里来？"),
        ("wohin", "", "adv.", "", "去哪里", "Wohin fährst du am Wochenende?", "你周末去哪儿？"),
        ("ja", "", "part.", "", "是的", "Ja, das stimmt genau.", "是的，完全正确。"),
        ("nein", "", "part.", "", "不，不是", "Nein, ich bin nicht müde.", "不，我不累。"),
        ("nicht", "", "adv.", "", "不，没有", "Das ist nicht schwer.", "这并不难。"),
        ("auch", "", "adv.", "", "也，同样", "Ich lerne auch Deutsch.", "我也在学德语。"),
        ("sehr", "", "adv.", "", "非常，很", "Vielen Dank, sehr nett von Ihnen!", "非常感谢，您真好！"),
        ("gut", "", "adj./adv.", "besser, am besten", "好的", "Das schmeckt wirklich gut.", "这尝起来真不错。"),
        ("schlecht", "", "adj./adv.", "schlechter, am schlechtesten", "坏的，差的", "Das Wetter ist heute schlecht.", "今天天气很差。"),
        ("der Herr", "der", "n.", "-en", "先生", "Guten Tag, Herr Müller!", "你好，穆勒先生！"),
        ("die Frau", "die", "n.", "-en", "女士，妻子", "Frau Weber ist Lehrerin.", "韦伯女士是教师。"),
        ("die Dame", "die", "n.", "-n", "女士，夫人", "Sehr geehrte Damen und Herren!", "尊敬的女士们、先生们！"),
        ("der Freund", "der", "n.", "-e", "男朋友，男性朋友", "Das ist mein bester Freund.", "这是我最好的朋友。"),
        ("die Freundin", "die", "n.", "-nen", "女朋友，女性朋友", "Meine Freundin lernt Medizin.", "我的女朋友学医。"),
        ("der Kollege", "der", "n.", "-n", "男同事", "Mein Kollege hilft mir gern.", "我的同事乐意帮我。"),
        ("die Kollegin", "die", "n.", "-nen", "女同事", "Sie ist eine nette Kollegin.", "她是一位和善的女同事。"),
        ("die Stadt", "die", "n.", "Städte", "城市", "München ist eine schöne Stadt.", "慕尼黑是一座美丽的城市。"),
        ("die Hauptstadt", "die", "n.", "Hauptstädte", "首都", "Berlin ist die Hauptstadt von Deutschland.", "柏林是德国首都。"),
        ("die Adresse", "die", "n.", "-n", "地址", "Wie ist deine Adresse?", "你的地址是什么？"),
        ("die Straße", "die", "n.", "-n", "街道", "Ich wohne in der Schillerstraße.", "我住在席勒街。"),
        ("die Hausnummer", "die", "n.", "-n", "门牌号", "Welche Hausnummer haben Sie?", "您的门牌号是几号？"),
        ("die Telefonnummer", "die", "n.", "-n", "电话号码", "Meine Telefonnummer ist 12345.", "我的电话号码是12345。"),
        ("die Handynummer", "die", "n.", "-n", "手机号码", "Kannst du mir deine Handynummer geben?", "你能给我你的手机号吗？"),
        ("die E-Mail", "die", "n.", "-s", "电子邮件", "Ich schreibe dir eine E-Mail.", "我给你发一封电子邮件。"),
        ("das Formular", "das", "n.", "-e", "表格", "Bitte füllen Sie das Formular aus.", "请填写这份表格。"),
        ("ausfüllen", "", "v.", "füllt aus, füllte aus, ausgefüllt", "填写（表格）", "Füllen Sie bitte Name und Vorname aus.", "请填写姓与名。"),
        ("die Unterschrift", "die", "n.", "-en", "签名", "Hier fehlt noch Ihre Unterschrift.", "这里还缺您的签名。"),
        ("unterschreiben", "", "v.", "unterschreibt, unterschrieb, unterschrieben", "签名，签署", "Bitte unterschreiben Sie hier!", "请在这里签名！")
    ]
    
    # We will build 15 distinct lessons for A1, each having 70 words
    lesson_titles = [
        ("A1_L01", "第1课：相识、寒暄与国籍 (Begrüßung & Länder)", "掌握人称代词、动词变位规则、sein/haben/heißen、国家与国籍表达",
         "动词现在时变位规则 (Präsens) 与基础疑问句",
         [{"heading": "1. 规则动词现在时词尾", "content": "ich -e, du -st, er/sie/es -t, wir -en, ihr -t, sie/Sie -en。\n例如：lernen (ich lerne, du lernst, er lernt)。"},
          {"heading": "2. 疑问句语序", "content": "特殊疑问句疑问词占首位，动词占第二位；一般疑问句动词位于句首。"}],
         [{"id": "A1_L01_Q1", "type": "GRAMMAR_FILL", "question": "Woher ______ du? - Ich ______ aus China.", "options": ["kommst / komme", "kommt / komme", "kommen / kommt", "kommst / bin"], "correctIndex": 0, "explanation": "du 词尾用 -st, ich 词尾用 -e。"}],
         l01_raw),
    ]

    # Let's programmatically construct the remaining 14 lessons with 70 words each
    # to form the complete 1050-word A1 lexicon!
    from .vocab_a1_data import get_a1_remaining_lessons
    remaining = get_a1_remaining_lessons()
    for item in remaining:
        lesson_titles.append(item)

    for les_id, title, summary, g_title, g_sec, q_items, raw_list in lesson_titles:
        words = [make_word(w[0], w[1], w[2], w[3], w[4], w[5], w[6]) for w in raw_list]
        lessons.append({
            "id": les_id,
            "title": title,
            "summary": summary,
            "grammar": {
                "title": g_title,
                "sections": g_sec
            },
            "words": words,
            "quiz": q_items
        })

    return lessons

def main():
    lessons = get_a1_lessons()
    total_words = sum(len(l["words"]) for l in lessons)
    print(f"[OK] Level A1 compiled: {len(lessons)} lessons, {total_words} words.")
    out_path = os.path.join(os.path.dirname(__file__), "curriculum_a1.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(lessons, f, ensure_ascii=False, indent=2)
    print(f"[OK] Saved {out_path}")

if __name__ == "__main__":
    main()
