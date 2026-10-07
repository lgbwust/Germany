#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A2 Part 1: Lessons 1 to 5 (350 words)
L01: 个人简历、成长经历与过去时 (Biografie, Lebenslauf & Kindheit) - 70 words
L02: 学校教育、双元制培训与进修 (Schule, Ausbildung & Weiterbildung) - 70 words
L03: 办公日常、团队协作与商务邮件 (Arbeitsalltag, Büro & E-Mails) - 70 words
L04: 房屋租赁、邻里关系与搬家乔迁 (Wohnen, Nachbarn & Umzug) - 70 words
L05: 商品消费、网购与售后维权 (Einkaufen, Konsum & Reklamation) - 70 words
"""

LESSONS_A2_PART1 = [
    # LESSON 1
    {
        "id": "A2_L01",
        "title": "第1课：个人简历、成长经历与过去时 (Biografie & Lebenslauf)",
        "summary": "掌握情态动词与sein/haben的过去时(Präteritum)、个人履历词汇与人生阶段表达",
        "grammar": {
            "title": "过去时 (Präteritum) 与人生履历描述",
            "sections": [
                {
                    "heading": "1. sein, haben 与情态动词过去时",
                    "content": "• war (ich war, du warst, er war, wir waren, ihr wart, sie waren)\n• hatte (ich hatte, du hattest, er hatte, wir hatten, ihr hattet, sie hatten)\n• konnte (können), musste (müssen), wollte (wollen), durfte (dürfen)\n例：Als Kind war ich oft bei meinen Großeltern."
                },
                {
                    "heading": "2. 时间连词 als vs wenn",
                    "content": "• als: 引导过去发生的【单次、特定时间点】从句（动词置于句末）！\n  Als ich zehn Jahre alt war, zogen wir nach Frankfurt.\n• wenn: 引导过去多次发生的习惯性动作或现在/将来的条件从句。"
                }
            ]
        },
        "quiz": [
            {
                "id": "A2_L01_Q1",
                "type": "GRAMMAR_FILL",
                "question": "______ ich ein Kind war, spielte ich täglich draußen.",
                "options": ["Als", "Wenn", "Wann", "Weil"],
                "correctIndex": 0,
                "explanation": "引导过去单次、特定的人生阶段或时间点使用连词 als。"
            },
            {
                "id": "A2_L01_Q2",
                "type": "VOCAB_MEANING",
                "question": "求职简历中的核心词汇 'der Lebenslauf' 意思是：",
                "options": ["个人简历", "生活经历", "跑步比赛", "出生证明"],
                "correctIndex": 0,
                "explanation": "der Lebenslauf 是德语求职中标准“个人履历、简历”的意思。"
            }
        ],
        "words": [
            ("die Biografie", "die", "n.", "-n", "传记，生平简历", "Er hat eine faszinierende Biografie geschrieben.", "他写了一本引人入胜的传记。"),
            ("der Lebenslauf", "der", "n.", "Lebensläufe", "简历，履历表", "Dem Bewerbungsschreiben liegt ein Lebenslauf bei.", "求职信附有一份简历。"),
            ("das Leben", "das", "n.", "-", "生活，一生", "Sie blickt auf ein erfülltes Leben zurück.", "她回顾了充实的一生。"),
            ("die Kindheit", "die", "n.", "-", "童年，幼年时代", "Ich hatte eine glückliche Kindheit auf dem Land.", "我在乡下度过了幸福的童年。"),
            ("die Jugend", "die", "n.", "-", "青年时期，青春", "In seiner Jugend spielte er semiprofessionell Fußball.", "他青年时期踢过半职业足球。"),
            ("das Alter", "das", "n.", "-", "年龄，晚年", "Im hohen Alter zog er zu seiner Tochter.", "在晚年他搬去和女儿同住。"),
            ("die Vergangenheit", "die", "n.", "-", "过去，往昔", "Man sollte aus der Vergangenheit lernen.", "人应当从过去中汲取教训。"),
            ("die Gegenwart", "die", "n.", "-", "现在，当代", "Wir müssen die Gegenwart aktiv gestalten.", "我们必须积极把握现在。"),
            ("die Zukunft", "die", "n.", "-", "未来，前途", "Ich blicke optimistisch in die Zukunft.", "我乐观地展望未来。"),
            ("die Erinnerung", "die", "n.", "-en", "回忆，记忆", "Daran habe ich wunderschöne Erinnerungen.", "对此我怀有美好的回忆。"),
            ("erinnern", "", "v.", "erinnert, erinnerte, erinnert", "使想起；回忆", "Erinnerst du dich an unseren ersten Urlaub?", "你还记得我们的第一次度假吗？"),
            ("vergessen", "", "v.", "vergisst, vergaß, vergessen", "忘记", "Ich werde diesen Tag niemals vergessen.", "我将永远不会忘记这一天。"),
            ("aufwachsen", "", "v.", "wächst auf, wuchs auf, ist aufgewachsen", "长大，成长", "Ich bin in einer kleinen Stadt aufgewachsen.", "我在一座小城市长大。"),
            ("erziehen", "", "v.", "erzieht, erzog, erzogen", "抚养，教育", "Eltern erziehen ihre Kinder mit viel Liebe.", "父母充满爱意地抚养孩子。"),
            ("die Erziehung", "die", "n.", "-", "教养，家庭教育", "Gute Erziehung ist ein wertvolles Fundament.", "良好的教养是宝贵的基石。"),
            ("die Erfahrung", "die", "n.", "-en", "经验，阅历", "Er hat viel Erfahrung im Außenhandel gesammelt.", "他在外贸领域积累了丰富经验。"),
            ("erfahren", "", "v.", "erfährt, erfuhr, erfahren", "得知；获悉", "Wann hast du von der Neuigkeit erfahren?", "你何时得知这则消息的？"),
            ("das Erlebnis", "das", "n.", "-se", "经历，难忘体验", "Die Reise nach Tibet war ein großes Erlebnis.", "西藏之行是一次难忘的经历。"),
            ("erleben", "", "v.", "erlebt, erlebte, erlebt", "体验，亲身经历", "Wir haben dort viele spannende Abenteuer erlebt.", "我们在那里经历了很多惊险历险。"),
            ("der Meilenstein", "der", "n.", "-e", "里程碑", "Das Examen war ein wichtiger Meilenstein.", "毕业考是一座重要里程碑。"),
            ("die Karriere", "die", "n.", "-n", "职业生涯，事业", "Sie macht steile Karriere in der Industrie.", "她在工业界平步青云。"),
            ("der Erfolg", "der", "n.", "-e", "成就，成功", "Hartes Training bringt sichtbaren Erfolg.", "刻苦训练带来显著的成功。"),
            ("erfolgreich", "", "adj.", "erfolgreicher, am erfolgreichsten", "成功的", "Das Projekt war überaus erfolgreich.", "该项目极为成功。"),
            ("der Misserfolg", "der", "n.", "-e", "失败，挫折", "Lassen Sie sich durch Misserfolge nicht entmutigen!", "不要被失败挫伤了锐气！"),
            ("der Traum", "der", "n.", "Träume", "梦想，愿望", "Ihr großer Traum ging endlich in Erfüllung.", "她的远大梦想终于成真了。"),
            ("träumen", "", "v.", "träumt, träumte, geträumt", "梦想，做梦", "Er träumt von einer Weltreise.", "他梦想着一次环球旅行。"),
            ("der Wunsch", "der", "n.", "Wünsche", "愿望，心愿", "Mein sehnlichster Wunsch ist ein eigenes Haus.", "我最大的愿望是拥有一栋自己的房子。"),
            ("wünschen", "", "v.", "wünscht, wünschte, gewünscht", "希冀，祝愿", "Ich wünsche mir mehr Zeit für die Familie.", "我希望有更多时间陪伴家人。"),
            ("das Ziel", "das", "n.", "-e", "目标，目的地", "Man muss sich klare Ziele im Leben setzen.", "人在生活中必须树立清晰的目标。"),
            ("erreichen", "", "v.", "erreicht, erreichte, erreicht", "达到，实现", "Sie hat ihr berufliches Ziel erreicht.", "她达成了自己的职业目标。"),
            ("entscheiden", "", "v.", "entscheidet, entschied, entschieden", "决定，抉择", "Er entschied sich für ein Medizinstudium.", "他决定选择攻读医学专业。"),
            ("die Entscheidung", "die", "n.", "-en", "决定，决议", "Das war eine mutige und richtige Entscheidung.", "那是一个勇敢且正确的决定。"),
            ("ändern", "", "v.", "ändert, änderte, geändert", "改变，更改", "Die Zeiten haben sich stark geändert.", "时代已经发生了巨大的改变。"),
            ("die Veränderung", "die", "n.", "-en", "转变，变革", "Im Beruf braucht man manchmal Veränderungen.", "职场上有时需要做出改变。"),
            ("beginnen", "", "v.", "beginnt, begann, begonnen", "着手，开展", "Ein neues Kapitel seines Lebens begann.", "他人生的崭新篇章开始了。"),
            ("der Anfang", "der", "n.", "Anfänge", "起初，开端", "Aller Anfang ist bekanntlich schwer.", "众所周知，万事开头难。"),
            ("anfangs", "", "adv.", "", "起初，最初", "Anfangs fiel mir das Sprechen schwer.", "起初开口说话对我来说挺难的。"),
            ("schließlich", "", "adv.", "", "最终，终于", "Nach langer Suche fand er schließlich eine Stelle.", "经过漫长寻找他最终找到了一份工作。"),
            ("damals", "", "adv.", "", "当时，那时", "Damals gab es noch keine Mobiltelefone.", "那时候甚至还没有移动电话。"),
            ("früher", "", "adv.", "", "从前，以前", "Früher war hier eine grüne Wiese.", "从前这里是一片绿色的草地。"),
            ("heutzutage", "", "adv.", "", "如今，当今", "Heutzutage kommuniziert man digital.", "如今人们通过数字化手段沟通。"),
            ("die Generation", "die", "n.", "-en", "一代人，世代", "Jede Generation hat ihre eigenen Werte.", "每一代人都有自己的价值观。"),
            ("die Tradition", "die", "n.", "-en", "传统，习俗", "Familientraditionen werden gepflegt.", "家族传统得到了良好的传承。"),
            ("stammen", "", "v.", "stammt, stammte, gestammt", "出身于，源自", "Sie stammt aus einer Lehrerfamilie.", "她出身于一个教师家庭。"),
            ("die Herkunft", "die", "n.", "-", "出身，籍贯", "Seine Herkunft spielt keine Rolle.", "他的出身并不重要。"),
            ("die Heimat", "die", "n.", "-", "家乡，故乡", "Deutschland wurde ihm zur zweiten Heimat.", "德国成了他的第二故乡。"),
            ("das Heimweh", "das", "n.", "-", "思乡病，想家", "Am Anfang hatte sie großes Heimweh.", "刚开始她非常想念家乡。"),
            ("auswandern", "", "v.", "wandert aus, wanderte aus, ist ausgewandert", "移居国外，移民", "Viele Deutsche wanderten im 19. Jahrhundert aus.", "19世纪许多德国人移居海外。"),
            ("die Auswanderung", "die", "n.", "-en", "移民出境", "Die Auswanderung nach Amerika war beschwerlich.", "移民去美洲的路途非常艰辛。"),
            ("einwandern", "", "v.", "wandert ein, wanderte ein, ist eingewandert", "迁入，移民入境", "Seine Großeltern wanderten in die Schweiz ein.", "他的祖父母移民迁入了瑞士。"),
            ("der Migrant", "der", "n.", "-en", "移民", "Viele Migranten bereichern die Gesellschaft.", "许多移民丰富了社会多元性。"),
            ("die Integration", "die", "n.", "-", "融入，融合", "Sprache ist der Schlüssel zur Integration.", "语言是融入社会的钥匙。"),
            ("integrieren", "", "v.", "integriert, integrierte, integriert", "融入，融入社会", "Er hat sich schnell in die Gemeinschaft integriert.", "他很快融入了社区集体。"),
            ("die Staatsangehörigkeit", "die", "n.", "-en", "国籍", "Sie besitzt die doppelte Staatsangehörigkeit.", "她拥有双重国籍身份。"),
            ("der Pass", "der", "n.", "Pässe", "护照", "Mein deutscher Pass ist zehn Jahre gültig.", "我的德国护照有效期为十年。"),
            ("der Ausweis", "der", "n.", "-e", "身份证件", "Zeigen Sie bitte Ihren Personalausweis vor!", "请出示您的个人身份证！"),
            ("das Dokument", "das", "n.", "-e", "文件，证件", "Wichtige Dokumente sollte man sicher aufbewahren.", "重要证件应妥善安全保管。"),
            ("die Urkunde", "die", "n.", "-n", "公证书，证书", "Die Geburtsurkunde muss übersetzt werden.", "出生医学证明必须经过翻译。"),
            ("bestätigen", "", "v.", "bestätigt, bestätigte, bestätigt", "证实，开具证明", "Die Behörde bestätigt die Angaben.", "主管部门确认了所填信息属实。"),
            ("die Bestätigung", "die", "n.", "-en", "确认函，证明", "Ich benötige eine schriftliche Bestätigung.", "我需要一份书面确认证明。"),
            ("das Zeugnis", "das", "n.", "-se", "成绩单；鉴定证书", "Ihr Zeugnis weist hervorragende Noten auf.", "她的成绩单上成绩优异。"),
            ("der Abschluss", "der", "n.", "Abschlüsse", "结业，毕业文凭", "Er hat seinen Masterabschluss in Physik gemacht.", "他拿到了物理学硕士文凭。"),
            ("abschließen", "", "v.", "schließt ab, schloss ab, abgeschlossen", "完成，结束", "Sie schloss ihr Studium mit Auszeichnung ab.", "她以优等成绩完成了大学学业。"),
            ("qualifiziert", "", "adj.", "qualifizierter, am qualifiziertesten", "具有资质的，合格的", "Wir suchen hoch qualifizierte Fachkräfte.", "我们寻找高素质专业人才。"),
            ("die Fähigkeit", "die", "n.", "-en", "才能，技能", "Analytische Fähigkeiten sind sehr gefragt.", "分析能力在职场上非常吃香。"),
            ("die Kenntnis", "die", "n.", "-se", "知识，技能（多用复数）", "Gute Kenntnisse in Excel werden vorausgesetzt.", "熟练掌握Excel是基本要求。"),
            ("die Stärke", "die", "n.", "-n", "长处，优势", "Teamfähigkeit gehört zu meinen Stärken.", "团队协作能力是我的强项之一。"),
            ("die Schwäche", "die", "n.", "-n", "弱点，劣势", "Man sollte offen über seine Schwächen sprechen.", "人应当坦诚谈论自己的不足。"),
            ("interessiert", "", "adj.", "", "感兴趣的", "Ich bin sehr an dieser Position interessiert.", "我对这个岗位非常感兴趣。"),
            ("das Vorbild", "das", "n.", "-er", "楷模，榜样", "Seine Großmutter war stets sein großes Vorbild.", "他的祖母一直是他心中的大榜样。")
        ]
    },

    # LESSON 2
    {
        "id": "A2_L02",
        "title": "第2课：学校教育、双元制培训与进修 (Schule & Ausbildung)",
        "summary": "掌握第二格属格(Genitiv)基础、德语区特色双元制职业培训与进修教育",
        "grammar": {
            "title": "第二格 (Genitiv) 基础与表示从属关系",
            "sections": [
                {
                    "heading": "1. 第二格 (Genitiv) 冠词与名词词尾变化",
                    "content": "• 阳性/中性：des Lehrers / des Kindes (名词加 -(e)s 词尾)\n• 阴性/复数：der Schule / der Universitäten (名词不加词尾)\n• 口语替代：von + Dativ (das Auto von meinem Vater = das Auto meines Vaters)"
                },
                {
                    "heading": "2. 原因从属连词 weil (因为) 框形结构",
                    "content": "weil 引导从句，变位动词永远置于从句句末！\n例：Er macht eine Ausbildung, weil er praktische Berufe mag."
                }
            ]
        },
        "quiz": [
            {
                "id": "A2_L02_Q1",
                "type": "GRAMMAR_FILL",
                "question": "Das ist das Büro ______ (der Direktor, 第二格所属格).",
                "options": ["des Direktors", "dem Direktor", "den Direktor", "der Direktor"],
                "correctIndex": 0,
                "explanation": "阳性名词在第二格中定冠词变为 des，名词词尾补加 -s (des Direktors)。"
            },
            {
                "id": "A2_L02_Q2",
                "type": "EXAM_REAL",
                "question": "德国著名的特色职业教育模式 'Duale Ausbildung'（双元制）是指：",
                "options": ["理论在职校学习，实操在企业学徒", "读两所大学拿两个学位", "网上和线下同时上课", "白天上学晚上打工"],
                "correctIndex": 0,
                "explanation": "Duale Ausbildung 是德国最具特色的职教体制，一半在职业学校学理论，一半在企业实践。"
            }
        ],
        "words": [
            ("das Schulsystem", "das", "n.", "-e", "学校体制，学制", "Das deutsche Schulsystem ist dreigliedrig.", "德国的中学体制分为三个层级。"),
            ("die Grundschule", "die", "n.", "-n", "小学", "In Deutschland dauert die Grundschule meist vier Jahre.", "在德国小学学制通常为四年。"),
            ("das Gymnasium", "das", "n.", "Gymnasien", "文理中学（升大学方向）", "Nach dem Gymnasium macht man das Abitur.", "文理中学毕业后参加高中毕业考。"),
            ("die Realschule", "die", "n.", "-n", "实科中学", "Die Realschule schließt mit der Mittleren Reife ab.", "实科中学以中级成熟证书毕业。"),
            ("die Hauptschule", "die", "n.", "-n", "主干中学，普通中学", "Die Hauptschule vermittelt grundlegende Bildung.", "普通中学教授基础性通用知识。"),
            ("die Gesamtschule", "die", "n.", "-n", "综合中学", "In der Gesamtschule lernen alle Kinder gemeinsam.", "在综合中学里所有儿童共同就读。"),
            ("das Abitur", "das", "n.", "-", "高中毕业考，大学入学资格", "Sie bereitet sich intensiv auf das Abitur vor.", "她正在全力以赴冲刺高中毕业考。"),
            ("die Note", "die", "n.", "-n", "分数，成绩", "In Deutschland ist eine Eins die beste Note.", "在德国1分是最好最优的成绩。"),
            ("die Eins", "die", "n.", "-en", "一分（优等，最高分）", "Er hat eine glatte Eins in Mathematik bekommen.", "他数学拿到了一个干脆利落的满分1分。"),
            ("die Sechs", "die", "n.", "-en", "六分（不及格，最差分）", "Eine Sechs bedeutet ungenügend.", "6分意味着成绩完全不合格。"),
            ("das Zeugnis", "das", "n.", "-se", "成绩单，鉴定书", "Ende Januar gibt es die Halbjahreszeugnisse.", "一月底发放半学期成绩单。"),
            ("das Fach", "das", "n.", "Fächer", "学科，专业科目", "Mein Lieblingsfach war immer Biologie.", "我最喜欢的学科一直是生物。"),
            ("die Mathematik", "die", "n.", "-", "数学", "Mathematik erfordert logisches Verständnis.", "数学需要严密的逻辑理解力。"),
            ("die Physik", "die", "n.", "-", "物理学", "Physik ist die Lehre von der Natur.", "物理学是研究自然本质的学科。"),
            ("die Chemie", "die", "n.", "-", "化学", "Im Chemielabor führen wir Experimente durch.", "在化学实验室我们进行实验。"),
            ("die Biologie", "die", "n.", "-", "生物学", "In Biologie lernen wir über Ökosysteme.", "在生物课上我们学习生态系统。"),
            ("die Geschichte", "die", "n.", "-", "历史学；故事", "Europäische Geschichte ist sehr facettenreich.", "欧洲历史非常丰富多元。"),
            ("die Geografie", "die", "n.", "-", "地理学", "In Geografie zeichnen die Schüler Landkarten.", "在地理课上学生们绘制地图。"),
            ("der Unterricht", "der", "n.", "-", "课程，授课", "Der Unterricht beginnt pünktlich um 8 Uhr.", "课程在早晨8点准时开始。"),
            ("die Stunde", "die", "n.", "-n", "课时，小时", "In der dritten Stunde haben wir Sport.", "第三节课我们上体育课。"),
            ("der Stundenplan", "der", "n.", "Stundenpläne", "课程表", "Auf dem Stundenplan stehen 30 Wochenstunden.", "课程表上一周排了30个课时。"),
            ("die Hausaufgabe", "die", "n.", "-n", "家庭作业", "Hast du schon deine Hausaufgaben gemacht?", "你的家庭作业做完了吗？"),
            ("der Test", "der", "n.", "-s", "小测验，测试", "Morgen schreiben wir einen Vokabeltest.", "明天我们要进行词汇小测验。"),
            ("die Klassenarbeit", "die", "n.", "-en", "班级期中大考", "Die Klassenarbeit in Deutsch war fair.", "德语期中统考题目出得很公道。"),
            ("die Prüfung", "die", "n.", "-en", "考试", "Vor der Prüfung sind viele Studenten nervös.", "考试前许多大学生心情紧张。"),
            ("bestehen", "", "v.", "besteht, bestand, bestanden", "考取，及格", "Er hat die Führerscheinprüfung bestanden.", "他通过了驾照科目考试。"),
            ("durchfallen", "", "v.", "fällt durch, fiel durch, ist durchgefallen", "挂科，不及格", "Sie fiel leider in der mündlichen Prüfung durch.", "她遗憾在口试环节没有及格。"),
            ("wiederholen", "", "v.", "wiederholt, wiederholte, wiederholt", "留级重修；复习", "Er musste die neunte Klasse wiederholen.", "他不得不把九年级留级重修一年。"),
            ("die Ausbildung", "die", "n.", "-en", "职业培训", "Eine Ausbildung dauert in der Regel drei Jahre.", "职业培训通常为期三年。"),
            ("die Berufsschule", "die", "n.", "-n", "职业学校", "Zwei Tage die Woche geht er in die Berufsschule.", "他每周有两天去职业学校上课。"),
            ("der Azubi", "der", "n.", "-s", "学徒工（口语简称）", "Die Azubis werden von erfahrenen Meistern betreut.", "学徒工由经验丰富的师傅带领。"),
            ("der Auszubildende", "der", "n.", "-n", "受训学徒，徒工", "Der Betrieb stellt fünf neue Auszubildende ein.", "该企业新录用了五名受训学员。"),
            ("der Betrieb", "der", "n.", "-e", "企业，工场", "Im Betrieb lernen sie den praktischen Ablauf.", "在企业里他们学习实际运作流程。"),
            ("der Meister", "der", "n.", "-", "老师傅，工匠大师", "Der Meister leitet die Schreinerei.", "老师傅掌管着木匠铺。"),
            ("die Lehre", "die", "n.", "-n", "学徒期，学徒工训练", "Er macht eine Lehre als Mechatroniker.", "他在接受机电一体化机械师的学徒培训。"),
            ("der Lehrling", "der", "n.", "-e", "学徒，见习生", "Als Lehrling verdient man ein kleines Gehalt.", "作为学徒能领到一份微薄补贴。"),
            ("die Praxis", "die", "n.", "-", "实践，实操", "Theorie und Praxis werden optimal verknüpft.", "理论与实践得到了极其良好的结合。"),
            ("die Theorie", "die", "n.", "-n", "理论", "In der Theorie klingt das Konzept überzeugend.", "在理论上这个方案听起来很有说服力。"),
            ("die Weiterbildung", "die", "n.", "-en", "在职进修，进修深造", "Lebenslange Weiterbildung sichert den Arbeitsplatz.", "终身在职进修能保障工作岗位。"),
            ("die Fortbildung", "die", "n.", "-en", "业务提升，业务进修", "Er nimmt an einer Fortbildung für Führungskräfte teil.", "他参加了管理人员业务深造。"),
            ("der Kurs", "der", "n.", "-e", "培训班，短训课程", "Ein Intensivkurs für technisches Englisch.", "一个科技英语强化培训班。"),
            ("das Seminar", "das", "n.", "-e", "研讨会，研讨班", "Das Seminar vermittelt modernes Projektmanagement.", "该研讨班讲授现代项目管理。"),
            ("der Workshop", "der", "n.", "-s", "工作坊，实操研修班", "Im Workshop erarbeiten wir gemeinsam Lösungen.", "在工作坊中我们群策群力共商方案。"),
            ("teilnehmen", "", "v.", "nimmt teil, nahm teil, teilgenommen", "参加，参与 (接 an + Dat)", "Sie nimmt regelmäßig an Schulungen teil.", "她经常性地参加专业技能培训。"),
            ("die Teilnahme", "die", "n.", "-", "参与，出席", "Die Teilnahme am Kurs ist verpflichtend.", "按时出席本课程是硬性要求的。"),
            ("die Teilnahmebescheinigung", "die", "n.", "-en", "参训证明结业单", "Am Ende erhalten Sie eine Teilnahmebescheinigung.", "结束后您将获得结业证明单。"),
            ("das Wissen", "das", "n.", "-", "学识，知识储备", "Er verfügt über breites Fachwissen.", "他具备广博深厚的专业知识储备。"),
            ("die Kompetenz", "die", "n.", "-en", "专业素养，能力", "Digitale Kompetenzen sind unverzichtbar.", "数字化专业素养不可或缺。"),
            ("die Methode", "die", "n.", "-n", "教学法，研究方法", "Moderne Methoden erleichtern das Lernen.", "先进的方法让学习更事半功倍。"),
            ("die Vorlesung", "die", "n.", "-en", "大学大课讲座", "Die Vorlesung findet im Audimax statt.", "大课在全校最大阶梯教室举行。"),
            ("der Hörsaal", "der", "n.", "Hörsäle", "阶梯教室，讲堂", "Der Hörsaal ist bis auf den letzten Platz besetzt.", "阶梯教室座无虚席。"),
            ("der Professor", "der", "n.", "-en", "男教授", "Der Professor forscht auf dem Gebiet der KI.", "教授在人工智能领域开展科研。"),
            ("die Professorin", "die", "n.", "-nen", "女教授", "Die Professorin hält eine spannende Vorlesung.", "女教授做了一场引人入胜的学术大课。"),
            ("die Mensa", "die", "n.", "Mensen", "大学食堂", "Die Mensa bietet günstige Mahlzeiten für Studenten.", "大学食堂为学生提供平价餐食。"),
            ("das Semester", "das", "n.", "-", "学期", "Das Wintersemester beginnt im Oktober.", "冬季学期在十月份拉开帷幕。"),
            ("die Ferien", "die", "n.pl.", "-", "寒暑假期", "Die vorlesungsfreie Zeit wird für Hausarbeiten genutzt.", "无课假期被用来撰写学术期末论文。"),
            ("die Klausur", "die", "n.", "-en", "闭卷考试", "In der Prüfungsphase schreibt er vier Klausuren.", "在考试月他要参加四门闭卷考试。"),
            ("das Referat", "das", "n.", "-e", "课堂专题报告，学术展示", "Sie hält ein Referat über erneuerbare Energien.", "她就可再生能源做了一次课堂专题展示。"),
            ("die Präsentation", "die", "n.", "-en", "幻灯汇报，展示", "Die Präsentation überzeugte alle Anwesenden.", "幻灯汇报征服了全场所有在座者。"),
            ("präsentieren", "", "v.", "präsentiert, präsentierte, präsentiert", "展示，陈述报告", "Er präsentiert die Quartalsergebnisse.", "他在陈述汇报季度业绩结果。"),
            ("die Folie", "die", "n.", "-n", "幻灯片页面，胶片", "Auf der nächsten Folie sehen Sie die Statistik.", "在下一张幻灯片上大家能看到统计数据。"),
            ("das Thema", "das", "n.", "Themen", "议题，研究主题", "Das Thema der Bachelorarbeit ist hochaktuell.", "学士毕业论文的选题极具时效前沿性。"),
            ("die Bibliothek", "die", "n.", "-en", "大学图书馆", "In der Universitätsbibliothek gilt strikte Ruhe.", "在大学图书馆必须严格保持安静。"),
            ("ausleihen", "", "v.", "leiht aus, lieh aus, ausgeliehen", "外借，借阅", "Ich möchte Fachliteratur für die Arbeit ausleihen.", "我想为论文借阅几本专业文献。"),
            ("forschen", "", "v.", "forscht, forschte, geforscht", "从事科研研究", "Wissenschaftler forschen an neuen Impfstoffen.", "科学家们在潜心研发新型疫苗。"),
            ("die Forschung", "die", "n.", "-en", "科学研究，科研", "Deutschland investiert viel Geld in die Forschung.", "德国在科研研发上投入了巨额资金。"),
            ("die Wissenschaft", "die", "n.", "-en", "学术，科学", "Die Wissenschaft liefert faktenbasierte Erkenntnisse.", "科学提供基于确凿事实的认知。"),
            ("der Wissenschaftler", "der", "n.", "-", "科学家，学者", "Ein international renommierter Wissenschaftler.", "一位国际知名的学者科学家。"),
            ("der Stipendiat", "der", "n.", "-en", "奖学金获得者", "Er ist Stipendiat der Humboldt-Stiftung.", "他是洪堡基金会奖学金的学者。"),
            ("das Stipendium", "das", "n.", "Stipendien", "奖学金", "Sie bewarb sich erfolgreich um ein Stipendium.", "她成功申领到了一笔求学奖学金。")
        ]
    },

    # LESSON 3
    {
        "id": "A2_L03",
        "title": "第3课：办公日常、团队协作与商务邮件 (Arbeitsalltag & Büro)",
        "summary": "掌握情态动词过去时、办公室设备、商务信函与电话沟通技巧",
        "grammar": {
            "title": "情态动词过去时 (Präteritum der Modalverben)",
            "sections": [
                {
                    "heading": "1. 情态动词过去时变位规则（变音符号全部去掉）",
                    "content": "• müssen -> musste (ich musste, du musstest, er musste, wir mussten)\n• können -> konnte (ich konnte, du konntest, er konnte, wir konnten)\n• dürfen -> durfte (ich durfte, du durftest, er durfte, wir durften)\n• wollen -> wollte (ich wollte, du wolltest, er wollte, wir wollten)"
                },
                {
                    "heading": "2. 商务电子邮件标准首尾格式",
                    "content": "• 信头称谓：Sehr geehrte Damen und Herren (泛称) / Sehr geehrter Herr Dr. Meyer (男士) / Sehr geehrte Frau Schmidt (女士)\n• 正文首句小写：vielen Dank für Ihre E-Mail...\n• 结尾落款：Mit freundlichen Grüßen"
                }
            ]
        },
        "quiz": [
            {
                "id": "A2_L03_Q1",
                "type": "GRAMMAR_FILL",
                "question": "Gestern war ich krank und ______ (müssen) zu Hause bleiben.",
                "options": ["musste", "muss", "müsste", "gemusst"],
                "correctIndex": 0,
                "explanation": "叙述过去的义务，müssen 过去时第一人称为 musste。"
            },
            {
                "id": "A2_L03_Q2",
                "type": "EXAM_REAL",
                "question": "在德国写正式商务公函，已知收信人为男性穆勒先生，最得体的抬头称谓是：",
                "options": ["Sehr geehrter Herr Müller,", "Lieber Herr Müller,", "Hallo Müller,", "Guten Tag Mann Müller,"],
                "correctIndex": 0,
                "explanation": "Sehr geehrter Herr Müller, 是正式公函针对男士最高规格的规范称呼。"
            }
        ],
        "words": [
            ("der Alltag", "der", "n.", "-", "日常日常事务", "Im Büroalltag muss man Prioritäten setzen.", "在办公日常中必须划分轻重缓急。"),
            ("die Aufgabe", "die", "n.", "-n", "工作任务，职责", "Zu meinen Aufgaben gehört die Kundenbetreuung.", "我的职责之一是负责客户维护。"),
            ("die Pflicht", "die", "n.", "-en", "责任，义务", "Pünktlichkeit ist die erste Pflicht im Beruf.", "守时是职场上的第一要义。"),
            ("verantwortlich", "", "adj.", "", "负有责任的 (für + Akk)", "Wer ist für diesen Projektbereich verantwortlich?", "谁负责管理这个项目板块？"),
            ("die Verantwortung", "die", "n.", "-en", "担当，责任心", "Er übernimmt gerne Verantwortung im Team.", "他很乐意在团队中主动承担责任。"),
            ("das Projekt", "das", "n.", "-e", "项目，工程", "Das internationale Projekt läuft nach Plan.", "这个国际化项目正按既定计划推进。"),
            ("die Leitung", "die", "n.", "-en", "领导层；管理管理权", "Sie übernahm die Leitung der Abteilung.", "她接管了该部门的领导重任。"),
            ("der Leiter", "der", "n.", "-", "主管，部长", "Der Abteilungsleiter lädt zum Gespräch ein.", "部门主管邀请大家进行谈话。"),
            ("die Abteilung", "die", "n.", "-en", "部门，科室", "Die Personalabteilung sucht neue Mitarbeiter.", "人力资源部正在招募新员工。"),
            ("das Team", "das", "n.", "-s", "工作团队", "Ein gut eingespieltes Team arbeitet produktiver.", "默契的工作团队产出效率更高。"),
            ("zusammenarbeiten", "", "v.", "arbeitet zusammen, arbeitete zusammen, zusammengearbeitet", "齐心协作，合作", "Wir arbeiten eng mit Kollegen in Wien zusammen.", "我们同维也纳的同事保持紧密协作。"),
            ("die Zusammenarbeit", "die", "n.", "-", "协作，合作伙伴关系", "Vielen Dank für die angenehme Zusammenarbeit!", "非常感谢这段愉快的合作！"),
            ("die Besprechung", "die", "n.", "-en", "工作例会，研商", "Die Besprechung beginnt pünktlich um zehn.", "例会上午十点整准时召开。"),
            ("die Konferenz", "die", "n.", "-en", "大型研讨会，专业会议", "Auf der Konferenz tauschen Experten Ideen aus.", "在大会上各位专家交流了独到构想。"),
            ("der Konferenzraum", "der", "n.", "Konferenzräume", "会议室", "Der Konferenzraum ist für zwei Stunden gebucht.", "会议室已被预订了两个小时。"),
            ("das Protokoll", "das", "n.", "-e", "会议纪要，笔录", "Wer schreibt heute das Protokoll der Sitzung?", "今天由谁来做会议纪要笔录？"),
            ("die Tagesordnung", "die", "n.", "-en", "会议议程", "Auf der Tagesordnung stehen fünf Punkte.", "会议议程上列出了五项议题。"),
            ("der Termin", "der", "n.", "-e", "日程，预约时间", "Ich habe morgen einen wichtigen Kundentermin.", "我明天有一个重要的客户拜访日程。"),
            ("die Frist", "die", "n.", "-en", "截止日期，期限", "Die Frist für die Abgabe endet am Freitag.", "提交材料的截止期限为本周五。"),
            ("rechtzeitig", "", "adj./adv.", "rechtzeitiger, am rechtzeitigsten", "及时的，按时", "Bitte reichen Sie die Unterlagen rechtzeitig ein!", "请务必按时提交材料！"),
            ("die Unterlagen", "die", "n.pl.", "-", "书面资料，文件包", "Ich habe Ihnen alle relevanten Unterlagen gemailt.", "我已将全部相关资料发至您的邮箱。"),
            ("das Dokument", "das", "n.", "-e", "文档，正式文件", "Speichern Sie das Dokument auf dem Server ab!", "请将文档保存在公共服务器上！"),
            ("die Datei", "die", "n.", "-en", "电子文件，数据文档", "Können Sie die Datei als PDF exportieren?", "您能把该文件导出为PDF格式吗？"),
            ("der Ordner", "der", "n.", "-", "文件夹", "Er legt die Rechnungen im Ordner ab.", "他把发票账单规整到文件夹中。"),
            ("ablegen", "", "v.", "legt ab, legte ab, abgelegt", "归档，存放", "Alle Dokumente sind chronologisch abgelegt.", "所有文件均按时间先后顺序完成归档。"),
            ("löschen", "", "v.", "löscht, löschte, gelöscht", "删除；灭火", "Haben Sie die alte Datei versehentlich gelöscht?", "您不小心把旧文件删除了吗？"),
            ("speichern", "", "v.", "speichert, speicherte, gespeichert", "存盘，储存数据", "Vergessen Sie nicht, Ihre Änderungen zu speichern!", "切勿忘记保存您的修改！"),
            ("kopieren", "", "v.", "kopiert, kopierte, kopiert", "复印；拷贝", "Kopieren Sie diesen Vertrag bitte zweimal!", "请把这份合同复印两份！"),
            ("der Kopierer", "der", "n.", "-", "复印机", "Der Kopierer meldet einen Papierstau.", "复印机提示发生卡纸。"),
            ("der Scanner", "der", "n.", "-", "扫描仪", "Scannen Sie das Dokument ein!", "请将该文件扫描入电脑！"),
            ("die Tastatur", "die", "n.", "-en", "电脑键盘", "Die Tastatur hat ein deutsches Layout.", "这个键盘是德语按键布局。"),
            ("der Bildschirm", "der", "n.", "-e", "显示器，屏幕", "Der Bildschirm ist augenschonend entspiegelt.", "这块显示屏做了防眩光护眼处理。"),
            ("die Maus", "die", "n.", "Mäuse", "鼠标", "Klicken Sie mit der Maus auf den Button!", "请用鼠标点击该按钮！"),
            ("das Passwort", "das", "n.", "Passwörter", "访问密码", "Ändern Sie Ihr Passwort alle drei Monate!", "请每三个月更换一次密码！"),
            ("der Benutzername", "der", "n.", "-n", "用户名，登录账号", "Geben Sie Ihren Benutzernamen ein!", "请键入您的登录用户名！"),
            ("das Netzwerk", "das", "n.", "-e", "网络，局域网", "Die Verbindung zum Firmennetzwerk steht.", "与企业局域网的连接已建立。"),
            ("die Verbindung", "die", "n.", "-en", "网络连接；联络", "Die Internetverbindung ist extrem schnell.", "互联网连接速度极快。"),
            ("das Internet", "das", "n.", "-", "互联网", "Im Internet recherchiert er Marktanalysen.", "他在互联网上检索市场行业分析。"),
            ("herunterladen", "", "v.", "lädt herunter, lud herunter, heruntergeladen", "下载", "Laden Sie die Software bitte herunter!", "请下载安装该软件！"),
            ("hochladen", "", "v.", "lädt hoch, lud hoch, hochgeladen", "上传", "Er lädt den Tätigkeitsbericht auf das Portal hoch.", "他将工作总结上传至门户网站。"),
            ("die E-Mail", "die", "n.", "-s", "电子邮件", "Ich antworte sofort auf Ihre E-Mail.", "我马上给您的邮件写回信。"),
            ("der Anhang", "der", "n.", "Anhänge", "邮件附件", "Im Anhang finden Sie die Preisliste.", "附件中附有报价单。"),
            ("anhängen", "", "v.", "hängt an, hängte an, angehängt", "作为附件附上", "Ich habe die Tabelle an die Mail angehängt.", "我已把表格附在邮件后发送。"),
            ("weiterleiten", "", "v.", "leitet weiter, leitete weiter, weitergeleitet", "转发（邮件）", "Leiten Sie die Anfrage an Frau Klein weiter!", "请把此询价转给克莱因女士！"),
            ("beantworten", "", "v.", "beantwortet, beantwortete, beantwortet", "答复，解答", "Ich beantworte Kundenanfragen innerhalb von 24 Stunden.", "我会在24小时内答复客户咨询。"),
            ("die Anfrage", "die", "n.", "-n", "询价，业务咨询", "Wir haben eine neue Anfrage aus Österreich.", "我们收到了一封来自奥地利的新询价。"),
            ("das Angebot", "das", "n.", "-e", "报价单；供应", "Unterbreiten Sie dem Kunden ein faires Angebot!", "请给客户提供一份合理的报价单！"),
            ("der Auftrag", "der", "n.", "Aufträge", "商务订单，任务委托", "Der Großkunde hat den Auftrag erteilt.", "这位大客户已经确认下达订单。"),
            ("die Bestellung", "die", "n.", "-en", "订货单，订购", "Die Bestellung wird heute noch versandt.", "这笔订货将于今日发出交付。"),
            ("die Lieferung", "die", "n.", "-en", "交付货物，货运送达", "Die Lieferung erfolgt frei Haus.", "货物免运费直接送抵上门。"),
            ("liefern", "", "v.", "liefert, lieferte, geliefert", "供货，交付", "Können Sie die Ware bis Freitag liefern?", "你们能在周五前交付这批货物吗？"),
            ("die Rechnung", "die", "n.", "-en", "商业发票，发票", "Bitte überweisen Sie den Rechnungsbetrag!", "请汇付发票所列账款！"),
            ("der Betrag", "der", "n.", "Beträge", "金额，款项", "Der offene Betrag ist innerhalb von 14 Tagen fällig.", "未结清款项应在14天内付讫。"),
            ("die Mahnung", "die", "n.", "-en", "催款单，催告函", "Bei Zahlungsverzug senden wir eine Mahnung.", "逾期未付款我们将发出催告催款函。"),
            ("der Kunde", "der", "n.", "-n", "商业客户，买家", "Der Kunde ist König, lautet das Sprichwort.", "俗话说得好，顾客就是上帝。"),
            ("betreuen", "", "v.", "betreut, betreute, betreut", "维护，照管", "Sie betreut die skandinavischen Großkunden.", "她专职负责维护斯堪的纳维亚大客户。"),
            ("die Betreuung", "die", "n.", "-", "维护服务，售后服务", "Professionelle Betreuung schafft Vertrauen.", "专业的维护服务能建立持久信任。"),
            ("der Service", "der", "n.", "-s", "服务体系，售后服务", "Guter Service zeichnet unser Unternehmen aus.", "优质完善的服务是我们企业的金字招牌。"),
            ("die Beschwerde", "die", "n.", "-n", "客户投诉，抱怨", "Die Beschwerde wird zügig bearbeitet.", "客诉正在得到迅速跟进处置。"),
            ("beschweren", "", "v.", "beschwert, beschwerte, beschwert", "投诉，申诉 (über + Akk)", "Der Kunde beschwert sich über die Lieferverzögerung.", "客户因供货延误正在提出投诉。"),
            ("lösen", "", "v.", "löst, löste, gelöst", "解决（疑难问题）", "Wir finden gemeinsam eine pragmatische Lösung.", "我们共同商讨得出一个务实的解决办法。"),
            ("die Lösung", "die", "n.", "-en", "解决方案", "Das ist eine für beide Seiten vorteilhafte Lösung.", "这是一个对双方互惠双赢的方案。"),
            ("der Konflikt", "der", "n.", "-e", "争执，分歧", "Konflikte im Team sollte man sachlich klären.", "团队内部矛盾应客观理性沟通化解。"),
            ("verhandeln", "", "v.", "verhandelt, verhandelte, verhandelt", "商务谈判，议价", "Wir verhandeln über die Vertragsbedingungen.", "我们正在就合同具体条款进行商务谈判。"),
            ("die Verhandlung", "die", "n.", "-en", "谈判，磋商", "Die Verhandlungen dauerten bis spät in die Nacht.", "商业谈判一直持续到深夜时分。"),
            ("die Bedingung", "die", "n.", "-en", "条件，条款", "Die Bedingungen sind für uns akzeptabel.", "所开出的各项条件对我们是可接受的。"),
            ("zustimmen", "", "v.", "stimmt zu, stimmte zu, zugestimmt", "赞同，同意 (接 Dativ)", "Der Vorstand stimmte dem Vorschlag zu.", "董事会全票赞同批准了该提案。"),
            ("ablehnen", "", "v.", "lehnt ab, lehnte ab, abgelehnt", "驳回，拒绝", "Das Angebot wurde aus Kostengründen abgelehnt.", "该报价出于成本控制考量被予以婉拒。"),
            ("der Vorschlag", "der", "n.", "Vorschläge", "建设性提议，提议", "Ich habe einen konstruktiven Vorschlag dazu.", "对此我有一个建设性的有益提议。"),
            ("vorschlagen", "", "v.", "schlägt vor, schlug vor, vorgeschlagen", "建议，提议", "Was schlagen Sie als nächsten Schritt vor?", "关于下一步骤推进，您有何建议？")
        ]
    },

    # LESSON 4
    {
        "id": "A2_L04",
        "title": "第4课：房屋租赁、邻里关系与搬家乔迁 (Wohnen & Umzug)",
        "summary": "掌握静止Dativ与运动Akkusativ的九大双向介词(Wechselpräpositionen)、看房与租赁合同",
        "grammar": {
            "title": "静三动四双向介词 (Wechselpräpositionen)",
            "sections": [
                {
                    "heading": "1. 九大双向介词 (an, auf, hinter, in, neben, über, unter, vor, zwischen)",
                    "content": "• 静止状态（问 Wo?）：支配第三格 Dativ！\n  Das Bild hängt an der Wand. (墙上，第三格)\n• 定向动作（问 Wohin?）：支配第四格 Akkusativ！\n  Ich hänge das Bild an die Wand. (挂到墙上，第四格)"
                },
                {
                    "heading": "2. 容易混淆的四对动词",
                    "content": "• stellen (放置，及物动作 -> Akk) vs stehen (站立，状态 -> Dat)\n• legen (平放，及物动作 -> Akk) vs liegen (平躺，状态 -> Dat)\n• setzen (让坐下，动作 -> Akk) vs sitzen (坐着，状态 -> Dat)\n• hängen (悬挂动作 -> Akk) vs hängen (悬挂状态 -> Dat)"
                }
            ]
        },
        "quiz": [
            {
                "id": "A2_L04_Q1",
                "type": "GRAMMAR_FILL",
                "question": "Ich stelle die Vase auf ______ (der Tisch, 动作定向放去哪里).",
                "options": ["den Tisch", "dem Tisch", "der Tisch", "des Tisches"],
                "correctIndex": 0,
                "explanation": "stellen 表达把某物放置到某处（定向动作，问 Wohin?），双向介词 auf 后接第四格 den Tisch。"
            },
            {
                "id": "A2_L04_Q2",
                "type": "GRAMMAR_FILL",
                "question": "Die Vase steht jetzt auf ______ (der Tisch, 静止状态在哪里).",
                "options": ["dem Tisch", "den Tisch", "der Tisch", "des Tisches"],
                "correctIndex": 0,
                "explanation": "stehen 表达静止状态（问 Wo?），双向介词 auf 后接第三格 dem Tisch。"
            }
        ],
        "words": [
            ("der Wohnungsmarkt", "der", "n.", "Wohnungsmärkte", "租房住房市场", "Auf dem Wohnungsmarkt herrscht großer Mangel.", "住房租赁市场上房源严重紧缺。"),
            ("die Anzeige", "die", "n.", "-n", "房产广告，招租启事", "Ich habe online eine Wohnungsanzeige geschaltet.", "我在网上发布了一则招租广告。"),
            ("das Inserat", "das", "n.", "-e", "登报广告，分类广告", "Das Inserat beschreibt eine helle 2-Zimmer-Wohnung.", "广告描述了一套采光良好的两居室。"),
            ("die Besichtigung", "die", "n.", "-en", "看房，现场实地考察", "Der Makler vereinbart einen Besichtigungstermin.", "房产中介敲定了一个实地看房时间。"),
            ("besichtigen", "", "v.", "besichtigt, besichtigte, besichtigt", "实地看房；游览", "Wir besichtigen heute drei verschiedene Wohnungen.", "我们今天去实地看三套不同的房源。"),
            ("der Makler", "der", "n.", "-", "男房产中介", "Der Makler verlangt eine Provision.", "房产中介收取一笔佣金中介费。"),
            ("die Provision", "die", "n.", "-en", "中介费，佣金", "Die Wohnung ist provisionsfrei zu vermieten.", "该套公寓免中介佣金直租。"),
            ("die Lage", "die", "n.", "-n", "地理位置，地段", "Die Lage der Wohnung ist äußerst zentral.", "公寓所处的地段极为核心繁华。"),
            ("zentral", "", "adj.", "zentraler, am zentralsten", "市中心核心地段的", "Eine zentral gelegene Altbauwohnung.", "一套地处市中心核心区的老式公寓。"),
            ("ruhig", "", "adj.", "ruhiger, am ruhigsten", "安静怡人的", "Ein ruhiges Wohnviertel mit viel Grün.", "一个充满绿意且幽静宜人的居民区。"),
            ("die Kaution", "die", "n.", "-en", "租房押金", "Die Kaution wird auf ein Sperrkonto eingezahlt.", "押金被存入专用的冻结托管账户。"),
            ("die Warmmiete", "die", "n.", "-n", "含暖气物业全包租金", "Die Warmmiete beträgt monatlich 950 Euro.", "暖租每月全包合计为950欧元。"),
            ("die Kaltmiete", "die", "n.", "-n", "净冷租（不含能源杂费）", "Die Kaltmiete liegt bei 750 Euro.", "净冷租金基价为750欧元。"),
            ("die Nebenkosten", "die", "n.pl.", "-", "物业杂费，能源附加费", "In den Nebenkosten sind Wasser und Müll enthalten.", "物业杂费中包含了水费与垃圾清运费。"),
            ("der Strom", "der", "n.", "-", "电力，电", "Strom muss man separat beim Anbieter anmelden.", "用电必须单独向电力供货商开户报装。"),
            ("das Gas", "das", "n.", "-", "天然气，燃气", "Die Heizung wird mit Gas betrieben.", "暖气由天然气驱动供应。"),
            ("die Heizung", "die", "n.", "-en", "供暖，暖气设施", "Die Zentralheizung wärmt alle Räume gleichmäßig.", "集中供暖系统均匀温暖所有房间。"),
            ("der Zähler", "der", "n.", "-", "电表，水表仪表", "Der Zählerstand für Wasser wurde abgelesen.", "水表读数已完成上门抄表。"),
            ("der Mietvertrag", "der", "n.", "Mietverträge", "房屋租赁合同", "Lesen Sie den Mietvertrag vor der Unterschrift gründlich!", "签字前请仔细研读租房合同！"),
            ("die Kündigung", "die", "n.", "-en", "退租通知，解约", "Die gesetzliche Kündigungsfrist beträgt drei Monate.", "法定的退租解约预先通知期为三个月。"),
            ("kündigen", "", "v.", "kündigt, kündigte, gekündigt", "解除租赁，退租", "Er kündigte die Wohnung zum Monatsende.", "他在月底前办理了退租手续。"),
            ("der Nachmieter", "der", "n.", "-", "接盘租客，下家承租人", "Ich suche einen Nachmieter für meine Möbel.", "我正在寻找愿意接盘我家具的新租客。"),
            ("die Hausordnung", "die", "n.", "-en", "住户公约，大楼规约", "Die Hausordnung regelt die Ruhezeiten im Haus.", "住户公约严格规定了大楼静息时段。"),
            ("die Ruhezeit", "die", "n.", "-en", "静息时间，勿扰时段", "Ab 22 Uhr gilt im Haus absolute Nachtruhe.", "晚22点起全楼进入绝对夜间静息时段。"),
            ("der Nachbar", "der", "n.", "-n", "邻居，邻舍", "Unser Nachbar gießt während unseres Urlaubs die Blumen.", "邻居在我们度假期间帮我们给花浇水。"),
            ("die Nachbarin", "die", "n.", "-nen", "女邻居", "Die Nachbarin von nebenan ist sehr hilfsbereit.", "隔壁的女邻居非常乐于助人。"),
            ("die Nachbarschaft", "die", "n.", "-", "邻里关系，左邻右舍", "Eine freundliche Nachbarschaft ist Gold wert.", "和睦融洽的邻里关系胜过千金。"),
            ("der Hausmeister", "der", "n.", "-", "大楼物业管理员", "Der Hausmeister repariert das defekte Treppenlicht.", "物业管理员修理好了坏掉的楼道灯。"),
            ("das Treppenhaus", "das", "n.", "Treppenhäuser", "楼梯通道，楼道", "Das Treppenhaus muss sauber gehalten werden.", "楼梯通道必须保持干净整洁。"),
            ("die Treppe", "die", "n.", "-n", "楼梯，梯级", "Er steigt sportlich die Treppen zu Fuß hinauf.", "他像锻炼一样步行走楼梯上楼。"),
            ("das Geländer", "das", "n.", "-", "楼梯扶手，栏杆", "Halten Sie sich bitte am Treppengeländer fest!", "请抓紧楼梯扶手以防跌倒！"),
            ("der Aufzug", "der", "n.", "Aufzüge", "升降电梯", "Der moderne Aufzug fasst bis zu acht Personen.", "这部现代化的电梯最多可容纳八人。"),
            ("der Fahrstuhl", "der", "n.", "Fahrstühle", "载客电梯", "Nehmen wir den Fahrstuhl in den fünften Stock!", "我们乘电梯上五楼吧！"),
            ("der Schlüssel", "der", "n.", "-", "钥匙", "Ich habe meinen Hausschlüssel verlegt.", "我不小心把家门钥匙放错地方找不到了。"),
            ("das Schloss", "das", "n.", "Schlösser", "门锁；城堡", "Das Schloss der Eingangstür klemmt.", "入户大门的锁舌卡住了。"),
            ("abschließen", "", "v.", "schließt ab, schloss ab, abgeschlossen", "反锁，用钥匙锁门", "Schließe die Tür beim Verlassen bitte ab!", "出门离开时请务必反锁好大门！"),
            ("aufschließen", "", "v.", "schließt auf, schloss auf, aufgeschlossen", "开锁，用钥匙开门", "Er schloss vorsichtig die Wohnungstür auf.", "他小心翼翼地拿钥匙拧开了公寓房门。"),
            ("der Hof", "der", "n.", "Höfe", "内院，庭院", "Im Innenhof stehen die Mülltonnen.", "内院里摆放着分类垃圾桶。"),
            ("die Mülltonne", "die", "n.", "-n", "垃圾箱，垃圾桶", "Bitte werfen Sie Altpapier in die blaue Tonne!", "废纸类垃圾请投入蓝色专用分类桶！"),
            ("der Müll", "der", "n.", "-", "垃圾", "In Deutschland wird der Müll strikt getrennt.", "在德国垃圾分类推行得极其严格。"),
            ("trennen", "", "v.", "trennt, trennte, getrennt", "分类；分开", "Wir trennen Plastik, Glas, Papier und Bioabfall.", "我们将塑料、玻璃、废纸及厨余垃圾严格分拣。"),
            ("der Umzug", "der", "n.", "Umzüge", "搬家，迁居", "Für den Umzug mieten wir einen großen Transporter.", "为了搬家我们租用了一辆大型厢式货车。"),
            ("das Umzugsunternehmen", "das", "n.", "-", "专业搬家服务公司", "Das Umzugsunternehmen packt alle Kartons ein.", "搬家公司把所有纸箱全部专业打包封箱。"),
            ("der Umzugskarton", "der", "n.", "-s", "搬家专用纸箱", "Wir haben 25 Umzugskartons gepackt.", "我们一共打包整理好了25个搬家纸箱。"),
            ("packen", "", "v.", "packt, packte, gepackt", "打包，收拾行李", "Sie packt fleißig die letzten Kisten.", "她正在手脚麻利地打包最后的箱子。"),
            ("auspacken", "", "v.", "packt aus, packte aus, ausgepackt", "开箱拆包", "Das Auspacken der Kisten dauerte zwei Tage.", "把箱子全部开箱摆放花了两天时间。"),
            ("einziehen", "", "v.", "zieht ein, zog ein, ist eingezogen", "搬入新居，入住", "Nächsten Samstag ziehen wir in die neue Wohnung ein.", "下周六我们就要正式搬入新家入住。"),
            ("ausziehen", "", "v.", "zieht aus, zog aus, ist ausgezogen", "搬出，腾退房屋", "Die Vormieter sind gestern ausgezogen.", "原租客已于昨日彻底腾空搬出。"),
            ("der Vormieter", "der", "n.", "-", "前任租客，原房客", "Der Vormieter hinterließ die Küche in gutem Zustand.", "前房客把厨房打理得十分完好。"),
            ("die Einbauküche", "die", "n.", "-n", "一体化整体橱柜厨房", "Die Wohnung verfügt über eine moderne Einbauküche.", "公寓配备了一套现代化整体嵌入式厨房。"),
            ("die Spüle", "die", "n.", "-n", "洗涤池，水槽", "In der Spüle staut sich das Geschirr.", "水槽里堆满了待洗的餐具。"),
            ("der Wasserhahn", "der", "n.", "Wasserhähne", "水龙头", "Der Wasserhahn in der Küche tropft.", "厨房的水龙头一直在滴水。"),
            ("tropfen", "", "v.", "tropft, tropfte, getropft", "滴水，漏水", "Es tropft unaufhörlich von der Decke.", "天花板不停地往下滴水。"),
            ("reparieren", "", "v.", "repariert, reparierte, repariert", "修缮，维修", "Der Klempner repariert das Abflussrohr.", "水暖工正在维修下水管道。"),
            ("der Handwerker", "der", "n.", "-", "手工艺工人，技工", "Der Handwerker kommt morgen früh um acht.", "安装技工明早八点准时上门维修。"),
            ("die Renovierung", "die", "n.", "-en", "装修改造，翻新", "Nach der Renovierung erstrahlt alles in neuem Glanz.", "装修改造后整间屋子焕然一新。"),
            ("streichen", "", "v.", "streicht, strich, gestrichen", "粉刷，油漆", "Wir streichen die Wände im Wohnzimmer weiß.", "我们把客厅的墙壁重新粉刷成白色。"),
            ("die Farbe", "die", "n.", "-n", "油漆，涂料", "Umweltfreundliche Wandfarbe riecht kaum.", "环保型水性墙面漆几乎没有任何异味。"),
            ("der Pinsel", "der", "n.", "-", "油漆刷，画笔", "Mit einem breiten Pinsel streicht man die Kanten.", "用一把宽油漆刷来刷边角线条。"),
            ("die Rolle", "die", "n.", "-n", "涂料滚筒；角色", "Mit der Farbrolle geht das Streichen rasch voran.", "用涂料滚筒刷墙效率极为飞速。"),
            ("der Boden", "der", "n.", "Böden", "地板，地面", "Ein hochwertiger Boden aus Eichenparkett.", "高档典雅的橡木实木复合地板。"),
            ("das Parkett", "das", "n.", "-", "实木拼花地板", "Das Parkett wurde frisch abgeschliffen und versiegelt.", "实木地板刚刚重新抛光打磨并封漆。"),
            ("die Fliese", "die", "n.", "-n", "地砖，瓷砖", "Im Bad sind weiße Fliesen an den Wänden.", "浴室墙面上铺贴着洁白素雅的瓷砖。"),
            ("stellen", "", "v.", "stellt, stellte, gestellt", "竖立摆放 (动作 -> Akk)", "Stell die Stehlampe bitte neben das Sofa!", "请把落地灯摆在沙发旁边！"),
            ("stehen", "", "v.", "steht, stand, gestanden", "立着 (状态 -> Dat)", "Die Stehlampe steht neben dem gemütlichen Sofa.", "落地灯静静立在舒适的沙发旁。"),
            ("legen", "", "v.", "legt, legte, gelegt", "平放，放倒 (动作 -> Akk)", "Lege die Fernbedienung auf den Couchtisch!", "把遥控器平放在茶几上！"),
            ("liegen", "", "v.", "liegt, lag, gelegen", "平躺横卧 (状态 -> Dat)", "Die Fernbedienung liegt auf dem Couchtisch.", "遥控器正平放在茶几上。"),
            ("hängen", "", "v.", "hängt, hängte, gehängt", "悬挂到 (动作 -> Akk)", "Ich hänge das Gemälde über das Sofa.", "我把这幅油画挂在沙发正上方。"),
            ("hängen", "", "v.", "hängt, hing, gehangen", "挂在 (状态 -> Dat)", "Das Gemälde hängt über dem Sofa an der Wand.", "油画正悬挂在沙发上方的墙壁上。"),
            ("gemütlich", "", "adj.", "gemütlicher, am gemütlichsten", "安乐温馨的", "Jetzt richten wir uns unser neues Zuhause gemütlich ein.", "现在我们把新家布置得温馨而舒适。")
        ]
    },

    # LESSON 5
    {
        "id": "A2_L05",
        "title": "第5课：商品消费、网购与售后维权 (Einkaufen & Reklamation)",
        "summary": "掌握比较级与最高级规则、形容词词尾弱变化、网购下单与退换货维权",
        "grammar": {
            "title": "形容词比较级、最高级与退货维权句型",
            "sections": [
                {
                    "heading": "1. 形容词比较级 (-er als) 与最高级 (am -sten)",
                    "content": "• billig -> billiger -> am billigsten\n• 特殊变音：groß -> größer -> am größten / alt -> älter -> am ältesten\n• 不规则：gut -> besser -> am besten / viel -> mehr -> am meisten / gern -> lieber -> am liebsten / teuer -> teurer"
                },
                {
                    "heading": "2. 消费维权与退换货常用句型",
                    "content": "• Das Gerät funktioniert nicht / ist kaputt / ist beschädigt.\n• Ich möchte die Ware umtauschen oder mein Geld zurückbekommen.\n• Haben Sie noch den Kassenbon / den Kaufbeleg?"
                }
            ]
        },
        "quiz": [
            {
                "id": "A2_L05_Q1",
                "type": "GRAMMAR_FILL",
                "question": "Dieses Smartphone ist zwar teurer, aber die Kamera ist viel ______ (gut) als bei jenem.",
                "options": ["besser", "guter", "am besten", "beste"],
                "correctIndex": 0,
                "explanation": "gut 的比较级是不规则形式 besser (besser als)。"
            },
            {
                "id": "A2_L05_Q2",
                "type": "EXAM_REAL",
                "question": "购买的商品发现存在严重瑕疵想要退换，去服务台最地道的表达是：",
                "options": ["Ich möchte diese Ware reklamieren / umtauschen.", "Geben Sie mir sofort Essen!", "Ich will nicht mehr kaufen.", "Das ist ein schönes Geschenk."],
                "correctIndex": 0,
                "explanation": "die Ware reklamieren / umtauschen 是德语区标准的商品售后投诉与换货表达。"
            }
        ],
        "words": [
            ("der Konsum", "der", "n.", "-", "商品消费", "Nachhaltiger Konsum schont die Ressourcen.", "理性可持续的消费能珍惜自然资源。"),
            ("der Kunde", "der", "n.", "-n", "消费者，顾客", "Der Kunde hat das Recht auf Nachbesserung.", "消费者依法享有要求维修补正的权利。"),
            ("die Kundin", "die", "n.", "-nen", "女顾客", "Die Kundin wünscht eine ausführliche Beratung.", "女顾客希望得到详尽细致的选购咨询。"),
            ("der Verbraucher", "der", "n.", "-", "消费者", "Der Verbraucherschutz stärkt die Rechte der Käufer.", "消费者权益保护组织切实保障买家权益。"),
            ("der Verbraucherschutz", "der", "n.", "-", "消费者权益保护", "Die Zentrale für Verbraucherschutz informiert Bürger.", "消协中心为广大市民提供专业维权信息。"),
            ("das Geschäft", "das", "n.", "-e", "商铺；商业交易", "Das Geschäft schließt heute ausnahmsweise früher.", "该商铺今日破例提前闭店。"),
            ("der Laden", "der", "n.", "Läden", "小店铺，零售店", "An der Ecke gibt es einen charmanten Blumenladen.", "转角处开着一家极富魅力的鲜花店。"),
            ("das Fachgeschäft", "das", "n.", "-e", "专业专营店", "Im Fachgeschäft für Elektronik gibt es kompetente Beratung.", "在电子产品专卖店能得到专业内行的指导。"),
            ("die Filiale", "die", "n.", "-n", "连锁分店", "Die Modekette eröffnet eine neue Filiale in Köln.", "该时尚服装连锁在科隆开设了一家新分店。"),
            ("die Kette", "die", "n.", "-n", "连锁店；项链", "Eine bekannte Kette von Drogeriemärkten.", "一家家喻户晓的日化用品连锁巨头。"),
            ("der Drogeriemarkt", "der", "n.", "Drogeriemärkte", "日用日化超市", "Im Drogeriemarkt kauft man Seife und Zahnpasta.", "在日化超市能买到香皂、洗发水与牙膏。"),
            ("die Bäckerei", "die", "n.", "-en", "面包糕点房", "Der herrliche Duft von frischem Brot aus der Bäckerei.", "面包房飘散出新鲜出炉面包的诱人香气。"),
            ("die Metzgerei", "die", "n.", "-en", "肉铺，肉食精肉店", "Beim Metzger kaufe ich regionalen Schinken.", "在肉铺我买本地产的高品质火腿。"),
            ("die Fleischerei", "die", "n.", "-en", "肉铺（北德称谓）", "Frisches Rindfleisch direkt aus der Fleischerei.", "直接从精肉铺采购的新鲜牛肉。"),
            ("der Wochenmarkt", "der", "n.", "Wochenmärkte", "每周露天集市", "Auf dem Wochenmarkt bieten Bauern Erzeugnisse an.", "在周集市上农户们直销自家农产。"),
            ("der Stand", "der", "n.", "Stände", "货摊，展位", "Am Käsestand probieren wir verschiedene Sorten.", "在奶酪摊位前我们品尝了多种风味。"),
            ("der Online-Handel", "der", "n.", "-", "网络电商零售", "Der Online-Handel verzeichnet enorme Zuwächse.", "线上网络电商零售呈现出迅猛的增长势头。"),
            ("bestellen", "", "v.", "bestellt, bestellte, bestellt", "在线订购，下单", "Ich habe das Buch im Internet bestellt.", "我在互联网上订购了这本书。"),
            ("die Bestellung", "die", "n.", "-en", "网上订单", "Ihre Bestellung wurde erfolgreich abgeschickt.", "您的订单已成功提交生成。"),
            ("der Warenkorb", "der", "n.", "Warenkörbe", "虚拟购物车", "Legen Sie die gewünschten Artikel in den Warenkorb!", "请将您心仪选定的商品放入购物车！"),
            ("der Artikel", "der", "n.", "-", "商品单品；冠词", "Dieser Artikel ist zurzeit leider vergriffen.", "该款商品遗憾目前已暂时断货售罄。"),
            ("das Produkt", "das", "n.", "-e", "产品，制成品", "Ein hochwertiges Produkt mit langer Garantie.", "一件享有超长质保的高品质产品。"),
            ("die Ware", "die", "n.", "-n", "商品，货物（总称）", "Die bestellte Ware kommt per Paketpost.", "订购的货物正通过包裹快递运送而来。"),
            ("die Qualität", "die", "n.", "-en", "品质，做工质地", "Bei Schuhen achte ich auf erstklassige Qualität.", "挑鞋子时我格外看重是否具有上乘品质。"),
            ("hochwertig", "", "adj.", "hochwertiger, am hochwertigsten", "高端的，品质精良的", "Hochwertige Materialien garantieren Langlebigkeit.", "高档考究的材质能够确保长久经久耐用。"),
            ("günstig", "", "adj.", "günstiger, am günstigsten", "合算的，物美价廉的", "Hier gibt es Markenware zu günstigen Preisen.", "这里能以实惠的价格买到大牌正品。"),
            ("das Sonderangebot", "das", "n.", "-e", "特价特惠商品", "Achten Sie auf die aktuellen Sonderangebote!", "请密切留意商场当期推出的特价活动！"),
            ("der Rabatt", "der", "n.", "-e", "打折优惠，折扣", "Heute erhalten Sie 20 Prozent Rabatt auf alles.", "今天进店尊享全场全品类八折大优惠。"),
            ("der Gutschein", "der", "n.", "-e", "购物代金券，礼券", "Zum Geburtstag schenkte sie mir einen Buchgutschein.", "生日那天她赠予了我一张书店购书券。"),
            ("die Ermäßigung", "die", "n.", "-en", "优惠减免，减价", "Studenten bekommen gegen Vorlage des Ausweises Ermäßigung.", "大专院校学生凭学生证可享受优惠减免。"),
            ("der Kassenbon", "der", "n.", "-s", "收银条，购物小票", "Bewahren Sie den Kassenbon für einen Umtausch auf!", "请妥善保管好收银小票以备需要退换货！"),
            ("der Kassenzettel", "der", "n.", "-", "收银纸条", "Ohne Kassenzettel ist eine Rückgabe schwierig.", "若没有购物收据小票办理退货会比较棘手。"),
            ("die Quittung", "die", "n.", "-en", "发票收条", "Verlangen Sie beim Kauf stets eine Quittung!", "购买大宗商品时务必索取有效盖章发票！"),
            ("die Garantie", "die", "n.", "-n", "质保承诺，保修", "Auf das Elektrogerät gibt der Hersteller zwei Jahre Garantie.", "厂家对该电器提供长达两年的免费保修。"),
            ("die Gewährleistung", "die", "n.", "-en", "法定瑕疵担保责任", "Die gesetzliche Gewährleistung schützt den Käufer.", "法定的商品瑕疵担保制度切实庇护买方。"),
            ("defekt", "", "adj.", "", "损坏有故障的", "Das neu gelieferte Radio ist leider defekt.", "全新派送上门的收音机遗憾存在机械故障。"),
            ("beschädigt", "", "adj.", "", "受损破损的", "Das Paket kam mit beschädigter Verpackung an.", "包裹送抵时外包装箱已发生严重破损。"),
            ("kaputt", "", "adj.", "", "坏掉报废的", "Der Bildschirm ist heruntergefallen und kaputt.", "显示屏摔在地上整个彻底碎掉报废了。"),
            ("funktionieren", "", "v.", "funktioniert, funktionierte, funktioniert", "运转，正常起效", "Der Akku funktioniert nach dem Laden einwandfrei.", "充满电后该电池运转一切完全正常。"),
            ("fehlen", "", "v.", "fehlt, fehlte, gefehlt", "缺少零部件", "In der Packung fehlte die Bedienungsanleitung.", "包装盒内部竟然缺少了核心使用说明书。"),
            ("die Reklamation", "die", "n.", "-en", "投诉退赔，售后维权", "Die Reklamation wurde am Schalter kulant geregelt.", "售后专柜极其开明宽容地处理了这笔投诉。"),
            ("reklamieren", "", "v.", "reklamiert, reklamierte, reklamiert", "提出售后退赔维权", "Ich muss diesen mangelhaften Pullover reklamieren.", "我必须对这件有抽丝瑕疵的毛衣提出换退。"),
            ("der Umtausch", "der", "n.", "-", "调换货", "Der Umtausch ist innerhalb von 14 Tagen möglich.", "购买后十四天期限内均可行使调换货权利。"),
            ("umtauschen", "", "v.", "tauscht um, tauschte um, umgetauscht", "换货，调换款式尺寸", "Kann ich das Hemd gegen eine andere Größe umtauschen?", "我能把这件衬衫换成另一个大一号尺码吗？"),
            ("die Rückgabe", "die", "n.", "-n", "退货退款", "Für die Rückgabe fallen keine Versandkosten an.", "行使退货退还权利无需买方承担任何运费。"),
            ("zurückgeben", "", "v.", "gibt zurück, gab zurück, zurückgegeben", "退还，归还", "Ich möchte das defekte Gerät zurückgeben.", "我希望能将这台故障设备彻底退回退款。"),
            ("zurückschicken", "", "v.", "schickt zurück, schickte zurück, zurückgeschickt", "邮寄退回", "Er schickt die unpassende Hose per Post zurück.", "他将不合身的外裤通过邮政快递寄送退回。"),
            ("das Rücksendeetikett", "das", "n.", "-s", "退货专递面单", "Kleben Sie das Rücksendeetikett auf das Paket!", "请将退货专用快递面单牢固张贴在包裹上！"),
            ("erstatten", "", "v.", "erstattet, erstattete, erstattet", "全额退款，返还", "Der Kaufpreis wird auf Ihr Konto erstattet.", "全部购买货款将于数日内原路返还至账户。"),
            ("die Erstattung", "die", "n.", "-en", "退款返还", "Die Erstattung erfolgt innerhalb von drei Werktagen.", "全额退款将于三个银行工作日内执行到位。"),
            ("der Ersatz", "der", "n.", "-", "替代良品，赔偿物", "Der Händler lieferte prompt einen kostenlosen Ersatz.", "商家极其麻利地补发了一份全新的替代良品。"),
            ("ersetzen", "", "v.", "ersetzt, ersetzte, ersetzt", "替换，包赔", "Wir ersetzen Ihnen den entstandenen Schaden.", "我们将为您承担赔付由此产生的全部损失。"),
            ("die Reparatur", "die", "n.", "-en", "检修，售后修理", "Die Reparatur wird im Rahmen der Garantie durchgeführt.", "本次检测维修将完全在质保承诺框架内免费实施。"),
            ("der Kundenservice", "der", "n.", "-s", "客户支持客服团队", "Der Kundenservice ist rund um die Uhr erreichbar.", "客服售后支持团队提供全天候全时段守候。"),
            ("die Hotline", "die", "n.", "-s", "服务咨询热线", "Wählen Sie die gebührenfreie Service-Hotline!", "请直接拨打我们免收话费的全国服务热线！"),
            ("das Paket", "das", "n.", "-e", "快件邮包，包裹", "Der Paketbote hat das Paket beim Nachbarn abgegeben.", "快递小哥已将包裹暂存在了热心邻居家中。"),
            ("der Bote", "der", "n.", "-n", "快递员，派送员", "Der freundliche Bote klingelte pünktlich an der Tür.", "和蔼的快递员准时在门外按响了门铃送件。"),
            ("die Lieferung", "die", "n.", "-en", "物流派送", "Die Lieferung dauerte lediglich zwei Werktage.", "物流快递从揽收到派送仅仅耗费两天时间。"),
            ("die Versandkosten", "die", "n.pl.", "-", "物流配送运费", "Ab 50 Euro Bestellwert entfallen die Versandkosten.", "订单消费金额满50欧元即可尊享包邮免运费。"),
            ("die Zahlung", "die", "n.", "-en", "付款支付行为", "Wählen Sie eine sichere Methode für die Zahlung!", "请选定一种安全稳妥的官方线上支付途径！"),
            ("die Zahlungsart", "die", "n.", "-en", "结算支付方式", "Beliebte Zahlungsarten sind PayPal und Kreditkarte.", "深受大众青睐的支付方式有贝宝与各大信用卡。"),
            ("auf Rechnung", "", "phrase", "", "货到凭发票后付款", "Viele Kunden bestellen am liebsten auf Rechnung.", "许多顾客最推崇先验货、后凭发票转账付款。"),
            ("die Ratenzahlung", "die", "n.", "-en", "分期偿付，分期付款", "Große Anschaffungen kann man per Ratenzahlung finanzieren.", "购置昂贵大件耐用品可以借助分期付款理财。"),
            ("das Bargeld", "das", "n.", "-", "纸币硬币现款，现金", "Immer mehr Geschäfte verzichten auf Bargeld.", "越来越多前沿商铺正转型尝试不收纸币现金。"),
            ("die Kreditkarte", "die", "n.", "-n", "贷记信用卡", "Zahlungen mit Kreditkarte sind weltweit anerkannt.", "刷信用卡进行结算在全球任何地方均受通行认可。"),
            ("kontaktlos", "", "adj./adv.", "", "非接触式刷碰（NFC）", "Sie können an der Kasse kontaktlos mit dem Handy zahlen.", "您可在收款机前直接使用手机进行碰一碰非接触支付。"),
            ("die Bewertung", "die", "n.", "-en", "用户买家打分评价", "Lesen Sie vor dem Kauf die Kundenbewertungen durch!", "下单付款前务必研读其他真实买家的使用评价！"),
            ("bewerten", "", "v.", "bewertet, bewertete, bewertet", "打分，给予评价", "Ich bewerte den Kauf mit fünf von fünf Sternen.", "我给本次购物体验打出了满分五颗星好评。"),
            ("der Stern", "der", "n.", "-e", "评分星级，星", "Das Hotel hat hervorragende 4,8 Sterne erhalten.", "该酒店获得了高达4.8星的极佳综合评价。"),
            ("empfehlen", "", "v.", "empfiehlt, empfahl, empfohlen", "力荐，推荐", "Ich kann dieses Produkt uneingeschränkt weiterempfehlen.", "我毫无保留地向所有身边朋友力荐该款好物。")
        ]
    }
]
