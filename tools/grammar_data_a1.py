#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enriched Grammar Content for Level A1 (Lessons 1-15):
Präsens conjugation, Articles (Nom./Akk./Dat.), Possessive, Modal Verbs,
Separable Verbs, Imperative, Perfekt, Numbers, and Goethe A1 Strategy.
"""

A1_GRAMMAR = {
    "A1_L01": {
        "title": "动词现在时变位规则 (Präsens) 与两大核心疑问句",
        "sections": [
            {
                "heading": "一、规则动词现在时词尾变化六大人称公式",
                "content": "德语动词由【词干 (Verbstamm)】和【词尾 (Endung)】组成。在现在时中，动词必须根据主语人称变换词尾：\n\n"
                           "┌──────────────┬──────────┬──────────────┬──────────────┐\n"
                           "│ 人称代词     │ 规则词尾 │ lernen (学习)│ kommen (来)  │\n"
                           "├──────────────┼──────────┼──────────────┼──────────────┤\n"
                           "│ ich (我)     │ -e       │ ich lerne    │ ich komme    │\n"
                           "│ du (你)      │ -st      │ du lernst    │ du kommst    │\n"
                           "│ er/sie/es(他)│ -t       │ er lernt     │ sie kommt    │\n"
                           "│ wir (我们)   │ -en      │ wir lernen   │ wir kommen   │\n"
                           "│ ihr (你们)   │ -t       │ ihr lernt    │ ihr kommt    │\n"
                           "│ sie/Sie(他们)│ -en      │ sie lernen   │ Sie kommen   │\n"
                           "└──────────────┴──────────┴──────────────┴──────────────┘\n\n"
                           "【特殊音变发音补偿】：\n"
                           "• 词干以 -t, -d 结尾的动词（如 arbeiten, finden），在 du, er/sie/es, ihr 变位时须加 -e- 缓冲：\n"
                           "  du arbeitest, er arbeitet, ihr arbeitet (便于发音，避免破裂音连缀)。\n"
                           "• 词干以 -s, -ß, -z 结尾的动词（如 heißen, reisen），du 变位词尾只加 -t：\n"
                           "  du heißt, du reist (与 er heißt 同形)。"
            },
            {
                "heading": "二、德语句法第一铁律：变位动词永远占第 2 位 (V2-Regel)",
                "content": "德语是典型的动词第二位语言 (Verb-Zweit-Sprache)！在陈述句和特殊疑问句中，无论第一位放什么，变位动词永远雷打不动占在第 2 位：\n\n"
                           "1. 【正语序】：主语在第 1 位，动词在第 2 位\n"
                           "   [Pos 1: 主语]       [Pos 2: 动词]   [其他成分]\n"
                           "   Ich                 lerne           heute Deutsch in Berlin.\n\n"
                           "2. 【反语序（主谓倒装）】：时间或地点状语占第 1 位，动词坚守第 2 位，主语退至第 3 位！\n"
                           "   [Pos 1: 时间状语]   [Pos 2: 动词]   [Pos 3: 主语]   [其他成分]\n"
                           "   Heute               lerne           ich             Deutsch in Berlin.\n"
                           "   In Berlin           lerne           ich             heute Deutsch.\n\n"
                           "【千万警惕】：绝不能写成 *Heute ich lerne...！动词第二位是德语语法的神圣防线！"
            },
            {
                "heading": "三、两大核心疑问句：W-Frage vs. Ja/Nein-Frage",
                "content": "德语提问分为两大阵营，语序结构截然分明：\n\n"
                           "1. 【特殊疑问句 (W-Frage)】：\n"
                           "   以 W 开头的疑问词占第 1 位，变位动词占第 2 位：\n"
                           "   • Woher [Pos 1] kommen [Pos 2] Sie [Pos 3]? (您来自哪里？)\n"
                           "   • Wie [Pos 1] heißen [Pos 2] du [Pos 3]? (你叫什么名字？)\n"
                           "   • Was [Pos 1] machen [Pos 2] Sie [Pos 3] beruflich? (您从事什么职业？)\n\n"
                           "2. 【是非疑问句 (Ja/Nein-Frage / Entscheidungsfrage)】：\n"
                           "   【动词直接提到第 1 位】！主语退至第 2 位：\n"
                           "   • Kommen [Pos 1] Sie [Pos 2] aus China? (您来自中国吗？)\n"
                           "     -> 回答：Ja, ich komme aus China. / Nein, ich komme aus Japan.\n\n"
                           "3. 【高频考点 Doch 的妙用】：\n"
                           "   针对【否定疑问句】的肯定回答，必须用 Doch，不能用 Ja！\n"
                           "   • Kommst du nicht aus China? (你难道不是来自中国吗？)\n"
                           "     -> Doch! (不，我就是来自中国！)"
            },
            {
                "heading": "四、高频实战场景与真题例句解析",
                "content": "• 场景 1：自我介绍与籍贯\n"
                           "  - Mein Name ist Thomas Müller, und ich komme aus Frankfurt.\n"
                           "    (分析：复合句，前后两句动词 ist 和 komme 均居第 2 位。)\n\n"
                           "• 场景 2：询问对方语种能力\n"
                           "  - Sprechen Sie Deutsch oder Englisch?\n"
                           "    (分析：动词 sprechen 居第 1 位，是一般疑问句；注意 sprechen 是强变化动词：ich spreche, du sprichst, er spricht。)\n\n"
                           "• 场景 3：确认信息与 Doch 回应\n"
                           "  - Wohnen Sie nicht in München? - Doch, ich wohne in Schwabing.\n"
                           "    (分析：歌德 A1 听力与阅读考点，对带否定词 nicht 的反问，用 doch 予以否定性反弹肯定！)"
            },
            {
                "heading": "五、歌德 A1 考试得分秘籍与变位速记歌",
                "content": "【变位词尾速记歌】：\n"
                           "我 (ich) 带 -e，你 (du) 带 -st；\n"
                           "他她它 (er/sie/es) 紧跟着加个 -t；\n"
                           "我们大家 (wir) 原样 -en；\n"
                           "你们 (ihr) 也是加个 -t；\n"
                           "尊称复数 (Sie/sie) -en 回归！\n\n"
                           "【考官评分标准点拨】：\n"
                           "口语 Teil 1 自我介绍及抽卡提问环节，主谓变位一致性 (Subjekt-Verb-Kongruenz) 占语法分 50% 以上。切勿将 du sprichst 错说成 *du sprecht，将 er kommt 错说成 *er kommen！"
            }
        ]
    },
    "A1_L02": {
        "title": "名词冠词系统 (Nominativ)、复数与物主代词",
        "sections": [
            {
                "heading": "一、德语核心三性冠词系统 (第一格 Nominativ)",
                "content": "德语名词分为三种语法性别：阳性 (maskulin)、阴性 (feminin)、中性 (neutral)。冠词在第一格（主格）的形态如下：\n\n"
                           "┌────────────┬──────────┬──────────┬──────────┬──────────┐\n"
                           "│ 冠词类别   │ 阳性 (m.)│ 阴性 (f.)│ 中性 (n.)│ 复数 (Pl)│\n"
                           "├────────────┼──────────┼──────────┼──────────┼──────────┤\n"
                           "│ 定冠词     │ der      │ die      │ das      │ die      │\n"
                           "│ 不定冠词   │ ein      │ eine     │ ein      │ —— (无)  │\n"
                           "│ 否定冠词   │ kein     │ keine    │ kein     │ keine    │\n"
                           "│ 物主代词   │ mein     │ meine    │ mein     │ meine    │\n"
                           "└────────────┴──────────┴──────────┴──────────┴──────────┘\n\n"
                           "【核心后缀记忆法】：\n"
                           "• 必为阳性 (der)：-ling, -or, -ist, -ismus (der Lehrling, der Motor)\n"
                           "• 必为阴性 (die)：-ung, -heit, -keit, -schaft, -tion, -tät, -ei (die Zeitung, die Freiheit, die Bäckerei)\n"
                           "• 必为中性 (das)：-chen, -lein, -ment, -um (das Mädchen, das Fräulein, das Zentrum)"
            },
            {
                "heading": "二、名词复数五大变化形式全览",
                "content": "德语名词复数并非简单加 -s，主要有 5 种形态，背单词时必须带冠词和复数一起记忆：\n\n"
                           "1. 【加 -e (常伴随变音)】：大部分阳性名词与部分中性名词\n"
                           "   • der Tisch -> die Tische, der Tag -> die Tage, der Sohn -> die Söhne\n\n"
                           "2. 【加 -(e)n】：95% 以上的阴性名词及弱变化阳性名词\n"
                           "   • die Frau -> die Frauen, die Zeitung -> die Zeitungen, die Lampe -> die Lampen\n\n"
                           "3. 【加 -er (通常变音)】：大部分单音节中性名词\n"
                           "   • das Kind -> die Kinder, das Buch -> die Bücher, das Bild -> die Bilder\n\n"
                           "4. 【无词尾 (或仅变音)】：以 -el, -en, -er 结尾的阳性和中性名词\n"
                           "   • der Lehrer -> die Lehrer, der Vater -> die Väter, das Fenster -> die Fenster\n\n"
                           "5. 【加 -s】：外来词、缩写词及以非 e 元音结尾的词\n"
                           "   • das Auto -> die Autos, das Sofa -> die Sofas, das Foto -> die Fotos"
            },
            {
                "heading": "三、物主代词系统 (Possessivartikel)",
                "content": "物主代词表示人与事物的所属关系，其词干随主语人称变换，其词尾完全模仿不定冠词 ein：\n\n"
                           "┌────────────┬──────────┬──────────────┬──────────────┐\n"
                           "│ 人称       │ 物主词干 │ 阳性 (der)   │ 阴性 (die)   │\n"
                           "├────────────┼──────────┼──────────────┼──────────────┤\n"
                           "│ ich (我)   │ mein-    │ mein Vater   │ meine Mutter │\n"
                           "│ du (你)    │ dein-    │ dein Bruder  │ deine Schwester│\n"
                           "│ er/es(他/它)│ sein-   │ sein Sohn    │ seine Tochter│\n"
                           "│ sie (她)   │ ihr-     │ ihr Mann     │ ihre Frau    │\n"
                           "│ wir (我们) │ unser-   │ unser Kollege│ unsere Freundin│\n"
                           "│ ihr (你们) │ euer-    │ euer Lehrer  │ eure Lehrerin│\n"
                           "│ Sie (您/您们)│ Ihr-   │ Ihr Chef     │ Ihre Kollegin│\n"
                           "└────────────┴──────────┴──────────────┴──────────────┘\n\n"
                           "【警惕 euer 的脱落现象】：\n"
                           "当 euer 加词尾时，中间的 -e- 必须脱落：euer Vater (阳), 但是 eure Mutter (阴, 非 *euere)！"
            },
            {
                "heading": "四、否定词 kein vs nicht 严格使用边界",
                "content": "这是中国学生 A1 阶段最容易扣分的语法点之一：\n\n"
                           "1. 【使用 kein 的唯一场景】：\n"
                           "   否定带有【不定冠词 (ein/eine)】或【零冠词 (无冠词的名词)】！\n"
                           "   • Ist das ein Hund? -> Nein, das ist kein Hund.\n"
                           "   • Haben Sie Geld? -> Nein, ich habe kein Geld. (Geld 是零冠词名词)\n\n"
                           "2. 【使用 nicht 的万能场景】：\n"
                           "   否定动词、形容词、副词、专有名词、带定冠词的名词、带物主代词的名词！\n"
                           "   • 否定动词：Ich rauche nicht.\n"
                           "   • 否定形容词：Das Auto ist nicht teuer.\n"
                           "   • 否定带定冠词名词：Das ist nicht der Schlüssel von Peter.\n"
                           "   • 否定物主代词：Das ist nicht meine Tasche."
            },
            {
                "heading": "五、歌德 A1 避坑口诀与应试要诀",
                "content": "【冠词与复数记忆诀】：\n"
                           "德语三性莫混淆，后缀规律是法宝；\n"
                           "-ung, -heit 都是女，-chen, -lein 中性跑；\n"
                           "复数变化分五路，记词带冠别拉倒；\n"
                           "不定零冠用 kein 否，其余全都交给 nicht！"
            }
        ]
    },
    "A1_L03": {
        "title": "第四格 (Akkusativ) 宾语与及物动词系统",
        "sections": [
            {
                "heading": "一、第四格 (Akkusativ) 的语法逻辑与本质",
                "content": "第四格（宾格）在德语中主要充当及物动词的【直接宾语 (Direktes Objekt)】，即动作的直接承受者。\n\n"
                           "【核心变化铁律】：在第四格中，【只有阳性发生变化】，阴性、中性和复数与第一格完全相同！\n"
                           "┌────────────┬──────────┬──────────┬──────────┬──────────┐\n"
                           "│ 格位       │ 阳性 (m.)│ 阴性 (f.)│ 中性 (n.)│ 复数 (Pl)│\n"
                           "├────────────┼──────────┼──────────┼──────────┼──────────┤\n"
                           "│ Nom. (一格)│ der      │ die      │ das      │ die      │\n"
                           "│ Akk. (四格)│ den      │ die      │ das      │ die      │\n"
                           "├────────────┼──────────┼──────────┼──────────┼──────────┤\n"
                           "│ 不定冠词一格│ ein     │ eine     │ ein      │ ——       │\n"
                           "│ 不定冠词四格│ einen   │ eine     │ ein      │ ——       │\n"
                           "├────────────┼──────────┼──────────┼──────────┼──────────┤\n"
                           "│ 否定冠词四格│ keinen  │ keine    │ kein     │ keine    │\n"
                           "│ 物主代词四格│ meinen  │ meine    │ mein     │ meine    │\n"
                           "└────────────┴──────────┴──────────────┴──────────┴──────────┘\n\n"
                           "【速记秘籍】：阳性一格是 der，变成四格尾巴拉长变成 den (-en)！"
            },
            {
                "heading": "二、支配第四格的高频及物动词群",
                "content": "日常生活中绝大多数动词都是及物动词 (Transitive Verben)，必须搭配第四格：\n\n"
                           "• haben (有): Ich habe einen Bruder und eine Schwester.\n"
                           "• brauchen (需要): Wir brauchen einen neuen Computer.\n"
                           "• kaufen (买): Er kauft einen teuren Anzug.\n"
                           "• essen (吃): Ich esse einen Apfel.\n"
                           "• trinken (喝): Möchtest du einen Kaffee trinken?\n"
                           "• suchen (寻找): Ich suche meinen Autoschlüssel.\n"
                           "• finden (找到/觉得): Wie finden Sie den neuen Film?\n"
                           "• lesen (读): Sie liest eine interessante Zeitung.\n"
                           "• sehen (看见): Siehst du den Mann dort?"
            },
            {
                "heading": "三、核心句型 Es gibt + Akkusativ 与 haben 的对比",
                "content": "德语表达‘存在、有’的两大核心支柱：\n\n"
                           "1. 【Es gibt + Akkusativ】（相当于英语 There is / There are）：\n"
                           "   表示客观环境或某个地点存在某物，主语恒为 es，后面的名词【必须用第四格】！\n"
                           "   • In der Stadt gibt es einen großen Park. (阳性 der Park -> einen Park)\n"
                           "   • Gibt es hier eine Apotheke? (阴性)\n"
                           "   • Hier gibt es kein Problem. (中性)\n\n"
                           "2. 【haben + Akkusativ】：\n"
                           "   表示特定人称主体‘拥有’某物，主语为人或机构：\n"
                           "   • Ich habe einen Termin um 14 Uhr. (我有预约。)\n"
                           "   • Das Zimmer hat einen Balkon. (房间带阳台。)"
            },
            {
                "heading": "四、人称代词的第四格形态对照表",
                "content": "当动作的宾语是人时，人称代词也必须变为第四格：\n\n"
                           "┌────────────┬─────────────┬───────────────────────────┐\n"
                           "│ 第一格主格 │ 第四格宾格  │ 经典例句                  │\n"
                           "├────────────┼─────────────┼───────────────────────────┤\n"
                           "│ ich (我)   │ mich (我)   │ Liebst du mich? (你爱我吗?)│\n"
                           "│ du (你)    │ dich (你)   │ Ich rufe dich an. (我给你打电话)│\n"
                           "│ er (他)    │ ihn (他)    │ Kennst du ihn? (你认识他吗?)│\n"
                           "│ sie (她)   │ sie (她)    │ Ich verstehe sie nicht.   │\n"
                           "│ es (它)    │ es (它)     │ Ich nehme es. (我买下它了) │\n"
                           "│ wir (我们) │ uns (我们)  │ Hört ihr uns?             │\n"
                           "│ ihr (你们) │ euch (你们) │ Ich besuche euch morgen.  │\n"
                           "│ sie (他们) │ sie (他们)  │ Wir laden sie ein.        │\n"
                           "│ Sie (您)   │ Sie (您)    │ Ich danke... (注意：danken加三格)│\n"
                           "└────────────┴─────────────┴───────────────────────────┘"
            },
            {
                "heading": "五、歌德 A1 易错题警示与速查口诀",
                "content": "【中国考生第一高频失分点】：\n"
                           "在超市购物或就餐点菜中，误说 *Ich möchte ein Kaffee (Kaffee 是阳性 der Kaffee，必须说 einen Kaffee)！\n\n"
                           "【四格速记口诀】：\n"
                           "及物动词带宾语，直接承受四格举；\n"
                           "阴性中性保原样，单看阳性变一个；\n"
                           "der 变 den，ein 变 einen；\n"
                           "见了 haben, brauchen, essen，阳性后头加个 -en！"
            }
        ]
    },
    "A1_L04": {
        "title": "点餐交际用语、情态表达 möchten 与尊称命令式",
        "sections": [
            {
                "heading": "一、情态表达 möchten 的六大人称变位与客气请求",
                "content": "möchten 实际上是 mögen 的第二虚拟式，但在 A1 阶段作为独立情态表达使用，意为‘想要、希望’，远比直接用 wollen 更客气有礼：\n\n"
                           "┌──────────────┬──────────────────┬───────────────────────────┐\n"
                           "│ 人称         │ 变位形式         │ 经典例句                  │\n"
                           "├──────────────┼──────────────────┼───────────────────────────┤\n"
                           "│ ich          │ möchte           │ Ich möchte einen Kaffee.  │\n"
                           "│ du           │ möchtest         │ Was möchtest du essen?    │\n"
                           "│ er/sie/es    │ möchte           │ Er möchte bezahlen.       │\n"
                           "│ wir          │ möchten          │ Wir möchten bestellen.    │\n"
                           "│ ihr          │ möchtet          │ Was möchtet ihr trinken?  │\n"
                           "│ sie/Sie      │ möchten          │ Möchten Sie noch etwas?   │\n"
                           "└──────────────┴──────────────────┴───────────────────────────┘\n\n"
                           "【特点牢记】：第 1 人称 (ich) 与第 3 人称单数 (er/sie/es) 变位完全同形，绝不加 -t！"
            },
            {
                "heading": "二、尊称命令式 (Imperativ für Sie) 规则",
                "content": "在餐厅、商店、职场中对陌生人或顾客提出礼貌要求或指示时，使用 Sie 的尊称命令式：\n\n"
                           "• 【构成法则】：【变位动词提到句首】 + 【代词 Sie】 + 【句末加感叹号！】\n"
                           "  - Nehmen Sie bitte Platz! (请坐！)\n"
                           "  - Probieren Sie diesen Wein! (请您品尝这款葡萄酒！)\n"
                           "  - Zahlen Sie bitte an der Kasse! (请您在收银台结账！)\n\n"
                           "• 【助动词 sein 的特殊形式】：\n"
                           "  sein 的尊称命令式不是 *Sind Sie，而是 Seien Sie！\n"
                           "  - Seien Sie bitte pünktlich! (请您务必准时！)"
            },
            {
                "heading": "三、餐厅就餐全流程高频句型矩阵",
                "content": "1. 【入座与看菜单】：\n"
                           "   • Haben Sie einen Tisch für zwei Personen? (有两人桌吗？)\n"
                           "   • Die Speisekarte, bitte! (请拿菜单！)\n\n"
                           "2. 【点餐与表达偏好】：\n"
                           "   • Ich möchte gern das Schnitzel mit Kartoffelsalat. (我想要一份炸肉排配土豆沙拉。)\n"
                           "   • Ich hätte gern ein Mineralwasser ohne Kohlensäure. (我想要一瓶不带气矿泉水。)\n"
                           "   • Für mich bitte eine Tomatensuppe. (给我来一份番茄汤。)\n\n"
                           "3. 【结账与买单 (Zahlen)】：\n"
                           "   • Wir möchten bitte bezahlen. / Zahlen, bitte! (我们要结账！)\n"
                           "   • Zusammen oder getrennt? (一起结还是分开结？)\n"
                           "   • Getrennt, bitte. (请分开结。)\n"
                           "   • Das stimmt so! (不用找零了！——德语区给小费标准句)"
            },
            {
                "heading": "四、语气词 (Partikeln) bitte, mal, doch 的润色功能",
                "content": "德语小品词没有实际词义，但能极大地柔化语气，使祈使和请求听起来亲切礼貌：\n\n"
                           "• bitte：最基本的客气礼貌词 (Ein Bier, bitte!)\n"
                           "• mal：表示‘一下’，消除生硬命令感 (Schauen Sie mal! 请看一下！)\n"
                           "• doch：表示鼓励或热情的敦促 (Probieren Sie doch mal! 您尝尝看嘛！)"
            },
            {
                "heading": "五、歌德 A1 口试实战秘籍与就餐交际法则",
                "content": "【口试 Teil 2 & 3 必胜句式】：\n"
                           "抽到食物或餐厅卡片时，迅速套用万能句型：\n"
                           "• 提问：Was möchten Sie trinken? / Möchten Sie einen Kaffee?\n"
                           "• 回答：Ich möchte gern ein Glas Wasser, danke!\n"
                           "千万不要直接说：*Ich will Wasser! (will 在德语中语气粗暴，像小孩子任性吵闹，扣礼貌分！)"
            }
        ]
    },
    "A1_L05": {
        "title": "第三格 (Dativ) 间接宾语与方位介词",
        "sections": [
            {
                "heading": "一、第三格 (Dativ) 的语法本质与完整变格表",
                "content": "第三格（与格）表示动作的受益者、间接受体，或者在方位介词后表示‘静态位置 (Wo?)’。\n\n"
                           "┌────────────┬──────────┬──────────┬──────────┬──────────────┐\n"
                           "│ 冠词类别   │ 阳性 (m.)│ 阴性 (f.)│ 中性 (n.)│ 复数 (Pl)    │\n"
                           "├────────────┼──────────┼──────────┼──────────┼──────────────┤\n"
                           "│ 定冠词     │ dem      │ der      │ dem      │ den ... -n   │\n"
                           "│ 不定冠词   │ einem    │ einer    │ einem    │ ——           │\n"
                           "│ 否定冠词   │ keinem   │ keiner   │ keinem   │ keinen ... -n│\n"
                           "│ 物主代词   │ meinem   │ meiner   │ meinem   │ meinen ... -n│\n"
                           "└────────────┴──────────┴──────────┴──────────┴──────────────┘\n\n"
                           "【两大极高频考点】：\n"
                           "1. 阳性与中性第三格完全同形：冠词一律变成 dem / einem！\n"
                           "2. 【复数名词必须加 -n 尾巴】：第三格复数不仅冠词是 den，名词末尾如果不是 -s 或 -n，也必须补加 -n！\n"
                           "   • den Kindern (das Kind -> die Kinder -> den Kindern)\n"
                           "   • den Freunden (der Freund -> die Freunde -> den Freunden)"
            },
            {
                "heading": "二、纯支配第三格的高频动词大家族",
                "content": "德语中有一批动词后面【只能接第三格】，绝不能接第四格，必须死记：\n\n"
                           "• helfen (帮助): Kann ich Ihnen helfen? (我能帮您吗？)\n"
                           "• danken (感谢): Ich danke dir von Herzen. (我由衷感谢你。)\n"
                           "• gefallen (喜欢): Das Bild gefällt mir sehr gut. (我非常喜欢这幅画。)\n"
                           "• gehören (属于): Das Buch gehört dem Lehrer. (这本书属于这位老师。)\n"
                           "• schmecken (合口味): Die Suppe schmeckt den Gästen ausgezeichnet. (客人们觉得汤味道极棒。)\n"
                           "• gratulieren (祝贺): Wir gratulieren dir zum Geburtstag! (我们祝你生日快乐！)\n"
                           "• passen (尺寸合适): Die Hose passt mir leider nicht. (这条裤子我穿不合适。)"
            },
            {
                "heading": "三、人称代词第三格形态全览",
                "content": "人称代词在第三格中的形式与第一格和第四格对照：\n\n"
                           "┌────────────┬────────────┬────────────┬────────────────────────┐\n"
                           "│ 一格 Nom.  │ 四格 Akk.  │ 三格 Dat.  │ 示范例句               │\n"
                           "├────────────┼────────────┼────────────┼────────────────────────┤\n"
                           "│ ich        │ mich       │ mir        │ Wie geht es dir? - Mir geht es gut. │\n"
                           "│ du         │ dich       │ dir        │ Ich helfe dir gern.    │\n"
                           "│ er         │ ihn        │ ihm        │ Das Auto gehört ihm.   │\n"
                           "│ sie        │ sie        │ ihr        │ Wir danken ihr.        │\n"
                           "│ es         │ es         │ ihm        │ Wie geht es dem Kind? - Es geht ihm gut. │\n"
                           "│ wir        │ uns        │ uns        │ Der Wein schmeckt uns. │\n"
                           "│ ihr        │ euch       │ euch       │ Ich gratuliere euch!   │\n"
                           "│ sie        │ sie        │ ihnen      │ Das gefällt ihnen nicht.│\n"
                           "│ Sie        │ Sie        │ Ihnen      │ Wie kann ich Ihnen helfen? │\n"
                           "└────────────┴────────────┴────────────┴────────────────────────┘"
            },
            {
                "heading": "四、方位介词与第三格的缩合形式",
                "content": "在生活口语与正式写作中，介词与后面的定冠词 dem/der 极其频繁缩合：\n\n"
                           "• in + dem = im: im Haus (在房子里), im Zimmer (在房间里)\n"
                           "• an + dem = am: am Bahnhof (在火车站), am Fenster (在窗户边)\n"
                           "• bei + dem = beim: beim Arzt (在医生那里), beim Essen (在吃饭时)\n"
                           "• von + dem = vom: vom Chef (从主管那里来)\n"
                           "• zu + dem = zum: zum Supermarkt (去超市)\n"
                           "• zu + der = zur: zur Bank (去银行), zur Schule (去学校)"
            },
            {
                "heading": "五、第三格速记口诀与真题避坑指南",
                "content": "【第三格变格歌谣】：\n"
                           "三格阳中是个 m (dem / einem)；\n"
                           "三格阴性变成了 r (der / einer)；\n"
                           "三格复数是个 n (den ... -n)，名词屁股别忘加个 -n！\n\n"
                           "【避坑指南】：\n"
                           "在问好句型中：*Wie geht es du? 是严重错误！必须用第三格：Wie geht es dir? 回答用 Mir geht's gut (不能说 *Ich bin gut)！"
            }
        ]
    },
    "A1_L06": {
        "title": "可分动词 (Trennbare Verben) 与时间介词用法",
        "sections": [
            {
                "heading": "一、可分动词结构原理与框形结构 (Satzklammer)",
                "content": "可分动词是由一个【前缀 (Präfix)】和一个【基础动词】结合而成的新动词。\n"
                           "【核心铁律】：在一般现在时陈述句与疑问句中，可分前缀与词干脱离，【直接被甩到句子最末尾】！\n\n"
                           "• 基础动词：stehen (站立) -> 可分动词：aufstehen (起床)\n"
                           "  - [Pos 1]  [Pos 2: 变位动词]  [时间/地点等成分]        [句末: 可分前缀]\n"
                           "    Ich      stehe             jeden Morgen um 6 Uhr    auf.\n"
                           "  - 一般疑问句：Stehst du am Sonntag auch so früh auf?\n\n"
                           "【框形结构】：第 2 位的变位动词与句末的前缀像两个括号，将句子的其它成分紧紧框在中间！"
            },
            {
                "heading": "二、高频可分前缀与经典动词表",
                "content": "┌────────┬──────────────┬──────────────┬────────────────────────┐\n"
                           "│ 前缀   │ 常见动词     │ 释义         │ 经典例句               │\n"
                           "├────────┼──────────────┼──────────────┼────────────────────────┤\n"
                           "│ auf-   │ aufstehen    │ 起床         │ Wann stehst du auf?    │\n"
                           "│ an-    │ anrufen      │ 打电话       │ Ich rufe meine Mutter an.│\n"
                           "│ an-    │ anfangen     │ 开始         │ Der Film fängt gleich an.│\n"
                           "│ ein-   │ einkaufen    │ 超市采购     │ Wir kaufen im Supermarkt ein.│\n"
                           "│ ein-   │ einladen     │ 邀请         │ Er lädt Freunde zur Party ein.│\n"
                           "│ aus-   │ aussteigen   │ 下车         │ Steigen Sie an der Station aus!│\n"
                           "│ mit-   │ mitkommen    │ 一同前来     │ Kommst du heute Abend mit?│\n"
                           "│ fern-  │ fernsehen    │ 看电视       │ Er sieht am Abend fern.│\n"
                           "│ zu-    │ zumachen     │ 关闭         │ Mach bitte das Fenster zu!│\n"
                           "└────────┴──────────────┴──────────────┴────────────────────────┘"
            },
            {
                "heading": "三、时间介词三巨头：um, am, im 的精确分工",
                "content": "表达具体时间节点时，德语有极其分明的三级介词体系：\n\n"
                           "1. 【um】搭配【具体时刻 (Uhrzeit)】：\n"
                           "   • um 8 Uhr (在8点), um halb zehn (在9点半), um Viertel vor fünf (在4点45分)\n\n"
                           "2. 【am】搭配【日子、星期与一天中的时段】：\n"
                           "   • 星期几：am Montag, am Dienstag, am Wochenende (在周末)\n"
                           "   • 日期：am 1. Mai (在5月1日)\n"
                           "   • 一天中的时段：am Morgen (在早晨), am Vormittag, am Nachmittag, am Abend (在傍晚)\n"
                           "   • 【唯一例外特记】：在夜里是 in der Nacht (不是 am Nacht)！\n\n"
                           "3. 【im】搭配【月份、季节、年份与较长时间段】：\n"
                           "   • 月份：im Januar, im Juli, im Oktober\n"
                           "   • 季节：im Frühling (春天), im Sommer, im Herbst, im Winter\n"
                           "   • 年份前【不用介词】：Ich bin 1995 geboren (或者 im Jahr 1995，绝不可用 *in 1995)！"
            },
            {
                "heading": "四、时间起止与持续介词家族",
                "content": "• von ... bis ...：从...到... (Der Unterricht dauert von 9 bis 12 Uhr.)\n"
                           "• ab + Dativ：从...起（将来时间起点）(Ab morgen rauche ich nicht mehr.)\n"
                           "• seit + Dativ：自从...以来（过去开始持续至今）(Ich lerne seit drei Monaten Deutsch.)\n"
                           "• bis + Akkusativ：直到...为止 (Ich bleibe bis nächsten Montag in Berlin.)"
            },
            {
                "heading": "五、可分动词与时间介词速记诀",
                "content": "【时间介词顺口溜】：\n"
                           "钟点用 um，日期星期 am，年月季节全都 im；\n"
                           "夜里睡觉 in der Nacht，年份裸奔别加 in！\n\n"
                           "【可分动词解题诀】：\n"
                           "前缀词干两分离，动词二位站第一；\n"
                           "可分前缀甩句末，牢牢框住不漏题！"
            }
        ]
    },
    "A1_L07": {
        "title": "职业后缀 -in、情态动词 können 与情态框架结构",
        "sections": [
            {
                "heading": "一、情态动词 können 的现在时变位特征",
                "content": "können 表示‘能力、客观可能或会做某事’，其变位具有典型的不规则特征：\n\n"
                           "┌──────────────┬──────────┬───────────────────────────┐\n"
                           "│ 人称         │ 变位形式 │ 经典例句                  │\n"
                           "├──────────────┼──────────┼───────────────────────────┤\n"
                           "│ ich          │ kann     │ Ich kann gut Deutsch sprechen.│\n"
                           "│ du           │ kannst   │ Kannst du Klavier spielen?│\n"
                           "│ er/sie/es    │ kann     │ Er kann nicht schwimmen.  │\n"
                           "│ wir          │ können   │ Wir können morgen kommen. │\n"
                           "│ ihr          │ könnt    │ Könnt ihr mir helfen?     │\n"
                           "│ sie/Sie      │ können   │ Können Sie das wiederholen?│\n"
                           "└──────────────┴──────────┴───────────────────────────┘\n\n"
                           "【三大关键法则】：\n"
                           "1. 单数人称词干元音发生音变：ö 变成 a (ich kann, du kannst, er kann)！\n"
                           "2. 第 1 人称 (ich) 与第 3 人称单数 (er/sie/es) 完全同形，且【绝无词尾 -t】！\n"
                           "3. 复数人称 (wir, ihr, sie/Sie) 词干元音恢复为 ö。"
            },
            {
                "heading": "二、情态动词框架结构：情态二位，实义句末！",
                "content": "当句子中出现情态动词时，必须构成严格的【双动词框形结构】：\n\n"
                           "• [Pos 1: 主语]  [Pos 2: 变位情态动词]  [中间状语/宾语]          [句末: 实义动词原形]\n"
                           "  Mein Bruder     kann                  sehr schnell und sicher    Auto fahren.\n"
                           "  Ich             kann                  diesen langen Text nicht   verstehen.\n\n"
                           "【句末实义动词铁律】：\n"
                           "句末的动词【必须是原形 (Infinitiv)】，不能带 zu，也不能做任何变位！所有的变位重担全由第 2 位的情态动词承担！"
            },
            {
                "heading": "三、职业词汇性别构成规律：男性词干与女性后缀 -in",
                "content": "德语对职业称谓有着极强的性别严谨性：\n\n"
                           "• 基础规则：男性职业名词多为原形，女性职业名词在词尾加上后缀 -in，复数加 -innen：\n"
                           "  - der Lehrer (男老师) -> die Lehrerin (女老师) -> die Lehrerinnen (女老师们)\n"
                           "  - der Arzt (男医生) -> die Ärztin (女医生，常带变音！) -> die Ärztinnen\n"
                           "  - der Student (男大学生) -> die Studentin (女大学生) -> die Studentinnen\n"
                           "  - der Kellner (男服务员) -> die Kellnerin (女服务员) -> die Kellnerinnen\n\n"
                           "• 【职业陈述的零冠词与 als】：\n"
                           "  表达职业身份时，名词前【不加冠词 (Nullartikel)】：\n"
                           "  - Ich bin Ingenieur. (我是工程师。)\n"
                           "  - Ich arbeite als Lehrerin bei Siemens. (我在西门子当老师。)"
            },
            {
                "heading": "四、高频实战场景与真题对话解析",
                "content": "• 场景 1：求职面试表达技能\n"
                           "  - Ich kann sehr gut Englisch und Deutsch in Wort und Schrift.\n"
                           "    (分析：语言技能动词 sprechen 可省略，kann 直接带语言名称。)\n\n"
                           "• 场景 2：请求他人协助\n"
                           "  - Können Sie mir bitte helfen? Mein Computer funktioniert nicht.\n"
                           "    (分析：Kannst du / Können Sie 在日常生活中用于提出请求，极其地道。)"
            },
            {
                "heading": "五、歌德 A1 情态动词得分秘籍",
                "content": "【情态动词构句口诀】：\n"
                           "情态动词占二位，承担变位不喊累；\n"
                           "单数元音要突变，一三无尾记心间；\n"
                           "实义动词甩句末，原形站定大功成！"
            }
        ]
    },
    "A1_L08": {
        "title": "身体疼痛表达 tut weh 与情态动词 müssen / sollen",
        "sections": [
            {
                "heading": "一、身体疼痛固定句型：...tut weh vs ...tun weh",
                "content": "德语表达身体不适或疼痛，使用核心动词 wehtun (可分动词: weh + tun)：\n\n"
                           "1. 【单数身体部位疼痛】：【身体部位】 + tut [mir/dir/ihm] weh\n"
                           "   • Mein Kopf tut weh. (我的头痛。)\n"
                           "   • Der Bauch tut mir weh. (我的肚子痛。)\n"
                           "   • Mein Hals tut weh. (我的嗓子痛。)\n\n"
                           "2. 【复数身体部位疼痛】：【复数部位】 + tun [mir/dir/ihm] weh\n"
                           "   • Meine Beine tun weh. (我的双腿痛。)\n"
                           "   • Seine Augen tun weh. (他的眼睛痛。)\n"
                           "   • Meine Ohren tun weh. (我的耳朵痛。)\n\n"
                           "【主谓一致注意点】：tut (单数) vs tun (复数)，取决于引起疼痛的器官单复数！"
            },
            {
                "heading": "二、情态动词 müssen 与 sollen 的本质语义对比",
                "content": "中国学习者极易混淆 müssen (必须) 与 sollen (应该)：\n\n"
                           "1. 【müssen (客观必然/必须)】：\n"
                           "   源自客观身体规律、法律或内在不可抗拒的必然要求：\n"
                           "   • Ich habe hohes Fieber, ich muss zum Arzt gehen. (我发高烧了，我必须去看医生。)\n"
                           "   • 变位：ich muss, du musst, er muss, wir müssen, ihr müsst, sie müssen\n\n"
                           "2. 【sollen (转述要求/医嘱/应当)】：\n"
                           "   传达第三方（如医生、上司、规章制度）的建议、指令或委托：\n"
                           "   • Der Arzt sagt, ich soll viel Wasser trinken und drei Tage im Bett bleiben.\n"
                           "     (医生说我应当多喝水，卧床三天。——转述医嘱必须用 sollen！)\n"
                           "   • 变位：ich soll, du sollst, er soll, wir sollen, ihr sollt, sie sollen (无元音变音！)"
            },
            {
                "heading": "三、否定对比：nicht müssen (不需要) vs nicht dürfen (禁止)",
                "content": "【严重陷阱】：德语中 nicht müssen 不等于英语的 mustn't！\n\n"
                           "• nicht müssen = need not (不需要、不必)：\n"
                           "  Du musst morgen nicht kommen, es ist Feiertag. (你明天不必来，明天是节假日。)\n\n"
                           "• nicht dürfen = mustn't (严禁、不允许)：\n"
                           "  Hier darf man nicht rauchen! (这里严禁吸烟！)\n"
                           "  Der Kranke darf keinen Alkohol trinken. (病人绝对不能喝酒。)"
            },
            {
                "heading": "四、就医看病高频实用会话与病假条",
                "content": "• 挂号问诊：\n"
                           "  - Was fehlt Ihnen denn? (您哪里不舒服？——医生标准开场白)\n"
                           "  - Ich habe seit zwei Tagen starke Kopfschmerzen und Husten. (我头痛咳嗽两天了。)\n\n"
                           "• 开药与处方：\n"
                           "  - Nehmen Sie diese Tabletten dreimal täglich nach dem Essen! (这药每天饭后吃三次！)\n\n"
                           "• 开具病假证明 (die Arbeitsunfähigkeitsbescheinigung / Krankschreibung)：\n"
                           "  - Ich schreibe Sie für drei Tage krank. (我给您开三天的病假条。)"
            },
            {
                "heading": "五、歌德 A1 听力与写作就医答题秘籍",
                "content": "【医嘱提分秘籍】：\n"
                           "听力中只要听到 'Der Arzt sagt...'，后面紧跟的正确选项必然对应情态动词 sollen！\n"
                           "写作中给公司写请假邮件：\n"
                           "Ich bin leider krank und kann heute nicht zur Arbeit kommen. Der Arzt hat mich bis Freitag krankgeschrieben. (满分请假金句！)"
            }
        ]
    },
    "A1_L09": {
        "title": "交通介词 mit + Dativ、方向介词与祈使句 (Imperativ)",
        "sections": [
            {
                "heading": "一、交通工具介词：mit + 第三格 (Dativ) 铁律",
                "content": "德语表达‘乘坐某种交通工具’，统一使用介词 mit + 第三格 (Dativ)：\n\n"
                           "• mit dem Bus (阳性: der Bus -> dem Bus)\n"
                           "• mit dem Zug / mit der Bahn (der Zug -> dem Zug; die Bahn -> der Bahn)\n"
                           "• mit der U-Bahn / mit der S-Bahn (die U-Bahn -> der U-Bahn)\n"
                           "• mit dem Fahrrad / mit dem Auto (das Fahrrad/Auto -> dem Fahrrad/Auto)\n"
                           "• mit dem Flugzeug (das Flugzeug -> dem Flugzeug)\n\n"
                           "【唯一零介词特殊表达】：\n"
                           "‘步行 / 走路’是固定短语 zu Fuß (不用 mit)！\n"
                           "例：Ich gehe jeden Tag zu Fuß zur Schule. (我每天步行去学校。)"
            },
            {
                "heading": "二、方向与目的地介词：nach, in, zu 的严格区分",
                "content": "针对疑问词 Wohin? (去哪里？)，根据目的地性质严格选用介词：\n\n"
                           "1. 【nach】：用于【无冠词的国家、城市与方向】：\n"
                           "   • nach Deutschland, nach Berlin, nach China, nach links/rechts (向左/右), nach Hause (回家)\n\n"
                           "2. 【in + Akkusativ】：用于【带冠词的国家、封闭建筑物内部】：\n"
                           "   • in die Schweiz (去瑞士), in die Türkei, in die USA (Pl.)\n"
                           "   • in die Schule, ins Kino (in das Kino), in den Supermarkt\n\n"
                           "3. 【zu + Dativ】：用于【具体的人、机构或地标场所】：\n"
                           "   • zum Arzt (去医生那里), zu Peter (去彼得家), zum Bahnhof (去火车站)"
            },
            {
                "heading": "三、祈使句全体系 (Imperativ) 生成法则",
                "content": "德语命令与指示句分为三大对象，构成规则严密：\n\n"
                           "1. 【对你 (du)】：\n"
                           "   • 规则：以现在时 du 变位为基准，【去掉人称代词 du】并【砍掉词尾 -st】！\n"
                           "   • kommen -> du kommst -> Komm!\n"
                           "   • machen -> du machst -> Mach deine Hausaufgaben!\n"
                           "   • 变音动词注意：a -> ä 的变音必须还原！(fahren -> du fährst -> Fahr langsam!)\n"
                           "     但是 e -> i 的换音必须保留！(lesen -> du liest -> Lies das Buch! / helfen -> Hilf mir!)\n\n"
                           "2. 【对你们 (ihr)】：\n"
                           "   • 规则：直接使用 ihr 变位形式，只需【去掉人称代词 ihr】！\n"
                           "   • Kommt bitte pünktlich! / Macht die Bücher auf!\n\n"
                           "3. 【对您/您们 (Sie)】：\n"
                           "   • 规则：动词原形居首，保留代词 Sie！\n"
                           "   • Steigen Sie hier bitte aus!"
            },
            {
                "heading": "四、高频实战场景与问路导航用语",
                "content": "• 问路标准交际：\n"
                           "  - Entschuldigung, wie komme ich zum Hauptbahnhof?\n"
                           "  - Gehen Sie geradeaus, dann die zweite Straße nach rechts!\n"
                           "  - Nehmen Sie den Bus Linie 100 bis zum Alexanderplatz!"
            },
            {
                "heading": "五、祈使句与交通出行速记口诀",
                "content": "【祈使句造句速记诀】：\n"
                           "命令 du 砍 -st，人称代词直接弃；\n"
                           "a 变 ä 变音脱，e 换 i 换音留；\n"
                           "你们 ihr 只去代，变位动词照样在；\n"
                           "尊称 Sie 最简单，颠倒顺序加惊叹！"
            }
        ]
    },
    "A1_L10": {
        "title": "动词 gefallen & passen、指示代词与购物句型",
        "sections": [
            {
                "heading": "一、动词 gefallen (喜欢/中意) 的倒置句法结构",
                "content": "gefallen 的句式逻辑与中文‘我喜欢某物’相反，在德语中是‘某物使我感到中意’：\n\n"
                           "• 句式公式：【引起喜好的物（主语 Nom.）】 + gefallen + 【人（第三格 Dat.）】\n"
                           "  - Das Kleid gefällt mir sehr gut. (我非常喜欢这件连衣裙。)\n"
                           "  - Gefallen dir die Schuhe? (你喜欢这双鞋吗？——鞋是复数，用 gefallen！)\n"
                           "  - Die Farbe gefällt meiner Mutter nicht. (我妈妈不喜欢这个颜色。)\n\n"
                           "【核心提示】：绝不能说 *Ich gefalle das Kleid！主语永远是那件衣服！"
            },
            {
                "heading": "二、passen (尺寸/样式合适) vs stehen (相衬美观)",
                "content": "在服饰购物场景中，德国人精准区分以下三个动词：\n\n"
                           "1. 【passen + Dativ】：指【尺码大小、尺寸、松紧】合适：\n"
                           "   • Die Hose passt mir perfekt, sie ist weder zu eng noch zu weit. (裤子尺码正合我身。)\n\n"
                           "2. 【stehen + Dativ】：指【颜色、款式与人的气质】相衬、好看：\n"
                           "   • Das rote Kleid steht dir hervorragend! (这件红裙子你穿太漂亮了！)\n\n"
                           "3. 【gefallen + Dativ】：指【纯粹的主观审美喜好】：\n"
                           "   • Es gefällt mir, aber es passt mir leider nicht. (我很喜欢，但可惜尺码不合适。)"
            },
            {
                "heading": "三、指示代词 dieser, diese, dieses 变格表",
                "content": "用于特指近处眼前的物品‘这一个’，其词尾变化完全等同于定冠词 der, die, das：\n\n"
                           "┌────────────┬──────────┬──────────┬──────────┬──────────┐\n"
                           "│ 格位       │ 阳性 (m.)│ 阴性 (f.)│ 中性 (n.)│ 复数 (Pl)│\n"
                           "├────────────┼──────────┼──────────┼──────────┼──────────┤\n"
                           "│ Nom. (一格)│ dieser   │ diese    │ dieses   │ diese    │\n"
                           "│ Akk. (四格)│ diesen   │ diese    │ dieses   │ diese    │\n"
                           "│ Dat. (三格)│ diesem   │ dieser   │ diesem   │ diesen   │\n"
                           "└────────────┴──────────┴──────────┴──────────┴──────────┘\n\n"
                           "• 例：Diesen Mantel [Akk.m] nehme ich. (这件大衣我买了。)"
            },
            {
                "heading": "四、商场服饰购物实战交际对话",
                "content": "• 试穿与尺码：\n"
                           "  - Kann ich diesen Pullover anprobieren? (我能试穿这件毛衣吗？)\n"
                           "  - Wo sind die Umkleidekabinen? (试衣间在哪里？)\n"
                           "  - Haben Sie diese Jacke eine Nummer größer / kleiner? (这件夹克有大一码/小一码的吗？)\n\n"
                           "• 价格询问与决定：\n"
                           "  - Was kostet diese Bluse? - Sie kostet 49 Euro.\n"
                           "  - Ich nehme sie! (我买下了！)"
            },
            {
                "heading": "五、歌德 A1 服饰购物速记口诀",
                "content": "【购物动词搭配口诀】：\n"
                           "尺码合适用 passen，气质相衬用 stehen；\n"
                           "心生爱慕用 gefallen，人做三格物作主！\n"
                           "挑选这件 dieser 指示，词尾跟着定冠走！"
            }
        ]
    },
    "A1_L11": {
        "title": "情态动词 wollen / dürfen 与状语时间先于地点原则",
        "sections": [
            {
                "heading": "一、情态动词 wollen (意愿) 与 dürfen (许可) 变位法则",
                "content": "┌──────────────┬──────────┬───────────────────────────┐\n"
                           "│ 人称         │ wollen   │ dürfen (许可/准许)        │\n"
                           "├──────────────┼──────────┼───────────────────────────┤\n"
                           "│ ich          │ will     │ darf                      │\n"
                           "│ du           │ willst   │ darfst                    │\n"
                           "│ er/sie/es    │ will     │ darf                      │\n"
                           "│ wir          │ wollen   │ dürfen                    │\n"
                           "│ ihr          │ wollt    │ dürft                     │\n"
                           "│ sie/Sie      │ wollen   │ dürfen                    │\n"
                           "└──────────────┴──────────┴───────────────────────────┘\n\n"
                           "【核心注意点】：\n"
                           "• dürfen 单数元音 ü 变为 a (ich darf, er darf)；\n"
                           "• wollen 单数元音 o 变为 i (ich will, er will)；一三单数同样无词尾！"
            },
            {
                "heading": "二、严禁表达：nicht dürfen (绝对不允许) 的法律效力",
                "content": "在德语公共场合与交通法规中，nicht dürfen 是最高级别的禁令标志词：\n\n"
                           "• Hier darf man nicht parken! (此处严禁停车！)\n"
                           "• Im Flugzeug darf man nicht rauchen. (飞机上绝对禁止吸烟。)\n"
                           "• Kinder dürfen hier nicht ohne Eltern schwimmen. (儿童未经家长陪同不得在此游泳。)\n\n"
                           "对比：man muss nicht (可以不.../没有必要) vs man darf nicht (万万不可/违法严禁)！"
            },
            {
                "heading": "三、喜好与偏好三级跳：gern -> lieber -> am liebsten",
                "content": "德语不用动词 'like'，而用副词 gern 搭配动词表达喜欢：\n\n"
                           "• 基础喜欢：Ich spiele gern Fußball. (我喜欢踢足球。)\n"
                           "• 比较偏好 (lieber)：Ich spiele aber lieber Tennis. (但我更喜欢打网球。)\n"
                           "• 最为喜爱 (am liebsten)：Am liebsten fahre ich Ski. (我最喜欢滑雪。)"
            },
            {
                "heading": "四、德语句中状语核心次序：时间先于地点 (TeKaMoLo 启蒙)",
                "content": "德语陈述句中，多个状语同时出现时，基本语序为【时间状语 (Temporal) 必须排在 地点状语 (Lokal) 之前】！\n\n"
                           "• 正确：Wir spielen [heute Nachmittag: 时间] [im Park: 地点] Fußball.\n"
                           "• 错误：*Wir spielen im Park heute Nachmittag Fußball. (英语思维语序，德语大忌！)\n"
                           "• 记住公式：【时间 Wann? 先跑，地点 Wo? 押后】！"
            },
            {
                "heading": "五、歌德 A1 业余爱好与空闲生活得分秘籍",
                "content": "【爱好介绍三件套模板】：\n"
                           "In meiner Freizeit treibe ich viel Sport. Am liebsten spiele ich mit meinen Freunden Basketball. Am Wochenende wollen wir zusammen schwimmen gehen.\n"
                           "精准包含 gern 比较级、情态动词 wollen 框架结构及时间先于地点语序，考官直接给满分！"
            }
        ]
    },
    "A1_L12": {
        "title": "无人称代词 es 与天气自然环境表达句式",
        "sections": [
            {
                "heading": "一、代词 es 的多元语法角色全览",
                "content": "在德语中，es 不仅是一个中性人称代词（指代 das Kind / das Buch），更常作为【无人称形式主语 (Unpersönliches Es)】：\n\n"
                           "1. 作为无人称气象主语：自然现象无施动主体，必须由 es 充当语法主语！\n"
                           "2. 作为时间与日期形式主语：Wie spät ist es? - Es ist 10 Uhr.\n"
                           "3. 作为生理与心理感受主语：Es ist mir kalt. (我觉得冷。)\n"
                           "4. 作为固定句型存在主语：Es gibt + Akkusativ."
            },
            {
                "heading": "二、天气现象固定句型矩阵",
                "content": "┌──────────────────┬──────────────┬───────────────────────────┐\n"
                           "│ 表达类型         │ 核心结构     │ 经典示范句                │\n"
                           "├──────────────────┼──────────────┼───────────────────────────┤\n"
                           "│ 动词直接表达     │ es + 气象动词│ Es regnet. (下雨了。)     │\n"
                           "│                  │              │ Es schneit. (下雪了。)    │\n"
                           "│                  │              │ Es donnert und blitzt. (雷电交加。)│\n"
                           "├──────────────────┼──────────────┼───────────────────────────┤\n"
                           "│ 形容词作表语     │ es ist + adj.│ Es ist heute sonnig / windig.│\n"
                           "│                  │              │ Es ist sehr kalt / warm.  │\n"
                           "├──────────────────┼──────────────┼───────────────────────────┤\n"
                           "│ 名词结合动词     │ 主语为人/物  │ Die Sonne scheint. (阳光普照。)│\n"
                           "│                  │              │ Der Wind weht stark. (风刮得大。)│\n"
                           "└──────────────────┴──────────────┴───────────────────────────┘"
            },
            {
                "heading": "三、个人体感温度的正确表达 (极高频易错！)",
                "content": "• 【正确表达】：用人称代词第三格 + es ist kalt/warm：\n"
                           "  - Mir ist kalt. (我觉得冷。)\n"
                           "  - Ist dir warm? (你觉得热吗？)\n\n"
                           "• 【致命文化误区】：\n"
                           "  千千万万不能说 *Ich bin kalt！\n"
                           "  在德语中，'Ich bin kalt' 的真实含义是‘我是一个冷酷无情的人’或‘我的尸体已经凉了’！\n"
                           "  表达生理体温感受，必须用 Mir ist kalt / warm！"
            },
            {
                "heading": "四、气象预报与温度读法规范",
                "content": "• 温度数值读法：\n"
                           "  - Heute sind es 25 Grad. (今天气温 25 度。)\n"
                           "  - In Berlin hat es minus fünf Grad. (柏林零下 5 度。)\n"
                           "• 天气预报高频用语：\n"
                           "  - Morgen wird es im Norden bewölkt, im Süden scheint die Sonne."
            },
            {
                "heading": "五、歌德 A1 天气口试与听力避坑口诀",
                "content": "【天气语法口诀】：\n"
                           "风霜雨雪天作怪，无人称 es 当主帅；\n"
                           "冷热感受 mir ist，莫说 ich bin 惹人怪；\n"
                           "度数前面加 Grad，零下记得 minus 带！"
            }
        ]
    },
    "A1_L13": {
        "title": "现在完成时入门 (Perfekt) 与助动词 haben/sein 选择",
        "sections": [
            {
                "heading": "一、现在完成时 (Perfekt) 的构成公式与框架结构",
                "content": "现在完成时是德语口语和日常通信中表达【过去发生事件】最核心的时态：\n\n"
                           "• 【构成黄金公式】：\n"
                           "  【变位助动词 haben / sein (位置 2)】 + ...... + 【第二分词 Partizip II (必须甩至句末！)】\n\n"
                           "• 经典示范：\n"
                           "  - [Pos 1]  [Pos 2: 助动词]   [时间/地点/宾语]          [句末: Partizip II]\n"
                           "    Ich      habe              gestern eine neue Jacke   gekauft.\n"
                           "    Wir      sind              am Wochenende nach Köln   gefahren."
            },
            {
                "heading": "二、第二分词 (Partizip II) 构成规则",
                "content": "1. 【规则动词 (Regelmäßige Verben)】：\n"
                           "   ge- + 动词词干 + -(e)t\n"
                           "   • machen -> gemacht, kaufen -> gekauft, hören -> gehört, arbeiten -> gearbeitet\n\n"
                           "2. 【不规则/强变化动词 (Unregelmäßige Verben)】：\n"
                           "   通常以 ge- 开头，词尾为 -en，词干元音往往改变：\n"
                           "   • trinken -> getrunken, essen -> gegessen, sprechen -> gesprochen, schreiben -> geschrieben\n\n"
                           "3. 【特殊前缀动词的分词规则】：\n"
                           "   • 可分动词：ge- 必须【插入在前缀与词干中间】！(einkaufen -> eingekauft, aufstehen -> aufgestanden)\n"
                           "   • 不可分动词 (be-, ge-, er-, ver-, zer-) 及以 -ieren 结尾的外来动词：【绝不能加 ge-】！\n"
                           "     (bezahlen -> bezahlt, studieren -> studiert, telefonieren -> telefoniert)"
            },
            {
                "heading": "三、助动词 haben vs sein 黄金分界定律",
                "content": "什么时候用 sein，什么时候用 haben 做助动词？牢记三大法则：\n\n"
                           "1. 【选用 sein 的三大情况】：\n"
                           "   • ① 表达【空间位置移动 (Ortswechsel)】的不及物动词：gehen, fahren, fliegen, kommen, laufen, reisen\n"
                           "     - Ich bin nach Berlin gefahren.\n"
                           "   • ② 表达【身体/生命状态改变 (Zustandswechsel)】的动词：aufstehen, aufwachen (醒来), sterben, einschlafen\n"
                           "     - Er ist um 7 Uhr aufgestanden.\n"
                           "   • ③ 两个特殊自身助动词：sein (ist gewesen) 和 bleiben (ist geblieben)！\n"
                           "     - Ich bin zu Hause geblieben.\n\n"
                           "2. 【选用 haben 的情况】：\n"
                           "   其余所有及物动词（带第四格宾语）、反身动词及大部分状态不动的不及物动词（haben, machen, schlafen, arbeiten...）统一用 haben！"
            },
            {
                "heading": "四、高频生活完成时句式范例",
                "content": "• 昨天日程陈述：\n"
                           "  - Gestern habe ich bis 18 Uhr im Büro gearbeitet. Danach bin ich mit Freunden ins Kino gegangen.\n"
                           "• 节日庆祝经历：\n"
                           "  - Wir haben Weihnachten mit der ganzen Familie gefeiert und sehr gut gegessen."
            },
            {
                "heading": "五、歌德 A1 完成时答题秘籍与速记口诀",
                "content": "【助动词 sein 选用歌谣】：\n"
                           "跑跳走飞位置移，醒来睡去状态变；\n"
                           "sein 和 bleiben 不离弃，助动词 sein 顶在前！\n"
                           "其余全用 haben 挑，分词沉底莫搞偏！"
            }
        ]
    },
    "A1_L14": {
        "title": "德语数字倒序读法、序数词与日期表达体系",
        "sections": [
            {
                "heading": "一、21 至 99 德语数字倒序读法铁律",
                "content": "德语数字在 21-99 之间，有着与中文和英语完全相反的读法——【个位数先读，十位数后读】！\n\n"
                           "• 构成公式：【个位数】 + und + 【十位数】\n"
                           "  - 21 = einundzwanzig (1 和 20，注意 eins 省略为 ein)\n"
                           "  - 35 = fünfunddreißig (5 和 30)\n"
                           "  - 48 = achtundvierzig (8 和 40)\n"
                           "  - 99 = neunundneunzig (9 和 90)\n\n"
                           "【听力防坑秘籍】：德国人念数字时先报尾数，听写时务必听完全部，切勿听到 'ein...' 就先下笔写 '1...'！"
            },
            {
                "heading": "二、序数词 (Ordinalzahlen) 构成规则",
                "content": "序数词表示‘第几个’或用于表示日期：\n\n"
                           "1. 【1 至 19 的序数词】：在基数词后加 -te (带定冠词时)\n"
                           "   • 1. = der erste (特殊！)\n"
                           "   • 3. = der dritte (特殊！)\n"
                           "   • 7. = der siebte (特殊，去 en)\n"
                           "   • 其余规则加 -te：der zweite, der vierte, der zehnte...\n\n"
                           "2. 【20 及以上的序数词】：在基数词后加 -ste\n"
                           "   • 20. = der zwanzigste\n"
                           "   • 21. = der einundzwanzigste\n"
                           "   • 30. = der dreißigste"
            },
            {
                "heading": "三、日期的书写与读法 (Datum)",
                "content": "在德语中，日期采用【日.月.年】格式，阿拉伯数字后必须打一个实心圆点表示序数词！\n\n"
                           "• 书写：der 15. Oktober 2026 或 15.10.2026\n"
                           "• 读法：\n"
                           "  - 第一格 (作为日期主语)：Heute ist der fünfzehnte Oktober. (加 -e)\n"
                           "  - 第三格 (在某个具体日期，带介词 am)：\n"
                           "    Ich habe am fünfzehnten Oktober Geburtstag. (am = an dem，加 -en！)\n"
                           "    【歌德 A1 听力必考】：只要听到 am...，日期词尾必定读 [-tən] 或 [-stən]！"
            },
            {
                "heading": "四、钟点时刻的口语与正式官方表达",
                "content": "┌──────────┬──────────────────────────┬────────────────────────┐\n"
                           "│ 时间     │ 日常生活口语表达         │ 官方/广播正式表达      │\n"
                           "├──────────┼──────────────────────────┼────────────────────────┤\n"
                           "│ 08:00    │ acht Uhr                 │ acht Uhr               │\n"
                           "│ 08:15    │ Viertel nach acht        │ acht Uhr fünfzehn      │\n"
                           "│ 08:30    │ halb neun (差半小时到9点!)│ acht Uhr dreißig       │\n"
                           "│ 08:45    │ Viertel vor neun         │ acht Uhr fünfundvierzig│\n"
                           "│ 08:25    │ fünf vor halb neun       │ acht Uhr fünfundzwanzig│\n"
                           "└──────────┴──────────────────────────┴────────────────────────┘\n\n"
                           "【致命陷阱 halb】：\n"
                           "halb neun 是 8:30（不是 9:30）！德国人的逻辑是：已经走了一半走向 9 点了！"
            },
            {
                "heading": "五、数字与日期考试速记诀",
                "content": "【数字速记歌谣】：\n"
                           "二十以上倒着念，先念个位再 und 连；\n"
                           "1 到 19 加 -te，20 往后加 -ste；\n"
                           "看到 halb 往前减一小时，看到 am 词尾加 -en！"
            }
        ]
    },
    "A1_L15": {
        "title": "歌德 A1 考点全景梳理与终极应试策略",
        "sections": [
            {
                "heading": "一、歌德 A1 考试四大模块分值与时间架构",
                "content": "歌德 A1 (Start Deutsch 1) 考试总分 100 分，60 分合格获得证书：\n\n"
                           "1. 【听力 (Hören)】：20 分钟，3 个部分共 15 题 (每题 1.66 分，折算 25 分)\n"
                           "2. 【阅读 (Lesen)】：25 分钟，3 个部分共 15 题 (信息匹配、真实告示、便条)\n"
                           "3. 【写作 (Schreiben)】：20 分钟，Teil 1 填表格 (5项)，Teil 2 写便条/邮件 (约30词)\n"
                           "4. 【口语 (Sprechen)】：约 15 分钟，4 人小组面试：\n"
                           "   - Teil 1: 个人信息自我介绍 + 现场拼写单词 + 念电话/手机号码\n"
                           "   - Teil 2: 抽单词卡提问并回答日常问题\n"
                           "   - Teil 3: 抽图片卡提出请求并做出动作回应"
            },
            {
                "heading": "二、写作 Teil 2 便条/邮件满分黄金模板",
                "content": "A1 写作题目给出 3 个要点 (Leitpunkte)，每个要点必须写 1-2 句完整德语句子：\n\n"
                           "【官方高分通用模板】：\n"
                           "Liebe Anna, / Lieber Peter, (熟人称呼，末尾用逗号)\n"
                           "(首句首字母小写！) wie geht es dir? Ich hoffe, es geht dir gut.\n"
                           "[要点1: 阐明事由] Ich mache am Samstag eine Geburtstagsparty.\n"
                           "[要点2: 提出邀请] Ich lade dich herzlich ein. Kannst du kommen?\n"
                           "[要点3: 交代时间地点] Die Party fängt um 18 Uhr bei mir zu Hause an.\n"
                           "Bitte antworte mir bald.\n"
                           "Viele Grüße (信末无标点！)\n"
                           "Dein Michael / Deine Maria"
            },
            {
                "heading": "三、口语 Teil 1 自我介绍万能句式",
                "content": "1. Name: Mein Name ist Lin Wang. / Ich heiße Lin Wang.\n"
                           "2. Alter: Ich bin 24 Jahre alt.\n"
                           "3. Land: Ich komme aus China.\n"
                           "4. Wohnort: Ich wohne jetzt in Frankfurt.\n"
                           "5. Sprachen: Meine Muttersprache ist Chinesisch. Ich spreche auch Englisch und ein bisschen Deutsch.\n"
                           "6. Beruf: Ich bin Student / Ich arbeite als Softwareentwickler.\n"
                           "7. Hobby: Meine Hobbys sind Schwimmen und Musik hören.\n\n"
                           "【考官加问】：\n"
                           "• 'Können Sie Ihren Nachnamen buchstabieren?' -> W-A-N-G [veː - aː - ɛn - ɡeː]\n"
                           "• 'Wie ist Ihre Handynummer?' -> 0176... (清晰单数报数)"
            },
            {
                "heading": "四、中国考生 A1 最容易丢分的十大语法陷阱",
                "content": "1. 漏大写名词首字母（写作直接扣分）。\n"
                           "2. 动词现在时变位错漏（如 du liest 写成 *du lesst）。\n"
                           "3. 动词没有放在第 2 位（如 *Gestern ich habe...）。\n"
                           "4. 第四格阳性漏变 den / einen。\n"
                           "5. 第三人称单数情态动词加了 -t（如 *er kannt / *er willt）。\n"
                           "6. 可分动词前缀忘记甩到句末。\n"
                           "7. kein 与 nicht 混淆。\n"
                           "8. 交通工具 mit 后面没有用第三格。\n"
                           "9. halb 时间误解多加一小时。\n"
                           "10. 过去完成时助动词 sein 与 haben 选错。"
            },
            {
                "heading": "五、A1 考前 24 小时通关速记口诀",
                "content": "【通关定心丸】：\n"
                           "名大写，动居二，人称变位莫大意；\n"
                           "阳性四格变一个，可分前缀甩句末；\n"
                           "信件称呼要分清，男 Lieber 女 Liebe；\n"
                           "听力两遍先抓题，从容自信过 A1！"
            }
        ]
    }
}
