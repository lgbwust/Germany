#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enriched Grammar Content for Level B2 (Lessons 1-15):
Nominalstil vs. Verbalstil, Erweiterte Partizipialattribute, High-level Konjunktiv II,
Passiversatzformen, Gehobene Genitiv-Präpositionen, Konjunktiv I in Science & Journalism,
Erweiterte Relativsätze (wer/was/dessen/deren), Zweiteilige Konnektoren,
Satzverbindungen & Adverbiale Angaben, Zustandspassiv vs Vorgangspassiv,
Subjektive Modalverben (Epistemische Modalität), Beinahe-Sätze & Irreale Hypothesen,
Textkohärenz & Adverbiale Konnektoren, Gehobene Funktionsverbgefüge,
and TestDaF / Goethe B2 Academic Writing & Graph Description Guide.
"""

B2_GRAMMAR = {
    "B2_L01": {
        "title": "名词化风格与学术表达 (Nominalstil vs. Verbalstil)",
        "sections": [
            {
                "heading": "一、名词化风格 (Nominalstil) 的学术本质与功能",
                "content": "德语学术论文 (Wissenschaftssprache)、科研报告与政经公文中，核心语法特征是广泛采用【名词化风格 (Nominalstil)】替代日常口语的从句风格 (Verbalstil)。\n\n"
                           "• 特征对比：\n"
                           "  - 动词从句风格 (Verbalstil)：结构松散，从句嵌套，偏口语化。\n"
                           "    Weil die Temperaturen der Weltmeere kontinuierlich ansteigen, schmelzen die Polkappen immer schneller.\n"
                           "  - 名词化风格 (Nominalstil)：高度凝练，信息密度极大，客观严谨。\n"
                           "    Aufgrund des kontinuierlichen Anstiegs der Meerestemperaturen schmelzen die Polkappen immer schneller."
            },
            {
                "heading": "二、从句转化为介词名词短语的转换矩阵",
                "content": "┌──────────────────┬──────────────────────────┬────────────────────────┐\n"
                           "│ 逻辑关系从句     │ 对应学术介词             │ 名词化结构示范         │\n"
                           "├──────────────────┼──────────────────────────┼────────────────────────┤\n"
                           "│ 原因 (weil / da) │ wegen / aufgrund /       │ aufgrund des schnellen │\n"
                           "│                  │ infolge (+ Gen.)         │ Wachstums              │\n"
                           "├──────────────────┼──────────────────────────┼────────────────────────┤\n"
                           "│ 条件 (wenn/falls)│ bei (+ Dat.) /           │ bei steigenden Zinsen  │\n"
                           "│                  │ im Falle (+ Gen.)        │                        │\n"
                           "├──────────────────┼──────────────────────────┼────────────────────────┤\n"
                           "│ 让步 (obwohl)    │ trotz / ungeachtet       │ trotz aller Bemühungen │\n"
                           "│                  │ (+ Gen.)                 │                        │\n"
                           "├──────────────────┼──────────────────────────┼────────────────────────┤\n"
                           "│ 时间 (nachdem)   │ nach (+ Dat.)            │ nach Abschluss der     │\n"
                           "│                  │                          │ Untersuchung           │\n"
                           "├──────────────────┼──────────────────────────┼────────────────────────┤\n"
                           "│ 时间 (während)   │ während (+ Gen.)         │ während des Experiments│\n"
                           "├──────────────────┼──────────────────────────┼────────────────────────┤\n"
                           "│ 目的 (damit)     │ zu / zwecks (+ Gen.)     │ zwecks Optimierung     │\n"
                           "└──────────────────┴──────────────────────────┴────────────────────────┘"
            },
            {
                "heading": "三、核心动词名词化派生后缀规律",
                "content": "• -ung (极高频阴性): untersuchen -> die Untersuchung, erforschen -> die Erforschung, ansteigen -> der Anstieg (无后缀阳性)\n"
                           "• -tion / -sion (外来学术动词): definieren -> die Definition, analysieren -> die Analyse\n"
                           "• -ment (中性): entwickeln -> die Entwicklung, experimentieren -> das Experiment\n"
                           "• 动名词原形 (大写中性 das): prüfen -> das Prüfen, messen -> das Messen"
            },
            {
                "heading": "四、学术论文引言与方法论深度实战",
                "content": "• 科研论文标准句式：\n"
                           "  - Verbalstil: Nachdem die Forscher die Daten ausgewertet hatten, veröffentlichten sie die Ergebnisse.\n"
                           "  -> Nominalstil: Nach der Auswertung der empirischen Daten durch das Forschungsteam erfolgte die Publikation der wegweisenden Forschungsergebnisse.\n"
                           "  - Zur Überprüfung der Hypothese wurden dreißig Probanden einer MRT-Untersuchung unterzogen."
            },
            {
                "heading": "五、德福 B2 名词化通关秘籍",
                "content": "【名词化转换口诀】：\n"
                           "学术高雅名词化，从句动词变名家；\n"
                           "介词引领第二格，状语缩入名词下；\n"
                           "Verbalstil 降档次，Nominalstil 德福夸！"
            }
        ]
    },
    "B2_L02": {
        "title": "扩展分词定语 (Erweiterte Partizipialattribute) 的解构与应用",
        "sections": [
            {
                "heading": "一、扩展分词定语的句法构造原理",
                "content": "扩展分词定语是德语高阶书面语最鲜明的标志，它是将一个完整的定语从句，压缩嵌入在【冠词与中心名词之间】的长定语结构：\n\n"
                           "• 结构骨架公式：\n"
                           "  【定冠词/不定冠词】 + [各种状语、补足语 + 分词 Partizip I/II (带词尾)] + 【中心名词】\n\n"
                           "• 经典示范：\n"
                           "  - die [gestern von der Bundesregierung verabschiedeten] Reformen\n"
                           "    (= die Reformen, die gestern von der Bundesregierung verabschiedet wurden)\n"
                           "  - der [seit Jahren in führenden Technologiekonzernen tätige] Ingenieur\n"
                           "    (= der Ingenieur, der seit Jahren in führenden Technologiekonzernen tätig ist)"
            },
            {
                "heading": "二、长难句破解：四步解构还原法定律",
                "content": "在阅读德福科技文章或高端商务合同时，遇到超过两行的扩展分词定语，使用四步拆解：\n\n"
                           "1. 【圈出两端】：先圈出前面的冠词 (die/der/das) 和它后面对应的中心名词；\n"
                           "2. 【找到分词】：紧贴在中心名词正前方带有形容词词尾的单词，就是分词核心；\n"
                           "3. 【判断类型】：\n"
                           "   - 若是 Partizip I (-end): 还原为主动态进行从句；\n"
                           "   - 若是 Partizip II (-t / -en): 还原为被动态已完成从句；\n"
                           "4. 【剥离修饰成分】：将冠词与分词中间夹带的时间、地点、方式状语全部还原进关系从句。"
            },
            {
                "heading": "三、带有 zu 的第一分词 (Gerundiv / 动名词定语)",
                "content": "当【zu + 第一分词】放在名词前作定语时，表示【必须被做 / 能够被做】的强制或可能含义：\n\n"
                           "• 结构：冠词 + [zu + Partizip I + 词尾] + 名词\n"
                           "  - die zu lösende Aufgabe = die Aufgabe, die gelöst werden muss/kann\n"
                           "  - das einzuhaltende Gesetz = das Gesetz, das eingehalten werden muss\n"
                           "  - die nicht zu unterschätzende Gefahr = die Gefahr, die nicht unterschätzt werden darf"
            },
            {
                "heading": "四、跨国商务并购与高端合同实战解析",
                "content": "• 商业合同条款：\n"
                           "  - Die [im Rahmen der Due-Diligence-Prüfung von den Wirtschaftsprüfern festgestellten] finanziellen Risiken müssen vor der Vertragsunterzeichnung umfassend minimiert werden.\n"
                           "  - Alle [aus dieser Vereinbarung resultierenden] Streitigkeiten unterliegen dem deutschen Handelsrecht."
            },
            {
                "heading": "五、扩展分词定语速查口诀",
                "content": "【长定语破解歌诀】：\n"
                           "冠词名词夹两头，中间长状如洪流；\n"
                           "名词之前寻分词，一分主动二分被；\n"
                           "zu 嵌一分表必须，还原从句破重围！"
            }
        ]
    },
    "B2_L03": {
        "title": "第二虚拟式高阶应用 (Spekulation, Diplomatie & Irreale Vergleiche)",
        "sections": [
            {
                "heading": "一、第二虚拟式在外交辞令与商务谈判中的妥协功能",
                "content": "在 B2 商务谈判与学术辩论中，第二虚拟式不仅用于礼貌，更用于【外交辞令 (Diplomatische Zurückhaltung)】与【非确定性推测】：\n\n"
                           "• 表达委婉保留意见与异议：\n"
                           "  - Ich würde vorschlagen, dass wir diesen Punkt nochmals überdenken.\n"
                           "  - Es wäre verfrüht, jetzt schon von einem endgültigen Scheitern der Gespräche zu sprechen.\n"
                           "  - Wir würden es begrüßen, wenn Sie uns preislich etwas entgegenkämen."
            },
            {
                "heading": "二、非现实比较从句：als ob / als wenn (仿佛/宛如)",
                "content": "als ob / als wenn 引导从句，表达主观感受与事实不符的虚假表象：\n\n"
                           "1. 【带连词 als ob / als wenn】（从句框形语序，动词置句末）：\n"
                           "   - Er tut so, als ob er von dem Betrug nichts gewusst hätte.\n"
                           "   - Der Markt reagiert so nervös, als ob eine schwere Rezession unmittelbar bevorstünde.\n\n"
                           "2. 【省略 ob 的倒装形式 als】（【变位动词紧贴 als 之后，居第 1 位】！）：\n"
                           "   - Er tut so, als hätte er von dem Betrug nichts gewusst.\n"
                           "   - Es scheint, als wäre das System vollständig kollabiert."
            },
            {
                "heading": "三、宏观经济学与金融市场推测",
                "content": "• 经济学预测与假定：\n"
                           "  - Würde die Europäische Zentralbank die Leitzinsen noch weiter anheben, so könnte dies die Konjunktur im Euroraum empfindlich dämpfen.\n"
                           "  - Ohne die staatlichen Rettungspakete wären zahlreiche Großbanken in die Insolvenz geschlittert."
            },
            {
                "heading": "四、第二虚拟式强变化动词独立形式精讲",
                "content": "在 B2 高阶德语中，尽量避免滥用 würde + Infinitiv，而应掌握常用动词的原生虚拟式：\n\n"
                           "• käme (kommen), ginge (gehen), fände (finden), wüsste (wissen), bliebe (bleiben), böte (bieten), gäbe (es gäbe)\n"
                           "  - Wenn es eine praktikable Alternative gäbe, bliebe uns dieser harte Schritt erspart."
            },
            {
                "heading": "五、高阶第二虚拟式速记口诀",
                "content": "【外交虚拟高阶诀】：\n"
                           "谈判磋商需克制，第二虚拟显睿智；\n"
                           "als ob 句末动词沉，单用 als 动词首位迎；\n"
                           "gäbe, bliebe, käme 现，学术德味立显真！"
            }
        ]
    },
    "B2_L04": {
        "title": "被动态替代形式全景体系 (Passiversatzformen mit Modalbedeutung)",
        "sections": [
            {
                "heading": "一、四大核心被动替代结构全景矩阵",
                "content": "德语书面语中为了避免 werden 频繁重复出现的单调感，构建了完整的替代系统：\n\n"
                           "┌──────────────────────┬────────────────────────┬────────────────────────────────────────────┐\n"
                           "│ 替代结构             │ 语法情态内涵           │ 典型示范句                                 │\n"
                           "├──────────────────────┼────────────────────────┼────────────────────────────────────────────┤\n"
                           "│ 1. sein + zu + Inf.  │ müssen / können        │ Der Vertrag ist unverzüglich zu ratifizieren.│\n"
                           "│                      │ (必须/能够被做)        │ (= muss ratifiziert werden)                │\n"
                           "├──────────────────────┼────────────────────────┼────────────────────────────────────────────┤\n"
                           "│ 2. sich lassen + Inf.│ können                 │ Diese Hypothese lässt sich empirisch belegen.│\n"
                           "│                      │ (可以/能够被做)        │ (= kann empirisch belegt werden)           │\n"
                           "├──────────────────────┼────────────────────────┼────────────────────────────────────────────┤\n"
                           "│ 3. 形容词 -bar/-lich │ können                 │ Die Schäden sind irreparabel / unersetzbar. │\n"
                           "│                      │ (具备被...的可能性)    │ (= können nicht repariert werden)          │\n"
                           "├──────────────────────┼────────────────────────┼────────────────────────────────────────────┤\n"
                           "│ 4. es gilt /         │ müssen                 │ Es gilt, die Ursachen zu analysieren.      │\n"
                           "│    es bleibt + zu    │ (必须被做 / 尚待被做)  │ (= Die Ursachen müssen analysiert werden)  │\n"
                           "└──────────────────────┴────────────────────────┴────────────────────────────────────────────┘"
            },
            {
                "heading": "二、法律德语契约与条款中的被动替代",
                "content": "• 司法与民法公文高频表达：\n"
                           "  - Das Urteil ist innerhalb einer Frist von zwei Wochen anzufechten.\n"
                           "    (= Das Urteil kann/muss angefochten werden.)\n"
                           "  - Es bleibt abzuwarten, wie das Bundesverfassungsgericht über die Klage entscheiden wird.\n"
                           "  - Der Mangel lässt sich auf einen Fabrikationsfehler zurückführen."
            },
            {
                "heading": "三、主动被动转换考题互换公式",
                "content": "• 考题句：Man kann die Software problemlos auf jedem Betriebssystem installieren.\n"
                           "  - 替换 1 (Passiv): Die Software kann problemlos installiert werden.\n"
                           "  - 替换 2 (sein + zu): Die Software ist problemlos zu installieren.\n"
                           "  - 替换 3 (sich lassen): Die Software lässt sich problemlos installieren.\n"
                           "  - 替换 4 (-bar): Die Software ist auf jedem System installierbar."
            },
            {
                "heading": "四、学术论文中表达客观研究前景",
                "content": "• 实验前景与讨论：\n"
                           "  - Es gilt nun, diese theoretischen Erkenntnisse in die industrielle Praxis zu überführen.\n"
                           "  - Eine endgültige Schlussfolgerung lässt sich zum gegenwärtigen Zeitpunkt noch nicht ziehen."
            },
            {
                "heading": "五、被动替代体系速记口诀",
                "content": "【被动替代四大法宝】：\n"
                           "sein + zu, sich lassen 巧，-bar 后缀法度高；\n"
                           "es gilt zu 表示必须做，es bleibt zu 尚待见分晓；\n"
                           "被动替换文章活，德福阅读秒破题！"
            }
        ]
    },
    "B2_L05": {
        "title": "第二格高阶介词体系 (Gehobene Genitiv-Präpositionen)",
        "sections": [
            {
                "heading": "一、高端第二格介词分类全览",
                "content": "在 B2/C1 社科文献与政经公文中，以下第二格介词出现极其频繁：\n\n"
                           "1. 【依据与关联】：\n"
                           "   • bezüglich (+ Gen.): 关于/鉴于 (Bezüglich Ihrer Anfrage teilen wir Folgendes mit.)\n"
                           "   • hinsichtlich (+ Gen.): 在...方面/鉴于 (Hinsichtlich der Effizienz gibt es noch Bedenken.)\n"
                           "   • anlässlich (+ Gen.): 值此...之际 (Anlässlich des 100-jährigen Firmenjubiläums...)\n"
                           "   • laut (+ Gen./Dat.): 依据/按照 (Laut des neuesten Berichts...)\n\n"
                           "2. 【因果与缺乏】：\n"
                           "   • infolge (+ Gen.): 由于...导致的结果 (Infolge des Erdbebens fielen Stromnetze aus.)\n"
                           "   • mangels (+ Gen.): 因缺乏... (Mangels hinreichender Beweise wurde er freigesprochen.)\n"
                           "   • kraft (+ Gen.): 凭借/依据法律效力 (Kraft meines Amtes erkläre ich...)\n\n"
                           "3. 【立场与利益】：\n"
                           "   • zugunsten (+ Gen.): 有利于/为了...的利益 (zugunsten der Arbeitnehmer)\n"
                           "   • zuungunsten (+ Gen.): 不利于 (zuungunsten der Umwelt)\n"
                           "   • seitens (+ Gen.): 出自...方面 (seitens der Gewerkschaften)"
            },
            {
                "heading": "二、介词后置与双向格位特殊规则 (gemäß & zufolge)",
                "content": "• 【zufolge】：\n"
                           "  - 若【前置】，支配第二格：Zufolge des internen Berichts ...\n"
                           "  - 若【后置】，强制支配第三格：Dem internen Bericht zufolge ... (极其高频！)\n\n"
                           "• 【gemäß】：\n"
                           "  - 前置或后置均支配第三格：Gemäß dem Gesetz / dem Gesetz gemäß"
            },
            {
                "heading": "三、生命伦理学与基因工程法律报告实战",
                "content": "• 伦理委员会审查报告：\n"
                           "  - Hinsichtlich der Risiken der CRISPR-Cas9-Gentechnik fordern Ethiker strenge Regulierungen.\n"
                           "  - Mangels international einheitlicher Standards droht eine unkontrollierte genetische Modifikation von Embryonen.\n"
                           "  - Die Entscheidung fiel zugunsten eines strikten Verbots von Klonexperimenten am Menschen aus."
            },
            {
                "heading": "四、论文中引用来源与交代论据的高阶句式",
                "content": "• 交代论据来源：\n"
                           "  - Aktuellen statistischen Erhebungen zufolge [后置+Dat.] stagniert die Wirtschaftsleistung im zweiten Halbjahr.\n"
                           "  - Seitens der Regierung wurden umfassende Hilfsmaßnahmen in Aussicht gestellt."
            },
            {
                "heading": "五、高端介词速记口诀",
                "content": "【高端二格介词歌】：\n"
                           "bezüglich 关于，hinsichtlich 视，anlässlich 庆典际；\n"
                           "infolge 恶果，mangels 缺，zugunsten 偏向你；\n"
                           "zufolge 后置变三格，严谨公文自成诗！"
            }
        ]
    },
    "B2_L06": {
        "title": "第一虚拟式深度进阶与学术客观转述 (Konjunktiv I in Wissenschaft & Medien)",
        "sections": [
            {
                "heading": "一、第一虚拟式各时态完整生成规则",
                "content": "在严肃学术论文中，引述他人文献研究结果时，必须使用第一虚拟式以表明客观中立立场：\n\n"
                           "┌────────────┬────────────────────────────┬────────────────────────────┐\n"
                           "│ 时态       │ 构成法则                   │ 经典示范句                 │\n"
                           "├────────────┼────────────────────────────┼────────────────────────────┤\n"
                           "│ 现在时     │ 动词词干 + 虚拟式词尾      │ Der Autor betone, das Modell│\n"
                           "│ (Präsens)  │ (er habe / er gehe)        │ sei universell anwendbar.  │\n"
                           "├────────────┼────────────────────────────┼────────────────────────────┤\n"
                           "│ 完成时     │ sei / habe (Konj.I) +      │ Der Experte erklärt, die   │\n"
                           "│ (Perfekt)  │ Partizip II (过去统领)     │ Daten seien manipuliert worden.│\n"
                           "├────────────┼────────────────────────────┼────────────────────────────┤\n"
                           "│ 将来时     │ werde (Konj.I) +           │ Das Institut prognostiziert,│\n"
                           "│ (Futur)    │ Infinitiv                  │ die Inflation werde sinken. │\n"
                           "├────────────┼────────────────────────────┼────────────────────────────┤\n"
                           "│ 被动态     │ werde (Konj.I) +           │ Der Sprecher teilte mit,   │\n"
                           "│ (Passiv)   │ Partizip II                │ das Werk werde geschlossen.│\n"
                           "└────────────┴────────────────────────────┴────────────────────────────┘"
            },
            {
                "heading": "二、学术转述动词 (Verba dicendi) 精准语义梯度表",
                "content": "引用不同学者观点时，选用不同的学术动词传递作者的态度立场：\n\n"
                           "• 中立客观阐述：darlegen, erläutern, berichten, feststellen, ausführen\n"
                           "  - Professor Schmidt führt aus, die Resultate seien signifikant.\n"
                           "• 坚定主张/强调：betonen, hervorheben, unterstreichen, verfechten\n"
                           "  - Die Forschergruppe betont, es gebe keine Alternative zu dieser Therapie.\n"
                           "• 怀疑/无把握之主张：behaupten, mutmaßen, vermuten, vorgeben\n"
                           "  - Der Konzern behauptet, er habe von den Sicherheitslücken nichts gewusst.\n"
                           "• 驳斥/否定：bestreiten, widerlegen, in Abrede stellen"
            },
            {
                "heading": "三、跨句长篇学术观点的时态连续性",
                "content": "在论文正文中，当转述连续几句话时，不需要每句都写 'Er sagt, dass...'，而是连续使用第一虚拟式变位，读者自然明了这是引述内容：\n\n"
                           "• 示范：\n"
                           "  Nach Ansicht von Meyer sei die Transformation des Energiesektors unumgänglich. Der bisherige Ausbau der Netze reiche jedoch bei weitem nicht aus. Es bedürfe daher massiver privater und staatlicher Investitionen."
            },
            {
                "heading": "四、人工智能与数字伦理学术研讨引述",
                "content": "• 学术会议观点引述：\n"
                           "  - Die Ethikkommission warnt davor, autonome Waffensysteme einzusetzen. Solche Systeme seien nicht in der Lage, moralische Dilemmata völkerrechtskonform aufzulösen."
            },
            {
                "heading": "五、学术第一虚拟式速记口诀",
                "content": "【学术引述金字塔】：\n"
                           "转述文献用一虚，客观中立不树敌；\n"
                           "三单 sei habe werde 守，多句连用语意齐；\n"
                           "学术动词显态度，德福论述霸气提！"
            }
        ]
    },
    "B2_L07": {
        "title": "高级关系从句体系 (wer, was, dessen/deren & 关系副词)",
        "sections": [
            {
                "heading": "一、泛指代词引导的自由关系从句 (Wer ..., der ...)",
                "content": "不指向具体先行词，而是泛指‘凡是...的人’，由 wer 引导从句，主句用 der / den / dem 呼应：\n\n"
                           "• 主格呼应：Wer die Wissenschaft voranbringen will, [der] muss Geduld haben.\n"
                           "• 格位不对等法则：\n"
                           "  - Wer [从句 Nom.] nicht hören will, dem [主句 Dat.] muss man helfen.\n"
                           "  - Wen [从句 Akk.] das Schicksal trifft, der [主句 Nom.] braucht Beistand."
            },
            {
                "heading": "二、第二格关系代词 dessen (阳/中) 与 deren (阴/复)",
                "content": "关系从句表达先行词的从属关系（‘...的’），使用第二格关系代词：\n\n"
                           "┌──────────────┬──────────────┬──────────────────────────────────────────┐\n"
                           "│ 先行词性属   │ 二格关系代词 │ 示范例句                                 │\n"
                           "├──────────────┼──────────────┼──────────────────────────────────────────┤\n"
                           "│ 阳性 / 中性  │ dessen       │ Der Autor, dessen Buch weltweit ein      │\n"
                           "│ (m. / n.)    │ (他的/它的)  │ Bestseller wurde, hält heute einen Vortrag.│\n"
                           "├──────────────┼──────────────┼──────────────────────────────────────────┤\n"
                           "│ 阴性 / 复数  │ deren        │ Die Forscherin, deren Theorien umstritten│\n"
                           "│ (f. / Pl.)   │ (她的/他们的)│ sind, erhielt den Nobelpreis.            │\n"
                           "└────────────┴──────────────┴──────────────────────────────────────────┘\n\n"
                           "【核心铁律】：dessen 和 deren 后面修饰的名词【绝不能加任何冠词】！\n"
                           "• 正确：dessen Buch / deren Theorien\n"
                           "• 错误：*dessen das Buch / *deren die Theorien"
            },
            {
                "heading": "三、关系代词 was 与关系副词 (wo-, woran, worauf)",
                "content": "• 在最高级中性形容词化名词后，强制用 was：\n"
                           "  - Das ist das Schönste, was ich je erlebt habe.\n"
                           "  - Es gibt vieles, was noch erforscht werden muss.\n"
                           "• 关系副词替代介词关系代词：\n"
                           "  - Der Grund, weshalb / warum er gekündigt hat, ist unklar."
            },
            {
                "heading": "四、脑科学与人类心智前沿研究解析",
                "content": "• 神经生物学文本：\n"
                           "  - Patienten, deren Hippocampus operativ entfernt wurde, verloren die Fähigkeit zur Bildung neuer Langzeiterinnerungen.\n"
                           "  - Das Gehirn ist das komplexeste Organ, dessen Funktionsweise die Wissenschaft bis heute vor gewaltige Rätsel stellt."
            },
            {
                "heading": "五、高级关系从句速记口诀",
                "content": "【二格关系代词诀】：\n"
                           "阳中 dessen 阴复 deren，代词之后零冠圈；\n"
                           "凡是何人 wer 领头，主句指示呼应全；\n"
                           "最高级后 was 紧跟，句法严丝合缝连！"
            }
        ]
    },
    "B2_L08": {
        "title": "二重连词体系 (Zweiteilige Konnektoren in Argumentation)",
        "sections": [
            {
                "heading": "一、核心二重连词语义与句法结构全览",
                "content": "在 B2/TestDaF 议论文写作中，二重连词是组织高分对比论证的核心武器：\n\n"
                           "┌──────────────────────────────┬──────────────┬──────────────────────────────────────────┐\n"
                           "│ 二重连词                     │ 逻辑关系     │ 示范例句                                 │\n"
                           "├──────────────────────────────┼──────────────┼──────────────────────────────────────────┤\n"
                           "│ 1. je [Komparativ] ...       │ 正比递进关系 │ Je höher der Bildungsstand ist, desto    │\n"
                           "│    desto/umso [Komparativ]   │ (越...越...) │ geringer ist das Arbeitslosigkeitsrisiko.│\n"
                           "├──────────────────────────────┼──────────────┼──────────────────────────────────────────┤\n"
                           "│ 2. nicht nur ...,            │ 递进强调     │ Er spricht nicht nur fließend Deutsch,   │\n"
                           "│    sondern auch ...          │ (不仅...而且)│ sondern beherrscht auch Spanisch.        │\n"
                           "├──────────────────────────────┼──────────────┼──────────────────────────────────────────┤\n"
                           "│ 3. sowohl ... als auch ...   │ 并列肯定     │ Wir schätzen sowohl seine Fachkompetenz  │\n"
                           "│                              │ (既...又...) │ als auch seine Teamfähigkeit.            │\n"
                           "├──────────────────────────────┼──────────────┼──────────────────────────────────────────┤\n"
                           "│ 4. weder ... noch ...        │ 双重完全否定 │ Er hat weder die Zeit noch das Geld dazu.│\n"
                           "│                              │ (既不...也不)│ (注意：句子不用其他否定词 nicht/kein！)  │\n"
                           "├──────────────────────────────┼──────────────┼──────────────────────────────────────────┤\n"
                           "│ 5. zwar ..., aber ...        │ 让步转折     │ Das Projekt ist zwar teuer, aber effektiv.│\n"
                           "├──────────────────────────────┼──────────────┼──────────────────────────────────────────┤\n"
                           "│ 6. entweder ... oder ...     │ 排他二选一   │ Entweder wir handeln jetzt, oder die     │\n"
                           "│                              │ (要么...要么)│ Gelegenheit ist für immer verpasst.      │\n"
                           "└──────────────────────────────┴──────────────┴──────────────────────────────────────────┘"
            },
            {
                "heading": "二、je ... desto/umso 极高频必考语序法则",
                "content": "【无数考生栽跟头的语序杀手】：\n\n"
                           "• 前半句 (je-从句)：je + 【比较级】 + 主语 + ...... + 【变位动词置句末 (从句框形)】！\n"
                           "• 后半句 (desto/umso-主句)：desto/umso + 【比较级】 + 【变位动词紧贴其后 (Pos 2 倒装)】 + 主语！\n\n"
                           "• 标准高分示范：\n"
                           "  Je [mehr erneuerbare Energien] wir nutzen [从句末!], desto [sauberer] wird [主句Pos 2!] unsere Umwelt.\n"
                           "  Je [schneller] wir handeln [从句末], umso [größer] sind [Pos 2] die Erfolgschancen."
            },
            {
                "heading": "三、weder ... noch ... 的语序与否定陷阱",
                "content": "• weder...noch 自身已具备绝对否定含义，【绝不能再出现 nicht 或 kein】！\n"
                           "• 语序示例：\n"
                           "  - Weder [Pos 1] hat [Pos 2] er sich entschuldigt, noch [Pos 1] zeigte [Pos 2] er Reue.\n"
                           "  - (若位于句首，两分句均引发主谓倒装！)"
            },
            {
                "heading": "四、全球气候治理与生态辩论实战",
                "content": "• 国际气候谈判语篇：\n"
                           "  - Der Klimawandel betrifft sowohl die Industriestaaten als auch die Entwicklungsländer gleichermaßen.\n"
                           "  - Je entschlossener die Staatengemeinschaft die CO2-Emissionen drosselt, desto eher lassen sich irreversible Kipppunkte im globalen Klimasystem noch verhindern."
            },
            {
                "heading": "五、二重连词速记口诀",
                "content": "【二重连词逻辑诀】：\n"
                           "je 带从句动沉底，desto 倒装紧相依；\n"
                           "nicht nur 之后 sondern 也，weder noch 里无 nicht 避；\n"
                           "二重连缀架梁栋，议论华章文气提！"
            }
        ]
    },
    "B2_L09": {
        "title": "从句与介词短语转换 (Verbalstil vs. Nominalstil in Bildung & Soziologie)",
        "sections": [
            {
                "heading": "一、复杂时间状语从句与介词短语全面转换法则",
                "content": "┌──────────────────┬──────────────────────────┬────────────────────────────────────────────┐\n"
                           "│ 时间从句 (Verbal)│ 对应介词 (Nominal)       │ 转换示范                                   │\n"
                           "├──────────────────┼──────────────────────────┼────────────────────────────────────────────┤\n"
                           "│ nachdem ...      │ nach (+ Dat.)            │ Nachdem die Reform eingeführt worden war, ...│\n"
                           "│ (过去完成时)     │                          │ -> Nach der Einführung der Reform ...      │\n"
                           "├──────────────────┼──────────────────────────┼────────────────────────────────────────────┤\n"
                           "│ bevor / ehe ...  │ vor (+ Dat.)             │ Bevor die Vorlesung beginnt, ...           │\n"
                           "│ (在...之前)      │                          │ -> Vor Beginn der Vorlesung ...            │\n"
                           "├──────────────────┼──────────────────────────┼────────────────────────────────────────────┤\n"
                           "│ während ...      │ während (+ Gen.)         │ Während die Kinder lernen, ...             │\n"
                           "│ (在...期间)      │                          │ -> Während des Lernprozesses der Kinder ...│\n"
                           "├──────────────────┼──────────────────────────┼────────────────────────────────────────────┤\n"
                           "│ seitdem ...      │ seit (+ Dat.)            │ Seitdem er in Berlin wohnt, ...            │\n"
                           "│ (自从...以来)    │                          │ -> Seit seinem Umzug nach Berlin ...       │\n"
                           "├──────────────────┼──────────────────────────┼────────────────────────────────────────────┤\n"
                           "│ sobald ...       │ gleich nach (+ Dat.) /   │ Sobald die Prüfung beendet ist, ...        │\n"
                           "│ (一...就...)     │ sofort bei (+ Dat.)      │ -> Gleich nach Beendigung der Prüfung ...  │\n"
                           "└──────────────────┴──────────────────────────┴────────────────────────────────────────────┘"
            },
            {
                "heading": "二、方式与情况状语转换 (indem -> durch)",
                "content": "• indem (通过做...的方式): 转化为 durch + Akkusativ\n"
                           "  - Verbalstil: Man kann Bildungschancen verbessern, indem man einkommensschwache Familien finanziell fördert.\n"
                           "  - Nominalstil: Man kann Bildungschancen durch die finanzielle Förderung einkommensschwacher Familien verbessern."
            },
            {
                "heading": "三、条件与让步状语转换 (wenn -> bei; obwohl -> ungeachtet)",
                "content": "• wenn/falls -> bei (+ Dat.) / im Falle (+ Gen.):\n"
                           "  - Wenn die Gebühren steigen -> Bei einer Erhöhung der Gebühren / Im Falle eines Anstiegs der Gebühren\n"
                           "• obwohl -> trotz (+ Gen.) / ungeachtet (+ Gen.):\n"
                           "  - Obwohl viele Hindernisse vorliegen -> Ungeachtet zahlreicher bürokratischer Hindernisse"
            },
            {
                "heading": "四、社会阶层流动与教育公平论文实战",
                "content": "• 社会学学术文本改写：\n"
                           "  - Verbal: Obwohl Deutschland ein hochentwickeltes Bildungssystem besitzt, hängt der Bildungserfolg von Schülern stark von der sozialen Herkunft ab.\n"
                           "  - Nominal: Trotz des hochentwickelten deutschen Bildungssystems ist eine starke Abhängigkeit des Bildungserfolgs von der sozioökonomischen Herkunft der Schüler zu konstatieren."
            },
            {
                "heading": "五、转换技能速记口诀",
                "content": "【动名双向互换诀】：\n"
                           "nachdem 换 nach，bevor 换 vor，indem 换 durch 功法多；\n"
                           "动词沉潜变名字，冠词第二格修饰过；\n"
                           "从句散开便口语，凝练如金学术博！"
            }
        ]
    },
    "B2_L10": {
        "title": "状态被动态与过程被动态 (Zustandspassiv vs. Vorgangspassiv)",
        "sections": [
            {
                "heading": "一、过程被动态 vs 状态被动态本质对比矩阵",
                "content": "┌──────────────────┬──────────────────────────┬────────────────────────────┐\n"
                           "│ 语法范畴         │ 过程被动态 (Vorgangspassiv)│ 状态被动态 (Zustandspassiv)│\n"
                           "├──────────────────┼──────────────────────────┼────────────────────────────┤\n"
                           "│ 构成公式         │ werden (变位) + P.II     │ sein (变位) + P.II         │\n"
                           "├──────────────────┼──────────────────────────┼────────────────────────────┤\n"
                           "│ 核心关注点       │ 动作的过程、执行与变动   │ 动作完成后呈现的静态现状   │\n"
                           "├──────────────────┼──────────────────────────┼────────────────────────────┤\n"
                           "│ 时间视角         │ 动态发展中               │ 结果已经确立               │\n"
                           "├──────────────────┼──────────────────────────┼────────────────────────────┤\n"
                           "│ 典型示范         │ Die Tür wird um 20 Uhr   │ Die Tür ist um 20 Uhr      │\n"
                           "│                  │ geschlossen. (正在关)    │ geschlossen. (已关好锁紧)  │\n"
                           "└──────────────────┴──────────────────────────┴────────────────────────────┘"
            },
            {
                "heading": "二、状态被动态的时态系统 (Präsens, Präteritum, Perfekt)",
                "content": "状态被动态通过助动词 sein 自身变化呈现不同时态：\n\n"
                           "• 现在时 (Präsens): Das Geschäft ist sonntags geschlossen.\n"
                           "• 过去时 (Präteritum): Als die Polizei eintraf, war das Fenster bereits zertrümmert.\n"
                           "• 完成时 (Perfekt): Die Straße ist seit Tagen gesperrt gewesen.\n\n"
                           "【警惕】：绝不可把状态被动态过去时 war geschlossen 与过程被动态过去时 wurde geschlossen 混淆！"
            },
            {
                "heading": "三、不能构成状态被动态的动词类型",
                "content": "并非所有动词都能变成状态被动！只有具备【结果性 (Resultative Verben)】的及物动词才能构成状态被动：\n\n"
                           "• 能构成状态被动 (有持久结果)：öffnen, schließen, reparieren, zerstören, verletzen\n"
                           "  - Das Auto ist repariert. (车修好了。)\n"
                           "• 不能构成状态被动 (动作无残留物理状态)：sehen, hören, loben, lieben, schlagen\n"
                           "  - 不能说 *Er ist gelobt. (只能说 Er wurde gelobt.)"
            },
            {
                "heading": "四、人口结构变化与养老体系现状报告",
                "content": "• 政策研究文本：\n"
                           "  - Viele Pflegeheime sind aufgrund des akuten Fachkräftemangels chronisch überlastet.\n"
                           "  - Die Rentenreform ist vom Bundestag bereits beschlossen und in den Gesetzesblättern verankert."
            },
            {
                "heading": "五、状态被动速记口诀",
                "content": "【被动态对比辨析歌】：\n"
                           "werden 进行重过程，动态发生看得清；\n"
                           "sein 配分词定状态，尘埃落定结果呈；\n"
                           "结果动词方适用，修毕紧锁状态成！"
            }
        ]
    },
    "B2_L11": {
        "title": "主观情态动词体系 (Subjektive Bedeutung der Modalverben)",
        "sections": [
            {
                "heading": "一、主观推测概率谱系 (Epistemische Modalität: von 100% bis 30%)",
                "content": "当情态动词用于表达说话人根据已知线索进行的【主观推测】时，构成严密的概率谱系：\n\n"
                           "┌────────────┬──────────┬──────────────────────────┬────────────────────────────────────────────┐\n"
                           "│ 情态动词   │ 确定性   │ 汉语对应                 │ 示范例句                                   │\n"
                           "├────────────┼──────────┼──────────────────────────┼────────────────────────────────────────────┤\n"
                           "│ muss       │ 90-100%  │ 一定/必然如此 (推理必然) │ Das Licht brennt, er muss zu Hause sein.   │\n"
                           "│ müsste     │ 85%      │ 按常理应该 (极大概率)    │ Er müsste jeden Moment ankommen.           │\n"
                           "│ dürfte     │ 75%      │ 大概/很有可能 (学术首选) │ Der Täter dürfte ortskundig gewesen sein.  │\n"
                           "│ kann       │ 50%      │ 可能/也许 (一半概率)     │ Die Prognose kann zutreffen oder nicht.    │\n"
                           "│ könnte     │ 40%      │ 或许/有可能 (委婉不确定) │ Das System könnte manipuliert worden sein. │\n"
                           "│ mag        │ 30%      │ 也许/姑且可能 (让步承认) │ Das mag stimmen, aber es ist irrelevant.   │\n"
                           "└────────────┴──────────┴──────────────────────────┴────────────────────────────────────────────┘"
            },
            {
                "heading": "二、对过去事实进行主观推测的时态公式",
                "content": "表达‘过去想必已经发生了某事’，必须使用【情态动词 + 完成时不定式 (Infinitiv Perfekt)】：\n\n"
                           "• 公式：【情态动词现在时】 + ...... + 【第二分词】 + 【haben / sein 原形 (句末)】\n"
                           "  - Er meldet sich nicht. Er muss den Zug verpasst haben. (他一定把火车坐落下了。)\n"
                           "  - Sie antwortet nicht auf die Mail. Sie dürfte im Urlaub gewesen sein. (她大概去度假了。)\n"
                           "  - Der Zeuge könnte sich geirrt haben. (证人或许当时看错了。)"
            },
            {
                "heading": "三、表达转述与自称：soll (据说) vs will (自称)",
                "content": "• 【soll (据说 / 传言)】：转述来自第三方的传闻或未经证实的报道：\n"
                           "  - Der Minister soll Schmiergelder angenommen haben. (据说该部长收受了贿赂。)\n"
                           "  - Das Unternehmen soll vor der Insolvenz stehen. (传言该公司濒临破产。)\n\n"
                           "• 【will (自称 / 谎称)】：转述当事人的自我声称，说话人通常持怀疑态度：\n"
                           "  - Der Verdächtige will zur Tatzeit geschlafen haben. (嫌疑人坚称案发时在睡觉。)\n"
                           "  - Er will den Nobelpreisträger persönlich kennen. (他自称亲自认识这位诺奖得主。)"
            },
            {
                "heading": "四、虚假信息鉴别与媒体可信度核查实战",
                "content": "• 新闻真实性调查：\n"
                           "  - Die im Internet kursierenden Gerüchte dürften von Fake-Accounts gezielt gestreut worden sein.\n"
                           "  - Der Sprecher will von den veruntreuten Parteispenden nichts gewusst haben, was Investigativjournalisten jedoch vehement bestreiten."
            },
            {
                "heading": "五、主观情态动词速记口诀",
                "content": "【主观推测概率歌】：\n"
                           "muss 必然九成九，dürfte 大概学术首；\n"
                           "könnte 或许半信疑，推测过去分词 + 原形走 (P.II + haben/sein)；\n"
                           "soll 是据说传言传，will 是自称留心眼！"
            }
        ]
    },
    "B2_L12": {
        "title": "高级非现实假设与愿望从句 (Erweiterte irreale Bedingungen & Beinahe-Sätze)",
        "sections": [
            {
                "heading": "一、差一点就...句型 (Beinahe- / Fast-Sätze)",
                "content": "表达‘过去差一点/险些发生某事（但幸好没有发生）’的高级句型：\n\n"
                           "• 【结构一 (倒装结构)】：Beinahe / Fast + 【wäre / hätte】 + [主语] ... + 【Partizip II】\n"
                           "  - Fast wäre das Flugzeug abgestürzt. (飞机差一点就坠毁了！)\n"
                           "  - Beinahe hätte ich den wichtigen Abgabetermin vergessen. (我险些忘记了关键截止日期。)\n\n"
                           "• 【结构二 (带 wenn 的从句)】：\n"
                           "  - Es fehlte nicht viel, und die Verhandlungen wären gescheitert.\n"
                           "  - Beinahe wäre der Patient an den Folgen der Infektion gestorben."
            },
            {
                "heading": "二、高级限制性排除假设从句 (es sei denn, dass...)",
                "content": "表达‘除非...否则不可能’：\n\n"
                           "• es sei denn, (dass) ... / außer wenn ...\n"
                           "  - Wir müssen die Preise erhöhen, es sei denn, dass die Rohstoffkosten wieder sinken.\n"
                           "  - (若省略 dass，后接正常主谓语序)：Wir müssen die Preise erhöhen, es sei denn, die Rohstoffkosten sinken wieder."
            },
            {
                "heading": "三、假设性让步从句 (selbst wenn / auch wenn)",
                "content": "• selbst wenn / auch wenn + Konjunktiv II: 表达‘即便/哪怕真的发生了某事，也...’：\n"
                           "  - Selbst wenn wir unbegrenzte finanzielle Mittel zur Verfügung hätten, könnten wir dieses biologische Problem nicht über Nacht lösen.\n"
                           "  - Auch wenn die Theorie plausibel erschiene, müsste sie erst empirisch verifiziert werden."
            },
            {
                "heading": "四、哲学思辨与思想实验 (Gedankenexperimente)",
                "content": "• 启蒙哲学与认识论思辨：\n"
                           "  - Angenommen, es gäbe ein absolut objektives Erkenntnisvermögen, so bliebe dennoch die Frage offen, wie der menschliche Verstand dieses abbilden könnte.\n"
                           "  - Fast wäre die neuzeitliche Philosophie im reinen Dogmatismus erstarrt, hätte Kant nicht die 'Kritik der reinen Vernunft' verfasst."
            },
            {
                "heading": "五、高级假设从句速记口诀",
                "content": "【险些假设与排除诀】：\n"
                           "Fast / Beinahe wäre 险发难，幸免于难第二虚；\n"
                           "es sei denn 除非排除，条件严谨立规章；\n"
                           "selbst wenn 即便千难阻，思辨立论笔力刚！"
            }
        ]
    },
    "B2_L13": {
        "title": "语篇衔接与高阶逻辑副词 (Textkohärenz & Adverbiale Konnektoren)",
        "sections": [
            {
                "heading": "一、高端议论文逻辑连接副词分类词库",
                "content": "德福/歌德 B2 写作中，词汇丰富度与篇章连贯性 (Kohärenz & Kohäsion) 占据 40% 的分值：\n\n"
                           "┌────────────┬──────────────────────────────────┬────────────────────────┐\n"
                           "│ 逻辑范畴   │ 高阶逻辑副词 (位于 Pos 1 倒装)    │ 汉语核心语义           │\n"
                           "├────────────┼──────────────────────────────────┼────────────────────────┤\n"
                           "│ 必然因果   │ folglich, demnach, somit,        │ 由此必然导致/因此      │\n"
                           "│            │ demzufolge, infolgedessen        │                        │\n"
                           "├────────────┼──────────────────────────────────┼────────────────────────┤\n"
                           "│ 转折让步   │ dennoch, nichtsdestotrotz,       │ 尽管如此/仍然/然而     │\n"
                           "│            │ dessen ungeachtet, allerdings    │                        │\n"
                           "├────────────┼──────────────────────────────────┼────────────────────────┤\n"
                           "│ 纠正对立   │ vielmehr, stattdessen,           │ 恰恰相反/反倒/而是     │\n"
                           "│            │ im Gegenteil                     │                        │\n"
                           "├────────────┼──────────────────────────────────┼────────────────────────┤\n"
                           "│ 限制说明   │ insofern, gewissermaßen,         │ 在此范围内/就此而言    │\n"
                           "│            │ namentlich                       │                        │\n"
                           "└────────────┴──────────────────────────────────┴────────────────────────┘"
            },
            {
                "heading": "二、连接副词的句法位置与倒装铁律",
                "content": "• 连接副词不是连词！它们是句子的独立成分，当它们【放在句首第 1 位】时，【变位动词紧随其后 (第 2 位)】，主语退至第 3 位：\n"
                           "  - 正确：Die Kosten sind explodiert. Folglich [Pos 1] müssen [Pos 2] wir [Pos 3] das Projekt stoppen.\n"
                           "  - 错误：*Folglich wir müssen... (严重英语语序感染！)\n\n"
                           "• 零位连词对比：und, aber, oder, denn, sondern 是 0 位连词，不占位不倒装！\n"
                           "  - Aber [0位] wir [Pos 1] müssen [Pos 2] das Projekt stoppen."
            },
            {
                "heading": "三、国际政治地缘格局深度语篇剖析",
                "content": "• 国际安全学术评论：\n"
                           "  - Die diplomatischen Verhandlungen verliefen zäh. Dennoch einigten sich die Delegationen auf einen Waffenstillstand.\n"
                           "  - Die Mitgliedsstaaten konnten ihre Haushaltsdefizite nicht konsolidieren; infolgedessen stiegen die Renditen der Staatsanleihen dramatisch an.\n"
                           "  - Der Vertrag stärkt nicht die nationale Souveränität, vielmehr schränkt er den Handlungsspielraum ein."
            },
            {
                "heading": "四、高分段落句间衔接金字塔模板",
                "content": "• [论点句: Behauptung] -> [因果展开: Demzufolge...] -> [对立考量: Allerdings darf nicht übersehen werden, dass...] -> [折中结论: Somit lässt sich schlussfolgern, dass...]"
            },
            {
                "heading": "五、语篇连接副词速记口诀",
                "content": "【逻辑衔接倒装歌】：\n"
                           "副词居首要倒装，动词二位主语让；\n"
                           "folglich 因而 dennoch 然，stattdessen 反倒换；\n"
                           "0 位连词 aber denn，逻辑流畅篇章展！"
            }
        ]
    },
    "B2_L14": {
        "title": "高阶功能动词体系 (Gehobene Funktionsverbgefüge in Rede & Debatte)",
        "sections": [
            {
                "heading": "一、高端功能动词短语分类实战库",
                "content": "在 B2 阶段，功能动词短语 (FVG) 是突破语言天花板的必经之路：\n\n"
                           "┌────────────────────────────┬────────────────────────┬────────────────────────────────────────┐\n"
                           "│ 动词族群                   │ 典型功能动词短语       │ 等价普通动词及释义                     │\n"
                           "├────────────────────────────┼────────────────────────┼────────────────────────────────────────┤\n"
                           "│ bringen (使动/开启)        │ in Erfahrung bringen   │ erfahren (探听到/获悉)                 │\n"
                           "│                            │ zum Ausdruck bringen   │ ausdrücken (表达出)                    │\n"
                           "│                            │ zur Sprache bringen    │ ansprechen (提出讨论)                  │\n"
                           "│                            │ in Gefahr bringen      │ gefährden (危及)                       │\n"
                           "├────────────────────────────┼────────────────────────┼────────────────────────────────────────┤\n"
                           "│ nehmen (采取/承受)         │ Stellung nehmen zu     │ sich äußern (表态/发表立场)            │\n"
                           "│                            │ in Kauf nehmen         │ akzeptieren (容忍/承受代价)            │\n"
                           "│                            │ Rücksicht nehmen auf   │ berücksichtigen (体谅/顾及)            │\n"
                           "├────────────────────────────┼────────────────────────┼────────────────────────────────────────┤\n"
                           "│ stellen (提供/置于)        │ unter Beweis stellen   │ beweisen (证明)                        │\n"
                           "│                            │ zur Diskussion stellen │ diskutieren (提交讨论)                 │\n"
                           "│                            │ in Rechnung stellen    │ berechnen (收取费用/考虑在内)          │\n"
                           "├────────────────────────────┼────────────────────────┼────────────────────────────────────────┤\n"
                           "│ treten (进入状态)          │ in Kraft treten        │ gültig werden (生效)                   │\n"
                           "│                            │ in Erscheinung treten  │ sichtbar werden (显露)                 │\n"
                           "└────────────────────────────┴────────────────────────┴────────────────────────────────────────┘"
            },
            {
                "heading": "二、功能动词短语的主动与被动内在机制",
                "content": "许多功能动词短语成对出现，分别代表主动使动与被动状态：\n\n"
                           "• 主动使动 (bringen / setzen / stellen)：\n"
                           "  - Das Ministerium setzt die Reform in Gang. (部门启动改革。)\n"
                           "• 被动状态 (kommen / stehen / geraten)：\n"
                           "  - Die Reform kommt in Gang. (改革进入运转阶段。)\n"
                           "  - Das Unternehmen gerät in Bedrängnis. (企业陷入困境。)"
            },
            {
                "heading": "三、学术演讲辩论与法庭控辩实操",
                "content": "• 辩论质询发言：\n"
                           "  - Ich möchte zu den Vorwürfen der Gegenseite ausführlich Stellung nehmen.\n"
                           "  - Wir müssen diesen kritischen Aspekt unbedingt zur Sprache bringen.\n"
                           "  - Die Bundesregierung hat ihre Handlungsfähigkeit eindrucksvoll unter Beweis gestellt."
            },
            {
                "heading": "四、高分作文点睛提分策略",
                "content": "写作时将普通的动词替换为高阶 FVG，瞬间提升学术质感：\n"
                           "• 基础：Wir müssen diesen Punkt diskutieren.\n"
                           "• 升华：Wir müssen diesen Punkt zur Diskussion stellen.\n"
                           "• 基础：Er akzeptierte das hohe Risiko.\n"
                           "• 升华：Er nahm das erhebliche Risiko bewusst in Kauf."
            },
            {
                "heading": "五、高阶功能动词速记口诀",
                "content": "【高阶 FVG 提分歌】：\n"
                           "Stellung nehmen 表立场，zur Sprache bringen 提商量；\n"
                           "in Kauf nehmen 担代价，unter Beweis 证明长；\n"
                           "in Kraft treten 新法立，高端修辞字字香！"
            }
        ]
    },
    "B2_L15": {
        "title": "歌德 B2 & TestDaF 德福备考终极冲刺与学术写作指南",
        "sections": [
            {
                "heading": "一、德福/歌德 B2 学术写作两大核心题型解构",
                "content": "德福 (TestDaF Schriftlicher Ausdruck) 与歌德 B2 写作是通往德国名校大学录取的终极关卡：\n\n"
                           "• 核心构成两大板块：\n"
                           "  1. 【图表描述 (Grafikbeschreibung)】：客观准确呈现图表数据、趋势与极端值。\n"
                           "  2. 【论辩论证 (Argumentation)】：就争议议题权衡正反立场，提出缜密的论据链并给出个人观点。"
            },
            {
                "heading": "二、学术图表描述六步曲标准学术语料库",
                "content": "1. 【引出主题 (Thema & Titel)】：\n"
                           "   - Die vorliegende Grafik mit dem Titel '...' liefert aufschlussreiche Daten über ...\n"
                           "2. 【交代数据来源与时间 (Quelle & Erhebungszeitraum)】：\n"
                           "   - Die Daten stammen vom Statistischen Bundesamt und beziehen sich auf das Jahr ...\n"
                           "3. 【图表类型与计量单位 (Form & Maßeinheit)】：\n"
                           "   - Die Angaben erfolgen in Prozent / absoluten Zahlen und sind in Form eines Balkendiagramms dargestellt.\n"
                           "4. 【趋势与发展描述 (Trendbeschreibung)】：\n"
                           "   - Im betrachteten Zeitraum ist ein kontinuierlicher Anstieg von ... auf ... zu verzeichnen.\n"
                           "   - Demgegenüber ist der Anteil drastisch gesunken / stagniert auf hohem Niveau.\n"
                           "5. 【极值与显著对比 (Extremwerte & Auffälligkeiten)】：\n"
                           "   - Spitzenreiter ist ..., gefolgt von ..., während ... das Schlusslicht bildet.\n"
                           "6. 【图表总结 (Zusammenfassung)】：\n"
                           "   - Zusammenfassend lässt sich festhalten, dass ..."
            },
            {
                "heading": "三、论证展开三要素：Behauptung -> Begründung -> Beispiel",
                "content": "德语严谨思辨要求的黄金论证链：\n\n"
                           "• 1. Behauptung (论点明确): Ein zentrales Argument gegen die Atomkraft ist das ungelöste Problem der Endlagerung.\n"
                           "• 2. Begründung (逻辑解释): Denn radioaktiver Müll strahlt Hunderttausende von Jahren und gefährdet das Grundwasser künftiger Generationen.\n"
                           "• 3. Beispiel / Beleg (实证或数据): Dies zeigt sich beispielhaft am maroden Zustand der Schachtanlage Asse in Niedersachsen."
            },
            {
                "heading": "四、德福/歌德 B2 考前 24 小时黄金自查清单",
                "content": "1. 扩展分词定语还原是否漏掉了状语？\n"
                           "2. 第一虚拟式引述他人观点时，时态是否保持一致？\n"
                           "3. 二重连词 je ... desto 后半句动词是否倒装？\n"
                           "4. 名词化风格中的第二格词尾 -(e)s 是否遗漏？\n"
                           "5. 图表描述是否误加入个人主观臆断（前部必须纯客观）？\n"
                           "6. 议论文论点是否做到有理有据有例证？"
            },
            {
                "heading": "五、德福 B2 终极通关定心口诀",
                "content": "【德福 B2 决胜歌】：\n"
                           "图表描摹六步走，来源趋势极值收；\n"
                           "论点因果例证紧，正反权衡立意高；\n"
                           "名词风格展功力，第一虚拟引文献；\n"
                           "沉着从容下笔顺，德意志名校任你挑！"
            }
        ]
    }
}
