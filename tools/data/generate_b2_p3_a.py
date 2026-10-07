#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator part A for tools/data/b2_part3.py (Lessons 11 and 12, 70 words each).
"""

L11 = {
    "id": "B2_L11",
    "title": "第11课：批判性传媒素养、新闻真实与虚假信息 (Medienkompetenz & Fake News)",
    "summary": "掌握主观情态动词 (Subjektive Modalverben: sollen, wollen, müssen, dürften) 与深度新闻调查词汇",
    "grammar": {
        "title": "主观情态动词体系 (Subjektive Bedeutung der Modalverben)",
        "sections": [
            {
                "heading": "1. 表示传闻与他人口述：",
                "content": "• sollen: 据说……，传闻…… (Der Minister soll zurücktreten. = Man sagt, dass der Minister zurücktritt.)\n• wollen: 自称……，扬言…… (Der Verdächtige will unschuldig sein. = Er behauptet, dass er unschuldig sei.)"
            },
            {
                "heading": "2. 表示说话人主观揣测与把握程度：",
                "content": "• müssen (95% 把握):肯定…… (Die Daten müssen gefälscht sein.)\n• dürfte (75% 把握):大概，很可能…… (Die Reform dürfte bald greifen.)\n• könnte (50% 把握):也许，可能…… (Es könnte zu Verzögerungen kommen.)\n• 与完成时不定式搭配表示对过去的推测：Er muss den Bericht gekannt haben."
            }
        ]
    },
    "quiz": [
        {
            "id": "B2_L11_Q1",
            "type": "GRAMMAR_FILL",
            "question": "Der Whistleblower ______ (sollen) brisante Dokumente an die Presse weitergegeben haben.",
            "options": ["soll", "will", "muss", "darf"],
            "correctIndex": 0,
            "explanation": "表示外界传闻“据说该告密者已经向媒体泄露了绝密文件”，使用 sollen: soll weitergegeben haben。"
        },
        {
            "id": "B2_L11_Q2",
            "type": "MEANING_SELECT",
            "question": "“die vierte Gewalt” 在现代宪政民主体制中的政治代名词是指：",
            "options": ["独立自主、行使舆论监督权的新闻媒体与新闻界", "秘密警察机关", "中央银行货币委员会", "宪法起草委员会"],
            "correctIndex": 0,
            "explanation": "die vierte Gewalt（第四权力）代指监督立法、行政、司法三权的新闻出版与独立媒体。"
        },
        {
            "id": "B2_L11_Q3",
            "type": "GRAMMAR_FILL",
            "question": "Der Konzernchef ______ (wollen) von den Manipulationen nichts gewusst haben.",
            "options": ["will", "soll", "muss", "mag"],
            "correctIndex": 0,
            "explanation": "表示当事人自我声称/狡辩“自称对篡改毫不知情”，主观情态动词使用 wollen: will gewusst haben。"
        },
        {
            "id": "B2_L11_Q4",
            "type": "LISTENING_MCQ",
            "question": "“Recherchierende Journalisten deckten einen gigantischen Steuerskandal auf.” 意味着：",
            "options": ["深入调查的新闻记者曝光了一起巨额偷逃税款丑闻。", "媒体隐瞒了丑闻真相。", "税务部门指控记者违法。", "调查因缺乏线索中断。"],
            "correctIndex": 0,
            "explanation": "recherchierende Journalisten = 调查记者，aufdecken = 揭露曝光，Steuerskandal = 税务丑闻。"
        },
        {
            "id": "B2_L11_Q5",
            "type": "SENTENCE_BUILDER",
            "question": "重组新闻自由核心命题：“garantiert / Eine freie und unabhängige Presse / das Recht auf Information / für alle Bürger”",
            "options": ["Eine freie und unabhängige Presse garantiert das Recht auf Information für alle Bürger.", "Für alle Bürger das Recht auf Information eine freie Presse garantiert nicht.", "Eine freie Presse für alle Bürger das Recht garantiert auf Information.", "Garantiert eine freie und unabhängige Presse das Recht auf Information für alle Bürger."],
            "correctIndex": 0,
            "explanation": "主语 (Eine freie und unabhängige Presse) + 谓语 (garantiert) + 宾语 (das Recht auf Information) + 补足语 (für alle Bürger)。"
        }
    ],
    "words": [
        ("die Medien", "die", "Nomen (Pl.)", "Pl.", "大众媒体，传播媒介", "Die freien Medien fungieren als unverzichtbare vierte Gewalt im Staat.", "独立自由的大众新闻媒体在现代国家体制中坚定充当着捍卫公众利益的第四权力。"),
        ("die Medienkompetenz", "die", "Nomen", "unz.", "批判性传媒素养", "Medienkompetenz befähigt Bürger, Propaganda von seriösen Fakten zu trennen.", "良好的批判性传媒素养赋予了公民一双慧眼，能够一眼洞穿虚假政治宣传与客观严肃事实的鸿沟。"),
        ("der Journalismus", "der", "Nomen", "unz.", "新闻学，新闻业", "Investigativer Journalismus scheut keine Mühe, um Korruption aufzudecken.", "坚守良知的深度调查性新闻记者从不计个人安危得失，誓要把一切深藏地下的腐败黑幕昭示天下。"),
        ("die Pressefreiheit", "die", "Nomen", "unz.", "新闻出版自由", "Die Pressefreiheit ist das unantastbare Lebenselixier jeder lebendigen Demokratie.", "依法捍卫新闻报道与独立出版自由，是滋养任何一个生机勃勃的宪政民主政体不可或缺的生命泉源。"),
        ("der Zensor", "der", "Nomen", "-en", "新闻审查官", "In autoritären Regimen unterdrücken Zensoren jede Form regierungskritischer Berichterstattung.", "在专制极权统治铁幕之下，无孔不入的新闻审查官残酷扼杀一切敢于针砭时弊的批评调查报道。"),
        ("die Zensur", "die", "Nomen", "-en", "新闻审查制度", "Artikel 5 Absatz 1 des Grundgesetzes garantiert unmissverständlich: Eine Zensur findet nicht statt.", "德国根本大法第五条第一款斩钉截铁地向历史宣告：新闻书刊审查制度永远不得设立。"),
        ("der Rundfunk", "der", "Nomen", "unz.", "广播电视传播", "Der öffentlich-rechtliche Rundfunk wird durch einen solidarischen Rundfunkbeitrag finanziert.", "德国公共广播电视系统通过全民法定缴纳的视听牌照费予以全额资助，从而保持其崇高的超然独立。"),
        ("die Tagesschau", "die", "Nomen", "unz.", "每日新闻联播 (ARD旗舰新闻)", "Die Tagesschau um 20 Uhr ist die traditionsreichste und meistgesehene Nachrichtensendung Deutschlands.", "每晚八点整准时在德意志各大荧屏响起的《每日新闻》，是德国历史最悠久、收视率最高的王牌旗舰新闻。"),
        ("die Redaktion", "die", "Nomen", "-en", "编辑部，编委会", "Die Redaktion prüft jede eingehende Meldung nach dem strengen Vier-Augen-Prinzip.", "在正式排版见报之前，编辑部必须按照国际通行的交叉双人复核原则对每条突发新闻进行事实校准。"),
        ("der Chefredakteur", "der", "Nomen", "-e", "总编辑", "Der Chefredakteur trägt die presserechtliche Gesamtverantwortung für die Publikation.", "总编辑依据国家出版新闻法对该报纸期刊刊发的所有文图内容的真实合法性承担全部终极法律责任。"),
        ("der Korrespondent", "der", "Nomen", "-en", "驻外记者，特派员", "Der Korrespondent berichtet live aus dem Krisengebiet über die aktuellen Entwicklungen.", "常驻战乱前沿的特派常驻战地记者手持卫星天线，在硝烟弥漫的第一线为国内受众发回最震撼的实时动态。"),
        ("die Recherche", "die", "Nomen", "-n", "深度调查核实，背景调研", "Monatelange akribische Recherche führte zur Aufdeckung eines weltweiten Geldwäschenetzwerks.", "历时数月之久、抽丝剥茧般的严密跨国背景调查，最终牵出并彻底打碎了一张横跨三大洲的地下洗钱巨网。"),
        ("die Quelle", "die", "Nomen", "-n", "新闻信源，爆料来源", "Journalisten haben das gesetzliche Recht auf Zeugnisverweigerung zum Schutz ihrer Quellen.", "职业新闻记者依法享有神圣的“拒绝作证特权”，任何公权力均无权强迫记者供出其秘密深喉信源。"),
        ("der Whistleblower", "der", "Nomen", "-", "内部吹哨人，揭秘者", "Der Whistleblower übermittelte verschlüsselte Dokumente über rechtswidrige Massenüberwachung.", "这位心怀正义的体制内深喉吹哨人，通过最高等级端到端加密信道向权威大报投递了关于非法窃听的铁证。"),
        ("der Informant", "der", "Nomen", "-en", "线人，线索提供者", "Der Informant bestand auf absoluter Anonymität aus berechtigter Angst um sein Leben.", "出于对自身与家庭人身安全的深刻恐惧，向媒体爆料内幕的关键线人坚决要求必须保持绝对隐姓埋名。"),
        ("die Schlagzeile", "die", "Nomen", "-n", "报纸头条大标题", "Die reißerische Schlagzeile auf der Titelseite erregte gestern bundesweites Aufsehen.", "赫然印在头版头条上的那行惊心动魄、字字见血的巨大醒目标题，昨日在全德朝野引爆了滔天巨浪。"),
        ("die Meldung", "die", "Nomen", "-en", "快讯，简讯", "Eine Eilmeldung über das Erdbeben unterbrach das laufende Fernsehprogramm.", "一条插播地震特大灾情的十万火急突发简讯，紧急中断了国家电视台正在热播的黄金档电视剧。"),
        ("der Leitartikel", "der", "Nomen", "-", "社论，编辑部社评", "Im Leitartikel bezog der Kommentator unmissverständlich Stellung gegen den Gesetzentwurf.", "在今日刊发的重磅社论中，特约资深评论员以极其犀利老辣的笔锋旗帜鲜明地痛批了该项争议法案草案。"),
        ("der Kommentar", "der", "Nomen", "-e", "新闻时评", "In seriösen Qualitätsmedien wird strikt zwischen sachlicher Nachricht und persönlichem Kommentar getrennt.", "在享誉世界的严肃高质量大报殿堂里，客观纯粹的新闻事实报道与执笔者鲜明的个人主观时评被严格物理隔离。"),
        ("die Kolumne", "die", "Nomen", "-n", "专栏，每周随笔", "Ihre wöchentliche Kolumne über gesellschaftliche Absurditäten wird millionenfach gelesen.", "她在每周各大综合性大刊上开设的关于当代奇葩社会现象的犀利杂文专栏，常年坐拥数以百万计的忠实读者。"),
        ("die Fake News", "die", "Nomen (Pl.)", "Pl.", "虚假新闻，网络谣言", "Manipulierte Fake News in sozialen Netzwerken können Wahlen und Demokratien manipulieren.", "在封闭式社交软件中病毒式传播的深度伪造恶意虚假新闻，完全有能力在暗中左右国家大选民意走向。"),
        ("die Desinformation", "die", "Nomen", "-en", "战略虚假信息战，造谣惑众", "Gezielte Desinformation wird im hybriden Krieg als Waffe zur Spaltung der Gesellschaft eingesetzt.", "处心积虑策划实施的战略级虚假认知作战，已在现代混合地缘战争中蜕变为瓦解敌国社会民心的一柄隐形利刃。"),
        ("die Fehlinformation", "die", "Nomen", "-en", "误传信息，错误资讯", "Im Chaos der Katastrophe kursierten zahlreiche unbeabsichtigte Fehlinformationen über Opferzahlen.", "在特大自然灾害突发爆发的初期极度混乱时刻，关于遇难同胞伤亡数字的各种无意误传信息一度满天飞。"),
        ("das Narrativ", "das", "Nomen", "-e", "宏大叙事，话语框架", "Propagandisten konstruieren ein verzerrtes Narrativ, um ihr aggressives Vorgehen zu rechtfertigen.", "职业宣传推手处心积虑编织构筑起一套彻底颠倒黑白的话语叙事圈套，企图为己方赤裸裸的武装侵略涂脂抹粉。"),
        ("das Framing", "das", "Nomen", "unz.", "框架效应，定调预设", "Durch geschicktes sprachliches Framing kann derselbe Sachverhalt völlig gegensätzlich dargestellt werden.", "通过在修辞用字上耍弄精巧的“语言框架”暗示魔术，完全相同的同一客观事物能够在受众脑海中呈现出截然相反的形象。"),
        ("die Echokammer", "die", "Nomen", "-n", "信息茧房，网络回音室", "Algorithmen drängen Nutzer in Echokammern, in denen sie nur noch die eigene Meinung bestätigt finden.", "投其所好的平台个性化推荐算法正在把广大网民生生赶进信息茧房，让他们在闭门造车的回音壁前日趋偏执封闭。"),
        ("die Filterblase", "die", "Nomen", "-n", "过滤气泡", "Aus der Filterblase auszubrechen erfordert die bewusste Konsultation kontroverser Medien.", "想要彻底打破将自身心智视野死死锁死的一孔之见“过滤气泡”，唯一解药便在于主动跳出圈层研读针锋相对的多元大报。"),
        ("der Klickköder", "der", "Nomen", "-", "标题党诱饵 (Clickbait)", "Clickbait-Überschriften versprechen Sensationen, enttäuschen die Leser aber mit trivialem Inhalt.", "低俗耸人听闻的标题党诱饵虽在短时间内能骗取可观流量点击，但点开后空洞低劣的垃圾内容只会招致读者的无尽鄙视。"),
        ("der Boulevardjournalismus", "der", "Nomen", "unz.", "黄色新闻，小报八卦新闻", "Boulevardjournalismus lebt von Skandalen, Intimsphäre-Verletzungen und grellen Übertreibungen.", "唯恐天下不乱的低俗黄色小报新闻文化，向来以吃人血馒头、恶意窥探名人床帏隐私与大肆夸大其词为谋生手段。"),
        ("die Sensationsgier", "die", "Nomen", "unz.", "猎奇心理，嗜血看客心态", "Die Sensationsgier mancher Fotografen behinderte die Rettungskräfte bei der Bergung der Verletzten.", "部分毫无职业道德底线的狗仔摄影记者在惨烈车祸现场贪婪猎奇抢拍特写，竟然无耻堵塞了急救抬担架的生命通道。"),
        ("die Verleumdung", "die", "Nomen", "-en", "诽谤罪，恶意中伤", "Gegen böswillige Verleumdung im Internet kann man mit einstweiligen Verfügungen gerichtlich vorgehen.", "面对隐匿在暗处敲击键盘、指鹿为马的恶意构陷与诽谤中伤，受害当事人依法有权向法院火速申请诉前人格权禁令。"),
        ("die Rufschädigung", "die", "Nomen", "-en", "名誉侵害，砸人商誉", "Falsche Anschuldigungen fügten dem traditionsreichen Familienbetrieb eine schwere Rufschädigung zu.", "无中生有、空穴来风的恶毒栽赃构陷，给这家历经数代人含辛茹苦打拼下的百年工匠名企造成了难以挽回的名誉商誉重创。"),
        ("die Richtigstellung", "die", "Nomen", "-en", "更正声明，辟谣致歉启事", "Die Zeitung musste auf Seite eins eine prominente Richtigstellung und Entschuldigung abdrucken.", "在原告代理律师铁证如山的通牒威慑下，该涉案报社被迫在次日头版显要位置刊发了白纸黑字的更正致歉声明。"),
        ("der Pressekodex", "der", "Nomen", "-e", "新闻出版自律伦理准则", "Der Deutsche Presserat wacht über die strikte Einhaltung der Grundsätze des Pressekodex.", "德意志新闻理事会如同新闻界的道德风纪监察法庭，严肃监察并惩戒任何胆敢违背行业最高自律准则的越界行径。"),
        ("die Rüge", "die", "Nomen", "-n", "公开谴责，书面申诫", "Der Presserat sprach gegen das Boulevardblatt eine öffentliche Rüge wegen Voyeurismus aus.", "针对该通俗小报在报道恶性绑架案时不顾人质安危、充当偷窥狂的卑鄙行径，新闻自律委员会出具了措辞严厉的公开谴责令。"),
        ("die Glaubwürdigkeit", "die", "Nomen", "unz.", "公信力，可信赖度", "Glaubwürdigkeit ist das unbezahlbare, über Jahrzehnte mühsam aufgebaute Kapital einer Zeitung.", "崇高的公信力是一座正规严肃大报历经几代编辑记者呕心沥血数十年如一日方能积攒下的最无价的黄金金字招牌。"),
        ("das Sommerloch", "das", "Nomen", "unz.", "暑期新闻淡季（新闻真空期）", "Im politischen Sommerloch füllen die Medien ihre Spalten gern mit absurden Tiermeldungen.", "每当联邦议院与内阁进入长达一个多月的暑期休会停摆期，闲得发慌的新闻版面往往只能拿各种奇闻异事滥竽充数。"),
        ("das Framing", "das", "Nomen", "unz.", "议题设置预设", "Mediales Framing lenkt den Fokus der Öffentlichkeit auf bestimmte Aspekte einer komplexen Debatte.", "大众传播中无形的话语框架定调，往往神不知鬼不觉地把全社会的焦点强行聚焦在争议事件被刻意剪裁的某一侧面。"),
        ("die Zivilcourage", "die", "Nomen", "unz.", "见义勇为的道德勇气", "Mutige Journalisten beweisen Zivilcourage, wenn sie Unrecht trotz massiver Drohungen beim Namen nennen.", "当面对黑恶势力的死亡威胁与巨额利益诱惑仍敢于站直脊梁、实名将罪恶公之于众时，调查记者彰显了何谓顶天立地的公民道德勇气。"),
        ("das Urheberrecht", "das", "Nomen", "-e", "新闻版权与知识产权", "Das Urheberrecht schützt die schöpferische Arbeit von Journalisten, Autoren und Bildreportern.", "知识产权法严格保护广大新闻一线记者、作家学者与战地摄影师倾尽心血创作的具有独创性的新闻文字与影像作品。"),
        ("recherchieren", "kein", "Verb", "recherchierte, recherchiert", "深入调查取证", "Die Redaktion recherchierte über zwei Jahre im geheimen Netzwerk der internationalen Steueroasen.", "由多国顶尖记者组成的跨国联合调查组整整潜伏暗访调查了两年，才终于摸清了离岸避税天堂背后错综复杂的空壳洗钱公司。"),
        ("aufdecken", "kein", "Verb", "deckte auf, aufgedeckt", "曝光，揭露黑幕", "Mutige Whistleblower deckten auf, dass Regierungsbehörden unschuldige Bürger illegal ausspioniert hatten.", "孤胆英雄吹哨人冒着粉身碎骨的代价向全世界彻底曝光揭露：国家情报安全部门多年来一直在大规模非法监听监控无辜良民。"),
        ("verifizieren", "kein", "Verb", "verifizierte, verifiziert", "事实核查，多方验真", "Bevor wir ein Handyvideo ausstrahlen, müssen wir Herkunft und Metadaten unabhängig verifizieren.", "在把一段来自社交网络的手机短视频播发到全国电视观众眼前之前，专职核查团队必须对原始拍摄地点与元数据实施严密多方核实。"),
        ("fälschen", "kein", "Verb", "fälschte, gefälscht", "伪造数据，篡改", "Der Reporter flog auf, weil er Interviews und Reportagedetails skrupellos erfunden und gefälscht hatte.", "这名曾斩获无数大奖的明星记者之所以彻底身败名裂，是因为他多年来竟然一直在肆无忌惮地闭门造车编造受访者引语与细节。"),
        ("manipulieren", "kein", "Verb", "manipulierte, manipuliert", "技术篡改，操纵受众", "Fotos können heute mit wenigen Klicks so perfekt manipuliert werden, dass selbst Experten zweifeln.", "借助现代尖端数字图形合成算法，一张新闻图片仅需轻点数下鼠标便能被篡改得天衣无缝，甚至连鉴宝专家都难辨雌雄。"),
        ("entlarven", "kein", "Verb", "entlarvte, entlarvt", "撕下伪装，揭穿谎言", "Faktenprüfer entlarvten das virale Propagandavideo binnen einer Stunde als dreiste Montage.", "全球各大独立专业事实核查机构的大神们在短短一个小时之内，便用铁一般的原始视频对比证据彻底揭穿了那段爆火虚假宣传视频的粗劣拼凑本质。"),
        ("zensieren", "kein", "Verb", "zensierte, zensiert", "删帖审查，封杀", "Diktatoren zensieren unliebsame Internetseiten und sperren den Zugang zu ausländischen Nachrichtenportalen.", "独裁专制暴君为了维系其摇摇欲坠的统治，疯狂筑起高墙封锁外网，残酷审查删削一切不利于自己的真相报道与海外独立门户网站。"),
        ("verbreiten", "kein", "Verb", "verbreitete, verbreitet", "散布传播流言", "Böswillige Falschmeldungen verbreiten sich in sozialen Netzwerken sechsmal schneller als die Wahrheit.", "权威大数据传播学实证调查揭示了一个令人骨脊发凉的事实：恶毒虚假的谣言在互联网上的扩散裂变速度竟然足足比真相快了六倍。"),
        ("korrigieren", "kein", "Verb", "korrigierte, korrigiert", "勘误纠错", "Eine seriöse Redaktion zögert keine Sekunde, einen sachlichen Fehler sofort transparent zu korrigieren.", "一家真正将公信力视如生命的卓越专业大报，在发现自身报道出现哪怕微小的事实硬伤时，绝不护短推诿，而是在第一时间公开透明勘误。"),
        ("polarisieren", "kein", "Verb", "polarisierte, polarisiert", "造成社会两极分化撕裂", "Reißerische Berichterstattung polarisiert die Gesellschaft und zerstört das Fundament des Dialogs.", "为了博取眼球而不择手段的煽情狗血小报式炒作报道，正在将整个社会推向你死我活的两极分化深渊，彻底摧毁了理性对话沟通的底盘。"),
        ("investigativ", "kein", "Adjektiv", "-", "调查性的，追查到底的", "Investigativer Journalismus ist der wirksamste Schutzschild gegen den Missbrauch staatlicher Macht.", "敢于顶风作案、死磕到底的深度调查性新闻报道，是防止国家公权力在暗室之中肆意膨胀滥用最坚固不可摧的民主防线盾牌。"),
        ("seriös", "kein", "Adjektiv", "-", "严谨客观正规的", "Seriöse Journalisten arbeiten nach den Grundsätzen wahrhaftiger, unparteiischer und belegbarer Berichterstattung.", "一位真正受人尊敬的严肃新闻匠人，毕生恪守着坚持真相、客观中立且拿得出铁证链条的最高专业采编伦理准则。"),
        ("reißerisch", "kein", "Adjektiv", "-", "耸人听闻煽情的，抓人眼球的", "Reißerische Titel locken oberflächliche Klicks an, zerstören aber das Vertrauen anspruchsvoller Leser.", "耸人听闻、语不惊人死不休的抓眼球标题固然能在算法海洋里捞到几许泛黄的点击率，但却在无形中将最有品位深度的高端忠实读者彻底推远。"),
        ("subjektiv", "kein", "Adjektiv", "-", "带有主观色彩的", "Jeder Kommentar spiegelt naturgemäß die subjektive Wertung und Weltsicht des Autors wider.", "任何一篇见解独到的时政专栏特稿，其行文论证之中自然无可厚非地折射出作者本人独特的精神世界、价值追求与主观研判。"),
        ("unparteiisch", "kein", "Adjektiv", "-", "不偏不倚客观中立的", "Der öffentlich-rechtliche Rundfunk ist vom Gesetzgeber zu einer strikt unparteiischen Berichterstattung verpflichtet.", "国家立法机关在视听法律规章中以最严厉的法律条款强制约束：公共广播电视台在全频道采编播发中必须对各政党政见保持绝对的不偏不倚。"),
        ("tendenziös", "kein", "Adjektiv", "-", "拉偏条带倾向性的", "Tendenziöse Berichterstattung verzerrt komplexe Tatsachen und manipuliert das Urteil der Bürger.", "带着预设立场、拉偏条拉偏架的倾向性失衡报道，严重扭曲了错综复杂的历史事件全貌，并在暗中愚弄操弄了广大市民的独立判断力。"),
        ("brisant", "kein", "Adjektiv", "-", "极度敏感爆炸性的", "Die Enthüllung dieser hochbrisanten Dokumente löste eine schwere diplomatische Krise aus.", "这批包含国家绝密内幕的高敏感度重磅档案文件的突然泄密外流，瞬间引爆了一场令两国国家元首焦头烂额的严重跨国外交危机。"),
        ("unabhängig", "kein", "Adjektiv", "-", "独立于财阀与权贵的", "Eine freie Gesellschaft braucht wirtschaftlich und politisch vollkommen unabhängige Medien.", "一个真正崇尚思想自由的成熟现代文明社会，迫切需要大批在财政上不受任何财阀绑架、在行政上不受任何权贵干预的绝对独立的媒体灯塔。"),
        ("authentisch", "kein", "Adjektiv", "-", "原汁原味真实可靠的", "Das Filmmaterial wurde von Gerichtsmedizinern und Technikern als zweifelsfrei authentisch eingestuft.", "在案由现场群众拍摄的珍贵视频物证经过法医与多媒体司法鉴定专家的层层穿透式光谱检测，最终被白纸黑字盖印鉴定为百分之百真实无篡改。"),
        ("viral", "kein", "Adjektiv", "-", "病毒式核爆蔓延的", "Das Entlarvungsvideo ging innerhalb weniger Stunden viral und erreichte weltweit über zehn Millionen Klicks.", "这段打假揭批劣币驱逐良币黑幕的超清硬核视频在上线发布后短短数小时内便掀起病毒式核爆裂变，在全球斩获了超千万播放量。"),
        ("anonym", "kein", "Adjektiv", "-", "隐姓埋名匿名的", "Anonyme Quellen dürfen im Journalismus nur nach rigoroser Prüfung ihrer Verlässlichkeit zitiert werden.", "在严谨负责的新闻殿堂里，对匿名信源所提供的惊天爆料必须经过反复多方背调与人身可靠性评估，方能在极为苛刻的条件下审慎引用。"),
        ("korrupt", "kein", "Adjektiv", "-", "贪婪腐败堕落的", "Investigative Reporter brachten das System korrupter Politiker und bestechlicher Richter zu Fall.", "无畏的调查记者凭借一腔孤勇与十万字铁证专案，一举将那个盘根错节盘踞在政法两界长达数十年的贪腐政客与司法硕鼠团伙彻底拉下神坛。"),
        ("skandalös", "kein", "Adjektiv", "-", "令人发指丑陋可耻的", "Die skandalösen Enthüllungen über die Ausbeutung von Wanderarbeitern lösten eine Gesetzesreform aus.", "关于某些无良血汗工厂残酷压榨剥削外来务工同胞合法权益的令人发指的丑闻曝光，最终倒逼国家立法机关以光速通过了专项劳工保障改革法案。"),
        ("ethisch", "kein", "Adjektiv", "-", "坚守职业道德底线的", "Ethischer Journalismus stellt das öffentliche Aufklärungsinteresse immer über den schnellen Profit.", "始终流淌着崇高职业道德血液的伟大新闻学，永远把唤醒公众良知、探求客观真理的神圣启蒙使命置于任何短平快的铜臭利益之上。"),
        ("fundiert", "kein", "Adjektiv", "-", "立论扎实论据充分的", "Ihr fundierter Artikel lieferte die beste ökonomische Analyse der Krise weit und breit.", "她笔下那篇立论极其扎实、通篇充盈着海量一手微观调研数据的高质量经济观察特稿，被业界一致公认为洞察本轮金融风暴的最佳定海神针杰作。"),
        ("plausibel", "kein", "Adjektiv", "-", "经得起逻辑推敲合情合理的", "Die vorgelegte Erklärung klang zunächst plausibel, erwies sich bei genauer Prüfung aber als falsch.", "涉案官方发言人最初在新闻发布会上给出的那套说辞听起来虽然合情合理貌似说得通，但在记者连环追问调取档案的显微镜下被证明彻头彻尾漏洞百出。"),
        ("täuschend", "kein", "Adjektiv", "-", "以假乱真极具欺骗性的", "Der computergenerierte Deepfake wirkte täuschend echt auf die Mehrheit der Internetnutzer.", "依托大模型全流程渲染合成的人物换脸视频在视觉光影上呈现得以假乱真、天衣无缝的超强欺骗性，轻而易举地把绝大多数普通吃瓜网民全蒙在鼓里。"),
        ("kritisch", "kein", "Adjektiv", "-", "保持审视怀疑与批判力度的", "Bürger müssen lernen, allen Medieninhalten mit einer gesunden Portion kritischer Distanz zu begegnen.", "生活在大数据算法信息狂轰滥炸新时代的每一位现代公民，都必须学会在心底构筑起一道坚实的心智防火墙：时刻对所接收到的碎片资讯保持理性批判距离。"),
        ("differenziert", "kein", "Adjektiv", "-", "条理分明兼顾各方视角的", "Eine differenzierte Berichterstattung vermeidet Schwarz-Weiß-Malerei und beleuchtet alle Grautöne.", "真正成熟健全的新闻报道绝不搞非黑即白、非友即敌的脸谱化单一粗暴二元对立，而是充满耐心地用笔触生动还原复杂人世间的所有多维灰色光谱。"),
        ("unverzichtbar", "kein", "Adjektiv", "-", "中流砥柱不可或缺的", "Eine freie, mutige und investigative Presse ist ein unverzichtbarer Wachhund der Demokratie.", "一支永远挺直脊梁、无所畏惧、敢于向一切公权力叫板追查到底的独立自由新闻调查力量，是现代宪政民主体制最忠诚不倦、不可或缺的守门看家之犬。")
    ]
}

# LESSON 12: Philosophie, Aufklärung & Geistesgeschichte (70 words)
L12 = {
    "id": "B2_L12",
    "title": "第12课：欧陆哲学、思想史与德意志启蒙传统 (Philosophie & Aufklärung)",
    "summary": "掌握高级非现实愿望与假设从句 (Irreale Bedingungssätze mit beinahe / fast) 与康德启蒙哲学思想核心词汇",
    "grammar": {
        "title": "高级非现实假设与愿望从句 (Erweiterte irreale Bedingungen & Beinahe-Sätze)",
        "sections": [
            {
                "heading": "1. 过去非现实假设从句 (hätte / wäre + Partizip II):",
                "content": "• Hätte Kant die Kritik der reinen Vernunft nicht geschrieben, wäre die Philosophiegeschichte anders verlaufen.\n• 省略 wenn 时，动词 hätte / wäre 必须置于从句句首！"
            },
            {
                "heading": "2. beinahe / fast + 第二虚拟式过去时（差一点就发生但未发生）：",
                "content": "• Beinahe wäre das Manuskript im Krieg zerstört worden. (差一点手稿就在战争中被毁了)\n• Fast hätte er vor der Zensur kapituliert."
            }
        ]
    },
    "quiz": [
        {
            "id": "B2_L12_Q1",
            "type": "GRAMMAR_FILL",
            "question": "______ (Wenn er nicht reflektiert hätte) Kant die Schrift nicht verfasst, wäre unser Begriff von Vernunft ärmer.",
            "options": ["Hätte", "Würde", "War", "Sei"],
            "correctIndex": 0,
            "explanation": "省略连词 wenn 的过去非现实条件句，虚拟助动词 hätte 提至句首。"
        },
        {
            "id": "B2_L12_Q2",
            "type": "MEANING_SELECT",
            "question": "康德在《何谓启蒙》中提出的哲学名言 “Sapere aude!” 的中文标准经典翻译是：",
            "options": ["敢于运用你自己的理性！", "顺从自然法则！", "怀疑一切权威！", "知识就是力量！"],
            "correctIndex": 0,
            "explanation": "Sapere aude! = Habe Mut, dich deines eigenen Verstandes zu bedienen!（敢于运用你自己的理性！）。"
        },
        {
            "id": "B2_L12_Q3",
            "type": "GRAMMAR_FILL",
            "question": "Das historische Archiv ______ (beinahe / verbrennen) im großen Stadtbrand beinahe verbrannt.",
            "options": ["wäre", "würde", "hatte", "wurde"],
            "correctIndex": 0,
            "explanation": "beinahe + 第二虚拟式过去时表达“差一点就……”：wäre beinahe verbrannt。"
        },
        {
            "id": "B2_L12_Q4",
            "type": "LISTENING_MCQ",
            "question": "“Der kategorische Imperativ fordert, nur nach Maximen zu handeln, die zugleich allgemeines Gesetz werden können.” 核心准则是：",
            "options": ["定言令式要求个体的行为准则必须能够同时成为普遍的立法准则。", "为了个人利益可以突破道德底线。", "道德标准随社会风俗随时改变。", "唯有法律命令才具有道德价值。"],
            "correctIndex": 0,
            "explanation": "Kategorischer Imperativ = 定言令式（绝对命令），allgemeines Gesetz = 普遍法则。"
        },
        {
            "id": "B2_L12_Q5",
            "type": "SENTENCE_BUILDER",
            "question": "重组启蒙时代格言：“ist der Ausgang des Menschen / Die Aufklärung / aus seiner selbstverschuldeten Unmündigkeit”",
            "options": ["Die Aufklärung ist der Ausgang des Menschen aus seiner selbstverschuldeten Unmündigkeit.", "Aus seiner selbstverschuldeten Unmündigkeit die Aufklärung der Ausgang ist nicht.", "Der Ausgang des Menschen aus der Aufklärung ist Unmündigkeit.", "Ist die Aufklärung der Ausgang des Menschen aus seiner selbstverschuldeten Unmündigkeit."],
            "correctIndex": 0,
            "explanation": "康德对启蒙的经典定义：启蒙是人类脱离自身所招致的不成熟状态的走出 (der Ausgang des Menschen...)。"
        }
    ],
    "words": [
        ("die Philosophie", "die", "Nomen", "-n", "哲学，爱智慧", "Die europäische Philosophie wurzelt im antiken Griechenland und der europäischen Aufklärung.", "欧陆哲学思想的浩瀚大厦深深扎根在古希腊城邦的辩证思辨与近代启蒙运动理性觉醒的肥沃土壤之中。"),
        ("die Aufklärung", "die", "Nomen", "unz.", "启蒙运动，启蒙", "Die Aufklärung befreite das menschliche Denken aus den Fesseln des religiösen Dogmatismus.", "波澜壮阔的欧洲启蒙运动犹如一道撕裂夜空的刺眼破晓之光，将人类心智从神学教条主义的沉重枷锁中彻底解救出来。"),
        ("die Vernunft", "die", "Nomen", "unz.", "人类理性", "Immanuel Kant erhob die Vernunft zum obersten Richter über Wahrheit, Erkenntnis und Moral.", "哲学家伊曼努尔·康德以无可匹敌的纯粹理性批判手笔，将理性确立为裁决一切真理探索、认识论与道德伦理的至高法官。"),
        ("der Verstand", "die", "Nomen", "unz.", "知性，心智 (der Verstand)", "Habe Mut, dich deines eigenen Verstandes ohne fremde Leitung zu bedienen!", "“敢于在没有他人监护指导的前提下，勇敢地运用你自己的知性与头脑去思辨！”这正是启蒙最震撼人心的永恒座右铭。"),
        ("die Ethik", "die", "Nomen", "unz.", "伦理学，道德哲学", "Kants Pflichtethik begründet moralisches Handeln aus reiner Pflicht und Achtung fürs Gesetz.", "康德创立的崇高“义务论伦理学”，坚决剥离一切功利诱惑，将真正的崇高道德行为全然确立于对道德律令的至诚敬畏与履行天职。"),
        ("die Moral", "die", "Nomen", "unz.", "道德规范，公序良俗", "Universelle Moral beruht auf der unteilbaren Anerkennung der Würde jedes einzelnen Menschen.", "普世的道德法则其最不可动摇的核心支柱，正在于毫无保留地平等敬畏承认生而为人的每一个人所与生俱来的神圣尊严。"),
        ("der Imperativ", "der", "Nomen", "-e", "定言令式，绝对命令 (der kategorische Imperativ)", "Der kategorische Imperativ gilt als universeller ethischer Prüfstein für jedes Gesetz.", "作为绝对命令存在的“定言令式”，被世世代代的法理学者尊奉为检验任何人类世俗实在法是否具备良法美德的终极试金石。"),
        ("die Maxime", "die", "Nomen", "-n", "行为准则，人生座右铭", "Handle nur nach derjenigen Maxime, durch die du zugleich wollen kannst, dass sie Gesetz werde.", "“请仅仅按照那些你能够同时由衷意愿使其上升为全人类普遍立法准则的人生信条去行事立身！”"),
        ("die Erkenntnis", "die", "Nomen", "-se", "认识，领悟，洞见", "Philosophische Erkenntnis beginnt mit dem schonungslosen Hinterfragen des vermeintlich Selbstverständlichen.", "通往博大精深哲学领悟的第一道神圣门槛，永远始于对那些平日里被世人奉为理所当然的庸俗常识发起毫不留情的刨根问底。"),
        ("die Erkenntnistheorie", "die", "Nomen", "unz.", "认识论", "Die Erkenntnistheorie fragt: Was können wir mit unseren kognitiven Sinnen wirklich wissen?", "纯粹认识论向全人类发出了振聋发聩的终极哲学三问之首：“凭借我们凡胎肉体有限的感官与知性框架，我们究竟能够确知什么？”"),
        ("die Ontologie", "die", "Nomen", "unz.", "本体论，存在论", "Die Ontologie erforscht die grundlegenden Strukturen des Seins und der Wirklichkeit.", "作为第一哲学的本体论不畏浮云遮望眼，直击万物本原，致力于穷极探求客观实在与宇宙万事万物最根本底层的“存在之结构”。"),
        ("die Metaphysik", "die", "Nomen", "unz.", "形而上学", "Kant begrenzte die traditionelle Metaphysik auf die Grenzen der reinen Erfahrung.", "康德以雷霆万钧的哲学划界手术，一举把传统漫无边际、空想神游的古典形而上学严格锚定在人类可能经验的合理边界之内。"),
        ("die Dialektik", "die", "Nomen", "unz.", "辩证法", "Hegels Dialektik beschreibt die Entwicklung des Geistes in These, Antithese und Synthese.", "黑格尔名垂青史的庞大唯心辩证法体系，以磅礴气势把宇宙绝对精神自我演进解构为正题、反题与合题在矛盾斗争中的螺旋上升。"),
        ("der Idealismus", "der", "Nomen", "unz.", "唯心主义，德意志唯心论", "Der Deutsche Idealismus um Fichte, Schelling und Hegel prägte das europäische Geistesleben.", "以费希特、谢林与黑格尔为巅峰旗帜的“德意志古典唯心主义哲学群星”，以前所未有的高度深刻重塑了整个近代欧罗巴的精神世界。"),
        ("der Materialismus", "der", "Nomen", "unz.", "唯物主义", "Der historische Materialismus von Marx und Engels erklärt Geschichte aus ökonomischen Triebkräften.", "马克思与恩格斯创立的历史唯物主义科学世界观，破天荒地从物质资料生产方式与阶级利益博弈这一根本动能中破译了人类社会发展铁律。"),
        ("der Existenzialismus", "der", "Nomen", "unz.", "存在主义", "Im Existenzialismus geht die menschliche Existenz der individuellen Essenz voraus.", "存在主义哲学的开山基石旗帜鲜明地昭示世人：“存在先于本质”——人首先赤条条来到这个荒谬的世界，随后全凭自由抉择定义自我。"),
        ("die Existenz", "die", "Nomen", "-en", "存在，生存状态", "Die Furcht vor dem Nichts konfrontiert den Menschen mit der Fragilität seiner eigenen Existenz.", "在午夜凝视深渊虚无时涌起的深层存在性焦虑，逼迫着每一个孤寂的个体直面自身肉体生命不可承受之轻的脆弱真相。"),
        ("das Wesen", "das", "Nomen", "-", "本质，实体", "Das wahre Wesen der Dinge verbirgt sich oft hinter der trügerischen Oberfläche des Scheins.", "隐藏在浩瀚大千世界表象假相帷幕深处的客观事物真正内在本质，需要人类凭借百折不挠的科学思维才能穿透把握。"),
        ("das Ding an sich", "das", "Nomen", "unz.", "物自体，自在之物 (Kant)", "Nach Kant bleibt das 'Ding an sich' für den menschlichen Verstand unerkennbar.", "在康德严密的批判哲学体系框架内，脱离了人类时空感性直观形式与纯粹知性范畴的“物自体本身”，永远处于人类理性不可认识的彼岸。"),
        ("das Phänomen", "das", "Nomen", "Phänomene", "现象，表象 (Erscheinung)", "Wir erkennen nicht die Dinge an sich, sondern nur, wie sie uns als Phänomene erscheinen.", "我们凡人的肉眼心智所能触及捕捉的，永远不可能是冷酷隔绝的物自体本体，而仅仅是它在我们先验感官滤镜折射下所显现的万千现象。"),
        ("die Utopie", "die", "Nomen", "-n", "乌托邦，理想国", "Philosophische Utopien entwerfen gerechte Gesellschaften als kritischen Gegenentwurf zur Gegenwart.", "历代先贤哲人构想编织的伟大哲学乌托邦理想国蓝图，从来都是一面高悬在历史苍穹之上、时刻无情照亮并鞭笞现实丑恶的批判镜鉴。"),
        ("die Dystopie", "die", "Nomen", "-n", "反乌托邦，反面极权图景", "George Orwells '1984' ist die beklemmendste literarische Dystopie totalitärer Überwachung.", "英国作家乔治·奥威尔倾尽心血铸就的惊世长篇预言《1984》，构成了人类文学史上面对极权主义精神奴役与全息监控最窒息的反乌托邦挽歌。"),
        ("der Skeptizismus", "der", "Nomen", "unz.", "怀疑论", "Radikaler Skeptizismus bezweifelt die Möglichkeit jeder gesicherten objektiven Wahrheit.", "贯彻到底的激进怀疑论哲学向一切自诩全知全能的狂妄宣称开炮，甚至敢于无情质疑人类能否真正把握哪怕任何一条颠扑不破的客观真理。"),
        ("der Nihilismus", "der", "Nomen", "unz.", "虚无主义", "Friedrich Nietzsche analysierte den heraufziehenden europäischen Nihilismus messerscharf.", "哲学狂人弗里德里希·尼采手握思想铁锤，以入木三分的惊人先知洞察力精准剖析了伴随“上帝之死”而在欧罗巴大地悄然降临的深渊虚无主义。"),
        ("der Humanismus", "der", "Nomen", "unz.", "人文主义，人道主义", "Der Neuhumanismus Wilhelm von Humboldts stellte die ganzheitliche Bildung des Menschen ins Zentrum.", "威廉·冯·洪堡所创立并奠基的现代新人文主义教育理想，坚定把促进每一个独特个体自由全面而和谐的心智博雅人格塑造推向王座。"),
        ("die Dogmatik", "die", "Nomen", "unz.", "教条主义，教理学", "Dogmatik erstickt das freie Denken und verlangt blinden, unkritischen Gehorsam.", "自命不凡、冥顽不灵的教条主义把真理教条化为僵死的木乃伊，不仅彻底扼杀了思想自由探索的火苗，更狂妄逼迫世人献上盲从的膝盖。"),
        ("das Dogma", "das", "Nomen", "Dogmen", "信条，教条", "Wissenschaftlicher Fortschritt verlangt das mutige Umstoßen veralteter ideologischer Dogmen.", "人类自然科学与人文精神要想实现真正划时代的飞跃，首要前提便在于拿出敢把皇帝拉下马的非凡勇气，将一切落后僵化的意识形态陈规教条砸个粉碎。"),
        ("die Willensfreiheit", "die", "Nomen", "unz.", "自由意志", "Ohne Willensfreiheit gäbe es weder moralische Schuld noch rechtliche Verantwortlichkeit.", "假若从根本上抹杀并剥夺了人类内心所拥有的抉择善恶的自由意志，那么整个人类文明赖以建立的道德负罪自责与司法民事刑事责任便将彻底灰飞烟灭。"),
        ("der Determinismus", "der", "Nomen", "unz.", "机械决定论", "Der strikte Determinismus behauptet, dass jedes künftige Ereignis durch Vorbedingungen festgelegt ist.", "刻板机械的宿命决定论断言：从宇宙大爆炸初期的微观粒子初速度开始，人类历史长河中所发生的每一桩细枝末节早已被冷酷写死、毫无转圜。"),
        ("das Schicksal", "das", "Nomen", "-e", "宿命，命运", "Der antike Held kämpft aufrecht gegen sein unausweichliches tragisches Schicksal an.", "古希腊悲剧舞台上的高贵英雄哪怕明知前路是无底深渊，依然在狂风暴雨中挺起不屈的胸膛，孤身一人向着那无可逃避的残酷宿命发起壮烈决斗。"),
        ("die Tugend", "die", "Nomen", "-en", "德性，美德 (die Arete)", "Aristoteles definierte die Tugend als die goldene Mitte zwischen zwei extremen Lastern.", "古希腊百科全书式思想巨匠亚里士多德在《尼各马可伦理学》中给美德下了千古定论：美德正是横亘在两个走向极端的恶德深渊之间恰到好处的“中庸之道”。"),
        ("das Laster", "das", "Nomen", "-", "恶习，恶德", "Völlerei und Maßlosigkeit galten den antiken Philosophen als schändliche Laster.", "放纵贪婪口腹之欲与毫无自律节制的纵欲无度，自古罗马斯多葛学派时代起便被一切修身明智的哲人痛斥为腐蚀灵魂的卑劣恶德。"),
        ("die Selbstbestimmung", "die", "Nomen", "unz.", "自决权，意志自主 (Autonomie)", "Kants Autonomiebegriff besagt, dass der Mensch sich selbst dem moralischen Gesetz unterwirft.", "康德哲学中最为灿烂夺目的核心概念“自律”，深刻揭示了真正的自由：它绝非随心所欲的任性胡来，而是人凭自身的理性自主立法并心悦诚服地皈依遵从。"),
        ("die Fremdbestimmung", "die", "Nomen", "unz.", "受制于人，被动他律 (Heteronomie)", "Befreiung aus geistiger Fremdbestimmung ist der erste und wichtigste Schritt zur Mündigkeit.", "主动挣脱外界强权、盲目民粹与庸俗舆论对自己心灵的无形精神他律与思想操控，是每一个独立灵魂走向心智真正成熟成人的第一道生死关隘。"),
        ("die Mündigkeit", "die", "Nomen", "unz.", "成熟自立，独立责任心", "Mündige Bürger hinterfragen die Entscheidungen der Herrschenden konstruktiv und mutig.", "一个拥有成熟健全自立心智的现代宪政公民，从不盲信盲从盲拜任何权贵救世主，而是以温和坚定、有理有据的建设性姿态对一切统治者的决断实施理性监督。"),
        ("die Würde", "die", "Nomen", "unz.", "人的尊严", "Die Würde des Menschen besitzt keinen Preis, sondern einen absoluten, unantastbaren inneren Wert.", "康德在《道德形而上学奠基》中留下不朽训诫：在宇宙间，凡是有价格的事物都可被金钱明码标价替代；唯有人的尊严超然绝俗，享有至高无上的内在尊严。"),
        ("das Gewissen", "das", "Nomen", "-", "良知，良心", "Das Gewissen ist die innere Stimme, die uns unbestechlich an unsere moralischen Pflichten mahnt.", "良知是深植在每一个人灵魂神庙最深处的一座不熄灯塔，如同一名永不收受贿赂、铁面无私的内心法官，时刻在暗室中拷问并提醒我们恪守做人的天职。"),
        ("das Ideal", "das", "Nomen", "-e", "崇高理想", "Die Ideale der Französischen Revolution lauteten: Freiheit, Gleichheit, Brüderlichkeit.", "震撼欧罗巴旧大陆封建王权专制基座的法国大革命，在战火硝烟中催生出三盏照亮后世现代文明征程的永恒精神火炬：自由、平等、博爱。"),
        ("das Paradoxon", "das", "Nomen", "Paradoxa", "悖论，反论", "Das Paradoxon der Toleranz: Eine Gesellschaft muss intolerant gegen Intoleranz sein, um zu überleben.", "现代批判理性主义宗师卡尔·波普尔提出的“宽容悖论”发人深省：一个追求包容的文明社会若想活下去，就必须对一切妄图消灭宽容的极端不宽容施以毫不手软的铁腕打击。"),
        ("der Diskurs", "der", "Nomen", "-e", "学术商谈，理性交往话语", "Jürgen Habermas entwickelte die Theorie des herrschaftsfreien diskursiven Handelns.", "法兰克福学派当代掌门人尤尔根·哈贝马斯倾毕生心力构筑起了宏大的“交往行为理论”，力主通过消除一切权力不对称的纯粹理性语言商谈来达成民主共识。"),
        ("philosophieren", "kein", "Verb", "philosophierte, philosophiert", "哲学思辨，探讨哲理", "Bis spät in die Nacht hinein philosophierten die Studenten über den Sinn des menschlichen Daseins.", "在微弱温暖的台灯摇曳光晕下，热血沸腾的哲学系学子一直激辩探讨哲学直到东方既白，尽情追问着人生的终极意义与宇宙归宿。"),
        ("hinterfragen", "kein", "Verb", "hinterfragte, hinterfragt", "深层反思质疑", "Kritische Philosophen müssen die bestehenden Machtverhältnisse radikal und furchtlos hinterfragen.", "真正拥有士子风骨的独立批判学者，必须以钢铁般的道义担当，无所畏惧地对现有不合理社会的权力架构与话语垄断展开打破砂锅问到底的深层反思。"),
        ("reflektieren", "kein", "Verb", "reflektierte, reflektiert", "反思沉淀", "Wer nicht über seine historischen Fehler reflektiert, ist verdammt, sie unweigerlich zu wiederholen.", "任何一个在历史灾难狂潮退去后拒绝以刮骨疗毒之勇气对自身民族过失展开深刻痛定思痛反省的族群，注定将被历史诅咒、不可逆转地在未来重蹈同一场血色覆辙。"),
        ("emanziperen", "kein", "Verb", "emanzipierte, emanzipiert", "获得解放，挣脱束缚 (sich von)", "Der Mensch emanzipierte sich im Zeitalter der Aufklärung schrittweise von feudaler Vormundschaft.", "在十八世纪启蒙时代波澜壮阔的理性洗礼下，广大平民大众破天荒地一步一个脚印将自身从千百年封建王权与教权的双重思想包办监护中彻底解放出来。"),
        ("postulieren", "kein", "Verb", "postulierte, postuliert", "提出先验设定，假定", "Kant postulierte die Unsterblichkeit der Seele und die Existenz Gottes als praktische Postulate der Vernunft.", "康德在其《实践理性批判》中，将灵魂的不朽、人的意志自由以及上帝的存在，作为保障人类道德律令在现实中行得通的实践理性三大不可或缺的崇高预设准则。"),
        ("deduzieren", "kein", "Verb", "deduzierte, deduziert", "演绎推导 (aus)", "Aus allgemeinen philosophischen Prämissen lassen sich konkrete Handlungsanweisungen logisch deduzieren.", "依据严丝合缝的形式逻辑学演绎铁律，从具有最高公理地位的宏观普遍哲学前提中，完全可以顺理成章地一步步演绎推导出指导日常处世的微观行为准绳。"),
        ("induzieren", "kein", "Verb", "induzierte, induziert", "归纳提升 (aus)", "Durch Beobachtung zahlreicher Einzelfälle induzierte der Naturphilosoph ein allgemeines Gesetz.", "通过在实验室夜以继日对成百上千起微观实验现象与离散样本的细致观测归纳，自然科学家最终凭借超凡的归纳跃迁法提炼出了放之四海而皆准的普遍物理定律。"),
        ("überwinden", "kein", "Verb", "überwand, überwunden", "超越，克服思维局限", "Der moderne Geist muss den zerstörerischen Dualismus von Geist und Natur endlich überwinden.", "当代崭新生态哲学与量子物理学正在向全人类发出呼唤：我们必须彻底摒弃并超越笛卡尔式的将精神灵肉与外在自然机械对立割裂的陈旧二元论思维桎梏。"),
        ("begründen", "kein", "Verb", "begründete, begründet", "奠基，确立理论大厦", "Kant begründete eine neue Ära des Denkens, die bis heute weltweit als Meilenstein verehrt wird.", "康德凭借其震古烁今的批判哲学体系，为全人类思想史开辟并奠基了一个崭新的黄金时代，时至今日依然作为不可逾越的理性丰碑受到全球学界的顶礼膜拜。"),
        ("zweifeln", "kein", "Verb", "zweifelte, gezweifelt", "怀疑探究 (an Dat.)", "René Descartes zweifelte an allem, bis er beim unumstößlichen 'Cogito ergo sum' anlangte.", "法国近代哲学奠基人笛卡尔曾对周遭一切肉眼可见之物施以最冷酷无情的普遍怀疑，直至在理性岩石的最深处撞见了那个唯一绝对无法被怀疑的铁打磐石：“我思故我在”。"),
        ("philosophisch", "kein", "Adjektiv", "-", "哲学思辨维度的", "Diese fundamentale ethische Frage berührt den Kern unseres gesamten philosophischen Menschenbildes.", "这项直击灵魂深处的现代生物伦理大考问，正深深触及到了我们整个人类文明关于“人之所以为人”这一终极哲学人性观的最本质内核。"),
        ("rational", "kein", "Adjektiv", "-", "基于理性的", "Eine rationale Begründung von Moral verzichtet bewusst auf religiöse Offenbarungen oder Mythen.", "建立在现代独立理性基石之上的道德合法性奠基，完全摒弃了对任何虚无缥缈的神学天启神谕或远古愚昧神话的依赖，全凭人类自身的清醒反思。"),
        ("vernünftig", "kein", "Adjektiv", "-", "明智合乎理性的", "Es ist vernünftig, langfristige globale Konsequenzen in jede politische Entscheidung einzubeziehen.", "在当代这个牵一发动全身的全球化互联世界里，每一位负责任的治国决策者在落笔签字时，把关乎子孙后代福祉的长远全球次生后果纳入通盘考量，才称得上是真正高瞻远瞩的理智之举。"),
        ("ethisch", "kein", "Adjektiv", "-", "符合伦理准则的", "Wissenschaftlicher Fortschritt ohne ethische Leitplanken führt direkt in die gesellschaftliche Barbarei.", "任何狂飙突进、脱离了神圣人道主义伦理护栏缰绳羁绊的所谓硬核科技单兵突进，最终只会不可避免地把全人类文明生生拖入万劫不复的野蛮杀戮深渊。"),
        ("moralisch", "kein", "Adjektiv", "-", "合乎道德操守的", "Eine moralische Handlung geschieht nicht aus Furcht vor Strafe, sondern aus freier innerer Einsicht.", "真正经得起天地良心检验的高尚道德行径，从来都不是出于对法律皮鞭惩罚的奴颜屈膝畏缩，而是全然发轫于个体灵魂深处由衷领悟善恶后的自觉向善抉择。"),
        ("aufgeklärt", "kein", "Adjektiv", "-", "思想启蒙开化的", "Eine aufgeklärte Bürgerschaft ist das stärkste Bollwerk gegen populistische Demagogen und Autokraten.", "由千千万万具备独立思辨能力、思想高度开化启蒙的清醒公民构筑起的心智城墙，是保卫自由民主共和国免遭各种煽动性民粹蛊惑政客与野心家颠覆的最强坚固堡垒。"),
        ("mündig", "kein", "Adjektiv", "-", "具备独立判断力成熟的", "Das oberste Erziehungsziel muss die Heranbildung mündiger, selbstständig denkender Persönlichkeiten sein.", "国民公共教育最至高无上、最崇高的终极培养天职，永远在于为国家和民族铸就大批具备独立思考风骨、不随波逐流、心智完全成熟自立的现代栋梁。"),
        ("idealistisch", "kein", "Adjektiv", "-", "满怀崇高理想主义的", "Trotz aller bitteren Zynismen der Realpolitik verlor sie nie ihren edlen, idealistischen Glauben an das Gute.", "即便在饱经冷酷现实政治算计的无数次毒打与沧桑洗礼之后，她依然在心底最柔软的角落里永远未曾熄灭那簇纯粹、崇高、甘愿为人类福祉献身的理想主义纯金之火。"),
        ("dialektisch", "kein", "Adjektiv", "-", "具备辩证思维张力的", "Die dialektische Beziehung zwischen Freiheit und Gesetz: Freiheit existiert nur im Rahmen des Rechts.", "自由与法律之间交织着生动深刻的辩证共生张力：绝对脱离了宪法秩序护佑的所谓绝对自由只会沦为丛林弱肉强食的杀戮狂欢，真正的公民自由唯有在法治轨道上才能盛开出最艳丽的花朵。"),
        ("metaphysisch", "kein", "Adjektiv", "-", "形而上超验维度的", "Die Suche nach dem Sinn des Seins ist ein unausrottbares metaphysisches Grundbedürfnis des Menschen.", "无论物质生活多么丰裕奢靡，人类灵魂深处对追问宇宙终极本原与生命归宿何在的形而上超验求索冲动，永远是一道不可磨灭的根本精神刚需。"),
        ("ontologisch", "kein", "Adjektiv", "-", "本体存在论层面的", "Die Frage nach dem Bewusstsein von Maschinen wirft eine radikale ontologische Debatte auf.", "硅基人工智能未来是否可能涌现出真正的自主痛苦体验与灵魂意识，正在当今哲学界引爆一场关于“机器与人何为存在主体”的激进本体论世纪大激辩。"),
        ("existentiell", "kein", "Adjektiv", "-", "事关人生根本生存的", "Schwere Krankheiten konfrontieren uns schlagartig mit existenziellen Grundfragen des Menschseins.", "一场突如其来的罕见重疾噩耗，往往如同一记当头棒喝，瞬间将平日里在名利场争名逐利的世人直接逼到悬崖边缘，去直面生老病死等最严峻的人生存在性终极命题。"),
        ("dogmatisch", "kein", "Adjektiv", "-", "死板教条固步自封的", "Eine dogmatische Weltanschauung schließt jeden fruchtbaren interkulturellen Dialog von vornherein aus.", "抱残守缺、将自身奉为唯一真理代言人的排他性教条主义意识形态作风，在客观上一开始便把任何基于平等尊重的跨文化文明交流互鉴之门彻底焊死关上。"),
        ("skeptisch", "kein", "Adjektiv", "-", "保持审慎怀疑理性的", "Wissenschaftler müssen neuen Verheißungen gegenüber stets eine gesunde skeptische Haltung bewahren.", "面对商业资本与公关推手在媒体上吹得天花乱坠的所谓颠覆性革命新神话，有良知的严肃科学家必须始终在显微镜前保留一份极其清醒冷峻的审慎怀疑定力。"),
        ("autonom", "kein", "Adjektiv", "-", "道德完全自律独立的", "Ein autonomer Mensch handelt nach Gesetzen, die er sich selbst durch seine eigene Vernunft gegeben hat.", "一个真正意义上顶天立地、实现了精神自律的崇高智者，其毕生言行唯一遵循的准绳，正是其凭借内心纯粹理性自审自律所庄严颁行给自己的人生最高律令。"),
        ("heteronom", "kein", "Adjektiv", "-", "盲从他律受制于人的", "Heteronomes Handeln geschieht aus Angst vor Strafe, sozialem Druck oder opportunistischer Gewinnsucht.", "完全处于受制于人状态的他律盲从行为，其可悲的驱使动力无外乎三样东西：对皮鞭的懦弱恐惧、对平庸世俗同侪压力的妥协顺从，或是对卑鄙蝇头小利的投机贪婪。"),
        ("kategorisch", "kein", "Adjektiv", "-", "无条件绝对无上命令的", "Das Folterverbot gilt im modernen Völkerrecht als eine absolute, kategorische Menschenrechtsnorm.", "在现代日内瓦公约与国际人权法体系之中，对任何战俘与嫌犯严禁实施刑讯逼供的禁令，被庄严确立为一项在任何紧急状态下均绝对不可破例的无条件绝对刚性底线。"),
        ("universal", "kein", "Adjektiv", "-", "普适全球四海皆准的", "Die universale Gültigkeit der Menschenrechte verbietet jegliche relativierende kulturelle Beschönigung.", "联合国《世界人权宣言》所确立的各项基本人权规范所具备的普适全人类崇高特质，坚决不容许任何别有用心者打着所谓“特殊国情文化差异”的旗号予以曲解阉割与粉饰洗白。"),
        ("dogmenfrei", "kein", "Adjektiv", "-", "彻底打破一切教条束缚的", "Nur eine vollkommen dogmenfreie Forschung führt zu revolutionären Durchbrüchen an den Grenzen des Wissens.", "唯有一处彻底打破学术门阀派系藩篱、允许年轻后生向学术权威大胆亮剑挑战的完全无拘无束自由研讨净土，方能孕育出真正叩击人类认知极限的最伟大颠覆性突破。"),
        ("epochemachend", "kein", "Adjektiv", "-", "开辟划时代全新纪元的", "Kants Schriften leiteten eine epochemachende Wende in der Philosophiegeschichte der Menschheit ein.", "伊曼努尔·康德笔下流淌出的三大批判皇皇巨著，如同横空出世的哥白尼日心说大革命，正式拉开了全人类哲学与人文思想史开天辟地、划时代全新纪元的宏伟序幕。")
    ]
}

print("Lessons 11 and 12 built successfully!")
