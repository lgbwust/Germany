#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator for tools/data/b2_part2.py (Lessons 6 to 10, 70 words each = 350 words).
L06: 人工智能、算法权力与数字伦理危机 (Künstliche Intelligenz & Digitale Ethik) - 70 words
L07: 认知心理学、脑科学与人类心智 (Kognitionspsychologie & Neurowissenschaften) - 70 words
L08: 全球气候治理、生物多样性与生态临界点 (Globale Klimapolitik & Biodiversität) - 70 words
L09: 教育公平、终身学习与社会阶层流动 (Bildungsgerechtigkeit & Soziale Mobilität) - 70 words
L10: 人口老龄化、移民融入与多元文化融合 (Demografischer Wandel & Migration) - 70 words
"""

import pprint

LESSONS_B2_PART2 = [
    # LESSON 6
    {
        "id": "B2_L06",
        "title": "第6课：人工智能、算法权力与数字伦理危机 (Künstliche Intelligenz & Ethik)",
        "summary": "掌握间接引语第一虚拟式 (Konjunktiv I) 深度进阶、学术引注客观性与人工智能伦理前沿词汇",
        "grammar": {
            "title": "第一虚拟式深度进阶与学术客观转述 (Konjunktiv I in Wissenschaft & Medien)",
            "sections": [
                {
                    "heading": "1. 第一虚拟式各人称构成与规则：",
                    "content": "• 词干 + -e, -est, -e, -en, -et, -en\n• er/sie/es habe, sei, könne, wolle, wisse, gehe\n• 转述他人学说或发言：Der Autor behaupte, Algorithmen seien grundsätzlich voreingenommen."
                },
                {
                    "heading": "2. 第一虚拟式同形替换规则：",
                    "content": "• 当第一虚拟式与直陈式同形时（如 sie haben, sie machen），必须用第二虚拟式 (hätten, machten / würden machen) 替换，以示转述与虚拟。"
                }
            ]
        },
        "quiz": [
            {
                "id": "B2_L06_Q1",
                "type": "GRAMMAR_FILL",
                "question": "Die KI-Ethikerin betonte, autonome Waffensysteme ______ (sein) völkerrechtlich zu ächten.",
                "options": ["seien", "sind", "wären", "waren"],
                "correctIndex": 0,
                "explanation": "转述复数主语时，第一虚拟式复数形式为 seien。"
            },
            {
                "id": "B2_L06_Q2",
                "type": "MEANING_SELECT",
                "question": "“der Algorithmus” 在计算机科学与社会学中的确切中文含义是：",
                "options": ["算法，计算规则", "数据黑客", "硬件加速卡", "屏幕分辨率"],
                "correctIndex": 0,
                "explanation": "der Algorithmus 指用于解决特定问题或执行计算的“算法、解题程序规则”。"
            },
            {
                "id": "B2_L06_Q3",
                "type": "GRAMMAR_FILL",
                "question": "Laut Regierungsbericht ______ (haben) das KI-Gesetz bereits erste positive Effekte gezeigt.",
                "options": ["habe", "hat", "hätte", "hatte"],
                "correctIndex": 0,
                "explanation": "第三人称单数间接引语第一虚拟式用 habe。"
            },
            {
                "id": "B2_L06_Q4",
                "type": "LISTENING_MCQ",
                "question": "“Algorithmen können gesellschaftliche Vorurteile und Diskriminierung reproduzieren.” 表达的核心观点是：",
                "options": ["算法可能会复现并强化既有的社会偏见与歧视。", "算法能够彻底根除一切社会偏见。", "算法在做决策时绝对客观公正。", "人类无法对算法进行任何监管。"],
                "correctIndex": 0,
                "explanation": "gesellschaftliche Vorurteile = 社会偏见，reproduzieren = 复制、再生产。"
            },
            {
                "id": "B2_L06_Q5",
                "type": "SENTENCE_BUILDER",
                "question": "重组规范科技伦理命题：“strikte ethische Leitplanken / Künstliche Intelligenz / benötigt / für ihren Einsatz”",
                "options": ["Künstliche Intelligenz benötigt strikte ethische Leitplanken für ihren Einsatz.", "Für ihren Einsatz künstliche Intelligenz strikte ethische Leitplanken benötigt.", "Strikte ethische Leitplanken künstliche Intelligenz für ihren Einsatz benötigt nicht.", "Benötigt künstliche Intelligenz strikte ethische Leitplanken für ihren Einsatz."],
                "correctIndex": 0,
                "explanation": "主语 (Künstliche Intelligenz) + 谓语 (benötigt) + 宾语 (strikte ethische Leitplanken) + 状语 (für ihren Einsatz)。"
            }
        ],
        "words": [
            ("die Intelligenz", "die", "Nomen", "unz.", "智能，智商", "Künstliche Intelligenz verändert alle Bereiche unseres Alltags.", "人工智能正在深刻改变我们日常生活的方方面面。"),
            ("der Algorithmus", "der", "Nomen", "Algorithmen", "算法", "Der Algorithmus optimiert den Energieverbrauch moderner Rechenzentren.", "该算法大幅优化了现代超算数据中心的电力能源消耗。"),
            ("das Neuron", "das", "Nomen", "-en", "神经元", "Künstliche neuronale Netze sind der Struktur des menschlichen Gehirns nachempfunden.", "人工神经网络高度模仿了人类大脑微观神经元的突触连接结构。"),
            ("das Modell", "das", "Nomen", "-e", "大模型，模型", "Große Sprachmodelle verarbeiten gewaltige Mengen an Textdaten.", "大型语言模型能够高速吞吐并深度学习海量文本训练语料。"),
            ("die Automatisierung", "die", "Nomen", "-en", "自动化", "Die fortschreitende Automatisierung ersetzt monotone Büroarbeiten.", "日新月异的自动化浪潮正在迅速替代大量机械重复的案头事务。"),
            ("die Robotik", "die", "Nomen", "unz.", "机器人工程学", "In der industriellen Fertigung spielt die moderne Robotik eine Schlüsselrolle.", "在现代智能工业装备总装制造中，工业机器人工程学发挥着中流砥柱作用。"),
            ("der Cyberspace", "der", "Nomen", "unz.", "赛博空间，网络空间", "Sicherheitsbehörden überwachen kriminelle Aktivitäten im Cyberspace.", "国家网络安全保卫部门密切监控着潜伏在赛博网络空间中的黑客恶意活动。"),
            ("der Datenschutz", "der", "Nomen", "unz.", "数据隐私保护", "Die europäische Datenschutz-Grundverordnung (DSGVO) setzt weltweit Maßstäbe.", "欧洲《通用数据保护条例》(GDPR)为全球数字主权隐私确立了标杆准绳。"),
            ("die Privatsphäre", "die", "Nomen", "unz.", "个人隐私，私密领域", "Bürgerrechtler fordern den Schutz der Privatsphäre vor staatlicher Überwachung.", "数字公民维权组织强烈呼吁捍卫民众个人私密隐私免遭公权力的无死角监控。"),
            ("die Überwachung", "die", "Nomen", "-en", "监控，监测", "Lückenlose Videoüberwachung im öffentlichen Raum stößt auf verfassungsrechtliche Kritik.", "在城市公共公共活动空间推行无死角的人脸识别视频监控引发了宪法层面的重重质疑。"),
            ("die Gesichtserkennung", "die", "Nomen", "-en", "人脸识别技术", "Der Einsatz automatischer Gesichtserkennung an Bahnhöfen bleibt hochgradig umstritten.", "在人流密集的交通枢纽车站常态化部署自动化人脸识别扫描系统依然饱受争议。"),
            ("die Biometrie", "die", "Nomen", "unz.", "生物识别技术", "Biometrische Daten wie Iris-Scans und Fingerabdrücke erfordern besonderen Schutz.", "虹膜扫描特征与指纹等具有唯一性的人体生物识别数据必须受到法定的顶格严密保护。"),
            ("die Manipulation", "die", "Nomen", "-en", "操纵，恶意误导", "Gezielte digitale Manipulation von Wählern untergräbt das Fundament der Demokratie.", "借助算法推荐机制对广大选民开展定向数字心智操纵，将从根本上侵蚀现代民主肌体。"),
            ("die Desinformation", "die", "Nomen", "-en", "虚假信息，假新闻", "Gezielte Desinformationskampagnen sollen das Vertrauen in Institutionen zerstören.", "有组织有预谋的大规模虚假信息造谣抹黑行动意在彻底瓦解公众对社会公共机构的信任。"),
            ("der Deepfake", "der", "Nomen", "-s", "深度伪造技术", "Täuschend echte Deepfakes erschweren die Verifizierung von Nachrichtenbildern.", "以假乱真、难辨真伪的深度伪造视频极大地加剧了新闻事实核查与溯源的难度。"),
            ("die Halluzination", "die", "Nomen", "-en", "模型幻觉，妄想", "Sprachmodelle neigen mitunter zu plausibel klingenden Halluzinationen.", "大型生成式语言大模型在回答特定问题时偶尔会一本正经地输出看似合理的模型幻觉胡话。"),
            ("der Bias", "der", "Nomen", "-es", "算法偏见，系统偏差", "Ein unreflektierter Trainingsdatensatz führt unweigerlich zu rassistischem Bias.", "未经严格数据清洗与伦理对齐的粗糙预训练数据集，必然导致算法输出种族偏见毒素。"),
            ("die Diskriminierung", "die", "Nomen", "-en", "差别待遇，算法歧视", "Automatisierte Bewerbungsscreenings dürfen nicht zur Diskriminierung von Minderheiten führen.", "自动化简历初筛HR算法程序绝不允许对少数族裔求职候选人造成隐蔽的系统性算法歧视。"),
            ("die Transparenz", "die", "Nomen", "unz.", "透明度，可解释性", "Wissenschaftler fordern mehr algorithmische Transparenz von Digitalkonzernen.", "全球前沿学者强烈敦促跨国科技平台巨头向监管机构全面开放其底层算法的逻辑透明度。"),
            ("die Nachvollziehbarkeit", "die", "Nomen", "unz.", "可追溯性，可核实性", "Die Entscheidungen einer KI müssen für betroffene Bürger nachvollziehbar sein.", "人工智能自主作出的任何影响公民重大利益的决策，对当事人在法理上必须具备充分的可解释性。"),
            ("die Autonomie", "die", "Nomen", "unz.", "自主性，独立决断权", "Vollautonome Waffensysteme treffen Tötungsentscheidungen ohne menschliche Kontrolle.", "全自主无人化作战武器系统能够在完全剥离人类最终伦理控制的前提下自主实施目标猎杀。"),
            ("die Singularität", "die", "Nomen", "unz.", "技术奇点", "Philosophen spekulieren über den Zeitpunkt einer technologischen Singularität.", "未来主义哲学家对机器智能全面碾压人类生物智慧的“技术奇点”何时降临展开了激辩。"),
            ("die Superintelligenz", "die", "Nomen", "unz.", "超级智能", "Eine unkontrollierbare künstliche Superintelligenz könnte die Menschheit bedrohen.", "一旦失控脱缰，凌驾于全人类总体智能之上的数字超级智能甚至可能对人类文明构成存亡威胁。"),
            ("das Risikomanagement", "das", "Nomen", "unz.", "风险管控机制", "Ein vorausschauendes Risikomanagement verhindert den Missbrauch mächtiger Algorithmen.", "前瞻性、全生命周期的风险管控审计机制能够有效遏制强大算法能力被不法分子恶意武器化滥用。"),
            ("die Haftung", "die", "Nomen", "-en", "法律侵权民事归责", "Die Haftungsfrage bei Fehlentscheidungen autonomer Fahrzeuge ist gesetzlich zu regeln.", "自动驾驶辅助汽车在遭遇车祸错判事故时的法律侵权责任划分归属必须通过立法明确界定。"),
            ("der Programmierer", "der", "Nomen", "-", "软件架构师，程序员", "Programmierer tragen eine immense ethische Verantwortung für den von ihnen geschriebenen Code.", "软件研发工程师对其敲下的每一行算法代码背后蕴含的伦理道德后果肩负着重逾千钧的责任。"),
            ("der Quellcode", "der", "Nomen", "-s", "开源/闭源源代码", "Open-Source-Software erlaubt die unabhängige Überprüfung des Quellcodes auf Sicherheitslücken.", "开源生态软件允许全球安全专家不受限制地深度审查其底层源代码以排查零日漏洞隐患。"),
            ("das Rechenzentrum", "das", "Nomen", "Rechenzentren", "超算中心，数据机房", "Moderne Rechenzentren werden zunehmend mit CO2-freiem Ökostrom betrieben.", "全球各大新建的现代超大规模数据中心正在加速向百分之百零碳绿电直供模式大步转型。"),
            ("der Energieverbrauch", "der", "Nomen", "unz.", "算力能耗，电力消耗", "Der gigantische Energieverbrauch generativer Modelle belastet die globale Klimabilanz.", "训练超大规模生成式语言大模型所需的惊人天文数字算力能耗正在沉重拖累全球碳减排进程。"),
            ("die Hardware", "die", "Nomen", "unz.", "计算硬件，芯片底座", "Hochmoderne KI-Chips und Grafikkarten bilden das Hardware-Fundament der Rechenleistung.", "顶尖的专用AI算力加速芯片与高性能GPU集群构筑起了现代大模型训练算力底座的坚实硬件磐石。"),
            ("die Schnittstelle", "die", "Nomen", "-n", "数据接口 (API)", "Eine offene API-Schnittstelle ermöglicht die nahtlose Integration in Drittsysteme.", "标准规范的开放API应用程序接口确保了该算法模块能够丝滑无缝接入各类第三方软件生态。"),
            ("die Blockchain", "die", "Nomen", "-s", "区块链，分布式账本", "Die Blockchain-Technologie garantiert manipulationssichere Transaktionsregister.", "去中心化的区块链分布式账本底层架构技术确保了资产交易流水账目具备绝对不可篡改的铁证效力。"),
            ("das Urheberrecht", "das", "Nomen", "-e", "著作权，版权", "Das Training von KIs mit urheberrechtlich geschützten Bildern wirft ungeklärte Rechtsfragen auf.", "直接利用受著作权法保护的美术设计作品对图像生成大模型进行无底线投喂引发了前所未有的知识产权大官司。"),
            ("das Patent", "das", "Nomen", "-e", "发明专利", "Das Europäische Patentamt prüft Anträge auf computerimplementierte Erfindungen sorgfältig.", "欧洲专利局对包含计算机软件算法在内的高价值前沿技术发明专利申请实施着严密细致的实质性审查。"),
            ("die Zensur", "die", "Nomen", "-en", "网络审查，言论把关", "Plattformbetreiber dürfen nicht unter dem Vorwand von Content-Moderation unliebsame Meinungen zensieren.", "跨国社交网络平台巨头绝不能打着内容合规治理的幌子肆意对异质性批判声音实施专横的算法限流或政治审查。"),
            ("die Monopolisierung", "die", "Nomen", "unz.", "行业垄断，寡头割据", "Wettbewerbshüter warnen vor der Monopolisierung des KI-Marktes durch wenige US-Tech-Riesen.", "反垄断监管机构多次敲响警钟，呼吁警惕极少数硅谷科技寡头巨无霸对全球人工智能生态形成铁幕般的赢者通吃垄断。"),
            ("die Souveränität", "die", "Nomen", "unz.", "数字主权，自主可控权", "Digitale Souveränität bedeutet, nicht von ausländischen Cloud-Anbietern abhängig zu sein.", "欧洲捍卫数字主权的核心要义，便在于彻底摆脱在底层算力云服务和核心操作系统上对外部单一国家的致命依赖。"),
            ("der Konsens", "der", "Nomen", "-e", "伦理共识", "Es bedarf eines globalen ethischen Konsenses über die roten Linien militärischer KIs.", "国际社会迫切需要在军事人工智能武器研发应用的终极不可逾越底线红线上凝聚起广泛持久的全球共识。"),
            ("die Richtlinie", "die", "Nomen", "-n", "监管指令，行业指导准则", "Die EU-Kommission verabschiedete wegweisende Richtlinien für vertrauenswürdige KI.", "欧盟委员会正式审议通过了一系列具有划时代风向标意义的全球首部“可信赖人工智能监管行动准则指令”。"),
            ("die Sanktionierung", "die", "Nomen", "-en", "行政处罚，法律惩戒", "Bei gravierenden Verstößen gegen das KI-Gesetz droht eine empfindliche finanzielle Sanktionierung.", "对于胆敢严重违反人工智能监管法案核心红线的跨国企业，将面临高达全球营业额数个百分点的天价行政严厉惩戒。"),
            ("generieren", "kein", "Verb", "generierte, generiert", "生成，批量创造", "Moderne Bildgeneratoren können fotorealistische Porträts in Sekundenschnelle generieren.", "现代顶尖的图像扩散生成大模型仅需数秒钟便能凭空合成出达到单反照相机实拍画质的人物写真。"),
            ("optimieren", "kein", "Verb", "optimierte, optimiert", "调优，精调优化", "Der Algorithmus wurde durch Reinforcement Learning mit menschlichem Feedback fein optimiert.", "该对话大模型借助融合人类真实偏好对齐的强化学习算法完成了深度的微调精调与价值观对齐。"),
            ("filtern", "kein", "Verb", "filterte, gefiltert", "清洗，过滤排查", "Intelligente Spamfilter blockieren schadhafte Phishing-Nachrichten vollautomatisch.", "高度智能化的邮件反垃圾清洗过滤网关能够在后台完全静默无感地将各类恶意钓鱼欺诈邮件直接予以拦截查杀。"),
            ("überwachen", "kein", "Verb", "überwachte, überwacht", "实时监控，严密盯防", "Automatisierte Systeme überwachen das Bankennetzwerk rund um die Uhr auf Geldwäscheverdacht.", "自动化大数据反洗钱风控中枢全天候24小时不间断对全网数以千万笔计的资金流水进行实时高危穿透式监控。"),
            ("regulieren", "kein", "Verb", "regulierte, reguliert", "立法监管，规制约束", "Der Gesetzgeber muss neue Technologien rechtzeitig regulieren, um Schaden abzuwenden.", "国家立法机关必须对突飞猛进的颠覆性前沿硬科技实施审慎包容且及时的立法监管，以彻底杜绝社会公害。"),
            ("antizipieren", "kein", "Verb", "antizipierte, antizipiert", "预判，超前洞悉", "Vorausschauende Sicherheitsforscher müssen künftige Cyberangriffsmethoden antizipieren.", "具备战略前瞻视野的高级网络攻防红蓝对抗安全专家必须在暗网黑客动手之前超前预判新型恶意攻击攻击向量。"),
            ("dezentralisieren", "kein", "Verb", "dezentralisierte, dezentralisiert", "去中心化，分布式改造", "Dezentralisierte Datenhaltung schützt sensible Nutzerdaten vor zentralen Datenlecks.", "推行去中心化的分布式数据存储架构，能够有效防止敏感数据集中沉淀引发灾难性的全局系统性单点数据泄漏。"),
            ("verankern", "kein", "Verb", "verankerte, verankert", "固化植入，确立于", "Ethische Prinzipien müssen fest in der Architektur jedes Algorithmus verankert werden.", "以人为本、科技向善的生命伦理原则必须在算法底层的每行架构设计之初便被牢牢固化熔铸在底层代码之中。"),
            ("unterwandern", "kein", "Verb", "unterwanderte, unterwandert", "暗中侵蚀，架空瓦解", "Falschinformationen im Netz unterwandern das Vertrauen in unabhängigen Journalismus.", "在互联网上肆意泛滥传播的黑灰产虚假有害信息正在潜移默化中严重侵蚀并架空公众对客观独立严肃新闻调查的信赖。"),
            ("harmonisieren", "kein", "Verb", "harmonisierte, harmonisiert", "协调统一，形成一体化规范", "Die Mitgliedstaaten versuchen, ihre nationalen Cybersicherheitsgesetze zu harmonisieren.", "欧盟各主权成员国正紧锣密鼓地开展顶层司法协调，力争在全欧境内将各自割裂的网络空间安全防卫法规彻底拉通一体化。"),
            ("autonom", "kein", "Adjektiv", "-", "高度自律的，完全自主的", "Autonome Fahrzeuge müssen in Sekundenbruchteilen hochkomplexe moralische Entscheidungen treffen.", "完全无人驾驶的自动驾驶机动车辆必须在遭遇突发险情的千分之一秒生死刹那间作出极度复杂的伦理道德抉择。"),
            ("algorithmisch", "kein", "Adjektiv", "-", "算法层面的，由算法驱动的", "Algorithmische Handelssysteme wickeln Milliarden an den globalen Wertpapierbörsen in Millisekunden ab.", "完全由高频算法驱动的量化交易系统在千分之一秒的极速之间于全球各大证券交易所吞吐着数以百亿计的巨量资本。"),
            ("vertrauenswürdig", "kein", "Adjektiv", "-", "可信赖的，安全可靠的", "Die Europäische Union setzt sich weltweit für die Entwicklung einer vertrauenswürdigen KI ein.", "欧洲联盟在国际外交多边舞台上全力摇旗呐喊，坚定倡导走一条安全可靠、合规可控、真正以人为本的可信赖人工智能发展道路。"),
            ("voreingenommen", "kein", "Adjektiv", "-", "存在固有偏见的", "Ein mit unausgewogenen Daten trainierter Algorithmus urteilt zwangsläufig voreingenommen.", "任何依赖于片面失真、样本失衡的数据集喂养训练出炉的算法模型，在做出评估判断时必然带着根深蒂固的偏见与歧视。"),
            ("intransparent", "kein", "Adjektiv", "-", "不透明的，黑箱操作的", "Die Entscheidungsgrundlagen der sogenannten Black-Box-Modelle sind für Menschen völlig intransparent.", "所谓“深度黑箱大模型”内部多达数千亿参数权重协同激发的底层决策逻辑链条，对于人类肉眼凡胎而言完全处于彻底不可知的不透明状态。"),
            ("disruptiv", "kein", "Adjektiv", "-", "颠覆性的，破局重塑的", "Generative KI ist eine disruptive Kraft, die traditionelle Wissensberufe von Grund auf umwälzt.", "生成式大模型是一股具有彻底破局力量的颠覆性浪潮，正在从最底层重构并深度洗牌传统的脑力劳动知识密集型行业。"),
            ("manipulativ", "kein", "Adjektiv", "-", "暗含操纵误导目的的", "Manipulative Designs in Smartphone-Apps zielen darauf ab, die Bildschirmzeit künstlich zu maximieren.", "各类商业手机应用App中处心积虑设计的各种隐蔽操纵性诱导算法，其唯一邪恶目的便是无所不用其极地压榨并榨取用户的屏幕停留时长。"),
            ("ubiquitär", "kein", "Adjektiv", "-", "无所不在的，泛在普及的", "Die ubiquitäre Präsenz vernetzter Sensoren verwandelt moderne Städte in sogenannte Smart Cities.", "数以亿计的物联网传感器设备在城市大街小巷无所不在的泛在渗透，正将传统钢筋水泥都市迅速脱胎换骨改造为现代智慧城市。"),
            ("synthetisch", "kein", "Adjektiv", "-", "合成的，人造数字生成的", "Synthetische Trainingsdaten können helfen, den gravierenden Mangel an realen Patientendaten zu kompensieren.", "在严格保护个人隐私的大前提下，依托大模型逆向生成的高拟真数字合成数据能够有效弥补临床医学真实脱敏病例数据的严重匮乏。"),
            ("deterministisch", "kein", "Adjektiv", "-", "决定论的，确定性的", "Klassische Softwareprogramme arbeiten nach rein deterministischen, fest kodierten Regeln.", "传统的经典计算机应用软件代码严格遵循着确定论的因果逻辑，完全按照程序员预先硬编码焊死的一套确定性规则逐行执行。"),
            ("stochastisch", "kein", "Adjektiv", "-", "随机概率统计的", "Moderne neuronale Netzwerke generieren Antworten auf Basis komplexer stochastischer Berechnungen.", "现代深度人工神经网络在生成行文输出时，其底层完全基于极其庞杂的高维超空间随机概率分布采样计算与统计推演。"),
            ("plausibel", "kein", "Adjektiv", "-", "貌似言之成理的", "Die KI formulierte eine plausibel klingende, aber inhaltlich völlig falsche physikalische Begründung.", "语言模型行云流水般煞有介事地编造出了一段读起来貌似无懈可击、但本质上荒诞不经、漏洞百出的错误物理学推导。"),
            ("auditierbar", "kein", "Adjektiv", "-", "可接受独立合规审计的", "Sicherheitskritische Softwarearchitekturen müssen für unabhängige Behörden jederzeit auditierbar sein.", "任何直接关系到国家命脉与公共生命财产安全的重特大工业控制软件，其底层架构必须全天候无条件接受权威监管机构的独立安全审查审计。"),
            ("resilient", "kein", "Adjektiv", "-", "高抗逆韧性的，鲁棒的", "Kritische Infrastrukturen müssen extrem resilient gegen feindliche Cyberangriffe ausgelegt werden.", "涉及国家电网调度与饮用水供应的绝密关键基础设施系统，在设计之初就必须具备能够硬抗国家级黑客部队狂轰滥炸的超高抗逆韧性。"),
            ("vulnerabel", "kein", "Adjektiv", "-", "脆弱的，易受攻击侵害的", "Veraltete Betriebssysteme in Krankenhäusern sind für bösartige Ransomware-Erpresser hochgradig vulnerabel.", "部分老旧公立医疗机构内部多年未打补丁的老化操作系统网络，在肆虐暗网的勒索病毒变种木马面前显得极其脆弱不堪、一触即溃。"),
            ("sensibel", "kein", "Adjektiv", "-", "高度机密敏感的", "Personenbezogene Gesundheitsdaten und genetische Profile gehören zu den hochsensiblen Daten.", "公民个人的过往电子病历病史档案与全基因组测序图谱在法律性质上属于受国家根本安全法保护的最高等级极度敏感隐私资产。"),
            ("rigoros", "kein", "Adjektiv", "-", "毫不妥协极其严厉的", "Wirtschaftsverbände fordern eine rigorose Verfolgung internationaler Wirtschaftsspionage im Netz.", "全国工商业联合会多次向司法与国安部门呈递请愿书，强烈敦促必须对隐匿在跨国网络电缆深处的境外商业商业间谍活动展开毫不手软的铁腕严厉打击。"),
            ("existenziell", "kein", "Adjektiv", "-", "关乎文明生死存亡的", "Führende Zukunftsforscher stufen das Risiko unkontrollierter Superintelligenz als existenziell ein.", "数十位全球顶尖未来学家与图灵奖得主共同发表联名公开信，郑重将失去人类掌控的通用超级人工智能所带来的潜在终极浩劫定性为关乎全人类生死存亡的系统性危机。"),
            ("anthropozentrisch", "kein", "Adjektiv", "-", "以人类为核心尺度的", "Ein anthropozentrischer Regulierungsansatz stellt die Würde des Menschen über den technologischen Selbstzweck.", "始终坚持以人为本的人本主义监管哲学，把坚定捍卫人的尊严与福祉置于纯粹的技术盲目狂热与虚无狂飙之上。"),
            ("zukunftsträchtig", "kein", "Adjektiv", "-", "具有广阔光明发展前景的", "Investitionen in ethisch fundierte Zukunftstechnologien schaffen krisenfeste Arbeitsplätze für Generationen.", "向底蕴深厚、合规向善的颠覆性硬核前沿未来技术坚定注资，必将为子孙后代铸就能够从容抵御任何周期狂风暴雨的坚实高薪就业基本盘。")
        ]
    }
]

# We need Lessons 7, 8, 9, 10 to complete Part 2
print("Prepared Lesson 6. Now building Lessons 7, 8, 9, 10...")
