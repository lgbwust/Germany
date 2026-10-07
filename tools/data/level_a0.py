#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Level A0: German Phonetics & Alphabet (5 Comprehensive Lessons)
20 foundation words per lesson = 100 total vocabulary words.
8 in-depth questions per lesson = 40 total quiz questions.
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from grammar_data_a0 import A0_GRAMMAR
from quiz_data_a0 import A0_QUIZZES

def get_level_a0():
    data = {
        "id": "A0",
        "name": "A0 语音与字母发音基石",
        "goetheLevel": "A0 零基础发音",
        "description": "系统掌握德语26个基础字母与4个特殊字母（ä, ö, ü, ß）、元音长短音、复合元音、辅音组合规律与重音规则，实现'见词能读，听音能写'！",
        "lessons": [
            {
                "id": "A0_L1",
                "title": "第1课：德语字母表与特殊字符 (Alphabet & Sonderzeichen)",
                "summary": "掌握德语26个字母与4个独有特殊字符 ä, ö, ü, ß 的标准发音",
                "grammar": {},
                "words": [
                    {"word": "das Alphabet", "article": "das", "type": "n.", "ipa": "[alfaˈbeːt]", "plural": "-e", "meaning": "字母表", "example": "Das deutsche Alphabet hat 26 Buchstaben und 4 Sonderzeichen.", "exampleCn": "德语字母表有26个基础字母和4个特殊字符。"},
                    {"word": "der Buchstabe", "article": "der", "type": "n.", "ipa": "[ˈbuːxˌʃtaːbə]", "plural": "-n", "meaning": "字母", "example": "Wie spricht man diesen Buchstaben aus?", "exampleCn": "这个字母怎么发音？"},
                    {"word": "das Wort", "article": "das", "type": "n.", "ipa": "[vɔʁt]", "plural": "Wörter", "meaning": "单词，字", "example": "Können Sie dieses deutsche Wort buchstabieren?", "exampleCn": "您能拼写一下这个德语单词吗？"},
                    {"word": "buchstabieren", "article": "", "type": "v.", "ipa": "[buːxʃtaˈbiːʁən]", "plural": "buchstabiert, buchstabierte, buchstabiert", "meaning": "拼读，拼写出字母", "example": "Bitte buchstabieren Sie Ihren Nachnamen!", "exampleCn": "请拼写您的姓氏！"},
                    {"word": "die Aussprache", "article": "die", "type": "n.", "ipa": "[ˈaʊsˌʃpʁaːxə]", "plural": "-n", "meaning": "发音，语音", "example": "Ihre Aussprache ist sehr deutlich und sauber.", "exampleCn": "您的发音非常清晰准确。"},
                    {"word": "sprechen", "article": "", "type": "v.", "ipa": "[ˈʃpʁɛçn̩]", "plural": "spricht, sprach, gesprochen", "meaning": "说，讲", "example": "Ich spreche langsam und klar.", "exampleCn": "我说得慢且清楚。"},
                    {"word": "hören", "article": "", "type": "v.", "ipa": "[ˈhøːʁən]", "plural": "hört, hörte, gehört", "meaning": "听，收听", "example": "Hören Sie den Dialog genau zu!", "exampleCn": "请仔细听这段对话！"},
                    {"word": "wiederholen", "article": "", "type": "v.", "ipa": "[viːdɐˈhoːlən]", "plural": "wiederholt, wiederholte, wiederholt", "meaning": "重复，复习", "example": "Wiederholen Sie bitte den Satz!", "exampleCn": "请重复一遍这个句子！"},
                    {"word": "laut", "article": "", "type": "adj./adv.", "ipa": "[laʊt]", "plural": "", "meaning": "大声的，响亮的", "example": "Lesen Sie den Text bitte laut vor!", "exampleCn": "请大声朗读课文！"},
                    {"word": "leise", "article": "", "type": "adj./adv.", "ipa": "[ˈlaɪzə]", "plural": "", "meaning": "轻声的，安静的", "example": "Bitte sprechen Sie nicht so leise.", "exampleCn": "请不要这么小声说话。"},
                    {"word": "der Umlaut", "article": "der", "type": "n.", "ipa": "[ˈʊmˌlaʊt]", "plural": "-e", "meaning": "变元音 (ä, ö, ü)", "example": "Im Deutschen gibt es drei Umlaute: ä, ö und ü.", "exampleCn": "德语中有三个变元音：ä、ö 和 ü。"},
                    {"word": "das Eszett", "article": "das", "type": "n.", "ipa": "[ɛsˈtsɛt]", "plural": "-", "meaning": "字母 ß (Eszett / scharfes S)", "example": "Das Eszett steht nur nach langen Vokalen.", "exampleCn": "字母 ß 只出现在长元音或双元音之后。"},
                    {"word": "der Vokal", "article": "der", "type": "n.", "ipa": "[voˈkaːl]", "plural": "-e", "meaning": "元音", "example": "Die Vokale im Deutschen sind a, e, i, o, u.", "exampleCn": "德语中的元音是 a, e, i, o, u。"},
                    {"word": "der Konsonant", "article": "der", "type": "n.", "ipa": "[kɔnzoˈnant]", "plural": "-en", "meaning": "辅音", "example": "B, C, D und F sind Konsonanten.", "exampleCn": "B, C, D 和 F 是辅音。"},
                    {"word": "die Silbe", "article": "die", "type": "n.", "ipa": "[ˈzɪlbə]", "plural": "-n", "meaning": "音节", "example": "Dieses Wort besteht aus zwei Silben.", "exampleCn": "这个单词由两个音节组成。"},
                    {"word": "schreiben", "article": "", "type": "v.", "ipa": "[ˈʃʁaɪbn̩]", "plural": "schreibt, schrieb, geschrieben", "meaning": "写，书写", "example": "Schreiben Sie das Wort bitte an die Tafel!", "exampleCn": "请把这个词写在黑板上！"},
                    {"word": "lesen", "article": "", "type": "v.", "ipa": "[ˈleːzn̩]", "plural": "liest, las, gelesen", "meaning": "读，朗读", "example": "Wir lesen den Text gemeinsam.", "exampleCn": "我们一起读这段课文。"},
                    {"word": "das Zeichen", "article": "das", "type": "n.", "ipa": "[ˈtsaɪçn̩]", "plural": "-", "meaning": "符号，字符", "example": "Satzzeichen sind wichtig für den Satzbau.", "exampleCn": "标点符号对句式结构很重要。"},
                    {"word": "groß", "article": "", "type": "adj.", "ipa": "[ɡʁoːs]", "plural": "", "meaning": "大写的，大的", "example": "Nomen werden im Deutschen immer großgeschrieben.", "exampleCn": "德语中名词一律大写。"},
                    {"word": "klein", "article": "", "type": "adj.", "ipa": "[klaɪn]", "plural": "", "meaning": "小写的，小的", "example": "Verben und Adjektive schreibt man meistens klein.", "exampleCn": "动词和形容词通常小写。"}
                ],
                "quiz": []
            },
            {
                "id": "A0_L2",
                "title": "第2课：元音体系与长短音发音秘籍 (Lange & kurze Vokale: a, e, i, o, u, ä, ö, ü)",
                "summary": "掌握德语元音长短音黄金三定律、变元音开口与舌位",
                "grammar": {},
                "words": [
                    {"word": "der Abend", "article": "der", "type": "n.", "ipa": "[ˈaːbn̩t]", "plural": "-e", "meaning": "晚上 (元音 a 发长音 [a:])", "example": "Guten Abend, meine Damen und Herren!", "exampleCn": "女士们先生们，晚上好！"},
                    {"word": "der Apfel", "article": "der", "type": "n.", "ipa": "[ˈapfl̩]", "plural": "Äpfel", "meaning": "苹果 (双辅音 pf 前发短音 [a])", "example": "Ein Apfel am Tag hält den Arzt fern.", "exampleCn": "一天一苹果，医生远离我。"},
                    {"word": "der See", "article": "der", "type": "n.", "ipa": "[zeː]", "plural": "-n", "meaning": "湖泊 (叠写 ee 发长音 [e:])", "example": "Wir machen am Wochenende einen Ausflug an den See.", "exampleCn": "我们周末去湖边郊游。"},
                    {"word": "das Bett", "article": "das", "type": "n.", "ipa": "[bɛt]", "plural": "-en", "meaning": "床 (双辅音 tt 前发短音 [ɛ])", "example": "Das Kind geht um acht Uhr ins Bett.", "exampleCn": "孩子八点上床睡觉。"},
                    {"word": "die Tür", "article": "die", "type": "n.", "ipa": "[tyːɐ̯]", "plural": "-en", "meaning": "门 (ü 发长音 [y:])", "example": "Bitte schließen Sie die Tür leise!", "exampleCn": "请轻声关门！"},
                    {"word": "die Mütter", "article": "die", "type": "n.pl.", "ipa": "[ˈmʏtɐ]", "plural": "-", "meaning": "母亲们 (双辅音 tt 前发短音 [ʏ])", "example": "Die Mütter sprechen über ihre Kinder.", "exampleCn": "母亲们在谈论她们的孩子。"},
                    {"word": "das Öl", "article": "das", "type": "n.", "ipa": "[øːl]", "plural": "-e", "meaning": "油 (ö 发长音 [ø:])", "example": "Olivenöl ist sehr gesund für den Körper.", "exampleCn": "橄榄油对身体非常有益。"},
                    {"word": "öffnen", "article": "", "type": "v.", "ipa": "[ˈœfnən]", "plural": "öffnet, öffnete, geöffnet", "meaning": "打开 (双辅音 fn 前发短音 [œ])", "example": "Öffnen Sie bitte das Buch auf Seite zehn!", "exampleCn": "请翻开书到第十页！"},
                    {"word": "der Name", "article": "der", "type": "n.", "ipa": "[ˈnaːmə]", "plural": "-n", "meaning": "名字 (开音节 a 发长音 [a:])", "example": "Mein Name ist Thomas Müller.", "exampleCn": "我的名字叫托马斯·穆勒。"},
                    {"word": "die Sonne", "article": "die", "type": "n.", "ipa": "[ˈzɔnə]", "plural": "-", "meaning": "太阳 (双辅音 nn 前发短音 [ɔ])", "example": "Die Sonne scheint heute sehr hell.", "exampleCn": "今天阳光明媚灿烂。"},
                    {"word": "das Paar", "article": "das", "type": "n.", "ipa": "[paːɐ̯]", "plural": "-e", "meaning": "一对，一双 (元音叠写 aa 发长音 [a:])", "example": "Ein Paar Schuhe steht vor der Tür.", "exampleCn": "一双鞋放在门前。"},
                    {"word": "die Uhr", "article": "die", "type": "n.", "ipa": "[uːɐ̯]", "plural": "-en", "meaning": "钟表，时间 (带 h 读长音 [u:])", "example": "Wie viel Uhr ist es jetzt?", "exampleCn": "现在几点了？"},
                    {"word": "der Tee", "article": "der", "type": "n.", "ipa": "[teː]", "plural": "-", "meaning": "茶 (元音叠写 ee 读长音 [e:])", "example": "Ich trinke morgens gerne heißen Tee.", "exampleCn": "我早上喜欢喝热茶。"},
                    {"word": "das Boot", "article": "das", "type": "n.", "ipa": "[boːt]", "plural": "-e", "meaning": "小船 (元音叠写 oo 读长音 [o:])", "example": "Das Boot schwimmt auf dem See.", "exampleCn": "小船在湖面上漂浮。"},
                    {"word": "die Mitte", "article": "die", "type": "n.", "ipa": "[ˈmɪtə]", "plural": "-", "meaning": "中间 (双辅音 tt 前读短音 [ɪ])", "example": "Er steht in der Mitte des Zimmers.", "exampleCn": "他站在房间的正中间。"},
                    {"word": "die Puppe", "article": "die", "type": "n.", "ipa": "[ˈpʊpə]", "plural": "-n", "meaning": "洋娃娃 (双辅音 pp 前读短音 [ʊ])", "example": "Das Kind spielt mit der Puppe.", "exampleCn": "孩子正在玩洋娃娃。"},
                    {"word": "die Tasse", "article": "die", "type": "n.", "ipa": "[ˈtasə]", "plural": "-n", "meaning": "茶杯 (双辅音 ss 前读短音 [a])", "example": "Eine Tasse Kaffee bitte!", "exampleCn": "请来一杯咖啡！"},
                    {"word": "die Nuss", "article": "die", "type": "n.", "ipa": "[nʊs]", "plural": "Nüsse", "meaning": "坚果 (双辅音 ss 前读短音 [ʊ])", "example": "Eichhörnchen essen gerne Nüsse.", "exampleCn": "松鼠喜欢吃坚果。"},
                    {"word": "lang", "article": "", "type": "adj.", "ipa": "[laŋ]", "plural": "", "meaning": "长的 (长元音)", "example": "Dieser Vokal wird lang ausgesprochen.", "exampleCn": "这个元音发长音。"},
                    {"word": "kurz", "article": "", "type": "adj.", "ipa": "[kʊʁts]", "plural": "", "meaning": "短的 (短元音)", "example": "Vor zwei Konsonanten ist der Vokal meistens kurz.", "exampleCn": "在两个辅音前，元音通常发短音。"}
                ],
                "quiz": []
            },
            {
                "id": "A0_L3",
                "title": "第3课：复合元音与双元音法则 (Diphthonge: ei, ai, au, eu, äu)",
                "summary": "掌握德语双元音滑动口型与同音异形组合",
                "grammar": {},
                "words": [
                    {"word": "mein", "article": "", "type": "pron.", "ipa": "[maɪn]", "plural": "", "meaning": "我的 (双元音 ei 读 [aɪ])", "example": "Das ist mein neuer Deutschlehrer.", "exampleCn": "这是我的新德语老师。"},
                    {"word": "dein", "article": "", "type": "pron.", "ipa": "[daɪn]", "plural": "", "meaning": "你的 (双元音 ei 读 [aɪ])", "example": "Ist das dein Koffer?", "exampleCn": "这是你的行李箱吗？"},
                    {"word": "das Haus", "article": "das", "type": "n.", "ipa": "[haʊs]", "plural": "Häuser", "meaning": "房子 (双元音 au 读 [aʊ])", "example": "Unser Haus hat einen schönen Garten.", "exampleCn": "我们的房子带有一座漂亮的花园。"},
                    {"word": "die Maus", "article": "die", "type": "n.", "ipa": "[maʊs]", "plural": "Mäuse", "meaning": "老鼠 (双元音 au 读 [aʊ])", "example": "Die Katze fängt eine kleine Maus.", "exampleCn": "猫抓到了一只小老鼠。"},
                    {"word": "heute", "article": "", "type": "adv.", "ipa": "[ˈhɔɪtə]", "plural": "", "meaning": "今天 (双元音 eu 读 [ɔɪ])", "example": "Heute ist das Wetter wunderbar.", "exampleCn": "今天天气非常晴朗。"},
                    {"word": "neu", "article": "", "type": "adj.", "ipa": "[nɔɪ]", "plural": "", "meaning": "新的 (双元音 eu 读 [ɔɪ])", "example": "Ich habe ein neues Lehrbuch gekauft.", "exampleCn": "我买了一本新教科书。"},
                    {"word": "die Frau", "article": "die", "type": "n.", "ipa": "[fʁaʊ]", "plural": "-en", "meaning": "女士，妻子 (双元音 au 读 [aʊ])", "example": "Frau Müller kommt aus Hamburg.", "exampleCn": "穆勒女士来自汉堡。"},
                    {"word": "der Baum", "article": "der", "type": "n.", "ipa": "[baʊm]", "plural": "Bäume", "meaning": "树木 (双元音 au 读 [aʊ])", "example": "Der Baum ist grün und hoch.", "exampleCn": "这棵树又绿又高。"},
                    {"word": "die Bäume", "article": "die", "type": "n.pl.", "ipa": "[ˈbɔɪmə]", "plural": "-", "meaning": "树木（复数，双元音 äu 读 [ɔɪ]）", "example": "Im Herbst verlieren die Bäume ihre Blätter.", "exampleCn": "秋天树木落叶。"},
                    {"word": "das Europa", "article": "das", "type": "n.", "ipa": "[ɔɪˈʁoːpa]", "plural": "-", "meaning": "欧洲 (双元音 eu 读 [ɔɪ])", "example": "Deutschland liegt in der Mitte von Europa.", "exampleCn": "德国位于欧洲中心。"},
                    {"word": "der Kaiser", "article": "der", "type": "n.", "ipa": "[ˈkaɪzɐ]", "plural": "-", "meaning": "皇帝 (双元音 ai 读 [aɪ])", "example": "Der Kaiser lebte im Schloss.", "exampleCn": "皇帝住在城堡里。"},
                    {"word": "der Mai", "article": "der", "type": "n.", "ipa": "[maɪ]", "plural": "-", "meaning": "五月 (双元音 ai 读 [aɪ])", "example": "Im Mai blühen viele Blumen.", "exampleCn": "五月鲜花盛开。"},
                    {"word": "der Euro", "article": "der", "type": "n.", "ipa": "[ˈɔɪʁo]", "plural": "-s", "meaning": "欧元 (双元音 eu 读 [ɔɪ])", "example": "Das Buch kostet 15 Euro.", "exampleCn": "这本书售价15欧元。"},
                    {"word": "die Beute", "article": "die", "type": "n.", "ipa": "[ˈbɔɪtə]", "plural": "-n", "meaning": "猎物，收获 (双元音 eu 读 [ɔɪ])", "example": "Der Löwe sucht nach Beute.", "exampleCn": "狮子正在寻找猎物。"},
                    {"word": "der Freund", "article": "der", "type": "n.", "ipa": "[fʁɔɪnt]", "plural": "-e", "meaning": "朋友 (双元音 eu 读 [ɔɪ])", "example": "Er ist mein bester Freund.", "exampleCn": "他是我最好的朋友。"},
                    {"word": "das Kleid", "article": "das", "type": "n.", "ipa": "[klaɪt]", "plural": "-er", "meaning": "连衣裙 (双元音 ei 读 [aɪ])", "example": "Sie trägt ein schönes Kleid.", "exampleCn": "她穿着一件漂亮的裙子。"},
                    {"word": "das Eis", "article": "das", "type": "n.", "ipa": "[aɪs]", "plural": "-", "meaning": "冰，冰淇淋 (双元音 ei 读 [aɪ])", "example": "Die Kinder essen gerne Eis.", "exampleCn": "孩子们喜欢吃冰淇淋。"},
                    {"word": "die Zeit", "article": "die", "type": "n.", "ipa": "[tsaɪt]", "plural": "-en", "meaning": "时间 (双元音 ei 读 [aɪ])", "example": "Ich habe heute leider keine Zeit.", "exampleCn": "我今天可惜没有时间。"},
                    {"word": "das Auge", "article": "das", "type": "n.", "ipa": "[ˈaʊɡə]", "plural": "-n", "meaning": "眼睛 (双元音 au 读 [aʊ])", "example": "Er hat blaue Augen.", "exampleCn": "他有一双蓝眼睛。"},
                    {"word": "das Gebäude", "article": "das", "type": "n.", "ipa": "[ɡəˈbɔɪdə]", "plural": "-", "meaning": "建筑物 (双元音 äu 读 [ɔɪ])", "example": "Das ist ein sehr modernes Gebäude.", "exampleCn": "这是一座非常现代化的建筑。"}
                ],
                "quiz": []
            },
            {
                "id": "A0_L4",
                "title": "第4课：特殊辅音组合与软硬音 (Konsonanten: ch, sp, st, sch, ig)",
                "summary": "彻底掌握 ch 软硬音判定、词首 sp/st 吐气破擦音与词尾弱化音",
                "grammar": {},
                "words": [
                    {"word": "der Sport", "article": "der", "type": "n.", "ipa": "[ʃpɔʁt]", "plural": "-", "meaning": "体育，运动 (词首 sp 读 [ʃp])", "example": "Ich treibe jeden Tag Sport.", "exampleCn": "我每天做运动。"},
                    {"word": "die Stadt", "article": "die", "type": "n.", "ipa": "[ʃtat]", "plural": "Städte", "meaning": "城市 (词首 st 读 [ʃt])", "example": "Berlin ist eine sehr lebendige Stadt.", "exampleCn": "柏林是一座非常有活力的城市。"},
                    {"word": "das Buch", "article": "das", "type": "n.", "ipa": "[buːx]", "plural": "Bücher", "meaning": "书本 (硬音 ch 读 [x])", "example": "Ich lese ein interessantes Buch.", "exampleCn": "我正在读一本有趣的书。"},
                    {"word": "ich", "article": "", "type": "pron.", "ipa": "[ɪç]", "plural": "", "meaning": "我 (软音 ch 读 [ç])", "example": "Ich lerne gerne Deutsch.", "exampleCn": "我喜欢学习德语。"},
                    {"word": "die Schule", "article": "die", "type": "n.", "ipa": "[ˈʃuːlə]", "plural": "-n", "meaning": "学校 (sch 读 [ʃ])", "example": "Die Kinder gehen um acht Uhr in die Schule.", "exampleCn": "孩子们八点去学校。"},
                    {"word": "wichtig", "article": "", "type": "adj.", "ipa": "[ˈvɪçtɪç]", "plural": "", "meaning": "重要的 (词尾 -ig 读 [ɪç])", "example": "Das ist eine wichtige Regel.", "exampleCn": "这是一条重要规则。"},
                    {"word": "das Fenster", "article": "das", "type": "n.", "ipa": "[ˈfɛnstɐ]", "plural": "-", "meaning": "窗户 (词中 st 读 [st])", "example": "Bitte öffnen Sie das Fenster!", "exampleCn": "请打开窗户！"},
                    {"word": "das Wasser", "article": "das", "type": "n.", "ipa": "[ˈvasɐ]", "plural": "-", "meaning": "水 (w 读 [v])", "example": "Wasser ist gesund.", "exampleCn": "水是有益健康的。"},
                    {"word": "der Vogel", "article": "der", "type": "n.", "ipa": "[ˈfoːɡl̩]", "plural": "Vögel", "meaning": "鸟 (本族词 v 读 [f])", "example": "Der Vogel singt im Baum.", "exampleCn": "鸟儿在树上歌唱。"},
                    {"word": "die Vase", "article": "die", "type": "n.", "ipa": "[ˈvaːzə]", "plural": "-n", "meaning": "花瓶 (外来词 v 读 [v])", "example": "Die Blumen stehen in der Vase.", "exampleCn": "花插在花瓶里。"},
                    {"word": "die Straße", "article": "die", "type": "n.", "ipa": "[ˈʃtʁaːsə]", "plural": "-n", "meaning": "街道 (词首 st 读 [ʃt])", "example": "Wir wohnen in dieser Straße.", "exampleCn": "我们住在这条街上。"},
                    {"word": "der Spielplatz", "article": "der", "type": "n.", "ipa": "[ˈʃpiːlˌplats]", "plural": "Spielplätze", "meaning": "游乐场 (词首 sp 读 [ʃp])", "example": "Kinder spielen auf dem Spielplatz.", "exampleCn": "孩子们在游乐场玩耍。"},
                    {"word": "die Kirche", "article": "die", "type": "n.", "ipa": "[ˈkɪʁçə]", "plural": "-n", "meaning": "教堂 (辅音 r 后的 ch 读软音 [ç])", "example": "Die alte Kirche steht im Zentrum.", "exampleCn": "古老教堂位于市中心。"},
                    {"word": "die Sprache", "article": "die", "type": "n.", "ipa": "[ˈʃpʁaːxə]", "plural": "-n", "meaning": "语言 (a 后的 ch 读硬音 [x])", "example": "Deutsch ist eine schöne Sprache.", "exampleCn": "德语是一门优美的语言。"},
                    {"word": "die Königin", "article": "die", "type": "n.", "ipa": "[ˈkøːnɪɡɪn]", "plural": "-nen", "meaning": "女王，王后 (词尾 -ig 读 [ɪç])", "example": "Die Königin winkt den Menschen zu.", "exampleCn": "女王向人们招手致意。"},
                    {"word": "das Licht", "article": "das", "type": "n.", "ipa": "[lɪçt]", "plural": "-er", "meaning": "光，灯光 (i 后的 ch 读软音 [ç])", "example": "Bitte machen Sie das Licht an!", "exampleCn": "请开灯！"},
                    {"word": "die Nacht", "article": "die", "type": "n.", "ipa": "[naxt]", "plural": "Nächte", "meaning": "夜晚 (a 后的 ch 读硬音 [x])", "example": "Gute Nacht und schlaf gut!", "exampleCn": "晚安，做个好梦！"},
                    {"word": "das Schwein", "article": "das", "type": "n.", "ipa": "[ʃvaɪn]", "plural": "-e", "meaning": "猪 (sch 读 [ʃ])", "example": "Schwein haben bedeutet Glück haben.", "exampleCn": "德语里‘有猪’意为走好运。"},
                    {"word": "der Fleiß", "article": "der", "type": "n.", "ipa": "[flaɪs]", "plural": "-", "meaning": "勤奋 (双元音后用 ß)", "example": "Ohne Fleiß kein Preis.", "exampleCn": "一份耕耘，一份收获（不劳则无获）。"},
                    {"word": "der Tag", "article": "der", "type": "n.", "ipa": "[taːk]", "plural": "-e", "meaning": "白天，天 (词尾 g 清化读 [k])", "example": "Schönen Tag noch!", "exampleCn": "祝您度过愉快的一天！"}
                ],
                "quiz": []
            },
            {
                "id": "A0_L5",
                "title": "第5课：德语重音、词尾弱化与综合拼读实战 (Betonung & Intonation)",
                "summary": "掌握德语单词重音规律、词尾 -e / -en / -er 的弱化发音与基础句调",
                "grammar": {},
                "words": [
                    {"word": "der Vater", "article": "der", "type": "n.", "ipa": "[ˈfaːtɐ]", "plural": "Väter", "meaning": "父亲 (词首重音，词尾 -er 弱化)", "example": "Mein Vater ist Ingenieur.", "exampleCn": "我父亲是工程师。"},
                    {"word": "bekommen", "article": "", "type": "v.", "ipa": "[bəˈkɔmən]", "plural": "bekommt, bekam, bekommen", "meaning": "得到，获得 (不可分前缀不重读)", "example": "Ich bekomme morgen einen Brief.", "exampleCn": "我明天会收到一封信。"},
                    {"word": "verstehen", "article": "", "type": "v.", "ipa": "[fɛɐ̯ˈʃteːən]", "plural": "versteht, verstand, verstanden", "meaning": "理解，听懂 (不可分前缀不重读)", "example": "Verstehen Sie mich gut?", "exampleCn": "您听得懂我的话吗？"},
                    {"word": "einkaufen", "article": "", "type": "v.", "ipa": "[ˈaɪnˌkaʊfn̩]", "plural": "kauft ein, kaufte ein, eingekauft", "meaning": "采购，购物 (可分前缀重读)", "example": "Wir kaufen am Samstag ein.", "exampleCn": "我们周六去购物。"},
                    {"word": "die Musik", "article": "die", "type": "n.", "ipa": "[muˈziːk]", "plural": "-", "meaning": "音乐 (外来词末音节重读)", "example": "Ich höre gerne klassische Musik.", "exampleCn": "我喜欢听古典音乐。"},
                    {"word": "der Student", "article": "der", "type": "n.", "ipa": "[ʃtuˈdɛnt]", "plural": "-en", "meaning": "男大学生 (末音节重读)", "example": "Er ist Student an der Universität.", "exampleCn": "他是大学里的大学生。"},
                    {"word": "die Lektion", "article": "die", "type": "n.", "ipa": "[lɛkˈtsi̯oːn]", "plural": "-en", "meaning": "课时，课 (末音节重读)", "example": "Wir beginnen heute mit Lektion 1.", "exampleCn": "我们今天开始学习第1课。"},
                    {"word": "entschuldigen", "article": "", "type": "v.", "ipa": "[ɛntˈʃʊldɪɡn̩]", "plural": "entschuldigt, entschuldigte, entschuldigt", "meaning": "原谅，对不起", "example": "Entschuldigen Sie bitte die Störung!", "exampleCn": "请原谅打扰了！"},
                    {"word": "aufstehen", "article": "", "type": "v.", "ipa": "[ˈaʊfˌʃteːən]", "plural": "steht auf, stand auf, ist aufgestanden", "meaning": "起床 (可分前缀重读)", "example": "Ich stehe früh auf.", "exampleCn": "我起得很早。"},
                    {"word": "die Übung", "article": "die", "type": "n.", "ipa": "[ˈyːbʊŋ]", "plural": "-en", "meaning": "练习，训练", "example": "Übung macht den Meister.", "exampleCn": "熟能生巧（练习造就大师）。"},
                    {"word": "die Frage", "article": "die", "type": "n.", "ipa": "[ˈfʁaːɡə]", "plural": "-n", "meaning": "问题 (是非问句升调，特殊问句降调)", "example": "Ich habe eine kurze Frage.", "exampleCn": "我有一个简短的问题。"},
                    {"word": "die Antwort", "article": "die", "type": "n.", "ipa": "[ˈantvɔʁt]", "plural": "-en", "meaning": "回答，答案 (陈述句句末降调)", "example": "Die Antwort ist vollkommen richtig.", "exampleCn": "回答完全正确。"},
                    {"word": "die Pause", "article": "die", "type": "n.", "ipa": "[ˈpaʊzə]", "plural": "-n", "meaning": "休息，停顿 (发音句间停顿)", "example": "Wir machen jetzt 15 Minuten Pause.", "exampleCn": "我们现在休息15分钟。"},
                    {"word": "der Satz", "article": "der", "type": "n.", "ipa": "[zats]", "plural": "Sätze", "meaning": "句子 (语调基本单位)", "example": "Bilden Sie bitte einen vollständigen Satz!", "exampleCn": "请造一个完整的句子！"},
                    {"word": "die Stimme", "article": "die", "type": "n.", "ipa": "[ˈʃtɪmə]", "plural": "-n", "meaning": "声音，嗓音 (语调抑扬升降)", "example": "Er hat eine sehr angenehme Stimme.", "exampleCn": "他的嗓音非常悦耳动听。"},
                    {"word": "fragen", "article": "", "type": "v.", "ipa": "[ˈfʁaːɡn̩]", "plural": "fragt, fragte, gefragt", "meaning": "问，询问", "example": "Darf ich Sie etwas fragen?", "exampleCn": "我可以请问您一件事吗？"},
                    {"word": "antworten", "article": "", "type": "v.", "ipa": "[ˈantvɔʁtn̩]", "plural": "antwortet, antwortete, geantwortet", "meaning": "回答", "example": "Bitte antworten Sie auf die Frage!", "exampleCn": "请回答这个问题！"},
                    {"word": "betonen", "article": "", "type": "v.", "ipa": "[bəˈtoːnən]", "plural": "betont, betonte, betont", "meaning": "重读，强调 (不可分前缀不重读)", "example": "Welche Silbe muss man betonen?", "exampleCn": "哪个音节需要重读？"},
                    {"word": "der Akzent", "article": "der", "type": "n.", "ipa": "[akˈtsɛnt]", "plural": "-e", "meaning": "口音，重音", "example": "Sie spricht Deutsch ohne Akzent.", "exampleCn": "她说德语没有任何口音。"},
                    {"word": "wunderbar", "article": "", "type": "adj.", "ipa": "[ˈvʊndɐbaːɐ̯]", "plural": "", "meaning": "太棒了，精彩绝伦", "example": "Ihre Aussprache ist wirklich wunderbar!", "exampleCn": "您的发音真的很棒！"}
                ],
                "quiz": []
            }
        ]
    }

    # Inject detailed grammar and comprehensive quiz bank
    for l in data["lessons"]:
        lid = l["id"]
        if lid in A0_GRAMMAR:
            l["grammar"] = A0_GRAMMAR[lid]
        if lid in A0_QUIZZES:
            l["quiz"] = A0_QUIZZES[lid]
            
    return data

if __name__ == "__main__":
    a0 = get_level_a0()
    print(f"Loaded Level A0: {len(a0['lessons'])} lessons")
    for l in a0["lessons"]:
        print(f"  {l['id']}: {len(l['words'])} words, {len(l['quiz'])} quizzes, {len(l['grammar']['sections'])} grammar sections")
