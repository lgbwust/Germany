#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enriched Grammar Content for Level A2 (Lessons 1-15):
Präteritum, Genitiv, Wechselpräpositionen, Adjektivdeklination (Typ I & II),
Konjunktiv II (Höflichkeit & Irreal), Passiv (Präsens), Relativsätze, Nebensätze (weil, dass, wenn, als),
Double Object Order, and Goethe A2 Exam Strategy.
"""

A2_GRAMMAR = {
    "A2_L01": {
        "title": "过去时 (Präteritum) 与时间连词 als vs wenn",
        "sections": [
            {
                "heading": "一、sein 与 haben 的过去时完整变位表",
                "content": "在日常口语与叙述中，助动词 sein 和 haben 极少用完成时，而是习惯直接使用过去时 (Präteritum)：\n\n"
                           "┌──────────────┬──────────────────┬───────────────────────────┐\n"
                           "│ 人称         │ sein (war: 曾是) │ haben (hatte: 曾有)       │\n"
                           "├──────────────┼──────────────────┼───────────────────────────┤\n"
                           "│ ich          │ war              │ hatte                     │\n"
                           "│ du           │ warst            │ hattest                   │\n"
                           "│ er/sie/es    │ war              │ hatte                     │\n"
                           "│ wir          │ waren            │ hatten                    │\n"
                           "│ ihr          │ wart             │ hattet                    │\n"
                           "│ sie/Sie      │ waren            │ hatten                    │\n"
                           "└──────────────┴──────────────────┴───────────────────────────┘\n\n"
                           "【核心特征】：过去时中第 1 人称 (ich) 与第 3 人称单数 (er/sie/es) 形式完全相同，无额外人称词尾！"
            },
            {
                "heading": "二、规则动词过去时构成法则",
                "content": "规则动词过去时通过在词干与人称词尾之间插入时态标记词缀 -te- 构成：\n\n"
                           "• 词缀公式：动词词干 + -te- + 人称词尾\n"
                           "  - ich lern-te\n"
                           "  - du lern-te-st\n"
                           "  - er/sie/es lern-te\n"
                           "  - wir lern-te-n\n"
                           "  - ihr lern-te-t\n"
                           "  - sie/Sie lern-te-n\n\n"
                           "• 词干以 -t, -d 结尾的动词加 -ete-：arbeiten -> ich arbeitete, du arbeitetest."
            },
            {
                "heading": "三、时间连词 als vs wenn 的根本辨析",
                "content": "这是 A2 阶段最核心、歌德必考的语法考点：\n\n"
                           "1. 【als】：专用于【过去发生的、单次特定的时间点或阶段】：\n"
                           "   • Als ich 18 Jahre alt war, machte ich das Abitur. (当我18岁那年，我参加了高考。)\n"
                           "   • Als wir gestern nach Hause kamen, regnete es in Strömen. (当我们昨天到家时，正下大雨。)\n\n"
                           "2. 【wenn】：用于【现在的事件】、【将来的事件】或【过去反复多次发生的事件 (immer wenn)】：\n"
                           "   • 现在/将来：Wenn das Wetter schön ist, gehen wir spazieren.\n"
                           "   • 过去重复：Immer wenn ich krank war, kochte meine Mutter Suppe. (每当我生病时...)\n\n"
                           "【从句语序】：无论是 als 还是 wenn，引导从句时，【变位动词永远置于从句句末】！"
            },
            {
                "heading": "四、个人生平与简历描述实战句式",
                "content": "• 出生与成长：\n"
                           "  - Ich wurde 1998 in Shanghai geboren. Als Kind wollte ich Musiker werden.\n"
                           "• 教育与求学：\n"
                           "  - Nach der Schule studierte ich Germanistik und Informatik an der Universität zu Köln.\n"
                           "• 工作经历：\n"
                           "  - Von 2022 bis 2025 arbeitete ich als Projektmanager bei Bosch in Stuttgart."
            },
            {
                "heading": "五、歌德 A2 过去时速记秘籍与口诀",
                "content": "【als 与 wenn 辨别口诀】：\n"
                           "过去单次只能 als，少年经历忆往昔；\n"
                           "现在将来全用 wenn，过去重复 immer wenn；\n"
                           "war 和 hatte 熟在心，口语自如展生平！"
            }
        ]
    },
    "A2_L02": {
        "title": "第二格 (Genitiv) 与原因连词 weil / da",
        "sections": [
            {
                "heading": "一、第二格 (Genitiv) 冠词变格与名词词尾法则",
                "content": "第二格表示‘所属关系（...的）’。在第二格中，不仅冠词变化，【阳性和中性名词本身也必须加词尾 -(e)s】！\n\n"
                           "┌────────────┬──────────────┬──────────┬──────────────┬──────────┐\n"
                           "│ 格位       │ 阳性 (m.)    │ 阴性 (f.)│ 中性 (n.)    │ 复数 (Pl)│\n"
                           "├────────────┼──────────────┼──────────┼──────────────┼──────────┤\n"
                           "│ 定冠词     │ des ...-(e)s │ der      │ des ...-(e)s │ der      │\n"
                           "│ 不定冠词   │ eines ...-(e)s│ einer   │ eines ...-(e)s│ ——      │\n"
                           "│ 否定冠词   │ keines ...-(e)s│ keiner │ keines ...-(e)s│ keiner │\n"
                           "│ 物主代词   │ meines ...-(e)s│ meiner │ meines ...-(e)s│ meiner │\n"
                           "└────────────┴──────────────┴──────────┴──────────────┴──────────┘\n\n"
                           "【名词词尾 -(e)s 加法】：\n"
                           "• 单音节词或以 -s, -ß, -z, -x 结尾的词，加 -es：des Kindes, des Mannes, des Hauses\n"
                           "• 多音节词通常直接加 -s：des Lehrers, des Computers, des Autos\n"
                           "• 阴性与复数名词：本身不加任何词尾！"
            },
            {
                "heading": "二、弱变化阳性名词 (N-Deklination) 启蒙",
                "content": "有一小批特殊的阳性名词，除了第一格单数外，在第二格、第三格、第四格【必须全部加上 -(e)n】：\n\n"
                           "• 代表词汇：der Student, der Kollege, der Junge, der Herr, der Kunde, der Nachbar\n"
                           "  - Nom.: der Kollege\n"
                           "  - Akk.: den Kollegen\n"
                           "  - Dat.: dem Kollegen\n"
                           "  - Gen.: des Kollegen (注意：加 -n，绝不加 -s！)"
            },
            {
                "heading": "三、原因从句连词：weil 与 da 的从句框形语序",
                "content": "表达因果关系时，weil (因为) 引导从属从句：\n\n"
                           "• 【语序铁律】：变位动词被踢到从句最末尾！\n"
                           "  [主句: V2]                              [weil 从句: 变位动词句末]\n"
                           "  Er lernt jeden Tag fleißig Deutsch,    weil er in Deutschland studieren [句末!] möchte.\n\n"
                           "• 【主从句调换】：当 weil / da 从句在前时，从句动词在逗号前，主句动词紧贴逗号在第 1 位！\n"
                           "  Weil das Wetter heute schlecht [从句末] ist, [主句1位] bleiben wir heute zu Hause.\n"
                           "  (即俗称的‘逗号两边动词碰头’！)"
            },
            {
                "heading": "四、第二格在现实与口语中的替换结构 (von + Dativ)",
                "content": "在日常口语中，第二格常被 von + 第三格代替：\n\n"
                           "• 书面标准语 (第二格)：das Auto meines Vaters / die Tasche der Lehrerin\n"
                           "• 日常口语 (第三格替代)：das Auto von meinem Vater / die Tasche von der Lehrerin\n"
                           "在歌德 A2 考试写作中，使用标准第二格会显著提升阅卷老师的评分好感！"
            },
            {
                "heading": "五、第二格与原因从句速记口诀",
                "content": "【第二格与 weil 口诀】：\n"
                           "二格阳中是 des -(e)s，二格阴复变成了 der；\n"
                           "所属关系 des 表现，弱变阳性加 -en 站；\n"
                           "weil 引导从属从，变位动词句末冲；\n"
                           "从句如果冲在前，逗号两头动词连！"
            }
        ]
    },
    "A2_L03": {
        "title": "情态动词过去时 (Präteritum der Modalverben) 与商务邮件",
        "sections": [
            {
                "heading": "一、六大情态动词过去时变位全景表",
                "content": "【核心铁律】：所有情态动词在过去时中【全部去除元音变音 (Kein Umlaut)】！\n\n"
                           "┌────────────┬──────────┬──────────┬──────────┬──────────┬──────────┬──────────┐\n"
                           "│ 人称       │ können   │ müssen   │ dürfen   │ wollen   │ sollen   │ mögen    │\n"
                           "├────────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────┤\n"
                           "│ ich        │ konnte   │ musste   │ durfte   │ wollte   │ sollte   │ mochte   │\n"
                           "│ du         │ konntest │ musstest │ durftest │ wolltest │ solltest │ mochtest │\n"
                           "│ er/sie/es  │ konnte   │ musste   │ durfte   │ wollte   │ sollte   │ mochte   │\n"
                           "│ wir        │ konnten  │ mussten  │ durften  │ wollten  │ sollten  │ mochten  │\n"
                           "│ ihr        │ konntet  │ musstet  │ durftet  │ wolltet  │ solltet  │ mochtet  │\n"
                           "│ sie/Sie    │ konnten  │ mussten  │ durften  │ wollten  │ sollten  │ mochten  │\n"
                           "└────────────┴──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘\n\n"
                           "无论是口语还是写作，描述过去的能够、不得不、打算，一律用过去时代替完成时！"
            },
            {
                "heading": "二、情态动词过去时与句末动词原形搭配",
                "content": "语序与现在时情态框形完全一致，只是位置 2 换成了过去时态：\n\n"
                           "• Gestern konnte ich leider nicht zum Unterricht [句末] kommen, weil ich krank war.\n"
                           "• Letztes Jahr durfte ich in den Sommerferien nach Deutschland [句末] reisen.\n"
                           "• Früher wollte mein Bruder immer Pilot [句末] werden."
            },
            {
                "heading": "三、德语职场商务邮件标准规范",
                "content": "1. 【尊称抬头 (Anrede)】：\n"
                           "   • 认识姓名：Sehr geehrte Frau Müller, / Sehr geehrter Herr Schmidt, (后接逗号！)\n"
                           "   • 不知具体姓名：Sehr geehrte Damen und Herren,\n\n"
                           "2. 【首句小写法则】：逗号之后第一句首字母【必须小写】！\n"
                           "   • ich schreibe Ihnen, weil...\n\n"
                           "3. 【结束问候语与署名】：\n"
                           "   • Mit freundlichen Grüßen (信末无逗号无标点！)\n"
                           "   • [您的全名: Lin Wang]"
            },
            {
                "heading": "四、办公室日常日程协调与请假标准表达",
                "content": "• 预约与推迟：\n"
                           "  - Könnten wir unseren Termin um einen Tag verschieben?\n"
                           "  - Ich musste gestern Überstunden machen, daher konnte ich die E-Mail nicht rechtzeitig beantworten.\n"
                           "• 确认与感谢：\n"
                           "  - Ich danke Ihnen für das angenehme Telefongespräch."
            },
            {
                "heading": "五、歌德 A2 职场写作得分秘籍",
                "content": "【情态过去时考题抓分点】：\n"
                           "写信给老师或老板道歉‘昨天没能来’：\n"
                           "Gestern konnte ich nicht zur Arbeit kommen, weil ich hohes Fieber hatte und zum Arzt musste. Ich bitte um Entschuldigung.\n"
                           "精准融合 konnte + musste + weil 框形，写作轻松拿下全部分值！"
            }
        ]
    },
    "A2_L04": {
        "title": "静三动四双向介词 (Wechselpräpositionen)",
        "sections": [
            {
                "heading": "一、九大双向介词矩阵与判定原则",
                "content": "德语有 9 个介词既可以接第三格，也可以接第四格，称为 Wechselpräpositionen：\n\n"
                           "【九大金刚】：an, auf, hinter, in, neben, über, unter, vor, zwischen\n\n"
                           "┌────────────┬────────────────────────────┬────────────────────────────┐\n"
                           "│ 提问疑问词 │ 格位要求                   │ 物理本质                   │\n"
                           "├────────────┼────────────────────────────┼────────────────────────────┤\n"
                           "│ Wo? (哪里) │ + 第三格 (Dativ)           │ 静态位置、状态、停留在某处 │\n"
                           "│ Wohin?(何处│ + 第四格 (Akkusativ)       │ 动态方向、位移、趋向目标处 │\n"
                           "└────────────┴────────────────────────────┴────────────────────────────┘\n\n"
                           "• 静态例句 (Wo? + Dat.)：Das Buch liegt auf dem Tisch.\n"
                           "• 动态例句 (Wohin? + Akk.)：Ich lege das Buch auf den Tisch."
            },
            {
                "heading": "二、四大成对方位动词深度对照表 (极核心考点！)",
                "content": "德语通过及物动词（带四格宾语）与不及物动词精准对应位置与动作：\n\n"
                           "┌──────────┬──────────────────────────┬──────────┬──────────────────────────┐\n"
                           "│ 动态动词 │ 变位/用法 (Wohin + Akk.) │ 静态动词 │ 变位/用法 (Wo + Dat.)    │\n"
                           "├──────────┼──────────────────────────┼──────────┼──────────────────────────┤\n"
                           "│ stellen  │ 放立 (stellt, stellte...)│ stehen   │ 站立 (steht, stand, gest.)│\n"
                           "│ legen    │ 放平 (legt, legte, gel.) │ liegen   │ 平躺 (liegt, lag, gelegen)│\n"
                           "│ setzen   │ 放置/使坐 (setzt, setzte)│ sitzen   │ 坐着 (sitzt, saß, gesess.)│\n"
                           "│ hängen   │ 挂上去 (hängt, hängte)   │ hängen   │ 悬挂着 (hängt, hing, geh.)│\n"
                           "└──────────┴──────────────────────────┴──────────┴──────────────────────────┘"
            },
            {
                "heading": "三、经典方位对比例句剖析",
                "content": "1. stellen vs stehen:\n"
                           "   • Wohin? -> Ich stelle die Vase auf den Tisch. (动态，阳性四格 den Tisch)\n"
                           "   • Wo? -> Die Vase steht auf dem Tisch. (静态，阳性三格 dem Tisch)\n\n"
                           "2. legen vs liegen:\n"
                           "   • Wohin? -> Er legt die Zeitung unter das Sofa. (动态，中性四格 das Sofa)\n"
                           "   • Wo? -> Die Zeitung liegt unter dem Sofa. (静态，中性三格 dem Sofa)\n\n"
                           "3. an vs auf (介词细微差别)：\n"
                           "   • an: 附着于垂直立面 (an die Wand hängen / an der Wand hängen)\n"
                           "   • auf: 放置于水平表面 (auf den Tisch legen / auf dem Tisch liegen)"
            },
            {
                "heading": "四、高频介词缩合形态速查",
                "content": "• in + das = ins (ins Bett, ins Kino)\n"
                           "• an + das = ans (ans Fenster, ans Meer)\n"
                           "• auf + das = aufs (aufs Land)\n"
                           "• in + dem = im (im Schrank)\n"
                           "• an + dem = am (am Bahnhof)"
            },
            {
                "heading": "五、静三动四通关口诀",
                "content": "【双向介词黄金歌诀】：\n"
                           "九大介词要牢记，in, an, auf, neben, hinter, vor, über, unter, zwischen；\n"
                           "问 Wo 静止用三格，问 Wohin 位移四格随；\n"
                           "legen, stellen, setzen, 动四及物亲手放；\n"
                           "liegen, stehen, sitzen, 静三稳坐不动摇！"
            }
        ]
    },
    "A2_L05": {
        "title": "形容词比较级、最高级与退货维权句型",
        "sections": [
            {
                "heading": "一、规则形容词比较级与最高级构成法则",
                "content": "德语形容词等级变化规律性极强：\n\n"
                           "• 原级 (Positiv) -> 比较级 (Komparativ: 加 -er) -> 最高级 (Superlativ: am ...-(e)sten)\n"
                           "  - schnell -> schneller -> am schnellsten\n"
                           "  - klein -> kleiner -> am kleinsten\n"
                           "  - billig -> billiger -> am billigsten\n\n"
                           "【最高级补加 -e- 规则】：以 -d, -t, -s, -ß, -z 结尾的形容词，最高级加 -esten 方便发音：\n"
                           "  - alt -> älter -> am ältesten\n"
                           "  - heiß -> heißer -> am heißesten"
            },
            {
                "heading": "二、单音节形容词的变音法则与三大核心不规则",
                "content": "1. 【变音规则】：词根含 a, o, u 的单音节常用形容词，比较级和最高级通常要【变音】！\n"
                           "   • alt -> älter -> am ältesten\n"
                           "   • groß -> größer -> am größten (注意去 s)\n"
                           "   • warm -> wärmer -> am wärmsten\n"
                           "   • jung -> jünger -> am jüngsten\n\n"
                           "2. 【四大必须死记的不规则形容词】：\n"
                           "   ┌────────────┬────────────┬────────────────────────┐\n"
                           "   │ 原级       │ 比较级     │ 最高级                 │\n"
                           "   ├────────────┼────────────┼────────────────────────┤\n"
                           "   │ gut (好)   │ besser     │ am besten              │\n"
                           "   │ viel (多)  │ mehr       │ am meisten             │\n"
                           "   │ gern (乐意)│ lieber     │ am liebsten            │\n"
                           "   │ nah (近)   │ näher      │ am nächsten            │\n"
                           "   └────────────┴────────────┴────────────────────────┘"
            },
            {
                "heading": "三、比较句型结构：so ... wie vs ... als",
                "content": "• 【同级比较（一样...）】：so + 原级 + wie\n"
                           "  - Mein Zimmer ist genauso groß wie dein Zimmer. (我的房间和你的一样大。)\n"
                           "  - Er arbeitet so fleißig wie sein Vater.\n\n"
                           "• 【不同级比较（比...更...）】：比较级 + als\n"
                           "  - Dieses Handy ist viel moderner als das alte Modell. (这部手机比旧款先进得多。)\n"
                           "  - Berlin ist größer als München.\n\n"
                           "【警惕】：绝不可把 als 写成 *wie！'比'永远用 als！"
            },
            {
                "heading": "四、商品消费与售后退换货 (Reklamation) 维权表达",
                "content": "• 表达缺陷：\n"
                           "  - Das Gerät funktioniert leider nicht mehr. Es ist kaputt.\n"
                           "  - Der Pullover hat ein Loch und ist kleiner als angegeben.\n"
                           "• 提出维权诉求：\n"
                           "  - Ich möchte das Produkt umtauschen oder mein Geld zurückbekommen.\n"
                           "  - Hier ist der Kassenbon (收据) und der Garantieschein."
            },
            {
                "heading": "五、形容词比较级速记口诀",
                "content": "【比较级速记歌】：\n"
                           "比较加 -er 最高 -sten，短词变音 ä, ö, ü；\n"
                           "一样大小 so ... wie，超越比较用一个 als；\n"
                           "gut 变 besser, am besten，viel 变 mehr, am meisten 牢记心！"
            }
        ]
    },
    "A2_L06": {
        "title": "第二虚拟式 (Konjunktiv II) 礼貌表达与交通出行",
        "sections": [
            {
                "heading": "一、第二虚拟式核心构成：würde + 动词原形",
                "content": "第二虚拟式在日常生活与交际中主要用于表达【极度客气的请求、委婉建议和礼貌询问】。\n\n"
                           "• 【万能公式】：【würde 变位 (Pos 2)】 + ...... + 【实义动词原形 (句末)】\n"
                           "┌──────────────┬──────────────────┬───────────────────────────┐\n"
                           "│ 人称         │ würde 变位       │ 示范例句                  │\n"
                           "├──────────────┼──────────────────┼───────────────────────────┤\n"
                           "│ ich          │ würde            │ Ich würde gern ein Ticket buchen.│\n"
                           "│ du           │ würdest          │ Würdest du mir bitte das Salz geben?│\n"
                           "│ er/sie/es    │ würde            │ Er würde gern mitkommen.  │\n"
                           "│ wir          │ würden           │ Wir würden Sie gern einladen.│\n"
                           "│ ihr          │ würdet           │ Würdet ihr mir bitte helfen?│\n"
                           "│ sie/Sie      │ würden           │ Würden Sie das bitte wiederholen?│\n"
                           "└──────────────┴──────────────────┴───────────────────────────┘"
            },
            {
                "heading": "二、常用助动词与情态动词的独立第二虚拟式",
                "content": "haben, sein 以及情态动词 können, dürfen 通常不加 würde，而是使用它们原生的第二虚拟式：\n\n"
                           "1. 【hätte (haben)】：\n"
                           "   • Ich hätte gern eine Tasse Kaffee. (我想要一杯咖啡。——最地道客气的点餐句！)\n"
                           "   • Hätten Sie heute Nachmittag kurz Zeit für mich?\n\n"
                           "2. 【wäre (sein)】：\n"
                           "   • Das wäre fantastisch! (那简直太棒了！)\n"
                           "   • Es wäre sehr nett, wenn Sie mir helfen könnten.\n\n"
                           "3. 【könnte (können)】：\n"
                           "   • Könnten Sie mir bitte sagen, wo der Bahnsteig 3 ist? (您能否告诉我3号站台在哪？)"
            },
            {
                "heading": "三、铁路出行与购票乘车交际句型",
                "content": "• 购票与车次询问：\n"
                           "  - Ich möchte eine Fahrkarte nach Hamburg, bitte. Einfach oder hin und zurück?\n"
                           "  - Hat der Zug Verspätung? (火车晚点了吗？)\n"
                           "  - Muss ich umsteigen? (我需要中途换乘吗？)\n"
                           "• 寻找座位：\n"
                           "  - Entschuldigung, ist dieser Platz noch frei?"
            },
            {
                "heading": "四、客气请求三大递进阶梯",
                "content": "• 阶梯 1 (直陈式命令): Geben Sie mir das Ticket! (生硬，易让人不适)\n"
                           "• 阶梯 2 (情态直陈): Können Sie mir bitte das Ticket geben? (正常礼貌)\n"
                           "• 阶梯 3 (第二虚拟式): Könnten Sie mir freundlicherweise das Ticket geben? (极其得体有教养！)"
            },
            {
                "heading": "五、歌德 A2 口试第二虚拟式提分口诀",
                "content": "【口试礼貌通关诀】：\n"
                           "口试考官最看重，礼貌交流分极重；\n"
                           "开口先带 könnte, hätte，请求全用 würden Sie；\n"
                           "语气温和礼数到，高分证书稳稳拿！"
            }
        ]
    },
    "A2_L07": {
        "title": "形容词定语词尾变格系统 (Typ I 定冠词后弱变化)",
        "sections": [
            {
                "heading": "一、定冠词后形容词弱变化规律 (Typ I: Schwache Deklination)",
                "content": "当形容词放在【定冠词 (der, die, das)】后修饰名词时，称为弱变化。\n"
                           "【核心秘密】：弱变化只有两个词尾——要么是 -e，要么是 -en！\n\n"
                           "┌────────────┬──────────┬──────────┬──────────┬──────────┐\n"
                           "│ 格位       │ 阳性 (m.)│ 阴性 (f.)│ 中性 (n.)│ 复数 (Pl)│\n"
                           "├────────────┼──────────┼──────────┼──────────┼──────────┤\n"
                           "│ Nom. (一格)│ der -e   │ die -e   │ das -e   │ die -en  │\n"
                           "│ Akk. (四格)│ den -en  │ die -e   │ das -e   │ die -en  │\n"
                           "│ Dat. (三格)│ dem -en  │ der -en  │ dem -en  │ den -en  │\n"
                           "│ Gen. (二格)│ des -en  │ der -en  │ des -en  │ der -en  │\n"
                           "└────────────┴──────────┴──────────┴──────────┴──────────┘"
            },
            {
                "heading": "二、著名的“-e 之岛”法则 (Die Insel der -e)",
                "content": "观察上面的表格，加上词尾 -e 的位置只有 5 个格子，像一座小岛：\n\n"
                           "• 【加 -e 的 5 个位置】：\n"
                           "  1. 第一格单数：der alte Mann, die junge Frau, das kleine Kind\n"
                           "  2. 第四格阴性与中性：die junge Frau, das kleine Kind\n\n"
                           "• 【其余所有位置统统加 -en】：\n"
                           "  1. 所有复数 (Plural) 无论何格位，一律加 -en：die alten Männer, die kleinen Kinder\n"
                           "  2. 所有第三格 (Dativ) 无论性属，一律加 -en：mit dem neuen Auto, von der netten Dame\n"
                           "  3. 所有第二格 (Genitiv) 一律加 -en：des neuen Autos\n"
                           "  4. 第四格阳性一律加 -en：Ich sehe den großen Tisch."
            },
            {
                "heading": "三、旅游度假与酒店场景经典例句",
                "content": "• 预订酒店房型：\n"
                           "  - Wir haben das ruhige Zimmer [Nom.n -e] mit dem schönen Balkon [Dat.m -en] gebucht.\n"
                           "• 旅游景点描述：\n"
                           "  - Der alte Dom [Nom.m -e] zieht jedes Jahr Millionen von Touristen an.\n"
                           "  - Ich möchte den berühmten Fernsehturm [Akk.m -en] besichtigen."
            },
            {
                "heading": "四、指示代词与同类冠词的联动法则",
                "content": "dieser (这个), jeder (每个), welcher (哪个) 之后的形容词变化，【完全等同于定冠词弱变化】！\n"
                           "• In diesem modernen Hotel [Dat.n -en] fühlen wir uns sehr wohl.\n"
                           "• Welche neue Tasche [Nom.f -e] gefällt dir am besten?"
            },
            {
                "heading": "五、形容词弱变化速记口诀",
                "content": "【-e 锅底速记法】：\n"
                           "定冠后面看变化，只有 -e 和 -en 挂；\n"
                           "一格单数四格阴中五块地，-e 之岛别忘记；\n"
                           "复数二三四格阳，统统 -en 扫全场！"
            }
        ]
    },
    "A2_L08": {
        "title": "从属连词 dass (宾语从句) 与 wenn (条件/时间从句)",
        "sections": [
            {
                "heading": "一、从属连词 dass 引导的陈述性宾语从句",
                "content": "dass 引导的从句充当主句动词的宾语，变位动词置于从句末尾：\n\n"
                           "• 常见支配 dass 从句的主句动词：\n"
                           "  - wissen (知道): Ich weiß, dass er heute nicht kommt.\n"
                           "  - glauben (相信): Wir glauben, dass die Reise wunderschön wird.\n"
                           "  - hoffen (希望): Ich hoffe, dass du bald wieder gesund wirst.\n"
                           "  - sich freuen (感到高兴): Es freut mich, dass Sie mich besuchen.\n\n"
                           "【逗号铁律】：主句与 dass 从句之间【必须有逗号隔离】！"
            },
            {
                "heading": "二、条件从句 wenn (如果/只要) 的逻辑结构",
                "content": "wenn 表达现实的条件、假设或规则：\n\n"
                           "• 正序：主句在前，wenn 从句在后\n"
                           "  - Ich gehe zum Arzt, wenn ich hohes Fieber habe.\n\n"
                           "• 倒装：wenn 从句在前，主句在后（逗号两端动词紧邻！）\n"
                           "  - Wenn Sie starke Schmerzen haben [从句末], nehmen [主句首] Sie diese Tablette!"
            },
            {
                "heading": "三、dass vs das 的致命拼写混淆",
                "content": "• dass (两个 s)：是从属连词，不能用其他词替换，表示‘...这件事’。\n"
                           "• das (一个 s)：是中性定冠词 (das Kind) 或指示代词/关系代词，可替换为 dieses 或 welches。\n"
                           "【检验法】：如果可以替换成 dieses / welches，拼写作 das；如果后面引导完整从句且无法替换，必须拼写作 dass！"
            },
            {
                "heading": "四、看病急救场景复合句实战",
                "content": "• 症状与病因陈述：\n"
                           "  - Der Notarzt sagt, dass der Patient sofort operiert werden muss.\n"
                           "  - Wenn der Unfall passiert, rufen Sie bitte sofort die Notrufnummer 112 an!"
            },
            {
                "heading": "五、从句标点与语序速查口诀",
                "content": "【从句框形语序口诀】：\n"
                           "连词 dass 和 wenn 一出，逗号先把门关住；\n"
                           "主语紧跟连词后，变位动词句末驻；\n"
                           "前置从句先讲完，主句动词顶前头！"
            }
        ]
    },
    "A2_L09": {
        "title": "过程被动语态 (Vorgangspassiv Präsens) 入门",
        "sections": [
            {
                "heading": "一、过程被动态本质与现在时构成公式",
                "content": "被动语态强调‘事情被怎样处理’，淡化施动者，突出动作过程：\n\n"
                           "• 【现在时被动态黄金公式】：\n"
                           "  【werden 现在时变位 (Pos 2)】 + ...... + 【第二分词 Partizip II (句末)】\n\n"
                           "┌──────────────┬──────────────────┬───────────────────────────┐\n"
                           "│ 人称         │ werden 变位      │ 示范例句                  │\n"
                           "├──────────────┼──────────────────┼───────────────────────────┤\n"
                           "│ ich          │ werde            │ Ich werde operiert.       │\n"
                           "│ du           │ wirst            │ Du wirst abgeholt.        │\n"
                           "│ er/sie/es    │ wird             │ Das Essen wird gekocht.   │\n"
                           "│ wir          │ werden           │ Wir werden informiert.    │\n"
                           "│ ihr          │ werdet           │ Ihr werdet geprüft.       │\n"
                           "│ sie/Sie      │ werden           │ Die Autos werden repariert.│\n"
                           "└──────────────┴──────────────────┴───────────────────────────┘"
            },
            {
                "heading": "二、施动者的介词表达：von (+ Dativ) vs durch (+ Akkusativ)",
                "content": "如果在被动句中必须点明是谁执行了动作，使用介词补足语：\n\n"
                           "1. 【von + 第三格】：用于【主动的人、机构、自然界具体实体】：\n"
                           "   • Der Patient wird von dem Arzt [Dat.m] untersucht.\n"
                           "   • Das Haus wird von einer Baufirma renoviert.\n\n"
                           "2. 【durch + 第四格】：用于【媒介、手段、抽象原因】：\n"
                           "   • Das Paket wird durch die Post geliefert.\n"
                           "   • Das Feuer wurde durch einen Kurzschluss verursacht."
            },
            {
                "heading": "三、主动态转化为被动态的三步转换法",
                "content": "• 主动句：Der Koch [Subjekt: Nom.] schneidet die Kartoffeln [Objekt: Akk.].\n"
                           "  - 第一步：原第四格宾语 (die Kartoffeln) 升级为被动句的主语 (Nominativ)；\n"
                           "  - 第二步：根据新主语匹配 werden 变位 (werden)；\n"
                           "  - 第三步：原及物动词变成第二分词置于句末 (geschnitten)；\n"
                           "• 被动句：Die Kartoffeln werden [von dem Koch] geschnitten."
            },
            {
                "heading": "四、德语区特色美食烹饪制作实战",
                "content": "• 烹饪食谱制作步骤（经典被动态场景）：\n"
                           "  - Zuerst werden die Zwiebeln fein geschnitten und in Butter angebraten.\n"
                           "  - Dann wird das Rindfleisch hinzugefügt und mit Rotwein abgelöscht.\n"
                           "  - Zum Schluss wird das Gericht heiß serviert."
            },
            {
                "heading": "五、被动语态速记口诀",
                "content": "【被动变位速记诀】：\n"
                           "宾语上位作主语，werden 变位居第二；\n"
                           "第二分词压句末，被动态势清晰起；\n"
                           "人出 von 来媒介 durch，公文烹饪必备它！"
            }
        ]
    },
    "A2_L10": {
        "title": "形容词混合变化 (Typ II: 不定冠词与物主代词后)",
        "sections": [
            {
                "heading": "一、不定冠词后形容词混合变化表 (Gemischte Deklination)",
                "content": "在【不定冠词 (ein)】、【否定冠词 (kein)】和【物主代词 (mein, dein...)】之后的形容词变格：\n\n"
                           "┌────────────┬──────────┬──────────┬──────────┬──────────────┐\n"
                           "│ 格位       │ 阳性 (m.)│ 阴性 (f.)│ 中性 (n.)│ 复数 (kein/mein)│\n"
                           "├────────────┼──────────┼──────────┼──────────┼──────────────┤\n"
                           "│ Nom. (一格)│ ein -er  │ eine -e  │ ein -es  │ keine -en    │\n"
                           "│ Akk. (四格)│ einen -en│ eine -e  │ ein -es  │ keine -en    │\n"
                           "│ Dat. (三格)│ einem -en│ einer -en│ einem -en│ keinen -en   │\n"
                           "│ Gen. (二格)│ eines -en│ einer -en│ eines -en│ keiner -en   │\n"
                           "└────────────┴──────────┴──────────┴──────────┴──────────────┘"
            },
            {
                "heading": "二、为什么叫“混合变化”？形态补偿原理",
                "content": "• 当冠词本身没有显露出性属标志时（如 ein 是阳性还是中性？分不清！）：\n"
                           "  【形容词必须挺身而出，带上标志性词尾】：\n"
                           "  - 一格阳性：ein alt-er Mann (显示 der 的 -er 标志！)\n"
                           "  - 一格中性：ein klein-es Kind (显示 das 的 -es 标志！)\n"
                           "  - 四格中性：ein neu-es Auto (同样保持 -es 标志！)\n\n"
                           "• 一旦冠词已经显示了格位（如 einen, einem, einer, eines）：\n"
                           "  形容词功成身退，全部统一弱化为 -en！"
            },
            {
                "heading": "三、服饰搭配与外貌描写经典例句",
                "content": "• 外貌与衣着描写：\n"
                           "  - Er trägt einen blauen Anzug [Akk.m -en] und ein weißes Hemd [Akk.n -es].\n"
                           "  - Sie ist eine hübsche Frau [Nom.f -e] mit langen blonden Haaren.\n"
                           "  - Mein neuer Kollege [Nom.m -er] ist sehr hilfsbereit."
            },
            {
                "heading": "四、高频易错：复数前用 keine / meine (不定冠词无复数！)",
                "content": "不定冠词 ein 没有复数形式！复数时：\n"
                           "• 如果带否定或物主代词：keine neuen Schuhe / meine neuen Schuhe (-en 词尾！)\n"
                           "• 如果是零冠词（无冠词复数）：则进入 Typ III 强变化 (neue Schuhe)！"
            },
            {
                "heading": "五、混合变化极速通关口诀",
                "content": "【混合变化记忆歌】：\n"
                           "混合变化看 ein 词，阳 -er 中 -es 显英姿；\n"
                           "阴性照常挂个 -e，一格四格莫迟疑；\n"
                           "只要冠词尾巴变，形容词全加 -en 齐！"
            }
        ]
    },
    "A2_L11": {
        "title": "关系从句基础 (Relativsätze im Nominativ und Akkusativ)",
        "sections": [
            {
                "heading": "一、关系从句的功能与引导词",
                "content": "关系从句紧跟在名词（先行词 Bezugswort）后面，充当详细修饰的定语，由关系代词引导：\n\n"
                           "【关系代词在 Nom. 与 Akk. 的形式】：\n"
                           "┌────────────┬──────────┬──────────┬──────────┬──────────┐\n"
                           "│ 格位       │ 阳性 (m.)│ 阴性 (f.)│ 中性 (n.)│ 复数 (Pl)│\n"
                           "├────────────┼──────────┼──────────┼──────────┼──────────┤\n"
                           "│ Nom. (一格)│ der      │ die      │ das      │ die      │\n"
                           "│ Akk. (四格)│ den      │ die      │ das      │ die      │\n"
                           "└────────────┴──────────┴──────────┴──────────┴──────────┘\n\n"
                           "关系代词的形态与定冠词完全一模一样！"
            },
            {
                "heading": "二、关系代词“性数从先行词，格看从句角色”铁律",
                "content": "1. 【性与数 (Genus & Numerus)】：由被修饰的先行词决定！\n"
                           "2. 【格位 (Kasus)】：由关系代词在【从句中扮演的成分】决定！\n\n"
                           "• 关系代词作主语 (Nominativ)：\n"
                           "  - Das ist der Mann, der [作从句主语] hier wohnt.\n"
                           "  - Kennst du die Frau, die [作从句主语] dort singt?\n\n"
                           "• 关系代词作直接宾语 (Akkusativ)：\n"
                           "  - Das ist der Film, den [作从句宾语] ich gestern gesehen habe.\n"
                           "  - Das Buch, das [作从句宾语] du mir geschenkt hast, ist spannend."
            },
            {
                "heading": "三、从句框形与逗号位置规则",
                "content": "• 关系从句必须由【逗号】与主句隔开；\n"
                           "• 关系从句的变位动词【必须置于从句句末】！\n"
                           "• 插入式关系从句（从句插入主句中间）：\n"
                           "  Der Mann, den du dort siehst, ist mein Deutschlehrer.\n"
                           "  (先行词紧贴关系代词，关系从句结束后再打一个逗号，主句动词继续！)"
            },
            {
                "heading": "四、文化艺术与展品赏析实用例句",
                "content": "• 博物馆展品介绍：\n"
                           "  - Dieses Gemälde, das im 19. Jahrhundert gemalt wurde, ist weltberühmt.\n"
                           "  - Die Künstler, die an dieser Ausstellung teilnehmen, kommen aus ganz Europa."
            },
            {
                "heading": "五、关系从句速记口诀",
                "content": "【关系代词选词诀】：\n"
                           "先行词定性和数，从句角色定其格；\n"
                           "逗号隔开莫遗漏，动词押到从句末；\n"
                           "阳性四格换成 den，句式高级上档次！"
            }
        ]
    },
    "A2_L12": {
        "title": "情态动词 sollte 提出建议与时间介词",
        "sections": [
            {
                "heading": "一、sollte (应当/最好) 的语义特征与变位",
                "content": "sollte 是 sollen 的第二虚拟式，用于提出【委婉建议、忠告与环保倡议】，语气比直陈式 sollen 和 müssen 亲切得多：\n\n"
                           "• 变位形式：\n"
                           "  - ich sollte\n"
                           "  - du solltest\n"
                           "  - er/sie/es sollte\n"
                           "  - wir sollten\n"
                           "  - ihr solltet\n"
                           "  - sie/Sie sollten\n\n"
                           "• 经典例句：\n"
                           "  - Du solltest mehr Obst und Gemüse essen. (你应当多吃水果蔬菜。)\n"
                           "  - Wir sollten weniger Plastik verbrauchen. (我们应该少用塑料。)"
            },
            {
                "heading": "二、表示时间跨度与先后的介词全解析",
                "content": "┌──────────────┬──────────┬──────────────┬────────────────────────┐\n"
                           "│ 介词         │ 搭配格位 │ 语义含义     │ 经典示范例句           │\n"
                           "├──────────────┼──────────┼──────────────┼────────────────────────┤\n"
                           "│ vor          │ + Dativ  │ 在...之前    │ Vor dem Essen waschen wir die Hände.│\n"
                           "│ nach         │ + Dativ  │ 在...之后    │ Nach der Arbeit gehe ich zum Sport.│\n"
                           "│ seit         │ + Dativ  │ 自从...以来  │ Er wohnt seit einem Jahr in Berlin.│\n"
                           "│ in           │ + Dativ  │ 在...之后(将来)│ Der Zug fährt in fünf Minuten ab.│\n"
                           "│ für          │ + Akkusativ│ 持续...之久│ Ich bleibe für zwei Wochen hier.│\n"
                           "│ während      │ + Genitiv│ 在...期间    │ Während der Ferien reisen wir viel.│\n"
                           "└──────────────┴──────────┴──────────────┴────────────────────────┘"
            },
            {
                "heading": "三、环境保护与垃圾分类实用倡议表达",
                "content": "• 环保日常行动建议：\n"
                           "  - Man sollte das Licht ausschalten, wenn man den Raum verlässt.\n"
                           "  - Man sollte Müll trennen: Biomüll, Papiermüll und Plastikmüll gehören in verschiedene Tonnen."
            },
            {
                "heading": "四、建议句式家族对比矩阵",
                "content": "• 强硬命令：Trenn den Müll! (祈使句，对下级或孩子)\n"
                           "• 客观要求：Du musst den Müll trennen. (法律/硬性规定)\n"
                           "• 友好建议：Du solltest den Müll trennen. (劝导、社交首选)"
            },
            {
                "heading": "五、sollte 与时间介词速记诀",
                "content": "【时间介词与建议歌】：\n"
                           "提出建议用 sollte，体贴得体人人夸；\n"
                           "vor 前 nach 后 seit 过去，三格介词常相随；\n"
                           "将来过后 in 加三，持续时长 für 四格管！"
            }
        ]
    },
    "A2_L13": {
        "title": "双宾语语序规则 (Dativ- und Akkusativobjekt)",
        "sections": [
            {
                "heading": "一、双宾语动词的基本概念",
                "content": "德语中许多动词（如 geben, schenken, zeigen, schicken, erklären, leihen）可以同时带两个宾语：\n"
                           "• 一个是动作的直接承受物（第四格 Akkusativ）；\n"
                           "• 一个是动作的间接受益人（第三格 Dativ）。"
            },
            {
                "heading": "二、语序铁律：名词形态 vs 代词形态",
                "content": "当双宾语在句中出现时，其相对次序严格遵循以下两条定律：\n\n"
                           "1. 【当两个宾语都是名词时】：【人 (Dativ) 先于 物 (Akkusativ)】！\n"
                           "   • 公式：动词 + [名词三格] + [名词四格]\n"
                           "   - Ich schenke [meinem Freund: Dat.] [ein Buch: Akk.].\n"
                           "   - Der Lehrer erklärt [den Schülern: Dat.] [die Grammatik: Akk.].\n\n"
                           "2. 【当出现人称代词时】：【代词永远抢占最前排】！\n"
                           "   • 若两个都是代词：【四格代词 (Akk.) 必须先于 三格代词 (Dat.)】！\n"
                           "   - Ich schenke es [Akk.] ihm [Dat.]. (我把它送给他。)\n"
                           "   - Er gibt sie [Akk.] mir [Dat.]. (他把它们给我。)\n\n"
                           "3. 【一个代词一个名词时】：代词排在名词前面！\n"
                           "   - Ich schenke es [Akk.代词] meinem Freund [Dat.名词].\n"
                           "   - Ich gebe ihm [Dat.代词] das Buch [Akk.名词]."
            },
            {
                "heading": "三、双宾语语序速查对照表",
                "content": "┌──────────────────┬──────────────────────────┬────────────────────────┐\n"
                           "│ 宾语组合情况     │ 正确语序规则             │ 经典示范例句           │\n"
                           "├──────────────────┼──────────────────────────┼────────────────────────┤\n"
                           "│ 名词 + 名词      │ Dat.先，Akk.后 (人先物后) │ Ich gebe der Frau den Schlüssel.│\n"
                           "│ 代词 + 代词      │ Akk.先，Dat.后 (它先他后) │ Ich gebe ihn ihr.      │\n"
                           "│ 代词 + 名词      │ 代词在前，名词在后       │ Ich gebe ihn der Frau. │\n"
                           "│ 名词 + 代词      │ 代词在前，名词在后       │ Ich gebe ihr den Schlüssel.│\n"
                           "└──────────────────┴──────────────────────────┴────────────────────────┘"
            },
            {
                "heading": "四、高频实战场景：赠礼与办公交接",
                "content": "• 赠送礼物：\n"
                           "  - Hast du deiner Schwester das Geburtstagsgeschenk schon gegeben?\n"
                           "  - Ja, ich habe es ihr gestern Abend überreicht.\n"
                           "• 办公文件传递：\n"
                           "  - Könnten Sie mir die Unterlagen bitte bis 14 Uhr zuschicken?"
            },
            {
                "heading": "五、双宾语语序速记口诀",
                "content": "【双宾语极简通关诀】：\n"
                           "两名相遇人先物 (三格在前四格后)；\n"
                           "两代相争物先人 (四格代词三格前)；\n"
                           "名代相争代为王，谁是代词谁领衔！"
            }
        ]
    },
    "A2_L14": {
        "title": "第二虚拟式表达非现实愿望 (Irreale Wünsche)",
        "sections": [
            {
                "heading": "一、非现实愿望句的语法本质与句型结构",
                "content": "非现实愿望句表达与当前客观现实相反的美好期盼或懊悔：\n\n"
                           "1. 【带连词 wenn 的句型】（动词置于从句句末）：\n"
                           "   • Wenn ich doch mehr Zeit hätte! (要是我有更多时间该多好啊！)\n"
                           "   • Wenn das Wetter nur schön wäre! (要是天气好就好了！)\n\n"
                           "2. 【无连词的倒装句型】（变位动词提到第 1 位！）：\n"
                           "   • Hätte ich doch bloß mehr Geld! (要是我有更多钱该多好啊！)\n"
                           "   • Wäre ich doch nur im Urlaub! (要是我现在正在度假该多好！)"
            },
            {
                "heading": "二、强烈的语气小品词 (Modalpartikeln)：doch, nur, bloß",
                "content": "在非现实愿望句中，doch, nur, bloß 几乎不可或缺，它们能够激发出强烈的感叹与渴望色彩：\n\n"
                           "• doch nur: Wenn ich doch nur fliegen könnte!\n"
                           "• doch bloß: Hätte ich doch bloß gestern gelernt!\n"
                           "句末必须打上感叹号 (!)。"
            },
            {
                "heading": "三、社交礼仪与节日祝福客气表达",
                "content": "• 节日与受邀客气回应：\n"
                           "  - Ich würde mich sehr freuen, Sie bei unserer Feier zu sehen.\n"
                           "  - Wir würden gern kommen, aber wir haben leider schon einen anderen Termin.\n"
                           "• 委婉提议：\n"
                           "  - Es wäre schön, wenn wir uns bald wieder treffen würden."
            },
            {
                "heading": "四、歌德 A2 口试 Teil 3 共同计划协调黄金句型",
                "content": "口试第三部分要求与搭档共同商量一个计划，第二虚拟式是斩获高分的利器：\n\n"
                           "• 提议：Was meinst du, wäre es besser, wenn wir am Samstag fahren würden?\n"
                           "• 赞同：Das wäre eine hervorragende Idee!\n"
                           "• 异议与替代方案：Ich würde lieber am Sonntag fahren, weil ich am Samstag arbeiten muss."
            },
            {
                "heading": "五、非现实愿望句速记口诀",
                "content": "【愿望句速记歌】：\n"
                           "非现实愿望抒心声，wäre, hätte, könnte 领；\n"
                           "wenn 句动词沉在底，无连动词首位顶；\n"
                           "doch 和 bloß 助感情，感叹号打在最末评！"
            }
        ]
    },
    "A2_L15": {
        "title": "歌德 A2 综合应试冲刺与高分通关法则",
        "sections": [
            {
                "heading": "一、歌德 A2 (Goethe-Zertifikat A2) 题型与评分标准",
                "content": "歌德 A2 总分 100 分，60 分及格。四大单项各占 25 分：\n\n"
                           "1. 【阅读 (Lesen)】：30 分钟，4 个部分共 20 题 (报刊短讯、网页信息筛选、官方通知、活动安排匹配)\n"
                           "2. 【听力 (Hören)】：约 30 分钟，4 个部分共 20 题 (日常广播通知、电话留言、深度对话、采访选择)\n"
                           "3. 【写作 (Schreiben)】：30 分钟，两大任务：\n"
                           "   - Teil 1: 个人短消息/便条 (约 20-30 词)\n"
                           "   - Teil 2: 正式/半正式邮件或书信 (约 30-40 词)\n"
                           "4. 【口语 (Sprechen)】：约 15 分钟，双人考试：\n"
                           "   - Teil 1: 抽卡就日常生活提问并回答 (4张卡)\n"
                           "   - Teil 2: 根据给定的主题卡讲述自己的一段经历/观点\n"
                           "   - Teil 3: 与搭档就一个共同任务进行协商并做出决定"
            },
            {
                "heading": "二、写作 Teil 2 满分书信高能结构模板",
                "content": "【题目情景：向语言班请假并补交作业】\n\n"
                           "Sehr geehrte Frau Braun, (称呼后逗号)\n"
                           "ich schreibe Ihnen, weil ich morgen leider nicht zum Unterricht kommen kann. (首句小写，weil 复合句)\n"
                           "Mein Sohn ist krank geworden und ich muss mit ihm zum Arzt gehen. (情态动词)\n"
                           "Könnten Sie mir bitte die Hausaufgaben per E-Mail schicken? (第二虚拟式客气请求)\n"
                           "Ich werde den verpassten Stoff am Wochenende selbstständig nachholen. (将来时表达承诺)\n"
                           "Vielen Dank für Ihr Verständnis.\n"
                           "Mit freundlichen Grüßen (无逗号！)\n"
                           "Lin Wang"
            },
            {
                "heading": "三、口语 Teil 2 & Teil 3 核心应答模板",
                "content": "• Teil 2 叙述个人经历：\n"
                           "  - Das Thema ist 'Mein schönster Urlaub'. Ich war letztes Jahr in Österreich. Das Wetter war herrlich und wir sind viel gewandert. Für mich war das ein unvergessliches Erlebnis.\n\n"
                           "• Teil 3 协商讨论推进万能句：\n"
                           "  - Wollen wir am Wochenende zusammen ein Picknick machen?\n"
                           "  - Gute Idee! Wann treffen wir uns?\n"
                           "  - Wie wäre es mit Samstag um 10 Uhr?\n"
                           "  - Passt mir super! Ich bringe Obst und Getränke mit."
            },
            {
                "heading": "四、A2 级别极高频语法陷阱自查清单",
                "content": "1. 过去时 als 与 wenn 选错。\n"
                           "2. 静三动四双向介词后格位判断颠倒。\n"
                           "3. 定冠词后形容词误用强变化词尾（正确是 -e 或 -en）。\n"
                           "4. dass 和 weil 从句动词忘记置于句末。\n"
                           "5. 被动语态 werden 变位与分词位置颠倒。\n"
                           "6. 比较级中误用 wie 代替 als (正确：größer als)。\n"
                           "7. 关系代词性数格一致性混乱。\n"
                           "8. 双宾语人称代词语序错误。"
            },
            {
                "heading": "五、A2 考前 24 小时通关速记口诀",
                "content": "【A2 通关口诀】：\n"
                           "weil 和 dass 动词甩句末，als 讲过去单次经历刻；\n"
                           "静三动四看状态，比较级后用 als 爱；\n"
                           "定冠形容 -e 与 -en，混合变化 ein 显身；\n"
                           "第二虚拟语气好，拿下 A2 乐陶陶！"
            }
        ]
    }
}
