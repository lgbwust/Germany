#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A1 Part 2: Lessons 6 to 10 (350 words)
L06: 时间钟点、作息与日程 (Zeit, Alltag & Termine) - 70 words
L07: 职业身份与办公文具 (Berufe & Arbeitsplatz) - 70 words
L08: 身体部位与基础医疗就医 (Körperteile & Gesundheit) - 70 words
L09: 城市设施与交通出行 (Stadt & Verkehrsmittel) - 70 words
L10: 服饰穿搭、色彩与商场购物 (Kleidung, Farben & Einkaufen) - 70 words
"""

LESSONS_PART2 = [
    # LESSON 6
    {
        "id": "A1_L06",
        "title": "第6课：时间钟点、作息与日程 (Zeit, Alltag & Termine)",
        "summary": "掌握官方与日常时钟表达法、时间介词(um, am, im)、可分动词 (trennbare Verben)",
        "grammar": {
            "title": "可分动词与时间介词用法",
            "sections": [
                {
                    "heading": "1. 可分动词前缀移至句末原则",
                    "content": "• aufstehen: Ich stehe jeden Morgen um 7 Uhr auf.\n• einkaufen: Er kauft am Nachmittag im Supermarkt ein.\n• fernsehen: Wir sehen abends zusammen fern.\n• anrufen: Ich rufe dich heute Abend an."
                },
                {
                    "heading": "2. 三大核心时间介词归纳",
                    "content": "• um + 具体时刻：um 8 Uhr, um halb neun\n• am + 星期/日期/特定时段：am Montag, am Morgen, am Wochenende\n• im + 月份/季节/年份：im Juli, im Sommer, im Jahr 2026"
                }
            ]
        },
        "quiz": [
            {
                "id": "A1_L06_Q1",
                "type": "GRAMMAR_FILL",
                "question": "Der Film beginnt ______ 20 Uhr und läuft ______ Freitag.",
                "options": ["um / am", "am / um", "im / am", "um / im"],
                "correctIndex": 0,
                "explanation": "钟点时刻用介词 um，星期几用介词 am。"
            },
            {
                "id": "A1_L06_Q2",
                "type": "VOCAB_MEANING",
                "question": "日常口语中 'halb acht'（半八点）代表的时间是：",
                "options": ["7:30 (七点半)", "8:30 (八点半)", "8:00 (八点整)", "7:15 (七点一刻)"],
                "correctIndex": 0,
                "explanation": "德语 halb acht 是指距离八点还差半小时，即 7:30。"
            }
        ],
        "words": [
            ("die Zeit", "die", "n.", "-en", "时间", "Hast du am Wochenende Zeit?", "你周末有时间吗？"),
            ("die Uhr", "die", "n.", "-en", "钟表；...点钟", "Es ist jetzt genau acht Uhr.", "现在正好八点整。"),
            ("die Stunde", "die", "n.", "-n", "小时，课时", "Der Kurs dauert zwei Stunden.", "这门课程持续两小时。"),
            ("die Minute", "die", "n.", "-n", "分钟", "Der Bus kommt in fünf Minuten.", "公共汽车五分钟后到。"),
            ("die Sekunde", "die", "n.", "-n", "秒", "Warten Sie bitte eine Sekunde!", "请稍等一秒钟！"),
            ("der Tag", "der", "n.", "-e", "天，白昼", "Ich wünsche dir einen schönen Tag!", "祝你拥有美好的一天！"),
            ("die Woche", "die", "n.", "-n", "周，星期", "Eine Woche hat sieben Tage.", "一周有七天。"),
            ("das Wochenende", "das", "n.", "-n", "周末", "Schönes Wochenende allerseits!", "祝大家周末愉快！"),
            ("der Monat", "der", "n.", "-e", "月，月份", "Er bleibt für einen Monat in Berlin.", "他在柏林待一个月。"),
            ("das Jahr", "das", "n.", "-e", "年，年份", "Ich lerne seit einem Jahr Deutsch.", "我学德语一年了。"),
            ("der Morgen", "der", "n.", "-", "早晨，上午", "Am Morgen trinke ich Kaffee.", "早晨我喝咖啡。"),
            ("der Vormittag", "der", "n.", "-e", "上午", "Am Vormittag habe ich Unterricht.", "上午我有课。"),
            ("der Mittag", "der", "n.", "-e", "正午，中午", "Wir machen um 12 Uhr Mittag.", "我们中午12点吃午饭。"),
            ("der Nachmittag", "der", "n.", "-e", "下午", "Am Nachmittag gehe ich einkaufen.", "下午我去购物。"),
            ("der Abend", "der", "n.", "-e", "傍晚，晚上", "Am Abend koche ich für Freunde.", "晚上我给朋友们做饭。"),
            ("die Nacht", "die", "n.", "Nächte", "夜晚，深夜", "In der Nacht ist es sehr still.", "夜里非常安静。"),
            ("der Montag", "der", "n.", "-e", "星期一", "Am Montag beginnt die neue Arbeitswoche.", "周一新工作周开始。"),
            ("der Dienstag", "der", "n.", "-e", "星期二", "Dienstags habe ich Deutschkurs.", "周二我有德语课。"),
            ("der Mittwoch", "der", "n.", "-e", "星期三", "Mittwoch ist die Mitte der Woche.", "周三是一周的中间。"),
            ("der Donnerstag", "der", "n.", "-e", "星期四", "Am Donnerstag gehe ich schwimmen.", "周四我去游泳。"),
            ("der Freitag", "der", "n.", "-e", "星期五", "Am Freitagabend treffen wir uns.", "周五晚上我们聚会。"),
            ("der Samstag", "der", "n.", "-e", "星期六", "Samstags schlafe ich gerne lange.", "周六我喜欢睡懒觉。"),
            ("der Sonntag", "der", "n.", "-e", "星期日", "Am Sonntag haben die Geschäfte zu.", "周日商店都关门歇业。"),
            ("heute", "", "adv.", "", "今天", "Heute ist ein sonniger Tag.", "今天是个大晴天。"),
            ("gestern", "", "adv.", "", "昨天", "Gestern hat es den ganzen Tag geregnet.", "昨天下一整天的雨。"),
            ("morgen", "", "adv.", "", "明天", "Morgen fahre ich nach Hamburg.", "明天我乘车去汉堡。"),
            ("jetzt", "", "adv.", "", "现在", "Jetzt müssen wir uns beeilen.", "现在我们得抓紧了。"),
            ("später", "", "adv.", "", "稍后，以后", "Ich rufe dich später noch an.", "我待会儿再给你打电话。"),
            ("immer", "", "adv.", "", "总是，一直", "Er steht immer um sechs Uhr auf.", "他总是六点起床。"),
            ("oft", "", "adv.", "", "经常，常常", "Wir gehen oft ins Kino.", "我们经常去看电影。"),
            ("manchmal", "", "adv.", "", "有时，偶尔", "Manchmal koche ich chinesisch.", "有时我做中国菜。"),
            ("selten", "", "adv.", "", "很少，罕见", "Ich esse sehr selten Fleisch.", "我极少吃肉。"),
            ("nie", "", "adv.", "", "从不，绝不", "Er kommt nie zu spät zum Unterricht.", "他上课从不迟到。"),
            ("früh", "", "adj./adv.", "früher, am frühesten", "早的，及早", "Ich muss morgen früh aufstehen.", "我明天必须早起。"),
            ("spät", "", "adj./adv.", "später, am spätesten", "晚的，迟", "Es ist schon sehr spät.", "时间已经很晚了。"),
            ("pünktlich", "", "adj./adv.", "pünktlicher, am pünktlichsten", "准时的，守时的", "Züge in Japan sind sehr pünktlich.", "日本的火车非常准时。"),
            ("aufstehen", "", "v.", "steht auf, stand auf, ist aufgestanden", "起床", "Wann stehst du morgens auf?", "你早晨几点起床？"),
            ("aufwachen", "", "v.", "wacht auf, wachte auf, ist aufgewacht", "醒来", "Ich wache meistens ohne Wecker auf.", "我通常不用闹钟就醒了。"),
            ("der Wecker", "der", "n.", "-", "闹钟", "Mein Wecker klingelt um sechs.", "我的闹钟六点响起。"),
            ("klingeln", "", "v.", "klingelt, klingelte, geklingelt", "鸣响，按门铃", "Das Telefon klingelt schon wieder.", "电话又响了。"),
            ("duschen", "", "v.", "duscht, duschte, geduscht", "冲凉，冲淋浴", "Ich dusche morgens nach dem Aufstehen.", "我早上起床后冲凉。"),
            ("waschen", "", "v.", "wäscht, wusch, gewaschen", "洗，清洗", "Vergiss nicht, die Hände zu waschen!", "别忘了洗手！"),
            ("anziehen", "", "v.", "zieht an, zog an, angezogen", "穿上（衣物）", "Zieh dir eine warme Jacke an!", "穿上一件暖和的外套！"),
            ("ausziehen", "", "v.", "zieht aus, zog aus, ausgezogen", "脱下（衣物）", "Zieh bitte die Schuhe aus!", "请脱掉鞋子！"),
            ("einkaufen", "", "v.", "kauft ein, kaufte ein, eingekauft", "购物，采买", "Samstags kaufe ich im Supermarkt ein.", "周六我在超市采购。"),
            ("fernsehen", "", "v.", "sieht fern, sah fern, ferngesehen", "看电视", "Wir sehen am Abend Nachrichten fern.", "我们在晚上收看电视新闻。"),
            ("anrufen", "", "v.", "ruft an, rief an, angerufen", "打电话给", "Ruf mich bitte morgen an!", "请明天给我打电话！"),
            ("anfangen", "", "v.", "fängt an, fing an, angefangen", "开始", "Der Unterricht fängt um 9 Uhr an.", "课程在9点开始。"),
            ("beginnen", "", "v.", "beginnt, begann, begonnen", "开始", "Die Konferenz beginnt pünktlich.", "会议准时开始。"),
            ("aufhören", "", "v.", "hört auf, hörte auf, aufgehört", "停止，结束", "Hör bitte auf mit dem Lärm!", "请停止吵闹！"),
            ("enden", "", "v.", "endet, endete, geendet", "完结，结束", "Das Konzert endet um 22 Uhr.", "音乐会在22点结束。"),
            ("der Termin", "der", "n.", "-e", "预约，日程安排", "Ich habe einen Termin beim Zahnarzt.", "我约了牙医的就诊时间。"),
            ("vereinbaren", "", "v.", "vereinbart, vereinbarte, vereinbart", "约定，商定", "Können wir einen Termin vereinbaren?", "我们能约个时间吗？"),
            ("verschieben", "", "v.", "verschiebt, verschob, verschoben", "改期，推迟", "Können wir das Treffen verschieben?", "我们能把会面推迟吗？"),
            ("absagen", "", "v.", "sagt ab, sagte ab, abgesagt", "取消（约会）", "Ich muss den Termin leider absagen.", "我很遗憾必须取消这次预约。"),
            ("passen", "", "v.", "passt, passte, gepasst", "合适，适宜", "Passt es Ihnen am Mittwoch um 10?", "周三上午10点对您合适吗？"),
            ("treffen", "", "v.", "trifft, traf, getroffen", "遇见，会面", "Wir treffen uns am Bahnhof.", "我们在火车站碰头。"),
            ("das Treffen", "das", "n.", "-", "会面，聚会", "Das Treffen war sehr erfolgreich.", "这次会面非常成功。"),
            ("warten", "", "v.", "wartet, wartete, gewartet", "等待", "Ich warte an der Haltestelle auf dich.", "我在车站等你。"),
            ("die Verspätung", "die", "n.", "-en", "晚点，延误", "Der Zug hat zehn Minuten Verspätung.", "火车晚点了十分钟。"),
            ("der Kalender", "der", "n.", "-", "日历，日程本", "Ich trage den Termin in den Kalender ein.", "我把日程记在日历本上。"),
            ("das Datum", "das", "n.", "Daten", "日期", "Welches Datum haben wir heute?", "今天几号？"),
            ("der Januar", "der", "n.", "-", "一月", "Im Januar schneit es oft in den Bergen.", "一月份山里经常下雪。"),
            ("der Februar", "der", "n.", "-", "二月", "Der Februar ist der kürzeste Monat.", "二月是一年中最短的月份。"),
            ("der März", "der", "n.", "-", "三月", "Im März beginnt der Frühling.", "三月春天开始降临。"),
            ("der April", "der", "n.", "-", "四月", "Der April macht, was er will.", "四月天气变化无常。"),
            ("der Mai", "der", "n.", "-", "五月", "Der erste Mai ist ein Feiertag.", "五月一日是法定假日。"),
            ("der Juni", "der", "n.", "-", "六月", "Im Juni fangen die Sommerferien an.", "六月暑假开始了。"),
            ("der Juli", "der", "n.", "-", "七月", "Im Juli ist es oft sehr heiß.", "七月份天气通常很热。"),
            ("der August", "der", "n.", "-", "八月", "Im August fliegen viele in den Urlaub.", "八月许多人乘飞机去度假。")
        ]
    },

    # LESSON 7
    {
        "id": "A1_L07",
        "title": "第7课：职业身份与办公文具 (Berufe & Arbeitsplatz)",
        "summary": "掌握男女职业双形变化规则(-in)、办公文具、日常工作活动与能力表达",
        "grammar": {
            "title": "职业词汇女性后缀 -in 与情态动词 können",
            "sections": [
                {
                    "heading": "1. 职业名称阴性后缀 -in 规则",
                    "content": "• 阳性职业加 -in 变为阴性职业，复数加 -nen：\n  der Lehrer -> die Lehrerin (Pl. Lehrerinnen)\n  der Student -> die Studentin (Pl. Studentinnen)\n  der Arzt -> die Ärztin (变音 Ä, Pl. Ärztinnen)\n• 询问职业：Was sind Sie von Beruf? / Was machen Sie beruflich?"
                },
                {
                    "heading": "2. 情态动词 können 表达能力与许可",
                    "content": "ich kann, du kannst, er/sie/es kann, wir können, ihr könnt, sie/Sie können。\n例：Er kann fließend Deutsch und Englisch sprechen."
                }
            ]
        },
        "quiz": [
            {
                "id": "A1_L07_Q1",
                "type": "ARTICLE",
                "question": "女性职业名词 'Lehrerin'（女教师）的冠词是：",
                "options": ["der", "die", "das", "den"],
                "correctIndex": 1,
                "explanation": "德语中所有以 -in 结尾的女性职业名词均为阴性，定冠词是 die。"
            },
            {
                "id": "A1_L07_Q2",
                "type": "EXAM_REAL",
                "question": "歌德A1职场初次交谈询问职业，最标准的问句是：",
                "options": ["Was sind Sie von Beruf?", "Wo ist Ihr Geld?", "Wie alt ist Ihr Chef?", "Haben Sie ein Auto?"],
                "correctIndex": 0,
                "explanation": "Was sind Sie von Beruf?（您的职业是什么？）是询问职业的标准口语表达。"
            }
        ],
        "words": [
            ("der Beruf", "der", "n.", "-e", "职业", "Was sind Sie von Beruf?", "您的职业是什么？"),
            ("beruflich", "", "adj./adv.", "", "职业上的，工作方面的", "Was machen Sie beruflich?", "您从事什么职业？"),
            ("arbeiten", "", "v.", "arbeitet, arbeitete, gearbeitet", "工作，劳动", "Ich arbeite als Ingenieur bei Siemens.", "我在西门子公司当工程师。"),
            ("die Arbeit", "die", "n.", "-en", "工作，活儿", "Ich habe heute viel Arbeit im Büro.", "我今天在办公室有很多工作。"),
            ("der Arbeitsplatz", "der", "n.", "Arbeitsplätze", "工作岗位，工位", "Mein Arbeitsplatz ist modern eingerichtet.", "我的工位布置得很现代。"),
            ("die Stelle", "die", "n.", "-n", "职位，岗位", "Er sucht eine neue Stelle als Buchhalter.", "他在找一份会计的新职位。"),
            ("das Büro", "das", "n.", "-s", "办公室", "Ich bin montags immer im Büro.", "我周一总是在办公室。"),
            ("die Firma", "die", "n.", "Firmen", "公司，企业", "Die Firma produziert Maschinen.", "这家公司生产机械设备。"),
            ("das Unternehmen", "das", "n.", "-", "企业，事业单位", "Das Unternehmen hat 500 Mitarbeiter.", "这家企业拥有500名员工。"),
            ("der Chef", "der", "n.", "-s", "领导，男老板", "Mein Chef ist sehr verständnisvoll.", "我的老板非常通情达理。"),
            ("die Chefin", "die", "n.", "-nen", "女老板，女领导", "Die Chefin leitet die Besprechung.", "女领导主持会议。"),
            ("der Kollege", "der", "n.", "-n", "男同事", "Mein Kollege hilft mir immer.", "我的同事总会帮我。"),
            ("die Kollegin", "die", "n.", "-nen", "女同事", "Meine Kollegin spricht drei Sprachen.", "我的女同事会说三种语言。"),
            ("der Mitarbeiter", "der", "n.", "-", "员工，职员", "Alle Mitarbeiter nehmen am Kurs teil.", "全体员工参加培训。"),
            ("der Lehrer", "der", "n.", "-", "男教师", "Der Lehrer erklärt die Grammatik.", "老师在讲解语法。"),
            ("die Lehrerin", "die", "n.", "-nen", "女教师", "Unsere Deutschlehrerin ist sehr nett.", "我们的德语女老师非常亲切。"),
            ("der Arzt", "der", "n.", "Ärzte", "男医生", "Der Arzt untersucht den Patienten.", "医生在给病人做检查。"),
            ("die Ärztin", "die", "n.", "-nen", "女医生", "Die Ärztin verschreibt ein Medikament.", "女医生开了一张药方。"),
            ("der Ingenieur", "der", "n.", "-e", "男工程师", "Er arbeitet als Ingenieur bei BMW.", "他在宝马公司当工程师。"),
            ("die Ingenieurin", "die", "n.", "-nen", "女工程师", "Sie ist Ingenieurin für Bauwesen.", "她是土木工程女工程师。"),
            ("der Informatiker", "der", "n.", "-", "男程序员，IT工程师", "Informatiker werden überall gesucht.", "各地都急需IT程序员。"),
            ("der Kaufmann", "der", "n.", "Kaufleute", "男商人，商务员", "Er hat eine Ausbildung zum Kaufmann gemacht.", "他完成了商务从业人员培训。"),
            ("der Verkäufer", "der", "n.", "-", "男售货员", "Der Verkäufer berät die Kunden.", "售货员为顾客提供选购建议。"),
            ("der Kellner", "der", "n.", "-", "男服务生", "Der Kellner bringt die Getränke.", "服务员端来了饮品。"),
            ("der Koch", "der", "n.", "Köche", "男厨师", "Der Koch bereitet das Essen zu.", "厨师正在准备菜肴。"),
            ("die Köchin", "die", "n.", "-nen", "女厨师", "Sie arbeitet als Köchin im Hotel.", "她在酒店担任女厨师。"),
            ("der Mechaniker", "der", "n.", "-", "男机修工", "Der Mechaniker repariert mein Auto.", "机修工在修我的汽车。"),
            ("der Fahrer", "der", "n.", "-", "司机，驾驶员", "Der Busfahrer fährt sehr vorsichtig.", "公交车司机开车非常小心稳当。"),
            ("der Polizist", "der", "n.", "-en", "男警察", "Der Polizist regelt den Verkehr.", "警察在疏导交通。"),
            ("die Polizistin", "die", "n.", "-nen", "女警察", "Die Polizistin hilft den Fußgängern.", "女警察帮助行人。"),
            ("der Student", "der", "n.", "-en", "男大学生", "Er ist Student an der TU München.", "他是慕尼黑工大的大学生。"),
            ("die Studentin", "die", "n.", "-nen", "女大学生", "Sie ist Studentin im dritten Semester.", "她是读大二的女大学生。"),
            ("studieren", "", "v.", "studiert, studierte, studiert", "攻读（大学专业）", "Ich studiere Informatik in Berlin.", "我在柏林攻读计算机专业。"),
            ("das Studium", "das", "n.", "Studien", "大学学业", "Nach dem Studium sucht er einen Job.", "大学毕业后他寻找工作。"),
            ("die Universität", "die", "n.", "-en", "大学", "Die Universität Heidelberg ist sehr alt.", "海德堡大学历史非常悠久。"),
            ("die Uni", "die", "n.", "-s", "大学（口语简称）", "Ich fahre morgens mit dem Rad zur Uni.", "我早晨骑自行车去大学。"),
            ("lernen", "", "v.", "lernt, lernte, gelernt", "学习", "Wir lernen fleißig Deutsch.", "我们勤奋地学德语。"),
            ("die Schule", "die", "n.", "-n", "学校", "Die Kinder gehen um acht in die Schule.", "孩子们八点去上学。"),
            ("der Schüler", "der", "n.", "-", "中小学男学生", "Die Schüler machen ihre Hausaufgaben.", "学生们在做家庭作业。"),
            ("der Computer", "der", "n.", "-", "电脑，计算机", "Ich arbeite den ganzen Tag am Computer.", "我一整天都在电脑前工作。"),
            ("der Laptop", "der", "n.", "-s", "笔记本电脑", "Ich nehme meinen Laptop mit ins Büro.", "我把笔记本电脑带到办公室。"),
            ("der Drucker", "der", "n.", "-", "打印机", "Der Drucker hat kein Papier mehr.", "打印机没有纸了。"),
            ("drucken", "", "v.", "druckt, druckte, gedruckt", "打印", "Drucken Sie bitte diesen Bericht aus!", "请打印出这份报告！"),
            ("das Papier", "das", "n.", "-e", "纸张，纸", "Ich brauche ein Blatt Papier zum Schreiben.", "我需要一张纸写字。"),
            ("der Stift", "der", "n.", "-e", "笔", "Hast du einen Stift für mich?", "你有一支笔借我用一下吗？"),
            ("der Kugelschreiber", "der", "n.", "-", "圆珠笔", "Unterschreiben Sie mit dem Kugelschreiber!", "请用圆珠笔签名！"),
            ("der Kuli", "der", "n.", "-s", "圆珠笔（口语）", "Mein Kuli schreibt nicht mehr.", "我的圆珠笔写不出水了。"),
            ("der Bleistift", "der", "n.", "-e", "铅笔", "Zeichnen Sie bitte mit Bleistift!", "请用铅笔作画！"),
            ("das Notizbuch", "das", "n.", "Notizbücher", "笔记本，记事本", "Ich schreibe alles in mein Notizbuch.", "我把一切都记在笔记本上。"),
            ("die Notiz", "die", "n.", "-en", "便签，记录", "Machen Sie sich bitte eine kurze Notiz!", "请您做个简短的记录！"),
            ("das Telefon", "das", "n.", "-e", "电话", "Das Telefon steht auf dem Schreibtisch.", "电话机放在办公桌上。"),
            ("telefonieren", "", "v.", "telefoniert, telefonierte, telefoniert", "打电话通话", "Er telefoniert gerade mit einem Kunden.", "他正在和一位客户通电话。"),
            ("die E-Mail", "die", "n.", "-s", "电子邮件", "Ich habe Ihnen eine E-Mail geschickt.", "我已经给您发了一封电子邮件。"),
            ("senden", "", "v.", "sendet, sandte, gesandt", "发送", "Senden Sie das Dokument per E-Mail!", "请通过电子邮件发送这份文件！"),
            ("schicken", "", "v.", "schickt, schickte, geschickt", "寄送，发送", "Ich schicke dir die Unterlagen heute noch.", "我今天内把材料寄发给你。"),
            ("bekommen", "", "v.", "bekommt, bekam, bekommen", "收到，得到", "Haben Sie meine Nachricht bekommen?", "您收到我的信息了吗？"),
            ("die Pause", "die", "n.", "-n", "休息，中场休息", "Um 12 Uhr machen wir eine Kaffeepause.", "中午12点我们喝咖啡休息一下。"),
            ("der Feierabend", "der", "n.", "-e", "下班，下班休息时间", "Schönen Feierabend allerseits!", "祝大家下班愉快！"),
            ("das Gehalt", "das", "n.", "Gehälter", "薪水，工资", "Das Gehalt kommt am Monatsende.", "工资在月底发放。"),
            ("verdienen", "", "v.", "verdient, verdiente, verdient", "赚取（薪水）；应得", "Er verdient gut in seinem neuen Job.", "他在新工作中收入颇丰。"),
            ("arbeitslos", "", "adj.", "", "失业的", "Er ist seit zwei Monaten arbeitslos.", "他失业两个月了。"),
            ("suchen", "", "v.", "sucht, suchte, gesucht", "寻找", "Ich suche eine Vollzeitstelle.", "我正在寻找一份全职工作。"),
            ("finden", "", "v.", "findet, fand, gefunden", "找到，觉得", "Er hat endlich eine gute Arbeit gefunden.", "他终于找到了一份好工作。"),
            ("die Besprechung", "die", "n.", "-en", "工作会议，商谈", "Wir haben um 14 Uhr eine Besprechung.", "我们下午2点有一场会议。"),
            ("das Meeting", "das", "n.", "-s", "会议", "Das Meeting findet im Konferenzraum statt.", "会议在会议室举行。"),
            ("der Vertrag", "der", "n.", "Verträge", "合同，协议", "Der Arbeitsvertrag ist unbefristet.", "这份劳动合同是无固定期限的。"),
            ("die Vollzeit", "die", "n.", "-", "全职", "Ich arbeite Vollzeit, 40 Stunden pro Woche.", "我是全职工作，每周40小时。"),
            ("die Teilzeit", "die", "n.", "-", "兼职，半职", "Viele Mütter arbeiten in Teilzeit.", "很多母亲从事兼职工作。"),
            ("das Praktikum", "das", "n.", "Praktika", "实习", "Ich mache im Sommer ein Praktikum.", "我暑假做一份实习。"),
            ("der Praktikant", "der", "n.", "-en", "男实习生", "Der Praktikant lernt schnell.", "实习生学得很快。")
        ]
    },

    # LESSON 8
    {
        "id": "A1_L08",
        "title": "第8课：身体部位与基础医疗就医 (Körperteile & Gesundheit)",
        "summary": "掌握身体器官词汇、常见病痛表达、就诊对话与情态动词 müssen/sollen",
        "grammar": {
            "title": "表达疼痛 tut weh 与情态动词 sollen",
            "sections": [
                {
                    "heading": "1. 表达身体不适与疼痛",
                    "content": "• 单数身体部位：Mein Kopf tut weh. (我的头痛。)\n• 复数身体部位：Meine Augen tun weh. (我的眼睛痛。)\n• 复合名词表达：Ich habe Kopfschmerzen / Bauchschmerzen / Halsschmerzen."
                },
                {
                    "heading": "2. 情态动词 sollen (遵医嘱/应该)",
                    "content": "ich soll, du sollst, er soll, wir sollen, ihr sollt, sie sollen。\n例：Der Arzt sagt, ich soll im Bett bleiben und Tee trinken."
                }
            ]
        },
        "quiz": [
            {
                "id": "A1_L08_Q1",
                "type": "EXAM_REAL",
                "question": "德国诊所医生问诊常用语：“Was fehlt Ihnen?” 的意思是：",
                "options": ["您哪里不舒服？", "您叫什么名字？", "您挂号了吗？", "您带钱了吗？"],
                "correctIndex": 0,
                "explanation": "Was fehlt Ihnen? 是德语医生向患者询问病情的标准问候语。"
            },
            {
                "id": "A1_L08_Q2",
                "type": "GRAMMAR_FILL",
                "question": "Meine Beine ______ weh (复数器官痛).",
                "options": ["tun", "tut", "macht", "haben"],
                "correctIndex": 0,
                "explanation": "主语 meine Beine 是复数，动词应用复数形式 tun weh。"
            }
        ],
        "words": [
            ("der Körper", "der", "n.", "-", "身体，躯体", "Sport ist gesund für den Körper.", "运动对身体健康有益。"),
            ("der Kopf", "der", "n.", "Köpfe", "头，头部", "Mein Kopf tut heute schrecklich weh.", "我的头今天疼得厉害。"),
            ("das Haar", "das", "n.", "-e", "头发，毛发", "Sie hat langes, blondes Haar.", "她留着一头金色长发。"),
            ("das Auge", "das", "n.", "-n", "眼睛", "Meine Augen brennen vom Computer.", "长时间看电脑我的眼睛发酸。"),
            ("das Ohr", "das", "n.", "-en", "耳朵", "Das Kind hat Schmerzen am linken Ohr.", "孩子左耳疼痛。"),
            ("die Nase", "die", "n.", "-n", "鼻子", "Meine Nase läuft wegen der Kälte.", "天冷我的鼻子一直在流涕。"),
            ("der Mund", "der", "n.", "Münder", "嘴，口", "Öffnen Sie bitte den Mund ganz weit!", "请把嘴张大！"),
            ("der Zahn", "der", "n.", "Zähne", "牙齿", "Ich muss zweimal im Jahr zum Zahnarzt.", "我一年必须看两次牙医。"),
            ("die Zunge", "die", "n.", "-n", "舌头", "Strecken Sie bitte die Zunge heraus!", "请把舌头伸出来！"),
            ("der Hals", "der", "n.", "Hälse", "脖子，喉咙", "Ich habe Halsschmerzen beim Schlucken.", "我吞咽时喉咙很疼。"),
            ("die Schulter", "die", "n.", "-n", "肩膀", "Meine rechte Schulter ist verspannt.", "我的右肩肌肉很僵硬。"),
            ("der Arm", "der", "n.", "-e", "手臂，胳膊", "Er hat sich den linken Arm gebrochen.", "他的左臂骨折了。"),
            ("die Hand", "die", "n.", "Hände", "手", "Waschen Sie sich vor dem Essen die Hände!", "饭前请洗手！"),
            ("der Finger", "der", "n.", "-", "手指", "Ich habe mich in den Finger geschnitten.", "我切到了手指。"),
            ("die Brust", "die", "n.", "Brüste", "胸部，胸膛", "Atmen Sie tief in die Brust ein!", "请深吸气进胸腔！"),
            ("der Bauch", "der", "n.", "Bäuche", "肚子，腹部", "Das Baby hat Bauchschmerzen.", "婴儿肚子疼。"),
            ("der Magen", "der", "n.", "Mägen", "胃", "Mein Magen knurrt vor Hunger.", "我的胃饿得咕咕叫。"),
            ("der Rücken", "der", "n.", "-", "背部，脊梁", "Viele Leute haben Probleme mit dem Rücken.", "许多人有脊背酸痛问题。"),
            ("das Bein", "das", "n.", "-e", "腿", "Meine Beine sind müde vom langen Gehen.", "走久了我的双腿很累。"),
            ("das Knie", "das", "n.", "-", "膝盖", "Mein rechtes Knie tut beim Laufen weh.", "我跑步时右膝盖疼。"),
            ("der Fuß", "der", "n.", "Füße", "脚", "Wir gehen heute zu Fuß nach Hause.", "我们今天步行走回家。"),
            ("die Gesundheit", "die", "n.", "-", "健康", "Gesundheit ist das Wichtigste im Leben.", "健康是生命中最重要的事。"),
            ("gesund", "", "adj.", "gesünder, am gesündesten", "健康的", "Obst und Gemüse sind sehr gesund.", "果蔬非常有益健康。"),
            ("krank", "", "adj.", "kränker, am kränksten", "生病的", "Er ist heute krank und bleibt zu Hause.", "他今天病了，留在家中。"),
            ("die Krankheit", "die", "n.", "-en", "疾病", "Die Krankheit ist nicht ansteckend.", "这种病不传染。"),
            ("der Schmerz", "der", "n.", "-en", "疼痛", "Haben Sie starke Schmerzen?", "您感到剧烈的疼痛吗？"),
            ("wehtun", "", "v.", "tut weh, tat weh, wehgetan", "感到疼痛", "Wo tut es Ihnen weh?", "您哪里觉得疼？"),
            ("die Kopfschmerzen", "die", "n.pl.", "-", "头痛", "Gegen Kopfschmerzen hilft eine Tablette.", "一片药片有助于缓解头痛。"),
            ("die Bauchschmerzen", "die", "n.pl.", "-", "腹痛，胃痛", "Ich habe nach dem Essen Bauchschmerzen.", "饭后我感到肚子痛。"),
            ("das Fieber", "das", "n.", "-", "发烧，发热", "Das Kind hat hohes Fieber, 39 Grad.", "孩子发高烧，39度。"),
            ("die Grippe", "die", "n.", "-n", "流感", "Er liegt mit einer schweren Grippe im Bett.", "他得了严重流感卧床不起。"),
            ("die Erkältung", "die", "n.", "-en", "感冒，着凉", "Ich habe mir eine Erkältung geholt.", "我不小心受凉感冒了。"),
            ("husten", "", "v.", "hustet, hustete, gehustet", "咳嗽", "Er hustet schon seit drei Tagen.", "他已经咳嗽三天了。"),
            ("der Husten", "der", "n.", "-", "咳嗽", "Hustensaft beruhigt die Bronchien.", "止咳糖浆能缓解支气管。"),
            ("der Schnupfen", "der", "n.", "-", "流鼻涕，伤风鼻塞", "Bei Schnupfen hilft ein Nasenspray.", "鼻塞流涕时鼻喷剂很管用。"),
            ("die Praxis", "die", "n.", "Praxen", "诊所", "Die Praxis von Dr. Weber ist heute offen.", "韦伯医生的诊所今天接诊。"),
            ("das Krankenhaus", "das", "n.", "Krankenhäuser", "医院", "Der Krankenwagen fährt ins Krankenhaus.", "救护车正开往医院。"),
            ("die Apotheke", "die", "n.", "-n", "药店，药房", "Die Medizin kaufe ich in der Apotheke.", "我在药店买这种药。"),
            ("das Medikament", "das", "n.", "-e", "药物，药品", "Nehmen Sie das Medikament dreimal täglich!", "请每日服用该药三次！"),
            ("die Medizin", "die", "n.", "-en", "医学；药物", "Haben Sie die Medizin schon genommen?", "您吃药了吗？"),
            ("die Tablette", "die", "n.", "-n", "药片", "Eine Tablette morgens mit Wasser schlucken.", "早晨就水吞服一片药片。"),
            ("das Pflaster", "das", "n.", "-", "创口贴", "Kleben Sie ein Pflaster auf die Wunde!", "在伤口上贴一张创口贴！"),
            ("der Verband", "der", "n.", "Verbände", "绷带", "Die Schwester wechselt den Verband.", "护士更换了包扎绷带。"),
            ("das Rezept", "das", "n.", "-e", "处方；菜谱", "Der Arzt gibt mir ein Rezept für die Pille.", "医生给我开了一张药方。"),
            ("untersuchen", "", "v.", "untersucht, untersuchte, untersucht", "检查，体检", "Der Arzt untersucht gründlich mein Herz.", "医生仔细检查了我的心脏。"),
            ("die Untersuchung", "die", "n.", "-en", "体检，检查", "Die Untersuchung dauert eine halbe Stunde.", "体检耗时半个小时。"),
            ("fehlen", "", "v.", "fehlt, fehlte, gefehlt", "缺少；不舒服", "Was fehlt Ihnen denn?", "您到底哪里不舒服？"),
            ("fühlen", "", "v.", "fühlt, fühlte, gefühlt", "感觉，体会", "Wie fühlen Sie sich heute?", "您今天感觉如何？"),
            ("besser", "", "adj./adv.", "", "更好，有好转", "Geht es dir heute schon besser?", "你今天感觉好点了吗？"),
            ("schlecht", "", "adj./adv.", "", "差，糟糕，恶心", "Mir ist plötzlich ganz schlecht.", "我突然感到非常恶心难受。"),
            ("müde", "", "adj.", "müder, am müdesten", "疲倦的，困倦的", "Ich bin nach der Arbeit sehr müde.", "下班后我感到非常疲倦。"),
            ("schlafen", "", "v.", "schläft, schlief, geschlafen", "睡觉", "Sie sollten mindestens 8 Stunden schlafen.", "您应该睡至少8小时。"),
            ("ausruhen", "", "v.", "ruht aus, ruhte aus, ausgeruht", "休整，歇息", "Ruh dich am Wochenende gut aus!", "周末好好休息放松一下！"),
            ("das Bett", "das", "n.", "-en", "床", "Bleiben Sie bitte zwei Tage im Bett!", "请在床上静养两天！"),
            ("die Krankenversicherung", "die", "n.", "-en", "医疗保险", "In Deutschland ist eine Versicherung Pflicht.", "在德国医疗保险是强制性的。"),
            ("die Versichertenkarte", "die", "n.", "-n", "医保卡", "Zeigen Sie bitte Ihre Versichertenkarte!", "请出示您的医保卡！"),
            ("die Notaufnahme", "die", "n.", "-n", "急诊室", "Bei einem Unfall fährt man zur Notaufnahme.", "发生意外事故时去急诊室。"),
            ("der Notarzt", "der", "n.", "Notärzte", "急救医生", "Rufen Sie sofort den Notarzt!", "请立刻拨打急救呼叫医生！"),
            ("der Krankenwagen", "der", "n.", "-", "救护车", "Der Krankenwagen kam nach fünf Minuten.", "救护车五分钟后赶到了。"),
            ("die Wunde", "die", "n.", "-n", "伤口", "Die Wunde verheilt erfreulich schnell.", "伤口愈合得令人欣喜地快。"),
            ("das Blut", "das", "n.", "-", "血液", "Der Arzt nimmt mir Blut ab.", "医生给我抽血检查。"),
            ("der Unfall", "der", "n.", "Unfälle", "事故，意外", "Zum Glück gab es beim Unfall keine Verletzten.", "所幸事故中无人受伤。"),
            ("verletzen", "", "v.", "verletzt, verletzte, verletzt", "使受伤", "Er hat sich am Knie verletzt.", "他的膝盖受了伤。"),
            ("das Gewicht", "das", "n.", "-e", "体重，重量", "Der Arzt misst Größe und Gewicht.", "医生测量了身高和体重。"),
            ("die Diät", "die", "n.", "-en", "节食，特殊饮食", "Er macht eine salzarme Diät.", "他在进行低盐饮食调理。"),
            ("der Sport", "der", "n.", "-", "体育运动", "Regelmäßiger Sport stärkt das Herz.", "经常锻炼能够强化心脏功能。"),
            ("die Luft", "die", "n.", "-", "空气", "Gehen wir an die frische Luft!", "我们到户外呼吸新鲜空气吧！"),
            ("spazieren gehen", "", "phrase", "", "散步，漫步", "Ich gehe jeden Tag eine Stunde spazieren.", "我每天散步一小时。"),
            ("die Besserung", "die", "n.", "-", "好转，康复", "Gute Besserung wünsche ich dir!", "祝你早日康复！"),
            ("überweisen", "", "v.", "überweist, überwies, überwiesen", "转诊；汇款", "Der Hausarzt überweist mich zum Facharzt.", "全科医生把我转诊给专科医生。")
        ]
    },

    # LESSON 9
    {
        "id": "A1_L09",
        "title": "第9课：城市设施与交通出行 (Stadt & Verkehrsmittel)",
        "summary": "掌握公共交通工具、车站买票、问路指路与祈使句(Imperativ)",
        "grammar": {
            "title": "交通工具介词 mit 与祈使句 (Imperativ)",
            "sections": [
                {
                    "heading": "1. 交通工具表达：mit + 第三格 Dativ",
                    "content": "• mit dem Bus (阳性)\n• mit dem Zug / mit der Straßenbahn (阴性)\n• mit dem Fahrrad / mit dem Auto (中性)\n• zu Fuß gehen (步行走路，固定搭配不用 mit)"
                },
                {
                    "heading": "2. 尊称祈使句 (Sie-Form) 规则",
                    "content": "动词原形放在句首，后接 Sie！\n• Gehen Sie bitte geradeaus!\n• Biegen Sie an der Ampel links ab!\n• Steigen Sie am Hauptbahnhof um!"
                }
            ]
        },
        "quiz": [
            {
                "id": "A1_L09_Q1",
                "type": "GRAMMAR_FILL",
                "question": "问路礼貌指路：“请您向左转！”德语是：",
                "options": ["Biegen Sie links ab!", "Sie biegen links ab.", "Biegst du links!", "Abbiegen links Sie!"],
                "correctIndex": 0,
                "explanation": "尊称祈使句结构：动词原形位于句首 + Sie + 其他成分 (Biegen Sie links ab!)。"
            },
            {
                "id": "A1_L09_Q2",
                "type": "VOCAB_MEANING",
                "question": "德语交通中 'am Hauptbahnhof umsteigen' 的意思是：",
                "options": ["在火车总站换乘车", "在火车总站买票", "在火车总站下车不出站", "在火车总站等车"],
                "correctIndex": 0,
                "explanation": "umsteigen 意为“换乘，倒车”；Hauptbahnhof 是“火车总站”。"
            }
        ],
        "words": [
            ("die Stadt", "die", "n.", "Städte", "城市", "Berlin ist eine lebendige Stadt.", "柏林是一座生机勃勃的城市。"),
            ("das Zentrum", "das", "n.", "Zentren", "中心，市中心", "Das Rathaus liegt mitten im Zentrum.", "市政厅位于市中心正中。"),
            ("die Innenstadt", "die", "n.", "Innenstädte", "市中心城区", "In der Innenstadt gibt es viele Geschäfte.", "市中心有很多商店商铺。"),
            ("die Straße", "die", "n.", "-n", "街道，马路", "Überqueren Sie die Straße an der Ampel!", "请在红绿灯处穿过马路！"),
            ("der Platz", "der", "n.", "Plätze", "广场；位置", "Der Alexanderplatz ist sehr berühmt.", "亚历山大广场非常著名。"),
            ("das Gebäude", "das", "n.", "-", "建筑，楼房", "Das historische Gebäude wurde saniert.", "这座历史建筑经过了修缮。"),
            ("die Ecke", "die", "n.", "-n", "拐角，角落", "Die Bäckerei ist gleich an der Ecke.", "面包房就在拐角处。"),
            ("die Kreuzung", "die", "n.", "-en", "十字路口", "An der nächsten Kreuzung biegen Sie rechts ab.", "在下一个十字路口向右转。"),
            ("die Ampel", "die", "n.", "-n", "红绿灯，交通信号灯", "Die Ampel steht auf Rot.", "红绿灯现在是红灯。"),
            ("die Brücke", "die", "n.", "-n", "桥，桥梁", "Wir gehen über die Brücke.", "我们走过大桥。"),
            ("der Fluss", "der", "n.", "Flüsse", "河流", "Der Rhein ist ein langer Fluss.", "莱茵河是一条长河。"),
            ("der Park", "der", "n.", "-s", "公园", "Sonntags gehen die Leute im Park spazieren.", "周日人们在公园里散步。"),
            ("der Bahnhof", "der", "n.", "Bahnhöfe", "火车站", "Der Zug fährt um 9 Uhr am Bahnhof ab.", "火车9点从车站发车。"),
            ("der Hauptbahnhof", "der", "n.", "Hauptbahnhöfe", "火车总站", "Treffen wir uns am Hauptbahnhof!", "我们在火车总站碰面！"),
            ("das Gleis", "das", "n.", "-e", "铁轨，站台股道", "Der ICE nach München steht auf Gleis 4.", "开往慕尼黑的高铁在4站台候车。"),
            ("der Bahnsteig", "der", "n.", "-e", "站台，月台", "Bitte Vorsicht am Bahnsteig!", "站台候车请注意安全！"),
            ("die Haltestelle", "die", "n.", "-n", "车站，公交停靠站", "Die nächste Haltestelle ist Goethestraße.", "下一站是歌德街。"),
            ("der Fahrplan", "der", "n.", "Fahrpläne", "时刻表", "Schau bitte im Fahrplan nach!", "请在时刻表上查一下！"),
            ("das Ticket", "das", "n.", "-s", "车票，门票", "Ich habe ein Ticket online gekauft.", "我在线上买了一张票。"),
            ("die Fahrkarte", "die", "n.", "-n", "车票", "Eine Fahrkarte nach Köln bitte!", "请来一张去科隆的车票！"),
            ("der Fahrkartenautomat", "der", "n.", "-en", "自动售票机", "Man kann am Automaten mit Karte zahlen.", "可以在自动售票机刷卡购票。"),
            ("entwerten", "", "v.", "entwertet, entwertete, entwertet", "检票，验票打孔", "Vergessen Sie nicht, das Ticket zu entwerten!", "别忘了将车票检票打孔！"),
            ("der Schaffner", "der", "n.", "-", "列车乘务员，查票员", "Der Schaffner kontrolliert die Fahrkarten.", "查票员在检查车票。"),
            ("der Bus", "der", "n.", "-se", "公共汽车，大巴", "Der Bus Nummer 100 fährt zum Zoo.", "100路公交车开往动物园。"),
            ("die Straßenbahn", "die", "n.", "-en", "有轨电车", "Die Straßenbahn kommt alle zehn Minuten.", "有轨电车每十分钟一趟。"),
            ("die Tram", "die", "n.", "-s", "电车（口语简称）", "Fahren wir mit der Tram!", "我们乘有轨电车走吧！"),
            ("die U-Bahn", "die", "n.", "-en", "地下铁道，地铁", "Die U-Bahn ist schnell und pünktlich.", "地铁快捷且准时。"),
            ("die S-Bahn", "die", "n.", "-en", "城市快铁", "Mit der S-Bahn fährt man zum Flughafen.", "乘城市快铁去机场。"),
            ("der Zug", "der", "n.", "Züge", "火车，列车", "Der Zug fährt pünktlich ab.", "火车准点发车。"),
            ("die Bahn", "die", "n.", "-en", "铁路，德国铁路", "Die Deutsche Bahn bietet Sparpreise an.", "德国铁路提供特惠票价。"),
            ("das Taxi", "das", "n.", "-s", "出租车", "Wir nehmen ein Taxi zum Hotel.", "我们打一辆出租车去酒店。"),
            ("das Auto", "das", "n.", "-s", "汽车，轿车", "Er fährt jeden Tag mit dem Auto zur Arbeit.", "他每天开汽车去上班。"),
            ("das Fahrrad", "das", "n.", "Fahrräder", "自行车", "Ich fahre gerne mit dem Fahrrad.", "我喜欢骑自行车出行。"),
            ("das Rad", "das", "n.", "Räder", "自行车；轮子", "Kommst du mit dem Rad?", "你是骑车过来的吗？"),
            ("das Flugzeug", "das", "n.", "-e", "飞机", "Das Flugzeug fliegt über die Alpen.", "飞机飞越阿尔卑斯山脉。"),
            ("der Flughafen", "der", "n.", "Flughäfen", "机场，航空港", "Wie komme ich am schnellsten zum Flughafen?", "怎么去机场最快？"),
            ("fahren", "", "v.", "fährt, fuhr, ist gefahren", "驾驶，乘车前往", "Wir fahren am Wochenende nach Hamburg.", "我们周末乘车去汉堡。"),
            ("abfahren", "", "v.", "fährt ab, fuhr ab, ist abgefahren", "发车，出发", "Der Bus fährt um Punkt 10 Uhr ab.", "大巴整十点发车。"),
            ("die Abfahrt", "die", "n.", "-en", "发车，出发时间", "Die Abfahrt verzögert sich um 15 Minuten.", "发车推迟15分钟。"),
            ("ankommen", "", "v.", "kommt an, kam an, ist angekommen", "到达，抵达", "Wann kommt der Flug in Frankfurt an?", "航班什么时候抵达法兰克福？"),
            ("die Ankunft", "die", "n.", "Ankünfte", "到达，抵达时间", "Die Ankunft ist für 18 Uhr geplant.", "计划到达时间为18点。"),
            ("einsteigen", "", "v.", "steigt ein, stieg ein, ist eingestiegen", "上车", "Bitte alle einsteigen, die Türen schließen!", "请全体上车，车门即将关闭！"),
            ("aussteigen", "", "v.", "steigt aus, stieg aus, ist ausgestiegen", "下车", "An der nächsten Station steigen wir aus.", "在下一站我们下车。"),
            ("umsteigen", "", "v.", "steigt um, stieg um, ist umgestiegen", "换乘，倒车", "Müssen wir unterwegs umsteigen?", "我们中途需要换乘吗？"),
            ("verpassen", "", "v.", "verpasst, verpasste, verpasst", "错过，耽误", "Beeil dich, sonst verpassen wir den Bus!", "快点，不然我们要错过公交了！"),
            ("gehen", "", "v.", "geht, ging, ist gegangen", "走，步行", "Ich gehe jeden Morgen zu Fuß.", "我每天早晨步行走路。"),
            ("die Fußgängerzone", "die", "n.", "-n", "步行街", "In der Fußgängerzone darf man nicht Auto fahren.", "步行街禁止机动车通行。"),
            ("die Post", "die", "n.", "-", "邮局；邮件", "Wo ist hier die nächste Post?", "请问这附近最近的邮局在哪里？"),
            ("die Bank", "die", "n.", "-en", "银行", "Ich muss schnell zur Bank Geld abheben.", "我得赶紧去银行取点钱。"),
            ("das Museum", "das", "n.", "Museen", "博物馆", "Montags ist das Museum geschlossen.", "周一博物馆闭馆。"),
            ("das Kino", "das", "n.", "-s", "电影院", "Gehen wir heute Abend ins Kino?", "今晚我们去看电影好吗？"),
            ("das Theater", "das", "n.", "-", "剧场，剧院", "Wir haben Karten für das Theater.", "我们有话剧院的门票。"),
            ("die Kirche", "die", "n.", "-n", "教堂", "Die alte Kirche steht am Marktplatz.", "老教堂伫立在集市广场旁。"),
            ("das Hotel", "das", "n.", "-s", "酒店，饭店", "Das Hotel liegt zentral und ruhig.", "这家酒店地处中心且安静。"),
            ("die Jugendherberge", "die", "n.", "-n", "青年旅舍", "Studenten übernachten in der Jugendherberge.", "大学生们夜宿在青年旅舍。"),
            ("die Information", "die", "n.", "-en", "问讯处；信息", "Fragen Sie an der Touristen-Information!", "请咨询旅游问讯处！"),
            ("der Stadtplan", "der", "n.", "Stadtpläne", "城市地图", "Haben Sie einen kostenlosen Stadtplan?", "您有一份免费城市地图吗？"),
            ("der Weg", "der", "n.", "-e", "道路，路线", "Können Sie mir den Weg zum Dom zeigen?", "您能给我指一下去大教堂的路吗？"),
            ("fragen", "", "v.", "fragt, fragte, gefragt", "询问，向...打听", "Wir fragen den Polizisten nach dem Weg.", "我们向警察问路。"),
            ("zeigen", "", "v.", "zeigt, zeigte, gezeigt", "指出，出示", "Er zeigt mir den Weg auf der Karte.", "他在地图上把路线指给我看。"),
            ("geradeaus", "", "adv.", "", "径直，一直向前", "Gehen Sie immer geradeaus weiter!", "请一直往前走！"),
            ("rechts", "", "adv.", "", "向右，在右边", "Biegen Sie an der Kreuzung rechts ab!", "在十字路口请向右拐！"),
            ("links", "", "adv.", "", "向左，在左边", "Das Museum liegt auf der linken Seite.", "博物馆位于左侧。"),
            ("oben", "", "adv.", "", "在上面", "Die Wohnung liegt ganz oben.", "公寓在最顶层。"),
            ("unten", "", "adv.", "", "在下面", "Der Keller ist ganz unten im Haus.", "地下室在房子的最底下。"),
            ("vorne", "", "adv.", "", "在前面", "Der Fahrer sitzt vorne im Bus.", "司机坐在大巴车的前排。"),
            ("hinten", "", "adv.", "", "在后面", "Die Toiletten befinden sich hinten.", "洗手间位于后部。"),
            ("in der Nähe", "", "phrase", "", "在附近", "Gibt es einen Bäcker in der Nähe?", "附近有面包房吗？"),
            ("weit", "", "adj./adv.", "weiter, am weitesten", "远，遥远", "Ist es noch sehr weit bis zum Zentrum?", "离市中心还很远吗？"),
            ("nah", "", "adj./adv.", "näher, am nächsten", "近的，靠近", "Die U-Bahn-Station liegt ganz nah.", "地铁站离得非常近。")
        ]
    },

    # LESSON 10
    {
        "id": "A1_L10",
        "title": "第10课：服饰穿搭、色彩与商场购物 (Kleidung, Farben & Einkaufen)",
        "summary": "掌握服装鞋帽词汇、基础颜色、试穿尺寸与尺码评价",
        "grammar": {
            "title": "动词 gefallen (喜欢) 与 passen (合适)",
            "sections": [
                {
                    "heading": "1. gefallen 与 passen 支配第三格用法",
                    "content": "• gefallen 表达审美上的喜爱：Das Hemd gefällt mir sehr gut.\n• passen 表达尺寸、尺码与时间上的吻合合适：Die Hose passt mir genau.\n• stehen 表达款式称身好看：Die Jacke steht dir ausgezeichnet."
                },
                {
                    "heading": "2. 形容词作为表语（不带词尾）",
                    "content": "形容词在 sein, finden 之后作表语时，永远不加词尾！\n例：Das Kleid ist schön. / Ich finde die Jacke teuer."
                }
            ]
        },
        "quiz": [
            {
                "id": "A1_L10_Q1",
                "type": "GRAMMAR_FILL",
                "question": "Wie gefällt ______ (ich, 第三人称代词格位) diese Jacke?",
                "options": ["mir", "mich", "ich", "mein"],
                "correctIndex": 0,
                "explanation": "gefallen 后面接人称代词第三格（Dativ），ich 变为 mir。"
            },
            {
                "id": "A1_L10_Q2",
                "type": "VOCAB_MEANING",
                "question": "在商场试穿衣服时想问“试衣间在哪里？”，德语是：",
                "options": ["Wo ist die Umkleidekabine?", "Wo ist das Essen?", "Wo ist der Bahnhof?", "Wo ist das Bett?"],
                "correctIndex": 0,
                "explanation": "die Umkleidekabine 是商场“试衣间”的标准词汇。"
            }
        ],
        "words": [
            ("die Kleidung", "die", "n.", "-", "衣服，服装（总称）", "Ich brauche warme Kleidung für den Winter.", "我需要准备过冬的暖和衣物。"),
            ("das Kleidungsstück", "das", "n.", "-e", "单件衣服", "Dieses Kleidungsstück ist aus reiner Wolle.", "这件衣服是纯羊毛面料。"),
            ("das Kaufhaus", "das", "n.", "Kaufhäuser", "百货百货大楼", "Im Kaufhaus gibt es Kleidung im 1. Stock.", "百货商场一楼有服饰专柜。"),
            ("das Einkaufszentrum", "das", "n.", "Einkaufszentren", "购物中心，商场", "Wir gehen samstags ins Einkaufszentrum.", "周六我们去购物中心。"),
            ("das Geschäft", "das", "n.", "-e", "商铺，商店", "Die Geschäfte öffnen um 9 Uhr 30.", "商店九点半开门营业。"),
            ("die Umkleidekabine", "die", "n.", "-n", "试衣间", "Wo finde ich eine freie Umkleidekabine?", "请问哪里有空的试衣间？"),
            ("die Größe", "die", "n.", "-n", "尺寸，尺码", "Welche Größe haben Sie? - Größe 38.", "您穿多大尺码？- 38码。"),
            ("anprobieren", "", "v.", "probiert an, probierte an, anprobiert", "试穿（衣物）", "Kann ich diese Jacke bitte anprobieren?", "我能试穿一下这件夹克吗？"),
            ("passen", "", "v.", "passt, passte, gepasst", "合身，合适", "Die Hose passt mir perfekt.", "这条裤子我穿很合适。"),
            ("gefallen", "", "v.", "gefällt, gefiel, gefallen", "合心意，讨人喜欢", "Wie gefällt Ihnen dieser blaue Mantel?", "您觉得这件蓝色大衣怎么样？"),
            ("stehen", "", "v.", "steht, stand, gestanden", "衬，适宜（气色气质）", "Die rote Farbe steht dir ausgezeichnet!", "红色非常衬你的气质！"),
            ("tragen", "", "v.", "trägt, trug, getragen", "穿戴，佩戴", "Er trägt heute einen schicken Anzug.", "他今天穿了一身帅气的西装。"),
            ("das Hemd", "das", "n.", "-en", "男士衬衫", "Ein weißes Hemd für das Vorstellungsgespräch.", "面试穿的一件白衬衫。"),
            ("die Bluse", "die", "n.", "-n", "女士衬衫", "Sie trägt eine seidene Bluse.", "她穿着一件丝质女衬衫。"),
            ("das T-Shirt", "das", "n.", "-s", "T恤衫", "Im Sommer trage ich bunte T-Shirts.", "夏天我喜欢穿彩色T恤。"),
            ("der Pullover", "der", "n.", "-", "毛衣，套头衫", "Der Wollpullover hält herrlich warm.", "羊毛套头衫非常保暖。"),
            ("der Pulli", "der", "n.", "-s", "毛衣（口语）", "Zieh einen warmen Pulli an!", "穿上一件暖和的毛衣！"),
            ("die Hose", "die", "n.", "-n", "裤子", "Die Hose ist ein wenig zu lang.", "这条裤子稍微有点偏长。"),
            ("die Jeans", "die", "n.pl.", "-", "牛仔裤", "Ich trage am liebsten bequeme Jeans.", "我最喜欢穿舒服的牛仔裤。"),
            ("das Kleid", "das", "n.", "-er", "连衣裙", "Sie hat ein elegantes Kleid gekauft.", "她买了一条高雅的连衣裙。"),
            ("der Rock", "der", "n.", "Röcke", "半身裙，裙子", "Der schwarze Rock passt zu vielen Blusen.", "这条黑短裙百搭各种衬衫。"),
            ("der Anzug", "der", "n.", "Anzüge", "西服套装", "Der Bräutigam trägt einen dunklen Anzug.", "新郎穿着一套深色西装。"),
            ("das Kostüm", "das", "n.", "-e", "女士西服套装", "Ein professionelles Kostüm fürs Büro.", "一套职业的办公室女西服。"),
            ("die Krawatte", "die", "n.", "-n", "领带", "Er bindet seine Krawatte um.", "他在系领带。"),
            ("die Jacke", "die", "n.", "-n", "夹克，外套", "Nimm eine Jacke mit, es kühlt ab!", "带上一件外套，天凉了！"),
            ("der Mantel", "der", "n.", "Mäntel", "大衣，风衣", "Im Winter trage ich einen Daunenmantel.", "冬天我穿一件羽绒大衣。"),
            ("der Regenmantel", "der", "n.", "Regenmäntel", "雨衣", "Vergiss deinen Regenmantel nicht!", "别忘了带你的雨衣！"),
            ("der Schuh", "der", "n.", "-e", "鞋子", "Ich brauche neue bequeme Schuhe.", "我需要买一双舒适的新鞋。"),
            ("die Schuhe", "die", "n.pl.", "-", "鞋子（复数）", "Zieh bitte die Schuhe vor der Tür aus!", "请在门外把鞋子脱掉！"),
            ("die Stiefel", "die", "n.pl.", "-", "靴子", "Im Winter brauche ich warme Stiefel.", "冬天我需要保暖的靴子。"),
            ("die Sportschuhe", "die", "n.pl.", "-", "运动鞋", "Ich gehe mit Sportschuhen joggen.", "我穿运动鞋去慢跑。"),
            ("die Socke", "die", "n.", "-n", "短袜", "Warme Wollsocken für kalte Tage.", "冷天穿的保暖羊毛袜。"),
            ("der Strumpf", "der", "n.", "Strümpfe", "长袜", "Sie trägt elegante Strümpfe.", "她穿着优雅的长统袜。"),
            ("die Mütze", "die", "n.", "-n", "帽子（毛线无檐帽）", "Die Mütze schützt die Ohren vor Kälte.", "毛线帽保护耳朵免受严寒。"),
            ("der Hut", "der", "n.", "Hüte", "帽子（有檐礼帽）", "Der Herr trägt einen eleganten Hut.", "那位先生戴着一顶优雅的礼帽。"),
            ("der Schal", "der", "n.", "-s", "围巾", "Ein weicher Schal hält den Hals warm.", "一条柔软的围巾让脖子暖和。"),
            ("die Handschuhe", "die", "n.pl.", "-", "手套", "Ich habe meine Handschuhe verloren.", "我把手套弄丢了。"),
            ("der Gürtel", "der", "n.", "-", "皮带，腰带", "Der Gürtel passt gut zur Hose.", "这条腰带和裤子很搭。"),
            ("die Tasche", "die", "n.", "-n", "包，手袋；口袋", "Wo hast du diese hübsche Tasche gekauft?", "你在哪里买的这个漂亮包包？"),
            ("die Handtasche", "die", "n.", "-n", "手提包", "Sie trägt eine braune Lederhandtasche.", "她提着一个棕色皮质手提包。"),
            ("der Rucksack", "der", "n.", "Rucksäcke", "双肩包，背包", "Der Rucksack ist praktisch für Reisen.", "双肩背包去旅行很实用。"),
            ("der Koffer", "der", "n.", "-", "行李箱", "Ich packe heute Abend meinen Koffer.", "我今晚收拾行李箱。"),
            ("die Brille", "die", "n.", "-n", "眼镜", "Ohne Brille kann ich nicht scharf sehen.", "不戴眼镜我看东西不清晰。"),
            ("die Sonnenbrille", "die", "n.", "-n", "太阳镜，墨镜", "Im Sommerurlaub brauche ich die Sonnenbrille.", "暑假去海边度假需要墨镜。"),
            ("der Schirm", "der", "n.", "-e", "雨伞", "Es regnet, nimm einen Schirm mit!", "外面下雨了，带把伞！"),
            ("der Regenschirm", "der", "n.", "-e", "雨伞", "Mein Regenschirm ist rot.", "我的雨伞是红色的。"),
            ("der Schmuck", "der", "n.", "-", "首饰，珠宝", "Sie mag schlichten Schmuck aus Silber.", "她喜欢朴素的银饰。"),
            ("die Uhr", "die", "n.", "-en", "手表，钟", "Meine Armbanduhr ist stehen geblieben.", "我的手表停走了。"),
            ("die Farbe", "die", "n.", "-n", "颜色，色彩", "Welche Farbe gefällt dir am besten?", "你最喜欢什么颜色？"),
            ("rot", "", "adj.", "röter, am rötesten", "红色的", "Ein rotes Kleid für das Fest.", "参加宴会穿的一条红色裙子。"),
            ("blau", "", "adj.", "blauer, am blausten", "蓝色的", "Der Himmel ist heute strahlend blau.", "今天天空湛蓝晴朗。"),
            ("grün", "", "adj.", "grüner, am grünsten", "绿色的", "Im Frühling wird das Gras wieder grün.", "春天小草又变绿了。"),
            ("gelb", "", "adj.", "gelber, am gelbsten", "黄色的", "Die Sonnenblume hat gelbe Blüten.", "向日葵开着黄色的花。"),
            ("schwarz", "", "adj.", "schwärzer, am schwärzesten", "黑色的", "Er trägt einen eleganten schwarzen Anzug.", "他穿一身优雅的黑色西装。"),
            ("weiß", "", "adj.", "weißer, am weißesten", "白色的", "Im Winter fällt weißer Schnee.", "冬天落下洁白的白雪。"),
            ("grau", "", "adj.", "grauer, am grausten", "灰色的", "Der Himmel ist heute grau und bewölkt.", "今天天空阴沉灰暗。"),
            ("braun", "", "adj.", "brauner, am braunsten", "棕色的，褐色的", "Sie hat schöne braune Augen.", "她有一双美丽的棕色眼睛。"),
            ("orange", "", "adj.", "", "橙色的", "Eine warme orange Jacke für Kinder.", "一件暖和的儿童橙色夹克。"),
            ("rosa", "", "adj.", "", "粉红色的", "Das kleine Mädchen mag rosa Kleider.", "小女孩喜欢粉色裙子。"),
            ("lila", "", "adj.", "", "紫色的", "Lavendel blüht in schönem Lila.", "薰衣草盛开着漂亮的紫色。"),
            ("bunt", "", "adj.", "bunter, am buntesten", "五颜六色的", "Die Herbstblätter sind bunt gefärbt.", "秋天的落叶色彩斑斓。"),
            ("hell", "", "adj.", "", "浅色的，明亮的", "Ein hellblaues Hemd passt gut zum Anzug.", "一件浅蓝色衬衫与西服很相配。"),
            ("dunkel", "", "adj.", "", "深色的，暗的", "Dunkle Farben wirken formeller.", "深色衣物显得更为正式。"),
            ("schön", "", "adj.", "schöner, am schönsten", "美丽的，好看的", "Das ist ein wirklich schönes Kleid.", "这真是一条漂亮的裙子。"),
            ("hässlich", "", "adj.", "hässlicher, am hässlichsten", "难看的，丑的", "Diese Krawatte finde ich ziemlich hässlich.", "我觉得这条领带挺难看的。"),
            ("modern", "", "adj.", "moderner, am modernsten", "时髦的，现代的", "Ihr Stil ist sehr modern und elegant.", "她的穿搭风格非常前卫优雅。"),
            ("altmodisch", "", "adj.", "", "过时的，老派的", "Dieser Schnitt wirkt etwas altmodisch.", "这种剪裁样式显得略微过时。"),
            ("bequem", "", "adj.", "bequemer, am bequemsten", "舒服的，便捷的", "Die Sportschuhe sind extrem bequem.", "这双运动鞋穿起来极度舒适。"),
            ("eng", "", "adj.", "enger, am engsten", "紧身的，窄小的", "Die Hose ist an den Beinen zu eng.", "这条裤子裤腿处太紧了。"),
            ("weit", "", "adj.", "weiter, am weitesten", "宽松的，宽大的", "Im Sommer trage ich gerne weite Hosen.", "夏天我喜欢穿宽松的裤子。")
        ]
    }
]
