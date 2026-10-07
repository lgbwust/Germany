#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive Quiz Bank for Level A0 (Phonetics & Alphabet):
5 Lessons, 8 in-depth questions per lesson = 40 total questions.
Covers German alphabet, Sonderzeichen, vowels (long/short), diphthongs, consonants (ch, sp, st, ig), and intonation.
"""

A0_QUIZZES = {
    "A0_L1": [
        {
            "id": "A0_L1_Q1",
            "type": "PRONUNCIATION",
            "question": "德语特有字母 'ß' (Eszett) 的发音特征是什么？",
            "options": ["发英语的 [z] 浊辅音", "永远发清辅音 [s]，绝不发浊音", "发双唇爆破音 [b]", "发小舌颤音 [r]"],
            "correctIndex": 1,
            "explanation": "德语中的字母 ß（称为 Eszett 或 scharfes S）永远发清辅音 [s]，如 Straße [ˈʃtʁaːsə], heißen [ˈhaɪsn̩]，且前接长元音或双元音。"
        },
        {
            "id": "A0_L1_Q2",
            "type": "GRAMMAR_FILL",
            "question": "德语最核心的大小写书写铁律是：",
            "options": ["只有人名和地名首字母才大写", "所有名词（无论是具体还是抽象名词）首字母必须大写", "只有句首单词首字母大写", "动词和形容词随意大写"],
            "correctIndex": 1,
            "explanation": "德语是现代语言中极少数保留名词首字母大写规则的语言，所有普通名词、物质名词、抽象名词和专有名词，首字母一律强制大写！"
        },
        {
            "id": "A0_L1_Q3",
            "type": "PRONUNCIATION",
            "question": "德语变音字母 'ä' 在单词 'Äpfel' (苹果复数) 中的发音最接近汉语拼音或国际音标的哪个音？",
            "options": ["汉语拼音 a [a]", "类似 [e] 或 [ɛ] 的开口扁平音", "英语中的 [uː]", "小舌音 [ʁ]"],
            "correctIndex": 1,
            "explanation": "ä 的口型扁平，开口度类似发 [e] 或短音 [ɛ]，Äpfel 发音为 [ˈɛpfl̩]，Käse 发音为 [ˈkɛːzə]。"
        },
        {
            "id": "A0_L1_Q4",
            "type": "PRONUNCIATION",
            "question": "发德语变音字母 'ö' (如 Öl, schön) 时，正确的口型动作是：",
            "options": ["完全张大嘴发拼音 o", "先摆出发 [e] 的舌位，舌头不动，双唇用力向前收圆突出", "舌尖顶住上齿龈发 [t]", "直接发英语的 [ə]"],
            "correctIndex": 1,
            "explanation": "ö 是圆唇前元音，发音要领是保持发 [e] 的舌位不变，双唇向前聚圆凸起发声。"
        },
        {
            "id": "A0_L1_Q5",
            "type": "PRONUNCIATION",
            "question": "德语变音字母 'ü' (如 Tür, über) 的标准口型最类似：",
            "options": ["英语中的 [iː]", "舌位保持发 [i]（如中文‘衣’），双唇用力向前收聚成小圆孔", "汉语拼音的 u", "英语中的 [w]"],
            "correctIndex": 1,
            "explanation": "ü 发音要领是舌位在 [i] 处，双唇用力向前收聚突出成小圆孔（类似汉语拼音 ü），发出的长音为 [yː] 或短音 [ʏ]。"
        },
        {
            "id": "A0_L1_Q6",
            "type": "GRAMMAR_FILL",
            "question": "根据德语正字法改革规则，'Straße' 用 ß 而 'Fluss' 用 ss，原因在于：",
            "options": ["纯属历史习惯，无规律可循", "长元音或双元音后拼写作 ß，短元音后拼写作 ss", "只有在词尾才用 ss", "瑞士德语必须使用 ß"],
            "correctIndex": 1,
            "explanation": "德语正字法铁律：长元音或双元音后拼写为 ß（Straße 的 a 为长音），而短元音后必须拼写为 ss（Fluss 的 u 为短音，küssen 的 ü 为短音）。"
        },
        {
            "id": "A0_L1_Q7",
            "type": "VOCAB_MEANING",
            "question": "动词 'buchstabieren' 在德语课堂中是什么意思？",
            "options": ["大声朗读课文", "拼读、按字母拼写出单词", "背诵德语文法", "造句练习"],
            "correctIndex": 1,
            "explanation": "buchstabieren 来源于 der Buchstabe（字母），意为“按字母逐个拼读/拼写”。例如：Können Sie Ihren Namen buchstabieren?"
        },
        {
            "id": "A0_L1_Q8",
            "type": "GRAMMAR_FILL",
            "question": "在书信或交际中，表示尊称的代词 '您 / 您们' (Sie) 及其物主代词：",
            "options": ["只有在句首才大写", "首字母必须永远大写 (Sie / Ihr / Ihnen)", "首字母永远小写", "与普通的 sie (她/他们) 没有任何书写区别"],
            "correctIndex": 1,
            "explanation": "德语中表示尊称的 Sie（您/您们）、Ihr（您的/您们的）以及第三格 Ihnen，在句中任何位置首字母【必须大写】，以此与第三人称 sie（她/他们）区别并示礼貌。"
        }
    ],
    "A0_L2": [
        {
            "id": "A0_L2_Q1",
            "type": "PRONUNCIATION",
            "question": "在德语中，下列哪种情况下的元音【必须读长音】？",
            "options": ["元音字母后紧跟两个相同辅音字母", "元音字母重叠（如 Tee, Boot, Paar）或后跟延音符 h（如 Zahn）", "元音后有两个不同辅音字母", "在句末感叹词中"],
            "correctIndex": 1,
            "explanation": "元音读长音三大铁律：① 元音重叠 (Tee, Boot, Paar)；② 元音后带有不发音的延音符 h (Zahn, Bahn, wohnen)；③ 开音节或相对开音节。"
        },
        {
            "id": "A0_L2_Q2",
            "type": "PRONUNCIATION",
            "question": "元音字母后紧跟两个相同辅音字母（双辅音，如 Bett, Kamm, hoffen），前面的元音：",
            "options": ["必须读长音", "必须读短音", "可以自由选择长短", "完全不发音"],
            "correctIndex": 1,
            "explanation": "双辅音（tt, mm, ff, pp 等）是德语判定短元音的标志！元音后紧跟双辅音时，元音发音短促有力，如 Bett [bɛt], Kamm [kam]。"
        },
        {
            "id": "A0_L2_Q3",
            "type": "PRONUNCIATION",
            "question": "单词 'die Bahn' (铁路) 与 'der Bann' (驱逐) 在发音上的关键区别是：",
            "options": ["辅音 b 发音不同", "Bahn 的 a 读长音 [aː]，Bann 的 a 读短音 [an]", "重音位置不同", "Bann 读成双元音"],
            "correctIndex": 1,
            "explanation": "die Bahn 有延音符 h，a 发长音 [baːn]；der Bann 后面是双辅音 nn，a 发短音 [ban]。长短音具有区别词义的决定性作用！"
        },
        {
            "id": "A0_L2_Q4",
            "type": "PRONUNCIATION",
            "question": "单词 'der Staat' (国家) 与 'die Stadt' (城市) 的读音区别是：",
            "options": ["Staat 是短元音，Stadt 是长元音", "Staat 带有重叠 aa 读长音 [ʃtaːt]，Stadt 后接 dt 读短音 [ʃtat]", "两者发音完全相同", "Stadt 结尾的 d 不发音"],
            "correctIndex": 1,
            "explanation": "der Staat 包含重叠元音 aa，读长音 [ʃtaːt]；die Stadt 后面跟有两个辅音 dt，元音 a 必须读短音 [ʃtat]。这是听力考试极高频考点！"
        },
        {
            "id": "A0_L2_Q5",
            "type": "PRONUNCIATION",
            "question": "单词 'das Beet' (花坛) 与 'das Bett' (床) 的发音对比是：",
            "options": ["Beet 读短音，Bett 读长音", "Beet 重叠 ee 读长音 [beːt]，Bett 紧跟 tt 读短音 [bɛt]", "两者词义相同", "Bett 的 t 必须重读两次"],
            "correctIndex": 1,
            "explanation": "das Beet (ee 读闭口长音 [eː]) vs. das Bett (tt 读开口短音 [bɛt])，长短音直接决定单词是花坛还是床！"
        },
        {
            "id": "A0_L2_Q6",
            "type": "PRONUNCIATION",
            "question": "非重读音节及词尾弱读的字母 'e'（如 bitte, Name, haben）发什么音？",
            "options": ["长音 [eː]", "央元音 Schwa-Laut [ə]（类似拼音轻读的 'e'）", "发成拼音 i", "发成双元音 [aɪ]"],
            "correctIndex": 1,
            "explanation": "在德语非重读音节及词尾中，字母 e 弱化为央元音 [ə]（倒 e，Schwa 音），口型自然放松微开。"
        },
        {
            "id": "A0_L2_Q7",
            "type": "PRONUNCIATION",
            "question": "德语非重读词尾组合 '-er'（如 Vater, Wasser, Lehrer）在标准德语中的正确读法是：",
            "options": ["发英语中强烈的卷舌音 r", "弱化为舌根半元音 [ɐ]（类似口型微开的短 a）", "发成清辅音 [s]", "完全吞音不发音"],
            "correctIndex": 1,
            "explanation": "标准德语中非重读词尾 -er 不卷舌，而是弱化为舌根半元音 [ɐ]，如 der Vater [ˈfaːtɐ]，切忌带出美语卷舌音！"
        },
        {
            "id": "A0_L2_Q8",
            "type": "VOCAB_MEANING",
            "question": "动词成对辨析：'fühlen' 与 'füllen' 的语义分别是：",
            "options": ["fühlen (装满) / füllen (感觉)", "fühlen (感觉/觉得) / füllen (装满/注满)", "两者都是填空的意思", "fühlen 是走，füllen 是跑"],
            "correctIndex": 1,
            "explanation": "fühlen 含有延音符 h，ü 读长音 [ˈfyːlən]，意为“感觉、摸”；füllen 含有双辅音 ll，ü 读短音 [ˈfʏlən]，意为“填满、装满”。"
        }
    ],
    "A0_L3": [
        {
            "id": "A0_L3_Q1",
            "type": "PRONUNCIATION",
            "question": "德语字母组合 'ei' 和 'ai' (如 mein, klein, Mai) 发什么音？",
            "options": ["发长元音 [eː]", "发复合双元音 [aɪ]（类似英语 'eye' 或拼音 'ai'）", "发拼音 ei", "发双元音 [ɔʏ]"],
            "correctIndex": 1,
            "explanation": "ei 和 ai 在德语中完全同音，均发双元音 [aɪ]，口型由开音 [a] 迅速滑向闭音 [ɪ]。"
        },
        {
            "id": "A0_L3_Q2",
            "type": "PRONUNCIATION",
            "question": "德语字母组合 'eu' 和 'äu' (如 neu, heute, Bäume) 发什么音？",
            "options": ["发拼音 ou", "发长音 [uː]", "发复合双元音 [ɔʏ]（由半开圆唇 [ɔ] 滑向闭唇 [ʏ]）", "发双元音 [aʊ]"],
            "correctIndex": 2,
            "explanation": "eu 与 äu 在德语中完全同音，均发双元音 [ɔʏ]，如 neu [nɔʏ], heute [ˈhɔʏtə], die Bäume [ˈbɔʏmə]。"
        },
        {
            "id": "A0_L3_Q3",
            "type": "PRONUNCIATION",
            "question": "德语字母组合 'ie' (如 die Liebe, sieben, wie) 的发音要领是：",
            "options": ["发复合双元音 [aɪ]", "发长元音 [iː]，i 后的 e 是延音标志", "发拼音 ie [jɛ]", "发短元音 [ɪ]"],
            "correctIndex": 1,
            "explanation": "ie 绝不是双元音！在德语中，i 后面加 e 是传统的拉长音标志，读纯正的长元音 [iː]，如 die Liebe [ˈliːbə]。"
        },
        {
            "id": "A0_L3_Q4",
            "type": "PRONUNCIATION",
            "question": "极易混淆词对辨析：'das Lied' 与 'das Leid' 的发音与词义是：",
            "options": ["Lied [laɪt] 痛苦 / Leid [liːt] 歌曲", "Lied [liːt] 歌曲 / Leid [laɪt] 痛苦、悲伤", "两者同音同义", "Lied 是轻，Leid 是重"],
            "correctIndex": 1,
            "explanation": "Lied 含有 ie 读长音 [liːt]（歌曲）；Leid 含有 ei 读双元音 [laɪt]（痛苦）。看第二个字母：后 e 发 i 的长音，后 i 往 i 滑动发 [aɪ]！"
        },
        {
            "id": "A0_L3_Q5",
            "type": "PRONUNCIATION",
            "question": "词对辨析：'die Miete' 与 'die Meite' 的读音分别是：",
            "options": ["Miete [ˈmiːtə] (租金) / Meite [ˈmaɪtə] (麦堆)", "Miete [ˈmaɪtə] / Meite [ˈmiːtə]", "两者均发 [miːtə]", "两者均发 [mɛtə]"],
            "correctIndex": 0,
            "explanation": "die Miete (含有 ie) 读 [ˈmiːtə]，意为房租租金；含有 ei 的组合读 [ˈmaɪtə]。"
        },
        {
            "id": "A0_L3_Q6",
            "type": "GRAMMAR_FILL",
            "question": "为什么名词 'der Baum' 变复数写成 'die Bäume' 而不是 'die Beume'？",
            "options": ["纯拼写错误", "词根含有 au 的名词复数时规则变音为 äu，保持词根形态亲缘性", "发音与 eu 不同", "古代方言残余"],
            "correctIndex": 1,
            "explanation": "德语词元学规律：含有 au 的词根变复数时变音为 äu (der Baum -> die Bäume; das Haus -> die Häuser)，拼写上显示与单数原词的亲缘关系。"
        },
        {
            "id": "A0_L3_Q7",
            "type": "PRONUNCIATION",
            "question": "字母组合 'au' (如 das Haus, die Frau, das Auto) 发什么音？",
            "options": ["发拼音 ao [aʊ]", "发长音 [oː]", "发双唇音 [uː]", "发短元音 [a]"],
            "correctIndex": 0,
            "explanation": "au 发复合双元音 [aʊ]，口型由开元音 [a] 滑向收圆的 [ʊ]，如 das Haus [haʊs], das Auto [ˈaʊtoː]。"
        },
        {
            "id": "A0_L3_Q8",
            "type": "SENTENCE_BUILDER",
            "question": "朗读句子 'Mein Haus ist neu und klein.' 时，包含了哪几组复合双元音？",
            "options": ["只有 ei 一种", "包含了 ei [aɪ], au [aʊ], eu [ɔʏ] 全部三大双元音", "只有 ie 和 au", "没有双元音"],
            "correctIndex": 1,
            "explanation": "Mein (ei), Haus (au), neu (eu), klein (ei)，一句话经典集齐了德语全部核心复合双元音！"
        }
    ],
    "A0_L4": [
        {
            "id": "A0_L4_Q1",
            "type": "PRONUNCIATION",
            "question": "字母组合 'ch' 在 a, o, u, au 之后（如 das Buch, machen, die Woche, auch）发什么音？",
            "options": ["发硬腭擦音 [ç]（微笑哈气音）", "发深喉舌根擦音 [x]（ach-Laut，清理嗓子音）", "发清辅音 [k]", "发清辅音 [tʃ]"],
            "correctIndex": 1,
            "explanation": "ch 前面是 a, o, u, au 时，必须发深喉擦音 [x]（称为 ach-Laut），如 das Buch [buːx], die Woche [ˈvɔxə]。"
        },
        {
            "id": "A0_L4_Q2",
            "type": "PRONUNCIATION",
            "question": "字母组合 'ch' 在 e, i, ä, ö, ü, eu 以及辅音 l, n, r 之后（如 ich, sprechen, welche）发什么音？",
            "options": ["发深喉擦音 [x]", "发硬腭擦音 [ç]（ich-Laut，咧嘴微笑擦音）", "发清辅音 [ʃ]", "完全不发音"],
            "correctIndex": 1,
            "explanation": "ch 前面是前元音 (e, i, ä, ö, ü, eu) 或辅音 (l, n, r) 时，发硬腭轻擦音 [ç]（称为 ich-Laut），如 ich [ɪç], sprechen [ˈʃpʁɛçn̩]。"
        },
        {
            "id": "A0_L4_Q3",
            "type": "PRONUNCIATION",
            "question": "字母组合 'sp' 和 'st' 位于【词首或词根开头】时（如 sprechen, Sport, Straße, Stadt）读作：",
            "options": ["依然读 [sp] 和 [st]", "s 必须清化发成 [ʃ]，即分别读作 [ʃp] 和 [ʃt]", "s 读成浊辅音 [z]", "p 和 t 不发音"],
            "correctIndex": 1,
            "explanation": "词首及词根开头的 sp 和 st，s 强制读为 [ʃ]！如 der Sport [ʃpɔʁt], die Straße [ˈʃtʁaːsə], sprechen [ˈʃpʁɛçn̩]。"
        },
        {
            "id": "A0_L4_Q4",
            "type": "PRONUNCIATION",
            "question": "字母组合 'sp' 和 'st' 位于【词中或词尾非词根开头】时（如 das Fenster, der Herbst, der Gast）读作：",
            "options": ["读作 [ʃp] 和 [ʃt]", "回归普通清辅音 [sp] 和 [st]", "读成浊音 [zb] 和 [zd]", "不发音"],
            "correctIndex": 1,
            "explanation": "不在词根开头的 sp/st 回归标准清辅音 [sp] 和 [st]，如 das Fenster [ˈfɛnstɐ], der Gast [ɡast]。"
        },
        {
            "id": "A0_L4_Q5",
            "type": "PRONUNCIATION",
            "question": "在标准高地德语 (Hochdeutsch) 中，词尾后缀 '-ig'（如 richtig, wichtig, fleißig）的官方标准读音是：",
            "options": ["发硬音 [ɪk]", "发软腭摩擦音 [ɪç]（同 ich 音）", "发浊音 [ɪɡ]", "发鼻音 [ɪŋ]"],
            "correctIndex": 1,
            "explanation": "根据德国官方标准杜登语音词典和歌德学院规范，词尾 -ig 必须读作 [ɪç]（如 wichtig [ˈvɪçtɪç]）。在后接元音后缀时才恢复 [ɡ]（wichtiger [ˈvɪçtɪɡɐ]）。"
        },
        {
            "id": "A0_L4_Q6",
            "type": "PRONUNCIATION",
            "question": "德语末尾辅音清化律 (Auslautverhärtung) 指的是：",
            "options": ["词尾元音全部变清", "浊辅音字母 b, d, g 位于词末或音节末尾时，必须完全清化发作清辅音 [p], [t], [k]", "词尾辅音必须吞音", "词尾一律发重音"],
            "correctIndex": 1,
            "explanation": "德语发音铁律：浊辅音 b, d, g 在词尾或音节末必须清化！如 der Tag 读 [taːk], und 读 [ʊnt], ab 读 [ap]。"
        },
        {
            "id": "A0_L4_Q7",
            "type": "PRONUNCIATION",
            "question": "德语原生词中字母 'v'（如 der Vater, vier, viel）的标准发音通常是：",
            "options": ["发英语的咬唇浊音 [v]", "发清辅音 [f]（同 f 音）", "发双唇音 [w]", "发双唇半元音 [b]"],
            "correctIndex": 1,
            "explanation": "德语原生词中 v 发清辅音 [f]（der Vater [ˈfaːtɐ], vier [fiːɐ̯]）；只有在少数外来词中才保留浊音 [v]（die Vase [ˈvaːzə]）。"
        },
        {
            "id": "A0_L4_Q8",
            "type": "PRONUNCIATION",
            "question": "字母组合 'sch'（如 schön, Schule, schreiben）的发音要领是：",
            "options": ["发清辅音 [s]", "双唇向前撅起呈圆筒状，发清辅音 [ʃ]", "发复合破擦音 [tʃ]", "发喉擦音 [h]"],
            "correctIndex": 1,
            "explanation": "sch 永远发清辅音 [ʃ]，双唇用力向前收聚撅起，气流摩擦而出，如 schön [ʃøːn], die Schule [ˈʃuːlə]。"
        }
    ],
    "A0_L5": [
        {
            "id": "A0_L5_Q1",
            "type": "PRONUNCIATION",
            "question": "德语原生单根词（如 Vater, Mutter, leben, lernen）的重音通常落在哪个音节？",
            "options": ["最后一个音节", "第一个音节（词根音节）", "倒数第二个音节", "随机无规律"],
            "correctIndex": 1,
            "explanation": "德语原生词具有强烈的词根重音倾向，重音绝大多数落在第一个音节（词根音节）上。"
        },
        {
            "id": "A0_L5_Q2",
            "type": "PRONUNCIATION",
            "question": "德语 8 大不可分前缀 (be-, ge-, er-, ver-, zer-, ent-, emp-, miss-) 的重音规律是：",
            "options": ["永远必须重读", "绝对不重读，重音必须落在后面的词根音节上", "可重读也可轻读", "放在句首时重读"],
            "correctIndex": 1,
            "explanation": "不可分前缀 8 大金刚永远不重读！例如：verstehen [fɛɐ̯ˈʃteːən], beginnen [bəˈɡɪnən], erzählen [ɛɐ̯ˈtsɛːlən]。"
        },
        {
            "id": "A0_L5_Q3",
            "type": "PRONUNCIATION",
            "question": "可分动词前缀（如 auf-, an-, aus-, ein-, mit-, vor-）在动词原形中的重音规律是：",
            "options": ["从不重读", "必须重读 (Betontes Präfix)", "重读在词尾 -en 上", "只有在从句中才重读"],
            "correctIndex": 1,
            "explanation": "可分动词的前缀在动词原形中必须重读！如 aufstehen [ˈaʊfˌʃteːən], anrufen [ˈanˌʁuːfn̩], mitkommen [ˈmɪtˌkɔmən]。"
        },
        {
            "id": "A0_L5_Q4",
            "type": "PRONUNCIATION",
            "question": "陈述句与特殊疑问句 (W-Frage，如 Woher kommen Sie?) 的句调通常采用：",
            "options": ["升调 ↗ (Steigende Melodie)", "降调 ↘ (Fallende Melodie)", "平调 →", "高声叹调"],
            "correctIndex": 1,
            "explanation": "陈述句、特殊疑问句以及祈使句，句子末尾语调自然下沉，采用降调 ↘。"
        },
        {
            "id": "A0_L5_Q5",
            "type": "PRONUNCIATION",
            "question": "是非疑问句 (Ja/Nein-Frage，如 Kommen Sie aus China?) 的句调通常采用：",
            "options": ["降调 ↘", "升调 ↗ (Steigende Melodie)", "降升调 ↘↗", "完全无语调起伏"],
            "correctIndex": 1,
            "explanation": "是非问句（动词首位的问句）句尾必须明显向上扬起，采用升调 ↗ 以提示对方做出判定回答。"
        },
        {
            "id": "A0_L5_Q6",
            "type": "PRONUNCIATION",
            "question": "德语特有的'喉塞音' (Knacklaut / Glottisschlag [ʔ]) 在什么情况下产生？",
            "options": ["在单词末尾辅音处", "在以元音开头的单词或词根前，声带紧闭后气流爆破产生清晰顿挫", "在句末标点符号处", "只在叹气时产生"],
            "correctIndex": 1,
            "explanation": "以元音开头的单词或词根前（如 ein Apfel [ʔaɪn ˈʔapfl̩]），声带紧闭瞬间爆破，不与前词辅音连读，造就了德语字字铿锵的金属质感。"
        },
        {
            "id": "A0_L5_Q7",
            "type": "VOCAB_MEANING",
            "question": "德国人日常见面与告别的最经典礼貌用语是：",
            "options": ["Guten Tag (日安/您好) / Auf Wiedersehen (再见)", "Gute Nacht / Bitte", "Hallo / Entschuldigung", "Danke / Sehr gut"],
            "correctIndex": 0,
            "explanation": "Guten Tag 是全天通用（除深夜清晨外）的正式问候语，Auf Wiedersehen 是标准告别用语（字面意思：期待再次相见）。"
        },
        {
            "id": "A0_L5_Q8",
            "type": "EXAM_REAL",
            "question": "初学者听不懂对方德语时，最地道得体的求助表达是：",
            "options": ["Was?", "Wie bitte? Könnten Sie bitte etwas langsamer sprechen?", "Nein, danke!", "Ich verstehe alles."],
            "correctIndex": 1,
            "explanation": "直接说 'Was?' 非常粗鲁无礼！标准得体的表达是：'Wie bitte? Bitte sprechen Sie etwas langsamer!'（请再说一遍好吗？请说慢一点！）"
        }
    ]
}
