#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator part B for tools/data/b2_part3.py: Lessons 13, 14, 15.
Then merges with Lessons 11, 12 and outputs tools/data/b2_part3.py.
"""

import pprint
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_b2_p3_a import L11, L12

# LESSON 13: EU-Politik, Geopolitik & Globale Sicherheit (70 words)
L13 = {
    "id": "B2_L13",
    "title": "第13课：欧盟宪政架构、地缘政治与国际安全 (EU-Politik & Geopolitik)",
    "summary": "掌握高阶语篇逻辑连接词 (Textkohärenz: demzufolge, infolgedessen, dennoch, vielmehr) 与欧洲多边外交词汇",
    "grammar": {
        "title": "语篇衔接与高阶逻辑副词 (Textkohärenz & Adverbiale Konnektoren)",
        "sections": [
            {
                "heading": "1. 因果与推论副词（占第一位，后紧接动词）：",
                "content": "• infolgedessen: 因此，其结果是…… (Die Verträge wurden gebrochen. Infolgedessen verhängte die EU Sanktionen.)\n• demzufolge: 据此，由此可见…… (Die Kriterien wurden erfüllt; demzufolge stimmte das Parlament zu.)\n• folglich: 因而，由此得出……"
            },
            {
                "heading": "2. 转折与纠偏副词：",
                "content": "• dennoch: 尽管如此，依然…… (Es gab Widerstand, dennoch setzten die Verhandler die Ratifizierung durch.)\n• vielmehr: 恰恰相反，而是…… (Es handelte sich um keine Krise, vielmehr bot die Lage eine historische Chance.)\n• indessen: 与此同时，然而……"
            }
        ]
    },
    "quiz": [
        {
            "id": "B2_L13_Q1",
            "type": "GRAMMAR_FILL",
            "question": "Die Friedensgespräche scheiterten; ______ (infolgedessen / trotzdem / weil) zogen sich die Diplomaten zurück.",
            "options": ["infolgedessen", "trotzdem", "weil", "obwohl"],
            "correctIndex": 0,
            "explanation": "infolgedessen 引导因果推论结果：“和平谈判破裂；因此外交官们撤回了。”"
        },
        {
            "id": "B2_L13_Q2",
            "type": "MEANING_SELECT",
            "question": "“das Subsidiaritätsprinzip” 在欧盟宪政分权体制中的核心指导法理是：",
            "options": ["辅德律原则（欧盟仅当下级成员国无力单独解决时才介入）", "欧盟法绝对无条件高于一切国内法", "所有提案必须全票通过", "取消一切国家边界"],
            "correctIndex": 0,
            "explanation": "das Subsidiaritätsprinzip 确立：凡各成员国在地方能妥善处理的事务，欧盟不得大包大揽越俎代庖。"
        },
        {
            "id": "B2_L13_Q3",
            "type": "GRAMMAR_FILL",
            "question": "Er wollte den Vertrag nicht schwächen, ______ (vielmehr) stärken.",
            "options": ["vielmehr", "infolgedessen", "trotzdem", "während"],
            "correctIndex": 0,
            "explanation": "否定词后表相反纠偏：“他并非想削弱条约，恰恰相反，而是想强化条约 (vielmehr stärken)。”"
        },
        {
            "id": "B2_L13_Q4",
            "type": "LISTENING_MCQ",
            "question": "“Die europäische Souveränität erfordert eine koordinierte gemeinsame Sicherheits- und Verteidigungspolitik.” 表达的政治共识是：",
            "options": ["欧洲实现战略自主必须依靠协同一致的共同安全与防务政策。", "欧洲应当彻底解散防务机制。", "各国应当完全各自为战。", "欧盟无需参与国际安全事务。"],
            "correctIndex": 0,
            "explanation": "europäische Souveränität = 欧洲战略自主，Sicherheits- und Verteidigungspolitik = 共同安全与防务政策。"
        },
        {
            "id": "B2_L13_Q5",
            "type": "SENTENCE_BUILDER",
            "question": "重组多边主义外交宣示：“basiert auf Völkerrecht / Die multilaterale Ordnung / und verbindlichen Verträgen”",
            "options": ["Die multilaterale Ordnung basiert auf Völkerrecht und verbindlichen Verträgen.", "Auf Völkerrecht und Verträgen verbindlichen die Ordnung multilaterale basiert nicht.", "Die Ordnung multilaterale basiert auf Verträgen und Völkerrecht verbindlichen.", "Basiert auf Völkerrecht die multilaterale Ordnung und Verträgen verbindlichen."],
            "correctIndex": 0,
            "explanation": "主语 (Die multilaterale Ordnung) + 谓语 (basiert auf) + 补足语 (Völkerrecht und verbindlichen Verträgen)。"
        }
    ],
    "words": [
        ("die Union", "die", "Nomen", "-en", "欧洲联盟，同盟 (die Europäische Union)", "Die Europäische Union ist ein einzigartiger staatenübergreifender Staatenverbund.", "欧洲联盟是由二十七个主权国家自愿联合结成的举世无双、超国家性质的主权国家联合体。"),
        ("die Souveränität", "die", "Nomen", "unz.", "国家主权，战略自主权", "Die nationale Souveränität muss im Einklang mit völkerrechtlichen Verpflichtungen ausgeübt werden.", "各主权国家行使对内对外最高主权，必须时刻恪守与联合国宪章国际法公约相统一的底线准绳。"),
        ("die Geopolitik", "die", "Nomen", "unz.", "地缘政治学，地缘战略", "Die Rückkehr geopolitischer Rivalitäten zwingt Europa zu einer Neubewertung seiner Sicherheitsarchitektur.", "大国地缘政治硬碰撞对抗的死灰复燃，迫使欧洲全方位对自身长达数十年的安全防御大厦实施重新评估。"),
        ("das Völkerrecht", "das", "Nomen", "unz.", "国际法，万国民法", "Das universelle Völkerrecht verbietet jegliche Form von Angriffskriegen und territorialen Annexionen.", "全人类公认的国际法铁律明令禁止任何形式的对外侵略扩张战争以及对邻国领土的野蛮武力兼并。"),
        ("die Charta", "die", "Nomen", "unz.", "宪章 (die UN-Charta)", "Die Charta der Vereinten Nationen bildet das völkerrechtliche Fundament der multilateralen Friedensordnung.", "《联合国宪章》构成了二战后全人类维系多边国际和平与安全秩序最高等级的不可动摇的法理磐石。"),
        ("das Bündnis", "das", "Nomen", "-se", "军事同盟，防务联盟", "Die NATO versteht sich als ein defensives politisch-militärisches Verteidigungsbündnis.", "北大西洋公约组织在战略定位上恪守集体防御原则，是一个坚不可摧的政治军事防御同盟。"),
        ("der Vertrag", "der", "Nomen", "-e", "国际条约，历史盟约", "Der Vertrag von Lissabon reformierte die Funktionsweise der Europäischen Union grundlegend.", "2009年正式生效实施的《里斯本条约》，从顶层宪政层面上彻底重塑并优化了欧盟的运行决策体制。"),
        ("das Parlament", "das", "Nomen", "-e", "欧洲议会 (das Europäische Parlament)", "Das Europäische Parlament wird alle fünf Jahre von den Bürgern der EU-Staaten direkt gewählt.", "作为全欧五亿民意最高殿堂的欧洲议会，每隔五年由全体欧盟主权成员国的合格选民依法直接普选产生。"),
        ("die Kommission", "die", "Nomen", "-en", "欧盟委员会（欧洲行政内阁）", "Die Europäische Kommission wacht als 'Hüterin der Verträge' über die Einhaltung des Europarechts.", "被庄严尊奉为“欧盟条约守护神”的欧洲委员会，作为常任行政执行中枢时刻监督着全欧统一法治的施行。"),
        ("der Rat", "der", "Nomen", "-e", "欧盟理事会，部长理事会 (der Europäische Rat)", "Im Europäischen Rat legen die Staats- und Regierungschefs die allgemeinen politischen Leitlinien fest.", "在由成员国国家元首或政府首脑出席的欧洲理事会峰会上，大国领袖们共同会商敲定全欧中长远宏观政治大方针。"),
        ("das Einstimmigkeitsprinzip", "das", "Nomen", "unz.", "全票一致表决通过原则", "Kritiker fordern die Abschaffung des Einstimmigkeitsprinzips in der europäischen Außen- und Sicherheitspolitik.", "众多资深欧洲战略家大声疾呼：必须彻底废除在欧盟对外外交与安全防务决策中陈旧僵化、极易被一票否决绑架的全票一致原则。"),
        ("das Vetorecht", "das", "Nomen", "-e", "一票否决权", "Das Vetorecht einzelner Mitgliedstaaten blockierte oft dringende gemeinsame Sanktionsbeschlüsse.", "个别不顾大局的小国成员国滥用其手中的一票否决权特权，屡屡导致欧盟急迫出台联合制裁决议的进程严重难产。"),
        ("das Subsidiaritätsprinzip", "das", "Nomen", "unz.", "辅德律分权原则", "Das Subsidiaritätsprinzip schützt die Eigenständigkeit der nationalen und regionalen Parlamente vor Übergriffigkeit.", "辅德律宪政分权原则如同一道坚实的防火墙，有效保护各成员国国内议会与地方自治机关免受布鲁塞尔官僚机构的越俎代庖。"),
        ("die Föderation", "die", "Nomen", "-en", "联邦制超级大国构想", "Manche Visionäre träumen von einer europäischen Föderation nach dem Vorbild der Vereinigten Staaten.", "不少胸怀抱负的欧洲一体化先锋理论家始终怀揣着一个宏伟梦想：即把欧洲最终打造成媲美美利坚合众国的真正欧洲联邦。"),
        ("der Binnenmarkt", "der", "Nomen", "-e", "欧洲统一大市场", "Der europäische Binnenmarkt garantiert die vier Grundfreiheiten: freier Verkehr von Waren, Personen, Dienstleistungen und Kapital.", "欧洲统一大市场不可撼动地庄严捍卫着四项最高根本自由：货物自由流通、人员自由往来、服务自由提供与资本无障碍流动。"),
        ("die Freizügigkeit", "die", "Nomen", "unz.", "人员全欧自由迁徙定居权", "Die Freizügigkeit erlaubt jedem Unionsbürger, in jedem beliebigen Mitgliedstaat zu wohnen und zu arbeiten.", "神圣的人员自由迁徙法权赋予了每一位欧盟公民在全欧二十七个成员国版图内任意选择定居与合法就业的无上尊严。"),
        ("der Schengen-Raum", "der", "Nomen", "unz.", "申根协议免签无国界区", "Im Schengen-Raum wurden die systematischen Personenkontrollen an den Binnengrenzen dauerhaft abgeschafft.", "在横跨整个欧洲大陆的申根区浩瀚版图之内，成员国彼此之间曾经荷枪实弹的边境口岸常态化系统性身份查验早已被彻底扫进历史烟尘。"),
        ("die Außengrenze", "die", "Nomen", "-n", "欧盟外围边界，外部国界", "Der effektive und menschenrechtskonforme Schutz der europäischen Außengrenzen ist eine gemeinsame Aufgabe.", "在严格坚守国际人道主义法治底线的大前提下，构筑起固若金汤的欧洲共同外部边界统一联防，是全欧共同的神圣使命。"),
        ("die Grenzschutzagentur", "die", "Nomen", "-en", "欧洲边境管理局 (Frontex)", "Die Grenzschutzagentur Frontex unterstützt die Mittelmeeranrainer bei der Überwachung der Seewege.", "欧洲边境管理局驻扎在地中海沿岸，出动无人机与高精度雷达巡逻舰全力配合沿线成员国海警严密监控非法偷渡通道。"),
        ("die Sicherheitsarchitektur", "die", "Nomen", "-en", "国际安全防务架构", "Die europäische Sicherheitsarchitektur muss gegen hybride Bedrohungen und Cyberattacken gehärtet werden.", "面对日趋险恶的高维网络战与混合战争威胁，欧洲整体安全大厦必须全面加固硬化其底层关键软硬件与指挥链路。"),
        ("die Abschreckung", "die", "Nomen", "unz.", "战略威慑力量", "Glaubwürdige militärische Abschreckung ist das beste Mittel, um künftige Angriffskriege von vornherein zu verhindern.", "具备在瞬间将侵略者化为齑粉的真实可信的战略军事毁灭性反击威慑力量，历来是遏制霸权野心、拒战争于国门之外的最有效护身法宝。"),
        ("die Aufrüstung", "die", "Nomen", "unz.", "扩军备战，整军备战", "Globale Aufrüstung verschlingt Billionen an Steuergeldern, die im Bildungs- und Gesundheitswesen fehlen.", "冷战思维死灰复燃所引爆的全球新一轮狂暴军备竞赛，正无情吞噬数以万亿计本应投向教书育人与救死扶伤的宝贵纳税人血汗钱。"),
        ("die Abrüstung", "die", "Nomen", "unz.", "军控裁军谈判", "Bilaterale Verträge über nukleare Abrüstung bildeten den friedenspolitischen Höhepunkt des 20. Jahrhunderts.", "美苏两大国在上世纪末艰难达成的一系列削减战略核进攻武器具有里程碑意义的双边裁军条约，构成了人类战后和平外交的巅峰之作。"),
        ("die Nonproliferation", "die", "Nomen", "unz.", "防核扩散机制", "Der Vertrag über die Nonproliferation von Kernwaffen soll verhindern, dass atomare Sprengköpfe sich weiter verbreiten.", "《不扩散核武器条约》在全球范围内筑起了一道刚性防线，旨在坚决斩断一切企图跨过核门槛、私自研发拥核的危险冒险冲动。"),
        ("die Nuklearwaffe", "die", "Nomen", "-n", "核武器，核弹头", "Ein Atomkrieg mit modernen Nuklearwaffen kennt keine Sieger, sondern nur die Vernichtung der Zivilisation.", "在充斥着数万枚热核弹头的毁灭性末日原子核战争中，绝对不可能存在任何胜利者，唯有全人类现代文明的彻底灰飞烟灭。"),
        ("das Waffenembargo", "das", "Nomen", "-s", "多边武器禁运制裁", "Der UN-Sicherheitsrat beschloss ein lückenloses Waffenembargo gegen die kriegführenden Bürgerkriegsparteien.", "联合国安理会五大常任理事国一致表决通过决议，对深陷血腥内战泥潭的当事各派武装实施全方位的严密武器与弹药禁运。"),
        ("die Sanktion", "die", "Nomen", "-en", "经济与金融制裁手段", "Finanzielle Sanktionen schnitten das gegnerische Regime vom internationalen Zahlungsverkehr und SWIFT-Netz ab.", "雷霆万钧的重磅金融制裁手段在一夜之间将敌对侵略政权从全球跨境美元欧元外汇清算SWIFT骨干网络中彻底断链踢出。"),
        ("die Diplomatie", "die", "Nomen", "unz.", "穿梭外交，外交智慧", "Klassische Diplomatie verlangt Geduld, Verschwiegenheit und die stete Suche nach tragfähigen Kompromissen.", "崇高的传统职业外交艺术需要如止水般的超凡耐性、恪守秘密谈判的职业操守，以及永不放弃在刀刃上寻觅折中方案的务实智慧。"),
        ("der Botschafter", "der", "Nomen", "-", "特命全权大使（男）", "Der Botschafter überreichte dem Staatsoberhaupt im Schloss Bellevue sein feierliches Beglaubigungsschreiben.", "这位资深特命全权大使在贝尔维尤总统官邸举行的大典上，郑重向驻在国国家元首呈递了其祖国元首签署的国书。"),
        ("die Botschafterin", "die", "Nomen", "-nen", "特命全权大使（女）", "Die Botschafterin vertrat die Position ihres Landes vor den Vereinten Nationen mit rhetorischer Brillanz.", "这位女特命全权大使在联合国大会讲坛上凭借其令人拍案叫绝的辞令魅力与严密法理，铿锵有力地捍卫了祖国的核心利益。"),
        ("das Konsulat", "das", "Nomen", "-e", "领事馆", "Das Generalkonsulat hilft in Not geratenen Landsleuten bei Passverlust und juristischen Notfällen im Ausland.", "常设在各大海外贸易口岸城市的总领事馆，日夜不停为在境外遭遇护照遗失、车祸险情的同胞提供坚强的人道外交领事保护。"),
        ("die Ratifizierung", "die", "Nomen", "-en", "条约批准程序", "Ein völkerrechtlicher Vertrag tritt erst nach seiner förmlichen Ratifizierung durch die nationalen Parlamente in Kraft.", "一项由外交官拟定的双边或多边国际条约，必须在各自成员国最高立法机构依法经辩论表决并完成正式批准程序后，方具备法律效力。"),
        ("das Veto", "das", "Nomen", "-s", "否决权，否决表决", "Mit seinem Veto verhinderte das ständige Mitglied eine Verurteilung des völkerrechtswidrigen Überfalls.", "凭借其所拥有的安理会常任理事国一票否决权，该大国公然动用否决权阻挠了大会旨在谴责这场背叛国际法侵略行径的决议草案。"),
        ("die Resolution", "die", "Nomen", "-en", "联合国大会/安理会正式决议", "Die Resolution fordert den sofortigen und bedingungslosen Rückzug aller ausländischen Besatzungstruppen.", "这项以压倒性多数赞成票通过的历史性正式决议，义正词严地强制勒令所有外国占领军武装必须在限定时间内无条件全数撤离。"),
        ("das Mandat", "das", "Nomen", "-e", "联合国维和授权，授权令", "Die Blauhelmsoldaten operieren unter einem strikten Mandat des UN-Sicherheitsrates zum Schutz der Zivilbevölkerung.", "头戴蓝色贝雷帽的联合国维和勇士部队，在安理会庄严赋予的保卫无辜平民生命安全的崇高人道授权框架下开展巡逻行动。"),
        ("die Blauhelme", "die", "Nomen (Pl.)", "Pl.", "联合国维和部队（蓝盔部队）", "Die Blauhelme trennten die verfeindeten Lager und sicherten die humanitäre Versorgung der Flüchtlingslager.", "联合国蓝盔维和部队用血肉之躯在交战双方狂暴的火线之间筑起了一道隔离缓冲带，拼死确保了沿途数十万难民的人道主义粮食大补给。"),
        ("die Allianz", "die", "Nomen", "-en", "战略联盟，多边结盟", "Eine transatlantische Allianz sichert seit über sieben Jahrzehnten Freiheit, Wohlstand und Stabilität in Europa.", "历经风雨考验跨越七十余载沧桑的跨大西洋战略同盟，始终为守护整个欧罗巴大陆的自由、经济繁荣与地缘稳定充当着最强支柱。"),
        ("die Hegemonie", "die", "Nomen", "unz.", "单边霸权，霸权主义", "Gegen den imperialen Versuch regionaler Hegemonie formierte sich ein breites Bündnis souveräner Nachbarn.", "面对某些野心家企图在地区强推顺我者昌逆我者亡的帝国单边霸权狂妄举动，周边所有爱好和平的主权邻邦迅速结成了坚固的统一战线。"),
        ("der Multilateralismus", "der", "Nomen", "unz.", "多边主义", "Multilateralismus bedeutet, weltweite Krisen gemeinsam durch völkerrechtliche Institutionen und Dialoge zu bewältigen.", "多边主义的灵魂底色正在于：拒绝弱肉强食的丛林法则，坚定依靠以联合国为核心的国际多边机制与平等协商共同破解全球危机。"),
        ("der Unilateralismus", "der", "Nomen", "unz.", "单边主义，唯我独尊", "Gefährlicher Unilateralismus untergräbt das mühsam aufgebaute System des weltweiten Völkerrechts.", "肆意践踏多边国际共识、奉行唯我独尊霸凌强权逻辑的单边主义，正在疯狂侵蚀人类历经两次世界大战惨烈浩劫才艰难构筑起的国际法大厦。"),
        ("verhandeln", "kein", "Verb", "verhandelte, verhandelt", "展开外交谈判 (über)", "Die Chefunterhändler verhandeln hinter verschlossenen Türen über einen nachhaltigen Waffenstillstand.", "双方的首席特使全权谈判代表在隔绝外界喧嚣的闭门密室之中，就达成具有长久约束力的停火停战主干协议展开极其艰苦的拉锯谈判。"),
        ("ratifizieren", "kein", "Verb", "ratifizierte, ratifiziert", "正式核准批准条约", "Der Deutsche Bundestag ratifizierte das historische Klimaschutzabkommen einstimmig bei nur wenigen Enthaltungen.", "德意志联邦议院国家立法大厅内响起雷鸣般的掌声，议员们以压倒性绝对优势正式表决通过并核准批准了这项划时代的气候协定。"),
        ("deeskalieren", "kein", "Verb", "deeskalierte, deeskaliert", "平息局势，降温降级", "Erfahrene Krisendiplomaten bemühten sich Tag und Nacht, den hochgefährlichen Grenzkonflikt rasch zu deeskalieren.", "经验老到的大国资深斡旋特使日夜兼程奔走呼号，竭尽全力赶在战火彻底失控前让剑拔弩张的致命边境流血摩擦全面降级降温。"),
        ("eskalieren", "kein", "Verb", "eskalierte, eskaliert", "冲突螺旋式升级失控", "Der verbale Schlagabtausch drohte binnen Tagen zu einem unkontrollierbaren militärischen Schlagabtausch zu eskalieren.", "两国高层原本仅停留在外交口水战的唇枪舌剑，在狂热民粹叫嚣裹挟下眼看就要在数天之内不可逆转地升级为全面武装热战。"),
        ("integrieren", "kein", "Verb", "integrierte, integriert", "一体化吸纳", "Die Europäische Union strebt an, die westlichen Balkanstaaten nach Reformen vollkommen zu integrieren.", "欧洲联盟展现出宏大战略定力，誓言在西巴尔干各国全面深化法治与市场化改革后，将其全数完整一体化吸纳接纳为正式成员。"),
        ("sanktionieren", "kein", "Verb", "sanktionierte, sanktioniert", "实施经贸制裁惩戒", "Die Weltgemeinschaft sanktionierte das völkerrechtswidrige Verhalten durch das Einfrieren aller Auslandsguthaben.", "国际社会针对其公然践踏国际公法的无耻强盗径施以铁腕制裁，当即以不可抗拒之力强行全面冻结其潜藏在海外各大银行的全部主权外汇资产。"),
        ("vermitteln", "kein", "Verb", "vermittelte, vermittelt", "外交斡旋调解 (in / zwischen)", "Neutrale Staaten wie die Schweiz vermitteln traditionell erfolgreich zwischen verfeindeten Kriegsparteien.", "像瑞士和奥地利这样恪守永久中立的法治典范国家，自古以来便以超然独立的崇高道德威望，在殊死拼杀的交战当事国之间充当着关键金牌调解人。"),
        ("intervenieren", "kein", "Verb", "intervenierte, interveniert", "武装干涉，人道主义介入", "Nur ein Mandat des UN-Sicherheitsrates legitimiert eine internationale Koalition, militärisch zu intervenieren.", "唯有持有联合国安全理事会白纸黑字严格审议签发的多边人道授权决议，国际多国维和联合武装力量方具备出兵开展军事干预的唯一合法法理基石。"),
        ("beilegen", "kein", "Verb", "legte bei, beigelegt", "和平化解和平息 (einen Streit)", "Durch zähe diplomatische Vermittlung konnte der jahrzehntelange Grenzstreit friedlich beigelegt werden.", "依托长达数年艰苦卓绝的耐性外交斡旋斡旋，这场困扰两国边民长达半个世纪之久的领土边界争端终于在法治框架下宣告和平烟消云散。"),
        ("beschließen", "kein", "Verb", "beschloss, beschlossen", "通过决议决定", "Die Staatschefs beschlossen die Schaffung eines gemeinsamen europäischen Verteidigungs- und Rüstungsfonds.", "齐聚布鲁塞尔的各国国家元首以高度历史担当共同通过重磅决议：正式出资设立首期规模达数百亿欧元的欧洲联合防务与联合军工攻关基金。"),
        ("diplomatisch", "kein", "Adjektiv", "-", "外交层面的，外交互惠的", "Auf diplomatischem Parkett zählen jedes Wort, jede Nuance und jedes scheinbar nebensächliche Signal.", "在刀光剑影隐于无形的高端多边跨国外交舞台之上，发言人的每一个措辞选词、每一个微妙语调甚至每一次看似不经意的肢体语言，都蕴含着深不可测的千钧分量。"),
        ("multilateral", "kein", "Adjektiv", "-", "多边共同参与的", "Multilaterale Verträge bieten den besten Schutz gegen das rücksichtslose Faustrecht des Stärkeren.", "涵盖全球绝大多数文明国家的包容性多边国际公约网络，是破除“弱肉强食、胜者通吃”丛林蛮霸法则的最坚实法治安全气囊。"),
        ("unilateral", "kein", "Adjektiv", "-", "单边霸道独断专行的", "Unilaterale Wirtschaftssanktionen ohne Rückendeckung der Vereinten Nationen verstoßen gegen den Geist des Völkerrechts.", "脱离了联合国集体审议多边授权、由个别大国出于一己私利在海外滥施的长臂管辖单边经贸金融制裁，在法理本质上严重违背了神圣的国际法精神。"),
        ("bilateral", "kein", "Adjektiv", "-", "双边两方的", "Die beiden Nachbarstaaten schlossen ein wegweisendes bilaterales Freundschafts- und Zusammenarbeitsabkommen.", "这对曾经世世代代兵戎相见的陆上邻邦彻底摒弃历史恩怨，在首都隆重签署了一份永结同好、造福边民的具有里程碑意义的双边睦邻友好合作公约。"),
        ("supranational", "kein", "Adjektiv", "-", "超国家的，让渡部分主权的", "Die Europäische Union verfügt in Umwelt- und Handelsfragen über echte supranationale Entscheidungskompetenzen.", "在攸关全欧长远福祉的生态环境保护与涉外进出口关税大权上，欧洲联盟被成员国合法赋予了凌驾于成员国国内法之上的真正超国家排他性终审裁决权。"),
        ("subsidiar", "kein", "Adjektiv", "-", "基于辅德律补充性的", "Entscheidungen sollten nach dem Prinzip der Subsidiarität immer so bürgernah wie möglich getroffen werden.", "依据神圣的辅德律分权精神，一切关乎老百姓切身利益的公共政策，原则上必须遵循“能由基层乡镇决定的绝不上交区县，能由成员国搞定的绝不推给布鲁塞尔”的就近便民法则。"),
        ("strategisch", "kein", "Adjektiv", "-", "事关国家命运战略性的", "Europas strategische Autonomie erfordert zwingend eine eigene krisenfeste Energie- und Halbleiterproduktion.", "欧洲若想在波诡云谲的世界大棋局中真正挺直腰杆挺起战略自主的脊梁，就必须在本土打造出固若金汤、绝不受制于人的新能源自给与车规芯片制造全产业链。"),
        ("souverän", "kein", "Adjektiv", "-", "享有完全独立自主主权的", "Jeder souveräne Staat besitzt das unantastbare Recht, seine gesellschaftliche Ordnung frei von äußerer Einmischung zu wählen.", "世间任何一个享有崇高独立主权的国家，均享有神圣不可侵犯的自主选择其政治制度与社会发展道路的权利，绝不容许任何外来势力指手画脚。"),
        ("imperial", "kein", "Adjektiv", "-", "带有帝国霸权侵略扩张色彩的", "Imperiale Großmachtfantasien aus dem vorigen Jahrhundert haben im modernen Völkerrecht keinen Platz mehr.", "那些源自前现代封建帝国殖民时代、做着瓜分势力范围迷梦的野蛮帝国霸权幻象，在全人类早已迈入和平与发展的现代文明法治坐标系中已被判处彻底死刑。"),
        ("hegemonial", "kein", "Adjektiv", "-", "搞霸权垄断的", "Kleine und mittlere Nationen wehren sich mit Entschiedenheit gegen hegemoniale Ansprüche dominanter Großmächte.", "在联合国内部，广大中小主权国家正空前紧密地携起手来，以坚如磐石的集体意志坚决抵制任何超级大国妄图在国际事务中搞一言堂、拉帮结派的霸权主义图谋。"),
        ("wehrhaft", "kein", "Adjektiv", "-", "具备钢铁自我防卫铠甲的", "Die Bundesrepublik Deutschland ist als eine wehrhafte, streitbare Demokratie gegen Extremisten konzipiert.", "德意志联邦共和国自战后建国第一天起，其宪制灵魂便被清醒定调为“具备战斗力自我防卫能力的武装民主体制”，坚决对任何妄图颠覆自由秩序的极端狂热分子依法予以专政痛击。"),
        ("pazifistisch", "kein", "Adjektiv", "-", "绝对和平主义的", "Eine rein pazifistische Haltung stößt an ihre tragischen Grenzen, wenn ein völkerrechtswidriger Aggressor Staaten überfällt.", "在面对武装到牙齿、公然撕毁一切国际公约的残暴侵略狂徒的钢铁洪流铁蹄蹂躏时，空洞教条的绝对和平主义往往会陷入无力保护妇孺的悲剧性伦理死结。"),
        ("defensiv", "kein", "Adjektiv", "-", "纯粹防御性的", "Alle NATO-Einsatzpläne dienen ausschließlich dem defensiven Schutz des gemeinsamen Bündnisgebietes.", "大西洋两岸防务联盟在参谋长联席会议上所制定的一切战役推演预案，其唯一神圣旨归永远全心全意服务于对成员国神圣领土免受外敌入侵的纯粹自卫防御。"),
        ("offensiv", "kein", "Adjektiv", "-", "先发制人进攻性的", "Offensive Militärstrategien verletzen das im Artikel 2 der UN-Charta festgeschriebene Gewaltverbot.", "任何崇尚先发制人打击、带有赤裸裸侵略扩张性质的所谓“攻势军事学说”，在法理本质上均已严重践踏触犯了《联合国宪章》第二条明文规定的全面禁止使用武力原则。"),
        ("koordiniert", "kein", "Adjektiv", "-", "协同一致步调一致的", "Eine koordinierte europäische Sanktionspolitik trifft die Finanzströme des Aggressors mit maximaler Härte.", "欧洲二十七国在布鲁塞尔统一部署、步调一致同频共振出台的精准重磅金融制裁杀手锏，能够以最大破坏力在源头上直接击碎侵略者的战争机器资金链条。"),
        ("solidarisch", "kein", "Adjektiv", "-", "患难与共守望相助的", "In Krisenzeiten stehen die europäischen Demokratien unverbrüchlich und solidarisch Schulter an Schulter.", "每当阴霾密布、极权主义风暴企图卷土重来的至暗时刻，欧洲各自由民主国家必将休戚与共，以坚如铁石的守望相助品格肩并肩共同筑起捍卫人类文明火种的铜墙铁壁。"),
        ("verbindlich", "kein", "Adjektiv", "-", "具有刚性法治约束力的", "Ein völkerrechtlicher Friedensvertrag muss für alle beteiligten Signatarstaaten absolut verbindlich sein.", "一份历经无数同胞鲜血洗礼才换来的神圣和平终战协约，对于所有在卷轴上郑重盖印签字的缔约主权国家均必须具备绝对不容亵渎的法治刚性约束力。"),
        ("unverrückbar", "kein", "Adjektiv", "-", "坚如磐石不可撼动的", "Die Unverletzlichkeit international anerkannter Staatsgrenzen ist eine unverrückbare Grundfeste des Friedens.", "国际社会公认的现有主权成员国领土边界神圣不可侵犯，是维系战后欧罗巴大陆乃至整个世界长治久安最不可撼动、绝对不容任何妄议的根本基石。"),
        ("konstruktiv", "kein", "Adjektiv", "-", "极具建设性破局导向的", "In den Verhandlungen leistete die Delegation einen konstruktiven Beitrag zur Beilegung des langen Konflikts.", "在这场举世瞩目的和平破冰峰会进程中，我国外交代表团以极高的政治胸襟提出了多项极具建设性的折中方案，为彻底平息这场世纪恩怨立下了汗马功劳。"),
        ("zukunftsorientiert", "kein", "Adjektiv", "-", "放眼长远面向未来的", "Eine zukunftsorientierte europäische Geopolitik verbindet wirtschaftliche Stärke, Diplomatie und Wertefestigkeit.", "一套真正能够经受住历史风云严酷检验、放眼未来百年的欧洲宏观地缘大战略，必须在最深层次将硬核的实体经济产业科技命脉、卓越高超的外交斡旋穿透力与坚如磐石的现代人权价值观定力融为一体。")
    ]
}

# LESSON 14: Rhetorik, Debatte & Argumentationskunst (70 words)
L14 = {
    "id": "B2_L14",
    "title": "第14课：高阶演讲修辞学、思辨论辩与说服艺术 (Rhetorik & Debatte)",
    "summary": "掌握高阶功能动词结构 (Gehobene Funktionsverbgefüge: in Erwägung ziehen, Vorrang haben) 与公众辩论修辞词汇",
    "grammar": {
        "title": "高阶功能动词体系 (Gehobene Funktionsverbgefüge in Rede & Debatte)",
        "sections": [
            {
                "heading": "1. 介词短语型功能动词结构：",
                "content": "• in Erwägung ziehen (= erwägen): 纳入慎重考虑\n• zur Geltung kommen (= wirksam werden): 充分彰显，发挥作用\n• in Kraft treten (= gültig werden): 正式生效实施\n• zum Ausdruck bringen (= ausdrücken): 明确表达"
            },
            {
                "heading": "2. 纯宾语型功能动词结构：",
                "content": "• Vorrang haben vor (+Dat.) (= wichtiger sein als): 享有绝对优先权\n• Kritik üben an (+Dat.) (= kritisieren): 对……提出严厉批评\n• Maßnahmen ergreifen (= handeln): 采取断然措施\n• einen Entschluss fassen (= sich entschließen): 痛下决心做出决断"
            }
        ]
    },
    "quiz": [
        {
            "id": "B2_L14_Q1",
            "type": "GRAMMAR_FILL",
            "question": "Die Bundesregierung muss diesen unkonventionellen Lösungsweg ernsthaft ______ (in Erwägung / zur Sprache / zum Abschluss) ziehen.",
            "options": ["in Erwägung", "zur Sprache", "zum Abschluss", "in Zweifel"],
            "correctIndex": 0,
            "explanation": "固定功能动词搭配：etwas in Erwägung ziehen (将某事纳入审慎考量范围)。"
        },
        {
            "id": "B2_L14_Q2",
            "type": "MEANING_SELECT",
            "question": "修辞格 “die Antithese” 在公众辩论与高阶演说中的艺术效果是：",
            "options": ["将截然对立的观点并列对比以强化反差与说服力", "故意含糊其辞回避核心问题", "以人身攻击替代逻辑论证", "重复朗读同一句话三次"],
            "correctIndex": 0,
            "explanation": "die Antithese 指在修辞上将对立冲突的意象或命题并置对比，以制造强烈的逻辑反差震撼。如“Friede den Hütten, Krieg den Palästen!”"
        },
        {
            "id": "B2_L14_Q3",
            "type": "GRAMMAR_FILL",
            "question": "Der Schutz des Lebens muss vor wirtschaftlichen Profitinteressen immer absoluten ______ (Vorrang) haben.",
            "options": ["Vorrang", "Vortritt", "Vorteil", "Vorfall"],
            "correctIndex": 0,
            "explanation": "固定功能动词表达：Vorrang haben vor (+Dat.) (享有绝对优先权)。"
        },
        {
            "id": "B2_L14_Q4",
            "type": "LISTENING_MCQ",
            "question": "“Der Redner entkräftete die Einwände der Opposition mit bestechender Logik.” 描述的辩论现场情况是：",
            "options": ["演讲者用无懈可击的严密逻辑彻底击溃了反对派的全部异议质问。", "演讲者因紧张忘词被对手打断。", "反对派说服了全场听众。", "双方因争执过激被议长逐出会场。"],
            "correctIndex": 0,
            "explanation": "entkräften = 驳倒、瓦解，Einwände = 异议反驳，bestechende Logik = 令人信服叫绝的严密逻辑。"
        },
        {
            "id": "B2_L14_Q5",
            "type": "SENTENCE_BUILDER",
            "question": "重组议会辩论名言：“überzeugte / Durch präzise Fakten und rhetorische Brillanz / das gesamte Parlament / der Redner”",
            "options": ["Durch präzise Fakten und rhetorische Brillanz überzeugte der Redner das gesamte Parlament.", "Der Redner das gesamte Parlament überzeugte durch präzise Fakten und Brillanz rhetorische nicht.", "Durch präzise Fakten der Redner das gesamte Parlament überzeugte und rhetorische Brillanz.", "Überzeugte der Redner durch präzise Fakten und rhetorische Brillanz das gesamte Parlament."],
            "correctIndex": 0,
            "explanation": "介词状语放句首 + 动词 (überzeugte) + 主语 (der Redner) + 宾语 (das gesamte Parlament)。"
        }
    ],
    "words": [
        ("die Rhetorik", "die", "Nomen", "unz.", "修辞学，演说雄辩之术", "Die antike Rhetorik lehrte die Kunst, das Publikum durch Argumente und Emotionen zu gewinnen.", "古希腊罗马的古典修辞学深刻揭示了演说的崇高真谛：凭借过硬铁证说服理性，依托充沛激情感动人心。"),
        ("die Debatte", "die", "Nomen", "-n", "议会公开大辩论", "Die leidenschaftliche Debatte im Bundestag spiegelte die Zerrissenheit der Bevölkerung wider.", "在联邦议院大厅展开的这场高潮迭起、针锋相对的议会大辩论，生动折射出了社会民意在改革阵痛面前的剧烈撕扯。"),
        ("der Diskurs", "der", "Nomen", "-e", "公众理性话语交往", "Ein gesunder demokratischer Diskurs verlangt das gegenseitige Zuhören und den Verzicht auf Hetze.", "维护健康健全的现代宪政民主公共讨论空间，核心底线在于学会倾听异见，并坚决向一切民粹造谣抹黑说不。"),
        ("die Kontroverse", "die", "Nomen", "-n", "争议焦点，大论争", "Die Kontroverse um die Reform des Rentensystems beschäftigt Ökonomen und Gewerkschafter seit Jahren.", "围绕法定养老金制度重构这一历史性争议焦点，宏观经济学者与全国各大工会领袖多年来已展开多轮攻防。"),
        ("die Polemik", "die", "Nomen", "-en", "论战挑衅，笔战论锋", "Übermäßige Polemik vergiftet die Debattenkultur und verhindert sachliche Kompromisse.", "过度充斥人身攻击与情绪发泄的恶性论战挑衅，不仅从根本上毒化了文明辩论土壤，更彻底堵死了务实协商的大门。"),
        ("die Argumentation", "die", "Nomen", "-en", "论证逻辑链条，推导过程", "Ihre stringente Argumentation ließ den Kritikern keinen Raum für schlüssige Gegenangriffe.", "她整篇发言那严丝合缝、如水银泻地般的缜密论证逻辑链条，根本没给台下蓄意挑刺的反对者留下任何翻盘的死角。"),
        ("das Argument", "das", "Nomen", "-e", "核心论据，论辩武器", "Ein stichhaltiges Argument wiegt schwerer als hundert wohlfeile populistische Parolen.", "一个拿得出经得起严格司法与科学重复验证的过硬客观论据，其分量胜过一万句轻佻迎合世俗的廉价民粹口号。"),
        ("das Gegenargument", "das", "Nomen", "-e", "反驳论据，抗辩理由", "Der Oppositionsführer konterte sofort mit einem brillanten ökonomischen Gegenargument.", "议会最大在野反对党党魁当即从容起立，凭借一组无可辩驳的宏观经济学硬核数据直接给出了最漂亮的反手回击。"),
        ("die Prämisse", "die", "Nomen", "-n", "论辩大前提，底层预设", "Wenn die ethische Prämisse lautet, dass jedes Leben gleich viel wert ist, folgt daraus absolute Solidarität.", "如果我们的根本伦理立论大前提是“每一个生命在上帝面前拥有无差别的绝对同等尊严”，那么全社会守望相助便是不言自明的铁律。"),
        ("die Schlussfolgerung", "die", "Nomen", "-en", "逻辑归纳推论，终审定论", "Die logische Schlussfolgerung aus den vorliegenden Fakten zwingt uns zum sofortigen Handeln.", "从所有无可辩驳的事实铁证中顺理成章推导出的唯一逻辑结论，正在以十万火急的姿态倒逼我们此刻必须雷厉风行断然采取行动。"),
        ("das Paradoxon", "das", "Nomen", "Paradoxa", "修辞悖论，自相矛盾", "In der Rede nutzte sie ein schlagendes Paradoxon: 'Wir müssen aufrüsten, um den Frieden zu bewahren.'", "在演说的高潮处，她巧妙抛出了一个令人拍案叫绝的辩证悖论：“我们今日唯有秣马厉兵备战，方能让和平的长剑永不饮血！”"),
        ("die Metapher", "die", "Nomen", "-n", "隐喻暗喻修辞", "Die sprachliche Metapher vom 'Schiff im tosenden Sturm' beschwor die Notwendigkeit des Zusammenhalts.", "主讲人巧妙化用了“暴风雨怒海狂涛中同舟共济的一叶孤舟”这一震撼人心的宏大隐喻，瞬间让全场感受到了团结一心的生死攸关。"),
        ("die Allegorie", "die", "Nomen", "-n", "讽喻，拟人象征", "Justitia mit Augenbinde und Waage ist die weltberühmte Allegorie für unparteiische Gerechtigkeit.", "眼蒙白布、左手高悬正义天平、右手紧握锋利宝剑的正义女神雕像，是全人类文明对司法裁判必须坚守客观中立最崇高生动的永恒象征。"),
        ("die Hyperbel", "die", "Nomen", "-n", "夸张修辞格", "Die bewusste Hyperbel 'Ich habe es dir schon eine Million Mal gesagt!' dient der emotionalen Verstärkung.", "在文学与演说中刻意运用诸如“我已经向你耳提面命整整一百万遍了！”此类极度放大的夸张修辞，旨在瞬间将说话者的焦灼情绪拉满。"),
        ("die Ironie", "die", "Nomen", "unz.", "反讽讽刺修辞", "Feine, feinsinnige Ironie ist die vornehmste und eleganteste Waffe des gebildeten Geistes im Streit.", "在有风度的君子论辩过招之中，运用得体、深藏不露的点睛讽刺，从来都是饱学之士手中最优雅端庄、杀人于无形的无形软剑。"),
        ("der Sarkasmus", "der", "Nomen", "unz.", "辛辣挖苦，尖刻讥讽", "Verletzender Sarkasmus zerstört das Vertrauensverhältnis und gehört nicht in ein Kollegialgespräch.", "带着恶意尖刺、专门往人伤口上撒盐的刻薄挖苦讥讽，只会彻底毒化同事同侪情谊，在任何健康的专业协作研讨中均属下下策。"),
        ("die Alliteration", "die", "Nomen", "-en", "头韵修辞格 (Stabreim)", "'Milch macht müde Männer munter' ist ein unvergänglicher Werbeslogan mit klassischer Alliteration.", "“Milch macht müde Männer munter”（牛奶让疲倦的男儿容光焕发）凭借精妙绝伦的M音头韵押韵节奏，铸就了跨越世纪的德语广告天花板神作。"),
        ("die Anapher", "die", "Nomen", "-n", "排比句首叠字修辞", "Martin Luther Kings berühmtes 'I have a dream' ist das wirkmächtigste Beispiel einer rhetorischen Anapher.", "马丁·路德·金在林肯纪念堂前连声呼喊、响彻云霄的“我有一个梦想”，是全人类演说史上运用首字排比叠句修辞感染力达到巅峰的绝唱。"),
        ("die Antithese", "die", "Nomen", "-n", "对仗反衬修辞格", "'Mehr Freiheit, weniger Staat!' ist eine klassische politische Antithese mit maximaler Signalwirkung.", "“要更多的自由，少一些官僚干预！”这句对仗工整、反差强烈的经典政治对偶口号，在选民心海中激起了犹如惊雷般的强烈认同回响。"),
        ("die Klimax", "die", "Nomen", "unz.", "层层递进修辞 (Veni, vidi, vici)", "'Ich kam, sah und siegte' ist Caesars unsterbliche rhetorische Dreierklimax von militärischem Triumph.", "凯撒大帝远征大捷后向元老院发回的千古战报“我来，我见，我征服”，凭借三段式层层递进的铿锵节奏，将大获全胜的豪迈霸气宣泄得淋漓尽致。"),
        ("die Eloquenz", "die", "Nomen", "unz.", "雄辩滔滔口才，口若悬河", "Ihre natürliche Eloquenz und ihr feuriges Charisma zogen das gesamte Auditorium in ihren Bann.", "她那与生俱来、口若悬河的卓越雄辩口才，再配以周身散发出的强大领袖气场，让诺大演讲大厅内数千名听众在长达两小时内完全如痴如醉。"),
        ("das Charisma", "das", "Nomen", "unz.", "领袖人格魅力", "Große Staatsmänner zeichnen sich durch unerschütterliche moralische Integrität und persönliches Charisma aus.", "真正能够青史留名的伟大政治领袖人物，无不兼具坚如磐石的道德廉洁操守与能够在大风大浪中稳住全民族心神的人格魅力定海神针。"),
        ("die Glaubwürdigkeit", "die", "Nomen", "unz.", "言行一致公信力 (das Ethos)", "Das rhetorische Ethos eines Redners beruht darauf, dass seine Taten mit seinen Worten übereinstimmen.", "亚里士多德修辞三要素中首屈一指的“人格公信力”(Ethos)，最根本的底气永远深植于演讲者一生言行一致、知行合一的人格硬汉底色。"),
        ("das Pathos", "das", "Nomen", "unz.", "崇高激情感染力", "Ein wohlproportionierter Hauch von moralischem Pathos verlieh der Gedenkrede tiefe Ergriffenheit.", "在国家公祭日悼念大典上，演讲者在沉静之中自然流淌出的崇高道义激情，让在场所有三军仪仗与中外元首无不潸然泪下、肃然起敬。"),
        ("der Logos", "der", "Nomen", "unz.", "严密理性逻辑说服力", "Der logos-orientierte Redner verlässt sich nicht auf billige Emotionen, sondern auf unumstößliche Fakten.", "真正崇尚“逻辑之道”(Logos)的大家风范学者，从不屑于在讲台上贩卖廉价的狗血煽情，而是全凭由无可辩驳的事实铁证铸就的逻辑巨浪平推全场。"),
        ("die Schlagfertigkeit", "die", "Nomen", "unz.", "机敏过人临场反击应对能力", "Ihre legendäre Schlagfertigkeit half ihr, feindselige Zwischenrufe im Handumdrehen lächerlich zu machen.", "她那在政坛早已名声在外的绝顶临场机敏应变反应，总能在千分之一秒内幽默反杀台下恶意起哄捣乱的不怀好意者，引得全场哄堂大笑。"),
        ("der Zwischenruf", "der", "Nomen", "-e", "现场插话起哄抗议", "Der Bundestagspräsident rügte den beleidigenden Zwischenruf eines Abgeordneten mit einem Ordnungsruf.", "面对个别在野党议员在他人发言时故意大声叫骂、进行人身攻击的无礼插话起哄，议长大锤落下，当庭依规对其亮出秩序申诫黄牌。"),
        ("die Körpersprache", "die", "Nomen", "unz.", "肢体体态语言", "Souveräne Körpersprache und ruhiger Augenkontakt signalisieren unerschütterliche innere Gelassenheit.", "舒展沉稳挺拔的仪态仪表与全场环视、坦荡温和的眼神交流，在无声之中向台下每一个人传递着发言者内心坚不可摧的处变不惊与强大自信。"),
        ("die Gestik", "die", "Nomen", "unz.", "手势配合，肢体动作", "Ausladende, unruhige Gestik wirkt nervös; gezielte, ruhige Handbewegungen unterstreichen Kernaussagen.", "在讲台上过度频繁、上蹿下跳的慌乱碎手势只会暴露出你内心的心慌意乱；唯有在点睛时刻果断挥出的沉稳手势，方能为核心论点一锤定音。"),
        ("die Mimik", "die", "Nomen", "unz.", "面部表情，眼神微表情", "Eine lebendige, zugewandte Mimik stellt vom ersten Satz an eine emotionale Brücke zum Zuhörer her.", "当演说者走上聚光灯讲台的一瞬间，生动真诚、满怀关切的面部神态便如同春风化雨，瞬间在冰冷的水泥礼堂内架起了一座直通听众心扉的心灵虹桥。"),
        ("die Modulation", "die", "Nomen", "unz.", "声调抑扬顿挫调控", "Die bewusste Modulation der Stimmlage verhindert Monotonie und hält die Aufmerksamkeit wach.", "一位深谙声学魅力的演讲大家，懂得像演奏交响乐般巧妙调控声调的抑扬顿挫与轻重缓急，彻底杜绝单调催眠，让全场自始至终高度警醒专注。"),
        ("die Sprechpause", "die", "Nomen", "-n", "演说留白停顿，此时无声胜有声", "Eine gezielt gesetzte dreisekündige Sprechpause vor dem Fazit erzeugt maximale dramatische Spannung.", "在把最终画龙点睛的雷霆结语抛出讲台前的关键一瞬，有意留出长达三秒钟针落可知的屏息沉默留白，往往能制造出震撼全场的最大戏剧张力。"),
        ("die Pointe", "die", "Nomen", "-n", "妙语包袱，画龙点睛一笔", "Mit einer geistreichen Pointe brachte er selbst seine härtesten politischen Widersacher zum Schmunzeln.", "在长篇演讲步入尾声之际，他极其从容地抖落出一个包袱妙语，其构思之精巧绝伦甚至让台下最固执刁难的死对头都忍不住咧嘴抚掌失笑。"),
        ("die Replik", "die", "Nomen", "-en", "辩论答辩词，即席反击", "In seiner fünfminütigen Replik wies der Minister alle Vorwürfe Punkt für Punkt minutiös zurück.", "在法定赋予其的五分钟最后反驳答辩陈词时段内，部长依据卷宗档案，一条一条巨细靡遗地将对手扣过来的所有脏水全数打回原形。"),
        ("die Redegewandtheit", "die", "Nomen", "unz.", "辞令敏捷流利，辩才无碍", "Seine unübertroffene Redegewandtheit machte ihn zu einem der gefürchtetsten Prozessanwälte des Landes.", "凭借在法庭上无人能及的敏捷辞令、口若悬河的大宗师级辩才，他成为了全国所有检察官在重大要案对决时最闻风丧胆的头号刑辩泰斗。"),
        ("die Schlagzeile", "die", "Nomen", "-n", "演说金句，提纲挈领金句", "Seine treffsichere Formulierung lieferte am nächsten Morgen die Titelseiten aller großen Zeitungen.", "他昨夜在集会讲坛上掷地有声抛出的那句金句，在今天清晨毫无悬念地成为了全国所有严肃大报竞相加粗刊发的头条大字。"),
        ("die Polemik", "die", "Nomen", "unz.", "笔伐口诛论战", "Sachliche Auseinandersetzung muss vor schriller persönlicher Polemik den Vorrang behalten.", "在现代文明学术与政策探讨的长河中，严肃负责、就事论事的学理事实交锋必须永远压过那些尖酸刻薄、攻讦私德的刺耳人身论战。"),
        ("die Konsensfindung", "die", "Nomen", "unz.", "凝聚各方共识", "Erfolgreiche Verhandlungsrhetorik dient letztlich nicht der Demütigung des Gegners, sondern der Konsensfindung.", "真正高段位的高维谈判雄辩艺术，其终极旨归绝非为了在台面上羞辱践踏对手的尊严，而是为了在水落石出之后求同存异、凝聚起各方妥协共识。"),
        ("das Schlusswort", "das", "Nomen", "-e", "闭幕总结词，压轴陈词", "In seinem bewegenden Schlusswort appellierte der Nobelpreisträger an das weltweite Gewissen der Menschheit.", "在全场大会的压轴总结陈词中，这位白发苍苍的诺贝尔和平奖得主手扶麦克风，向全人类良知发出了发自肺腑的和平呼唤。"),
        ("der Appell", "der", "Nomen", "-e", "庄严呼吁，向天下疾呼", "Ein flammender Appell zur Rettung der Demokratie riss das Publikum von den Sitzen.", "演说最后那声如洪钟、点燃全场的捍卫民主之庄严疾呼，让在场数千名听众在雷鸣般的轰动中齐刷刷从座椅上一跃而起、掌声如潮。"),
        ("debattieren", "kein", "Verb", "debattierte, debattiert", "展开正式公开大辩论 (über)", "Die Abgeordneten debattierten bis in die frühen Morgenstunden leidenschaftlich über das Haushaltsgesetz.", "全体人民议员就国家年度财政预算的每一笔大宗民生开支，在议会大厦红木讲坛上秉烛夜战，一直激辩到凌晨东方破晓。"),
        ("überzeugen", "kein", "Verb", "überzeugte, überzeugt", "说服，以理服人 (von)", "Eine brillante Rede überzeugt nicht durch Lautstärke, sondern durch gedankliche Tiefe und innere Wahrhaftigkeit.", "一场足以名垂青史的伟大演说，从来都不是靠在台上竭斯底里地扯着嗓子大喊大叫来吓唬人，而是全凭震撼人心的思想厚度与赤诚真理以理服人。"),
        ("entkräften", "kein", "Verb", "entkräftete, entkräftet", "驳倒，化解对方论据", "Mit einem einzigen historischen Präzedenzfall entkräftete die Juristin die gesamte Argumentationskette der Gegenseite.", "这位精通宪政史的女法学家仅仅通过援引先例法上一个铁打的经典判例，便在谈笑风生间彻底将对方精心构筑的论证城堡瞬间瓦解冰消。"),
        ("brillieren", "kein", "Verb", "brillierte, brilliert", "大放异彩，技惊四座 (mit)", "Die junge Debattantin brillierte mit messerscharfer Logik und entwaffnender Eloquenz auf dem Podium.", "初生牛犊不怕虎的年轻辩论新星在决赛讲台上，凭借剔骨尖刀般的锋利逻辑与令人缴械投降的雄辩口才，在全场掀起了惊艳四座的风暴。"),
        ("widerlegen", "kein", "Verb", "widerlegte, widerlegt", "推翻，铁证驳斥", "Die empirischen Forschungsergebnisse widerlegen die populistische Behauptung bis auf die Grundmauern.", "刚刚出炉的一手实证科学调研大数据，以泰山压顶之势将那个在网上流传甚广的民粹虚假断言彻底推翻打回原形、寸草不生。"),
        ("appellieren", "kein", "Verb", "appellierte, appelliert", "向天下疾呼呼吁 (an)", "Wir appellieren an die Vernunft aller Staats- und Regierungschefs, die diplomatischen Verhandlungen nicht abreißen zu lassen.", "我们在此向全世界所有大国领袖的人类理性庄严疾呼：在战争阴云密布的悬崖关头，绝不能轻易斩断外交和平谈判这根唯一的悬丝。"),
        ("artikulieren", "kein", "Verb", "artikulierte, artikuliert", "字正腔圆吐字，清晰表述", "In öffentlichen Reden muss man seine Anliegen prägnant, unmissverständlich und druckreif artikulieren.", "置身于成百上千闪光灯对准的公众公众演说考场之上，发言人必须把自己心中的核心诉求以字正腔圆、毫无歧义且达到出版印刷标准的语言精准表达。"),
        ("differenzieren", "kein", "Verb", "differenzierte, differenziert", "细分，严密辨析区分 (zwischen)", "Ein gebildeter Redner differenziert penibel zwischen legitimer Kritik und verhetzender Schmähung.", "一个真正有修养风骨的文明演说家，在字里行间时刻保持高度清醒自律，在正当犀利的建设性批评与造谣生事的下流诽谤之间严密划清鸿沟。"),
        ("fesseln", "kein", "Verb", "fesselte, gefesselt", "牢牢抓住听众，深深吸引", "Mit spannenden Anekdoten und packenden Beispielen fesselte die Historikerin ihr Publikum bis zur letzten Minute.", "借助一个个饱含历史温度的珍贵名人掌故与扣人心弦的生动案例，这位女历史学者让台下全神贯注的听众从头到尾屏息凝神、无一分心。"),
        ("provozieren", "kein", "Verb", "provozierte, provoziert", "刻意激将挑衅，诱敌深入", "Der Redner provozierte das Plenum ganz bewusst, um eine längst überfällige Grundsatzdebatte zu erzwingen.", "演讲人在开篇处故意抛出了一枚极具颠覆性的思想深水炸弹挑衅全场，目的正是为了强行逼迫朝野政坛展开一场早已拖延太久的根本制度大决战。"),
        ("eloquent", "kein", "Adjektiv", "-", "雄辩滔滔口才卓绝的", "Ihre eloquente Verteidigung der Menschenrechte trug ihr weltweiten Respekt und stehende Ovationen ein.", "她在联合国人权大会上那场堪称教科书级的雄辩滔滔大义陈词，在全场为她赢得了全体外长起立长达数分钟的崇高致敬。"),
        ("schlagfertig", "kein", "Adjektiv", "-", "机敏过人瞬间反杀的", "Auf jede bösartige Zwischenfrage fand der Kanzlerkandidat eine bestechend schlagfertige und humorvolle Antwort.", "面对台下记者席抛过来的每一个刁钻恶毒、暗藏陷阱的尖锐提问，这位总理候选人总能以令人拍案叫绝的机敏幽默瞬间将其化解于无形。"),
        ("stringent", "kein", "Adjektiv", "-", "逻辑环环相扣严丝合缝的", "Ein stringenter Gedankenaufbau führt den Zuhörer wie an einer unsichtbaren Leine von der These zum Fazit.", "一篇内在逻辑环环相扣、如水银泻地般的上乘演说架构，能够如同一条无形的神奇红线，牵引着台下听众的心智毫无阻滞地从立论大步迈向结语。"),
        ("bestechend", "kein", "Adjektiv", "-", "令人心悦诚服叹为观止的", "Seine bestechende Beweisführung überzeugte selbst diejenigen im Saal, die anfangs voller Skepsis waren.", "他在大屏幕前展示的那套令人拍案叫绝、无懈可击的数据推演铁证，彻底折服了台下在开场时曾满脸写满怀疑与不屑的所有挑剔同行。"),
        ("authentisch", "kein", "Adjektiv", "-", "真情实感不端不装的", "Nichts wirkt auf ein anspruchsvolles Publikum entwaffnender als ein ehrlicher, authentischer und verletzlicher Auftritt.", "在面对挑剔严苛的现代知识分子听众时，世间没有任何华丽的修辞技巧能比一个敢于走下神坛、掏出赤子之心、真情流露的真实坦诚形象更具征服力。"),
        ("chrysostomisch", "kein", "Adjektiv", "-", "妙语连珠黄金般口才的", "Mit chrysostomischer Zungenfertigkeit begeisterte der Prediger die gläubige Gemeinde.", "凭借其宛如金口约翰再世般字字玑珠、流光溢彩的绝世口才口才，这位传道名士在布道坛上令全场善男信女如饮甘露、醍醐灌顶。"),
        ("reißerisch", "kein", "Adjektiv", "-", "廉价煽情哗众取宠的", "Seriöse Politiker verzichten auf reißerische Parolen und setzen auf nüchterne Aufklärung.", "真正对国家民族前途抱有敬畏担当的严肃治国政治家，坚决唾弃一切哗众取宠、煽动仇恨的廉价口号，始终坚定选择走一条冷峻务实的理性启蒙路线。"),
        ("polemisch", "kein", "Adjektiv", "-", "充满针锋相对攻讦锋芒的", "Ein allzu polemischer Vortrag verhärtet die Fronten und verhindert jedes konstruktive Nachdenken.", "一场充斥着浓厚硝烟味与人身攻讦火药味的过度尖酸演说，只会让台下原本就对立的阵营立场更加顽固冰封，彻底扼杀任何建设性破局的可能。"),
        ("kontrovers", "kein", "Adjektiv", "-", "引发全社会白热化争议大讨论的", "Die Frage der Impfpflicht war eines der am heißesten und kontroversesten diskutierten Themen der Gegenwart.", "关于是否应当在国家层面立法推行特定传染病强制接种这一民生法理议题，在近些年的朝野广场引爆了数十年来罕见的白热化大辩论风暴。"),
        ("unwiderlegbar", "kein", "Adjektiv", "-", "颠扑不破无可辩驳的", "Dass der Klimawandel vom Menschen verursacht wird, ist eine wissenschaftlich unwiderlegbare Tatsache.", "气候变暖这一严峻现实是由人类工业文明自身无节制排放所造成的，早已成为被全世界自然科学界共同锁死的颠扑不破的铁打真理。"),
        ("differenziert", "kein", "Adjektiv", "-", "兼顾多维细致入微的", "Eine differenzierte Argumentation würdigt die Argumente der Gegenseite, bevor sie Gegenargumente vorbringt.", "一种真正体现出大师学术修养的成熟论证艺术，永远懂得在挥剑反驳之前，先以极大的耐心与尊重完整呈现并剖析对手方案的合理内核。"),
        ("prägnant", "kein", "Adjektiv", "-", "简明扼要一语中的的", "Formulieren Sie Ihre Thesen so prägnant, dass sie auch auf einem Twitter-Banner ihre volle Wucht entfalten!", "在现代信息爆炸大潮中，请务必把你的核心理论观点淬炼得如同一柄出鞘利剑般简明扼要、一语中的，让任何人在三秒钟内过目难忘！"),
        ("plakativ", "kein", "Adjektiv", "-", "通俗直观招贴画风格的", "Plakative Slogans eignen sich hervorragend für den Wahlkampf, taugen aber nicht zur Lösung komplexer Krisen.", "那些通俗直观、老头老太都能听懂的招贴画式竞选口号固然是下乡扫街拉选票的利器，但面对千头万绪的宏观经济危机时却根本开不出半副管用药方。"),
        ("pathetisch", "kein", "Adjektiv", "-", "饱含崇高悲壮史诗激情的", "Mit pathetischen Worten schwor der Staatspräsident das leidgeprüfte Volk auf harte Entbehrungen ein.", "国家元首在电视转播前动用了极其沉郁悲壮的史诗般语言，号召全体坚韧不屈的英雄同胞做好在漫长严冬中勒紧裤带共克时艰的战斗准备。"),
        ("zugewandt", "kein", "Adjektiv", "-", "平易近人充满亲和力的", "Ein zugewandter Blickkontakt und ein offenes Lächeln nehmen dem Dialogpartner jede anfängliche Befangenheit.", "一道平易近人、充满真诚尊重的温暖注视目光，再配合一抹发自肺腑的友善微笑，瞬间便能把坐在谈判桌对面的异国客商心底最后的戒备彻底融化。"),
        ("treffsicher", "kein", "Adjektiv", "-", "一针见血百步穿杨的", "Mit einer treffsicheren Metapher legte sie den Finger genau in die schmerzhafteste Wunde des Systems.", "凭借一个百步穿杨、一针见血的生动比喻，她宛如手持柳叶手术刀的外科圣手，极其精准地直接按在了整个官僚体制多年来最致命的脓疮隐疾痛处。"),
        ("entwaffnend", "kein", "Adjektiv", "-", "令人缴械投降难以抗拒的", "Ihre entwaffnende Ehrlichkeit im Eingestehen eigener Schwächen nahm den Kritikern augenblicklich allen Wind aus den Segeln.", "她在聚光灯前坦然承认自己执政失误的那份令人缴械投降的非凡真诚，瞬间便让台下磨刀霍霍准备大做文章的反对派媒体彻底哑火熄火。"),
        ("konstruktiv", "kein", "Adjektiv", "-", "富有建设性促成解决的", "Statt gegenseitiger Schuldzuweisungen braucht die Stadtpolitik nun einen sachlichen und konstruktiven Dialog.", "与其在电视机镜头前无休止地上演互相推卸责任的低俗政治扯皮大戏，当下的市政厅议会比任何时候都更迫切需要一场就事论事、富有建设性的务实大商讨。"),
        ("unumstößlich", "kein", "Adjektiv", "-", "铁证如山无可动摇的", "Die durch DNA-Abgleich gesicherten Beweise lieferten dem Gericht eine unumstößliche Grundlage für das Urteil.", "由国家物证中心通过双盲DNA高通量测序比对锁死的铁证如山法医学物证链，为合议庭法官作出终审死刑判决提供了坚如磐石、无可动摇的铁证支柱。"),
        ("wirkungsvoll", "kein", "Adjektiv", "-", "成效斐然行之有效的", "Eine gut strukturierte Rede ist das wirkungsvollste Instrument, um Menschen für große Ideale zu begeistern.", "一篇布局严密、起承转合浑然天成的传世演说杰作，是全人类手中能够将千百万人心底沉睡的英雄理想彻底点燃的最成效卓著的神奇乐器。")
    ]
}

# LESSON 15: Goethe B2 / TestDaF Prüfungstraining (70 words)
L15 = {
    "id": "B2_L15",
    "title": "第15课：歌德 B2 & TestDaF 德福备考终极冲刺与高分攻略 (Goethe B2 & TestDaF)",
    "summary": "掌握学术图表描述语块 (Grafikbeschreibung)、议论文高阶论证架构与歌德B2/德福满分核心词汇",
    "grammar": {
        "title": "学术图表描述与议论文高分语篇体系 (Grafikbeschreibung & Wissenschaftliches Argumentieren)",
        "sections": [
            {
                "heading": "1. 德福/歌德B2图表描述必背三段论：",
                "content": "• 来源与主题：Die vorliegende Grafik gibt Auskunft über ... und stammt vom Statistischen Bundesamt aus dem Jahr ...\n• 数据动态：Die Zahl ist im Zeitraum von ... bis ... kontinuierlich um ... Prozent gestiegen / um die Hälfte eingebrochen.\n• 极值与比较：An der Spitze liegt ..., während ... das Schlusslicht bildet."
            },
            {
                "heading": "2. 高阶学术论证与平衡论辩：",
                "content": "• Befürworter heben hervor, dass ... Demgegenüber wenden Kritiker ein, dass ...\n• Alles in allem komme ich zu dem Schluss, dass die Vorteile die Nachteile überwiegen."
            }
        ]
    },
    "quiz": [
        {
            "id": "B2_L15_Q1",
            "type": "GRAMMAR_FILL",
            "question": "Die vorliegende Grafik ______ (liefern) Aufschluss über die Entwicklung des internationalen Handels.",
            "options": ["gibt", "macht", "stellt", "bringt"],
            "correctIndex": 0,
            "explanation": "学术图表描述标准固定搭配：Aufschluss geben über (+Akk.) / Auskunft geben über (+Akk.)。"
        },
        {
            "id": "B2_L15_Q2",
            "type": "MEANING_SELECT",
            "question": "德福写作与歌德B2中表达“位列倒数第一，垫底”的高分学术表达是：",
            "options": ["das Schlusslicht bilden", "an der Spitze stehen", "im Mittelfeld rangieren", "stagnieren"],
            "correctIndex": 0,
            "explanation": "das Schlusslicht bilden 指在统计图表排名中“位居榜尾、垫底”。"
        },
        {
            "id": "B2_L15_Q3",
            "type": "GRAMMAR_FILL",
            "question": "Im Vergleich zum Vorjahr hat sich der Wert nahezu ______ (doppelt / verdoppelt / gedoppelt).",
            "options": ["verdoppelt", "doppelt", "gedoppelt", "verzweifacht"],
            "correctIndex": 0,
            "explanation": "表达数据翻倍使用及物反身动词完成时：hat sich nahezu verdoppelt。"
        },
        {
            "id": "B2_L15_Q4",
            "type": "LISTENING_MCQ",
            "question": "“Wägt man alle Argumente sorgfältig ab, so überwiegen die langfristigen Vorteile des Ausbaus.” 的论证结语是：",
            "options": ["综合权衡所有论据，该扩建工程所带来的长远优势占据明显上风。", "扩建工程彻底弊大于利。", "所有论据均被推翻。", "政府应立即取消该工程。"],
            "correctIndex": 0,
            "explanation": "abwägen = 权衡斟酌，überwiegen = 占据压倒性上风。"
        },
        {
            "id": "B2_L15_Q5",
            "type": "SENTENCE_BUILDER",
            "question": "重组学术图表转折句式：“verzeichnete der Sektor / Während die Industrie stagnierte, / ein enormes Wachstum”",
            "options": ["Während die Industrie stagnierte, verzeichnete der Sektor ein enormes Wachstum.", "Verzeichnete der Sektor ein enormes Wachstum während die Industrie stagnierte nicht.", "Während stagnierte die Industrie, verzeichnete ein enormes Wachstum der Sektor.", "Ein enormes Wachstum der Sektor verzeichnete, während die Industrie stagnierte."],
            "correctIndex": 0,
            "explanation": "从句居首 (Während die Industrie stagnierte) + 主句动词在第一位 (verzeichnete) + 主语 (der Sektor) + 宾语 (ein enormes Wachstum)。"
        }
    ],
    "words": [
        ("das Zertifikat", "das", "Nomen", "-e", "高阶语言证书 (Goethe-Zertifikat B2 / TestDaF)", "Das Goethe-Zertifikat B2 öffnet Türen zu deutschen Universitäten und dem globalen Arbeitsmarkt.", "一张盖有歌德学院火漆钢印的B2语言等级合格证书，是叩响德国顶尖公立综合性大学校门与跨国名企高薪大门的黄金金钥匙。"),
        ("der TestDaF", "der", "Nomen", "unz.", "德福考试 (Test Deutsch als Fremdsprache)", "Der TestDaF ist die international anerkannte sprachliche Eintrittskarte für das Studium in Deutschland.", "德福全国统考(TestDaF)是德国高校校长联席会议与学术交流中心官方认可的外国留学生赴德攻读学位必备的最高语言入场券。"),
        ("das Niveau", "das", "Nomen", "-s", "语言能力层级 (GER B2)", "Das Niveau B2 des Gemeinsamen Europäischen Referenzrahmens bescheinigt selbstständige Sprachverwendung.", "欧洲共同语言参考框架(CEFR)下设的B2等级标准，官方严肃认定持有人已完全具备高阶、独立、游刃有余的专业语言运用素养。"),
        ("die Prüfung", "die", "Nomen", "-en", "等级大考，结业统考", "Die B2-Prüfung verlangt höchste Konzentration, differenzierten Wortschatz und präzise Grammatik.", "面对歌德B2这道含金量极高的大考，考生必须在考场全神贯注，熟练调用海量差异化的高阶词汇并恪守严谨无瑕的语法底线。"),
        ("das Modul", "das", "Nomen", "-e", "测试模块 (Lesen, Hören, Schreiben, Sprechen)", "Jedes der vier Module kann bei Bedarf einzeln wiederholt werden, bis alle Teilbereiche bestanden sind.", "听说读写四大核心应试模块实行人性化制度设计，考生可根据自身强弱项针对未过关单科模块反复刷分，直至全科功德圆满。"),
        ("das Leseverstehen", "das", "Nomen", "unz.", "长篇学术阅读理解", "Im Leseverstehen müssen anspruchsvolle Kommentare und wissenschaftliche Fachartikel analysiert werden.", "在德福与歌德长篇阅读理解考场上，考生必须在分秒必争的高压时间倒计时下，快速吃透长篇学术期刊论文与犀利时评的核心脉络。"),
        ("das Hörverstehen", "das", "Nomen", "unz.", "高阶学术听力理解", "Das Hörverstehen simuliert authentische universitäre Vorlesungen und hitzige Expertendiskussionen im Radio.", "听力理解模块高度还原德国一流名校大阶梯教室内的硬核教授前沿学术讲座原声，以及德国公共电台专家圆桌派的激烈交锋。"),
        ("der schriftliche Ausdruck", "der", "Nomen", "unz.", "学术书面写作表达", "Der schriftliche Ausdruck besteht aus einer präzisen Grafikbeschreibung und einer fundierten dialektischen Stellungnahme.", "在书面笔试大作答卷上，考生必须在规定时间内一气呵成完成两项重头戏：极其严谨的学术图表量化描述与立论深刻的辩证议论文。"),
        ("der mündliche Ausdruck", "der", "Nomen", "unz.", "即兴学术口语表达", "Im mündlichen Ausdruck beweisen Kandidaten ihre Spontaneität, Eloquenz und argumentative Überzeugungskraft.", "在口语机考人机对话或考官面对面面试大厅中，考生必须向主考官淋漓尽致地展现自身即兴反应、滔滔雄辩与逻辑说服的真才实学。"),
        ("die Grafik", "die", "Nomen", "-en", "统计图表，学术图表", "Die vorliegende Grafik illustriert die demografische Entwicklung in Deutschland über die letzten fünfzig Jahre.", "试卷上呈现的这幅权威统计图表，以精准的曲线坐标生动展示了过去半个世纪以来德国人口结构演变的历史变迁脉络。"),
        ("das Schaubild", "das", "Nomen", "-er", "信息图，示意图表", "Das Schaubild veranschaulicht die komplexen Stoffkreisläufe in einem modernen Industriepark.", "这幅结构严谨的信息图解示意图，极其直观明了地向考生阐明了现代化零碳工业产业园区内部错综复杂的物质全闭环循环流程。"),
        ("das Diagramm", "das", "Nomen", "-e", "数据图，坐标图表", "Ein Säulendiagramm eignet sich hervorragend, um diskrete Vergleichswerte verschiedener Länder darzustellen.", "垂直柱状柱形图是进行多国离散横向指标数据大PK与量化比对时，在学术论文中被最广泛采纳的经典制图典范。"),
        ("die Achse", "die", "Nomen", "-n", "坐标轴 (die X-Achse, die Y-Achse)", "Auf der vertikalen Achse ist der prozentuale Anteil der erneuerbaren Energien an der Stromerzeugung abgetragen.", "在直角坐标系纵立着的Y轴之上，精密标注着可再生清洁能源在全社会发电总装机容量中所占据的动态百分比份额。"),
        ("der Maßstab", "der", "Nomen", "-e", "比例尺，衡量尺度", "Die Daten wurden in absoluten Zahlen sowie in Relation zur Gesamtbevölkerung als Maßstab erfasst.", "为了杜绝统计口径偏差，全套调研数据不仅列出了绝对实物量指标，更引入人均占有量作为科学衡量尺度的基准参照。"),
        ("der Trend", "der", "Nomen", "-s", "宏观演变趋势", "Aus der Zeitreihe lässt sich ein eindeutiger, stetig ansteigender Trend zugunsten der Elektromobilität ablesen.", "从长达十年的连续时间序列折线图中，任何人均能一眼洞悉出一个不可逆转、扶摇直上的压倒性大趋势：新能源电车正在横扫市场。"),
        ("die Tendenz", "die", "Nomen", "-en", "动态走势，潜在倾向", "Die Grafik zeigt eine besorgniserregende Tendenz: Die Jugendarbeitslosigkeit klettert im Krisenjahr rasant.", "这幅折线走势图亮起了一道令人揪心的警红灯：在经济逆风危机大年里，全社会青年失业率竟然呈现出野蛮狂飙的恶性走势。"),
        ("der Anstieg", "der", "Nomen", "-e", "显著上升，增长上扬", "Ein steiler Anstieg der Immobilienpreise machte den Wohnungskauf für junge Familien nahezu unerschwinglich.", "一线大都市商业住宅销售单价那犹如火箭发射般的陡峭暴涨，让千千万万刚步入职场的年轻家庭在安居梦想面前望洋兴叹。"),
        ("der Rückgang", "der", "Nomen", "-e", "明显回落，下挫收缩", "Nach der Einführung strenger Umweltgesetze war ein spürbarer Rückgang der Feinstaubemissionen zu verzeichnen.", "在国家以雷霆手腕正式落地施行最严苛环保法典之后，全域空气质量监测站实测到的PM2.5工业烟尘排放量迎来了立竿见影的显著下挫。"),
        ("der Höchststand", "der", "Nomen", "-e", "历史最高峰值", "Im vergangenen Jahr erreichte der Anteil internationaler Studierender in Deutschland einen historischen Höchststand.", "在刚刚过去的历史大年里，在德意志各大一流高校攻读学位的海外国际留学生绝对总人数历史性地冲上了历史最高峰值。"),
        ("der Tiefststand", "der", "Nomen", "-e", "历史最低谷底值", "Während des Lockdowns fiel der internationale Flugverkehr auf einen nie dagewesenen Tiefststand.", "在疫情突发导致全球口岸紧急熔断的极度冰封时刻，跨国洲际民航客运出港执飞航线跌落到了人类航空史上绝无仅有的谷底冰点。"),
        ("der Spitzenreiter", "der", "Nomen", "-", "位列榜首第一名", "Bei den weltweiten Patentanmeldungen für Zukunftstechnologien ist das Forschungsinstitut der unangefochtene Spitzenreiter.", "在前沿颠覆性高精尖硬核技术领域全要素发明专利国际PCT申请排行榜上，该国家实验室是无可撼动的头号榜首领头羊。"),
        ("das Schlusslicht", "das", "Nomen", "-er", "位列榜尾倒数第一", "Bei der Digitalisierung der Verwaltung bildet die Behörde im bundesweiten Vergleich leider das traurige Schlusslicht.", "在由权威第三方智库发布的全国各级政府政务网络数字化便民改革综合效能大比拼红黑榜上，该局不幸沦为了全网倒数第一的垫底笑柄。"),
        ("der Durchschnitt", "der", "Nomen", "-e", "统计平均水平", "Das durchschnittliche Einstiegsgehalt für Masterabsolventen der Ingenieurwissenschaften liegt über dem Bundesdurchschnitt.", "从德国一流工科名校工科硕士讲台昂首走出的毕业生，其首期入职试用期起薪水准远远甩开了全国各行业工种平均水平一大截。"),
        ("die Mehrheit", "die", "Nomen", "-en", "压倒性大多数", "Eine überwältigende Mehrheit der befragten Experten befürwortet eine zügige Reform der Energiebesteuerung.", "在接受匿名权威行业问卷穿透调研的数百名资深能源经济学者中，高达八成以上的压倒性绝大多数一致力挺加速推进能源税制大刀阔斧改革。"),
        ("die Minderheit", "die", "Nomen", "-en", "少数派群体", "Lediglich eine verschwindend geringe Minderheit sprach sich für eine Rückkehr zu fossilen Brennstoffen aus.", "在大会不记名大盘表决现场，仅有不足百分之二微不足道的极少数抱残守缺者，依然顽固地主张开历史倒车重回高污染燃煤老路。"),
        ("die Quote", "die", "Nomen", "-n", "比率，份额指标", "Die Akademikerquote ist in den letzten zwei Jahrzehnten in fast allen Industriestaaten kontinuierlich geklettert.", "在过去风云变幻的二十年漫长岁月里，全社会拥有大学本科学士及以上文凭的高学历人口占总人口的比率在各大工业国均呈稳健攀升态势。"),
        ("der Prozentsatz", "der", "Nomen", "-e", "百分比，百分数", "Der Prozentsatz der Vollzeitbeschäftigten, die regelmäßig im Homeoffice arbeiten, hat sich seit der Pandemie verdreifacht.", "在全职白领正规就业大军之中，每周享有固定天数合法居家远程灵活办公特权的人群百分比，在后疫情时代迎来了惊人的三倍翻番暴增。"),
        ("die Proportion", "die", "Nomen", "-en", "比例关系，匀称度", "Die Proportionen im Bundeshaushalt verschoben sich massiv zugunsten von Zukunftsinvestitionen in Bildung und Klimaschutz.", "在最新由联邦财政部呈递国家议会审议的年度账单草案中，各项支出结构的比例配额历史性地向着教育培优与绿色减排两大核心底盘大步倾斜。"),
        ("die Verdopplung", "die", "Nomen", "-en", "翻倍翻一番", "Innerhalb von fünf Jahren kam es zu einer schier unglaublichen Verdopplung der installierten Photovoltaikleistung.", "在短短五年如白驹过隙的时间窗口内，全国范围内并网运行的分布式太阳能光伏累计装机总功率奇迹般地实现了令人叹为观止的彻底翻倍翻番。"),
        ("die Halbierung", "die", "Nomen", "-en", "减半拦腰斩断", "Das erklärte Ziel der Bundesregierung ist die Halbierung der bürokratischen Antragszeiten bei Unternehmensgründungen.", "本届内阁向全社会工商业青年才俊做出的庄严政治许诺坚如磐石：誓要把硬科技初创企业注册审批的官方平均法定等待时限彻底拦腰减半砍掉50%。"),
        ("die Einleitung", "die", "Nomen", "-en", "学术议论文引言开头", "Eine gelungene Einleitung benennt prägnant das Thema, skizziert die Problematik und formuliert die eigene Leitfrage.", "一篇堪称范文典范的高分学术议论文开头引言，必须以精悍洗练的笔力开门见山点题、勾勒现实矛盾张力，并抛出贯穿全篇的核心学术设问。"),
        ("die Überleitung", "die", "Nomen", "-en", "段落之间逻辑承上启下过渡", "Eine geschmeidige Überleitung verbindet die Interpretation der Grafik nahtlos mit der nachfolgenden Pro-und-Contra-Debatte.", "一句设计巧妙、行云流水般的承上启下过渡金句，能够将前一段枯燥的数据图表量化分析与后半段波澜壮阔的辩证思辨正反方大博弈天衣无缝地焊成一体。"),
        ("die Gegenüberstellung", "die", "Nomen", "-en", "正反两方论据对垒比照", "Die Gegenüberstellung von Pro- und Contra-Argumenten bildet das Herzstück jeder anspruchsvollen dialektischen Erörterung.", "把正方力挺的坚实理由与反方犀利的质疑论据在同一张大天平上实施全景式的严密对垒比照，构成了任何一篇高阶德语议论文最核心的硬核灵魂。"),
        ("das Fazit", "das", "Nomen", "-s", "全文画龙点睛大总结，总论", "Im Fazit fasst der Autor die Kernergebnisse nochmals prägnant zusammen und wagt einen fundierten Zukunftsausblick.", "在文章步入尾声的总论收官段落中，作者再次以高屋建瓴的大师笔意对全篇核心发现作凝练总结，并奉上一份充满真知灼见的未来战略前瞻。"),
        ("der Standpunkt", "der", "Nomen", "-e", "作者鲜明立场观点", "Aus meinem Standpunkt überwiegen die gesamtgesellschaftlichen Chancen der Digitalisierung die damit einhergehenden Risiken bei weitem.", "从我个人经过深思熟虑后的严肃学术立场审视出发：全面拥抱数字化转型所能赋予全社会的时代红利与发展机遇，显而易见远远超越了其附带的次生风险。"),
        ("die Stellungnahme", "die", "Nomen", "-n", "官方立场声明，书面表态", "In seiner ausführlichen schriftlichen Stellungnahme forderte der Verband eine sofortige finanzielle Nachbesserung.", "在向联邦立法委员会正式递交的长达数万言的详尽书面意见表中，行业联合会代表千万工商业者义正词严地要求必须即刻出台二次财政补贴纠偏方案。"),
        ("das Zeitmanagement", "das", "Nomen", "unz.", "考场答题答卷时间严密管控", "Ein diszipliniertes Zeitmanagement sichert das vollständige Ausfüllen aller Aufgabenblätter vor dem Schlusspfiff.", "在分秒必争、考题体量巨大的德福大考现场，恪守钢铁般严密的时间管控战术节奏，是确保你在终场哨吹响前从容答完并复核全部答题卡的制胜法宝。"),
        ("die Prüfungsangst", "die", "Nomen", "unz.", "考前怯场心慌考试焦虑", "Gezielte Atemtechniken und realitätsnahe Prüfungssimulationen im Vorfeld kurieren jede noch so lähmende Prüfungsangst.", "只要在考前冲刺阶段多做几套全真模拟仿真模考全流程大演练并掌握科学的深呼吸心法，任何平日里看似令人生畏的考前心慌焦虑都将不药而愈。"),
        ("die Souveränität", "die", "Nomen", "unz.", "游刃有余从容自信", "Mit bemerkenswerter sprachlicher Souveränität meisterte die Kandidatin den anspruchsvollen mündlichen Prüfungsteil.", "在面对考官环环相扣、步步紧逼的连环即兴高难发问时，这位女考生展现出了令人叹服的语言运用游刃有余大家风范，以满分战绩昂首走出考场。"),
        ("die Traumnote", "die", "Nomen", "-n", "梦寐以求的满分高分", "Mit der Traumnote 'TestDaF 5x4' in der Tasche erfüllte er sich seinen Lebenstraum von einem Medizinstudium an der Charité.", "怀揣着各科全满分“德福全5分”的梦幻般殿堂级成绩单，他终于在今天圆了自己毕生梦寐以求踏入享誉全球的柏林夏里特医学院攻读医学博士的夙愿。"),
        ("darstellen", "kein", "Verb", "stellte dar, dargestellt", "图表呈现展示", "Das vorliegende Säulendiagramm stellt die Verteilung der staatlichen Forschungsgelder auf verschiedene Disziplinen dar.", "试卷中所展示的这幅多色柱状图，条理井然、层次分明地向考生完整呈现了国家公共科研专项基金在各个前沿学科门类之间的配额划分格局。"),
        ("veranschaulichen", "kein", "Verb", "veranschaulichte, veranschaulicht", "直观生动展现", "Zahlreiche anschauliche Fallstudien veranschaulichen die praktische Anwendung des komplexen theoretischen Modells.", "穿插在各章节之中大量鲜活生动的真实行业一线经典深度案例，极其直观生动地向读者展现了这套深奥理论数学模型在实战中的威力。"),
        ("verdeutlichen", "kein", "Verb", "verdeutlichte, verdeutlicht", "阐明，使跃然纸上", "Die Grafik verdeutlicht mit aller Schärfe, dass die CO2-Emissionen im Verkehrssektor seit Jahren nicht gesunken sind.", "这组由国家环境署发布的权威硬核监测曲线极其残酷地向世人阐明：过去十数年里交通运输行业的碳排放总量不仅毫无起色，反而在原地踏步。"),
        ("überwiegen", "kein", "Verb", "überwog, überwogen", "占据压倒性优势 (die Vorteile überwiegen)", "Nach sorgfältiger Abwägung aller Vor- und Nachteile bin ich fest davon überzeugt, dass die positiven Effekte überwiegen.", "在将正反两方面的全部红利与潜在弊端置于天平两侧进行彻夜反复权衡之后，我深信不疑地得出定论：该方案所能激发的长期正向动能占据绝对压倒性上风。"),
        ("kontern", "kein", "Verb", "konterte, gekontert", "机敏反驳反击", "Auf die scharfe Kritik der Gutachter konterte der Doktorand mit unanfechtbaren labortechnischen Messergebnissen.", "面对盲审评审委员会权威专家在答辩现场抛出的极其苛刻的连环诘难质疑，在读博士生不慌不忙，直接调出实验室无可辩驳的原始光谱实测数据漂亮反杀。"),
        ("belegen", "kein", "Verb", "belegte, belegt", "拿出确凿证据佐证", "Können Sie diese weitreichende kühne Behauptung auch durch repräsentative statistische Erhebungen belegen?", "请问您能否为您方才在讲坛上提出的这项石破天惊的大胆宏大主张，当场拿出具有全国普查代表性的大数据权威统计报告作为坚实佐证？"),
        ("strukturieren", "kein", "Verb", "strukturierte, strukturiert", "布局谋篇，构筑逻辑框架", "Wer seinen Aufsatz klar strukturiert, erleichtert den Korrektoren die Lektüre und sammelt wertvolle Extrapunkte.", "凡是懂得在动笔写下第一个字母前先花五分钟在草稿纸上把全文脉络骨架搭建得条理分明的聪明考生，在阅卷考官眼中无异于直接提前锁定了结构加分项。"),
        ("differenzieren", "kein", "Verb", "differenzierte, differenziert", "多维度兼顾思辨", "Man muss in der Debatte feinfühlig zwischen kurzfristigen Übergangskosten und dem dauerhaften volkswirtschaftlichen Nutzen differenzieren.", "置身于这场事关国运的大辩论漩涡之中，严肃的学者必须明察秋毫，在转型初期不可避免要承受的阵痛代价与未来惠及子孙的持久国民经济红利之间作深层辩证辨析。"),
        ("abwägen", "kein", "Verb", "wog ab, abgewogen", "深谋远虑全面权衡", "Entscheidungsträger müssen die ökonomischen Interessen von heute gegen die Überlebensinteressen von morgen gewissenhaft abwägen.", "手握千钧治国大权的执政先锋必须时刻把良知置于案头，在满足当代人眼前短暂的经济利益冲动与捍卫后世子孙赖以安身立命的长远生存权益之间实施良心大权衡。"),
        ("bestehen", "kein", "Verb", "bestand, bestanden", "全科通关大考", "Wer mit Ausdauer, System und Leidenschaft lernt, wird das Zertifikat B2 mit Bravour und Bestnoten bestehen!", "任何一位始终怀揣对德意志语言文化博大精深魅力的炽热热爱、恪守科学学习系统并挥洒汗水者，必将在即将到来的B2等级大考中一路所向披靡、旗开得胜！"),
        ("präzise", "kein", "Adjektiv", "-", "严谨精准无误的", "Eine präzise Begriffsdefinition ist das absolute A und O für jedes erfolgreiche wissenschaftliche Arbeiten.", "在学术论文创作与高等学术研究的世界里，开宗明义对核心概念给出无懈可击、极其严谨精准的定义界定，永远是被奉为第一铁律的生命线。"),
        ("fundiert", "kein", "Adjektiv", "-", "底蕴深厚经得起检验的", "Ihre Argumente waren so fundiert und stichhaltig, dass es der Gegenseite die Sprache verschlug.", "她当场所抛出的论据论述在学理与事实上是如此底蕴深厚、坚不可摧，以至于让坐在辩论席对面的挑战者一时间瞠目结舌、哑口无言。"),
        ("schlüssig", "kein", "Adjektiv", "-", "逻辑自洽顺理成章的", "Der rote Faden zog sich vollkommen schlüssig von der Einleitung bis zum abschließenden Fazit durch.", "整篇议论文思维清晰的“逻辑红线”如同一条贯穿首尾的黄金经脉，无比自洽严密地从开篇引言一直行云流水顺畅延伸至最终的总论收官。"),
        ("kontinuierlich", "kein", "Adjektiv", "-", "持之以恒稳步持续的", "Ein kontinuierlicher Wortschatzerwerb Tag für Tag schlägt jedes panische Bulimielernen in der letzten Nacht.", "长年累月如小桥流水般每日打卡吸收二三十个高阶核心词汇的持之以恒定力，其最终沉淀出的真实语言实力，足以把任何企图在考前通宵死记硬背的投机分子甩出十条街。"),
        ("drastisch", "kein", "Adjektiv", "-", "断崖式剧烈的，重拳出击的", "Ein drastischer Kurseinbruch an den Weltbörsen vernichtete über Nacht Hunderte Milliarden an Buchwerten.", "受地缘政治突发黑天鹅突袭，全球各大主要证券交易所股指遭遇断崖式惨烈暴跌，在短短一夜之间将数以千亿美元计的浮盈账面资产无情蒸发扫荡一空。"),
        ("stetig", "kein", "Adjektiv", "-", "稳如泰山持续向上的", "Das stetige Wachstum des Bildungssektors belegt den unstillbaren gesellschaftlichen Wissensdurst.", "在过去数年经济阴晴不定的周期中，全社会对终身职业教育进修培训领域常年保持的稳步向上强劲需求，生动证明了大众对知识赋能抵御危机的如饥似渴。"),
        ("signifikant", "kein", "Adjektiv", "-", "在统计学上极其显著的", "Die Abweichungen zwischen beiden Testgruppen waren statistisch hochgradig signifikant.", "两组受试者在历经长达半年的新型神经认知康复强化训练之后，在最终对比量表上的得分差异在统计学上展现出了置信度极高的极其显著性水平。"),
        ("marginal", "kein", "Adjektiv", "-", "微不足道略微边缘的", "Der Unterschied von 0,1 Prozentpunkten ist in der Praxis vollkommen vernachlässigbar und marginal.", "在宏观经济体量高达数万亿欧元的庞大总账本中，仅仅零点一个百分点的微小账面统计扰动，在实际战略决策中完全可以被视作微不足道的毛毛雨忽略不计。"),
        ("repräsentativ", "kein", "Adjektiv", "-", "具有大样本普查代表性的", "Die empirische Umfrage basiert auf einer repräsentativen Stichprobe von über fünftausend Bundesbürgern.", "该国家级社会学民调报告的大数据底座，扎扎实实奠基于覆盖全国不同联邦州、不同收入年龄阶层的超过五千名成年公民的代表性随机抽样大样本。"),
        ("überzeugend", "kein", "Adjektiv", "-", "令人心悦诚服信服的", "Mit einer inhaltlich und sprachlich überzeugenden Leistung sicherte sich der Kandidat die Bestnote.", "凭借在答题卡上所展现出的在学术思辨思想深度与德语高级行文表达上无可挑剔的卓越统治力，这位考生毫无悬念地斩获了全优通关大奖。"),
        ("eloquent", "kein", "Adjektiv", "-", "辞令典雅口才绝伦的", "Ihr eloquenter Schreibstil im Aufsatz verriet eine jahrelange intensive Beschäftigung mit klassischer Literatur.", "他在德福命题议论文写作中所展现出的那种字里行间流淌出的典雅严密、博大精深的辞令文风，一眼便能让阅卷教授领略出其背后十数载浸淫古典文学名著的非凡功力。"),
        ("kompetent", "kein", "Adjektiv", "-", "专业过硬胜任有余的", "Er ist ein fachlich hochkompetenter Ansprechpartner für alle Fragen rund um das Auslandsstudium.", "在涉及如何申请德国顶级公立大学全额奖学金、如何攻破APS审核与外管局签证面签等全部全流程死结上，他是一位在业内公认经验最老到、最值得信赖的权威咨询专家。"),
        ("selbstständig", "kein", "Adjektiv", "-", "完全能够自立独立完成的", "Das Zertifikat B2 bescheinigt dem Inhaber die Fähigkeit zur vollkommen selbstständigen Sprachverwendung im Beruf.", "歌德B2权威资质认证以最庄严的官方形式向全球各大跨国雇主证明：该持有人在职场环境下完全具备无需依赖他人翻译、独立自主处理任何复杂专业事务的成熟外语能力。"),
        ("ambitioniert", "kein", "Adjektiv", "-", "雄心勃勃志存高远的", "Das ambitionierte Reformpaket soll das Bildungswesen des Landes innerhalb einer Dekade an die Weltspitze führen.", "这项由内阁重磅出台的雄心勃勃的宏大教育强国一揽子改革蓝图，誓要在接下来的整整十年黄金窗口期内，将本国国民教育综合创新实力强力推进世界第一梯队。"),
        ("diszipliniert", "kein", "Adjektiv", "-", "恪守高度自律精神的", "Mit disziplinierter täglicher Übungsroutine wirst du die hohen Hürden der B2-Prüfung spielend meistern.", "只要你能够在接下来的强化冲刺备考岁月里耐得住寂寞、恪守雷打不动的严谨每日模块化实战演练作风，那么在别人眼中看似高不可攀的B2大考龙门，对你而言都将如履平地。"),
        ("resilient", "kein", "Adjektiv", "-", "处变不惊高抗压韧性的", "Ein resilienter Geist lässt sich durch eine überraschende, knifflige Prüfungsaufgabe nicht aus der Ruhe bringen.", "一位真正具备大将之风、拥有超高心理韧性的顶级考生，即便在考场第一题便迎面撞上从未见过的冷门怪题刁钻设问，也绝不会慌乱阵脚，而是能够瞬间气定神闲从容破局。"),
        ("akademisch", "kein", "Adjektiv", "-", "象牙塔学术标准的", "Die TestDaF-Aufgaben verlangen das Verfassen von Texten nach strengen akademischen Konventionen.", "德福书面表达与口语表达所考查的全部题型，其评卷给分唯一严格遵循的硬指标，正在于考生的表述是否百分之百符合德语区一流大学学术界通行的严密治学规范与文风。"),
        ("dialektisch", "kein", "Adjektiv", "-", "具备两分法辩证思维张力的", "Eine gelungene dialektische Erörterung wägt gegensätzliche Positionen mit meisterhafter Ausgewogenheit ab.", "一篇被奉为模范样板的优秀双向辩证议论文大作，其最引人入胜的魅力，正在于能够以大师级的公允与深邃视野将相互冲突对立的两派观点剖析得入木三分、兼收并蓄。"),
        ("erfolgreich", "kein", "Adjektiv", "-", "胜利通关凯旋而归的", "Wir gratulieren allen Absolventen von ganzem Herzen zum erfolgreichen Abschluss dieses intensiven Kurses!", "我们全体教研团队满怀由衷的自豪与欣慰，发自肺腑地热烈祝贺每一位刻苦自强、圆满通关这场魔鬼强化集训的优秀学子凯旋夺魁、前程似锦！"),
        ("zukunftsfähig", "kein", "Adjektiv", "-", "能够从容应对未来风云挑战的", "Solide Deutschkenntnisse auf B2-Niveau sind Ihr zukunftsfähigstes Kapital für Studium, Karriere und Leben!", "一口扎实精湛、达到欧洲主流社会高度公认的B2高阶德语真功夫，将成为你漫长一生在赴德研学、纵横跨国职场与走向世界大舞台征途上最坚不可摧、最具生命力的传世财富！")
    ]
}

# Now assemble full Part 3
all_part3 = [L11, L12, L13, L14, L15]

print("Part 3 assembled. Total lessons:", len(all_part3))
for l in all_part3:
    print(f"  {l['id']}: {len(l['words'])} words - {l['title']}")

out_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "b2_part3.py")
with open(out_file, "w", encoding="utf-8") as f:
    f.write("#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n")
    f.write('"""\nB2 Part 3: Lessons 11 to 15 (350 words: 5 x 70 words)\n"""\n\n')
    f.write("LESSONS_B2_PART3 = " + pprint.pformat(all_part3, width=120, compact=False) + "\n")

print(f"Saved {out_file} successfully!")
