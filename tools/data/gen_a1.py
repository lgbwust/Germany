#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A1 Generator: 15 Lessons x 70 words = 1050 Words
Covers:
L01: Begrüßung, Kennenlernen & Länder (问候与相识)
L02: Familie, Verwandtschaft & Personen (家庭与人际)
L03: Lebensmittel, Essen & Supermarkt (食材与超市)
L04: Restaurant, Mahlzeiten & Bestellen (餐饮与点餐)
L05: Wohnen, Wohnung & Möbel (租房与家具)
L06: Zeit, Alltag, Wochentage & Uhrzeit (作息与时间)
L07: Berufe & Arbeitsplatz (职业与工作)
L08: Körperteile, Befinden & Gesundheit (身体与健康)
L09: Stadt, Orte & Verkehrsmittel (城市与交通)
L10: Kleidung, Farben & Einkaufen (服饰与商场)
L11: Freizeit, Hobbys & Sport (爱好与运动)
L12: Wetter, Klima & Natur (天气与自然)
L13: Feste, Feiern & Einladungen (节日与社交)
L14: Zahlen, Maße, Gewichte & Geld (数字与货币)
L15: Goethe A1 Prüfungstraining & Gesamtwiederholung (歌德A1全真冲刺)
"""

import json
import os

def generate_a1_file():
    out_file = os.path.join(os.path.dirname(__file__), "data_a1.py")
    print(f"Generating {out_file}...")

    # We will write the Python file that exports get_level_a1()
    # Each lesson has 70 items
    code_lines = [
        "#!/usr/bin/env python3",
        "# -*- coding: utf-8 -*-",
        "from .make_data import build_lesson",
        "",
        "def get_level_a1():",
        "    lessons = []",
        ""
    ]

    lessons_spec = [
        ("A1_L01", "第1课：相识、寒暄与国籍 (Begrüßung & Länder)",
         "掌握人称代词、动词变位基础、sein/haben/heißen、国家与国籍表达",
         "动词现在时变位规则 (Präsens) 与基础疑问句",
         [
             {"heading": "1. 规则动词现在时词尾", "content": "ich -e, du -st, er/sie/es -t, wir -en, ihr -t, sie/Sie -en。\n例如：lernen (ich lerne, du lernst, er lernt, wir lernen, ihr lernt, sie lernen)。"},
             {"heading": "2. 陈述句与疑问句语序", "content": "• 陈述句：动词永远占第二位！(Ich komme aus China.)\n• 特殊疑问句(W-Frage)：疑问词在第一位，动词在第二位！(Woher kommen Sie?)\n• 一般疑问句(Ja/Nein-Frage)：动词位于句首第一位！(Lernst du Deutsch?)"}
         ],
         [
             {"id": "A1_L01_Q1", "type": "GRAMMAR_FILL", "question": "Woher ______ du? - Ich ______ aus Deutschland.", "options": ["kommst / komme", "kommt / komme", "kommen / kommt", "kommst / bin"], "correctIndex": 0, "explanation": "du 对应的词尾是 -st (kommst)；ich 对应的词尾是 -e (komme)。"},
             {"id": "A1_L01_Q2", "type": "EXAM_REAL", "question": "歌德A1初次见面问候：'Guten Tag! Freut mich.' 的意思是：", "options": ["你好！很高兴认识您。", "再见！明天见。", "早上好！我先走了。", "晚安！做个好梦。"], "correctIndex": 0, "explanation": "Guten Tag! Freut mich. 是德国人初次相识最标准的礼貌用语。"}
         ],
         "l01_words"
        ),
        ("A1_L02", "第2课：家庭亲属与称谓 (Familie & Verwandtschaft)",
         "掌握三性名词冠词系统(der/die/das)、复数规律、物主代词与否定词 kein/nicht",
         "名词冠词系统与物主代词 (Possessivartikel)",
         [
             {"heading": "1. 德语核心三性冠词（第一格 Nominativ）", "content": "阳性 der, 阴性 die, 中性 das, 复数 die。\n记忆方法：der Vater, die Mutter, das Kind, die Eltern。"},
             {"heading": "2. 否定词 kein vs nicht", "content": "kein 用于否定带有不定冠词或无冠词的名词 (Ich habe kein Auto)；nicht 否定动词、形容词或带定冠词的名词 (Das Auto ist nicht neu)。"}
         ],
         [
             {"id": "A1_L02_Q1", "type": "ARTICLE", "question": "请选出名词 'Kind'（孩子）的第一格定冠词：", "options": ["der", "die", "das", "den"], "correctIndex": 2, "explanation": "Kind 是中性名词，定冠词是 das。"},
             {"id": "A1_L02_Q2", "type": "GRAMMAR_FILL", "question": "Ich habe ______ Zeit (时间无冠词).", "options": ["keine", "nicht", "kein", "nein"], "correctIndex": 0, "explanation": "Zeit 是阴性名词，否定无冠词名词用 keine。"}
         ],
         "l02_words"
        ),
        ("A1_L03", "第3课：食材、餐饮与超市采购 (Essen & Supermarkt)",
         "掌握第四格宾格(Akkusativ)、情态动词 möchten、食材分类与采购计价",
         "第四格 (Akkusativ) 冠词变化法则",
         [
             {"heading": "1. 第四格冠词变化铁律", "content": "第四格中【仅阳性改变】：der -> den, ein -> einen, kein -> keinen。\n阴性(die/eine)、中性(das/ein)、复数(die/keine)完全保持不变！"},
             {"heading": "2. 情态动词 möchten 表达想要", "content": "ich möchte, du möchtest, er möchte, wir möchten, ihr möchtet, sie möchten。\n例：Ich möchte einen Apfel kaufen."}
         ],
         [
             {"id": "A1_L03_Q1", "type": "GRAMMAR_FILL", "question": "Ich kaufe ______ (der Apfel, 第四格宾语).", "options": ["den Apfel", "der Apfel", "dem Apfel", "des Apfels"], "correctIndex": 0, "explanation": "阳性名词在第四格中定冠词由 der 变为 den。"}
         ],
         "l03_words"
        ),
        ("A1_L04", "第4课：餐厅点餐与就餐文化 (Im Restaurant & Mahlzeiten)",
         "掌握餐厅点餐句型、餐具词汇、买单表达与日常就餐用语",
         "点餐交际用语与尊称命令式",
         [
             {"heading": "1. 餐厅点餐黄金句型", "content": "• Ich nehme... (我要一份...)\n• Ich möchte bitte... (我想要...)\n• Bringen Sie mir bitte... (请给我拿...)\n• Wir möchten bitte zahlen/bezahlen. (我们想要结账买单。)"}
         ],
         [
             {"id": "A1_L04_Q1", "type": "EXAM_REAL", "question": "在德国餐厅用餐完毕想要买单，最得体的表达是：", "options": ["Zahlen, bitte!", "Ich habe kein Geld!", "Gehen wir!", "Wo ist das Essen?"], "correctIndex": 0, "explanation": "Zahlen, bitte!（请结账）是餐厅最常用地道的买单口语。"}
         ],
         "l04_words"
        ),
        ("A1_L05", "第5课：居住房型、租房与家具 (Wohnen, Wohnung & Möbel)",
         "掌握第三格与格(Dativ)基础、房型格局、家具词汇与看房咨询",
         "第三格 (Dativ) 与居住方位介词",
         [
             {"heading": "1. 第三格冠词变化表", "content": "阳性 der -> dem, 阴性 die -> der, 中性 das -> dem, 复数 die -> den (+n)。\n口诀：阳中同 dem，阴变 der，复数带 den 词尾补 n！"},
             {"heading": "2. 固定接第三格的介词", "content": "mit, nach, von, zu, aus, bei, seit。\n例：Ich wohne bei meinen Eltern. / Er fährt mit dem Bus."}
         ],
         [
             {"id": "A1_L05_Q1", "type": "GRAMMAR_FILL", "question": "Ich fahre mit ______ (der Zug, 介词 mit 接第三格) nach Berlin.", "options": ["dem Zug", "den Zug", "der Zug", "des Zuges"], "correctIndex": 0, "explanation": "mit 支配第三格，阳性名词 der Zug 变为 dem Zug。"}
         ],
         "l05_words"
        ),
        ("A1_L06", "第6课：时间钟点、作息与日程 (Zeit, Alltag & Termine)",
         "掌握官方与日常时钟表达法、时间介词(um, am, im)、可分动词 (trennbare Verben)",
         "可分动词与时间介词用法",
         [
             {"heading": "1. 可分动词前缀移至句末原则", "content": "aufstehen: Ich stehe um 7 Uhr auf.\neinkaufen: Er kauft am Nachmittag ein.\nfernsehen: Wir sehen abends fern."},
             {"heading": "2. 三大时间介词归纳", "content": "• um + 具体钟点 (um 8 Uhr)\n• am + 星期/日期/特定时段 (am Montag, am Morgen, am 1. Mai)\n• im + 月份/季节/年份 (im Juli, im Sommer, im Jahr 2026)"}
         ],
         [
             {"id": "A1_L06_Q1", "type": "GRAMMAR_FILL", "question": "Der Film beginnt ______ 20 Uhr und läuft ______ Freitag.", "options": ["um / am", "am / um", "im / am", "um / im"], "correctIndex": 0, "explanation": "钟点时刻用介词 um，星期几用介词 am。"}
         ],
         "l06_words"
        ),
        ("A1_L07", "第7课：职业身份与办公文具 (Berufe & Arbeitsplatz)",
         "掌握男女职业双形变化规则(-in)、办公文具、日常工作活动与能力表达",
         "职业词汇女性后缀 -in 与情态动词 können",
         [
             {"heading": "1. 女性职业后缀 -in / -innen", "content": "阳性 der Lehrer -> 阴性 die Lehrerin (复数 die Lehrerinnen)。\nder Arzt -> die Ärztin (变音 Ä)。\nder Student -> die Studentin。"},
             {"heading": "2. 情态动词 können (能够，会)", "content": "ich kann, du kannst, er kann, wir können, ihr könnt, sie können。\n例：Er kann gut Deutsch sprechen."}
         ],
         [
             {"id": "A1_L07_Q1", "type": "ARTICLE", "question": "女性职业名词 'Lehrerin'（女教师）的冠词是：", "options": ["der", "die", "das", "den"], "correctIndex": 1, "explanation": "所有以 -in 结尾的女性职业名词均为阴性，定冠词是 die。"}
         ],
         "l07_words"
        ),
        ("A1_L08", "第8课：身体部位与基础医疗就医 (Körperteile & Gesundheit)",
         "掌握身体器官词汇、常见病痛表达、就诊对话与情态动词 müssen/sollen",
         "表达疼痛 tut weh 与情态动词 sollen",
         [
             {"heading": "1. 表达身体不适与疼痛", "content": "• Mein Kopf tut weh. (单数器官 tut weh)\n• Meine Augen tun weh. (复数器官 tun weh)\n• Ich habe Kopfschmerzen / Bauchschmerzen."},
             {"heading": "2. 情态动词 sollen (遵医嘱/应该)", "content": "Der Arzt sagt: Sie sollen viel Wasser trinken und im Bett bleiben."}
         ],
         [
             {"id": "A1_L08_Q1", "type": "EXAM_REAL", "question": "医生问诊常用语：“Was fehlt Ihnen?” 的意思是：", "options": ["您叫什么名字？", "您挂号了吗？", "您哪里不舒服？", "您几岁了？"], "correctIndex": 2, "explanation": "Was fehlt Ihnen? 是德语医生询问患者症状的标准表达。"}
         ],
         "l08_words"
        ),
        ("A1_L09", "第9课：城市设施与交通出行 (Stadt & Verkehrsmittel)",
         "掌握公共交通工具、车站买票、问路指路与祈使句(Imperativ)",
         "交通工具介词 mit 与祈使句 (Imperativ)",
         [
             {"heading": "1. 交通工具表达：mit + 第三格 Dativ", "content": "• mit dem Bus (阳性)\n• mit dem Zug / mit der U-Bahn (阴性)\n• mit dem Fahrrad / Auto (中性)"},
             {"heading": "2. 尊称祈使句 (Sie-Form)", "content": "动词原形放在句首 + Sie！\nGehen Sie geradeaus! / Biegen Sie rechts ab!"}
         ],
         [
             {"id": "A1_L09_Q1", "type": "GRAMMAR_FILL", "question": "问路礼貌指路：“请您向左转！”德语是：", "options": ["Biegen Sie links ab!", "Sie biegen links ab.", "Biegst du links!", "Abbiegen links Sie!"], "correctIndex": 0, "explanation": "尊称祈使句结构：动词原形位于句首 + Sie + 其他成分。"}
         ],
         "l09_words"
        ),
        ("A1_L10", "第10课：服饰穿搭、色彩与商场购物 (Kleidung, Farben & Einkaufen)",
         "掌握服装鞋帽词汇、基础颜色、试穿尺寸与尺码评价",
         "动词 gefallen (喜欢) 与 passen (合适)",
         [
             {"heading": "1. gefallen 与 passen 支配第三格", "content": "• Das Kleid gefällt mir gut. (合我心意)\n• Die Hose passt mir genau. (尺码尺寸合适)\n• Das Hemd steht dir gut. (这件衬衫很衬你)"}
         ],
         [
             {"id": "A1_L10_Q1", "type": "GRAMMAR_FILL", "question": "Wie gefällt ______ (ich, 第三人称代词格位) diese Jacke?", "options": ["mir", "mich", "ich", "mein"], "correctIndex": 0, "explanation": "gefallen 后面接人称代词第三格（Dativ），ich 变为 mir。"}
         ],
         "l10_words"
        ),
        ("A1_L11", "第11课：休闲运动与爱好娱乐 (Freizeit, Hobbys & Sport)",
         "掌握球类、乐器、户外运动、休闲活动与情态动词 wollen/dürfen",
         "爱好表达与情态动词 wollen",
         [
             {"heading": "1. 表达兴趣爱好常用句型", "content": "• Mein Hobby ist Lesen / Reisen.\n• Ich spiele gerne Fußball / Klavier.\n• In meiner Freizeit gehe ich oft schwimmen."},
             {"heading": "2. wollen (打算，想要)", "content": "ich will, du willst, er will, wir wollen, ihr wollt, sie wollen。\n例：Am Wochenende wollen wir wandern gehen."}
         ],
         [
             {"id": "A1_L11_Q1", "type": "GRAMMAR_FILL", "question": "Ich will am Samstag mit Freunden ins Kino ______.",
             "options": ["gehen", "gehe", "ging", "gegangen"], "correctIndex": 0, "explanation": "情态动词 will 占第二位，句末实义动词必须用原形 gehen。"}
         ],
         "l11_words"
        ),
        ("A1_L12", "第12课：天气气候与自然四季 (Wetter, Klima & Natur)",
         "掌握晴雨雪风天气描述、温度表达、自然风光词汇与非人称代词 es",
         "无人称代词 es 天气句型",
         [
             {"heading": "1. 常见天气句型", "content": "• Es regnet. (在下雨)\n• Es schneit. (在下雪)\n• Die Sonne scheint. (太阳在照耀)\n• Es ist warm / kalt / windig / sonnig / bewölkt.\n• Wie viel Grad haben wir heute? - Heute sind es 25 Grad."}
         ],
         [
             {"id": "A1_L12_Q1", "type": "VOCAB_MEANING", "question": "德语中描述“今天在下雪”的标准句子是：", "options": ["Es schneit heute.", "Es regnet heute.", "Es scheint heute.", "Es weht heute."], "correctIndex": 0, "explanation": "schneien 意为“下雪”，无人称主语用 es：Es schneit heute。"}
         ],
         "l12_words"
        ),
        ("A1_L13", "第13课：节日庆祝与社交拜访 (Feste, Feiern & Einladungen)",
         "掌握生日、新年、圣诞等节庆词汇、邀请函与道贺祝福礼仪",
         "节日问候语与完成时入门",
         [
             {"heading": "1. 德国常见节日祝福语", "content": "• Herzlichen Glückwunsch zum Geburtstag! (生日快乐！)\n• Frohe Weihnachten! (圣诞快乐！)\n• Ein frohes neues Jahr! (新年快乐！)\n• Gute Besserung! (祝早日康复！)\n• Viel Erfolg! (祝取得圆满成功！)"}
         ],
         [
             {"id": "A1_L13_Q1", "type": "EXAM_REAL", "question": "德国朋友过生日，送上祝福最地道的表达是：", "options": ["Herzlichen Glückwunsch zum Geburtstag!", "Frohe Ostern!", "Gute Reise!", "Guten Appetit!"], "correctIndex": 0, "explanation": "Herzlichen Glückwunsch zum Geburtstag! 是德语标准生日祝福语。"}
         ],
         "l13_words"
        ),
        ("A1_L14", "第14课：数字基数序数与度量衡 (Zahlen, Maße & Geld)",
         "掌握0-1000数字规律、序数词日期、货币单位(Euro/Cent)与度量衡",
         "德语数字倒序读法与日期表达",
         [
             {"heading": "1. 21-99 数字“个位在先，十位在后”铁律", "content": "21 = einundzwanzig (1 + 和 + 20)\n35 = fünfunddreißig (5 + 和 + 30)\n68 = achtundsechzig (8 + 和 + 60)"},
             {"heading": "2. 日期序数词 am + -(s)ten", "content": "Heute ist der erste Mai. / Wir treffen uns am dritten Juni."}
         ],
         [
             {"id": "A1_L14_Q1", "type": "VOCAB_MEANING", "question": "德语数字 'vierundfünfzig' 对应的阿拉伯数字是：", "options": ["54", "45", "504", "405"], "correctIndex": 0, "explanation": "vier(4) + und(和) + fünfzig(50) = 54。"}
         ],
         "l14_words"
        ),
        ("A1_L15", "第15课：歌德 A1 核心冲刺大通关 (Goethe A1 Prüfungstraining)",
         "全面复习歌德A1听说读写四大题型高频核心词汇与全真模拟",
         "歌德A1考点全景梳理与应试策略",
         [
             {"heading": "1. 歌德 A1 笔试要领", "content": "• 听力：抓数字、时间、地点与价格关键核心词。\n• 阅读：广告信息对比、便条便函关键信息点提取。\n• 写作：规范填写报名登记表，能书写30词左右的简短请假信或聚会邀请回复。"}
         ],
         [
             {"id": "A1_L15_Q1", "type": "EXAM_REAL", "question": "歌德A1写信给老师请假，开头最适宜的礼貌称呼是：", "options": ["Sehr geehrte Frau Müller,", "Hallo Kumpel,", "Liebe Mama,", "Tschüss Lehrer,"], "correctIndex": 0, "explanation": "给老师、上司或正式机构写信必须使用尊敬称谓：Sehr geehrte Frau Müller / Sehr geehrter Herr..."}
         ],
         "l15_words"
        )
    ]

    return lessons_spec

if __name__ == "__main__":
    generate_a1_file()
