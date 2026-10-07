import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from grammar_data_a0 import A0_GRAMMAR

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Level A0: German Phonetics & Alphabet (5 Comprehensive Lessons)
"""

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
                "grammar": {
                    "title": "德语特有字符与发音入门",
                    "sections": [
                        {
                            "heading": "1. 德语四个特殊字母 (Sonderzeichen)",
                            "content": "德语在26个拉丁字母基础上，增加了4个独特字母：\n"
                                       "• ä [ɛː] / [ɛ]：口型扁平，开口度类似发 [e]，例如：Äpfel [ˈɛpfl̩], Käse [ˈkɛːzə]。\n"
                                       "• ö [øː] / [œ]：先摆出 [e] 的发音口型，然后双唇用力向前突出收圆。例如：Öl [øːl], schön [ʃøːn]。\n"
                                       "• ü [yː] / [ʏ]：舌位保持发 [i] 音，双唇向前聚圆凸起（类似汉语拼音 ü）。例如：über [ˈyːbɐ], Tür [tyːɐ̯]。\n"
                                       "• ß [s]：德语特有的清辅音字母（称为 Eszett 或 scharfes S），发清音 [s]，永远出现在长元音或双元音之后。例如：Straße [ˈʃtʁaːsə], heißen [ˈhaɪsn̩]。"
                        },
                        {
                            "heading": "2. 大小写书写规则",
                            "content": "德语最核心书写铁律：\n"
                                       "所有名词（无论普通名词、人名、国家、抽象名词），【首字母必须大写】！\n"
                                       "句首第一个单词首字母必须大写；尊称代词 Sie / Ihr / Ihnen 首字母必须大写以示礼貌！"
                        }
                    ]
                },
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
                    {"word": "leise", "article": "", "type": "adj./adv.", "ipa": "[ˈlaɪzə]", "plural": "", "meaning": "轻声的，安静的", "example": "Bitte sprechen Sie nicht so leise.", "exampleCn": "请不要这么小声说话。"}
                ],
                "quiz": [
                    {
                        "id": "A0_L1_Q1",
                        "type": "PRONUNCIATION",
                        "question": "德语特有字母 'ß' 的正确发音是：",
                        "options": ["发英语的 [z] 浊音", "发清辅音 [s]", "发双唇破裂音 [b]", "发小舌颤音 [r]"],
                        "correctIndex": 1,
                        "explanation": "德语中 ß（Eszett）永远发清辅音 [s]，前接长元音或双元音。"
                    },
                    {
                        "id": "A0_L1_Q2",
                        "type": "ARTICLE",
                        "question": "请选出名词 'Alphabet'（字母表）的正确中性定冠词：",
                        "options": ["der", "die", "das", "den"],
                        "correctIndex": 2,
                        "explanation": "Alphabet 是中性名词，定冠词为 das (das Alphabet)。"
                    }
                ]
            },
            {
                "id": "A0_L2",
                "title": "第2课：元音长短音与发音规则 (Vokale: lang und kurz)",
                "summary": "掌握德语 5 个核心元音 a, e, i, o, u 的长音与短音辨析",
                "grammar": {
                    "title": "元音长短音判定铁律",
                    "sections": [
                        {
                            "heading": "1. 读长元音的三大规则",
                            "content": "• 元音字母重叠时读长音：Tee [teː], Boot [boːt], Paar [paːɐ̯]。\n"
                                       "• 元音后带有不发音的延音符 h 时读长音：Zahn [tsaːn], Uhr [uːɐ̯], Bahn [baːn]。\n"
                                       "• 元音字母后只有一个辅音或处于开音节时读长音：Tag [taːk], gut [ɡuːt], Mut [muːt]。\n"
                                       "• ie 固定发长音 [iː]：sie [ziː], Liebe [ˈliːbə], Bier [biːɐ̯]。"
                        },
                        {
                            "heading": "2. 读短元音的关键特征",
                            "content": "• 元音字母后紧跟两个或两个以上辅音字母时，该元音必须读短音！\n"
                                       "  例如：Bett [bɛt] (双辅音 tt -> 短音 e)，Kamm [kam]，offen [ˈɔfn̩]，Mutter [ˈmʊtɐ]。\n"
                                       "• 短元音发音短促有力，口型通常较长音更为开放松弛。"
                        }
                    ]
                },
                "words": [
                    {"word": "der Tag", "article": "der", "type": "n.", "ipa": "[taːk]", "plural": "-e", "meaning": "白天，日子 (长元音 a)", "example": "Guten Tag! Schön dich zu sehen.", "exampleCn": "你好！很高兴见到你。"},
                    {"word": "die Nacht", "article": "die", "type": "n.", "ipa": "[naxt]", "plural": "Nächte", "meaning": "夜晚，夜间 (短元音 a)", "example": "Gute Nacht und schlaf gut!", "exampleCn": "晚安，睡个好觉！"},
                    {"word": "der Tee", "article": "der", "type": "n.", "ipa": "[teː]", "plural": "-s", "meaning": "茶 (长元音 e)", "example": "Ich trinke morgens gerne heißen Tee.", "exampleCn": "我早上喜欢喝热茶。"},
                    {"word": "das Bett", "article": "das", "type": "n.", "ipa": "[bɛt]", "plural": "-en", "meaning": "床 (短元音 e)", "example": "Das Kind liegt schon im Bett.", "exampleCn": "孩子已经躺在床上了。"},
                    {"word": "die Uhr", "article": "die", "type": "n.", "ipa": "[uːɐ̯]", "plural": "-en", "meaning": "钟表，点钟 (长元音 u)", "example": "Es ist genau acht Uhr.", "exampleCn": "现在刚好八点整。"},
                    {"word": "die Mutter", "article": "die", "type": "n.", "ipa": "[ˈmʊtɐ]", "plural": "Mütter", "meaning": "母亲 (短元音 u)", "example": "Meine Mutter kocht sehr gut.", "exampleCn": "我母亲做饭很好吃。"},
                    {"word": "das Boot", "article": "das", "type": "n.", "ipa": "[boːt]", "plural": "-e", "meaning": "小船，汽艇 (长元音 o)", "example": "Wir fahren mit dem Boot auf dem See.", "exampleCn": "我们乘船在湖上游玩。"},
                    {"word": "die Sonne", "article": "die", "type": "n.", "ipa": "[ˈzɔnə]", "plural": "-n", "meaning": "太阳 (短元音 o)", "example": "Die Sonne scheint heute herrlich.", "exampleCn": "今天阳光明媚灿烂。"},
                    {"word": "das Lied", "article": "das", "type": "n.", "ipa": "[liːt]", "plural": "-er", "meaning": "歌曲 (长元音 ie)", "example": "Wir singen ein deutsches Lied.", "exampleCn": "我们唱一首德语歌。"},
                    {"word": "das Bild", "article": "das", "type": "n.", "ipa": "[bɪlt]", "plural": "-er", "meaning": "画，图片 (短元音 i)", "example": "Das Bild hängt an der Wand.", "exampleCn": "画挂在墙上。"}
                ],
                "quiz": [
                    {
                        "id": "A0_L2_Q1",
                        "type": "PRONUNCIATION",
                        "question": "在单词 'Bett'（床）中，元音字母 'e' 读长音还是短音？",
                        "options": ["读长元音 [e:]", "读短元音 [ɛ]", "发双元音 [ai]", "不发音"],
                        "correctIndex": 1,
                        "explanation": "因为 e 后面紧跟两个相同的辅音字母 tt，所以元音必须读短音 [ɛ]。"
                    }
                ]
            },
            {
                "id": "A0_L3",
                "title": "第3课：复合双元音与拼读规律 (Diphthonge: ei, eu, au, äu)",
                "summary": "攻克德语四大核心双元音 ei, eu, äu, au 的标准拼读",
                "grammar": {
                    "title": "四大双元音发音要领",
                    "sections": [
                        {
                            "heading": "1. 德语核心双元音总结",
                            "content": "• ei / ai [aɪ]：发音类似汉语“爱”，从开口度较大的 [a] 快速滑动至较闭的 [ɪ]。\n"
                                       "  例如：mein, kein, nein, Mai, Kaiser。\n"
                                       "• eu / äu [ɔɪ]：发音类似“奥伊”，从圆唇的 [ɔ] 滑动至 [ʏ]。\n"
                                       "  例如：neu, heute, Europa, Häuser, Bäume。\n"
                                       "• au [aʊ]：发音类似汉语“奥”，从 [a] 滑动到圆唇的 [ʊ]。\n"
                                       "  例如：Haus, Frau, Auto, Baum, laut。"
                        },
                        {
                            "heading": "2. 易混淆对比：ie vs ei",
                            "content": "极度关键辨析：\n"
                                       "• ie 读长音 [i:]（相当于长音 i）：Bier, Liebe, sie, wie。\n"
                                       "• ei 读双元音 [aɪ]（相当于“爱”）：Wein, mein, nein, zwei。\n"
                                       "口诀：哪个字母在后，就发哪个字母相关的音！"
                        }
                    ]
                },
                "words": [
                    {"word": "mein", "article": "", "type": "pron.", "ipa": "[maɪn]", "plural": "", "meaning": "我的 (双元音 ei)", "example": "Das ist mein Buch.", "exampleCn": "这是我的书。"},
                    {"word": "kein", "article": "", "type": "pron.", "ipa": "[kaɪn]", "plural": "", "meaning": "没有，无 (双元音 ei)", "example": "Ich habe keine Zeit.", "exampleCn": "我没有时间。"},
                    {"word": "neu", "article": "", "type": "adj.", "ipa": "[nɔɪ]", "plural": "", "meaning": "新的 (双元音 eu)", "example": "Das Auto ist ganz neu.", "exampleCn": "这辆汽车是崭新的。"},
                    {"word": "heute", "article": "", "type": "adv.", "ipa": "[ˈhɔɪtə]", "plural": "", "meaning": "今天 (双元音 eu)", "example": "Was machst du heute Abend?", "exampleCn": "你今晚做什么？"},
                    {"word": "das Haus", "article": "das", "type": "n.", "ipa": "[haʊs]", "plural": "Häuser", "meaning": "房子 (双元音 au)", "example": "Das Haus hat einen schönen Garten.", "exampleCn": "这座房子有一个漂亮的花园。"},
                    {"word": "die Häuser", "article": "die", "type": "n.pl.", "ipa": "[ˈhɔɪzɐ]", "plural": "-", "meaning": "房屋（复数，双元音 äu）", "example": "In dieser Straße stehen viele moderne Häuser.", "exampleCn": "这条街上立着许多现代化房屋。"},
                    {"word": "die Frau", "article": "die", "type": "n.", "ipa": "[fʁaʊ]", "plural": "-en", "meaning": "女士，妻子 (双元音 au)", "example": "Frau Müller kommt aus Hamburg.", "exampleCn": "穆勒女士来自汉堡。"},
                    {"word": "der Baum", "article": "der", "type": "n.", "ipa": "[baʊm]", "plural": "Bäume", "meaning": "树木 (双元音 au)", "example": "Der Baum ist grün und hoch.", "exampleCn": "这棵树又绿又高。"},
                    {"word": "die Bäume", "article": "die", "type": "n.pl.", "ipa": "[ˈbɔɪmə]", "plural": "-", "meaning": "树木（复数，双元音 äu）", "example": "Im Herbst verlieren die Bäume ihre Blätter.", "exampleCn": "秋天树木落叶。"},
                    {"word": "das Europa", "article": "das", "type": "n.", "ipa": "[ɔɪˈʁoːpa]", "plural": "-", "meaning": "欧洲 (双元音 eu)", "example": "Deutschland liegt in der Mitte von Europa.", "exampleCn": "德国位于欧洲中心。"}
                ],
                "quiz": [
                    {
                        "id": "A0_L3_Q1",
                        "type": "PRONUNCIATION",
                        "question": "单词 'neu' 和 'Häuser' 中的双元音字母组合分别读什么？",
                        "options": ["两者都读 [ɔɪ]（奥伊）", "分别读 [e:] 和 [a:]", "分别读 [ai] 和 [au]", "分别读 [u:] 和 [o:]"],
                        "correctIndex": 0,
                        "explanation": "德语中 eu 和 äu 的标准发音完全一致，皆读作双元音 [ɔɪ]。"
                    }
                ]
            },
            {
                "id": "A0_L4",
                "title": "第4课：特殊辅音组合与软硬音 (Konsonanten: ch, sp, st, sch, ig)",
                "summary": "彻底掌握 ch 软硬音判定、词首 sp/st 吐气破擦音与词尾弱化音",
                "grammar": {
                    "title": "辅音拼读核心避坑指南",
                    "sections": [
                        {
                            "heading": "1. ch 软音 [ç] 与硬音 [x] 铁律",
                            "content": "• 在 a, o, u, au 之后读硬音 [x]（喉部摩擦音，类似吐气）：\n"
                                       "  Bach [bax], Buch [buːx], Loch [lɔx], auch [aʊx]。\n"
                                       "• 在其他元音（e, i, ä, ö, ü, ei, eu）以及辅音 l, n, r 之后，或名词缩小后缀 -chen 中读软音 [ç]（舌面前部抬起轻触硬腭摩擦）：\n"
                                       "  ich [ɪç], nicht [nɪçt], echt [ɛçt], Küche [ˈkʏçə], Mädchen [ˈmɛːtçən]。"
                        },
                        {
                            "heading": "2. sp 与 st 读音规则",
                            "content": "• 位于【词首或前缀后】时，s 读成 [ʃ]：\n"
                                       "  Sport [ʃpɔrt], sprechen [ˈʃpʁɛçn̩], Stadt [ʃtat], Stunde [ˈʃtʊndə]。\n"
                                       "• 位于词中或词尾时，恢复普通 [s]：\n"
                                       "  Fenster [ˈfɛnstɐ], Post [pɔst], Last [last]。"
                        }
                    ]
                },
                "words": [
                    {"word": "der Sport", "article": "der", "type": "n.", "ipa": "[ʃpɔʁt]", "plural": "-", "meaning": "体育，运动 (词首 sp 读 [ʃp])", "example": "Ich treibe jeden Tag Sport.", "exampleCn": "我每天做运动。"},
                    {"word": "die Stadt", "article": "die", "type": "n.", "ipa": "[ʃtat]", "plural": "Städte", "meaning": "城市 (词首 st 读 [ʃt])", "example": "Berlin ist eine sehr lebendige Stadt.", "exampleCn": "柏林是一座非常有活力的城市。"},
                    {"word": "das Buch", "article": "das", "type": "n.", "ipa": "[buːx]", "plural": "Bücher", "meaning": "书本 (硬音 ch 读 [x])", "example": "Ich lese ein interessantes Buch.", "exampleCn": "我正在读一本有趣的书。"},
                    {"word": "ich", "article": "", "type": "pron.", "ipa": "[ɪç]", "plural": "", "meaning": "我 (软音 ch 读 [ç])", "example": "Ich lerne gerne Deutsch.", "exampleCn": "我喜欢学习德语。"},
                    {"word": "die Schule", "article": "die", "type": "n.", "ipa": "[ˈʃuːlə]", "plural": "-n", "meaning": "学校 (sch 读 [ʃ])", "example": "Die Kinder gehen um acht Uhr in die Schule.", "exampleCn": "孩子们八点去学校。"},
                    {"word": "wichtig", "article": "", "type": "adj.", "ipa": "[ˈvɪçtɪç]", "plural": "", "meaning": "重要的 (词尾 -ig 读 [ɪç])", "example": "Das ist eine wichtige Regel.", "exampleCn": "这是一条重要规则。"},
                    {"word": "das Fenster", "article": "das", "type": "n.", "ipa": "[ˈfɛnstɐ]", "plural": "-", "meaning": "窗户 (词中 st 读 [st])", "example": "Bitte öffnen Sie das Fenster!", "exampleCn": "请打开窗户！"},
                    {"word": "der Wasser", "article": "das", "type": "n.", "ipa": "[ˈvasɐ]", "plural": "-", "meaning": "水 (w 读 [v])", "example": "Wasser ist gesund.", "exampleCn": "水是有益健康的。"},
                    {"word": "der Vogel", "article": "der", "type": "n.", "ipa": "[ˈfoːɡl̩]", "plural": "Vögel", "meaning": "鸟 (本族词 v 读 [f])", "example": "Der Vogel singt im Baum.", "exampleCn": "鸟儿在树上歌唱。"},
                    {"word": "die Vase", "article": "die", "type": "n.", "ipa": "[ˈvaːzə]", "plural": "-n", "meaning": "花瓶 (外来词 v 读 [v])", "example": "Die Blumen stehen in der Vase.", "exampleCn": "花插在花瓶里。"}
                ],
                "quiz": [
                    {
                        "id": "A0_L4_Q1",
                        "type": "PRONUNCIATION",
                        "question": "在单词 'ich' 和 'Küche' 中，字母组合 'ch' 发什么音？",
                        "options": ["发硬音 [x]", "发软音 [ç]", "发清辅音 [k]", "发破擦音 [tʃ]"],
                        "correctIndex": 1,
                        "explanation": "在 i, ü 等前元音后，ch 发舌面软音 [ç]。"
                    }
                ]
            },
            {
                "id": "A0_L5",
                "title": "第5课：德语重音、词尾弱化与综合拼读实战 (Betonung & Intonation)",
                "summary": "掌握德语单词重音规律、词尾 -e / -en / -er 的弱化发音与基础句调",
                "grammar": {
                    "title": "重音规律与音调",
                    "sections": [
                        {
                            "heading": "1. 单词重音基本规律",
                            "content": "• 德语本土词绝大多数重音在【第一个音节】（根词干）：\n"
                                       "  Mutter [ˈmʊtɐ], Fenster [ˈfɛnstɐ], arbeiten [ˈaʁbaɪtn̩]。\n"
                                       "• 不可分前缀 (be-, ge-, ent-, emp-, er-, ver-, zer-, miss-) 【永远不重读】，重音落在紧随其后的词根上！\n"
                                       "  bekommen [bəˈkɔmən], verstehen [fɛɐ̯ˈʃteːən], erzählen [ɛɐ̯ˈtsɛːlən]。\n"
                                       "• 可分前缀 (auf-, an-, ab-, aus-, ein-, mit-) 【永远重读】：\n"
                                       "  ˈaufstehen, ˈanrufen, ˈeinkaufen。"
                        },
                        {
                            "heading": "2. 词尾弱化音规律",
                            "content": "• 词尾非重读的 -e 弱化为央元音 [ə]（发轻短“呃”音）：Name [ˈnaːmə], Bitte [ˈbɪtə]。\n"
                                       "• 词尾 -er 弱化为低央元音 [ɐ]（类似非常短促轻柔的“啊”）：Mutter [ˈmʊtɐ], Vater [ˈfaːtɐ], Lehrer [ˈleːʁɐ]。\n"
                                       "• 词尾 -en 弱化为成音节鼻辅音 [n̩]：lernen [ˈlɛʁnən / ˈlɛʁnn̩]。"
                        }
                    ]
                },
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
                    {"word": "die Übung", "article": "die", "type": "n.", "ipa": "[ˈyːbʊŋ]", "plural": "-en", "meaning": "练习，训练", "example": "Übung macht den Meister.", "exampleCn": "熟能生巧（练习造就大师）。"}
                ],
                "quiz": [
                    {
                        "id": "A0_L5_Q1",
                        "type": "PRONUNCIATION",
                        "question": "动词 'verstehen'（理解）的重音落在哪个音节上？",
                        "options": ["在第一个音节 ver- 上", "在第二个音节 -steh- 上", "平均用力", "在词尾 -en 上"],
                        "correctIndex": 1,
                        "explanation": "ver- 是德语不可分前缀，永远不重读，重音落在词根音节 -steh- 上。"
                    }
                ]
            }
        ]
    }

    for l in data["lessons"]:
        if l["id"] in A0_GRAMMAR:
            l["grammar"] = A0_GRAMMAR[l["id"]]
    return data
