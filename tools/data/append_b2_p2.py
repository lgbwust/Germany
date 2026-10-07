#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Appends Lessons 7, 8, 9, 10 to tools/data/generate_b2_p2.py,
then compiles tools/data/b2_part2.py.
"""

import os
import sys

# LESSON 7: Kognitionspsychologie & Neurowissenschaften (70 words)
L07 = {
    "id": "B2_L07",
    "title": "第7课：认知心理学、脑科学与人类心智 (Kognitionspsychologie)",
    "summary": "掌握高级关系从句 (wer, was, dessen, deren, worüber)、脑科学与认知神经科学前沿词汇",
    "grammar": {
        "title": "高级关系从句体系 (Erweiterte Relativsätze mit wer, was, dessen/deren)",
        "sections": [
            {
                "heading": "1. 第二格关系代词 dessen (阳性/中性) 与 deren (阴性/复数)：修饰所属关系，无须变格词尾：",
                "content": "• Der Proband, dessen Gehirnaktivität gemessen wurde, zeigte keine Ermüdung.\n• Die Forscherin, deren bahnbrechende Studie publiziert wurde, erhielt den Preis.\n• In dessen / deren 后紧随所修饰的名词，名词前绝对不加冠词！"
            },
            {
                "heading": "2. 泛指代词 wer / was 引导自由关系从句：",
                "content": "• Wer rastet, der rostet. (流水不腐，户枢不蠹)\n• Was die Kognitionsforschung herausfand, überraschte die Fachwelt."
            }
        ]
    },
    "quiz": [
        {
            "id": "B2_L07_Q1",
            "type": "GRAMMAR_FILL",
            "question": "Die Patientin, ______ (deren / dessen / welcher) Gedächtnisleistung untersucht wurde, erholte sich rasch.",
            "options": ["deren", "dessen", "welcher", "denen"],
            "correctIndex": 0,
            "explanation": "先行词是阴性单数 die Patientin，第二格物主关系代词必须用 deren。"
        },
        {
            "id": "B2_L07_Q2",
            "type": "MEANING_SELECT",
            "question": "“die Neuroplastizität” 在现代脑科学中的重大理论发现是：",
            "options": ["大脑神经突触随学习与经验终身重塑重构的能力", "脑血管硬化指数", "头骨外伤修复速度", "神经系统遗传退化"],
            "correctIndex": 0,
            "explanation": "die Neuroplastizität 指人脑神经回路在后天学习刺激下终身具备“神经可塑性”。"
        },
        {
            "id": "B2_L07_Q3",
            "type": "GRAMMAR_FILL",
            "question": "Der Wissenschaftler, ______ (dessen / deren / dem) Thesen diskutiert wurden, hielt einen Vortrag.",
            "options": ["dessen", "deren", "dem", "desselben"],
            "correctIndex": 0,
            "explanation": "先行词是阳性单数 der Wissenschaftler，第二格所属关系代词用 dessen。"
        },
        {
            "id": "B2_L07_Q4",
            "type": "LISTENING_MCQ",
            "question": "“Kognitive Dissonanz entsteht, wenn Handeln und innere Überzeugungen im Widerspruch stehen.” 描述的心理学机制是：",
            "options": ["当实际行为与内心深层信念发生冲突矛盾时，便会诱发认知失调与心理不适。", "行为完全由潜意识决定。", "认知能力随年龄下降。", "大脑无法同时处理两条信息。"],
            "correctIndex": 0,
            "explanation": "Kognitive Dissonanz = 认知失调，im Widerspruch stehen = 处于自相矛盾之中。"
        },
        {
            "id": "B2_L07_Q5",
            "type": "SENTENCE_BUILDER",
            "question": "重组认知神经学核心句式：“verarbeitet / Ununterbrochen / sensorische Reize / Das menschliche Gehirn”",
            "options": ["Das menschliche Gehirn verarbeitet ununterbrochen sensorische Reize.", "Ununterbrochen sensorische Reize das menschliche Gehirn verarbeitet.", "Sensorische Reize das menschliche Gehirn verarbeitet ununterbrochen nicht.", "Verarbeitet das menschliche Gehirn ununterbrochen sensorische Reize."],
            "correctIndex": 0,
            "explanation": "主语 (Das menschliche Gehirn) + 谓语 (verarbeitet) + 状语 (ununterbrochen) + 宾语 (sensorische Reize)。"
        }
    ],
    "words": [
        ("das Gehirn", "das", "Nomen", "-e", "大脑，脑", "Das Gehirn verbraucht etwa zwanzig Prozent des gesamten Grundumsatzes.", "人脑虽仅占微小体重，却长年消耗着机体整整五分之一的基础代谢能量。"),
        ("die Kognition", "die", "Nomen", "-en", "认知能力，认知过程", "Die Kognition umfasst Wahrnehmung, Erinnerung, Denken und Sprache.", "广义认知科学范畴完整涵盖了微观感知觉、长短期记忆编码、逻辑思辨与符号语言中枢。"),
        ("das Bewusstsein", "das", "Nomen", "unz.", "意识，清醒状态", "Das Geheimnis des menschlichen Bewusstseins bleibt eine der größten Fragen.", "人类自我反思性清醒主观意识的本质生成源泉，依然是现代自然哲学最高深莫测的未解之谜。"),
        ("das Gedächtnis", "das", "Nomen", "-se", "记忆力，记忆中枢", "Das Arbeitsgedächtnis hält Informationen für wenige Sekunden abrufbereit.", "额叶工作记忆中枢能够在短短数秒至数十秒的极短时间窗口内保持信息的高速暂存与实时调用。"),
        ("die Wahrnehmung", "die", "Nomen", "-en", "知觉，感官认知", "Subjektive Wahrnehmung kann durch optische Täuschungen leicht verzerrt werden.", "人类个体的主观感官知觉往往极其容易被精心设计的视错觉图案轻而易举地带偏误导。"),
        ("der Reiz", "der", "Nomen", "-e", "外界刺激，诱惑", "Sensorische Reize werden über Nervenbahnen direkt ins Zentralnervensystem geleitet.", "外界五彩斑斓的微观感官刺激经由传入周围神经纤维通路，以神经电冲动形式闪电汇聚至中枢神经系统。"),
        ("das Nervensystem", "das", "Nomen", "-e", "神经系统", "Das vegetative Nervensystem steuert unwillkürliche Körperfunktionen wie Herzschlag und Atmung.", "植物性自主神经系统在潜意识后台精密调控着心跳律动、呼吸节律与平滑肌蠕动等非意志所能支配的生命本能。"),
        ("die Synapse", "die", "Nomen", "-n", "神经元突触", "An den Synapsen übertragen chemische Botenstoffe elektrische Signale auf Nachbarzellen.", "在神经元交接的微米级突触间隙中，化学神经递质以量子级别释放传递着神经元之间的双向交互电位。"),
        ("der Neurotransmitter", "der", "Nomen", "-", "神经递质", "Dopamin und Serotonin sind lebenswichtige Neurotransmitter für Stimmung und Motivation.", "多巴胺与五羟色胺等单胺类神经递质是调控人类情绪高低、愉悦奖赏体验与内生奋斗动力不可或缺的核心生化信使。"),
        ("das Dopamin", "das", "Nomen", "unz.", "多巴胺", "Dopamin wird im Belohnungszentrum des Gehirns bei unerwartetem Erfolg freigesetzt.", "每当我们在生活中意外收获超预期的惊喜回报或成就奖励时，脑中中脑边缘奖赏通路便会激增释放充沛的多巴胺。"),
        ("das Serotonin", "das", "Nomen", "unz.", "五羟色胺，血清素", "Ein Mangel an Serotonin wird in der Psychiatrie mit depressiven Episoden in Verbindung gebracht.", "临床精神病理学与神经生物学研究证实，中枢突触间隙五羟色胺水平的长期严重匮乏与抑郁发作高度正相关。"),
        ("die Neuroplastizität", "die", "Nomen", "unz.", "大脑神经可塑性", "Dank der Neuroplastizität kann das menschliche Gehirn bis ins hohe Alter neue Verbindungen knüpfen.", "得益于人脑终身保留的神经可塑性神迹，即便步入耄耋之年，人类依然可以通过积极用脑持续编织崭新的神经网络回路。"),
        ("das Neuron", "das", "Nomen", "-en", "神经细胞，神经元", "Milliarden von Neuronen bilden ein hochkomplexes verschaltetes neuronales Netzwerk.", "数百亿枚高度特化的神经元细胞交织重叠，构筑成了一张全宇宙已知结构最为精妙绝伦的高维神经网络互联大网。"),
        ("die Hirnrinde", "die", "Nomen", "unz.", "大脑皮层 (Kortex)", "Der präfrontale Kortex der Hirnrinde ist für planvolles und rationales Handeln zuständig.", "坐落于大脑皮质最前端的前额叶皮层，专门负责统筹人类最长远的理性深谋远虑规划与严密执行控制。"),
        ("der Kortex", "der", "Nomen", "Kortizes", "大脑皮层", "Im visuellen Kortex werden die von den Augen übermittelten Lichtimpulse zu Bildern verarbeitet.", "在枕叶初级视觉皮层中，由视网膜视神经实时编码传输的感光电脉冲信号被瞬间复原拼装为栩栩如生的三维现实画面。"),
        ("die Amygdala", "die", "Nomen", "Amygdalae", "杏仁核（恐惧与情绪中枢）", "Die Amygdala reagiert blitzschnell auf drohende Gefahren und löst Alarmbereitschaft aus.", "位于颞叶深处的杏仁核中枢在捕捉到潜在外部致命险情的一刹那，便以毫秒级极速在全身拉响红色战斗或逃跑警报。"),
        ("der Hippocampus", "der", "Nomen", "Hippocampi", "海马体（记忆巩固中枢）", "Der Hippocampus überführt flüchtige Kurzzeitinformationen in das dauerhafte Langzeitgedächtnis.", "海马体如同大脑的记忆中央调度服务器，负责在夜间深度睡眠中将白昼摄入的短时记忆固化转录为持久的长时记忆。"),
        ("die Intuition", "die", "Nomen", "-en", "直觉，下意识洞察", "Erfahrene Diagnostiker verlassen sich neben Laborwerten auch auf ihre klinische Intuition.", "经验极其丰富的临床顶尖泰斗在面对疑难杂症时，除了依赖化验单硬核指标外，同样高度信赖自己多年积淀形成的敏锐临床直觉。"),
        ("der Instinkt", "der", "Nomen", "-e", "本能", "Im Angesicht existenzieller Lebensgefahr übernimmt der uralte tierische Selbsterhaltungstrieb.", "当遭遇命悬一线的极端生死考验时，潜藏在人类基因最底层、历经数百万年淬炼的古老求生本能瞬间接管一切行为主导权。"),
        ("die Reflexion", "die", "Nomen", "-en", "反思，省察", "Kritisches Denken setzt die ständige Reflexion eigener Vorurteile und Denkmuster voraus.", "践行真正的批判性独立思考，首要前提便在于永不自满地对自身固有的认知偏见与思维盲区实施深度省察剖析。"),
        ("das Denkmuster", "das", "Nomen", "-", "思维定式，认知模式", "Verkrustete Denkmuster behindern Innovationen und kreative Problemlösungen in Konzernen.", "僵化教条、因循守旧的陈旧思维定式在跨国大企业内部往往成为扼杀前沿技术创新与敏捷突破的最大隐形阻力。"),
        ("die Heuristik", "die", "Nomen", "-en", "启发法，直觉经验推断法则", "Im Alltag greift das Gehirn auf Heuristiken zurück, um Entscheidungen blitzschnell zu treffen.", "在面对信息不完备的复杂日常抉择时，人脑会本能调用启发式经验法则，以极低的算力能耗瞬间拍板敲定决策。"),
        ("die Dissonanz", "die", "Nomen", "-en", "不协调，认知失调", "Kognitive Dissonanz zwingt den Menschen oft dazu, seine Überzeugungen nachträglich schönzureden.", "认知失调诱发的心灵痛苦，往往迫使当事人在事后本能地为自己前后矛盾的可笑举动编造冠冕堂皇的借口予以合理化粉饰。"),
        ("die Rationalität", "die", "Nomen", "unz.", "理性", "Vollkommene Rationalität ist eine idealisierte Annahme der neoklassischen Wirtschaftswissenschaft.", "所谓“具备绝对完备信息与冷酷计算能力的全知理性经济人”，从来都只是新古典主义微观经济学高度空中楼阁式的理想假定。"),
        ("die Emotionalität", "die", "Nomen", "unz.", "感性，情绪化倾向", "Entscheidungen an den internationalen Finanzmärkten sind stark von unbewusster Emotionalität geprägt.", "在瞬息万变、惊涛骇浪的全球跨国金融博弈博弈深处，巨头决策往往深受集体潜意识盲从与非理性情绪的深度操弄。"),
        ("die Fokussierung", "die", "Nomen", "unz.", "专注聚焦，注意力集中", "Tiefe mentale Fokussierung versetzt den Geist in den Zustand des schöpferischen Flow-Erlebens.", "心无旁骛、神注一掷的深层沉浸式精神聚焦，能够将创作者的整个心智带入天人合一、灵感井喷的巅峰“心流状态”。"),
        ("die Ablenkung", "die", "Nomen", "-en", "分心干扰，诱惑", "Ständige Benachrichtigungen auf dem Smartphone sind die größte Ablenkung im digitalen Zeitalter.", "智能手机屏幕上此起彼伏、永无宁日的推送横幅弹窗，已成为数字时代彻底撕碎现代人深度注意力的头号无形杀手。"),
        ("die Vergesslichkeit", "die", "Nomen", "unz.", "健忘，遗忘倾向", "Leichte Vergesslichkeit im Alltag ist oft lediglich die Folge von chronischem Schlafmangel.", "日常生活中偶发的丢三落四轻微健忘现象，在绝大多数情况下其实仅仅是长期慢性报复性熬夜睡眠匮乏所亮起的警灯。"),
        ("die Demenz", "die", "Nomen", "unz.", "阿尔茨海默病，老年痴呆综合征", "Frühe Diagnose und gezieltes Gehirntraining können den Verlauf einer Demenz spürbar verlangsamen.", "尽早完成高通量脑脊液分子靶向筛查并辅以针对性的认知中枢功能康复训练，能够显著延缓早发性老年认知症的恶化进程。"),
        ("das Trauma", "das", "Nomen", "Traumen", "心理创伤，精神应激损伤", "Posttraumatische Belastungsstörungen entstehen durch seelische Erschütterungen schweren Ausmaßes.", "创伤后应激障碍(PTSD)深植于个体在历经战争、空难或严重暴力等极端毁灭性外界精神重创后在大脑中枢烙下的血色印记。"),
        ("die Resilienz", "die", "Nomen", "unz.", "心理韧性，抗逆力", "Psychologische Resilienz befähigt Individuen, schwere Lebenskrisen ohne seelischen Bruch zu überstehen.", "强大的内在心理韧性与复原力，赋予了个体在直面泰山崩于前般的命运重特大灾难变故时仍能保持精神骨架绝不折断的坚韧品格。"),
        ("die Empathie", "die", "Nomen", "unz.", "共情能力，神入同理心", "Spiegelneuronen im Gehirn bilden die biologische Grundlage menschlicher Empathie und Nächstenliebe.", "弥散分布在大脑皮层各功能区的镜像神经元回路，构成了人类能够感知他人喜怒哀乐、践行深切同理心与博爱的生物学根基。"),
        ("die Verhaltensforschung", "die", "Nomen", "unz.", "行为学，动物行为学研究", "Die moderne Verhaltensforschung analysiert Entscheidungsabläufe unter kontrollierten Laborbedingungen.", "现代行为心理科学在严格隔绝外部干扰的标准化心理学实验室环境中，逐帧拆解并量化人类面临风险收益时的微观决策逻辑。"),
        ("die Hypnose", "die", "Nomen", "unz.", "催眠疗法", "Medizinische Hypnose kann chronische Schmerzzustände und Phobien nachweisbar lindern.", "在正规三甲医院心理科由执业资深专家主持的现代医疗催眠，已被多项循证医学严格证实能切实大幅缓解难治性顽固神经痛。"),
        ("die Suggestion", "die", "Nomen", "-en", "暗示，心理诱导", "Autosuggestion ist eine wirksame Methode, um hemmende Glaubenssätze schrittweise aufzulösen.", "通过每天清晨进行正向积极的自我心理暗示冥想，能够循序渐进地打破潜藏在心底深处自我设限、固步自封的消极认知枷锁。"),
        ("das Motiv", "das", "Nomen", "-e", "深层行为动机", "Kriminalisten und Psychologen versuchen gleichermaßen, das verborgene Motiv des Täters zu ergründen.", "经验丰富的刑侦法医心理学家与专案侦查员协同发力，誓要从杂乱无章的蛛丝马迹中穿透抽丝剥茧还原凶手深藏于心的作案动机。"),
        ("der Anreiz", "der", "Nomen", "-e", "激励因素，诱因", "Finanzielle Anreize allein reichen nicht aus, um kreative Spitzenkräfte langfristig zu binden.", "单单依靠粗暴单一的薪酬现金绩效考核激励诱饵，在现实中根本无法真正长久拴住并彻底激发顶尖硬核创意天才的毕生向心力。"),
        ("die Frustrationstoleranz", "die", "Nomen", "unz.", "逆商，挫折容忍耐受力", "Eine hohe Frustrationstoleranz ist die wichtigste Voraussetzung für wissenschaftliche Pionierarbeit.", "具备在历经上千次甚至数万次实验无情失败后仍能掸去尘土微笑重来的超高抗挫折逆商，是攀登世界科学绝顶的最核心底色。"),
        ("die Selbstwirksamkeit", "die", "Nomen", "unz.", "自我效能感", "Der Glaube an die eigene Selbstwirksamkeit versetzt Menschen in die Lage, Berge zu versetzen.", "深信自己凭借坚持不懈的奋斗与科学方法必能掌控局面、克服万难的“自我效能感”，往往能在绝境中催生出改写乾坤的人间奇迹。"),
        ("das Unterbewusstsein", "das", "Nomen", "unz.", "深层潜意识", "Sigmund Freud postulierte, dass der Großteil unserer seelischen Antriebe im Unterbewusstsein schlummert.", "现代精神分析学派泰斗西格蒙德·弗洛伊德明确指出：人类绝大多数奔涌咆哮的情感欲望动能，在平日其实深沉潜伏在冰山之下的潜意识深渊。"),
        ("stimulieren", "kein", "Verb", "stimulierte, stimuliert", "刺激神经元，激发兴奋", "Transkranielle Magnetstimulation kann gezielt spezifische Areale der Großhirnrinde stimulieren.", "前沿无创经颅磁刺激物理疗法能够以非侵入方式极其精准地靶向激活并刺激大脑特定功能皮质靶区的神经元兴奋性。"),
        ("inhibieren", "kein", "Verb", "inhibierte, inhibiert", "抑制，阻遏活性", "Bestimmte hemmende Botenstoffe wie GABA inhibieren die Reizübertragung im zentralen Nervensystem.", "中枢神经系统内由神经元分泌释放的伽马氨基丁酸等典型抑制性神经递质，能够强力阻遏并平息神经电冲动的过度放电。"),
        ("konditionieren", "kein", "Verb", "konditionierte, konditioniert", "条件反射训练，驯化", "Pawlows berühmte Hundeexperimente zeigten, wie man Tiere auf akustische Reize konditionieren kann.", "俄国生理学家巴甫洛夫名垂青史的经典犬类实验，极其直观生动地向世人揭示了如何借助特定节拍声响建立坚不可摧的条件反射。"),
        ("reflektieren", "kein", "Verb", "reflektierte, reflektiert", "深度反思，映射 (über)", "Wer weise handeln will, muss vor jedem folgenschweren Schritt über die Konsequenzen reflektieren.", "任何渴望在错综复杂的世事中做出明智决断的智者，在迈出牵一发动全身的关键步伐前，都必须对全部潜在次生后果展开彻夜深度反思。"),
        ("wahrnehmen", "kein", "Verb", "nahm wahr, wahrgenommen", "感知，洞悉察觉", "Menschen nehmen ihre Umwelt durch eine hochgradig subjektive und selektive kognitive Brille wahr.", "世间凡夫俗子在打量周遭大千世界时，无时无刻不在透过一副由自身成长经历与固有认知高度局限所铸造的主观选择性有色眼镜。"),
        ("internalisieren", "kein", "Verb", "internalisierte, internalisiert", "内化为自身信念", "Kinder internalisieren gesellschaftliche Normen und elterliche Wertmaßstäbe im Zuge der Sozialisation.", "稚嫩的孩子在漫长潜移默化的社会化与家风熏陶进程中，不知不觉将主流社会伦理规范与父母言传身教的道德尺度彻底内化于心。"),
        ("projizieren", "kein", "Verb", "projizierte, projiziert", "投射，转嫁心理 (auf)", "Es ist ein weit verbreiteter seelischer Abwehrmechanismus, eigene innere Ängste auf andere zu projizieren.", "在面对内心的自卑与无端恐惧时，人类极其普遍本能地会激活一种精神防御机制：即毫不客气地将自己的一切负面情绪投射转嫁到他人头上。"),
        ("rationalisieren", "kein", "Verb", "rationalisierte, rationalisiert", "合理化伪饰，强辩", "Um Schuldgefühle zu ersticken, versuchte der Täter seine verwerfliche Tat krampfhaft zu rationalisieren.", "为了强行掐灭内心良知深处如影随形的负罪愧疚折磨，凶手甚至在法庭上面对确凿铁证仍处心积虑妄图对自己人神共愤的恶行进行狡辩洗白。"),
        ("kompensieren", "kein", "Verb", "kompensierte, kompensiert", "代偿，弥补心理失落", "Er versuchte, seine quälenden beruflichen Misserfolge durch hemmungslosen Konsumrausch zu kompensieren.", "为了疯狂填补自己因职场接连遭受致命惨败而支离破碎的脆弱自尊心，他一度走上了企图依靠挥金如土的报复性疯狂消费来麻醉自我的不归路。"),
        ("reagieren", "kein", "Verb", "reagierte, reagiert", "应激反应，做出回馈 (auf)", "Das vegetative Nervensystem reagiert bei akutem Stress binnen Bruchteilen einer Sekunde mit Herzrasen.", "在突遭泰山崩覆般的急性危机应激刺激时，机体交感神经系统会在千分之一秒内拉响战斗戒备，诱发心率爆表与血压骤升。"),
        ("kognitiv", "kein", "Adjektiv", "-", "认知维度的", "Kognitive Verhaltenstherapie zählt weltweit zu den wissenschaftlich am besten belegten psychotherapeutischen Methoden.", "聚焦于重构不合理认知信念与重塑应对模式的认知行为疗法(CBT)，被公认为国际循证效度最高、治愈确定性最强的金标准心理治疗体系。"),
        ("neuronal", "kein", "Adjektiv", "-", "神经元的，神经回路的", "Moderne Bildgebungsverfahren machen komplexe neuronale Aktivitätsmuster im lebenden Gehirn sichtbar.", "尖端功能性磁共振成像与正电子发射计算机断层显像技术，让活体人脑在进行深层抽象思辨时的复杂微观神经元放电图谱历历在目。"),
        ("sensorisch", "kein", "Adjektiv", "-", "感官感觉的", "Sensorische Reizüberflutung in modernen Metropolen führt bei vielen sensiblen Menschen zu chronischer Erschöpfung.", "在光怪陆离、霓虹闪烁的超大型现代不夜城都市中，日夜无休止轰炸的感官刺激过载正成为诱发当代高敏感人群慢性精神衰竭的元凶。"),
        ("emotional", "kein", "Adjektiv", "-", "情感充沛的，情绪层面的", "Emotionale Intelligenz ist für eine erfolgreiche Personalführung mindestens ebenso entscheidend wie fachliche Brillanz.", "在锻造卓越非凡的现代团队领导力征途上，懂得体察人心、善解人意的情商魅力，其定海神针般的分量丝毫不逊色于硬核技术才华。"),
        ("subjektiv", "kein", "Adjektiv", "-", "主观体验的", "Schmerz ist ein zutiefst subjektives Phänomen, das sich mit starren Skalen nur unvollständig quantifizieren lässt.", "躯体与心灵所承受的剧痛从来都是一种极具个体异质性的深层主观体验，单单依靠刻板冷酷的数字量表绝对无法完整衡量其痛苦广度。"),
        ("intuitiv", "kein", "Adjektiv", "-", "直觉敏锐的，凭借灵感的", "Eine intuitive Benutzeroberfläche ermöglicht auch technischen Laien eine spielend leichte Bedienung der Software.", "完全遵循人类本能认知心理学构建的极简直觉式图形人机交互界面，即便让毫无编程基础的科技小白也能在一分钟内行云流水般上手驾驭。"),
        ("instinktiv", "kein", "Adjektiv", "-", "出于本能冲动的", "Die Mutter riss ihr Kind instinktiv von der Straße, Sekunden bevor der Lastwagen vorbeiraste.", "就在失控重型泥头卡车如狂暴巨兽般贴身呼啸擦过的千钧一发刹那，伟大的母亲完全出于骨肉母爱本能一把将幼子拽入怀中。"),
        ("plastisch", "kein", "Adjektiv", "-", "具备微观可塑性的", "Dank plastischer Gehirnstrukturen können Schlaganfallpatienten verlorene motorische Fähigkeiten mühsam wiedererlernen.", "得益于人脑神经元结构在创伤后所展现出的顽强代偿与微观神经可塑性，脑梗死偏瘫患者通过大剂量康复训练仍能重获肢体运动功能。"),
        ("bewusst", "kein", "Adjektiv", "-", "清醒自觉的，蓄意的", "Wir müssen lernen, bewusste Pausen in unseren extrem durchgetakteten, hektischen Alltag einzubauen.", "在当今这个被各项考勤打卡与KPI日程表催逼得近乎喘不过气来的狂飙内卷时代，我们必须学会有意识地给自己按下暂停键。"),
        ("unbewusst", "kein", "Adjektiv", "-", "潜意识中发生的，下意识的", "Viele tief sitzende Ängste steuern unser tägliches Beziehungsverhalten auf vollkommen unbewusste Weise.", "许多深植于童年原生家庭缺憾深处的心灵阴影，往往在成年后以完全不为人知的潜意识幽灵姿态暗中操弄着我们在亲密关系中的一举一动。"),
        ("dissonant", "kein", "Adjektiv", "-", "不和谐的，失调矛盾的", "Dissonante Gedanken über den eigenen Lebensstil erzeugen inneren seelischen Stress.", "内心深处关于自身苟且生活现状的巨大失调反思与道德谴责，在午夜梦回时分会酿成折磨人心的沉重精神应激风暴。"),
        ("rational", "kein", "Adjektiv", "-", "高度理性冷静的", "Ein rationaler Geist lässt sich auch im Auge des heftigsten Shitstorms nicht zu unbedachten Kurzschlusshandlungen hinreißen.", "一位心如止水、真正具备钢铁般绝对理性定力的顶级操盘手，即便身处全网舆论狂风暴雨的暴风眼核心，亦绝不会被煽动做出失去理智的短视宣泄。"),
        ("empirisch", "kein", "Adjektiv", "-", "实证可检验的", "Die kognitive Psychologie liefert empirisch überprüfbare Modelle über die Gesetzmäßigkeiten des menschlichen Denkens.", "现代实证认知心理科学拒绝空洞苍白的玄学揣测，始终致力于输出具备严密实验数据支撑、在全球范围内可被反复检验的科学心智规律模型。"),
        ("vulnerabel", "kein", "Adjektiv", "-", "心灵脆弱易感的", "Jugendliche in der sensiblen Umbauphase der Pubertät sind für psychische Störungen besonders vulnerabel.", "正处于大脑神经元突触大规模二次修剪重塑与荷尔蒙激荡青春期的懵懂少男少女，在遭遇校园霸凌时在心理防线上显得格外脆弱易折。"),
        ("resilient", "kein", "Adjektiv", "-", "内心极度抗压强大的", "Resiliente Persönlichkeiten betrachten schwere Rückschläge nicht als Endstation, sondern als willkommene Lektionen.", "真正内心强大到骨子里的高抗逆韧性智者，从不把人生旅途中遭遇的任何灭顶之灾视为末日终点，而是将其坦然视作磨砺灵魂的宝贵淬火磨刀石。"),
        ("hypnotisch", "kein", "Adjektiv", "-", "如催眠般的，令人神往的", "Die monotone Melodie des Meeresrauschens übte eine zutiefst beruhigende, fast hypnotische Wirkung auf ihn aus.", "太平洋岸边那永不停歇、日夜拍岸的单调海浪潮汐声，仿佛带着一种神秘的东方催眠魔力，瞬间彻底抚平了他紧绷已久的躁动心绪。"),
        ("präventiv", "kein", "Adjektiv", "-", "防微杜渐预防性的", "Präventives Achtsamkeitstraining am Arbeitsplatz beugt dem schleichenden Entstehen schwerer Burnout-Syndrome vor.", "在全公司范围内由工会出资常态化普及推广前瞻性正念减压干预工坊，能够将职业枯竭综合征扼杀在萌芽破土之前。"),
        ("suggestiv", "kein", "Adjektiv", "-", "极具诱导性心理暗示的", "Der Staatsanwalt rügte die suggestive Fragestellung des Zeugenvernehmers als verfahrensrechtlich unzulässig.", "国家公诉人在法庭上拍案而起，当庭依法对侦查取证人员在笔录询问中带有强烈诱导性心理暗示的诱供提问提出程序违法严重抗议。"),
        ("selektiv", "kein", "Adjektiv", "-", "选择性过滤的", "Selektive Wahrnehmung führt dazu, dass Menschen nur diejenigen Fakten wahrnehmen, die ihr Weltbild bestätigen.", "人性深处的选择性记忆与感知偏误往往会让人变成睁眼瞎：即下意识只过滤吸收那些能够迎合自身固有认知偏见的碎片信息。"),
        ("innovativ", "kein", "Adjektiv", "-", "革故鼎新引领潮流的", "Innovative Schnittstellen zwischen menschlichem Gehirn und Computer (BCI) eröffnen Gelähmten völlig neue Lebenswelten.", "将人类大脑生物电信号与外部硅基计算机直接跨界相连的前沿侵入式脑机接口革命，正为高位截瘫残障人士彻底打开通往赛博重生世界的崭新大门。")
    ]
}

# LESSON 8: Globale Klimapolitik & Biodiversität (70 words)
L08 = {
    "id": "B2_L08",
    "title": "第8课：全球气候治理、生物多样性与生态临界点 (Globale Klimapolitik)",
    "summary": "掌握二重连词 (Zweiteilige Konnektoren) 进阶运用、生态多米诺骨牌效应与全球绿色低碳治理大纲词汇",
    "grammar": {
        "title": "二重连词体系 (Zweiteilige Konnektoren in Argumentation)",
        "sections": [
            {
                "heading": "1. 表示并列与递进：",
                "content": "• sowohl ... als auch ... (既……又……)\n• nicht nur ..., sondern auch ... (不仅……而且……)\n• weder ... noch ... (既不……也不……，否定并列)"
            },
            {
                "heading": "2. 表示转折、让步与比例关系：",
                "content": "• zwar ..., aber ... (虽然……但是……)\n• einerseits ..., andererseits ... (一方面……另一方面……)\n• je + 比较级 (从句尾动词), desto / umso + 比较级 (主句反转动词在第二位): Je wärmer die Ozeane werden, desto zerstörerischer wüten die Hurrikans."
            }
        ]
    },
    "quiz": [
        {
            "id": "B2_L08_Q1",
            "type": "GRAMMAR_FILL",
            "question": "Je schneller die Permafrostböden auftauen, ______ (desto mehr / desto / umso schneller) Methan wird freigesetzt.",
            "options": ["desto mehr", "desto", "umso schneller", "weil mehr"],
            "correctIndex": 0,
            "explanation": "je + 比较级 ..., desto + 比较级 ...: desto mehr Methan wird freigesetzt。"
        },
        {
            "id": "B2_L08_Q2",
            "type": "MEANING_SELECT",
            "question": "“der Kipppunkt” 在全球气候动力学系统中的科学含义是：",
            "options": ["不可逆生态崩溃临界点", "全球碳排放峰值年", "海洋潮汐最低点", "极地科考补给站"],
            "correctIndex": 0,
            "explanation": "der Kipppunkt (tipping point) 指气候系统一旦被突破即触发不可逆连锁崩溃的“临界点”。"
        },
        {
            "id": "B2_L08_Q3",
            "type": "GRAMMAR_FILL",
            "question": "Die Industriestaaten müssen ______ (nicht nur) die Emissionen senken, sondern auch Entwicklungsländer finanziell unterstützen.",
            "options": ["nicht nur", "sowohl", "weder", "zwar"],
            "correctIndex": 0,
            "explanation": "固定递进搭配：nicht nur ..., sondern auch ... (不仅……而且……)。"
        },
        {
            "id": "B2_L08_Q4",
            "type": "LISTENING_MCQ",
            "question": "“Das Überschreiten planetarer Belastungsgrenzen gefährdet die Existenz künftiger Generationen.” 的主旨是：",
            "options": ["突破地球生态承载极限将危及未来子孙后代的生存基石。", "地球承载力是无限的。", "只要开发新技术，资源消耗就无关紧要。", "人口增长不会对生态造成影响。"],
            "correctIndex": 0,
            "explanation": "planetare Belastungsgrenzen = 地球极限承载边界，gefährdet die Existenz = 危及生存。"
        },
        {
            "id": "B2_L08_Q5",
            "type": "SENTENCE_BUILDER",
            "question": "重组气候治理多边公约核心论点：“schützt / Ein ambitioniertes internationales Abkommen / die Artenvielfalt / weltweit”",
            "options": ["Ein ambitioniertes internationales Abkommen schützt die Artenvielfalt weltweit.", "Weltweit ein ambitioniertes internationales Abkommen die Artenvielfalt schützt.", "Die Artenvielfalt schützt weltweit ein Abkommen internationales ambitioniertes nicht.", "Schützt ein ambitioniertes internationales Abkommen die Artenvielfalt weltweit."],
            "correctIndex": 0,
            "explanation": "主语 (Ein ambitioniertes internationales Abkommen) + 谓语 (schützt) + 宾语 (die Artenvielfalt) + 状语 (weltweit)。"
        }
    ],
    "words": [
        ("das Klima", "das", "Nomen", "-s", "气候，大气候", "Das globale Klima erwärmt sich infolge anthropogener Treibhausgasemissionen drastisch.", "在人类工业活动温室气体排放狂飙的驱动下，全球整体气候正在经历剧烈而危险的非线性升温。"),
        ("die Atmosphäre", "die", "Nomen", "unz.", "大气层，大气环境", "Die Konzentration von Kohlendioxid in der Erdatmosphäre hat Rekordwerte erreicht.", "地球外层大气圈层内部所截留的二氧化碳摩尔浓度已彻底飙升至数百万年未见的灾难性峰值。"),
        ("das Treibhausgas", "das", "Nomen", "-e", "温室气体", "Methan ist ein kurzlebiges, aber ungleich potenteres Treibhausgas als Kohlendioxid.", "甲烷虽然在大气中的化学半衰期较为短暂，但其单分子温室保温绝热效应却比二氧化碳凶猛数十倍。"),
        ("die Erderwärmung", "die", "Nomen", "unz.", "全球变暖", "Die Begrenzung der globalen Erderwärmung auf 1,5 Grad erfordert radikale Dekarbonisierung.", "想要将全球变暖终极中枢控制在相较于工业化前不超过1.5摄氏度的生死线上，必须掀起触及全产业命脉的激进脱碳风暴。"),
        ("die Dekarbonisierung", "die", "Nomen", "unz.", "去碳化，脱碳转型", "Die vollständige Dekarbonisierung der Schwerindustrie erfordert gewaltige Mengen an grünem Wasserstoff.", "想要对特种钢铁治炼与重型水泥化肥等重化工业基本盘实施彻底脱碳，需要以海量清洁绿氢作为工业还原剂。"),
        ("der Kipppunkt", "der", "Nomen", "-e", "气候系统不可逆临界点", "Beim Überschreiten eines Kipppunkts droht ein unaufhaltsamer Dominoeffekt im Erdsystem.", "气候系统多米诺骨牌内部一旦有哪怕任何一个关键临界点被强行冲破，势必触发全系统不可逆转的自加速连锁崩塌浩劫。"),
        ("der Permafrost", "der", "Nomen", "unz.", "永久冻土层", "Das Auftauen sibirischer Permafrostböden setzt gigantische Mengen konservierten Methans frei.", "西伯利亚与北极圈广袤永久冻土带的加速融化解冻，正在向大气中肆虐释放封印沉睡了千万年之久的巨量易燃甲烷地雷。"),
        ("der Gletscher", "der", "Nomen", "-", "高山冰川", "Die Alpengletscher verlieren Jahr für Jahr dramatisch an Masse und Dicke.", "阿尔卑斯山脉连绵起伏的高原冰川群落，在炎炎酷暑之下正以令人肉眼可见的骇人速度经历着雪崩般的体积与厚度萎缩。"),
        ("der Meeresspiegel", "der", "Nomen", "unz.", "海平面", "Der Anstieg des Meeresspiegels bedroht die schiere Existenz tief liegender Inselstaaten.", "两极冰盖消融导致的海平面持续加速抬升，正直接将若干地势低洼的南太平洋岛屿国家的存续彻底推向沉入汪洋的深渊。"),
        ("die Dürre", "die", "Nomen", "-n", "干旱，旱灾", "Verheerende Dürreperioden vernichten Ernten und verschärfen den Hunger in der Sahelzone.", "连续数年干旱无雨的百年不遇大旱酷刑，不仅让原本贫瘠的农田颗粒无收，更在非洲萨赫勒地带掀起了触目惊心的大饥荒浪潮。"),
        ("die Flut", "die", "Nomen", "-en", "特大洪涝，洪水", "Sintflutartige Regenfälle lösten im Ahrtal eine historische Flutkatastrophe aus.", "百年一遇的极端短时强对流暴雨在德国阿尔河谷盆地引发了一场载入史册、冲毁无数家园的特大洪水泥石流惨剧。"),
        ("die Katastrophe", "die", "Nomen", "-n", "生态浩劫，特大灾难", "Wissenschaftler warnen vor einer humanitären Katastrophe ungeahnten Ausmaßes.", "联合国跨政府气候专门委员会权威科学家反复发出最严厉的末日预警：谨防人类面临一场史无前例的全球人道主义总灾难。"),
        ("die Biodiversität", "die", "Nomen", "unz.", "生物多样性", "Der rapide Verlust an Biodiversität bedroht die Stabilität globaler Ökosysteme fundamental.", "全球范围内动植物物种遗传基因库与生物多样性的雪崩式灭绝，正在从地基层面动摇整个地球生命维持系统的根本稳态。"),
        ("das Artensterben", "das", "Nomen", "unz.", "物种灭绝狂潮", "Das aktuelle sechste Massen-Artensterben wird primär durch menschliche Landnutzung verursacht.", "地质年代史上正在上演的第六次地球生命大灭绝惨剧，其幕后最大罪魁祸首正是人类对自然森林湿地肆无忌惮的开垦蚕食。"),
        ("das Ökosystem", "das", "Nomen", "-e", "生态系统", "Tropische Regenwälder sind hochkomplexe Ökosysteme von unschätzbarem ökologischem Wert.", "被誉为“地球之肺”的热带雨林构成了微观结构极度精妙复杂的庞大生态群落，蕴含着无可估量的全球气候调节生态价值。"),
        ("der Lebensraum", "der", "Nomen", "-e", "生境，栖息地", "Die Rodung der Urwälder raubt zahllosen bedrohten Tierarten ihren natürlichen Lebensraum.", "对原始热带雨林展开灭绝式大面积商业采伐，生生剥夺了数以万计受保护濒危珍稀野生动植物赖以繁衍生息的天然家园。"),
        ("die Entwaldung", "die", "Nomen", "unz.", "森林滥伐，毁林", "Die illegale Entwaldung des Amazonasbeckens schreitet trotz internationaler Proteste voran.", "尽管遭到国际环保公义力量的强烈抗议与谴责，巴西亚马孙河流域的非法滥砍滥伐毁林恶行依然在贪婪资本驱使下暗中肆虐。"),
        ("die Aufforstung", "die", "Nomen", "-en", "植树造林，生态复绿", "Großflächige Aufforstungsprojekte binden Kohlenstoff und stoppen die fortschreitende Wüstenbildung.", "在干旱半干旱风沙前沿开展大规模集中连片人工植树造林国家防线工程，能够封存巨量活性碳汇并彻底筑牢阻遏土地荒漠化的绿色长城。"),
        ("die Wüste", "die", "Nomen", "-n", "荒漠，沙漠", "Die Ausbreitung von Wüsten bedroht die fruchtbaren Böden ganzer Kontinente.", "沙漠化风沙前沿以每年数千米的速度野蛮扩张，正在将各大洲成片肥沃平原良田彻底吞噬蚕食为寸草不生的生命绝境。"),
        ("die Erosion", "die", "Nomen", "-en", "水土流失，风蚀剥蚀", "Intensive Monokulturen ohne Fruchtfolge beschleunigen die verheerende Bodenerosion.", "脱离自然农耕规律、不搞作物轮作的掠夺性单一化密集大农场耕作，正在不可阻挡地加速导致全球顶级黑土层遭遇毁灭性水土流失。"),
        ("die Renaturierung", "die", "Nomen", "-en", "生态再自然化，退耕还湖还林", "Die Renaturierung von Mooren und Flussauen reaktiviert riesige natürliche Kohlenstoffspeicher.", "全面推行退耕还湿、退田还湖与泥炭沼泽湿地生态再自然化修复工程，能够重新唤醒沉睡在欧罗巴大地上巨大的天然二氧化碳超级海绵。"),
        ("das Moor", "das", "Nomen", "-e", "泥炭沼泽湿地", "Intakte Moore speichern pro Hektar mehr Kohlenstoff als alle Wälder der Erde zusammen.", "保存完好无损的原始泥炭沼泽湿地每公顷所能牢牢封锁固化的碳储量，竟然远超同等面积下地球上任何茂密热带温带原始森林的总和。"),
        ("die Korallenbleiche", "die", "Nomen", "-n", "珊瑚礁白化，珊瑚大面积死亡", "Die Erwärmung der Weltmeere führt zur katastrophalen Korallenbleiche am Great Barrier Reef.", "海水水温异常持续偏高所酿成的大规模海洋热浪，正在导致澳大利亚大堡礁等举世闻名的海底珊瑚礁王国遭遇灭绝性的全面白化死亡。"),
        ("die Versauerung", "die", "Nomen", "unz.", "海洋酸化", "Die Versauerung der Ozeane gefährdet Meeresorganismen mit kalkhaltigen Schalen.", "海水吸收过量人为二氧化碳所诱发的表层海水化学酸化灾难，正在残酷溶蚀并扼杀微小浮游生物与贝类甲壳纲动物的钙质外骨骼外壳。"),
        ("der Fußabdruck", "der", "Nomen", "-e", "碳足迹 (ökologischer Fußabdruck)", "Jeder Konsument kann seinen ökologischen Fußabdruck durch bewusste Ernährung verkleinern.", "每一位对地球未来心存敬畏的现代消费者，完全能够通过主动拥抱植物基膳食与低碳绿色消费来大幅压减自身的个人生态足迹。"),
        ("die Klimaneutralität", "die", "Nomen", "unz.", "碳中和，气候中和", "Deutschland hat sich gesetzlich verpflichtet, bis zum Jahr 2045 vollkommene Klimaneutralität zu erreichen.", "德意志联邦共和国已通过联邦立法庄严宣告：全国上下誓要在2045年之前实现净零温室气体排放的全面碳中和宏伟目标。"),
        ("die Energiewende", "die", "Nomen", "unz.", "新能源转型革命", "Der zügige Ausbau von Wind- und Solarenergie ist das Herzstück der deutschen Energiewende.", "坚定不移、开足马力全面加速风力发电与分布式光伏矩阵的装机投产，是支撑德国新能源绿色转型战略的最核心命脉支柱。"),
        ("die Fotovoltaik", "die", "Nomen", "unz.", "太阳能光伏发电", "Auf den Dächern von Privathäusern boomt die Installation moderner Fotovoltaikanlagen.", "在成千上万普通家庭的独立式屋顶上，先进高效、光电转换率极高的分布式太阳能光伏面板正迎来井喷式爆发安装浪潮。"),
        ("die Windkraft", "die", "Nomen", "unz.", "风力发电，风能", "Offshore-Windparks auf hoher See liefern gewaltige Mengen verlässlichen Ökostroms.", "耸立在惊涛骇浪深远海之上的巨型海上风电场群落，日夜不停为内陆高耗能产业园区输送着源源不断、清洁可靠的巨量零碳绿色电力。"),
        ("das Geothermie", "die", "Nomen", "unz.", "深层地热能 (die Geothermie)", "Tiefengeothermie bietet großes Potenzial für eine klimaneutrale städtische Fernwärmeversorgung.", "开发埋藏在地心深处的深层高温干热岩地热能，为北方各大重镇彻底实现冬季集中城市供暖管网的百分之百无煤脱碳展现了无限可能。"),
        ("die Kernfusion", "die", "Nomen", "unz.", "可控核聚变", "Die Kernfusion gilt als der Heilige Gral einer sauberen und unerschöpflichen Energiequelle.", "被全球科学家梦寐以求的可控人造太阳核聚变物理学突破，被公认为人类彻底终结能量危机、迈向星际文明的无尽终极圣杯。"),
        ("das Endlager", "das", "Nomen", "-", "高放射性核废料永久深地质处置库", "Die jahrzehntelange Suche nach einem sicheren nuklearen Endlager spaltet Politik und Bevölkerung.", "针对如何为遗留的高放射性剧毒核电乏燃料废料寻觅一处能够固若金汤隔绝十万年的安全永久深地质处置库，朝野政坛与民意持续剧烈割裂撕扯。"),
        ("die Ressource", "die", "Nomen", "-n", "自然资源，原料储备", "Endliche fossile Ressourcen wie Kohle und Erdöl müssen im Erdreich verbleiben.", "大自然馈赠给人类的煤炭与原油等不可再生化石能源总储量极其有限，人类必须克制贪婪本能，将它们永久封存在地底深渊。"),
        ("die Kreislaufwirtschaft", "die", "Nomen", "unz.", "循环经济", "In einer echten Kreislaufwirtschaft werden alle Abfälle als wertvolle Sekundärrohstoffe wiederverwertet.", "在真正闭环运转的极致现代循环经济体系中，一切被丢弃的城市废弃物均将被百炼成钢，作为高净值二次再生原材料实现全循环再利用。"),
        ("das Recycling", "das", "Nomen", "unz.", "物资循环回收利用", "Fortschrittliches chemisches Recycling ermöglicht die Wiederaufbereitung gemischter Plastikabfälle.", "突破传统物理粉碎局限的顶尖热解催化化学回收技术，让成分杂乱难分的大宗生活混杂废旧塑料实现了高附加值的分子级解聚回炉重生。"),
        ("die Deponie", "die", "Nomen", "-n", "垃圾填埋场", "Auf modernen Deponien wird austretendes Deponiegas zur umweltfreundlichen Stromerzeugung genutzt.", "在达标防渗的高科技现代化垃圾卫生填埋场上，底部逸散发酵生成的有毒填埋沼气被全封闭收集引流，用于清洁热电联产发电。"),
        ("die Verschmutzung", "die", "Nomen", "-en", "环境污染，水体污染", "Mikroplastik in den Ozeanen ist eine unsichtbare, aber tödliche Verschmutzung der Nahrungskette.", "在浩瀚全球大洋深处无所不在游弋漂浮的微塑料纳米颗粒，已成为暗中悄无声息毒化整条海洋生物食物链的致命幽灵污染物。"),
        ("der Schadstoff", "der", "Nomen", "-e", "有害物质，空气污染物", "Feinstaub und Stickoxide gehören zu den gefährlichsten Schadstoffen in städtischen Ballungsräumen.", "可吸入超细颗粒物与高毒性氮氧化物，并列为现代重工业密集型城市大都市圈内威胁千百万市民呼吸系统健康的最危险头号有害污染物。"),
        ("die Grenzwerte", "die", "Nomen (Pl.)", "Pl.", "法定环保排放限量指标 (der Grenzwert, -e)", "Die Europäische Union verschärfte die Grenzwerte für industrielle Abgasemissionen signifikant.", "欧洲联盟环境保护委员会大刀阔斧正式出台新政，极其显著地下调收紧了针对全欧大型工业化工厂废气烟尘排放的法定限值红线。"),
        ("das Umweltabkommen", "das", "Nomen", "-", "国际多边环境保护公约", "Das Montrealer Umweltabkommen verhinderte die vollständige Zerstörung der lebenswichtigen Ozonschicht.", "三十多年前由全球主要大国联袂庄严签署的《蒙特利尔议定书》，在悬崖勒马之际挽救了为整个地球生命阻挡宇宙致命紫外线侵袭的臭氧层。"),
        ("emittieren", "kein", "Verb", "emittierte, emittiert", "排放废气温室气体", "Große Kohlekraftwerke emittieren jedes Jahr Abermillionen Tonnen klimaschädliches CO2 in die Luft.", "单座超大规模的老旧燃煤火力发电厂每年向蔚蓝的大气层肆意吞云吐雾，直接倾泻喷吐出高达数以千万吨计的严重破坏气候平衡的碳废气。"),
        ("reduzieren", "kein", "Verb", "reduzierte, reduziert", "削减，大幅压缩", "Bis 2030 müssen die Industriestaaten ihre nationalen Emissionen um mindestens 55 Prozent reduzieren.", "到2030年这一严峻倒逼时间节点，全球主要传统工业化发达国家必须无条件将其年度综合碳排放基准总量大砍至少55%以上。"),
        ("kompensieren", "kein", "Verb", "kompensierte, kompensiert", "碳抵消，对冲中和", "Fluggäste können die CO2-Emissionen ihrer Fernflüge durch zertifizierte Klimaschutzprojekte kompensieren.", "搭乘洲际长途越洋民航客机的旅客可以通过自愿出资认购由权威机构认证的造林清洁发展机制项目，在经济账面上对冲抵消此行的碳排放。"),
        ("verschmutzen", "kein", "Verb", "verschmutzte, verschmutzt", "污染江河大地", "Gefährliche Industrieabwässer dürfen nicht unbehandelt die natürlichen Flussläufe verschmutzen.", "任何含有重金属毒素与致癌化学残留的危险工业生产废水，绝对不可未经无害化深度生化处理便擅自偷排至天然江河湖泊污染水源。"),
        ("zerstören", "kein", "Verb", "zerstörte, zerstört", "摧毁，破坏生态", "Unkontrollierte Flächenversiegelung für Straßen und Gewerbegebiete zerstört wertvollen Ackerboden.", "为了修建高速路网与盲目铺摊子拓建工业园区而肆意推行的水泥大硬化，正在毁灭性剥夺本已极其紧缺珍贵的高标准农田黑土地。"),
        ("bedrohen", "kein", "Verb", "bedrohte, bedroht", "威胁生态安全", "Eingeschleppte invasive Tier- und Pflanzenarten bedrohen das empfindliche Gleichgewicht einheimischer Biotope.", "随跨国航运压舱水与国际贸易无序入侵的境外恶性外来物种，正以前所未有的凶残态势严重威胁并霸凌本土脆弱生境的生态平衡。"),
        ("schonen", "kein", "Verb", "schonte, geschont", "爱护，珍惜利用", "Wir müssen die verbleibenden natürlichen Ressourcen unseres Heimatplaneten maximal schonen.", "面对已经满目疮痍、不堪重负的这颗蔚蓝色脆弱家园母星，我们这代人唯有竭尽全副心力、最大限度地倍加珍惜爱护残存的自然造化。"),
        ("überfischen", "kein", "Verb", "überfischte, überfischt", "过度捕捞掠夺", "Riesige Fangflotten mit zerstörerischen Grundschleppnetzen haben die Weltmeere drastisch überfischt.", "装备着毁灭性海底深海拖网的大型现代化远洋钢铁捕捞船队肆无忌惮地连窝端洗劫，已将公海全球各大主力传统渔场的渔业资源彻底逼入枯竭境地。"),
        ("versickern", "kein", "Verb", "versickerte, versickert", "渗入地下水脉", "Regenwasser sollte nach Möglichkeit vor Ort im Erdreich versickern, anstatt in die Kanalisation zu fließen.", "在海绵城市生态规划设计中，纯净的天然雨水应当尽可能就地垂直渗透补给地下含水层，而非被白白当作废水排入市政雨水管网。"),
        ("austrocknen", "kein", "Verb", "trocknete aus, ausgetrocknet", "彻底干涸干裂", "Wegen anhaltender Hitzewellen trockneten historische Wasserstraßen und Flüsse in Europa bedrohlich aus.", "在接二连三创纪录高温热浪的持续炙烤下，包括莱茵河与多瑙河在内的多条欧洲历史母亲河与黄金水运大动脉局部航段竟出现了触目惊心的断流干涸。"),
        ("ökologisch", "kein", "Adjektiv", "-", "生态文明维度的", "Ökologisches Bauen mit nachwachsendem Holz verringert den energetischen Aufwand im Gebäudesektor.", "在现代民用与商业建筑营造中大力推广采用全生命周期固碳的绿色工程木材，能够大幅拉低整个高能耗建材建筑行业的隐形能耗基准。"),
        ("nachhaltig", "kein", "Adjektiv", "-", "可持续长久的", "Eine nachhaltige Bewirtschaftung der Forste entnimmt dem Wald niemals mehr Holz als parallel nachwächst.", "源自德意志林业古训的现代可持续森林集约化经营法则是铁律：即每年采伐的外运木材总量绝不允许超出林场年新生蓄积量的客观上限。"),
        ("erneuerbar", "kein", "Adjektiv", "-", "可再生的，源源不绝的", "Erneuerbare Energieträger sind der unersetzliche Schlüssel für eine saubere, krisensichere Energieversorgung.", "太阳能、风能与水力地热等取之不尽用之不竭的清洁可再生二次能源，构成了全人类彻底摆脱地缘油气勒索的最坚固金钟罩铁布衫。"),
        ("klimaneutral", "kein", "Adjektiv", "-", "净零碳排放的", "Moderne Vorzeigestädte streben an, ihren gesamten Nahverkehr bis zum Ende des Jahrzehnts klimaneutral umzustellen.", "站在时代弄潮儿潮头的全球顶尖绿色典范标杆城市，正誓言在当前这十年之内将其全域城市公共交通工具全部置换为零排放纯电驱动。"),
        ("katastrophal", "kein", "Adjektiv", "-", "毁灭性的，灾难性的", "Ein Zusammenbruch der atlantischen Meeresströmungen hätte katastrophale Folgen für das Weltklima.", "全球海洋学家经过严密超级计算机流体力学推演给出警告：北大西洋大洋环流传送带一旦彻底熄火骤停，将给全球文明带来灭绝级毁灭打击。"),
        ("irreversibel", "kein", "Adjektiv", "-", "不可逆转的", "Das großflächige Abschmelzen des antarktischen Eisschildes gilt ab einer gewissen Schwelle als irreversibel.", "南极大陆绵延数千公里的庞大陆架永久巨型冰川冰盖，一旦跨过某一临界温度触发点，其全面坍塌消融在物理力学上将变得无可逆转。"),
        ("absehbar", "kein", "Adjektiv", "-", "肉眼可见不久的，可预见的", "In absehbarer Zeit werden extreme Wetterereignisse wie Wirbelstürme und Starkregen dramatisch zunehmen.", "在清晰可预见的肉眼可见未来数十年内，诸如超强台风、毁灭性龙卷风与特大极值暴雨等超级极端气象异象的发生频次与破坏烈度将呈指数级剧增。"),
        ("substanziell", "kein", "Adjektiv", "-", "实质性的，举足轻重的", "Ohne substanzielle finanzielle Hilfen der Industrienationen können Entwicklungsländer den Klimaschutz nicht stemmen.", "若没有传统高污染工业化富裕国在联合国框架下向全球南方贫困国提供真金白银的实质性专项气候援助基金，全球应对气候变暖的崇高大计注定沦为空谈。"),
        ("biodivers", "kein", "Adjektiv", "-", "物种繁茂多样的", "Uralte Naturwälder und unberührte Urwälder sind ungleich biodiverser als forstwirtschaftliche Fichtenmonokulturen.", "历经数千年自然演替而成的原始蛮荒自然阔叶林，相较于人类出于单一快速经济利益考量而人工栽植的整齐划一单一人工针叶林，展现出百倍丰富的繁茂生物多样性。"),
        ("anthropogen", "kein", "Adjektiv", "-", "由人类活动诱发造成的", "Der wissenschaftliche Konsens darüber, dass der Klimawandel primär anthropogen bedingt ist, liegt bei nahezu 100 Prozent.", "全人类国际顶级学术同行评审期刊上白纸黑字形成的终极压倒性科学共识坚如磐石：当代全球急剧气候变暖最主要的始作俑者几乎百分之百就是人类自身工业活动。"),
        ("meteorologisch", "kein", "Adjektiv", "-", "气象观测学的", "Meteorologische Langzeitdaten belegen unbestreitbar die dramatische Zunahme tropischer Nächte in Mitteleuropa.", "欧洲各大百年国家气象台站所留存的精密水文观测数据显示：中欧地区夏季夜间最低气温不低于20摄氏度的所谓“热带夜”发生天数在近三十年内呈爆发式直线上扬。"),
        ("reziprok", "kein", "Adjektiv", "-", "倒数的，相互成反比的", "Zwischen globalen Schutzanstrengungen und den kumulierten volkswirtschaftlichen Katastrophenschäden besteht ein reziprokes Verhältnis.", "全人类在源头治本上所舍得倾囊付出的全球气候生态保护专项前瞻性注资力度，与放任气候失控所必然引发的数以万亿计的滞后性超级天灾经济损失之间，呈现出绝对的负相关反比。"),
        ("kumulativ", "kein", "Adjektiv", "-", "累积叠加的", "Die kumulative Wirkung von Treibhausgasen im Ozeansystem bleibt auch nach einem sofortigen Emissionsstopp noch Jahrhunderte spürbar.", "由于大洋深水水体拥有超乎想象的巨大热惯性，即便全人类自下一秒起瞬间让所有烟囱和内燃机排放全部归零，温室气体在大气和海洋中数百年累积沉淀的增温恶果依然将幽灵般持续回荡震荡数百年之久。"),
        ("fragil", "kein", "Adjektiv", "-", "极度娇嫩脆弱的", "Das arktische Ökosystem ist eines der fragilsten und am stärksten bedrohten Refugien auf unserem Planeten.", "被终年积雪覆盖的高纬度北极苔原与极地边缘海冰生态系统，是整个蓝色星球上生命网结构最为脆弱纤细、最经不起任何外部风吹草动折腾的生死濒危避风港。"),
        ("resilient", "kein", "Adjektiv", "-", "具备强悍自我修复韧性的", "Durch natürliche Artenvielfalt stabilisierte Mischwälder sind wesentlich resilienter gegen Schädlinge und Stürme.", "依托乔木灌木草本多物种自然混交而成的健康天然混交林，在面对落叶松毛虫、松皮蠹害虫侵袭以及超级飓风扫荡时，展现出人工单一针叶林望尘莫及的强大自我韧性修复力。"),
        ("effizient", "kein", "Adjektiv", "-", "高能效的，事半功倍的", "Energieeffiziente Dämmung senkt die Heizkosten privater Haushalte massiv und schont die Umwelt.", "选用经严格环保质量认证的高标准气密保温隔热岩棉材料对老旧民房外立面实施节能大改造，不仅能让普通百姓在寒冬腊月的取暖燃气费账单拦腰斩断，更为保护环境立下了大功。"),
        ("autark", "kein", "Adjektiv", "-", "自给自足的，能源独立的", "Mit eigener Solaranlage und Stromspeicher im Keller kann ein Einfamilienhaus energetisch weitgehend autark agieren.", "在自家地下室安装高安全磷酸铁锂家庭储能电箱并配合屋顶大功率光伏电池板，能让一栋独栋别墅在全年绝大多数时段轻松潇洒地摆脱公共电网束缚，实现真正意义上的家庭绿色能源独立自主。"),
        ("radikal", "kein", "Adjektiv", "-", "从根源彻底破局的", "Um das Pariser Klimaziel noch rechtzeitig zu retten, bedarf es eines radikalen Wandels unseres gesamten Wirtschaftssystems.", "为了赶在气候毁灭倒计时沙漏漏尽之前死死捍卫《巴黎协定》生死目标，我们必须拿出刮骨疗毒的铁血魄力，对整个以化石燃料为食粮的传统贪婪资本经济体系掀起一场从最底层根基洗牌的彻底革新变革。"),
        ("dringend", "kein", "Adjektiv", "-", "十万火急迫在眉睫的", "Die Rettung der letzten verbleibenden globalen Urwälder ist eine dringend gebotene historische Pflicht der Gegenwart.", "将散落在这个星球角落里仅存的最后几片原始蛮荒热带雨林从电锯与烈火前完好无损地抢救保留下来，是当代全人类面对后世子孙无论如何也无法推卸、十万火急的崇高历史受托使命。"),
        ("unverzichtbar", "kein", "Adjektiv", "-", "不可或缺的，中流砥柱的", "Der weltweite Ausbau der Schienennetze ist ein unverzichtbarer Baustein einer wahrhaft zukunftsfähigen Verkehrswende.", "在全球各大洲纵横捭阖地大力织密现代化电气化高铁轨道交通路网，是推动全人类出行彻底告别高污染燃油时代、打赢绿色交通绿色转型硬仗最不可或缺、不可动摇的黄金中流砥柱支柱。")
    ]
}

# LESSON 9: Bildungsgerechtigkeit & Soziale Mobilität (70 words)
L09 = {
    "id": "B2_L09",
    "title": "第9课：教育公平、终身学习与社会阶层流动 (Bildungsgerechtigkeit)",
    "summary": "掌握动名词同义转换与介词短语转换 (Präpositionale Fügungen vs. Nebensätze) 与教育社会学词汇",
    "grammar": {
        "title": "从句与介词短语转换 (Verbalstil vs. Nominalstil in Bildung & Soziologie)",
        "sections": [
            {
                "heading": "1. 时间状语从句向介词短语转换：",
                "content": "• Während die Studierenden lernten, ... -> Während des Lernens der Studierenden, ...\n• Nachdem sie das Examen bestanden hatte, ... -> Nach dem Bestehen des Examens ...\n• Sobald das Semester beginnt, ... -> Bei Beginn des Semesters ..."
            },
            {
                "heading": "2. 条件与让步从句向介词短语转换：",
                "content": "• Wenn man sich anstrengt, ... -> Bei ausreichender Anstrengung ...\n• Obwohl er aus einer bildungsfernen Schicht stammt, ... -> Ungeachtet seiner bildungsfernen Herkunft ..."
            }
        ]
    },
    "quiz": [
        {
            "id": "B2_L09_Q1",
            "type": "GRAMMAR_FILL",
            "question": "______ (Obwohl er aus einer Arbeiterfamilie stammte) schaffte er den Aufstieg zum Universitätsprofessor.",
            "options": ["Trotz seiner Herkunft aus einer Arbeiterfamilie", "Weil er aus einer Arbeiterfamilie stammte", "Damit er aus einer Arbeiterfamilie stammt", "Während der Arbeiterfamilie"],
            "correctIndex": 0,
            "explanation": "让步从句虽然……转换为介词短语：Trotz (+Gen.) seiner Herkunft aus einer Arbeiterfamilie。"
        },
        {
            "id": "B2_L09_Q2",
            "type": "MEANING_SELECT",
            "question": "“die Chancengleichheit” 在现代教育学中的宪政核心内涵是：",
            "options": ["接受优质教育与发展的机会均等", "按家庭资产分配名额", "统一所有人的期末考分", "免除所有学科家庭作业"],
            "correctIndex": 0,
            "explanation": "die Chancengleichheit 表示无论家庭出身背景，人人依法享有平等公平的受教育发展机会。"
        },
        {
            "id": "B2_L09_Q3",
            "type": "GRAMMAR_FILL",
            "question": "______ (Wenn die soziale Herkunft entscheidet) bleibt das Bildungssystem ungerecht.",
            "options": ["Bei einer Entscheidung durch die soziale Herkunft", "Trotz der sozialen Herkunft", "Nach der sozialen Herkunft", "Ohne soziale Herkunft"],
            "correctIndex": 0,
            "explanation": "条件从句 wenn 转换为介词短语：Bei (+Dat.) einer Entscheidung durch die soziale Herkunft。"
        },
        {
            "id": "B2_L09_Q4",
            "type": "LISTENING_MCQ",
            "question": "“Der Bildungserfolg in Deutschland hängt nach wie vor überdurchschnittlich stark vom Elternhaus ab.” 揭示的核心社会学问题是：",
            "options": ["在德国个人的学业成功依然过度严重地受制于原生家庭的阶层背景。", "德国教育已彻底消除了阶层差距。", "父母学历与孩子成绩毫无关联。", "公立大学仅向高收入家庭开放。"],
            "correctIndex": 0,
            "explanation": "Bildungserfolg = 学业成功，abhängen vom Elternhaus = 依赖于原生家庭。"
        },
        {
            "id": "B2_L09_Q5",
            "type": "SENTENCE_BUILDER",
            "question": "重组教育公平宏观议题：“erfordert / Ein gerechtes Schulsystem / frühkindliche Förderung / für alle Kinder”",
            "options": ["Ein gerechtes Schulsystem erfordert frühkindliche Förderung für alle Kinder.", "Für alle Kinder frühkindliche Förderung ein gerechtes Schulsystem erfordert.", "Ein gerechtes Schulsystem für alle Kinder erfordert frühkindliche Förderung nicht.", "Erfordert ein gerechtes Schulsystem frühkindliche Förderung für alle Kinder."],
            "correctIndex": 0,
            "explanation": "主语 (Ein gerechtes Schulsystem) + 谓语 (erfordert) + 宾语 (frühkindliche Förderung) + 补足语 (für alle Kinder)。"
        }
    ],
    "words": [
        ("die Bildung", "die", "Nomen", "unz.", "教育，个人教养", "Bildung ist die mächtigste Waffe, um die Welt nachhaltig zum Besseren zu verändern.", "真正健全完整的启蒙教育与博雅素养，是全人类手中能够持久把世界变得更美好的最强大和平武器。"),
        ("die Bildungsgerechtigkeit", "die", "Nomen", "unz.", "教育公平，教育正义", "Echte Bildungsgerechtigkeit verlangt den Abbau aller herkunftsbedingten Hürden.", "捍卫真正意义上的教育公平与代际社会正义，当务之急在于彻底铲除一切由原生家庭阶层出身所人为筑起的高墙门槛。"),
        ("die Chancengleichheit", "die", "Nomen", "unz.", "机会均等", "Chancengleichheit im Bildungssystem sichert jedem Talent den verdienten Weg nach oben.", "在国民教育体制中坚决捍卫机会均等原则，能够确保任何寒门子弟凭借自身勤学苦练均能顺利登顶人生坦途。"),
        ("das Bildungssystem", "das", "Nomen", "-e", "国民教育体制", "Das föderale deutsche Bildungssystem führt zu sechzehn verschiedenen Lehrplänen.", "联邦制下的德国教育体制导致十六个联邦州各自为政、独立制定十六套彼此割裂的教学大纲。"),
        ("die PISA-Studie", "die", "Nomen", "-n", "国际学生评估项目 (PISA测试)", "Die Ergebnisse der jüngsten PISA-Studie lösten erneut eine heftige Schockdebatte aus.", "经济合作与发展组织最新公布的PISA国际学生评估综合测评排行榜，再次在德国朝野政坛引爆了犹如大地震般的“教育休克大论战”。"),
        ("die Schule", "die", "Nomen", "-n", "基础教育学校", "Schulen müssen zu Orten lebendiger Neugier und kreativer Entfaltung werden.", "现代中小学校园绝不能沦为摧残孩子童年灵性的死板应试灌输牢笼，而必须真正蜕变为激发蓬勃求知欲与自由创造力的乐园。"),
        ("das Gymnasium", "das", "Nomen", "Gymnasien", "文理中学（学术型高中）", "Das Gymnasium bereitet Schüler traditionell auf das anspruchsvolle Hochschulstudium vor.", "德国文理中学自洪堡时代起便恪守深厚人文底蕴传统，旨在为各大一流学术研究型大学输送基本功扎实的栋梁苗子。"),
        ("die Realschule", "die", "Nomen", "-n", "实科中学", "Die Realschule vermittelt eine fundierte allgemeine und praxisorientierte Vorbildung.", "德国实科中学注重将扎实的通识文化素养传授与紧密结合工商业职场实操的实用性导向完美糅合一体。"),
        ("die Hauptschule", "die", "Nomen", "-n", "普通中学，职业预校", "Die Hauptschule qualifiziert Absolventen traditionell für das duale handwerkliche Ausbildungssystem.", "传统普通中学通过紧凑务实的针对性课程设置，全力为德国享誉全球的手工业与机械制造业双元制职业培训输送生源。"),
        ("die Gesamtschule", "die", "Nomen", "-n", "综合中学（全包容型中学）", "In der Gesamtschule lernen Kinder unterschiedlicher Leistungsstufen länger gemeinsam.", "在破除过早分流弊端而设立的综合性公立中学大院里，具备不同学习领悟天赋的孩子们能够打破隔阂在一起长久共同相处成长。"),
        ("das Abitur", "das", "Nomen", "unz.", "德国高中毕业文凭与大学入学统考", "Das bestandene Abitur berechtigt zum Studium an allen Universitäten in ganz Europa.", "一张盖有州教育部钢印、凝结着数年心血的高中毕业证书(Abitur)，是畅行无阻直通全欧洲任何顶尖公立大学学术殿堂的神圣通行证。"),
        ("die Hochschulreife", "die", "Nomen", "unz.", "大学入学资格", "Die allgemeine Hochschulreife bescheinigt die geistige Reife für ein Universitätsstudium.", "拥有完备的普通高等学术院校入学资格认证，官方庄严证明了该学子在知识储备与心智成熟度上已彻底做好了攀登学术高地的准备。"),
        ("das Studium", "das", "Nomen", "Studien", "大学学业，高校研读", "Ein universitäres Studium erfordert ein hohes Maß an Selbstdisziplin und Autonomie.", "在欧洲古典大学体制下攻读全日制学士与硕士学位，在无人监管催促的自由学风中对学子的自我高度自律与独立探索能力提出了极高考验。"),
        ("die Universität", "die", "Nomen", "-en", "综合性研究型大学", "Die Heidelberger Universität ist die älteste Hochschule auf dem Territorium Deutschlands.", "创立于中世纪1386年的海德堡大学，是坐落在当代德意志联邦共和国辽阔版图之上历史最为悠久沧桑的学界泰斗级知识策源地。"),
        ("die Hochschule", "die", "Nomen", "-n", "高等学校，大学", "Fachhochschulen zeichnen sich durch extreme Praxisnähe und enge Industriekooperationen aus.", "德国应用技术大学(FH)以其课程内容直击行业一线前沿痛点、与本土大型工业巨头产学研无缝深度咬合的鲜明实操特色而名扬四海。"),
        ("die Fachhochschule", "die", "Nomen", "-n", "应用科学大学", "Absolventen einer Fachhochschule sind in Industrie und Mittelstand begehrte Ingenieure.", "从应用科学大学昂首走出的工科毕业生，在德语区各行业龙头制造企业与隐形冠军矩阵中历来被各大雇主作为王牌工程师争相高薪疯抢。"),
        ("die Duale Ausbildung", "die", "Nomen", "unz.", "双元制职业教育培训", "Die duale Ausbildung in Betrieb und Berufsschule gilt weltweit als deutsches Erfolgsmodell.", "在现代车间拜师学艺与在公立职业学校系统研习理论紧密轮动的“双元制”，被国际劳工组织公认为德国战后创造举世瞩目经济奇迹的核心制度法宝。"),
        ("der Auszubildende", "der", "Nomen", "-n", "双元制学徒工，受培学员", "Der Auszubildende erlernt das Mechatroniker-Handwerk von der Pike auf.", "这名怀揣匠心梦想的双元制年轻学徒工在老资格资深特级技师的严厉手把手传授下，正从最底层螺丝钉做起一点一滴精研机电一体化绝活。"),
        ("der Meister", "der", "Nomen", "-", "特级技师，手工艺大师", "Der Meisterbrief ist das Gütesiegel für Spitzenleistungen im deutschen Traditionshandwerk.", "一张凝聚着一生心血的高含金量国家工匠大师资格证书，是德意志传统百年手工业制造业精益求精、登峰造极卓越品质的最高黄金认证标识。"),
        ("das Stipendium", "das", "Nomen", "Stipendien", "奖学金，助学金", "Das renommierte Deutschlandstipendium fördert begabte und gesellschaftlich engagierte Studierende.", "享誉全德的“德国国家奖学金计划”每年拔款数亿，定向重奖那些在专业学术成绩出类拔萃且长期热心公益反哺社会的优秀栋梁大学生。"),
        ("das BAföG", "das", "Nomen", "unz.", "联邦教育促进法助学贷款", "BAföG ermöglicht Kindern aus einkommensschwachen Familien ein sorgenfreies Universitätsstudium.", "德国《联邦教育促进法》(BAföG)国家免息助学补贴贷款制度，为千千万万出身低收入贫困农工阶层的莘莘学子扫平了求学路上的经济拦路虎。"),
        ("die Studiengebühren", "die", "Nomen (Pl.)", "Pl.", "大学学费", "In fast allen deutschen Bundesländern wurden allgemeine Studiengebühren vor Jahren abgeschafft.", "在几乎全部德国联邦州，向公立高等学府全日制攻读学位的学子粗暴强行征收全额学费的陈规陋习早已有口皆碑地被彻底扫进历史垃圾堆。"),
        ("der Bildungsabschluss", "der", "Nomen", "-e", "受教育文凭学历，毕业证书", "Ein anerkannter Bildungsabschluss ist der beste Schutzschild gegen drohende Arbeitslosigkeit.", "手握一张含金量过硬、受国家法律与全社会公认的正规高等教育或高级职教毕业学历文凭，是抵御未来任何突发经济危机失业寒潮的最强合金盾牌。"),
        ("die Qualifikation", "die", "Nomen", "-en", "职业资质，专业技能水平", "Ständige Weiterbildung und der Erwerb neuer Qualifikationen sind das Gebot der Stunde.", "在各行各业突飞猛进的技术大爆炸时代，时刻保持如饥似渴的本领恐慌感、终身不间断考取迭代崭新职业核心资质，已成为破局制胜的时代硬要求。"),
        ("die Weiterbildung", "die", "Nomen", "-en", "职场进修，再教育", "Unternehmen investieren verstärkt in die modulare Weiterbildung ihrer Belegschaft.", "高瞻远瞩的现代化行业翘楚企业无不大手笔砸下重金专项预算，全力为旗下全体中青年骨干员工常态化赋能定制模块化职场在岗深度再教育进修体系。"),
        ("das Lebenslange Lernen", "das", "Nomen", "unz.", "终身学习理念", "Lebenslanges Lernen ist im Zeitalter der Künstlichen Intelligenz zur existenziellen Notwendigkeit geworden.", "在人工智能与算法狂飙大面积洗牌传统岗位版图的新世纪大潮中，“活到老、学到老”的终身学习理念已彻底上升为不可回避的生存立命刚需。"),
        ("die Umschulung", "die", "Nomen", "-en", "职业技能转岗重训", "Nach der Stilllegung des Kohlekraftwerks bot die Agentur für Arbeit geförderte Umschulungen an.", "在老旧燃煤火电厂关停拆除后，地方公共就业服务管理局第一时间无缝进驻，为数千名原产业工人全额资助安排了转岗新能源运维高薪工种技能重训。"),
        ("die Alphabetisierung", "die", "Nomen", "unz.", "扫盲，基础识字率普及", "Globale Alphabetisierungsprogramme sind das Fundament für die wirtschaftliche Entwicklung.", "在广大亚非拉欠发达偏远乡村聚落大刀阔斧推行面向妇女儿童的全球基础扫盲脱贫行动，是撬动当地经济拔除穷根、实现跨越式腾飞的第一块压舱石基石。"),
        ("die Sprachförderung", "die", "Nomen", "unz.", "针对性语言强化培训", "Frühkindliche Sprachförderung in Kindergärten ist der Schlüssel zu gelungener gesellschaftlicher Integration.", "在社区公立幼儿园托育阶段尽早对移民后代幼童开展高标准浸润式针对性德语语言强化辅导，是确保多元族裔群体无缝融入主流现代社会的金钥匙。"),
        ("die Inklusion", "die", "Nomen", "unz.", "融合教育，全包容普惠接纳", "Inklusion an Regelschulen bedeutet, dass Kinder mit und ohne Behinderung gemeinsam unterrichtet werden.", "在普通公立全日制中小学大力推行全融合全包容教育，其最高境界便是让身患残障的孩子与健康同龄伙伴平等坐进同一间阳光教室其乐融融共同学习成长。"),
        ("die Barrierefreiheit", "die", "Nomen", "unz.", "无障碍化环境建设", "Die bauliche Barrierefreiheit aller Bildungseinrichtungen muss endlich flächendeckend umgesetzt werden.", "将全国大中小学及各类科研图书馆的一切物理台阶楼梯与公共活动空间全面改建为电动轮椅畅通无阻的无障碍环境，必须在国家层面雷厉风行全面落地。"),
        ("die soziale Herkunft", "die", "Nomen", "unz.", "原生家庭社会阶层背景", "Die soziale Herkunft darf nicht länger wie ein Schicksal über den Bildungsweg eines Kindes entscheiden.", "投胎降生在何种贫富家庭的原生阶层背景印记，在现代文明宪政社会中绝不应当再像封建宿命般残酷粗暴地提前锁定判决一个无辜孩童一生的学业前程上限。"),
        ("die Chancengerechtigkeit", "die", "Nomen", "unz.", "起跑线机会正义", "Chancengerechtigkeit erfordert ungleiche Investitionen zugunsten sozial benachteiligter Stadtteile.", "践行真正的起跑线机会正义，绝非搞教条绝对的平均主义“撒胡椒面”，而是要求公共财政以更大的力度向老破小社区与薄弱学校进行倾斜性大输血。"),
        ("die Schicht", "die", "Nomen", "-en", "社会阶层", "Kinder aus wohlhabenden akademischen Schichten studieren fünfmal häufiger als Arbeiterkinder.", "在高等公立大学校园里，来自优渥精英知识分子家庭背景的后代攻读博士学位的比例，竟然令人痛心地数倍于平凡普通一线产业工人家庭的子弟。"),
        ("das Milieu", "das", "Nomen", "-s", "社会阶层生活圈层，社会群落", "In verschiedenen sozialen Milieus herrschen völlig unterschiedliche Erziehungsstile und Bildungsambitionen.", "在彼此割裂、壁垒分明的不同社会经济地位圈层大院之中，为人父母者在下一代身上所倾注的家教言传身教范式与升学抱负期望存在着宛如鸿沟般的巨大差异。"),
        ("der Bildungsaufstieg", "der", "Nomen", "unz.", "知识改变命运，学业逆袭跃迁", "Er ist das leuchtende Beispiel für einen gelungenen Bildungsaufstieg aus einfachen Verhältnissen.", "他那充满辛酸与汗水的求学成长奋斗史诗，成为了当代全社会无数出身寒微的无名小卒凭借十年寒窗苦读终成学术泰斗、实现阶层逆袭跃迁的最璀璨典范。"),
        ("die Bildungsbenachteiligung", "die", "Nomen", "unz.", "教育资源结构性匮乏劣势", "Strukturelle Bildungsbenachteiligung verfestigt soziale Ungleichheit über viele Generationen hinweg.", "全社会若长期漠视基层薄弱校在优秀师资配置与硬件资源上的严重结构性匮乏劣势，只会让阶层固化与贫富鸿沟如恶性肿瘤般在代际之间残酷遗传世袭。"),
        ("die Segregation", "die", "Nomen", "unz.", "居住与学区空间阶层隔离分化", "Räumliche Segregation führt dazu, dass sogenannte Brennpunktschulen völlig überfordert sind.", "城市地产商业化狂飙所催生的富人豪宅区与贫民窟在居住空间上的极端物理割裂分化，直接把位于底层的“焦点问题学区薄弱校”推入了师资流失、不堪重负的绝境。"),
        ("die Brennpunktschule", "die", "Nomen", "-n", "生源薄弱困难学校，问题学区校", "Brennpunktschulen brauchen die besten Lehrkräfte, kleinere Klassen und massive sozialpädagogische Unterstützung.", "这批在薄弱生源底色下苦苦支撑的焦点困难攻坚学校，迫切需要举全省之力调配最顶尖的特级骨干名师倾情任教，并全面实行精品小班化教学与专职心理社工驻校。"),
        ("der Lehrermangel", "der", "Nomen", "unz.", "中小学骨干师资匮乏荒", "Der akute Lehrermangel an deutschen Grundschulen bedroht die Unterrichtsqualität elementar.", "在德国各大联邦州全日制公立小学蔓延日久的严重骨干教师大面积荒缺危机，正从最根本地基上粗暴蚕食并威胁着启蒙义务教育的课堂基本质量底线。"),
        ("fördern", "kein", "Verb", "förderte, gefördert", "针对性帮扶，专项培优资助", "Der Staat muss sozial benachteiligte Kinder bereits im Kindergartenalter intensiv fördern.", "各级政府财政必须把大笔公共教育经费精准砸向刀刃上，从幼童尚在嗷嗷待哺的学前托幼阶段便对处境不利家庭的子女实施全方位的倾斜性帮扶培优。"),
        ("benachteiligen", "kein", "Verb", "benachteiligte, benachteiligt", "置于不利境地，歧视亏待", "Ein dreigliedriges Schulsystem neigt dazu, Kinder aus Arbeiterfamilien systematisch zu benachteiligen.", "在孩子仅有十岁稚龄时便过早进行一考定终身分流的传统所谓三级分轨基础教育模式，在现实运行中极易在体制层面上系统性亏待压制广大工人家庭后代。"),
        ("integrieren", "kein", "Verb", "integrierte, integriert", "融入，全纳接纳", "Es ist eine gesamtgesellschaftliche Aufgabe, Geflüchtete rasch in Arbeitsmarkt und Schulen zu integrieren.", "动员全社会一切力量以最快速度将背井离乡的难民孤儿老小妥善安置并全面融入本土正规基础公立学校与职业技能培训就业市场，是一项刻不容缓的宏大人道主义大爱工程。"),
        ("aufsteigen", "kein", "Verb", "stieg auf, aufgestiegen", "阶层跃升，寒门逆袭 (in der Gesellschaft)", "Wer fleißig und begabt ist, sollte in einer gerechten Leistungsgesellschaft ungehindert sozial aufsteigen können.", "在任何一个真正自诩为崇尚公正公平的现代贤能绩效功绩主义文明社会中，凡是心怀远大抱负、品学兼优且挥洒汗水者，均应当畅通无阻地在社会天梯上实现阶层跃升。"),
        ("stagnieren", "kein", "Verb", "stagnierte, stagniert", "陷入横盘停滞", "Wenn Löhne stagnieren und die Inflation frisst, verliert die Mittelschicht ihr Sicherheitsgefühl.", "一旦广大产业一线工人的工资收入陷入长年横盘停滞而恶性通胀又在无情吞噬钱包，哪怕曾经自命优渥的中产阶级也将瞬间彻底丧失内心的阶层安全感。"),
        ("kompensieren", "kein", "Verb", "kompensierte, kompensiert", "对冲弥补先天劣势", "Ganztagsschulen können Bildungsdefizite des Elternhauses durch gezielte Hausaufgabenbetreuung kompensieren.", "推行下午放学后提供专业营养配餐与自习答疑的现代化全日制寄宿或半托制学校，能够通过高标准课后托管有效对冲弥补原生贫困家庭无力辅导功课的先天劣势。"),
        ("qualifizieren", "kein", "Verb", "qualifizierte, qualifiziert", "考取高精尖资质 (sich für)", "Ingenieure müssen sich fortlaufend für die Anforderungen der Industrie 4.0 qualifizieren.", "置身于工业4.0智能物联革命第一线的广大资深研发工程师，必须时刻主动充电，持续考取匹配人机协作与全自动柔性黑灯工厂产线运转的最高级别数字化资质。"),
        ("investieren", "kein", "Verb", "investierte, investiert", "下重注投资教育 (in)", "Eine zukunftsorientierte Nation investiert vor allem in die Köpfe ihrer Kinder und Jugendlichen.", "一个真正拥有长远眼光、誓要屹立于世界强国之林的成熟伟大民族，其国家战略财政永远最舍得倾囊下注投资的，毫无疑问正是其祖国下一代生生不息的智慧大脑。"),
        ("reformieren", "kein", "Verb", "reformierte, reformiert", "大刀阔斧改革变革", "Kultusministerkonferenzen müssen den Mut aufbringen, verkrustete Bildungsstrukturen grundlegend zu reformieren.", "各联邦州主管教育大权的历届教育部长联席会议必须真正拿出破釜沉舟的政治勇气，彻底破除并大刀阔斧重构早已严重因循守旧、脱离数字时代现实的僵化教育体制大厦。"),
        ("ermutigen", "kein", "Verb", "ermutigte, ermutigt", "鼓舞激励，赋能打气 (zu)", "Engagierte Lehrer können Schülerinnen und Schüler aus bildungsfernen Familien zu Spitzenleistungen ermutigen.", "一位真正把教书育人作为毕生天职的伟大恩师所投来的温暖关切与信任目光，完全足以瞬间点燃并鼓舞那些自卑怯懦的寒门少年向着人类学术最高峰发起无畏冲锋。"),
        ("elitär", "kein", "Adjektiv", "-", "高高在上孤芳自赏的，精英主义排他的", "Ein elitäres Bildungssystem schottet Privilegien ab und erstickt Talente im Keim.", "充斥着铜臭味与自命清高阶层排他性的封闭精英主义教育体制，不仅只会沦为少数权贵寄生虫自我保护代际特权的私器，更会冷酷将万千民间天才扼杀于微时。"),
        ("egalitär", "kein", "Adjektiv", "-", "崇尚众生平等的，扁平包容的", "Skandinavische Länder verfolgen ein egalitäres Schulmodell mit herausragenden Erfolgen.", "以芬兰和瑞典为标杆的北欧模式全面践行不分贫富贵贱一视同仁的众生平等大同全纳教育范式，并在国际教育评估舞台上交出了令全球瞩目的满分答卷。"),
        ("bildungsnah", "kein", "Adjektiv", "-", "拥有优良书香家风学术底蕴的", "Kinder aus bildungsnahen Haushalten besitzen von klein auf einen gewaltigen Wortschatz.", "成长于藏书万卷、父母均拥有名校高等学府背景的书香门第书香门第家庭中的幼童，往往在刚咿呀学语阶段便拥有令人叹为观止的超大词汇储备。"),
        ("bildungsfern", "kein", "Adjektiv", "-", "文化程度较低的，缺乏学术资源的", "Jugendliche aus bildungsfernen Schichten brauchen Mentoren, die ihnen neue Horizonte eröffnen.", "出身于祖祖辈辈目不识丁、缺乏起码文化藏书滋养的困顿底层家庭的年轻后生，最迫切需要有社会良知兼具学术底蕴的校外资深导师为他们推开通往世界大舞台的崭新天窗。"),
        ("chancengerecht", "kein", "Adjektiv", "-", "起跑线严格正义公平的", "Ein chancengerechtes Prüfungswesen bewertet ausschließlich Leistung, Fleiß und Wissen.", "一套完全符合现代法治与文明标准的起跑线正义国家选拔考核体系，在阅卷打分时唯一考量且唯一尊重的准绳，只有考生自身的真实实力、辛勤汗水与真才实学。"),
        ("durchlässig", "kein", "Adjektiv", "-", "立交桥式四通八达可灵活转轨的", "Das deutsche Ausbildungssystem muss durchlässiger werden, sodass jeder Geselle ohne Umwege studieren kann.", "德国的大中专职业教育与高等学术大学文凭互认体制必须打造得更加兼收并蓄、如立交桥般四通八达，确保任何一位拥有过硬实操经验的工匠大师都能免试敲开大学校门。"),
        ("kompensatorisch", "kein", "Adjektiv", "-", "针对弱者补偿性倾斜的", "Kompensatorische Erziehungsprogramme zielen darauf ab, frühkindliche Defizite rasch auszubügeln.", "在贫困社区大办普惠托育并辅以专项财政定向奖补的现代补偿性教育倾斜大方针，旨在争分夺秒在孩子心智成型黄金期迅速弥合原生家庭教育短板。"),
        ("leistungsfähig", "kein", "Adjektiv", "-", "学术科研战斗力充沛过硬的", "Ein modernes Bildungswesen ist die Grundvoraussetzung für eine wirtschaftlich leistungsfähige Industriegesellschaft.", "构筑起一套面向世界科技前沿、生机勃勃的世界一流现代国民教育体系，是任何一个国家维系其经济机体长久保持强悍国际创新竞争力的立国之本。"),
        ("inkludierend", "kein", "Adjektiv", "-", "有教无类普惠包容全纳的", "Eine wahrhaft inkludierende Schule lässt kein einziges Kind am Wegesrand zurück.", "一所真正流淌着现代人道主义博爱血液、践行有教无类的伟大典范公立学校，绝不会在波涛汹涌的应试狂潮与升学率考核面前把任何一个暂时掉队的孩子无情抛弃。"),
        ("herkunftsbedingt", "kein", "Adjektiv", "-", "由家庭阶层出生所先天的", "Herkunftsbedingte Nachteile dürfen durch das staatliche Schulsystem nicht noch vertieft werden.", "由投胎家庭经济拮据所不可避免带来的各种微观先天劣势，绝不允许被原本应当充当社会公平最后兜底平衡器的人民公立教育体系进一步推波助澜、恶性放大。"),
        ("ganztägig", "kein", "Adjektiv", "-", "全日制从早到晚托管的", "Der bundesweite Rechtsanspruch auf ganztägige Betreuung für Grundschulkinder entlastet berufstätige Eltern.", "写入联邦法典的针对全体公立在校小学生全面落地推行全日制晚托托管放学法权，为千家万户在职场疲于奔命的年轻双职工父母彻底卸下了后顾之忧。"),
        ("berufsbegleitend", "kein", "Adjektiv", "-", "在职兼读不脱产的", "Berufsbegleitende Masterstudiengänge erfreuen sich bei ehrgeizigen Nachwuchsführungskräften wachsender Beliebtheit.", "利用周末与晚间远程结合开展的在职不脱产高阶管理硕士与工程博士研修班，正受到各大跨国公司梯队年轻骨干新星的极度追捧。"),
        ("interkulturell", "kein", "Adjektiv", "-", "跨越文化种族隔阂的", "Interkulturelle Kompetenz ist an Schulen mit hoher Migrationsquote unverzichtbar für ein friedliches Miteinander.", "在移民后代比例高达半数以上的超大型都市公立学校校园里，掌握海纳百川、尊重异质文化的跨文化沟通包容智慧，是维护不同族裔师生和谐共处的生命线。"),
        ("praxisorientiert", "kein", "Adjektiv", "-", "直击生产第一线实战务实的", "Das duale Studium bietet eine perfekte Symbiose aus anspruchsvoller Theorie und praxisorientierter Ausbildung im Betrieb.", "双元制双轨制本科与研究生联合培养模式，完美融合了象牙塔内博大精深的顶尖前沿理论与深入跨国企业一线车间摸爬滚打的硬核实战大练兵。"),
        ("akademisch", "kein", "Adjektiv", "-", "象牙塔学术界的", "Akademische Freiheit der Lehre und Forschung ist im Grundgesetz unter Art. 5 Abs. 3 unverbrüchlich geschützt.", "大学讲台之上的思想自由、学术论辩与科学真理求索自由，在德国宪法《基本法》第五条第三款之中被赋予了至高无上、神圣不可侵犯的宪治最高护佑。"),
        ("autodidaktisch", "kein", "Adjektiv", "-", "自学成才无师自通的", "Er erwarb fundierte Programmierkenntnisse auf rein autodidaktischem Wege über frei zugängliche Online-Vorlesungen.", "他凭借一腔对科技的炽热狂热与钢铁般的毅力，完全依靠互联网上海量完全免费开放的全球顶级名校开源公开课，无师自通地自学成为了精通分布式架构的代码宗师。"),
        ("kontraproduktiv", "kein", "Adjektiv", "-", "适得其反背道而驰的", "Übermäßiger Notendruck im Grundschulalter wirkt sich nachweislich kontraproduktiv auf die kindliche Lernfreude aus.", "在孩子启蒙稚气未脱的小学一二年级阶段便过早施加令人窒息的分数应试内卷重压，已被无数儿童心理学大数据实锤证明只会对天生的求知欲造成彻底适得其反的毁灭性打击。"),
        ("exemplarisch", "kein", "Adjektiv", "-", "具有典型教科书级示范意义的", "Dieses Vorzeigeprojekt zeigt exemplarisch, wie sozialer Aufstieg durch gezielte Talentförderung gelingen kann.", "这项发轫于基层的标杆示范工程以教科书般的无可辩驳事实生动向全社会雄辩证明：只要精准挖掘潜力苗子并施以甘霖，寒门逆袭的神话完全可以照进现实。"),
        ("substantiell", "kein", "Adjektiv", "-", "实质性真金白银的", "Die Universitäten benötigen eine substantielle und langfristig verlässliche Erhöhung der staatlichen Grundfinanzierung.", "各大公立研究型大学迫切需要国家公共财政从顶层拿出实打实、具有长远可预期战略定力的真金白银经常性经常性办学底盘基准预算增拨。"),
        ("erkenntnisreich", "kein", "Adjektiv", "-", "启迪心智获益匪浅的", "Wir wünschen allen Studierenden ein erkenntnisreiches Semester voller intellektueller Horizonterweiterung!", "我们满怀诚挚地衷心祝愿全天下所有跋涉在求学求真大道上的莘莘学子，都能度过一个思想迸发、视野大开、获益匪浅的丰收新学期！")
    ]
}

# LESSON 10: Demografischer Wandel & Migration (70 words)
L10 = {
    "id": "B2_L10",
    "title": "第10课：人口老龄化、移民融入与多元文化融合 (Demografischer Wandel)",
    "summary": "掌握状态被动态 (Zustandspassiv: sein + Partizip II) 与过程被动态深度对比、人口变迁与移民融入词汇",
    "grammar": {
        "title": "状态被动态与过程被动态 (Zustandspassiv vs. Vorgangspassiv)",
        "sections": [
            {
                "heading": "1. 过程被动态 (werden + Partizip II): 强调动作正在发生或事件过程：",
                "content": "• Ein neues Zuwanderungsgesetz wird im Bundestag debattiert. (正在被辩论)\n• Die Fachkräfte werden im Ausland angeworben. (正在被招揽)"
            },
            {
                "heading": "2. 状态被动态 (sein + Partizip II): 强调动作完成后遗留的静止状态：",
                "content": "• Die Stelle ist seit Monaten unbesetzt. (岗位空缺状态已持续数月)\n• Das Gesetz ist bereits beschlossen. (法律已被通过，处于生效状态)\n• 必须严格区分动作过程与结果状态在政经与社会语境中的精准运用！"
            }
        ]
    },
    "quiz": [
        {
            "id": "B2_L10_Q1",
            "type": "GRAMMAR_FILL",
            "question": "Die neuen Visabestimmungen für Fachkräfte ______ (beschließen - Zustandspassiv) und treten morgen in Kraft.",
            "options": ["sind bereits beschlossen", "werden bereits beschlossen", "haben bereits beschlossen", "seien beschlossen"],
            "correctIndex": 0,
            "explanation": "强调法规通过后的现存法律状态，使用状态被动态：sind bereits beschlossen。"
        },
        {
            "id": "B2_L10_Q2",
            "type": "MEANING_SELECT",
            "question": "“der demografische Wandel” 在社会学中的核心内涵是：",
            "options": ["人口年龄结构、出生率与老龄化变迁", "季节性候鸟迁徙", "城市地下水网改造", "外汇储备增减"],
            "correctIndex": 0,
            "explanation": "der demografische Wandel 指整个人口结构（出生率、死亡率、寿命延长及老龄化）的根本性演变。"
        },
        {
            "id": "B2_L10_Q3",
            "type": "GRAMMAR_FILL",
            "question": "Tausende unbesetzte Stellen in der Pflege ______ (können... besetzen) nur durch qualifizierte Zuwanderung besetzt werden.",
            "options": ["können", "müssen", "dürfen", "lassen"],
            "correctIndex": 0,
            "explanation": "情态被动态复数主语使用 können: Tausende Stellen können ... besetzt werden。"
        },
        {
            "id": "B2_L10_Q4",
            "type": "LISTENING_MCQ",
            "question": "“Eine alternde Gesellschaft ist auf eine geordnete Arbeitsmigration angewiesen, um den Wohlstand zu sichern.” 的核心结论是：",
            "options": ["老龄化社会唯有依靠有序劳动力移民才能维系经济繁荣。", "移民会削弱国家经济。", "老龄化对社会福利制度毫无压力。", "应当全面禁止外国劳工入境。"],
            "correctIndex": 0,
            "explanation": "auf ... angewiesen sein = 依赖于，geordnete Arbeitsmigration = 有序技术劳动力移民。"
        },
        {
            "id": "B2_L10_Q5",
            "type": "SENTENCE_BUILDER",
            "question": "重组跨文化融合倡议命题：“bereichert / Eine weltoffene Gesellschaft / durch Vielfalt / das kulturelle Leben”",
            "options": ["Eine weltoffene Gesellschaft bereichert das kulturelle Leben durch Vielfalt.", "Durch Vielfalt eine weltoffene Gesellschaft das kulturelle Leben bereichert.", "Das kulturelle Leben bereichert eine weltoffene Gesellschaft durch Vielfalt nicht.", "Bereichert eine weltoffene Gesellschaft das kulturelle Leben durch Vielfalt."],
            "correctIndex": 0,
            "explanation": "主语 (Eine weltoffene Gesellschaft) + 谓语 (bereichert) + 宾语 (das kulturelle Leben) + 状语 (durch Vielfalt)。"
        }
    ],
    "words": [
        ("die Demografie", "die", "Nomen", "unz.", "人口统计学，人口学", "Die Demografie liefert exakte statistische Grundlagen für die staatliche Rentenplanung.", "人口统计学为国家未来数十年的基本养老保险精算与劳动力供需预测提供了坚如磐石的数据底盘。"),
        ("der Wandel", "der", "Nomen", "unz.", "深刻变迁，时代转型", "Der demografische Wandel transformiert die Altersstruktur der gesamten westlichen Welt.", "席卷发达世界的深层人口结构大变迁，正在从最底层彻底重构整个欧美现代社会的代际金字塔格局。"),
        ("die Geburtenrate", "die", "Nomen", "-n", "出生率，生育率", "Eine anhaltend niedrige Geburtenrate führt unweigerlich zur Überalterung der Gesellschaft.", "长期徘徊在超低极值区间的总和生育率低迷，必然不可逆转地把整个国家推入深度超老龄化社会深渊。"),
        ("die Sterberate", "die", "Nomen", "-n", "死亡率", "Die Sterberate übersteigt in vielen Regionen Deutschlands seit Jahren die Zahl der Neugeborenen.", "在德国不少内陆工业重镇与偏远乡村，全年的自然死亡人数早已有过之而无不及地大幅反超了新生儿啼哭降生数量。"),
        ("die Lebenserwartung", "die", "Nomen", "unz.", "人均预期寿命", "Die durchschnittliche Lebenserwartung ist dank moderner Medizin auf über achtzig Jahre gestiegen.", "得益于现代循证医学的飞跃发展与公共卫生体系的健全普及，当代国民的人均预期寿命已昂首迈过八十岁大关。"),
        ("die Überalterung", "die", "Nomen", "unz.", "人口极度老龄化", "Die drohende Überalterung bringt die umlagefinanzierten Sozialversicherungssysteme an ihre Belastungsgrenzen.", "迫在眉睫的重度老龄化海啸，正在将原本依靠年轻一代现收现付的传统社会养老保险资金池推向崩溃临界边缘。"),
        ("die Verrentung", "die", "Nomen", "unz.", "退休退职狂潮 (der Renteneintritt)", "Die massenhafte Verrentung der geburtenstarken Jahrgänge hinterlässt gewaltige Lücken im Arbeitsmarkt.", "被称为“婴儿潮一代”的庞大黄金劳动力主力军的排队集中退休退职，正在全德实体企业留下了难以填补的千万人力真空。"),
        ("der Ruhestand", "der", "Nomen", "unz.", "退休养老生活", "Viele aktive Senioren engagieren sich auch im wohlverdienten Ruhestand ehrenamtlich für das Gemeinwohl.", "成千上万身子骨硬朗、阅历丰富的退休银发族，在安享惬意晚年生活的同时依然满腔热情投身于志愿公益反哺社会。"),
        ("das Rentenalter", "das", "Nomen", "unz.", "法定退休年龄", "Die Debatte über eine schrittweise Anhebung des gesetzlichen Rentenalters auf 68 oder 70 Jahre reißt nicht ab.", "围绕是否应当通过分阶段法定延迟退休年龄至68岁乃至70周岁的重大民生争议，在朝野舆论场持续引发激烈博弈。"),
        ("der Generationenvertrag", "der", "Nomen", "unz.", "代际抚养契约", "Der Generationenvertrag besagt, dass die erwerbstätige Generation für die Renten der Alten aufkommt.", "立国之本的“代际抚养契约”核心法理即在于：正在挥洒汗水的一线中青年劳动大军全额供养已经告老还乡的老一辈晚年开支。"),
        ("die Altersarmut", "die", "Nomen", "unz.", "老年绝对贫困，老年返贫", "Insbesondere Frauen mit unterbrochenen Erwerbsbiografien sind im Alter überdurchschnittlich von Armut bedroht.", "尤其是对于那些因生育照料子女而职业生涯长期中断的广大女性群体而言，步入晚年后遭遇绝对贫困的概率居高不下。"),
        ("die Pflegebedürftigkeit", "die", "Nomen", "unz.", "失能失智照护依赖状态", "Mit steigendem Lebensalter nimmt das statistische Risiko einer dauerhaften Pflegebedürftigkeit dramatisch zu.", "随着人均寿命的不断攀升，高龄老人晚年由于脑梗偏瘫或认知衰退而陷入全天候失能依赖照护的现实风险急剧飙升。"),
        ("der Fachkräftemangel", "der", "Nomen", "unz.", "高精尖专业技术人才荒", "Der akute Fachkräftemangel bremst das Wirtschaftswachstum in Industrie, Handwerk und Pflegeberufen.", "在重载装备制造工业、精细手工业以及一线医疗重症护理领域全面爆发的严重技术工人饥渴，正成为扼制国家GDP增长的最大锁喉死结。"),
        ("der Arbeitskräftemangel", "der", "Nomen", "unz.", "基础劳动力大面积匮乏", "Restaurants und Hotels mussten wegen allgemeinen Arbeitskräftemangels ihre Öffnungszeiten drastisch verkürzen.", "在全国各大餐饮连锁商号与度假酒店大堂，因招不到基础服务与后厨洗碗服务人员而被迫忍痛大幅削减营业时段。"),
        ("die Zuwanderung", "die", "Nomen", "unz.", "人口迁入，海外移民引入", "Eine gezielte, an den Bedürfnissen der Wirtschaft ausgerichtete Zuwanderung ist für Deutschland überlebenswichtig.", "建立在国民经济实体产业急迫刚需基础之上的精准技术移民大战略，对德意志联邦共和国的未来堪称关乎生死存亡。"),
        ("die Abwanderung", "die", "Nomen", "unz.", "人口流出，人才外流 (Braindrain)", "Die Abwanderung hochqualifizierter Spitzenforscher ins Ausland alarmiert die heimische Forschungselite.", "大批拥有博士学位的本土顶尖科研领军新星因薪酬待遇与科研体制掣肘而外流奔赴大洋彼岸，为国内学界敲响了沉重警钟。"),
        ("die Einwanderung", "die", "Nomen", "unz.", "入境定居，移民入境", "Deutschland ist de facto seit Jahrzehnten ein modernes und weltoffenes Einwanderungsland.", "毫无争议的历史客观铁证早已雄辩地证明：德国事实上在过去数十年里早已蜕变成为一座生机勃勃的现代化开放移民大国。"),
        ("das Einwanderungsgesetz", "das", "Nomen", "-e", "移民法典", "Das neue Fachkräfteeinwanderungsgesetz senkt bürokratische Hürden für ausländische Spezialisten.", "全新颁布实施的《技术移民法案》以极具战略前瞻性的改革手笔，全面拆除了阻碍海外高素质专业工匠入境发展的官僚壁垒。"),
        ("die Green-Card", "die", "Nomen", "-s", "蓝卡/绿卡居留许可 (die Chancenkarte)", "Die neu eingeführte Chancenkarte ermöglicht Arbeitssuchenden eine unkomplizierte Einreise nach Deutschland.", "重磅全新推出的“求职机会卡”签证制度，让全球怀揣梦想的优秀青年学子得以在尚未拿到正式雇佣合同前即合法赴德找工作。"),
        ("die Arbeitserlaubnis", "die", "Nomen", "-se", "工作许可执照", "Mit der Ausstellung der unbeschränkten Arbeitserlaubnis stand einer Festanstellung im Konzern nichts mehr im Wege.", "随着外管局正式为其核发下不限行业工种的永久全职工作许可执照，他入职知名跨国企业担任高级架构师的最后阻碍烟消云散。"),
        ("die Anerkennung", "die", "Nomen", "unz.", "海外学历文凭同等学力认证", "Die schnelle Anerkennung ausländischer Berufsabschlüsse ist der Schlüssel zur erfolgreichen Arbeitsmarktintegration.", "开足马力全面提速对海外正规高校学历与工匠证书的同等学力无缝认定，是破解引进人才落地难、用工难的最核心关键抓手。"),
        ("die Bürokratie", "die", "Nomen", "unz.", "官僚作风，繁琐审批", "Überbordende Bürokratie und endlose Bearbeitungszeiten in den Behörden schrecken viele willige Zuwanderer ab.", "冗长拖沓、刻板教条的繁文缛节官僚审批流程与动辄数月的漫长签证排队，在现实中狠狠劝退了无数本来诚意满满的海外求职英才。"),
        ("die Integration", "die", "Nomen", "unz.", "社会一体化融入", "Gelingende Integration erfordert Anstrengungen sowohl von den Zuwanderern als auch von der Mehrheitsgesellschaft.", "真正意义上的社会深度融合，绝非单向索取或居高临下的施舍，而是要求新移民群体与主流本土社会两头并进、相互奔赴。"),
        ("die Assimilation", "die", "Nomen", "unz.", "同化，单向彻底同化", "Demokratische Staaten fordern heute keine vollkommene kulturelle Assimilation mehr, sondern friedliche Integration.", "现代成熟的宪政民主文明国度早已彻底抛弃了过去粗暴要求新移民放弃原有文化母体的极端同化老路，转而坚定拥抱多元共生。"),
        ("die Segregation", "die", "Nomen", "unz.", "族裔割裂隔离，平行社会", "Soziale Segregation begünstigt die Entstehung abgeschotteter Parallelgesellschaften in Großstädten.", "因住房歧视与阶层割裂所引发的空间族裔聚集，在部分大都会个别街区不幸孕育出了老死不相往来的极端封闭“平行社会”。"),
        ("die Parallelgesellschaft", "die", "Nomen", "-en", "封闭平行社会", "Rechtsstaatliche Normen müssen ausnahmslos in allen Milieus gelten; Parallelgesellschaften dürfen nicht toleriert werden.", "神圣的法治与宪政准绳在共和国的每一寸土地上均必须得到无差别捍卫；绝不允许任何无视国法的封闭平行私刑社会野蛮生长。"),
        ("die Vielfalt", "die", "Nomen", "unz.", "多元包容，多样性 (Diversity)", "Kulturelle Vielfalt bereichert eine offene Gesellschaft in Gastronomie, Kunst, Wirtschaft und Lebensart.", "充满勃勃生机的多元异质文化，在舌尖美食品鉴、舞台艺术创造、国际商贸开拓以及日常处世之道上极大地丰润了一座现代开放包容社会。"),
        ("der Pluralismus", "der", "Nomen", "unz.", "多元主义", "Politischer und weltanschaulicher Pluralismus bildet den unverzichtbaren Wesenskern unserer freiheitlichen Verfassung.", "捍卫多元并存的政见表达与不同人生信仰取向，构成了我们现行自由民主根本大法不可动摇、神圣不可侵犯的立身立宪灵魂。"),
        ("die Toleranz", "die", "Nomen", "unz.", "宽容，包容异己", "Toleranz endet dort, wo Hasskriminalität und die Ablehnung von Menschenrechten beginnen.", "真正具有战斗力的宽容精神绝非没有底线的纵容与退缩：在面对反人类极端仇恨犯罪与肆意践踏基本人权的行径面前，宽容坚决亮剑。"),
        ("die Fremdenfeindlichkeit", "die", "Nomen", "unz.", "排外主义，仇外情绪 (Xenophobie)", "Demokratische Kräfte müssen entschlossen aufstehen gegen jede Form von Rassismus und Fremdenfeindlichkeit.", "全社会一切有正义感的公民与宪政力量必须同仇敌忾，坚定不移地向任何死灰复燃的种族主义病毒与狭隘排外情绪作最坚决的斗争。"),
        ("der Rassismus", "der", "Nomen", "unz.", "种族主义歧视", "Struktureller Rassismus am Wohnungs- und Arbeitsmarkt muss durch klare Antidiskriminierungsgesetze bekämpft werden.", "潜伏在日常租房看房门槛与求职简历隐形初筛深处的系统性隐性种族歧视，必须通过刚性亮剑的反歧视特别法予以雷霆万钧的重拳痛击。"),
        ("die Diskriminierung", "die", "Nomen", "-en", "歧视，差别待遇", "Niemand darf wegen seines Geschlechts, seiner Abstammung, seiner Rasse oder seiner Heimat benachteiligt werden.", "《基本法》第三条第三款庄严宣告：任何人均不得因其性别特征、门第出身、种族肤色或祖籍故土而在法律地位上遭受任何不公歧视。"),
        ("die Staatsangehörigkeit", "die", "Nomen", "-en", "国籍", "Das neue Staatsangehörigkeitsrecht ermöglicht die Beibehaltung der bisherigen Staatsbürgerschaft.", "全面落地的全新国籍法改革历史性放开了双重国籍限制，允许归化入籍的新公民在宣誓效忠基本法的同时依法保留其原有祖国国籍。"),
        ("die Einbürgerung", "die", "Nomen", "-en", "入籍归化仪式", "Nach fünf Jahren rechtmäßigem Aufenthalt in Deutschland kann man einen Antrag auf Einbürgerung stellen.", "在德国合法居留、依法纳税并熟练掌握德语水平达到B1标准满五年之后，外籍移民即可向政府主管机关正式递交入籍归化申请。"),
        ("die doppelte Staatsbürgerschaft", "die", "Nomen", "unz.", "双重国籍", "Die doppelte Staatsbürgerschaft stärkt das Zugehörigkeitsgefühl von Millionen Zuwanderern der zweiten Generation.", "依法承认并保障双重国籍身份，极大地强化了数以百万计在德土生土长但身兼双重文化血脉的第二代移民对这片热土的政治归属感。"),
        ("das Asyl", "das", "Nomen", "unz.", "政治庇护权", "Politisch Verfolgte genießen nach Artikel 16a des Grundgesetzes das einklagbare Grundrecht auf Asyl.", "依据德国基本法第16a条之明确规定，在母国因政见或信仰遭受专制铁腕政治迫害的受难者，在德国享有通过司法起诉保障的避难法权。"),
        ("der Flüchtling", "der", "Nomen", "-e", "难民", "Die Genfer Flüchtlingskonvention definiert den völkerrechtlichen Schutzstatus für geflüchtete Menschen.", "联合国《关于难民地位的日内瓦公约》在全球国际法维度上极其严谨地确立并保障了因战乱灾荒被迫背井离乡流亡难民的国际人道庇护地位。"),
        ("das Herkunftsland", "das", "Nomen", "-er", "原籍国，出发国", "Wirtschaftliche Kooperation mit den Herkunftsländern soll Fluchtursachen an der Wurzel bekämpfen.", "在平等互利基础上与难民主要流出来源国展开深度的绿色能源与工业产能基建合作，旨在从根本源头上铲除迫使民众流离失所的贫困毒瘤。"),
        ("der Integrationskurs", "der", "Nomen", "-e", "国家融入培训班", "Im staatlich geförderten Integrationskurs lernen Neuzugewanderte Deutsch und gesellschaftliche Grundwerte.", "在由联邦移民与难民局全额出资补贴举办的国家融入班课堂上，新抵德国的新移民系统研读德语日常交流并深入领会现代民主法治核心理念。"),
        ("die Identität", "die", "Nomen", "-en", "文化认同，身份认同", "Identität ist kein starres Gefängnis, sondern ein sich im Austausch mit der Welt ständig weiterentwickelnder Prozess.", "一个人的精神文化认同从来都不是一座画地为牢的冰冷监牢，而是一个在与大千世界不断交流碰撞、兼收并蓄中持续自我升华的鲜活生命进程。"),
        ("altern", "kein", "Verb", "alterte, gealtert", "变老，老龄化 (die Gesellschaft altert)", "Die deutsche Gesellschaft altert rapide und steht vor einem tiefgreifenden demografischen Strukturwandel.", "当代德国社会的人口年龄中位数正在以肉眼可见的速度飞速老化，并在全方位逼近一场牵动医疗、养老金与产业命脉的深层结构大地震。"),
        ("schrumpfen", "kein", "Verb", "schrumpfte, geschrumpft", "萎缩，人口总量负增长", "Ohne kontinuierliche Zuwanderung würde die erwerbsfähige Bevölkerung in den nächsten Jahren dramatisch schrumpfen.", "假若没有源源不断、高素质海外新移民劳动力的持续补充注入，德国国内的核心适龄劳动大军总量将在接下来的数年之内遭遇雪崩式断崖萎缩。"),
        ("zuwandern", "kein", "Verb", "wanderte zu, zugewandert", "迁入定居 (nach)", "Tausende qualifizierte IT-Spezialisten wandern jedes Jahr aus aller Welt nach Deutschland zu.", "每年都有数以万计来自五湖四海、手握硬核代码开发技术的优秀年轻IT极客跨越千山万水，欣然奔赴德意志各大双创中心追逐科技梦想。"),
        ("abwandern", "kein", "Verb", "wanderte ab, abgewandert", "外流，迁出", "Wegen hoher Steuerlasten und erstickender Regulierung wandern innovative Gründer zunehmend in die USA ab.", "面对本土高昂的企业所得税负担与动辄得咎的繁琐行政治理羁绊，部分怀揣颠覆性硬核创意的本土新锐创始人痛下决心转战美国硅谷创业。"),
        ("integrieren", "kein", "Verb", "integrierte, integriert", "融入，吸纳接纳 (sich in)", "Wer sich aktiv in das gesellschaftliche Leben integriert, findet rasch Freunde und berufliche Chancen.", "任何主动走出舒适圈、积极敞开心扉投身社区公共志愿生活并打磨德语技能的新朋友，都能在最短时间内收获真挚友谊与无限职场机遇。"),
        ("assimilieren", "kein", "Verb", "assimilierte, assimiliert", "同化 (sich an)", "Niemand muss seine familiären kulturellen Wurzeln leugnen, um sich vollkommen zu assimilieren.", "在现代包容成熟的现代文明社会大院里，绝对没有任何人需要为了证明自己的忠诚而被迫削足适履、违心割裂并背叛自己原生家族的文化母体。"),
        ("einbürgern", "kein", "Verb", "bürgerte ein, eingebürgert", "接纳归化入籍 (lassen)", "Nach bestandener B1-Prüfung und dem Einbürgerungstest ließ sie sich voller Stolz einbürgern.", "在以全优成绩顺利通过歌德B1全国语言大考并一举拿下德国归化国情知识大考后，她在庄严的市政大厅里满怀自豪地宣誓并正式领到了归化国籍证书。"),
        ("anwerben", "kein", "Verb", "warb an, angeworben", "招揽吸纳人才", "Kliniken werben händeringend examinierte Pflegekräfte und Ärzte in Südostasien und Lateinamerika an.", "为了彻底摆脱ICU重症监护室与外科手术台的空转停摆危机，各大顶级公立医疗集团正十万火急地在东南亚与拉美各大院校定向招募骨干护士与医师。"),
        ("diskriminieren", "kein", "Verb", "diskriminierte, diskriminiert", "歧视虐待", "Unternehmen, die Bewerber wegen ihres ausländisch klingenden Nachnamens diskriminieren, verstoßen gegen das AGG.", "任何在HR初筛环节仅凭应聘者简历上的异域风情外国姓氏便暗中予以淘汰除名的用人单位，在法律上均已直接触犯了国家《普通平等待遇法》的违法红线。"),
        ("tolerieren", "kein", "Verb", "tolerierte, toleriert", "包容宽容", "Eine wehrhafte Demokratie toleriert friedliche Meinungsvielfalt, aber niemals extremistische Gewalt.", "一个具备自我防卫铠甲的坚强宪政民主政体，能够胸襟坦荡地海纳百川包容一切不同声音的交锋，但绝对对任何妄图推翻法治的极端暴力行径施以零容忍制裁。"),
        ("demografisch", "kein", "Adjektiv", "-", "人口结构统计维度的", "Der demografische Faktor in der Rentenformel dämpft den künftigen Anstieg der gesetzlichen Auszahlungen.", "被立法者巧妙写入国家法定养老金测算公式深处的人口结构调节杠杆参数，能够自动对冲平抑未来老龄化对国库财政造成的过度冲击。"),
        ("alternd", "kein", "Adjektiv", "-", "正在加速变老的", "Eine rapide alternde Gesellschaft muss ihren städtischen Raum durch barrierefreie Infrastruktur radikal umbauen.", "一座正在不可逆转地大步迈入老龄化的现代大都会，必须拿出前所未有的魄力将城市全部台阶与老旧街区彻底改造成老幼皆宜的无障碍乐土。"),
        ("arbeitsfähig", "kein", "Adjektiv", "-", "具备完全劳动能力的", "Der Anteil der arbeitsfähigen Bevölkerung an der Gesamtbevölkerung wird in den nächsten zwanzig Jahren spürbar sinken.", "在未来长达二十年的漫长岁月里，处于黄金年龄、具备完全劳动创造能力的青壮年人口占全社会总人口的比重将呈现出无可挽回的持续下挫。"),
        ("erwerbstätig", "kein", "Adjektiv", "-", "在岗在职从事有报酬工作的", "In Deutschland waren im vergangenen Jahr über 45 Millionen Menschen sozialversicherungspflichtig erwerbstätig.", "在刚刚过去的历史大年里，德国全国在岗缴纳全额法定社保的在职正规就业大军总人数历史性地突破了四千五百万人大关。"),
        ("multikulturell", "kein", "Adjektiv", "-", "多民族多元文化交融的", "Berlin-Kreuzberg und Neukölln sind weltberühmte Beispiele für pulsierende, lebendige multikulturelle Stadtviertel.", "坐落于首都柏林核心地带的克罗伊茨贝格与新克尔恩街区，被全球城市规划学者公认为多民族、多族裔文化在同一屋檐下激荡共融的生动教科书典范。"),
        ("kosmopolitisch", "kein", "Adjektiv", "-", "具有世界主义胸襟的，海纳百川的", "Großstädte wie Hamburg und Frankfurt pflegen traditionell ein weltoffenes, kosmopolitisches Selbstverständnis.", "诸如汉堡与法兰克福等拥有数百年自由商贸对外开放基因的欧洲重镇，自古以来便将放眼全球、海纳百川的世界主义世界公民胸襟视为其最骄傲的城市名片。"),
        ("pluralistisch", "kein", "Adjektiv", "-", "多元包容的，拒绝一言堂的", "In einer pluralistischen Medienlandschaft streiten unterschiedliche politische Strömungen frei und öffentlich.", "在坚决捍卫新闻出版自由的多元化现代媒体生态之中，各种不同学术流派与政治意识形态观点在阳光下自由激辩交锋。"),
        ("tolerant", "kein", "Adjektiv", "-", "宽容友善的", "Eine tolerante Grundhaltung gegenüber Andersdenkenden ist die unverzichtbare Basis für gesellschaftlichen Frieden.", "对待那些在生活习惯与价值偏好上与自己截然不同的异己同胞始终秉持包容友善的温和定力，是维护现代社会长治久安的最珍贵底色。"),
        ("fremdenfeindlich", "kein", "Adjektiv", "-", "充斥排外仇恨色彩的", "Fremdenfeindliche Parolen vergiften das gesellschaftliche Klima und schaden dem Ruf des Landes in aller Welt.", "带有恶毒狭隘色彩的极端排外仇外煽动性口号，不仅从根本上毒化了社会的友善包容风气，更在国际舞台上将整个国家几十年积攒下的崇高国际声誉毁于一旦。"),
        ("integriert", "kein", "Adjektiv", "-", "深度融入主流社会的", "Gut integrierte Zuwanderer leisten einen unschätzbaren Beitrag zum wirtschaftlichen und kulturellen Wohlstand.", "早已在第二故乡落地生根、深度融入主流法治社会的数百万新移民同胞，正在为这个国家的实体经济腾飞与文化繁荣贡献着无可替代的巨大正能量。"),
        ("assimiliert", "kein", "Adjektiv", "-", "已完全同化的", "Die Nachkommen der Einwanderergeneration sind sprachlich und beruflich vollkommen assimiliert.", "当年第一代披荆斩棘赴德谋生拓荒者的二代三代后裔，如今在母语德语掌握与职场融入度上早已与土生土长的本土居民毫无二致。"),
        ("geflüchtet", "kein", "Adjektiv", "-", "逃亡避难流离失所的", "Geflüchtete Menschen haben nach dem Völkerrecht Anspruch auf eine menschenwürdige Unterbringung und medizinische Notversorgung.", "历经千难万险逃离战火浩劫的流亡难民，依据神圣的国际法准则，享有获得尊严安置住所与紧急重症医疗托底救治的绝对合法权利。"),
        ("einbürgerungsberechtigt", "kein", "Adjektiv", "-", "依法完全符合归化入籍资格的", "Mehr als fünf Millionen in Deutschland lebende Ausländer sind nach den neuen gesetzlichen Kriterien sofort einbürgerungsberechtigt.", "依据刚刚生效实施的更加包容开明的新入籍法案，目前在德稳定生活多年的五百多万外籍侨胞在法律上已即刻符合归化入籍的全部法定门槛。"),
        ("bilingual", "kein", "Adjektiv", "-", "双语兼通的", "Bilingual aufwachsende Kinder wechseln spielend leicht zwischen zwei Sprachen und Denkmustern.", "在跨国双语原生家庭环境中浸润长大的混血儿童，在日常交谈与深度思维时能够游刃有余地在两套完全不同的语言体系与思维定式之间行云流水自由切换。"),
        ("xenophob", "kein", "Adjektiv", "-", "患有严重恐外排外心理的", "Xenophobe Einstellungen beruhen in den allermeisten Fällen auf tief sitzenden unbegründeten Abstiegsängsten.", "潜藏在某些底层极端排外分子内心的恐外厌外畸形心态，在大数据剖析之下绝大多数本质上其实源自其自身对在残酷市场竞争中被时代淘汰落伍的深深恐惧。"),
        ("intergenerationell", "kein", "Adjektiv", "-", "跨越不同代际之间的", "Intergenerationelle Solidarität bedeutet, dass Junge und Alte Verantwortung füreinander übernehmen.", "真正意义上的代际跨越沟通与守望相助，要求朝气蓬勃的年轻人与步入暮年的银发长辈之间常怀感恩与体谅，在漫长岁月里休戚与共、携手相扶。"),
        ("unverzichtbar", "kein", "Adjektiv", "-", "决不可缺席的，命脉攸关的", "Die Arbeitskraft ausländischer Ärzte ist in ländlichen Kliniken für die Grundversorgung unverzichtbar.", "在偏远乡村与基层县域公立综合医院里，常年坚守在救死扶伤一线的大批外籍主治医师对于兜底维系全区基本急诊重症医疗运转已达到不可或缺的生死地步。"),
        ("weltoffen", "kein", "Adjektiv", "-", "胸怀世界开放包容的", "Ein weltoffenes Deutschland zieht die klügsten Köpfe und innovativsten Talente aus allen Kontinenten magisch an.", "一个始终坚持在政治、文化与经贸上对外全方位敞开温暖怀抱的现代开放德国，如同一块巨大的强力磁石，正对全球各大洲最智慧的大脑展现出无限的迷人魅力。"),
        ("heterogen", "kein", "Adjektiv", "-", "成分多元丰富各异的", "Moderne Schulklassen in der Großstadt weisen eine hochentwickelte, multikulturell heterogene Zusammensetzung auf.", "置身于现代化繁华大都会公立学校宽敞的明亮教室里，讲台下端坐着的学生群体在文化族裔、宗教信仰与母语背景上呈现出百花齐放、高度多元异质的迷人图景。"),
        ("respektvoll", "kein", "Adjektiv", "-", "充满敬畏礼貌与尊重的", "Ein respektvoller Umgangston im gesellschaftlichen Diskurs schützt die Demokratie vor Spaltung.", "在面对重大争议公共政策议题展开全网大讨论时时刻保持得体有礼、就事论事、互相尊重的文明理性底线，是防止现代社会被极端偏激情绪彻底撕裂走向对抗的最佳安全阀。")
    ]
}

# Now assemble full Part 2
import importlib.util
spec = importlib.util.spec_from_file_location("gen_b2_p2", "tools/data/generate_b2_p2.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
lessons_p2 = mod.LESSONS_B2_PART2

# Add L07, L08, L09, L10
lessons_p2.extend([L07, L08, L09, L10])

# Verify counts
print("Lessons in Part 2:", len(lessons_p2))
for l in lessons_p2:
    print(f"  {l['id']}: {len(l['words'])} words - {l['title']}")

# Write tools/data/b2_part2.py
import pprint
with open("tools/data/b2_part2.py", "w", encoding="utf-8") as f:
    f.write("#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n")
    f.write('"""\nB2 Part 2: Lessons 6 to 10 (350 words: 5 x 70 words)\n"""\n\n')
    f.write("LESSONS_B2_PART2 = " + pprint.pformat(lessons_p2, width=120, compact=False) + "\n")

print("Created tools/data/b2_part2.py successfully!")
