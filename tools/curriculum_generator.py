#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Curriculum Generator for DeutschMeister (Goethe A1-B2 German Learning App)
Generates full CEFR Goethe curriculum: A0, A1, A2, B1, B2.
Includes vocabulary with IPA, articles, plurals, example sentences, audio text,
in-depth grammar explanations with tables, and Goethe-aligned interactive quizzes.
"""

import json
import os
import sys

def get_full_curriculum():
    return {
        "appName": "DeutschMeister",
        "version": "1.0.0",
        "description": "德语从零基础到B2全系统学习与歌德考试备考大纲",
        "levels": [
            {
                "id": "A0",
                "name": "A0 语音与字母发音基石",
                "goetheLevel": "A0 零基础",
                "description": "掌握德语26个字母与4个特殊字母、元音辅音拼读规则与自然发音规律，彻底攻克'见词能读'！",
                "lessons": [
                    {
                        "id": "A0_L1",
                        "title": "字母表与特殊字符 (Alphabet & Sonderzeichen)",
                        "summary": "掌握德语基础字母发音及独有的 ä, ö, ü, ß",
                        "grammar": {
                            "title": "德语字母发音与变元音规则",
                            "sections": [
                                {
                                    "heading": "1. 德语四个特殊字母 (Sonderzeichen)",
                                    "content": "德语特有变元音（Umlaute）和双S（Eszett）：\n"
                                               "• ä [ɛː] / [ɛ]：口型发 [e]，音接近中文“哎”。例如：Äpfel, Käse。\n"
                                               "• ö [øː] / [œ]：先发 [e] 的音，双唇向前突出聚拢呈圆形。例如：Öl, schön。\n"
                                               "• ü [yː] / [ʏ]：先发 [i] 的音，双唇向前突出聚拢呈圆形（类似汉语拼音 ü）。例如：über, Tür。\n"
                                               "• ß [s]：称作 scharfes S，永远发清辅音 [s]，前接长元音或双元音。例如：Straße, heißen。"
                                },
                                {
                                    "heading": "2. 复合元音拼读规律",
                                    "content": "• ei / ey / ai [aɪ]：发音如“爱”，例如：mein, Mai, Arbeit。\n"
                                               "• eu / äu [ɔɪ]：发音如“奥伊”，例如：neu, heute, Häuser。\n"
                                               "• au [aʊ]：发音如“奥”，例如：Haus, Frau, Auto。\n"
                                               "• ie [iː]：长元音 [i:]，例如：sie, Liebe, Bier。"
                                },
                                {
                                    "heading": "3. 关键辅音拼读规则",
                                    "content": "• sp / st 位于词首或前缀后时读 [ʃp] / [ʃt]：Sport [ʃpɔrt], Stadt [ʃtat]。\n"
                                               "• ch 发音规则：在 a, o, u, au 之后读硬音 [x]（如 Bach, Buch）；在其他元音或变元音后读软音 [ç]（如 ich, möchte, Milch）。\n"
                                               "• sch 读 [ʃ]：Schule, schön。\n"
                                               "• w 读 [v]：Wasser, wer。\n"
                                               "• v 在德语本族词中读 [f]（如 Vater, viel），外来词中读 [v]（如 Vase）。\n"
                                               "• r 为小舌颤音 [ʀ] 或舌尖颤音，在词尾常弱化为 [ɐ]（如 Mutter [ˈmʊtɐ], aber [ˈaːbɐ]）。"
                                }
                            ]
                        },
                        "words": [
                            {"word": "das Alphabet", "article": "das", "type": "n.", "ipa": "[alfaˈbeːt]", "plural": "-e", "meaning": "字母表", "example": "Das deutsche Alphabet hat 26 Buchstaben.", "exampleCn": "德语字母表有26个基础字母。"},
                            {"word": "der Buchstabe", "article": "der", "type": "n.", "ipa": "[ˈbuːxˌʃtaːbə]", "plural": "-n", "meaning": "字母", "example": "Wie buchstabiert man diesen Buchstaben?", "exampleCn": "这个字母怎么拼写？"},
                            {"word": "schön", "article": "", "type": "adj.", "ipa": "[ʃøːn]", "plural": "", "meaning": "美丽的，美好的", "example": "Guten Tag! Das Wetter ist heute sehr schön.", "exampleCn": "你好！今天天气非常美好。"},
                            {"word": "heißen", "article": "", "type": "v.", "ipa": "[ˈhaɪsn̩]", "plural": "heißt, hieß, geheißen", "meaning": "名叫，称为", "example": "Ich heiße Anna und komme aus Berlin.", "exampleCn": "我叫安娜，来自柏林。"},
                            {"word": "die Straße", "article": "die", "type": "n.", "ipa": "[ˈʃtʁaːsə]", "plural": "-n", "meaning": "街道，马路", "example": "Ich wohne in der Goethe-Straße.", "exampleCn": "我住在歌德大街。"},
                            {"word": "die Tür", "article": "die", "type": "n.", "ipa": "[tyːɐ̯]", "plural": "-en", "meaning": "门", "example": "Bitte schließen Sie die Tür!", "exampleCn": "请您关上门！"},
                            {"word": "das Haus", "article": "das", "type": "n.", "ipa": "[haʊs]", "plural": "Häuser", "meaning": "房屋，房子", "example": "Das Haus ist neu und groß.", "exampleCn": "这座房子又新又大。"},
                            {"word": "deutsch", "article": "", "type": "adj.", "ipa": "[dɔɪtʃ]", "plural": "", "meaning": "德语的，德国的", "example": "Ich lerne Deutsch für die Goethe-Prüfung.", "exampleCn": "我为了歌德考试学习德语。"}
                        ],
                        "quiz": [
                            {
                                "id": "A0_Q1",
                                "type": "PRONUNCIATION",
                                "question": "单词 'Sport' 中词首字母组合 'sp' 应该发什么音？",
                                "options": ["[sp]", "[ʃp]", "[zp]", "[sk]"],
                                "correctIndex": 1,
                                "explanation": "德语中 sp 位于词首或前缀后时读 [ʃp]，因此 Sport 读作 [ʃpɔrt]。"
                            },
                            {
                                "id": "A0_Q2",
                                "type": "ARTICLE",
                                "question": "请选出 'Straße'（街道）正确的定冠词：",
                                "options": ["der", "die", "das", "dem"],
                                "correctIndex": 1,
                                "explanation": "Straße 是阴性名词，定冠词是 die（die Straße）。以 -e 结尾的名词大多为阴性。"
                            },
                            {
                                "id": "A0_Q3",
                                "type": "VOCAB_MEANING",
                                "question": "变元音字母 'ö' 在单词 'schön' 中的标准发音方法是：",
                                "options": ["发英语的 [o] 音", "口型发 [e]，双唇前凸聚圆", "口型发 [u]，舌位压低", "发中文拼音的 ou 音"],
                                "correctIndex": 1,
                                "explanation": "发 ö 音的诀窍：先保持发 [e]（类似汉语“诶”）的舌位，然后双唇向前用力撅起聚圆即可准确发出 [øː]。"
                            }
                        ]
                    }
                ]
            },
            {
                "id": "A1",
                "name": "A1 入门起步 (Goethe-Zertifikat A1)",
                "goetheLevel": "A1 突破级",
                "description": "达到歌德A1标准：能理解并运用日常熟悉表达与极简单句子，满足日常生活具体需求与自我介绍。",
                "lessons": [
                    {
                        "id": "A1_L1",
                        "title": "第1课：相识与寒暄 (Begrüßung & Vorstellen)",
                        "summary": "掌握人称代词、动词变位基础、sein / haben 及基础疑问句",
                        "grammar": {
                            "title": "人称代词与动词现在时现在变位",
                            "sections": [
                                {
                                    "heading": "1. 规则动词现在时词尾 (Präsens)",
                                    "content": "动词原形通常以 -en 结尾，变位时去掉 -en 加上人称词尾：\n"
                                               "• ich (我): -e  (ich lerne)\n"
                                               "• du (你): -st  (du lernst)\n"
                                               "• er/sie/es (他/她/它): -t  (er lernt)\n"
                                               "• wir (我们): -en  (wir lernen)\n"
                                               "• ihr (你们): -t  (ihr lernt)\n"
                                               "• sie/Sie (他们/您): -en  (sie/Sie lernen)"
                                },
                                {
                                    "heading": "2. 两个最重要的不规则动词：sein (是) 与 haben (有)",
                                    "content": "• sein: ich bin, du bist, er/sie/es ist, wir sind, ihr seid, sie/Sie sind\n"
                                               "• haben: ich habe, du hast, er/sie/es hat, wir haben, ihr habt, sie/Sie haben"
                                },
                                {
                                    "heading": "3. 句型：陈述句与疑问句语序",
                                    "content": "• 陈述句：动词永远占第二位！(Ich lerne heute Deutsch.)\n"
                                               "• 一般疑问句(Ja/Nein-Frage)：动词占第一位！(Lernst du Deutsch? - Ja, ich lerne Deutsch.)\n"
                                               "• 特殊疑问句(W-Frage)：疑问词第一位，动词第二位！(Wie heißen Sie? / Woher kommst du?)"
                                }
                            ]
                        },
                        "words": [
                            {"word": "begrüßen", "article": "", "type": "v.", "ipa": "[bəˈɡʁyːsn̩]", "plural": "begrüßt, begrüßte, begrüßt", "meaning": "问候，打招呼", "example": "Ich begrüße meine neuen Kollegen.", "exampleCn": "我向我的新同事打招呼。"},
                            {"word": "der Name", "article": "der", "type": "n.", "ipa": "[ˈnaːmə]", "plural": "-n", "meaning": "名字，姓名", "example": "Mein Name ist Thomas Müller.", "exampleCn": "我的名字叫托马斯·穆勒。"},
                            {"word": "kommen", "article": "", "type": "v.", "ipa": "[ˈkɔmən]", "plural": "kommt, kam, ist gekommen", "meaning": "来，来自", "example": "Woher kommen Sie? - Ich komme aus China.", "exampleCn": "您来自哪里？- 我来自中国。"},
                            {"word": "wohnen", "article": "", "type": "v.", "ipa": "[ˈvoːnən]", "plural": "wohnt, wohnte, gewohnt", "meaning": "居住", "example": "Wo wohnst du jetzt? - In München.", "exampleCn": "你现在住在哪里？- 在慕尼黑。"},
                            {"word": "sprechen", "article": "", "type": "v.", "ipa": "[ˈʃpʁɛçn̩]", "plural": "spricht, sprach, gesprochen", "meaning": "说，讲（语言）", "example": "Sprichst du Englisch und Deutsch?", "exampleCn": "你说英语和德语吗？"},
                            {"word": "die Sprache", "article": "die", "type": "n.", "ipa": "[ˈʃpʁaːxə]", "plural": "-n", "meaning": "语言", "example": "Deutsch ist eine interessante Sprache.", "exampleCn": "德语是一门有趣的语言。"},
                            {"word": "gut", "article": "", "type": "adj./adv.", "ipa": "[ɡuːt]", "plural": "besser, am besten", "meaning": "好，好的", "example": "Guten Morgen! Wie geht es Ihnen?", "exampleCn": "早上好！您身体好吗？"},
                            {"word": "danke", "article": "", "type": "int.", "ipa": "[ˈdaŋkə]", "plural": "", "meaning": "谢谢", "example": "Danke gut, und Ihnen?", "exampleCn": "很好谢谢，您呢？"}
                        ],
                        "quiz": [
                            {
                                "id": "A1_L1_Q1",
                                "type": "GRAMMAR_FILL",
                                "question": "请选择正确的动词变位：Woher ______ du? - Ich ______ aus Deutschland.",
                                "options": ["kommst / komme", "kommt / komme", "kommen / kommt", "kommst / bin"],
                                "correctIndex": 0,
                                "explanation": "第二人称单数 du 的词尾是 -st (du kommst)；第一人称单数 ich 的词尾是 -e (ich komme)。"
                            },
                            {
                                "id": "A1_L1_Q2",
                                "type": "GRAMMAR_FILL",
                                "question": "请选出正确的 sein 动词形式：Wir ______ Studenten und ihr ______ Lehrer.",
                                "options": ["sind / seid", "seid / sind", "ist / sind", "sind / ist"],
                                "correctIndex": 0,
                                "explanation": "wir 对应的 sein 变位是 sind；ihr 对应的变位是 seid。"
                            },
                            {
                                "id": "A1_L1_Q3",
                                "type": "ARTICLE",
                                "question": "请选出名词 'Name' 的正确阳性定冠词：",
                                "options": ["der", "die", "das", "ein"],
                                "correctIndex": 0,
                                "explanation": "Name 是德语中弱变化的阳性名词：der Name, des Namens, dem Namen。"
                            },
                            {
                                "id": "A1_L1_Q4",
                                "type": "EXAM_REAL",
                                "question": "【歌德A1考题情景】在听力自我介绍中听到：“Ich bin verheiratet und habe zwei Kinder.” 这句话的意思是：",
                                "options": ["我单身，没有孩子。", "我已婚，有两个孩子。", "我已婚，正准备生孩子。", "我离异，有两个兄弟姐妹。"],
                                "correctIndex": 1,
                                "explanation": "verheiratet 意为“已婚”，zwei Kinder 意为“两个孩子”。"
                            }
                        ]
                    },
                    {
                        "id": "A1_L2",
                        "title": "第2课：家庭与称谓 (Familie & Berufe)",
                        "summary": "掌握三性冠词系统(der/die/das)、复数、物主代词与否定词 kein/nicht",
                        "grammar": {
                            "title": "冠词系统与否定词 kein vs nicht",
                            "sections": [
                                {
                                    "heading": "1. 德语核心三性冠词（第一格 Nominativ）",
                                    "content": "• 阳性 (Maskulinum): der Vater (一位父亲: ein Vater)\n"
                                               "• 阴性 (Femininum): die Mutter (一位母亲: eine Mutter)\n"
                                               "• 中性 (Neutrum): das Kind (一个孩子: ein Kind)\n"
                                               "• 复数 (Plural): die Eltern (父母，复数无不定冠词)"
                                },
                                {
                                    "heading": "2. 物主代词 (Possessivartikel)",
                                    "content": "• 第一人称 '我的'：mein Vater (阳), meine Mutter (阴), mein Kind (中), meine Eltern (复)\n"
                                               "• 第二人称 '你的'：dein Vater, deine Mutter, dein Kind, deine Eltern\n"
                                               "• 尊称 '您的'：Ihr Vater, Ihre Mutter, Ihr Kind, Ihre Eltern"
                                },
                                {
                                    "heading": "3. 否定词 kein 与 nicht 的严格区别",
                                    "content": "• kein: 专门否定带有不定冠词或无冠词的名词！(Das ist kein Apfel. Ich habe keine Zeit.)\n"
                                               "• nicht: 否定动词、形容词、副词、带定冠词的名词、人名或整个句子！(Ich arbeite nicht. Das Auto ist nicht teuer.)"
                                }
                            ]
                        },
                        "words": [
                            {"word": "der Vater", "article": "der", "type": "n.", "ipa": "[ˈfaːtɐ]", "plural": "Väter", "meaning": "父亲，爸爸", "example": "Mein Vater arbeitet als Arzt im Krankenhaus.", "exampleCn": "我父亲在医院当医生。"},
                            {"word": "die Mutter", "article": "die", "type": "n.", "ipa": "[ˈmʊtɐ]", "plural": "Mütter", "meaning": "母亲，妈妈", "example": "Meine Mutter ist Lehrerin von Beruf.", "exampleCn": "我母亲的职业是教师。"},
                            {"word": "das Kind", "article": "das", "type": "n.", "ipa": "[kɪnt]", "plural": "Kinder", "meaning": "孩子，小孩", "example": "Das Kind spielt gerne im Park.", "exampleCn": "小孩喜欢在公园里玩耍。"},
                            {"word": "der Beruf", "article": "der", "type": "n.", "ipa": "[bəˈʁuːf]", "plural": "-e", "meaning": "职业，工作", "example": "Was sind Sie von Beruf?", "exampleCn": "您的职业是什么？"},
                            {"word": "die Familie", "article": "die", "type": "n.", "ipa": "[faˈmiːli̯ə]", "plural": "-n", "meaning": "家庭，家族", "example": "Meine Familie lebt in Hamburg.", "exampleCn": "我的家人生活在汉堡。"},
                            {"word": "arbeiten", "article": "", "type": "v.", "ipa": "[ˈaʁbaɪtn̩]", "plural": "arbeitet, arbeitete, gearbeitet", "meaning": "工作，劳动", "example": "Er arbeitet bei Siemens in Berlin.", "exampleCn": "他在柏林的西门子公司工作。"},
                            {"word": "der Arzt", "article": "der", "type": "n.", "ipa": "[aːɐ̯tst]", "plural": "Ärzte", "meaning": "男医生", "example": "Der Arzt untersucht den Patienten.", "exampleCn": "医生正在检查病人。"},
                            {"word": "die Ärztin", "article": "die", "type": "n.", "ipa": "[ˈɛːɐ̯tstɪn]", "plural": "-nen", "meaning": "女医生", "example": "Frau Weber ist eine gute Ärztin.", "exampleCn": "韦伯女士是一位优秀的女医生。"}
                        ],
                        "quiz": [
                            {
                                "id": "A1_L2_Q1",
                                "type": "GRAMMAR_FILL",
                                "question": "请选出正确的否定词填空：Ich trinke heute ______ Kaffee (咖啡无冠词), ich trinke Tee.",
                                "options": ["keinen", "nicht", "nein", "kein"],
                                "correctIndex": 0,
                                "explanation": "Kaffee 是阳性名词（der Kaffee），此处作宾语为第四格（Akkusativ），否定无冠词名词用 keinen。"
                            },
                            {
                                "id": "A1_L2_Q2",
                                "type": "ARTICLE",
                                "question": "请选出名词 'Kind'（孩子）的定冠词：",
                                "options": ["der", "die", "das", "den"],
                                "correctIndex": 2,
                                "explanation": "Kind 是中性名词，定冠词为 das (das Kind, die Kinder)。"
                            },
                            {
                                "id": "A1_L2_Q3",
                                "type": "EXAM_REAL",
                                "question": "【歌德A1笔试读信】信件开头为：'Sehr geehrte Damen und Herren,...' 适用的收信人是：",
                                "options": ["亲密的朋友", "自己的父母", "不认识或正式机构/公司的收信人", "学校的同学"],
                                "correctIndex": 2,
                                "explanation": "'Sehr geehrte Damen und Herren' 是正式书信中收件人姓名不确定时的标准礼貌称呼（相当于“尊敬的女士们、先生们”）。"
                            }
                        ]
                    },
                    {
                        "id": "A1_L3",
                        "title": "第3课：餐饮与购物 (Essen & Einkaufen)",
                        "summary": "掌握第四格(Akkusativ)、情态动词 möchten、价格与数量表达",
                        "grammar": {
                            "title": "第四格（Akkusativ 直接宾语）与情态动词",
                            "sections": [
                                {
                                    "heading": "1. 第四格（Akkusativ）冠词变化",
                                    "content": "四格中【仅阳性】发生明显改变，阴性、中性、复数保持与第一格一致：\n"
                                               "• 阳性：der -> den  |  ein -> einen  |  kein -> keinen  |  mein -> meinen\n"
                                               "• 阴性：die -> die  |  eine -> eine  |  keine -> keine  |  meine -> meine\n"
                                               "• 中性：das -> das  |  ein -> ein    |  kein -> kein    |  mein -> mein\n"
                                               "• 复数：die -> die  |  -- -> --      |  keine -> keine  |  meine -> meine\n"
                                               "例如：Ich kaufe den Apfel (阳). Ich esse eine Banane (阴)."
                                },
                                {
                                    "heading": "2. 想要：möchten 的现在时变位",
                                    "content": "• ich möchte, du möchtest, er/sie/es möchte, wir möchten, ihr möchtet, sie/Sie möchten\n"
                                               "• 句子结构：情态动词占第2位，实义动词原形放在句末！\n"
                                               "例：Ich möchte einen Kaffee trinken."
                                }
                            ]
                        },
                        "words": [
                            {"word": "der Apfel", "article": "der", "type": "n.", "ipa": "[ˈapfl̩]", "plural": "Äpfel", "meaning": "苹果", "example": "Ich esse jeden Tag einen Apfel.", "exampleCn": "我每天吃一个苹果。"},
                            {"word": "das Brot", "article": "das", "type": "n.", "ipa": "[bʁoːt]", "plural": "-e", "meaning": "面包", "example": "Das deutsche Brot schmeckt sehr lecker.", "exampleCn": "德国面包尝起来非常美味。"},
                            {"word": "der Kaffee", "article": "der", "type": "n.", "ipa": "[ˈkafe]", "plural": "-s", "meaning": "咖啡", "example": "Möchten Sie eine Tasse Kaffee trinken?", "exampleCn": "您想喝一杯咖啡吗？"},
                            {"word": "das Wasser", "article": "das", "type": "n.", "ipa": "[ˈvasɐ]", "plural": "Wässer", "meaning": "水，饮用水", "example": "Ein Glas Wasser bitte!", "exampleCn": "请给我一杯水！"},
                            {"word": "kaufen", "article": "", "type": "v.", "ipa": "[ˈkaʊfn̩]", "plural": "kauft, kaufte, gekauft", "meaning": "购买，买", "example": "Wir kaufen Obst und Gemüse im Supermarkt.", "exampleCn": "我们在超市买水果和蔬菜。"},
                            {"word": "kosten", "article": "", "type": "v.", "ipa": "[ˈkɔstn̩]", "plural": "kostet, kostete, gekostet", "meaning": "花费，价值", "example": "Wie viel kostet ein Kilo Tomaten?", "exampleCn": "一公斤西红柿多少钱？"},
                            {"word": "der Supermarkt", "article": "der", "type": "n.", "ipa": "[ˈzuːpɐˌmaʁkt]", "plural": "Supermärkte", "meaning": "超市", "example": "Der Supermarkt öffnet um 8 Uhr.", "exampleCn": "超市早上8点开门。"},
                            {"word": "lecker", "article": "", "type": "adj.", "ipa": "[ˈlɛkɐ]", "plural": "", "meaning": "美味的，好吃的", "example": "Das Essen im Restaurant ist sehr lecker.", "exampleCn": "这家餐馆的饭菜非常可口。"}
                        ],
                        "quiz": [
                            {
                                "id": "A1_L3_Q1",
                                "type": "GRAMMAR_FILL",
                                "question": "请选出正确的第四格冠词填空：Ich möchte ______ Apfel (der Apfel) kaufen.",
                                "options": ["einen", "ein", "eine", "einem"],
                                "correctIndex": 0,
                                "explanation": "Apfel 是阳性名词（der Apfel），在动词 möchte kaufen 的宾语位置变为第四格（Akkusativ），不定冠词用 einen。"
                            },
                            {
                                "id": "A1_L3_Q2",
                                "type": "VOCAB_MEANING",
                                "question": "日常口语中询问价格 'Wie viel kostet das?' 的含义是：",
                                "options": ["这个有多少个？", "这个多少钱？", "这个好吃吗？", "这个是什么时候买的？"],
                                "correctIndex": 1,
                                "explanation": "Wie viel kostet das? 是歌德A1考试中在超市/商店购物场景的最高频核心问句，意为“这个多少钱？”。"
                            }
                        ]
                    },
                    {
                        "id": "A1_L4",
                        "title": "第4课：时间与日常节奏 (Alltag & Uhrzeit)",
                        "summary": "掌握时钟表达、时间介词(um, am, im)、可分动词 (trennbare Verben)",
                        "grammar": {
                            "title": "可分动词与时间介词用法",
                            "sections": [
                                {
                                    "heading": "1. 可分动词 (trennbare Verben)",
                                    "content": "德语特有结构：动词前缀可拆分，在现在时陈述句中，前缀脱落并【移至句子最末尾】！\n"
                                               "常见可分前缀：auf-, an-, ab-, aus-, ein-, mit-, vor-, fern-, zu-\n"
                                               "例1：aufstehen (起床) -> Ich stehe jeden Tag um 7 Uhr auf.\n"
                                               "例2：einkaufen (购物) -> Er kauft am Nachmittag im Supermarkt ein.\n"
                                               "例3：fernsehen (看电视) -> Wir sehen am Abend fern."
                                },
                                {
                                    "heading": "2. 三大核心时间介词归纳",
                                    "content": "• um: 用于钟点具体时刻 (um 8:00 Uhr, um Punkt 9 Uhr)\n"
                                               "• am: 用于星期几、一天中的具体时段 (am Montag, am Morgen, am Abend) *注意：in der Nacht\n"
                                               "• im: 用于月份、季节、年份前 (im Januar, im Sommer, im Jahr 2026)"
                                }
                            ]
                        },
                        "words": [
                            {"word": "aufstehen", "article": "", "type": "v.", "ipa": "[ˈaʊfˌʃteːən]", "plural": "steht auf, stand auf, ist aufgestanden", "meaning": "起床，站起", "example": "Wann stehst du sonntags auf?", "exampleCn": "你周日什么时候起床？"},
                            {"word": "die Uhr", "article": "die", "type": "n.", "ipa": "[uːɐ̯]", "plural": "-en", "meaning": "钟表，点钟", "example": "Wie viel Uhr ist es? - Es ist Viertel vor zehn.", "exampleCn": "现在几点？- 差一刻十点（9点45）。"},
                            {"word": "der Morgen", "article": "der", "type": "n.", "ipa": "[ˈmɔʁɡn̩]", "plural": "-", "meaning": "早晨，上午", "example": "Am Morgen trinke ich immer schwarzen Tee.", "exampleCn": "早晨我总是喝红茶。"},
                            {"word": "anrufen", "article": "", "type": "v.", "ipa": "[ˈanˌʁuːfn̩]", "plural": "ruft an, rief an, angerufen", "meaning": "给……打电话", "example": "Ich rufe dich heute Abend an.", "exampleCn": "我今晚给你打电话。"},
                            {"word": "der Tag", "article": "der", "type": "n.", "ipa": "[taːk]", "plural": "-e", "meaning": "白天，天，日子", "example": "Ich wünsche Ihnen einen schönen Tag!", "exampleCn": "祝您度过愉快的一天！"},
                            {"word": "die Woche", "article": "die", "type": "n.", "ipa": "[ˈvɔxə]", "plural": "-n", "meaning": "星期，周", "example": "Der Deutschkurs dauert vier Wochen.", "exampleCn": "这门德语课持续四周。"},
                            {"word": "frühstücken", "article": "", "type": "v.", "ipa": "[ˈfʁyːˌʃtʏkn̩]", "plural": "frühstückt, frühstückte, gefrühstückt", "meaning": "吃早餐", "example": "Um wie viel Uhr frühstückst du?", "exampleCn": "你几点吃早饭？"},
                            {"word": "abfahren", "article": "", "type": "v.", "ipa": "[ˈapˌfaːʁən]", "plural": "fährt ab, fuhr ab, ist abgefahren", "meaning": "（列车/车辆）出发，发车", "example": "Der Zug nach Frankfurt fährt um 14:30 Uhr ab.", "exampleCn": "开往法兰克福的火车在14:30发车。"}
                        ],
                        "quiz": [
                            {
                                "id": "A1_L4_Q1",
                                "type": "GRAMMAR_FILL",
                                "question": "请选出正确的时间介词填空：Der Zug fährt ______ 8 Uhr ab und wir treffen uns ______ Montag.",
                                "options": ["um / am", "am / um", "im / am", "um / im"],
                                "correctIndex": 0,
                                "explanation": "钟点时刻用介词 um (um 8 Uhr)；星期几用介词 am (am Montag)。"
                            },
                            {
                                "id": "A1_L4_Q2",
                                "type": "GRAMMAR_FILL",
                                "question": "请完成可分动词句子：Er ruft seine Mutter ______.",
                                "options": ["an", "auf", "ein", "ab"],
                                "correctIndex": 0,
                                "explanation": "打电话是 anrufen，可分前缀 an 在主句中必须放在句末：Er ruft seine Mutter an。"
                            }
                        ]
                    },
                    {
                        "id": "A1_L5",
                        "title": "第5课：居住与方位 (Wohnen & Möbel)",
                        "summary": "掌握第三格(Dativ)、静止位置与方向表达、歌德A1全真模拟",
                        "grammar": {
                            "title": "第三格（Dativ 间接宾语）与居住方位介词",
                            "sections": [
                                {
                                    "heading": "1. 第三格（Dativ）冠词变化全表",
                                    "content": "• 阳性：der -> dem  |  ein -> einem  |  kein -> keinem\n"
                                               "• 阴性：die -> der  |  eine -> einer  |  keine -> keiner\n"
                                               "• 中性：das -> dem  |  ein -> einem  |  kein -> keinem\n"
                                               "• 复数：die -> den (+ 名词词尾+n) |  keine -> keinen (+n)\n"
                                               "记忆口诀：阳中同 dem，阴变 der，复数带 den 词尾补 n！"
                                },
                                {
                                    "heading": "2. 固定接第三格的常见介词",
                                    "content": "aus, bei, mit, nach, seit, von, zu (常合写：beim = bei dem, zum = zu dem, zur = zu der)\n"
                                               "例：Ich fahre mit dem Bus (阳). Er wohnt bei seinen Eltern (复)."
                                }
                            ]
                        },
                        "words": [
                            {"word": "die Wohnung", "article": "die", "type": "n.", "ipa": "[ˈvoːnʊŋ]", "plural": "-en", "meaning": "公寓，套房", "example": "Die Wohnung hat drei Zimmer, eine Küche und ein Bad.", "exampleCn": "这套公寓有三个房间、一个厨房和一个卫生间。"},
                            {"word": "das Zimmer", "article": "das", "type": "n.", "ipa": "[ˈtsɪmɐ]", "plural": "-", "meaning": "房间", "example": "Mein Zimmer ist hell und ruhig.", "exampleCn": "我的房间采光好并且很安静。"},
                            {"word": "die Miete", "article": "die", "type": "n.", "ipa": "[ˈmiːtə]", "plural": "-n", "meaning": "房租，租金", "example": "Wie hoch ist die Miete warm im Monat?", "exampleCn": "包含暖气费的月租金是多少？"},
                            {"word": "der Tisch", "article": "der", "type": "n.", "ipa": "[tɪʃ]", "plural": "-e", "meaning": "桌子", "example": "Das Buch liegt auf dem Tisch.", "exampleCn": "书放在桌子上。"},
                            {"word": "der Stuhl", "article": "der", "type": "n.", "ipa": "[ʃtuːl]", "plural": "Stühle", "meaning": "椅子", "example": "Bitte nehmen Sie auf dem Stuhl Platz!", "exampleCn": "请在这把椅子上坐下！"},
                            {"word": "das Bett", "article": "das", "type": "n.", "ipa": "[bɛt]", "plural": "-en", "meaning": "床", "example": "Das Bett ist sehr bequem.", "exampleCn": "这张床非常舒适。"},
                            {"word": "der Schrank", "article": "der", "type": "n.", "ipa": "[ʃʁaŋk]", "plural": "Schränke", "meaning": "柜子，衣柜", "example": "Die Kleidung hängt im Schrank.", "exampleCn": "衣服挂在衣柜里。"},
                            {"word": "die Küche", "article": "die", "type": "n.", "ipa": "[ˈkʏçə]", "plural": "-n", "meaning": "厨房", "example": "Wir kochen gemeinsam in der Küche.", "exampleCn": "我们一起在厨房做饭。"}
                        ],
                        "quiz": [
                            {
                                "id": "A1_L5_Q1",
                                "type": "GRAMMAR_FILL",
                                "question": "介词 'mit' 固定后接第三格（Dativ），请选出正确形式：Ich fahre mit ______ (der Bus) zur Arbeit.",
                                "options": ["dem Bus", "den Bus", "der Bus", "des Busses"],
                                "correctIndex": 0,
                                "explanation": "der Bus 在第三格中变为 dem Bus。mit dem Bus 表示“乘公交车”。"
                            },
                            {
                                "id": "A1_L5_Q2",
                                "type": "EXAM_REAL",
                                "question": "【歌德A1阶段真题模拟】租房广告写道：“3-Zimmer-Wohnung, 75 qm, 800 Euro Kaltmiete, frei ab 01.11.” 这里的 'Kaltmiete' 含义是：",
                                "options": ["包含冬季供暖费的暖租", "不含供暖与物业附加杂费的净租金（冷租）", "押金", "中介费"],
                                "correctIndex": 1,
                                "explanation": "德国租房核心词汇：Kaltmiete 为“冷租”（纯租金，不含水暖杂费）；Warmmiete 为“暖租”（含供暖及物业费）。"
                            }
                        ]
                    }
                ]
            },
            {
                "id": "A2",
                "name": "A2 基础进阶 (Goethe-Zertifikat A2)",
                "goetheLevel": "A2 初级运用",
                "description": "达到歌德A2标准：能理解大部分与切身利益相关的句子与高频词汇，能简单直接交流日常习惯任务，完成现在完成时与从句表达。",
                "lessons": [
                    {
                        "id": "A2_L1",
                        "title": "第1课：旅行与回忆 (Reisen & Urlaub)",
                        "summary": "掌握现在完成时 (Perfekt: haben/sein + Partizip II) 及过去事件叙述",
                        "grammar": {
                            "title": "德语现在完成时 (Perfekt) 构成全解析",
                            "sections": [
                                {
                                    "heading": "1. 现在完成时基本框架",
                                    "content": "现在完成时是德语口语和日常书信中表达【过去发生事情】的最核心时态！\n"
                                               "结构：助动词 haben / sein（变位占第2位） + 过去分词 Partizip II（放句末）！"
                                },
                                {
                                    "heading": "2. 助动词用 haben 还是 sein？",
                                    "content": "• 绝大部分动词用 haben（包括所有及物动词）：\n"
                                               "  Ich habe ein Buch gekauft. / Wir haben Deutsch gelernt.\n"
                                               "• 只有两类动词用 sein：\n"
                                               "  1. 表示【位置移动】的不及物动词：gehen, fahren, fliegen, kommen, reisen...\n"
                                               "  2. 表示【状态改变】的不及物动词及特殊动词：aufstehen, einschlafen, werden, sein, bleiben...\n"
                                               "  例：Er ist nach Berlin gefahren. / Sie ist gestern zu Hause geblieben."
                                },
                                {
                                    "heading": "3. 规则与不规则过去分词 (Partizip II)",
                                    "content": "• 规则动词：ge- + 词干 + -(e)t  (lernen -> gelernt, machen -> gemacht)\n"
                                               "• 可分动词：前缀 + ge- + 词干 + -t/-en (einkaufen -> eingekauft, abfahren -> abgefahren)\n"
                                               "• -ieren 结尾动词：不加 ge-，以 -t 结尾 (studieren -> studiert, reparieren -> repariert)"
                                }
                            ]
                        },
                        "words": [
                            {"word": "die Reise", "article": "die", "type": "n.", "ipa": "[ˈʁaɪzə]", "plural": "-n", "meaning": "旅行，旅程", "example": "Gute Reise! Viel Spaß in Deutschland!", "exampleCn": "旅途愉快！在德国玩得开心！"},
                            {"word": "reisen", "article": "", "type": "v.", "ipa": "[ˈʁaɪzn̩]", "plural": "reist, reiste, ist gereist", "meaning": "旅行，出游", "example": "Im Sommer bin ich nach Italien gereist.", "exampleCn": "夏天我去了意大利旅行。"},
                            {"word": "der Urlaub", "article": "der", "type": "n.", "ipa": "[ˈuːɐ̯laʊp]", "plural": "-e", "meaning": "假期，休假", "example": "Ich habe zwei Wochen Urlaub im August.", "exampleCn": "我在八月份有两周的假期。"},
                            {"word": "besuchen", "article": "", "type": "v.", "ipa": "[bəˈzuːxn̩]", "plural": "besucht, besuchte, besucht", "meaning": "拜访，参观", "example": "Gestern habe ich ein Museum in Wien besucht.", "exampleCn": "昨天我参观了维也纳的一家博物馆。"},
                            {"word": "das Flugzeug", "article": "das", "type": "n.", "ipa": "[ˈfluːkˌtsɔɪk]", "plural": "-e", "meaning": "飞机", "example": "Das Flugzeug landet pünktlich um 16 Uhr.", "exampleCn": "飞机在16点准时降落。"},
                            {"word": "der Koffer", "article": "der", "type": "n.", "ipa": "[ˈkɔfɐ]", "plural": "-", "meaning": "行李箱", "example": "Ich muss noch meinen Koffer packen.", "exampleCn": "我还得收拾我的行李箱。"},
                            {"word": "das Hotel", "article": "das", "type": "n.", "ipa": "[hoˈtɛl]", "plural": "-s", "meaning": "酒店，宾馆", "example": "Wir haben ein Doppelzimmer im Hotel gebucht.", "exampleCn": "我们在酒店预订了一间双人房。"},
                            {"word": "bleiben", "article": "", "type": "v.", "ipa": "[ˈblaɪbn̩]", "plural": "bleibt, blieb, ist geblieben", "meaning": "停留，保持", "example": "Wie lange sind Sie in München geblieben?", "exampleCn": "您在慕尼黑停留了多久？"}
                        ],
                        "quiz": [
                            {
                                "id": "A2_L1_Q1",
                                "type": "GRAMMAR_FILL",
                                "question": "请选出正确的完成时助动词：Er ______ gestern mit dem Zug nach München gefahren.",
                                "options": ["ist", "hat", "wird", "war"],
                                "correctIndex": 0,
                                "explanation": "fahren 属于表示位置位移的不及物动词，其完成时助动词必须使用 sein (Er ist gefahren)。"
                            },
                            {
                                "id": "A2_L1_Q2",
                                "type": "GRAMMAR_FILL",
                                "question": "以 -ieren 结尾的外来词动词（如 reparieren 维修），其过去分词规则是：",
                                "options": ["gerepariert", "repariert", "gereparieren", "reparieren"],
                                "correctIndex": 1,
                                "explanation": "德语中以 -ieren 结尾的动词构成过去分词时不加前缀 ge-，词尾加 -t：repariert。"
                            },
                            {
                                "id": "A2_L1_Q3",
                                "type": "EXAM_REAL",
                                "question": "【歌德A2真题】朋友发信息写道：“Ich habe den Flug verpasst! Kannst du mich vom Bahnhof abholen?” 朋友遇到了什么状况？",
                                "options": ["他退了飞机票", "他错过了航班，想让你去火车站接他", "他已经登机了", "他的行李丢失了"],
                                "correctIndex": 1,
                                "explanation": "verpassen 意为“错过，耽误”；den Flug verpasst 意为“错过了航班”；vom Bahnhof abholen 意为“去火车站接人”。"
                            }
                        ]
                    },
                    {
                        "id": "A2_L2",
                        "title": "第2课：健康与身体 (Gesundheit & Körper)",
                        "summary": "掌握情态动词(sollen, müssen, dürfen)、反身代词与反身动词 (Reflexivpronomen)",
                        "grammar": {
                            "title": "情态动词精讲与反身动词结构",
                            "sections": [
                                {
                                    "heading": "1. 核心情态动词语义区分",
                                    "content": "• müssen (必须，出于客观规律/必要性): Der Patient muss die Medizin nehmen.\n"
                                               "• sollen (应该，转达他人医嘱/建议): Der Arzt sagt, ich soll viel Wasser trinken.\n"
                                               "• dürfen (允许，有权利): Hier darf man nicht rauchen (禁止吸烟).\n"
                                               "• können (能够，有能力): Ich kann heute nicht zur Arbeit kommen."
                                },
                                {
                                    "heading": "2. 反身代词与反身动词 (Reflexive Verben)",
                                    "content": "动作作用于主体自身，伴随反身代词 sich：\n"
                                               "• ich freue mich, du freust dich, er/sie/es freut sich, wir freuen uns, ihr freut euch, sie/Sie freuen sich\n"
                                               "例：Ich fühle mich heute nicht gut. (我今天感觉不太舒服。)"
                                }
                            ]
                        },
                        "words": [
                            {"word": "die Gesundheit", "article": "die", "type": "n.", "ipa": "[ɡəˈzʊnthaɪt]", "plural": "-", "meaning": "健康", "example": "Gesundheit ist das Wichtigste im Leben.", "exampleCn": "健康是生命中最重要的事情。"},
                            {"word": "der Schmerz", "article": "der", "type": "n.", "ipa": "[ʃmɛʁts]", "plural": "-en", "meaning": "疼痛，痛", "example": "Ich habe seit drei Tagen starke Kopfschmerzen.", "exampleCn": "我头痛得很厉害已经三天了。"},
                            {"word": "das Fieber", "article": "das", "type": "n.", "ipa": "[ˈfiːbɐ]", "plural": "-", "meaning": "发烧，发热", "example": "Das Kind hat hohes Fieber und bleibt im Bett.", "exampleCn": "孩子发高烧，正卧床休息。"},
                            {"word": "die Medizin", "article": "die", "type": "n.", "ipa": "[mediˈtsiːn]", "plural": "-en", "meaning": "药，药物；医学", "example": "Nehmen Sie diese Medizin dreimal täglich nach dem Essen.", "exampleCn": "这种药请您每天饭后服用三次。"},
                            {"word": "der Termin", "article": "der", "type": "n.", "ipa": "[tɛʁˈmiːn]", "plural": "-e", "meaning": "预约，约定时间", "example": "Ich möchte einen Termin beim Arzt vereinbaren.", "exampleCn": "我想预约看医生。"},
                            {"word": "fehlen", "article": "", "type": "v.", "ipa": "[ˈfeːlən]", "plural": "fehlt, fehlte, gefehlt", "meaning": "缺少；觉得哪儿不适", "example": "Was fehlt Ihnen denn? - Mein Bauch tut weh.", "exampleCn": "您哪儿不舒服？- 我肚子疼。"},
                            {"word": "sich ausruhen", "article": "", "type": "v.", "ipa": "[zɪç ˈaʊsˌʁuːən]", "plural": "ruht sich aus, ruhte sich aus, ausgeruht", "meaning": "休息，调养", "example": "Sie müssen sich am Wochenende gut ausruhen.", "exampleCn": "您周末必须好好休息。"},
                            {"word": "die Apotheke", "article": "die", "type": "n.", "ipa": "[apoˈteːkə]", "plural": "-n", "meaning": "药店，药房", "example": "Ich hole das Medikament aus der Apotheke ab.", "exampleCn": "我去药店取药。"}
                        ],
                        "quiz": [
                            {
                                "id": "A2_L2_Q1",
                                "type": "GRAMMAR_FILL",
                                "question": "医生给出嘱咐：“您应当卧床休息三天。”请选出正确的德语句子：",
                                "options": [
                                    "Sie sollen drei Tage im Bett bleiben.",
                                    "Sie dürfen nicht im Bett bleiben.",
                                    "Sie wollen drei Tage im Bett bleiben.",
                                    "Sie können kein Bett haben."
                                ],
                                "correctIndex": 0,
                                "explanation": "转述医生/权威的嘱咐和要求使用情态动词 sollen (Sie sollen im Bett bleiben)。"
                            },
                            {
                                "id": "A2_L2_Q2",
                                "type": "VOCAB_MEANING",
                                "question": "看病就医时医生常问：“Was fehlt Ihnen?” 这句话的标准含义是：",
                                "options": ["您叫什么名字？", "您带病历本了吗？", "您哪里不舒服？有什么症状？", "您挂号了吗？"],
                                "correctIndex": 2,
                                "explanation": "德语就诊核心问答：Was fehlt Ihnen? 是德语医生问诊的标准固定表达，等同于“您哪儿不适？”。"
                            }
                        ]
                    },
                    {
                        "id": "A2_L3",
                        "title": "第3课：城市交通与静三动四 (Stadt & Wechselpräpositionen)",
                        "summary": "彻底掌握9大二位介词（静三动四法则）与城市出行问路",
                        "grammar": {
                            "title": "九大二位介词：静三动四核心突破",
                            "sections": [
                                {
                                    "heading": "1. 九大二位介词 (Wechselpräpositionen)",
                                    "content": "an (紧贴表面), auf (在...上方接触), in (在...里面), über (在...正上方悬空), unter (在...下方), vor (在...前面), hinter (在...后面), neben (在...旁边), zwischen (在...两者之间)"
                                },
                                {
                                    "heading": "2. 静三动四黄金铁律",
                                    "content": "• 静态位置 (Wo? 问在哪里，强调无位置改变的静止状态) -> 接【第三格 Dativ】！\n"
                                               "  例：Das Buch liegt auf dem Tisch (der Tisch -> dem Tisch).\n"
                                               "  例：Das Bild hängt an der Wand (die Wand -> der Wand).\n"
                                               "• 动态位移 (Wohin? 问去哪里，强调有方向有位移的目标动作) -> 接【第四格 Akkusativ】！\n"
                                               "  例：Ich lege das Buch auf den Tisch (der Tisch -> den Tisch).\n"
                                               "  例：Er hängt das Bild an die Wand (die Wand -> die Wand)."
                                },
                                {
                                    "heading": "3. 四组核心成对动词（摆放 vs 处于）",
                                    "content": "• 放置动词（动作，及物，接4格宾语 + 介词4格）：legen (平放), stellen (竖放), hängen (挂上), setzen (坐下)\n"
                                               "• 状态动词（静止，不及物，接介词3格）：liegen (平躺), stehen (竖立), hängen (悬挂), sitzen (坐着)"
                                }
                            ]
                        },
                        "words": [
                            {"word": "die Stadt", "article": "die", "type": "n.", "ipa": "[ʃtat]", "plural": "Städte", "meaning": "城市", "example": "Berlin ist die größte Stadt Deutschlands.", "exampleCn": "柏林是德国最大的城市。"},
                            {"word": "der Bahnhof", "article": "der", "type": "n.", "ipa": "[ˈbaːnˌhoːf]", "plural": "Bahnhöfe", "meaning": "火车站", "example": "Entschuldigung, wie komme ich zum Bahnhof?", "exampleCn": "劳驾，去火车站怎么走？"},
                            {"word": "die Haltestelle", "article": "die", "type": "n.", "ipa": "[ˈhaltəˌʃtɛlə]", "plural": "-n", "meaning": "车站，停靠站", "example": "Der Bus hält an der nächsten Haltestelle.", "exampleCn": "公共汽车在下一站停靠。"},
                            {"word": "die Ampel", "article": "die", "type": "n.", "ipa": "[ˈampl̩]", "plural": "-n", "meaning": "红绿灯，交通信号灯", "example": "An der Ampel biegen Sie bitte rechts ab.", "exampleCn": "在红绿灯处请您向右转。"},
                            {"word": "stellen", "article": "", "type": "v.", "ipa": "[ˈʃtɛlən]", "plural": "stellt, stellte, gestellt", "meaning": "竖放，竖立放置", "example": "Stellen Sie die Flasche bitte auf den Tisch!", "exampleCn": "请把瓶子竖放在桌子上！"},
                            {"word": "stehen", "article": "", "type": "v.", "ipa": "[ˈʃteːən]", "plural": "steht, stand, hat gestanden", "meaning": "竖立着，站立", "example": "Die Flasche steht auf dem Tisch.", "exampleCn": "瓶子立在桌子上。"},
                            {"word": "geradeaus", "article": "", "type": "adv.", "ipa": "[ɡəʁaːdəˈʔaʊs]", "plural": "", "meaning": "径直，一直向前", "example": "Gehen Sie immer geradeaus, dann nach links.", "exampleCn": "一直往前走，然后向左拐。"},
                            {"word": "die Kreuzung", "article": "die", "type": "n.", "ipa": "[ˈkʁɔɪtsʊŋ]", "plural": "-en", "meaning": "十字路口", "example": "An der zweiten Kreuzung sehen Sie die Bank.", "exampleCn": "在第二个十字路口您就能看到银行。"}
                        ],
                        "quiz": [
                            {
                                "id": "A2_L3_Q1",
                                "type": "GRAMMAR_FILL",
                                "question": "【静三动四判定】Ich stelle die Lampe in ______ (die Ecke, 动态放入角落).",
                                "options": ["die Ecke", "der Ecke", "den Ecke", "dem Ecke"],
                                "correctIndex": 0,
                                "explanation": "stellen 是动作（把某物竖放移向某处），表示方向和位移，二位介词后必须接第四格（Akkusativ）：die Ecke 保持不变。"
                            },
                            {
                                "id": "A2_L3_Q2",
                                "type": "GRAMMAR_FILL",
                                "question": "【静三动四判定】Die Lampe steht in ______ (die Ecke, 静态立在角落).",
                                "options": ["der Ecke", "die Ecke", "dem Ecke", "den Ecken"],
                                "correctIndex": 0,
                                "explanation": "stehen 是静止状态（某物立在那里），二位介词后接第三格（Dativ）：阴性名词 die Ecke 变为 der Ecke。"
                            }
                        ]
                    },
                    {
                        "id": "A2_L4",
                        "title": "第4课：职场交流与复合从句 (Arbeit & Nebensätze)",
                        "summary": "掌握三大基础从句连词 (weil, dass, wenn) 及动词尾置语序规则",
                        "grammar": {
                            "title": "德语副句（从句 Nebensatz）核心语序铁律",
                            "sections": [
                                {
                                    "heading": "1. 从句动词置底原则 (Verb am Ende)",
                                    "content": "德语从句最核心也是最严苛的规则：\n"
                                               "在从属连词引导的从句中，【变位动词必须放在从句的最后一个位置】！\n"
                                               "如果从句中有助动词/情态动词，变位的助动词/情态动词放在最最后面！"
                                },
                                {
                                    "heading": "2. 三大歌德A2核心从属连词",
                                    "content": "• weil (因为，引导原因从句):\n"
                                               "  Ich lerne Deutsch, weil ich in Deutschland studieren will.\n"
                                               "• dass (表宾语陈述，相当于 that 从句):\n"
                                               "  Ich glaube, dass er heute pünktlich kommt.\n"
                                               "• wenn (如果/当...时候，引导条件或时间从句):\n"
                                               "  Wenn das Wetter schön ist, machen wir einen Ausflug."
                                }
                            ]
                        },
                        "words": [
                            {"word": "die Bewerbung", "article": "die", "type": "n.", "ipa": "[bəˈvɛʁbʊŋ]", "plural": "-en", "meaning": "求职申请，应聘", "example": "Ich habe meine Bewerbung per E-Mail geschickt.", "exampleCn": "我已经通过电子邮件发送了我的求职申请。"},
                            {"word": "der Kollege", "article": "der", "type": "n.", "ipa": "[kɔˈleːɡə]", "plural": "-n", "meaning": "男同事", "example": "Mein Kollege hilft mir bei dem neuen Projekt.", "exampleCn": "我的同事在这个新项目中协助我。"},
                            {"word": "der Chef", "article": "der", "type": "n.", "ipa": "[ʃɛf]", "plural": "-s", "meaning": "上司，老板", "example": "Der Chef leitet die Besprechung.", "exampleCn": "老板正在主持会议。"},
                            {"word": "das Büro", "article": "das", "type": "n.", "ipa": "[byˈʁoː]", "plural": "-s", "meaning": "办公室", "example": "Unser Büro befindet sich im Stadtzentrum.", "exampleCn": "我们的办公室位于市中心。"},
                            {"word": "die Besprechung", "article": "die", "type": "n.", "ipa": "[bəˈʃpʁɛçʊŋ]", "plural": "-en", "meaning": "会议，商讨", "example": "Die Besprechung beginnt um Punkt 10 Uhr.", "exampleCn": "会议在10点整开始。"},
                            {"word": "die Erfahrung", "article": "die", "type": "n.", "ipa": "[ɛɐ̯ˈfaːʁʊŋ]", "plural": "-en", "meaning": "经验，阅历", "example": "Sie hat bereits viel Erfahrung im Marketing.", "exampleCn": "她在市场营销领域已经有丰富的经验。"},
                            {"word": "verdienen", "article": "", "type": "v.", "ipa": "[fɛɐ̯ˈdiːnən]", "plural": "verdient, verdiente, verdient", "meaning": "挣钱，赚得；值得", "example": "Wie viel verdient ein Ingenieur in Deutschland?", "exampleCn": "在德国一名工程师能挣多少钱？"},
                            {"word": "kündigen", "article": "", "type": "v.", "ipa": "[ˈkʏndɪɡn̩]", "plural": "kündigt, kündigte, gekündigt", "meaning": "解约，辞职", "example": "Er möchte seinen Vertrag kündigen.", "exampleCn": "他想解除他的合同。"}
                        ],
                        "quiz": [
                            {
                                "id": "A2_L4_Q1",
                                "type": "GRAMMAR_FILL",
                                "question": "请选出语序完全正确的从句句子：",
                                "options": [
                                    "Ich lerne Deutsch, weil ich will in Berlin arbeiten.",
                                    "Ich lerne Deutsch, weil ich in Berlin arbeiten will.",
                                    "Ich lerne Deutsch, weil in Berlin ich arbeiten will.",
                                    "Ich lerne Deutsch, weil will ich in Berlin arbeiten."
                                ],
                                "correctIndex": 1,
                                "explanation": "在 weil 引导的从句中，变位的情态动词 will 必须放在从句句末，实义动词 arbeiten 在倒数第二位：weil ich in Berlin arbeiten will。"
                            },
                            {
                                "id": "A2_L4_Q2",
                                "type": "GRAMMAR_FILL",
                                "question": "请选出引导词：Er hat mir gesagt, ______ er morgen keine Zeit hat.",
                                "options": ["dass", "weil", "wenn", "denn"],
                                "correctIndex": 0,
                                "explanation": "表达“他说他明天没时间”，宾语从句使用引导词 dass。"
                            }
                        ]
                    },
                    {
                        "id": "A2_L5",
                        "title": "第5课：比较与偏好 (Vergleich & Vorlieben)",
                        "summary": "掌握形容词比较级与最高级 (Komparativ & Superlativ)、歌德A2模拟考",
                        "grammar": {
                            "title": "形容词比较级与最高级规则",
                            "sections": [
                                {
                                    "heading": "1. 规则变化规律",
                                    "content": "• 原级 (Positiv): schnell (快)\n"
                                               "• 比较级 (Komparativ): 词尾加 -er + als (比...更) -> schneller als (比...更快)\n"
                                               "• 最高级 (Superlativ): am + 词尾 -(e)sten -> am schnellsten (最快)"
                                },
                                {
                                    "heading": "2. 单音节元音变音 (a->ä, o->ö, u->ü)",
                                    "content": "alt -> älter -> am ältesten\ngroß -> größer -> am größten\nwarm -> wärmer -> am wärmsten"
                                },
                                {
                                    "heading": "3. 四大极高频不规则形容词（歌德必考！）",
                                    "content": "• gut -> besser -> am besten (好)\n"
                                               "• viel -> mehr -> am meisten (多)\n"
                                               "• gern -> lieber -> am liebsten (喜欢)\n"
                                               "• hoch -> höher -> am höchsten (高)"
                                }
                            ]
                        },
                        "words": [
                            {"word": "schnell", "article": "", "type": "adj.", "ipa": "[ʃnɛl]", "plural": "schneller, am schnellsten", "meaning": "快的，迅速的", "example": "Der ICE-Zug ist viel schneller als das Auto.", "exampleCn": "ICE高速火车比汽车快得多。"},
                            {"word": "billig", "article": "", "type": "adj.", "ipa": "[ˈbɪlɪç]", "plural": "billiger, am billigsten", "meaning": "便宜的，廉价的", "example": "Dieses T-Shirt ist billiger als das Hemd.", "exampleCn": "这件T恤比衬衫便宜。"},
                            {"word": "teuer", "article": "", "type": "adj.", "ipa": "[ˈtɔɪ̯ɐ]", "plural": "teurer, am teuersten", "meaning": "昂贵的，贵的", "example": "Das Leben in München ist am teuersten.", "exampleCn": "慕尼黑的生活成本最高。"},
                            {"word": "wichtig", "article": "", "type": "adj.", "ipa": "[ˈvɪçtɪç]", "plural": "wichtiger, am wichtigsten", "meaning": "重要的", "example": "Grammatik ist wichtig, aber Sprechen ist noch wichtiger.", "exampleCn": "语法很重要，但口语更重要。"},
                            {"word": "das Angebot", "article": "das", "type": "n.", "ipa": "[ˈanɡəˌboːt]", "plural": "-e", "meaning": "优惠特价；供给", "example": "Im Supermarkt gibt es heute tolle Angebote.", "exampleCn": "超市今天有很棒的特价商品。"},
                            {"word": "die Qualität", "article": "die", "type": "n.", "ipa": "[kvaliˈtɛːt]", "plural": "-en", "meaning": "质量，品质", "example": "Deutsche Produkte haben eine hohe Qualität.", "exampleCn": "德国产品拥有很高的质量。"},
                            {"word": "auswählen", "article": "", "type": "v.", "ipa": "[ˈaʊsˌvɛːlən]", "plural": "wählt aus, wählte aus, ausgewählt", "meaning": "挑选，选择", "example": "Sie können das beste Produkt auswählen.", "exampleCn": "您可以挑选最好的产品。"},
                            {"word": "gefallen", "article": "", "type": "v.", "ipa": "[ɡəˈfaln̩]", "plural": "gefällt, gefiel, gefallen", "meaning": "使喜欢，合...心意 (接Dativ)", "example": "Wie gefällt Ihnen dieser Mantel?", "exampleCn": "您觉得这件大衣怎么样？"}
                        ],
                        "quiz": [
                            {
                                "id": "A2_L5_Q1",
                                "type": "GRAMMAR_FILL",
                                "question": "请选出 'gern' 的最高级填空：Ich trinke gern Tee, lieber Kaffee, aber am ______ trinke ich Wasser.",
                                "options": ["besten", "liebsten", "meisten", "höchsten"],
                                "correctIndex": 1,
                                "explanation": "gern 的比较级和最高级为特殊变化：gern -> lieber -> am liebsten。"
                            },
                            {
                                "id": "A2_L5_Q2",
                                "type": "EXAM_REAL",
                                "question": "【歌德A2真题】阅读比较：“Peter ist 25 Jahre alt, Klaus ist 28 Jahre alt.” 下列陈述正确的是：",
                                "options": [
                                    "Peter ist älter als Klaus.",
                                    "Klaus ist älter als Peter.",
                                    "Klaus ist jünger als Peter.",
                                    "Peter ist am ältesten."
                                ],
                                "correctIndex": 1,
                                "explanation": "Klaus 28岁比 Peter 25岁年龄更大，因此 Klaus ist älter als Peter (alt -> älter)。"
                            }
                        ]
                    }
                ]
            },
            {
                "id": "B1",
                "name": "B1 进阶中级 (Goethe-Zertifikat B1)",
                "goetheLevel": "B1 独立运用门槛",
                "description": "达到歌德B1标准：能在工作、学习与休闲场景自如交流；能清楚连贯叙述经历、梦想与目标，并简要说明理由与论据。涵盖过去时、形容词词尾变化、虚拟式、关系从句与被动语态！",
                "lessons": [
                    {
                        "id": "B1_L1",
                        "title": "第1课：历史与书面叙述 (Vergangenheit & Präteritum)",
                        "summary": "掌握过去时 (Präteritum) 书面表达、新闻叙事与小说语态",
                        "grammar": {
                            "title": "过去时 (Präteritum) 构成与用法",
                            "sections": [
                                {
                                    "heading": "1. 过去时 (Präteritum) 与完成时 (Perfekt) 的使用边界",
                                    "content": "• 完成时 (Perfekt)：主要用于【口语交流、日常对话、即时短信】。\n"
                                               "• 过去时 (Präteritum)：主要用于【书面语、新闻报道、小说传记、正式报告】。\n"
                                               "• 特例：sein, haben 以及情态动词在口语中也极度偏好使用过去时 (ich war, ich hatte, ich musste...)！"
                                },
                                {
                                    "heading": "2. 动词过去时变位规律",
                                    "content": "• 规则动词：词干 + -te- + 人称词尾 (ich lernte, er lernte, wir lernten)\n"
                                               "• 不规则强变化动词：词干元音发生音变 (Ablaut)，第1和第3人称单数【无词尾】！\n"
                                               "  gehen -> ging (ich ging, er ging)\n"
                                               "  sehen -> sah (ich sah, er sah)\n"
                                               "  kommen -> kam (ich kam, er kam)\n"
                                               "  schreiben -> schrieb (ich schrieb, er schrieb)"
                                }
                            ]
                        },
                        "words": [
                            {"word": "die Vergangenheit", "article": "die", "type": "n.", "ipa": "[fɛɐ̯ˈɡaŋənhaɪt]", "plural": "-", "meaning": "过去，往昔", "example": "In der Vergangenheit gab es noch kein Internet.", "exampleCn": "在过去还没有互联网。"},
                            {"word": "die Geschichte", "article": "die", "type": "n.", "ipa": "[ɡəˈʃɪçtə]", "plural": "-n", "meaning": "历史；故事", "example": "Er erzählt eine spannende Geschichte aus seiner Jugend.", "exampleCn": "他讲述了一个他青年时期的精彩故事。"},
                            {"word": "geschehen", "article": "", "type": "v.", "ipa": "[ɡəˈʃeːən]", "plural": "geschieht, geschah, ist geschehen", "meaning": "发生 (只用第三人称)", "example": "Was ist gestern Abend geschehen?", "exampleCn": "昨晚发生了什么事？"},
                            {"word": "die Nachricht", "article": "die", "type": "n.", "ipa": "[ˈnaːxˌʁɪçt]", "plural": "-en", "meaning": "新闻；消息", "example": "Ich habe die Nachrichten im Radio gehört.", "exampleCn": "我在收音机里收听了新闻。"},
                            {"word": "der Schriftsteller", "article": "der", "type": "n.", "ipa": "[ˈʃʁɪftˌʃtɛlɐ]", "plural": "-", "meaning": "作家", "example": "Goethe ist der berühmteste deutsche Schriftsteller.", "exampleCn": "歌德是德国最著名的作家。"},
                            {"word": "entdecken", "article": "", "type": "v.", "ipa": "[ɛntˈdɛkn̩]", "plural": "entdeckt, entdeckte, entdeckt", "meaning": "发现，发掘", "example": "Die Forscher entdeckten eine neue Methode.", "exampleCn": "研究人员发现了一种新方法。"},
                            {"word": "erfolgreich", "article": "", "type": "adj.", "ipa": "[ɛɐ̯ˈfɔlkˌʁaɪç]", "plural": "", "meaning": "成功的，有成效的", "example": "Das Projekt war sehr erfolgreich.", "exampleCn": "这个项目非常成功。"},
                            {"word": "die Entwicklung", "article": "die", "type": "n.", "ipa": "[ɛntˈvɪklʊŋ]", "plural": "-en", "meaning": "发展，演变", "example": "Die wirtschaftliche Entwicklung verläuft positiv.", "exampleCn": "经济发展态势良好。"}
                        ],
                        "quiz": [
                            {
                                "id": "B1_L1_Q1",
                                "type": "GRAMMAR_FILL",
                                "question": "请选出动词 'sehen' 在过去时第三人称单数 (er) 的正确形式：",
                                "options": ["sehte", "sah", "saht", "gesehen"],
                                "correctIndex": 1,
                                "explanation": "sehen 过去时为强变化动词，词干发生元音突变变为 sah，且第1/3人称单数无词尾：er sah。"
                            },
                            {
                                "id": "B1_L1_Q2",
                                "type": "EXAM_REAL",
                                "question": "【歌德B1阅读】历史人物传记中写道：“Im Jahre 1879 wurde Albert Einstein in Ulm geboren.” 句中的 'wurde geboren' 含义是：",
                                "options": ["逝世", "出生", "结婚", "移民"],
                                "correctIndex": 1,
                                "explanation": "geboren werden 是表示“出生”的固定被动表达，过去时形式为 wurde geboren。"
                            }
                        ]
                    },
                    {
                        "id": "B1_L2",
                        "title": "第2课：形容词词尾变化 (Adjektivdeklination)",
                        "summary": "全面攻克德语语法第一大难关：定冠词、不定冠词与零冠词后的形容词词尾",
                        "grammar": {
                            "title": "形容词词尾三大体系总结表",
                            "sections": [
                                {
                                    "heading": "1. 定冠词体系（弱变化 Schwache Deklination）",
                                    "content": "当冠词已经明确指示出格位时，形容词只需要加 -e 或 -en：\n"
                                               "• 第一格 Nominativ 单数全部加 -e (der gute Mann, die schöne Frau, das kleine Kind)\n"
                                               "• 第四格 Akkusativ 中性与阴性依然为 -e；【其余全部变为 -en】！\n"
                                               "（包含阳性四格 den guten Mann、全部第三格 dem guten Mann / der schönen Frau、全部第二格、以及所有复数 die kleinen Kinder）"
                                },
                                {
                                    "heading": "2. 不定冠词体系（混合变化 Gemischte Deklination）",
                                    "content": "当 ein/kein/mein 没有显示词性特征时，形容词必须补足词性特征：\n"
                                               "• 阳性第一格：ein gut-er Mann (补阳性特征 -er)\n"
                                               "• 中性第一格：ein klein-es Kind (补中性特征 -es)\n"
                                               "• 阴性第一格：eine schön-e Frau (-e)\n"
                                               "• 在所有第三格、第二格以及阳性第四格（einen guten Mann）中，词尾统一为 -en！"
                                },
                                {
                                    "heading": "3. 零冠词体系（强变化 Starke Deklination）",
                                    "content": "当名词前没有任何冠词时，形容词直接承担定冠词的词尾特征！\n"
                                               "例如：kaltes Wasser (das Wasser -> -es), frische Milch (die Milch -> -e), guter Wein (der Wein -> -er)."
                                }
                            ]
                        },
                        "words": [
                            {"word": "die Erfahrung", "article": "die", "type": "n.", "ipa": "[ɛɐ̯ˈfaːʁʊŋ]", "plural": "-en", "meaning": "经验，体会", "example": "Er sammelt wertvolle praktische Erfahrungen.", "exampleCn": "他积累了宝贵的实践经验。"},
                            {"word": "das Angebot", "article": "das", "type": "n.", "ipa": "[ˈanɡəˌboːt]", "plural": "-e", "meaning": "报价，供应", "example": "Das ist ein sehr günstiges Angebot.", "exampleCn": "这是一个非常划算的优惠。"},
                            {"word": "interessant", "article": "", "type": "adj.", "ipa": "[ɪntəʁɛˈsant]", "plural": "", "meaning": "有趣的，有意思的", "example": "Wir führen ein interessantes Gespräch.", "exampleCn": "我们进行了一次有趣的谈话。"},
                            {"word": "die Zukunft", "article": "die", "type": "n.", "ipa": "[ˈtsuːkʊnft]", "plural": "-", "meaning": "未来，前途", "example": "Er plant seine berufliche Zukunft sehr sorgfältig.", "exampleCn": "他非常周密地规划着自己的职业前途。"},
                            {"word": "das Ziel", "article": "das", "type": "n.", "ipa": "[tsiːl]", "plural": "-e", "meaning": "目标，目的地", "example": "Mein wichtigstes Ziel ist das Bestehen der B1-Prüfung.", "exampleCn": "我最重要的目标是通过B1考试。"},
                            {"word": "erreichen", "article": "", "type": "v.", "ipa": "[ɛɐ̯ˈʁaɪçn̩]", "plural": "erreicht, erreichte, erreicht", "meaning": "达到，实现；赶上", "example": "Mit Fleiß kann man jedes Ziel erreichen.", "exampleCn": "只要勤奋，就能实现任何目标。"},
                            {"word": "modern", "article": "", "type": "adj.", "ipa": "[moˈdɛʁn]", "plural": "", "meaning": "现代的，新式的", "example": "Das Unternehmen nutzt moderne Technologien.", "exampleCn": "该企业应用了现代技术。"},
                            {"word": "die Möglichkeit", "article": "die", "type": "n.", "ipa": "[ˈmøːklɪçkaɪt]", "plural": "-en", "meaning": "可能性，机会", "example": "Hier gibt es viele neue Möglichkeiten.", "exampleCn": "这里有许多新的机遇。"}
                        ],
                        "quiz": [
                            {
                                "id": "B1_L2_Q1",
                                "type": "GRAMMAR_FILL",
                                "question": "【不定冠词后形容词】Ich trinke gern ein ______ (kalt, 中性 das Bier) Bier.",
                                "options": ["kaltes", "kalten", "kalte", "kaltem"],
                                "correctIndex": 0,
                                "explanation": "Bier 是中性名词（das Bier），在第四格不定冠词 ein 后，形容词必须补足中性特征词尾 -es：ein kaltes Bier。"
                            },
                            {
                                "id": "B1_L2_Q2",
                                "type": "GRAMMAR_FILL",
                                "question": "【定冠词第三格】Er schenkt dem ______ (nett, 阳性 der Mann) Mann eine Blume.",
                                "options": ["netten", "nettem", "netter", "nette"],
                                "correctIndex": 0,
                                "explanation": "定冠词第三格中，阳性、中性、阴性、复数后面的形容词词尾一律全部为 -en (dem netten Mann)。"
                            }
                        ]
                    },
                    {
                        "id": "B1_L3",
                        "title": "第3课：愿望与礼貌虚拟式 (Konjunktiv II)",
                        "summary": "掌握第二虚拟式：würde + 原形、hätte, wäre, könnte 表达非真实愿望、假设与极度礼貌表达",
                        "grammar": {
                            "title": "第二虚拟式 (Konjunktiv II) 应用法则",
                            "sections": [
                                {
                                    "heading": "1. 核心构成形式",
                                    "content": "• 替代形式：würde + 动词不定式（放在句末）\n"
                                               "  ich würde, du würdest, er würde, wir würden, ihr würdet, sie/Sie würden\n"
                                               "  例：Ich würde gerne eine Reise machen. (我很想去旅行。)\n"
                                               "• 核心动词必须用自身固有虚拟式形式：\n"
                                               "  sein -> wäre (Ich wäre jetzt gern am Strand.)\n"
                                               "  haben -> hätte (Wenn ich viel Geld hätte...)\n"
                                               "  können -> könnte (Könnten Sie mir bitte helfen?)\n"
                                               "  müssen -> müsste (Ich müsste eigentlich mehr lernen.)"
                                },
                                {
                                    "heading": "2. 歌德B1三大高频运用场景",
                                    "content": "• 极度委婉礼貌的请求：Könnten Sie das bitte wiederholen? / Hätten Sie Zeit?\n"
                                               "• 非真实条件从句：Wenn ich reich wäre, würde ich ein Haus kaufen.\n"
                                               "• 表达建议 (sollen -> sollte)：Du solltest zum Arzt gehen."
                                }
                            ]
                        },
                        "words": [
                            {"word": "der Wunsch", "article": "der", "type": "n.", "ipa": "[vʊnʃ]", "plural": "Wünsche", "meaning": "愿望，心愿", "example": "Mein größter Wunsch ging in Erfüllung.", "exampleCn": "我最大的心愿实现了。"},
                            {"word": "die Höflichkeit", "article": "die", "type": "n.", "ipa": "[ˈhøːflɪçkaɪt]", "plural": "-", "meaning": "礼貌，客气", "example": "Höflichkeit ist im Berufsleben unerlässlich.", "exampleCn": "礼貌在职场生涯中是不可或缺的。"},
                            {"word": "der Ratschlag", "article": "der", "type": "n.", "ipa": "[ˈʁaːtˌʃlaːk]", "plural": "Ratschläge", "meaning": "建议，劝告", "example": "Darf ich Ihnen einen guten Ratschlag geben?", "exampleCn": "我可以给您提一个好建议吗？"},
                            {"word": "die Wirklichkeit", "article": "die", "type": "n.", "ipa": "[ˈvɪʁklɪçkaɪt]", "plural": "-en", "meaning": "现实，事实", "example": "In der Wirklichkeit sieht alles ganz anders aus.", "exampleCn": "在现实中一切看起来截然不同。"},
                            {"word": "vorschlagen", "article": "", "type": "v.", "ipa": "[ˈfoːɐ̯ˌʃlaːɡn̩]", "plural": "schlägt vor, schlug vor, vorgeschlagen", "meaning": "提议，建议", "example": "Ich würde vorschlagen, dass wir eine Pause machen.", "exampleCn": "我提议我们休息一下。"},
                            {"word": "der Traum", "article": "der", "type": "n.", "ipa": "[tʁaʊm]", "plural": "Träume", "meaning": "梦想；梦境", "example": "Er möchte seinen Lebenstraum verwirklichen.", "exampleCn": "他想实现他的人生梦想。"},
                            {"word": "zufrieden", "article": "", "type": "adj.", "ipa": "[tsuˈfʁiːdn̩]", "plural": "", "meaning": "满意的，知足的", "example": "Bist du mit deiner aktuellen Stelle zufrieden?", "exampleCn": "你对你现在的职位满意吗？"},
                            {"word": "die Bedingung", "article": "die", "type": "n.", "ipa": "[bəˈdɪŋʊŋ]", "plural": "-en", "meaning": "条件，前提", "example": "Unter dieser Bedingung stimme ich zu.", "exampleCn": "在此条件下我同意。"}
                        ],
                        "quiz": [
                            {
                                "id": "B1_L3_Q1",
                                "type": "GRAMMAR_FILL",
                                "question": "【歌德B1口语高频】餐厅中礼貌点餐表达“我想要一杯咖啡”的最地道第二虚拟式是：",
                                "options": [
                                    "Ich hätte gern eine Tasse Kaffee.",
                                    "Ich will eine Tasse Kaffee haben!",
                                    "Ich habe eine Tasse Kaffee.",
                                    "Ich bin eine Tasse Kaffee."
                                ],
                                "correctIndex": 0,
                                "explanation": "Ich hätte gern... (第二虚拟式) 是德语国家在餐厅、商店中最标准得体的高级礼貌表达。"
                            },
                            {
                                "id": "B1_L3_Q2",
                                "type": "GRAMMAR_FILL",
                                "question": "非真实条件句：Wenn ich Zeit ______ (haben), ______ (gehen) ich ins Kino.",
                                "options": ["hätte / würde", "habe / gehe", "hätte / gehe", "hatte / ging"],
                                "correctIndex": 0,
                                "explanation": "非真实条件句中从句使用 hätte，主句使用 würde + 动词原形 gehen。"
                            }
                        ]
                    },
                    {
                        "id": "B1_L4",
                        "title": "第4课：关系从句与社会描述 (Relativsätze)",
                        "summary": "掌握关系从句 (Relativpronomen: 格位取决于从句角色，性与数取决于先行词)",
                        "grammar": {
                            "title": "关系从句 (Relativsatz) 结构全解析",
                            "sections": [
                                {
                                    "heading": "1. 关系代词与先行词的关系法则",
                                    "content": "• 关系代词的【性(阳/阴/中)与数(单/复)】：由它修饰的先行词决定！\n"
                                               "• 关系代词的【格位(1/2/3/4格)】：由它在从句内部充当的句子成分决定！\n"
                                               "• 语序：属于从句，关系从句内部动词一律置于【句末】！"
                                },
                                {
                                    "heading": "2. 关系代词变化表格",
                                    "content": "• 第一格 Nom: der (阳) / die (阴) / das (中) / die (复)\n"
                                               "• 第四格 Akk: den (阳) / die (阴) / das (中) / die (复)\n"
                                               "• 第三格 Dat: dem (阳) / der (阴) / dem (中) / denen (复 - 注意特异形式！)\n"
                                               "• 第二格 Gen: dessen (阳/中) / deren (阴/复)"
                                },
                                {
                                    "heading": "3. 典型例句对比",
                                    "content": "• Das ist der Mann, der nebenan wohnt. (Mann为主语，阳性1格 -> der)\n"
                                               "• Das ist der Mann, den ich gestern gesehen habe. (Mann为宾语，阳性4格 -> den)\n"
                                               "• Das ist der Mann, mit dem ich gesprochen habe. (mit后接3格，阳性3格 -> dem)"
                                }
                            ]
                        },
                        "words": [
                            {"word": "die Beziehung", "article": "die", "type": "n.", "ipa": "[bəˈtsiːʊŋ]", "plural": "-en", "meaning": "关系，交往", "example": "Gute Beziehungen zu Kollegen sind sehr wichtig.", "exampleCn": "与同事保持良好关系非常重要。"},
                            {"word": "die Gesellschaft", "article": "die", "type": "n.", "ipa": "[ɡəˈzɛlʃaft]", "plural": "-en", "meaning": "社会；公司", "example": "Die moderne Gesellschaft verändert sich rasant.", "exampleCn": "现代社会正在迅速发生变化。"},
                            {"word": "unterstützen", "article": "", "type": "v.", "ipa": "[ˌʊntɐˈʃtʏtsn̩]", "plural": "unterstützt, unterstützte, unterstützt", "meaning": "支持，资助", "example": "Wir unterstützen unsere Freunde in schwierigen Zeiten.", "exampleCn": "我们在困难时期支持我们的朋友。"},
                            {"word": "der Nachbar", "article": "der", "type": "n.", "ipa": "[ˈnaxbaːɐ̯]", "plural": "-n", "meaning": "邻居", "example": "Das ist mein neuer Nachbar, der aus Spanien kommt.", "exampleCn": "这是我的新邻居，他来自西班牙。"},
                            {"word": "vertrauen", "article": "", "type": "v.", "ipa": "[fɛɐ̯ˈtʁaʊən]", "plural": "vertraut, vertraute, vertraut", "meaning": "信任，信赖 (接Dativ)", "example": "Ich vertraue meinem besten Freund vollkommen.", "exampleCn": "我完全信任我最好的朋友。"},
                            {"word": "die Kultur", "article": "die", "type": "n.", "ipa": "[kʊlˈtuːɐ̯]", "plural": "-en", "meaning": "文化，文明", "example": "Er interessiert sich für die deutsche Kultur und Geschichte.", "exampleCn": "他对德国文化和历史很感兴趣。"},
                            {"word": "gemeinsam", "article": "", "type": "adj./adv.", "ipa": "[ɡəˈmaɪnzaːm]", "plural": "", "meaning": "共同的，一起", "example": "Gemeinsam können wir diese Herausforderung meistern.", "exampleCn": "我们齐心协力就能克服这个挑战。"},
                            {"word": "die Lösung", "article": "die", "type": "n.", "ipa": "[ˈløːzʊŋ]", "plural": "-en", "meaning": "解决方案，答案", "example": "Wir suchen nach einer praktischen Lösung.", "exampleCn": "我们在寻找一个实用的解决方案。"}
                        ],
                        "quiz": [
                            {
                                "id": "B1_L4_Q1",
                                "type": "GRAMMAR_FILL",
                                "question": "请选出正确的关系代词：Das ist das Buch, ______ (das Buch, 从句宾语4格) ich gestern gekauft habe.",
                                "options": ["das", "dem", "dessen", "welches"],
                                "correctIndex": 0,
                                "explanation": "先行词是 das Buch（中性），在从句中作为 gekauft 的第四格直接宾语，中性第四格关系代词为 das。"
                            },
                            {
                                "id": "B1_L4_Q2",
                                "type": "GRAMMAR_FILL",
                                "question": "【介词与关系代词】Hier ist die Kollegin, mit ______ ich das Projekt plane.",
                                "options": ["der", "die", "denen", "deren"],
                                "correctIndex": 0,
                                "explanation": "Kollegin 是阴性名词，mit 要求接第三格，阴性第三格关系代词为 der (mit der)。"
                            }
                        ]
                    },
                    {
                        "id": "B1_L5",
                        "title": "第5课：过程与科技被动语态 (Passiv)",
                        "summary": "掌握过程被动语态 (Vorgangspassiv: werden + Partizip II)、施动者 von/durch、歌德B1综合真题",
                        "grammar": {
                            "title": "过程被动语态 (Vorgangspassiv) 全时态",
                            "sections": [
                                {
                                    "heading": "1. 被动态基本公式",
                                    "content": "主动句宾语 -> 变被动句主语！\n"
                                               "被动态结构：werden（变位） + ... + 过去分词 Partizip II（放句末）！\n"
                                               "• 现在时：Das Auto wird repariert.\n"
                                               "• 过去时：Das Auto wurde repariert.\n"
                                               "• 完成时：Das Auto ist repariert worden. (注意：被动完成时不用 geworden，而用 worden！)\n"
                                               "• 带情态动词：Das Auto muss repariert werden."
                                },
                                {
                                    "heading": "2. 动作发出者（施动者）介词",
                                    "content": "• 人或具体行为者用 von + 第三格 Dativ：Das Haus wird von den Bauarbeitern gebaut.\n"
                                               "• 媒介、手段或抽象原因用 durch + 第四格 Akkusativ：Die Stadt wurde durch das Erdbeben zerstört."
                                }
                            ]
                        },
                        "words": [
                            {"word": "die Umwelt", "article": "die", "type": "n.", "ipa": "[ˈʊmˌvɛlt]", "plural": "-", "meaning": "环境，自然界", "example": "Die Umwelt muss geschützt werden.", "exampleCn": "环境必须得到保护。"},
                            {"word": "die Energie", "article": "die", "type": "n.", "ipa": "[enɛʁˈɡiː]", "plural": "-n", "meaning": "能源，能量", "example": "Erneuerbare Energien werden in Deutschland gefördert.", "exampleCn": "可再生能源在德国受到大力推广。"},
                            {"word": "bauen", "article": "", "type": "v.", "ipa": "[ˈbaʊən]", "plural": "baut, baute, gebaut", "meaning": "建造，修建", "example": "Hier wird eine neue Brücke gebaut.", "exampleCn": "这里正在修建一座新桥。"},
                            {"word": "die Produktion", "article": "die", "type": "n.", "ipa": "[pʁodʊkˈtsi̯oːn]", "plural": "-en", "meaning": "生产，制造", "example": "Die Produktion von Elektroautos steigt stark an.", "exampleCn": "电动汽车的产量大幅攀升。"},
                            {"word": "die Technologie", "article": "die", "type": "n.", "ipa": "[tɛçnoloˈɡiː]", "plural": "-n", "meaning": "科技，工艺", "example": "Moderne Technologie wird in allen Bereichen eingesetzt.", "exampleCn": "现代技术被应用在各个领域。"},
                            {"word": "zerstören", "article": "", "type": "v.", "ipa": "[tsɛɐ̯ˈʃtøːʁən]", "plural": "zerstört, zerstörte, zerstört", "meaning": "破坏，摧毁", "example": "Wälder dürfen nicht zerstört werden.", "exampleCn": "森林绝不能被破坏。"},
                            {"word": "die Maßnahme", "article": "die", "type": "n.", "ipa": "[ˈmaːsˌnaːmə]", "plural": "-n", "meaning": "措施，行动", "example": "Wirksame Maßnahmen wurden sofort ergriffen.", "exampleCn": "有效的措施被立即采纳。"},
                            {"word": "schützen", "article": "", "type": "v.", "ipa": "[ˈʃʏtsn̩]", "plural": "schützt, schützte, geschützt", "meaning": "保护，防御", "example": "Die Natur wird durch strenge Gesetze geschützt.", "exampleCn": "大自然受到严格法律的保护。"}
                        ],
                        "quiz": [
                            {
                                "id": "B1_L5_Q1",
                                "type": "GRAMMAR_FILL",
                                "question": "【被动态现在时】请将句子转换为过程被动态：“Der Mechaniker repariert das Auto.” -> “Das Auto ______ .”",
                                "options": [
                                    "wird repariert",
                                    "ist repariert",
                                    "wurde repariert",
                                    "wird reparieren"
                                ],
                                "correctIndex": 0,
                                "explanation": "过程被动态现在时公式：werden + Partizip II。das Auto 第三人称单数用 wird，过去分词为 repariert：Das Auto wird repariert。"
                            },
                            {
                                "id": "B1_L5_Q2",
                                "type": "EXAM_REAL",
                                "question": "【歌德B1综合模拟】书面通知写道：“Wegen Renovierungsarbeiten bleibt die Bibliothek bis Montag geschlossen.” 此句表达的核心通知是：",
                                "options": [
                                    "图书馆正在举办装修讲座",
                                    "图书馆因为翻修施工，一直关闭至周一",
                                    "图书馆下周一重新开始装修",
                                    "图书馆下周一开始延长借书期限"
                                ],
                                "correctIndex": 1,
                                "explanation": "Wegen Renovierungsarbeiten 表示“由于装修工程”；bleibt geschlossen 属于状态描述“保持关闭”；bis Montag 意为“直到周一”。"
                            }
                        ]
                    }
                ]
            },
            {
                "id": "B2",
                "name": "B2 高级精通 (Goethe-Zertifikat B2)",
                "goetheLevel": "B2 高级流利表达",
                "description": "达到歌德B2标准：能理解复杂主题的核心思想（包括专业技术讨论）；能自然流畅地与母语者交流，就广泛话题表达清晰详尽的见解，阐述各种视角的利弊。",
                "lessons": [
                    {
                        "id": "B2_L1",
                        "title": "第1课：论证逻辑与连词 (Konnektoren)",
                        "summary": "掌握高级成对双重连词 (sowohl... als auch, weder... noch, nicht nur... sondern auch)",
                        "grammar": {
                            "title": "双重并列连词 (Zweiteilige Konnektoren) 逻辑网络",
                            "sections": [
                                {
                                    "heading": "1. 递进与并列连词",
                                    "content": "• sowohl A als auch B (既 A 又 B，两方面皆肯定):\n"
                                               "  Er spricht sowohl fließend Deutsch als auch Englisch.\n"
                                               "• nicht nur A, sondern auch B (不仅 A，而且 B，强调后者):\n"
                                               "  Diese Maßnahme schützt nicht nur das Klima, sondern spart auch Geld."
                                },
                                {
                                    "heading": "2. 全面否定与选择连词",
                                    "content": "• weder A noch B (既不 A 也不 B，两方面皆否定，无需再加 nicht):\n"
                                               "  Er hat weder Zeit noch Geld für lange Urlaube.\n"
                                               "• entweder A oder B (要么 A 要么 B，二选一):\n"
                                               "  Entweder wir finden jetzt eine Lösung, oder wir brechen das Projekt ab."
                                },
                                {
                                    "heading": "3. 让步与转折连词",
                                    "content": "• zwar A, aber B (虽然 A，但是 B):\n"
                                               "  Das Auto ist zwar teuer, aber sehr zuverlässig."
                                }
                            ]
                        },
                        "words": [
                            {"word": "die Digitalisierung", "article": "die", "type": "n.", "ipa": "[diɡitaliˈziːʁʊŋ]", "plural": "-", "meaning": "数字化，数字转型", "example": "Die Digitalisierung verändert unsere Arbeitswelt grundlegend.", "exampleCn": "数字化从根本上改变着我们的工作世界。"},
                            {"word": "der Vorteil", "article": "der", "type": "n.", "ipa": "[ˈfoːɐ̯ˌtaɪl]", "plural": "-e", "meaning": "优势，长处", "example": "Das neue Modell bietet sowohl ökologische als auch finanzielle Vorteile.", "exampleCn": "这款新机型兼具环保与经济双重优势。"},
                            {"word": "der Nachteil", "article": "der", "type": "n.", "ipa": "[ˈnaxˌtaɪl]", "plural": "-e", "meaning": "缺点，劣势", "example": "Man muss die Vor- und Nachteile sorgfältig abwägen.", "exampleCn": "人们必须仔细权衡利弊。"},
                            {"word": "beeinflussen", "article": "", "type": "v.", "ipa": "[bəˈʔaɪnflʊsn̩]", "plural": "beeinflusst, beeinflusste, beeinflusst", "meaning": "影响，对...起作用", "example": "Soziale Medien beeinflussen die öffentliche Meinung stark.", "exampleCn": "社交媒体极大地影响着公众舆论。"},
                            {"word": "die Auswirkung", "article": "die", "type": "n.", "ipa": "[ˈaʊsˌvɪʁkʊŋ]", "plural": "-en", "meaning": "影响，效果", "example": "Welche Auswirkungen hat der Klimawandel auf die Landwirtschaft?", "exampleCn": "气候变化对农业有哪些影响？"},
                            {"word": "die Diskussion", "article": "die", "type": "n.", "ipa": "[dɪskʊˈsi̯oːn]", "plural": "-en", "meaning": "讨论，辩论", "example": "Die Debatte führte zu einer lebhaften Diskussion.", "exampleCn": "这场辩论引发了热烈的讨论。"},
                            {"word": "argumentieren", "article": "", "type": "v.", "ipa": "[aʁɡumɛnˈtiːʁən]", "plural": "argumentiert, argumentierte, argumentiert", "meaning": "论证，阐述理由", "example": "Die Rednerin argumentierte sehr überzeugend.", "exampleCn": "演讲者的论述非常具有说服力。"},
                            {"word": "überzeugend", "article": "", "type": "adj.", "ipa": "[yːbɐˈtsɔɪ̯ɡn̩t]", "plural": "", "meaning": "令人信服的，有力的", "example": "Seine Argumente klingen plausibel und überzeugend.", "exampleCn": "他的论据听起来合理且令人信服。"}
                        ],
                        "quiz": [
                            {
                                "id": "B2_L1_Q1",
                                "type": "GRAMMAR_FILL",
                                "question": "【歌德B2写作论据】表达“既不仅节约成本，而且提高了工作效率”的最佳连词搭配是：",
                                "options": [
                                    "nicht nur ... sondern auch",
                                    "weder ... noch",
                                    "entweder ... oder",
                                    "zwar ... aber nicht"
                                ],
                                "correctIndex": 0,
                                "explanation": "nicht nur... sondern auch 表示“不仅……而且……”，用于递进强化两个积极论点，是歌德B2议论文写作黄金句型。"
                            },
                            {
                                "id": "B2_L1_Q2",
                                "type": "GRAMMAR_FILL",
                                "question": "请选出正确连词：“Er hat ______ Zeit ______ Lust, an der Konferenz teilzunehmen (他既没时间也没兴致).”",
                                "options": [
                                    "weder ... noch",
                                    "sowohl ... als auch",
                                    "entweder ... oder",
                                    "nicht nur ... sondern auch"
                                ],
                                "correctIndex": 0,
                                "explanation": "weder... noch 用于双重否定（既不……也不……），其本身已包含否定语义，句中不应重复出现 nicht 或 kein。"
                            }
                        ]
                    },
                    {
                        "id": "B2_L2",
                        "title": "第2课：公文、经济与第二格介词 (Genitiv)",
                        "summary": "掌握四大高频第二格介词 (trotz, wegen, während, anstatt) 与名物化学术风格",
                        "grammar": {
                            "title": "第二格 (Genitiv) 介词与名物化表达",
                            "sections": [
                                {
                                    "heading": "1. 歌德B2四大高频第二格介词",
                                    "content": "• trotz + Gen: 尽管，虽然 (Trotz des schlechten Wetters gingen wir spazieren.)\n"
                                               "• wegen + Gen: 由于，因为 (Wegen eines schweren Unfalls ist die Straße gesperrt.)\n"
                                               "• während + Gen: 在...期间 (Während des Aufenthalts in Deutschland lernte er viel.)\n"
                                               "• anstatt + Gen: 代替，而不是 (Anstatt einer schriftlichen Prüfung gibt es ein Referat.)"
                                },
                                {
                                    "heading": "2. 第二格名词词尾规则",
                                    "content": "• 阳性与中性名词第二格：词尾通常加 -(e)s (des Mannes, des Kindes, des Tages)\n"
                                               "• 阴性与复数名词第二格：名词词尾不加 -s，仅冠词变为 der (der Frau, der Studenten)"
                                },
                                {
                                    "heading": "3. 名物化学术风格 (Nominalisierung)",
                                    "content": "动词转化为名词以增强表达精炼度与学术规范性：\n"
                                               "Weil die Preise steigen -> Wegen des Anstiegs der Preise (由于价格上涨)"
                                }
                            ]
                        },
                        "words": [
                            {"word": "die Wirtschaft", "article": "die", "type": "n.", "ipa": "[ˈvɪʁtʃaft]", "plural": "-en", "meaning": "经济，经济学", "example": "Die deutsche Wirtschaft exportiert viele hochwertige Maschinen.", "exampleCn": "德国经济出口大量高质量机械。"},
                            {"word": "die Konsequenz", "article": "die", "type": "n.", "ipa": "[kɔnzeˈkvɛnts]", "plural": "-en", "meaning": "后果，结论", "example": "Diese Entscheidung hat weitreichende Konsequenzen.", "exampleCn": "这个决定带来了深远的后果。"},
                            {"word": "der Vertrag", "article": "der", "type": "n.", "ipa": "[fɛɐ̯ˈtʁaːk]", "plural": "Verträge", "meaning": "合同，契约", "example": "Beide Parteien haben den Arbeitsvertrag unterzeichnet.", "exampleCn": "双方都签署了劳动合同。"},
                            {"word": "die Verantwortung", "article": "die", "type": "n.", "ipa": "[fɛɐ̯ˈʔantvɔʁtʊŋ]", "plural": "-en", "meaning": "责任，职责", "example": "Führungskräfte tragen eine große Verantwortung.", "exampleCn": "管理人员承担着巨大的责任。"},
                            {"word": "das Unternehmen", "article": "das", "type": "n.", "ipa": "[ʊntɐˈneːmən]", "plural": "-", "meaning": "企业，公司", "example": "Das Unternehmen investiert stark in Forschung und Entwicklung.", "exampleCn": "该企业大力投资于研发。"},
                            {"word": "die Bedingung", "article": "die", "type": "n.", "ipa": "[bəˈdɪŋʊŋ]", "plural": "-en", "meaning": "条件，规程", "example": "Die Arbeitsbedingungen müssen kontinuierlich verbessert werden.", "exampleCn": "工作条件必须持续得到改善。"},
                            {"word": "trotzdem", "article": "", "type": "adv.", "ipa": "[ˈtʁɔtsdeːm]", "plural": "", "meaning": "尽管如此，仍然", "example": "Es regnete stark, trotzdem gingen wir wandern.", "exampleCn": "雨下得很大，尽管如此我们依然去徒步了。"},
                            {"word": "berücksichtigen", "article": "", "type": "v.", "ipa": "[bəˈʁʏkˌzɪçtɪɡn̩]", "plural": "berücksichtigt, berücksichtigte, berücksichtigt", "meaning": "顾及，考虑到", "example": "Wir müssen alle Kundenwünsche berücksichtigen.", "exampleCn": "我们必须兼顾所有的客户需求。"}
                        ],
                        "quiz": [
                            {
                                "id": "B2_L2_Q1",
                                "type": "GRAMMAR_FILL",
                                "question": "【第二格介词】请选出正确词尾填空：Trotz ______ (der Regen) gingen wir in die Stadt.",
                                "options": ["des Regens", "dem Regen", "den Regen", "der Regen"],
                                "correctIndex": 0,
                                "explanation": "trotz 支配第二格（Genitiv）。阳性名词 der Regen 在第二格中冠词为 des，名词词尾加 -s，即 des Regens。"
                            },
                            {
                                "id": "B2_L2_Q2",
                                "type": "EXAM_REAL",
                                "question": "【歌德B2商务信函】句子写道：“Während der Probezeit kann das Arbeitsverhältnis mit einer Frist von zwei Wochen gekündigt werden.” 这意味着：",
                                "options": [
                                    "员工试用期必须工作两周",
                                    "在试用期期间，劳资双方可提前两周通知解除劳动关系",
                                    "劳动合同两周后自动转为正式工",
                                    "试用期内不允许辞职"
                                ],
                                "correctIndex": 1,
                                "explanation": "Probezeit 为“试用期”；mit einer Frist von zwei Wochen 意为“提前两周通知期限”；gekündigt werden 意为“被解除/解约”。"
                            }
                        ]
                    },
                    {
                        "id": "B2_L3",
                        "title": "第3课：不定式与从句复合结构 (Infinitiv mit zu)",
                        "summary": "掌握带 zu 的不定式句 (um... zu, ohne... zu, anstatt... zu) 与情态结构拓展",
                        "grammar": {
                            "title": "带 zu 的不定式 (Infinitivkonstruktionen)",
                            "sections": [
                                {
                                    "heading": "1. 基础 Infinitiv mit zu 结构",
                                    "content": "当主句与从句的主语一致时，可用 Infinitiv mit zu 代替 dass 从句，zu 紧接在动词原形前：\n"
                                               "• 规则动词：Ich habe vor, Deutsch zu lernen.\n"
                                               "• 可分动词：zu 嵌入在前缀与词干之间！\n"
                                               "  例：Er hat vergessen, die Tür abzuschließen (ab + zu + schließen)."
                                },
                                {
                                    "heading": "2. 三大核心复合不定式句型",
                                    "content": "• um... zu + Infinitiv (为了...，表达明确目的，主语必须一致):\n"
                                               "  Ich lerne fleißig Deutsch, um die Goethe-B2-Prüfung zu bestehen.\n"
                                               "• ohne... zu + Infinitiv (没有做...，而做了某事):\n"
                                               "  Er ging aus dem Haus, ohne ein Wort zu sagen.\n"
                                               "• anstatt... zu + Infinitiv (不做...，反而做某事):\n"
                                               "  Er sah den ganzen Tag fern, anstatt für die Prüfung zu lernen."
                                }
                            ]
                        },
                        "words": [
                            {"word": "bestehen", "article": "", "type": "v.", "ipa": "[bəˈʃteːən]", "plural": "besteht, bestand, hat bestanden", "meaning": "通过（考试）；存在", "example": "Ich habe die Goethe-Zertifikat B2 Prüfung bestanden!", "exampleCn": "我顺利通过了歌德B2等级考试！"},
                            {"word": "die Absicht", "article": "die", "type": "n.", "ipa": "[ˈapˌzɪçt]", "plural": "-en", "meaning": "意图，打算", "example": "Ich habe die feste Absicht, in Deutschland zu promovieren.", "exampleCn": "我坚决打算在德国攻读博士学位。"},
                            {"word": "die Fähigkeit", "article": "die", "type": "n.", "ipa": "[ˈfɛːɪçkaɪt]", "plural": "-en", "meaning": "能力，技能", "example": "Analytische Fähigkeiten sind in diesem Beruf unerlässlich.", "exampleCn": "分析能力在这一行业中必不可少。"},
                            {"word": "sich bemühen", "article": "", "type": "v.", "ipa": "[zɪç bəˈmyːən]", "plural": "bemüht sich, bemühte sich, bemüht", "meaning": "尽力，努力", "example": "Wir bemühen uns, den besten Service zu bieten.", "exampleCn": "我们努力提供最优质的服务。"},
                            {"word": "empfehlen", "article": "", "type": "v.", "ipa": "[ɛmˈpfeːlən]", "plural": "empfiehlt, empfahl, empfohlen", "meaning": "推荐，建议", "example": "Der Experte empfiehlt, täglich Vokabeln zu wiederholen.", "exampleCn": "专家建议每天复习词汇。"},
                            {"word": "verzichten", "article": "", "type": "v.", "ipa": "[fɛɐ̯ˈtsɪçtn̩]", "plural": "verzichtet, verzichtete, verzichtet", "meaning": "放弃，舍弃 (接auf + Akk)", "example": "Man sollte auf Einwegplastik verzichten.", "exampleCn": "人们应当放弃使用一次性塑料制品。"},
                            {"word": "die Priorität", "article": "die", "type": "n.", "ipa": "[pʁioʁiˈtɛːt]", "plural": "-en", "meaning": "优先事项，首要地位", "example": "Sicherheit hat für uns oberste Priorität.", "exampleCn": "安全对我们而言具有最高优先级。"},
                            {"word": "entscheiden", "article": "", "type": "v.", "ipa": "[ɛntˈʃaɪdn̩]", "plural": "entscheidet, entschied, entschieden", "meaning": "决定，决断", "example": "Wir haben uns entschieden, das Projekt fortzusetzen.", "exampleCn": "我们已决定继续推进该项目。"}
                        ],
                        "quiz": [
                            {
                                "id": "B2_L3_Q1",
                                "type": "GRAMMAR_FILL",
                                "question": "【目的不定式】请完成句子：“Ich besuche diesen Vorbereitungskurs, ______ die Prüfung zu bestehen.”",
                                "options": ["um", "damit", "ohne", "anstatt"],
                                "correctIndex": 0,
                                "explanation": "当主从句主语相同时，表达“为了达到某目的”使用固定搭配 um... zu + 动词不定式。"
                            },
                            {
                                "id": "B2_L3_Q2",
                                "type": "GRAMMAR_FILL",
                                "question": "【可分动词不定式】可分动词 'einschlafen' 构成带 zu 不定式时的正确形式是：",
                                "options": ["einzuschlafen", "zu einschlafen", "einschlafenzu", "geeinschlafen"],
                                "correctIndex": 0,
                                "explanation": "可分动词构成不定式结构时，zu 必须插在可分前缀与主词干中间：ein + zu + schlafen -> einzuschlafen。"
                            }
                        ]
                    },
                    {
                        "id": "B2_L4",
                        "title": "第4课：新闻报道与第一虚拟式 (Konjunktiv I)",
                        "summary": "掌握第一虚拟式 (Konjunktiv I) 在新闻报道与间接引语 (Indirekte Rede) 中的专业运用",
                        "grammar": {
                            "title": "间接引语与第一虚拟式 (Konjunktiv I)",
                            "sections": [
                                {
                                    "heading": "1. 第一虚拟式核心功能",
                                    "content": "德语新闻、学术论文、司法与正式媒体中，转述他人言论必须保持中立与客观，使用第一虚拟式表明【这是引述第三方的说法，作者不作真伪担保】。\n"
                                               "例：Der Minister sagte, die Lage sei unter Kontrolle."
                                },
                                {
                                    "heading": "2. 构成法与核心变位",
                                    "content": "词干 + -e, -est, -e, -en, -et, -en\n"
                                               "• 核心动词 sein 的 Konjunktiv I:\n"
                                               "  ich sei, du seiest, er/sie/es sei, wir seien, ihr seiet, sie/Sie seien\n"
                                               "• 核心动词 haben: er habe\n"
                                               "• 规则：若 Konjunktiv I 与直陈式现在时形式相同时（尤其第1人称与复数），用第二虚拟式 (Konjunktiv II) 或 würde 形式替代！"
                                }
                            ]
                        },
                        "words": [
                            {"word": "die Medien", "article": "die", "type": "n.pl.", "ipa": "[ˈmeːdi̯ən]", "plural": "-", "meaning": "媒体，新闻界", "example": "Die Medien berichten ausführlich über die Verhandlungen.", "exampleCn": "媒体详细报道了此次谈判。"},
                            {"word": "die Aussage", "article": "die", "type": "n.", "ipa": "[ˈaʊsˌzaːɡə]", "plural": "-n", "meaning": "陈述，言论；证词", "example": "Seine Aussage wurde von mehreren Zeugen bestätigt.", "exampleCn": "他的证词得到了多名证人的证实。"},
                            {"word": "behaupten", "article": "", "type": "v.", "ipa": "[bəˈhaʊptn̩]", "plural": "behauptet, behauptete, behauptet", "meaning": "声称，主张", "example": "Der Sprecher behauptete, alle Fristen seien eingehalten worden.", "exampleCn": "发言人声称所有期限均已得到遵守。"},
                            {"word": "die Forschung", "article": "die", "type": "n.", "ipa": "[ˈfɔʁʃʊŋ]", "plural": "-en", "meaning": "科研，学术研究", "example": "Neueste Forschungen belegen den Trend eindeutig.", "exampleCn": "最新科研成果明确证实了这一趋势。"},
                            {"word": "bestätigen", "article": "", "type": "v.", "ipa": "[bəˈʃtɛːtɪɡn̩]", "plural": "bestätigt, bestätigte, bestätigt", "meaning": "证实，确认", "example": "Die offizielle Quelle hat den Bericht soeben bestätigt.", "exampleCn": "官方消息源刚刚证实了这一报道。"},
                            {"word": "die Quelle", "article": "die", "type": "n.", "ipa": "[ˈkvɛlə]", "plural": "-n", "meaning": "来源，出处", "example": "Journalisten müssen ihre Quellen gewissenhaft prüfen.", "exampleCn": "记者必须严谨核实其消息来源。"},
                            {"word": "offiziell", "article": "", "type": "adj.", "ipa": "[ɔfiˈtsi̯ɛl]", "plural": "", "meaning": "官方的，正式的", "example": "Es gibt dazu noch keine offizielle Stellungnahme.", "exampleCn": "对此尚无任何官方声明。"},
                            {"word": "kritisieren", "article": "", "type": "v.", "ipa": "[kʁitiˈziːʁən]", "plural": "kritisiert, kritisierte, kritisiert", "meaning": "批评，指责", "example": "Experten kritisieren den übermäßigen Bürokratieaufwand.", "exampleCn": "专家批评了过度的官僚主义程序负担。"}
                        ],
                        "quiz": [
                            {
                                "id": "B2_L4_Q1",
                                "type": "GRAMMAR_FILL",
                                "question": "【新闻间接引语】“Der Kanzler betont, die Reform ______ (sein) notwendig.” 请选出第一虚拟式正确形式：",
                                "options": ["sei", "wäre", "ist", "sind"],
                                "correctIndex": 0,
                                "explanation": "sein 动词第三人称单数的第一虚拟式（Konjunktiv I）标准形式为 sei (die Reform sei notwendig)。"
                            },
                            {
                                "id": "B2_L4_Q2",
                                "type": "EXAM_REAL",
                                "question": "【歌德B2阅读理解】报刊评论中出现“Laut Sprecher habe der Konzern keine Fehler gemacht.” 其语体色彩是：",
                                "options": [
                                    "作者完全赞同发言人的观点",
                                    "客观引述发言人的原话，作者并不对该说法真实性直接背书",
                                    "作者认为该说法一定是谎言",
                                    "该事件是虚构的假新闻"
                                ],
                                "correctIndex": 1,
                                "explanation": "使用第一虚拟式（habe gemacht）结合引语来源标记（Laut Sprecher），是德语权威新闻报道中保持客观中立转述的经典标准规范。"
                            }
                        ]
                    },
                    {
                        "id": "B2_L5",
                        "title": "第5课：状态被动与情态推测 (Zustand & Subjektive Modalverben)",
                        "summary": "掌握状态被动 (Zustandspassiv: sein + Partizip II)、情态动词主观推测用法、歌德B2全套应考通关",
                        "grammar": {
                            "title": "状态被动态与情态动词主观推测 (Subjektive Bedeutung)",
                            "sections": [
                                {
                                    "heading": "1. 状态被动 (Zustandspassiv) vs 过程被动 (Vorgangspassiv)",
                                    "content": "• 过程被动态 (werden + Partizip II)：强调【动作正在发生或执行的过程】\n"
                                               "  Die Tür wird um 8 Uhr geschlossen. (门在8点被关上 - 强调关门的动作)\n"
                                               "• 状态被动态 (sein + Partizip II)：强调【动作完成后已经处于并保持的状态】\n"
                                               "  Die Tür ist geschlossen. (门是关着的 - 强调关着的状态)"
                                },
                                {
                                    "heading": "2. 情态动词的主观推测程度阶梯",
                                    "content": "说话人借由情态动词对某事件发生的【真实概率】进行主观推断：\n"
                                               "• müssen (100% 必然，毫无疑问): Er muss zu Hause sein, sein Auto steht vor der Tür.\n"
                                               "• dürfte (约75% 很可能，符合逻辑): Er dürfte den Zug pünktlich erreicht haben.\n"
                                               "• könnte / mag (约50% 也许，不确定): Er könnte im Stau stehen.\n"
                                               "• kann nicht (0% 绝不可能): Das kann unmöglich wahr sein!"
                                }
                            ]
                        },
                        "words": [
                            {"word": "die Voraussetzung", "article": "die", "type": "n.", "ipa": "[foːɐ̯ˈʔaʊsˌzɛtsʊŋ]", "plural": "-en", "meaning": "前提条件，必要素养", "example": "C1-Sprachkenntnisse sind eine zwingende Voraussetzung für das Studium.", "exampleCn": "C1语言水平是大学入学的硬性前提条件。"},
                            {"word": "die Herausforderung", "article": "die", "type": "n.", "ipa": "[hɛˈʁaʊsˌfɔʁdəʁʊŋ]", "plural": "-en", "meaning": "挑战，艰巨任务", "example": "Der demografische Wandel stellt eine große gesellschaftliche Herausforderung dar.", "exampleCn": "人口结构转型构成了一项重大的社会挑战。"},
                            {"word": "der Fortschritt", "article": "der", "type": "n.", "ipa": "[ˈfɔʁtˌʃʁɪt]", "plural": "-e", "meaning": "进步，飞跃", "example": "Wissenschaftliche Fortschritte verbessern unsere Lebensqualität.", "exampleCn": "科技进步改善着我们的生活质量。"},
                            {"word": "die Nachhaltigkeit", "article": "die", "type": "n.", "ipa": "[ˈnaːxˌhaltɪçkaɪt]", "plural": "-", "meaning": "可持续性，持久性", "example": "Ökologische Nachhaltigkeit steht im Mittelpunkt moderner Politik.", "exampleCn": "生态可持续性位于现代政策的核心地位。"},
                            {"word": "bewältigen", "article": "", "type": "v.", "ipa": "[bəˈvɛltɪɡn̩]", "plural": "bewältigt, bewältigte, bewältigt", "meaning": "克服，战胜，胜任", "example": "Mit vereinten Kräften können wir jede Krise bewältigen.", "exampleCn": "齐心协力我们就能克服任何危机。"},
                            {"word": "der Unterschied", "article": "der", "type": "n.", "ipa": "[ˈʊntɐˌʃiːt]", "plural": "-e", "meaning": "区别，差异", "example": "Es besteht ein gravierender Unterschied zwischen beiden Konzepten.", "exampleCn": "两个方案之间存在着重大差异。"},
                            {"word": "die Perspektive", "article": "die", "type": "n.", "ipa": "[pɛʁspɛkˈtiːvə]", "plural": "-n", "meaning": "视角，前瞻视角", "example": "Wir müssen das Problem aus einer ganz neuen Perspektive betrachten.", "exampleCn": "我们必须从一个全新的视角来审视这个问题。"},
                            {"word": "reibungslos", "article": "", "type": "adj.", "ipa": "[ˈʁaɪbʊŋsˌloːs]", "plural": "", "meaning": "顺利的，无摩擦的", "example": "Der Ablauf der Veranstaltung verlief absolut reibungslos.", "exampleCn": "活动的整个流程进行得绝对顺利。"}
                        ],
                        "quiz": [
                            {
                                "id": "B2_L5_Q1",
                                "type": "GRAMMAR_FILL",
                                "question": "【状态被动态】请选出状态被动态表达：“Das Geschäft ______ bereits ______ (sein + Partizip II, 商店已经关门打烊了).”",
                                "options": [
                                    "ist ... geschlossen",
                                    "wird ... geschlossen",
                                    "wurde ... geschlossen",
                                    "hat ... geschlossen"
                                ],
                                "correctIndex": 0,
                                "explanation": "状态被动表示动作完成后呈现并保持的状态，由 sein + Partizip II 构成：Das Geschäft ist bereits geschlossen。"
                            },
                            {
                                "id": "B2_L5_Q2",
                                "type": "GRAMMAR_FILL",
                                "question": "【情态推测】根据证据做出100%确定推断：“他的车停在楼下，他______一定在家。”",
                                "options": [
                                    "muss zu Hause sein",
                                    "könnte zu Hause sein",
                                    "darf zu Hause sein",
                                    "will zu Hause sein"
                                ],
                                "correctIndex": 0,
                                "explanation": "情态动词 müssen 用于主观推测时表示“极大概率/必然如此”（毫无疑问必然在），因此用 muss zu Hause sein。"
                            },
                            {
                                "id": "B2_L5_Q3",
                                "type": "EXAM_REAL",
                                "question": "【歌德B2应考冲刺】在歌德B2口语第一部分（Vortrag 命题演讲）中，获取高分的最关键策略是：",
                                "options": [
                                    "背诵一篇范文且语速越快越好",
                                    "结构清晰：引言、阐述自身经历与本国现状、对比多种方案利弊并得出结论，合理使用B2连接词",
                                    "只用最简单的句子以保证没有任何语法错误",
                                    "全程使用第一人称只讲个人情感故事"
                                ],
                                "correctIndex": 1,
                                "explanation": "歌德B2口语评分标准重点考察逻辑框架结构、连接词多样性（zweisilbige Konnektoren）、多角度权衡利弊（Vor- und Nachteile abwägen）以及论点说服力。"
                            }
                        ]
                    }
                ]
            }
        ]
    }

def main():
    curriculum = get_full_curriculum()
    out_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(out_dir)
    
    # 1. Output to tools/curriculum.json
    local_json_path = os.path.join(out_dir, "curriculum.json")
    with open(local_json_path, "w", encoding="utf-8") as f:
        json.dump(curriculum, f, ensure_ascii=False, indent=2)
    print(f"[OK] Generated {local_json_path}")
    
    # 2. Output directly to Android app assets
    assets_dir = os.path.join(project_root, "android", "app", "src", "main", "assets")
    os.makedirs(assets_dir, exist_ok=True)
    android_asset_path = os.path.join(assets_dir, "curriculum_data.json")
    with open(android_asset_path, "w", encoding="utf-8") as f:
        json.dump(curriculum, f, ensure_ascii=False, indent=2)
    print(f"[OK] Generated {android_asset_path}")

    # Summary statistics
    total_lessons = sum(len(lvl["lessons"]) for lvl in curriculum["levels"])
    total_words = sum(len(les["words"]) for lvl in curriculum["levels"] for les in lvl["lessons"])
    total_quizzes = sum(len(les["quiz"]) for lvl in curriculum["levels"] for les in lvl["lessons"])
    
    print("=" * 60)
    print("DeutschMeister Curriculum Generation Summary:")
    print(f"Total Levels: {len(curriculum['levels'])} (A0, A1, A2, B1, B2)")
    print(f"Total Lessons (Lektionen): {total_lessons}")
    print(f"Total Core Goethe Words (with IPA, Audio, Examples): {total_words}")
    print(f"Total Goethe Exam & Grammar Quiz Questions: {total_quizzes}")
    print("=" * 60)

if __name__ == "__main__":
    main()
