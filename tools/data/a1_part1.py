#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A1 Part 1: Lessons 1 to 5 (350 words)
L01: 相识、寒暄与国籍 (Begrüßung & Länder) - 70 words
L02: 家庭、亲属与称谓 (Familie & Verwandtschaft) - 70 words
L03: 食材、餐饮与超市采购 (Essen & Supermarkt) - 70 words
L04: 餐厅点餐与就餐文化 (Im Restaurant & Mahlzeiten) - 70 words
L05: 居住房型、租房与家具 (Wohnen, Wohnung & Möbel) - 70 words
"""

LESSONS_PART1 = [
    # LESSON 1
    {
        "id": "A1_L01",
        "title": "第1课：相识、寒暄与国籍 (Begrüßung & Länder)",
        "summary": "掌握人称代词、动词变位规则、sein/haben/heißen、国家与国籍表达",
        "grammar": {
            "title": "动词现在时变位规则 (Präsens) 与基础疑问句",
            "sections": [
                {
                    "heading": "1. 规则动词现在时词尾 (ich -e, du -st, er/sie/es -t, wir -en, ihr -t, sie/Sie -en)",
                    "content": "• lernen: ich lerne, du lernst, er lernt, wir lernen, ihr lernt, sie lernen\n• kommen: ich komme, du kommst, er kommt, wir kommen, ihr kommt, sie kommen\n• sein: ich bin, du bist, er ist, wir sind, ihr seid, sie sind\n• haben: ich habe, du hast, er hat, wir haben, ihr habt, sie haben"
                },
                {
                    "heading": "2. 陈述句与两大核心疑问句语序",
                    "content": "• 陈述句：变位动词永远占第 2 位！(Ich komme aus China.)\n• 特殊疑问句(W-Frage)：疑问词第一位，动词第二位！(Woher kommen Sie?)\n• 一般疑问句(Ja/Nein-Frage)：动词位于句首第一位！(Lernst du Deutsch?)"
                }
            ]
        },
        "quiz": [
            {
                "id": "A1_L01_Q1",
                "type": "GRAMMAR_FILL",
                "question": "请选出正确的动词变位：Woher ______ du? - Ich ______ aus Deutschland.",
                "options": ["kommst / komme", "kommt / komme", "kommen / kommt", "kommst / bin"],
                "correctIndex": 0,
                "explanation": "du 对应的词尾是 -st (kommst)；ich 对应的词尾是 -e (komme)。"
            },
            {
                "id": "A1_L01_Q2",
                "type": "EXAM_REAL",
                "question": "歌德A1初次见面礼貌问候：'Guten Tag! Freut mich.' 的意思是：",
                "options": ["你好！很高兴认识您。", "再见！明天见。", "早上好！我先走了。", "晚安！做个好梦。"],
                "correctIndex": 0,
                "explanation": "Guten Tag! Freut mich. 是德语国家初次见面最标准的礼貌问候语。"
            }
        ],
        "words": [
            ("hallo", "", "int.", "", "你好，喂", "Hallo, wie geht es dir?", "你好，你身体好吗？"),
            ("guten Morgen", "", "phrase", "", "早上好", "Guten Morgen, Herr Schmidt!", "早上好，施密特先生！"),
            ("guten Tag", "", "phrase", "", "你好，日安", "Guten Tag, wie kann ich helfen?", "你好，我能帮什么忙？"),
            ("guten Abend", "", "phrase", "", "晚上好", "Guten Abend allerseits!", "大家晚上好！"),
            ("gute Nacht", "", "phrase", "", "晚安", "Gute Nacht, schlaf gut!", "晚安，做个好梦！"),
            ("auf Wiedersehen", "", "phrase", "", "再见（正式面谈）", "Auf Wiedersehen und einen schönen Tag!", "再见，祝您一天愉快！"),
            ("auf Wiederhören", "", "phrase", "", "再见（电话通话）", "Auf Wiederhören, Frau Bauer!", "再见（挂电话），鲍尔女士！"),
            ("tschüss", "", "int.", "", "再见（口语熟人）", "Tschüss, bis morgen!", "拜拜，明天见！"),
            ("bis bald", "", "phrase", "", "回头见，待会见", "Tschüss, bis bald!", "再见，回头见！"),
            ("bis später", "", "phrase", "", "稍后见", "Wir sehen uns später, bis später!", "我们稍后见！"),
            ("bitte", "", "adv./int.", "", "请；不客气", "Ein Wasser, bitte!", "请来一杯水！"),
            ("danke", "", "int.", "", "谢谢", "Danke für Ihre Hilfe!", "谢谢您的帮助！"),
            ("vielen Dank", "", "phrase", "", "非常感谢", "Vielen Dank für die Einladung.", "非常感谢您的邀请。"),
            ("bitte schön", "", "phrase", "", "不客气，请", "Bitte schön, bedienen Sie sich!", "不客气，请自便！"),
            ("danke schön", "", "phrase", "", "多谢，非常感谢", "Danke schön für das Geschenk!", "非常感谢您的礼物！"),
            ("entschuldigen", "", "v.", "entschuldigt, entschuldigte, entschuldigt", "原谅，抱歉", "Entschuldigen Sie bitte die Störung!", "抱歉打扰您了！"),
            ("die Entschuldigung", "die", "n.", "-en", "抱歉，歉意", "Entschuldigung, wo ist der Bahnhof?", "抱歉请问，火车站怎么走？"),
            ("leid tun", "", "v.", "tut leid, tat leid, leidgetan", "感到遗憾抱歉", "Es tut mir sehr leid.", "我感到非常抱歉。"),
            ("der Name", "der", "n.", "-n", "名字，姓名", "Mein Name ist Peter.", "我的名字叫彼得。"),
            ("der Vorname", "der", "n.", "-n", "名", "Mein Vorname ist Thomas.", "我的名是托马斯。"),
            ("der Nachname", "der", "n.", "-n", "姓氏", "Wie ist Ihr Nachname?", "您的姓氏是什么？"),
            ("heißen", "", "v.", "heißt, hieß, geheißen", "名叫，称为", "Ich heiße Anna.", "我叫安娜。"),
            ("sein", "", "v.", "ist, war, ist gewesen", "是，存在", "Wir sind Studenten.", "我们是大学生。"),
            ("haben", "", "v.", "hat, hatte, gehabt", "有，拥有", "Ich habe eine Frage.", "我有一个问题。"),
            ("kommen", "", "v.", "kommt, kam, ist gekommen", "来，来自", "Woher kommen Sie?", "您来自哪里？"),
            ("wohnen", "", "v.", "wohnt, wohnte, gewohnt", "居住", "Ich wohne in Berlin.", "我住在柏林。"),
            ("leben", "", "v.", "lebt, lebte, gelebt", "生活，活着", "Er lebt in München.", "他生活在慕尼黑。"),
            ("sprechen", "", "v.", "spricht, sprach, gesprochen", "说，讲", "Sprechen Sie Englisch?", "您讲英语吗？"),
            ("die Sprache", "die", "n.", "-n", "语言", "Deutsch ist eine schöne Sprache.", "德语是一门优美的语言。"),
            ("das Deutsch", "das", "n.", "-", "德语", "Ich lerne jetzt Deutsch.", "我现在正在学德语。"),
            ("das Chinesisch", "das", "n.", "-", "汉语，中文", "Chinesisch ist meine Muttersprache.", "汉语是我的母语。"),
            ("das Englisch", "das", "n.", "-", "英语", "Er spricht sehr gut Englisch.", "他英语说得非常好。"),
            ("das Land", "das", "n.", "Länder", "国家；乡村", "Deutschland ist ein schönes Land.", "德国是个美丽的国家。"),
            ("das Deutschland", "das", "n.", "-", "德国", "Wir fliegen nach Deutschland.", "我们乘飞机去德国。"),
            ("das China", "das", "n.", "-", "中国", "Ich komme aus China.", "我来自中国。"),
            ("das Österreich", "das", "n.", "-", "奥地利", "Wien ist die Hauptstadt von Österreich.", "维也纳是奥地利的首都。"),
            ("die Schweiz", "die", "n.", "-", "瑞士", "Er wohnt in der Schweiz.", "他住在瑞士。"),
            ("das Frankreich", "das", "n.", "-", "法国", "Paris liegt in Frankreich.", "巴黎位于法国。"),
            ("das Italien", "das", "n.", "-", "意大利", "Rom ist eine alte Stadt in Italien.", "罗马是意大利的一座古老城市。"),
            ("das Spanien", "das", "n.", "-", "西班牙", "Wir machen Urlaub in Spanien.", "我们在西班牙度假。"),
            ("das Japan", "das", "n.", "-", "日本", "Tokio liegt in Japan.", "东京在日本。"),
            ("die USA", "die", "n.pl.", "-", "美国", "Er studiert in den USA.", "他在美国留学。"),
            ("neu", "", "adj.", "neuer, am neuesten", "新的", "Das ist mein neuer Kollege.", "这是我的新同事。"),
            ("alt", "", "adj.", "älter, am ältesten", "老的，旧的", "Wie alt bist du?", "你多大了？"),
            ("groß", "", "adj.", "größer, am größten", "大的，高大的", "Berlin ist eine große Stadt.", "柏林是一座大城市。"),
            ("klein", "", "adj.", "kleiner, am kleinsten", "小的", "Mein Zimmer ist klein aber fein.", "我的房间小但精致。"),
            ("wer", "", "pron.", "", "谁", "Wer ist das?", "那是谁？"),
            ("was", "", "pron.", "", "什么", "Was machen Sie beruflich?", "您从事什么职业？"),
            ("wie", "", "adv.", "", "怎样，如何", "Wie geht es Ihnen?", "您最近好吗？"),
            ("wo", "", "adv.", "", "在哪里", "Wo wohnen Sie jetzt?", "您现在住在哪里？"),
            ("woher", "", "adv.", "", "从哪里来", "Woher kommst du?", "你从哪里来？"),
            ("wohin", "", "adv.", "", "去哪里", "Wohin fährst du am Wochenende?", "你周末去哪儿？"),
            ("ja", "", "part.", "", "是的", "Ja, das stimmt genau.", "是的，完全正确。"),
            ("nein", "", "part.", "", "不，不是", "Nein, ich bin nicht müde.", "不，我不累。"),
            ("nicht", "", "adv.", "", "不，没有", "Das ist nicht schwer.", "这并不难。"),
            ("auch", "", "adv.", "", "也，同样", "Ich lerne auch Deutsch.", "我也在学德语。"),
            ("sehr", "", "adv.", "", "非常，很", "Vielen Dank, sehr nett von Ihnen!", "非常感谢，您真好！"),
            ("gut", "", "adj./adv.", "besser, am besten", "好的", "Das schmeckt wirklich gut.", "这尝起来真不错。"),
            ("schlecht", "", "adj./adv.", "schlechter, am schlechtesten", "坏的，差的", "Das Wetter ist heute schlecht.", "今天天气很差。"),
            ("der Herr", "der", "n.", "-en", "先生", "Guten Tag, Herr Müller!", "你好，穆勒先生！"),
            ("die Frau", "die", "n.", "-en", "女士，妻子", "Frau Weber ist Lehrerin.", "韦伯女士是教师。"),
            ("die Dame", "die", "n.", "-n", "女士，夫人", "Sehr geehrte Damen und Herren!", "尊敬的女士们、先生们！"),
            ("der Freund", "der", "n.", "-e", "男朋友，朋友", "Das ist mein bester Freund.", "这是我最好的朋友。"),
            ("die Freundin", "die", "n.", "-nen", "女朋友，女性朋友", "Meine Freundin lernt Medizin.", "我的女朋友学医。"),
            ("der Kollege", "der", "n.", "-n", "男同事", "Mein Kollege hilft mir gern.", "我的同事乐意帮我。"),
            ("die Kollegin", "die", "n.", "-nen", "女同事", "Sie ist eine nette Kollegin.", "她是一位和善的女同事。"),
            ("die Stadt", "die", "n.", "Städte", "城市", "München ist eine schöne Stadt.", "慕尼黑是一座美丽的城市。"),
            ("die Hauptstadt", "die", "n.", "Hauptstädte", "首都", "Berlin ist die Hauptstadt von Deutschland.", "柏林是德国首都。"),
            ("die Adresse", "die", "n.", "-n", "地址", "Wie ist deine Adresse?", "你的地址是什么？"),
            ("die Straße", "die", "n.", "-n", "街道", "Ich wohne in der Schillerstraße.", "我住在席勒街。")
        ]
    },

    # LESSON 2
    {
        "id": "A1_L02",
        "title": "第2课：家庭、亲属与称谓 (Familie & Verwandtschaft)",
        "summary": "掌握三性名词冠词系统(der/die/das)、复数规律、物主代词与否定词 kein/nicht",
        "grammar": {
            "title": "名词冠词系统与物主代词 (Possessivartikel)",
            "sections": [
                {
                    "heading": "1. 德语核心三性冠词（第一格 Nominativ）",
                    "content": "• 阳性 (Maskulinum): der Vater / ein Vater / kein Vater / mein Vater\n• 阴性 (Femininum): die Mutter / eine Mutter / keine Mutter / meine Mutter\n• 中性 (Neutrum): das Kind / ein Kind / kein Kind / mein Kind\n• 复数 (Plural): die Eltern / -- / keine Eltern / meine Eltern"
                },
                {
                    "heading": "2. 否定词 kein vs nicht 严格区别",
                    "content": "• kein: 只用于否定带有不定冠词或无冠词的名词！(Das ist kein Hund. Ich habe kein Geld.)\n• nicht: 否定动词、形容词、副词、带定冠词的名词及整个句子！(Ich arbeite nicht. Das Haus ist nicht groß.)"
                }
            ]
        },
        "quiz": [
            {
                "id": "A1_L02_Q1",
                "type": "ARTICLE",
                "question": "请选出名词 'Kind'（孩子）在第一格的定冠词：",
                "options": ["der", "die", "das", "den"],
                "correctIndex": 2,
                "explanation": "Kind 是中性名词，定冠词是 das (das Kind, die Kinder)。"
            },
            {
                "id": "A1_L02_Q2",
                "type": "GRAMMAR_FILL",
                "question": "请选出正确的否定词填空：Ich habe ______ Zeit (时间无冠词).",
                "options": ["keine", "nicht", "kein", "nein"],
                "correctIndex": 0,
                "explanation": "Zeit 是阴性名词（die Zeit），否定无冠词名词用 keine。"
            }
        ],
        "words": [
            ("die Familie", "die", "n.", "-n", "家庭，家族", "Meine Familie ist sehr groß.", "我的家庭很大。"),
            ("die Eltern", "die", "n.pl.", "-", "父母，双亲", "Meine Eltern wohnen auf dem Land.", "我的父母住在乡下。"),
            ("der Vater", "der", "n.", "Väter", "父亲", "Mein Vater liest gerne die Zeitung.", "我的父亲喜欢读报。"),
            ("die Mutter", "die", "n.", "Mütter", "母亲", "Meine Mutter backt am Sonntag Kuchen.", "我母亲周日烤蛋糕。"),
            ("das Kind", "das", "n.", "Kinder", "孩子，小孩", "Das Kind spielt fröhlich.", "孩子在快乐地玩耍。"),
            ("der Sohn", "der", "n.", "Söhne", "儿子", "Mein Sohn geht schon in die Schule.", "我的儿子已经在上学了。"),
            ("die Tochter", "die", "n.", "Töchter", "女儿", "Ihre Tochter studiert Jura in Bonn.", "她的女儿在波恩学法律。"),
            ("die Geschwister", "die", "n.pl.", "-", "兄弟姐妹", "Hast du Geschwister?", "你有兄弟姐妹吗？"),
            ("der Bruder", "der", "n.", "Brüder", "哥哥，弟弟", "Mein Bruder ist älter als ich.", "我的哥哥比我年长。"),
            ("die Schwester", "die", "n.", "-n", "姐姐，妹妹", "Meine Schwester wohnt in Wien.", "我的妹妹住在维也纳。"),
            ("die Großeltern", "die", "n.pl.", "-", "祖父母，外祖父母", "Ich besuche am Wochenende meine Großeltern.", "我周末去看望祖父母。"),
            ("der Großvater", "der", "n.", "Großväter", "祖父，外祖父", "Mein Großvater ist 80 Jahre alt.", "我祖父80岁了。"),
            ("der Opa", "der", "n.", "-s", "爷爷，外公（口语）", "Mein Opa erzählt tolle Geschichten.", "我爷爷讲的故事很精彩。"),
            ("die Großmutter", "die", "n.", "Großmütter", "祖母，外祖母", "Meine Großmutter kocht sehr lecker.", "我的祖母做饭很可口。"),
            ("die Oma", "die", "n.", "-s", "奶奶，外婆（口语）", "Liebe Oma, alles Gute zum Geburtstag!", "亲爱的奶奶，祝您生日快乐！"),
            ("das Enkelkind", "das", "n.", "-er", "孙子，孙女，外孙", "Die Großeltern lieben ihre Enkelkinder.", "祖父母深爱着他们的孙辈。"),
            ("der Enkel", "der", "n.", "-", "孙子，外孙", "Mein Enkel heißt Lukas.", "我的孙子名叫卢卡斯。"),
            ("die Enkelin", "die", "n.", "-nen", "孙女，外孙女", "Sie hat zwei Enkelinnen.", "她有两个孙女。"),
            ("der Onkel", "der", "n.", "-", "叔伯，舅舅，姑父", "Mein Onkel arbeitet bei Siemens.", "我的叔叔在西门子公司工作。"),
            ("die Tante", "die", "n.", "-n", "姑姑，姨妈，婶婶", "Tante Julia kommt morgen zu Besuch.", "茱莉亚阿姨明天来做客。"),
            ("der Cousin", "der", "n.", "-s", "堂兄弟，表兄弟", "Mein Cousin lebt in Frankfurt.", "我的表哥住在法兰克福。"),
            ("die Cousine", "die", "n.", "-n", "堂姐妹，表姐妹", "Meine Cousine ist Musikerin.", "我的表姐是一位音乐家。"),
            ("der Mann", "der", "n.", "Männer", "男人；丈夫", "Ihr Mann ist Arzt von Beruf.", "她的丈夫职业是医生。"),
            ("die Frau", "die", "n.", "-en", "女人；妻子", "Seine Frau arbeitet als Architektin.", "他的妻子从事建筑师工作。"),
            ("das Baby", "das", "n.", "-s", "婴儿，宝宝", "Das Baby schläft ruhig in der Wiege.", "婴儿在摇篮里安静地睡着。"),
            ("der Junge", "der", "n.", "-n", "男孩", "Die Jungen spielen Fußball im Hof.", "男孩们在院子里踢足球。"),
            ("das Mädchen", "das", "n.", "-", "女孩（中性名词）", "Das Mädchen liest ein Märchen.", "女孩正在读童话故事。"),
            ("der Mensch", "der", "n.", "-en", "人，人类", "Alle Menschen brauchen Liebe und Respekt.", "所有人都需要爱与尊重。"),
            ("die Leute", "die", "n.pl.", "-", "人们，大家", "Viele Leute warten am Bahnhof.", "许多人在火车站等候。"),
            ("die Person", "die", "n.", "-en", "人，人物，位", "Ein Tisch für vier Personen bitte!", "请给一张四人桌！"),
            ("leben", "", "v.", "lebt, lebte, gelebt", "生活，居住", "Sie leben schon lange zusammen.", "他们在一起生活很久了。"),
            ("lieben", "", "v.", "liebt, liebte, geliebt", "爱，热爱", "Eltern lieben ihre Kinder.", "父母爱他们的孩子。"),
            ("der Hund", "der", "n.", "-e", "狗", "Mein Hund heißt Bello.", "我的狗叫贝洛。"),
            ("die Katze", "die", "n.", "-n", "猫", "Die Katze schläft auf dem Sofa.", "猫睡在沙发上。"),
            ("das Haustier", "das", "n.", "-e", "宠物", "Haben Sie ein Haustier zu Hause?", "您家里养宠物了吗？"),
            ("besuchen", "", "v.", "besucht, besuchte, besucht", "拜访，看望", "Wir besuchen heute unsere Tante.", "我们今天去探望阿姨。"),
            ("helfen", "", "v.", "hilft, half, geholfen", "帮助 (接Dativ)", "Ich helfe meiner Mutter in der Küche.", "我在厨房帮母亲的忙。"),
            ("fragen", "", "v.", "fragt, fragte, gefragt", "询问，提问", "Das Kind fragt den Vater nach dem Weg.", "小孩向父亲问路。"),
            ("antworten", "", "v.", "antwortet, antwortete, geantwortet", "回答", "Er antwortet schnell auf meine Frage.", "他迅速回答了我的问题。"),
            ("kennen", "", "v.", "kennt, kannte, gekannt", "认识，了解", "Kennen Sie Herrn Müller persönlich?", "您亲自认识穆勒先生吗？"),
            ("jung", "", "adj.", "jünger, am jüngsten", "年轻的", "Er ist noch sehr jung.", "他还很年轻。"),
            ("alt", "", "adj.", "älter, am ältesten", "年老的", "Meine Großmutter ist sehr alt.", "我的祖母年纪很大了。"),
            ("nett", "", "adj.", "netter, am nettesten", "友善的，亲切的", "Deine Schwester ist wirklich nett.", "你的姐姐真的很和蔼。"),
            ("freundlich", "", "adj.", "freundlicher, am freundlichsten", "友好的", "Die Nachbarn sind sehr freundlich.", "邻居们非常友好。"),
            ("sympathisch", "", "adj.", "", "讨人喜欢的，令人有好感的", "Unser neuer Lehrer ist sehr sympathisch.", "我们的新老师非常有亲和力。"),
            ("glücklich", "", "adj.", "glücklicher, am glücklichsten", "幸福的，高兴的", "Sie führen ein glückliches Leben.", "他们过着幸福的生活。"),
            ("traurig", "", "adj.", "trauriger, am traurigsten", "伤心的，难过的", "Warum bist du heute so traurig?", "你今天为什么这么难过？"),
            ("das Foto", "das", "n.", "-s", "照片", "Hier ist ein Foto von meiner Familie.", "这是一张我的全家福。"),
            ("zeigen", "", "v.", "zeigt, zeigte, gezeigt", "展示，出示", "Zeig mir bitte deine neuen Fotos!", "请给我看你的新照片！"),
            ("sehen", "", "v.", "sieht, sah, gesehen", "看见，看", "Siehst du den Mann dort drüben?", "你看到那边那个男人了吗？"),
            ("zusammen", "", "adv.", "", "一起，共同", "Wir lernen jeden Abend zusammen.", "我们每天晚上一起学习。"),
            ("allein", "", "adj./adv.", "", "独自一人", "Er wohnt ganz allein in der Stadt.", "他独自一人住在城里。"),
            ("alle", "", "pron.", "", "所有人，全部", "Alle Kinder freuen sich auf die Ferien.", "所有孩子都期盼着假期。"),
            ("viele", "", "pron./adj.", "", "许多，很多", "In Deutschland leben viele Ausländer.", "在德国生活着很多外国人。"),
            ("wenige", "", "pron./adj.", "", "少数，很少的", "Nur wenige Menschen kennen die Antwort.", "只有极少数人知道答案。"),
            ("mein", "", "poss.", "", "我的", "Das ist mein neuer Computer.", "这是我的新电脑。"),
            ("dein", "", "poss.", "", "你的", "Ist das dein Fahrrad?", "这是你的自行车吗？"),
            ("sein", "", "poss.", "", "他的，它的", "Sein Vater ist Ingenieur.", "他的父亲是工程师。"),
            ("ihr", "", "poss.", "", "她的；他们的", "Ihr Bruder wohnt in München.", "她的哥哥住在慕尼黑。"),
            ("unser", "", "poss.", "", "我们的", "Unser Haus ist hell und gemütlich.", "我们的房子采光好且舒适。"),
            ("euer", "", "poss.", "", "你们的", "Wo ist euer Auto geparkt?", "你们的车停在哪儿了？"),
            ("Ihr", "", "poss.", "", "您的，您各位的（尊称）", "Wie lautet Ihre Adresse, Frau Berg?", "贝尔格女士，您的地址是什么？"),
            ("die Nummer", "die", "n.", "-n", "号码", "Das ist meine private Nummer.", "这是我的私人号码。"),
            ("rufen", "", "v.", "ruft, rief, gerufen", "呼唤，叫喊", "Die Mutter ruft die Kinder zum Essen.", "母亲叫孩子们来吃饭。"),
            ("heiraten", "", "v.", "heiratet, heiratete, geheiratet", "结婚", "Sie möchten im nächsten Sommer heiraten.", "他们想在明年夏天结婚。"),
            ("die Hochzeit", "die", "n.", "-en", "婚礼", "Wir sind zu einer Hochzeit eingeladen.", "我们受邀参加一场婚礼。"),
            ("geboren", "", "adj./part.", "", "出生的", "Ich bin im Jahr 2000 geboren.", "我出生于2000年。"),
            ("sterben", "", "v.", "stirbt, starb, ist gestorben", "死亡，逝世", "Sein Urgroßvater starb vor vielen Jahren.", "他的曾祖父多年前去世了。"),
            ("das Alter", "das", "n.", "-", "年龄", "In welchem Alter lernt man eine Fremdsprache am besten?", "在什么年龄学外语最好？"),
            ("die Jugend", "die", "n.", "-", "青年时代；青年人", "Er verbrachte seine Jugend in Hamburg.", "他在汉堡度过了青年时代。")
        ]
    },

    # LESSON 3
    {
        "id": "A1_L03",
        "title": "第3课：食材、餐饮与超市采购 (Essen & Supermarkt)",
        "summary": "掌握第四格宾格(Akkusativ)、情态动词 möchten、食材分类与采购计价",
        "grammar": {
            "title": "第四格 (Akkusativ) 冠词变化法则",
            "sections": [
                {
                    "heading": "1. 第四格冠词变化铁律",
                    "content": "第四格中【仅阳性改变】：der -> den, ein -> einen, kein -> keinen。\n阴性(die/eine)、中性(das/ein)、复数(die/keine)完全保持不变！"
                },
                {
                    "heading": "2. 情态动词 möchten 表达想要",
                    "content": "ich möchte, du möchtest, er möchte, wir möchten, ihr möchtet, sie möchten。\n例：Ich möchte einen Apfel kaufen."
                }
            ]
        },
        "quiz": [
            {
                "id": "A1_L03_Q1",
                "type": "GRAMMAR_FILL",
                "question": "Ich kaufe ______ (der Apfel, 第四格宾语).",
                "options": ["den Apfel", "der Apfel", "dem Apfel", "des Apfels"],
                "correctIndex": 0,
                "explanation": "阳性名词在第四格中定冠词由 der 变为 den。"
            },
            {
                "id": "A1_L03_Q2",
                "type": "ARTICLE",
                "question": "食材名词 'Brot'（面包）的定冠词是：",
                "options": ["der", "die", "das", "den"],
                "correctIndex": 2,
                "explanation": "Brot 是中性名词，定冠词是 das (das Brot)。"
            }
        ],
        "words": [
            ("das Essen", "das", "n.", "-", "食物，饮食", "Das Essen schmeckt hervorragend.", "这食物味道好极了。"),
            ("das Lebensmittel", "das", "n.", "-", "食品，食材", "Wir kaufen frische Lebensmittel auf dem Markt.", "我们在市场上买新鲜食品。"),
            ("der Supermarkt", "der", "n.", "Supermärkte", "超市", "Der Supermarkt öffnet um 8 Uhr.", "超市早晨8点开门。"),
            ("der Markt", "der", "n.", "Märkte", "集市，市场", "Samstags gehen wir immer auf den Markt.", "周六我们总是去集市。"),
            ("kaufen", "", "v.", "kauft, kaufte, gekauft", "购买", "Ich kaufe heute Obst und Gemüse.", "我今天买水果和蔬菜。"),
            ("verkaufen", "", "v.", "verkauft, verkaufte, verkauft", "卖，售卖", "Der Bauer verkauft frische Eier.", "农夫在卖新鲜鸡蛋。"),
            ("kosten", "", "v.", "kostet, kostete, gekostet", "花费，价格为", "Wie viel kostet ein Kilo Tomaten?", "一公斤西红柿多少钱？"),
            ("der Preis", "der", "n.", "-e", "价格", "Die Preise im Supermarkt sind günstig.", "超市的价格很实惠。"),
            ("das Geld", "das", "n.", "-", "钱，金钱", "Ich habe leider nicht genug Geld dabei.", "可惜我身上没带够钱。"),
            ("der Euro", "der", "n.", "-s", "欧元", "Das Buch kostet 15 Euro.", "这本书售价15欧元。"),
            ("der Cent", "der", "n.", "-s", "欧分", "Fünfzig Cent Rückgeld, bitte.", "请收好找回的50欧分。"),
            ("billig", "", "adj.", "billiger, am billigsten", "便宜的", "Äpfel sind hier sehr billig.", "这里的苹果很便宜。"),
            ("teuer", "", "adj.", "teurer, am teuersten", "昂贵的", "Das Fleisch ist ziemlich teuer.", "这块肉相当贵。"),
            ("frisch", "", "adj.", "frischer, am frischesten", "新鲜的", "Hier gibt es frisches Brot.", "这里有新鲜面包。"),
            ("das Obst", "das", "n.", "-", "水果（总称）", "Obst ist sehr gesund.", "水果非常有益健康。"),
            ("das Gemüse", "das", "n.", "-", "蔬菜（总称）", "Kinder sollten viel Gemüse essen.", "孩子们应该多吃蔬菜。"),
            ("der Apfel", "der", "n.", "Äpfel", "苹果", "Ein Apfel am Tag hält gesund.", "一天一苹果，医生远离我。"),
            ("die Banane", "die", "n.", "-n", "香蕉", "Ich esse zum Frühstück eine Banane.", "我早餐吃一根香蕉。"),
            ("die Orange", "die", "n.", "-n", "橙子", "Orangen enthalten viel Vitamin C.", "橙子富含维生素C。"),
            ("die Zitrone", "die", "n.", "-n", "柠檬", "Zitronen sind sehr sauer.", "柠檬非常酸。"),
            ("die Tomate", "die", "n.", "-n", "西红柿，番茄", "Tomaten für die Sauce schneiden.", "把番茄切碎做酱汁。"),
            ("die Kartoffel", "die", "n.", "-n", "土豆，马铃薯", "Kartoffeln sind in Deutschland sehr beliebt.", "土豆在德国非常受欢迎。"),
            ("die Zwiebel", "die", "n.", "-n", "洋葱", "Beim Zwiebelschneiden weine ich oft.", "切洋葱时我经常流泪。"),
            ("der Salat", "der", "n.", "-e", "沙拉；生菜", "Möchtest du einen grünen Salat dazu?", "你想配一份蔬菜沙拉吗？"),
            ("das Brot", "das", "n.", "-e", "面包", "Deutsches Brot hat eine feste Kruste.", "德国面包有一层硬硬的外皮。"),
            ("das Brötchen", "das", "n.", "-", "小面包", "Am Sonntag hole ich frische Brötchen.", "周日我去买新鲜小面包。"),
            ("die Butter", "die", "n.", "-", "黄油", "Ich streiche Butter auf das Brot.", "我把黄油抹在面包上。"),
            ("der Käse", "der", "n.", "-", "奶酪，芝士", "Gouda ist ein bekannter Käse.", "高达是一种著名的奶酪。"),
            ("die Wurst", "die", "n.", "Würste", "香肠", "Bratwurst ist eine Spezialität.", "煎香肠是一道特色菜。"),
            ("das Fleisch", "das", "n.", "-", "肉，肉类", "Isst du gerne Schweinefleisch?", "你喜欢吃猪肉吗？"),
            ("das Rindfleisch", "das", "n.", "-", "牛肉", "Das Rindfleisch schmeckt zart.", "这块牛肉尝起来很嫩。"),
            ("das Schweinefleisch", "das", "n.", "-", "猪肉", "Schweinefleisch wird oft gebraten.", "猪肉经常用来煎烤。"),
            ("das Hähnchen", "das", "n.", "-", "童子鸡，鸡肉", "Wir essen heute gebratenes Hähnchen.", "我们今天吃烤鸡。"),
            ("der Fisch", "der", "n.", "-e", "鱼，鱼肉", "Freitags essen viele Deutschen Fisch.", "周五很多德国人吃鱼。"),
            ("das Ei", "das", "n.", "-er", "鸡蛋，蛋", "Ich koche mir zwei weiche Eier.", "我给自己煮了两个溏心蛋。"),
            ("die Milch", "die", "n.", "-", "牛奶", "Kaffee mit Milch und Zucker bitte.", "请加牛奶和糖的咖啡。"),
            ("der Joghurt", "der", "n.", "-s", "酸奶", "Naturjoghurt mit Honig schmeckt gut.", "原味酸奶配蜂蜜很好吃。"),
            ("das Wasser", "das", "n.", "-", "水", "Ich trinke zwei Liter Wasser am Tag.", "我一天喝两升水。"),
            ("das Mineralwasser", "das", "n.", "-", "矿泉水", "Mit oder ohne Kohlensäure?", "带气还是不带气矿泉水？"),
            ("der Saft", "der", "n.", "Säfte", "果汁", "Orangensaft ist erfrischend.", "橙汁非常清爽提神。"),
            ("der Apfelsaft", "der", "n.", "Apfelsäfte", "苹果汁", "Eine Apfelschorle bitte!", "请来一杯苹果汽水！"),
            ("das Bier", "das", "n.", "-e", "啤酒", "In Bayern trinkt man gern Bier.", "在巴伐利亚人们爱喝啤酒。"),
            ("der Wein", "der", "n.", "-e", "葡萄酒", "Ein Glas Rotwein zum Abendessen.", "晚餐喝一杯红葡萄酒。"),
            ("der Tee", "der", "n.", "-s", "茶", "Im Winter trinke ich heißen Tee.", "冬天我喝热茶。"),
            ("der Kaffee", "der", "n.", "-s", "咖啡", "Morgens brauche ich eine Tasse Kaffee.", "早晨我需要一杯咖啡。"),
            ("der Zucker", "der", "n.", "-", "糖", "Nehmen Sie Zucker in den Tee?", "您在茶里加糖吗？"),
            ("das Salz", "das", "n.", "-", "盐", "Die Suppe braucht noch etwas Salz.", "这碗汤还需要一点盐。"),
            ("der Pfeffer", "der", "n.", "-", "胡椒", "Mit Salz und Pfeffer würzen.", "用盐和胡椒调味。"),
            ("das Öl", "das", "n.", "-e", "油，植物油", "Olivenöl ist gut für den Salat.", "橄榄油很适合拌沙拉。"),
            ("der Essig", "der", "n.", "-e", "醋", "Essig und Öl stehen auf dem Tisch.", "醋和油摆在桌上。"),
            ("der Reis", "der", "n.", "-", "米饭，大米", "In Asien isst man täglich Reis.", "在亚洲人们每天吃米饭。"),
            ("die Nudel", "die", "n.", "-n", "面条，意面", "Nudeln mit Tomatensauce kochen.", "煮番茄酱意大利面。"),
            ("die Suppe", "die", "n.", "-n", "汤", "Die Hühnersuppe wärmt gut auf.", "鸡汤很暖胃。"),
            ("der Kuchen", "der", "n.", "-", "蛋糕", "Am Nachmittag essen wir Kuchen.", "下午我们吃蛋糕。"),
            ("die Schokolade", "die", "n.", "-n", "巧克力", "Dunkle Schokolade ist gesund.", "黑巧克力有益健康。"),
            ("das Eis", "das", "n.", "-", "冰淇淋；冰", "Kinder lieben Schokoladeneis.", "孩子们喜爱巧克力冰淇淋。"),
            ("der Honig", "der", "n.", "-", "蜂蜜", "Honig schmeckt süß und cremig.", "蜂蜜尝起来甜美细腻。"),
            ("die Marmelade", "die", "n.", "-n", "果酱", "Erdbeermarmelade aufs Brot streichen.", "把草莓果酱抹在面包上。"),
            ("das Kilo", "das", "n.", "-s", "公斤，千克", "Ein Kilo Äpfel kostet zwei Euro.", "一公斤苹果售价两欧元。"),
            ("das Gramm", "das", "n.", "-e", "克", "Ich brauche 200 Gramm Käse.", "我需要200克奶酪。"),
            ("der Liter", "der", "n.", "-", "升", "Ein Liter Milch bitte!", "请来一升牛奶！"),
            ("die Packung", "die", "n.", "-en", "盒，包装包", "Eine Packung Nudeln bitte.", "请给我一包意面。"),
            ("die Flasche", "die", "n.", "-n", "瓶子，一瓶", "Zwei Flaschen Mineralwasser bitte.", "请来两瓶矿泉水。"),
            ("die Dose", "die", "n.", "-n", "罐头，易拉罐", "Eine Dose Tomaten öffnen.", "打开一罐番茄罐头。"),
            ("die Tüte", "die", "n.", "-n", "袋子，购物塑料袋", "Brauchen Sie eine Plastiktüte?", "您需要一个塑料袋吗？"),
            ("der Einkaufswagen", "der", "n.", "-", "购物车", "Man braucht eine Münze für den Wagen.", "用购物车需要一枚硬币。"),
            ("die Kasse", "die", "n.", "-n", "收银台，付款处", "Bezahlen Sie bitte an Kasse zwei.", "请到二号收银台结账。"),
            ("die Quittung", "die", "n.", "-en", "收据，发票", "Möchten Sie den Kassenzettel haben?", "您需要收银小票吗？"),
            ("der Kunde", "der", "n.", "-n", "顾客，客户", "Der Kunde wird freundlich bedient.", "顾客受到热情的接待。"),
            ("die Verkäuferin", "die", "n.", "-nen", "女售货员", "Die Verkäuferin berät die Kundin.", "女售货员在为顾客提供咨询。")
        ]
    },

    # LESSON 4
    {
        "id": "A1_L04",
        "title": "第4课：餐厅点餐与就餐文化 (Im Restaurant & Mahlzeiten)",
        "summary": "掌握餐厅点餐句型、餐具词汇、买单表达与日常就餐用语",
        "grammar": {
            "title": "点餐交际用语与尊称命令式",
            "sections": [
                {
                    "heading": "1. 餐厅点餐黄金句型",
                    "content": "• Ich nehme... (我要一份...)\n• Ich möchte bitte... (我想要...)\n• Bringen Sie mir bitte... (请给我拿...)\n• Wir möchten bitte zahlen/bezahlen. (我们想要结账买单。)\n• Zusammen oder getrennt? (一起付还是分开付？)"
                },
                {
                    "heading": "2. 赞美食物与就餐寒暄",
                    "content": "• Guten Appetit! (祝您好胃口！)\n• Danke, gleichfalls! (谢谢，您也一样！)\n• Prost! / Zum Wohl! (干杯！/ 祝您健康！)\n• Das schmeckt sehr gut / lecker! (这味道真好/真美味！)"
                }
            ]
        },
        "quiz": [
            {
                "id": "A1_L04_Q1",
                "type": "EXAM_REAL",
                "question": "在德国餐厅用餐完毕想要买单，最得体的表达是：",
                "options": ["Zahlen, bitte!", "Ich habe kein Geld!", "Gehen wir!", "Wo ist das Essen?"],
                "correctIndex": 0,
                "explanation": "Zahlen, bitte!（请结账）是德语餐厅最常用、最得体的买单口语。"
            },
            {
                "id": "A1_L04_Q2",
                "type": "VOCAB_MEANING",
                "question": "就餐前德国人互相道祝福“祝你好胃口”，德语是：",
                "options": ["Guten Appetit!", "Gute Nacht!", "Guten Tag!", "Viel Glück!"],
                "correctIndex": 0,
                "explanation": "Guten Appetit! 是用餐时地道的好胃口祝福。"
            }
        ],
        "words": [
            ("das Restaurant", "das", "n.", "-s", "餐馆，饭店", "Wir gehen heute ins Restaurant.", "我们今天去餐馆吃饭。"),
            ("das Café", "das", "n.", "-s", "咖啡馆", "Treffen wir uns im Café!", "我们在咖啡馆碰面吧！"),
            ("die Kneipe", "die", "n.", "-n", "酒馆，小酒吧", "Nach der Arbeit gehen sie in die Kneipe.", "下班后他们去小酒馆喝一杯。"),
            ("der Kellner", "der", "n.", "-", "男服务员", "Der Kellner bringt die Speisekarte.", "服务员拿来了菜单。"),
            ("die Kellnerin", "die", "n.", "-nen", "女服务员", "Die Kellnerin nimmt die Bestellung auf.", "女服务员记录下点单。"),
            ("der Gast", "der", "n.", "Gäste", "客人，宾客", "Die Gäste sitzen draußen auf der Terrasse.", "客人们坐在外面的露台上。"),
            ("die Speisekarte", "die", "n.", "-n", "菜单", "Könnten wir bitte die Karte sehen?", "请问我们能看下菜单吗？"),
            ("die Getränkekarte", "die", "n.", "-n", "饮品单", "Auf der Getränkekarte gibt es Bier und Wein.", "酒水单上有啤酒和红酒。"),
            ("das Gericht", "das", "n.", "-e", "菜肴，菜品", "Welches Gericht empfehlen Sie uns?", "您向我们推荐哪道菜？"),
            ("die Vorspeise", "die", "n.", "-n", "开胃前菜", "Als Vorspeise nehme ich eine Suppe.", "前菜我点一份汤。"),
            ("das Hauptgericht", "das", "n.", "-e", "主菜", "Das Hauptgericht ist Rinderbraten.", "主菜是烤牛肉。"),
            ("das Dessert", "das", "n.", "-s", "甜品，甜点", "Möchten Sie noch ein Dessert bestellen?", "您还想点一份甜点吗？"),
            ("die Nachspeise", "die", "n.", "-n", "餐后甜点", "Als Nachspeise gibt es Apfelstrudel.", "餐后甜点是苹果卷。"),
            ("bestellen", "", "v.", "bestellt, bestellte, bestellt", "订购，点餐", "Wir möchten jetzt gerne bestellen.", "我们现在想点餐了。"),
            ("nehmen", "", "v.", "nimmt, nahm, genommen", "拿，要（某菜）", "Ich nehme das Wiener Schnitzel.", "我要一份维也纳炸小牛排。"),
            ("empfehlen", "", "v.", "empfiehlt, empfahl, empfohlen", "推荐", "Was können Sie uns heute empfehlen?", "您今天有什么向我们推荐的吗？"),
            ("bringen", "", "v.", "bringt, brachte, gebracht", "带来，拿来", "Bringen Sie mir bitte ein Glas Wasser!", "请给我拿一杯水！"),
            ("zahlen", "", "v.", "zahlt, zahlte, gezahlt", "付款，买单", "Herr Ober, wir möchten bitte zahlen!", "服务员，我们想结账！"),
            ("bezahlen", "", "v.", "bezahlt, bezahlte, bezahlt", "支付，结账", "Kann ich mit Kreditkarte bezahlen?", "我能用信用卡付款吗？"),
            ("getrennt", "", "adj./adv.", "", "分开地（AA制）", "Wir möchten bitte getrennt zahlen.", "我们想分开结账。"),
            ("zusammen", "", "adv.", "", "一起地（统结）", "Zusammen oder getrennt zahlen?", "一起付还是分开付？"),
            ("das Trinkgeld", "das", "n.", "-er", "小费", "In Deutschland gibt man Trinkgeld.", "在德国通常会给小费。"),
            ("stimmen", "", "v.", "stimmt, stimmte, gestimmt", "符合，正确", "Stimmt so, danke! (不用找零钱了)", "不用找零了，谢谢！"),
            ("der Tisch", "der", "n.", "-e", "桌子，餐桌", "Ein Tisch für zwei Personen bitte.", "请安排一张两人桌。"),
            ("reservieren", "", "v.", "reserviert, reservierte, reserviert", "预订，保留", "Haben Sie einen Tisch reserviert?", "您预订了餐桌吗？"),
            ("die Reservierung", "die", "n.", "-en", "预订", "Ich habe eine Reservierung auf den Namen Müller.", "我以穆勒的名字订了位。"),
            ("frei", "", "adj.", "freier, am freiesten", "空闲的，自由的", "Ist dieser Platz hier noch frei?", "这个座位还空着吗？"),
            ("besetzt", "", "adj.", "", "有人占用的", "Entschuldigung, dieser Platz ist besetzt.", "抱歉，这个座位有人了。"),
            ("das Besteck", "das", "n.", "-e", "餐具（刀叉匙总称）", "Hier fehlt noch ein Besteck.", "这里还缺一套餐具。"),
            ("die Gabel", "die", "n.", "-n", "叉子", "Ich esse die Pasta mit der Gabel.", "我用叉子吃意大利面。"),
            ("das Messer", "das", "n.", "-", "餐刀", "Das Messer schneidet sehr gut.", "这把刀切起来很锋利。"),
            ("der Löffel", "der", "n.", "-", "勺子，调羹", "Ich brauche einen Löffel für die Suppe.", "我需要一个喝汤的勺子。"),
            ("der Teller", "der", "n.", "-", "盘子，碟子", "Der Teller ist sehr heiß.", "这个盘子非常烫。"),
            ("die Tasse", "die", "n.", "-n", "茶杯，咖啡杯", "Eine Tasse Kaffee bitte!", "请来一杯咖啡！"),
            ("das Glas", "das", "n.", "Gläser", "玻璃杯", "Ein Glas Weißwein bitte.", "请来一杯白葡萄酒。"),
            ("die Serviette", "die", "n.", "-n", "餐巾纸，餐巾", "Bringen Sie mir eine Serviette bitte.", "请给我拿一张餐巾纸。"),
            ("das Frühstück", "das", "n.", "-e", "早餐", "Das Frühstück ist im Preis inbegriffen.", "早餐包含在房费中。"),
            ("das Mittagessen", "das", "n.", "-", "午餐", "Um 12 Uhr gibt es Mittagessen.", "中午12点吃午饭。"),
            ("das Abendessen", "das", "n.", "-", "晚餐", "Was essen wir heute zum Abendessen?", "今天晚饭我们吃什么？"),
            ("frühstücken", "", "v.", "frühstückt, frühstückte, gefrühstückt", "吃早餐", "Am Wochenende frühstücken wir spät.", "周末我们很晚才吃早餐。"),
            ("essen", "", "v.", "isst, aß, gegessen", "吃", "Er isst sehr gerne Pizza.", "他很喜欢吃披萨。"),
            ("trinken", "", "v.", "trinkt, trank, getrunken", "喝，饮用", "Was möchtest du trinken?", "你想喝点什么？"),
            ("schmecken", "", "v.", "schmeckt, schmeckte, geschmeckt", "尝起来，味道如何", "Wie schmeckt Ihnen das Essen?", "您觉得菜的味道怎么样？"),
            ("lecker", "", "adj.", "leckerer, am leckersten", "好吃的，美味的", "Der Schokoladenkuchen ist sehr lecker.", "巧克力蛋糕非常好吃。"),
            ("süß", "", "adj.", "süßer, am süßesten", "甜的", "Der Apfel ist saftig und süß.", "这个苹果多汁且香甜。"),
            ("salzig", "", "adj.", "salziger, am salzigsten", "咸的", "Die Suppe ist ein bisschen zu salzig.", "这碗汤有点太咸了。"),
            ("sauer", "", "adj.", "saurer, am sauersten", "酸的", "Die Zitrone schmeckt sauer.", "柠檬尝起来很酸。"),
            ("bitter", "", "adj.", "bitterer, am bittersten", "苦的", "Schwarzer Kaffee schmeckt oft bitter.", "黑咖啡尝起来往往发苦。"),
            ("scharf", "", "adj.", "schärfer, am schärfsten", "辣的，辛辣的", "Chinesisches Essen ist manchmal scharf.", "中国菜有时比较辣。"),
            ("heiß", "", "adj.", "heißer, am heißesten", "滚烫的，炎热的", "Vorsicht, der Tee ist noch sehr heiß!", "小心，茶还非常烫！"),
            ("kalt", "", "adj.", "kälter, am kältesten", "冷的，凉的", "Im Sommer trinke ich kaltes Wasser.", "夏天我喝凉水。"),
            ("warm", "", "adj.", "wärmer, am wärmsten", "温暖的，温热的", "Möchten Sie eine warme Mahlzeit?", "您想要一份热乎饭菜吗？"),
            ("voll", "", "adj.", "voller, am vollsten", "满的，吃饱的", "Das Restaurant ist heute ganz voll.", "今天餐馆全坐满了。"),
            ("satt", "", "adj.", "", "吃饱的", "Danke, ich bin schon ganz satt!", "谢谢，我已经吃得非常饱了！"),
            ("der Hunger", "der", "n.", "-", "饥饿", "Ich habe großen Hunger.", "我肚子很饿。"),
            ("der Durst", "der", "n.", "-", "口渴", "Hast du Durst? Hier ist Wasser.", "你口渴吗？这里有水。"),
            ("hungrig", "", "adj.", "hungriger, am hungrigsten", "饥饿的", "Die Kinder kommen hungrig nach Hause.", "孩子们饥肠辘辘地回到家。"),
            ("durstig", "", "adj.", "durstiger, am durstigsten", "口渴的", "Nach dem Sport bin ich durstig.", "运动后我很口渴。"),
            ("vegetarisch", "", "adj.", "", "素食的", "Gibt es auch vegetarische Gerichte?", "这里有素食菜肴吗？"),
            ("vegan", "", "adj.", "", "全素的，纯素的", "Ich lebe seit einem Jahr vegan.", "我吃纯素一年了。"),
            ("das Schnitzel", "das", "n.", "-", "炸肉排", "Schnitzel mit Pommes frites bestellen.", "点一份炸肉排配薯条。"),
            ("die Pommes", "die", "n.pl.", "-", "炸薯条", "Eine Portion Pommes bitte!", "请来一份炸薯条！"),
            ("das Hähnchen", "das", "n.", "-", "烤鸡", "Halbes Hähnchen mit Brot.", "半只烤鸡配面包。"),
            ("die Pizza", "die", "n.", "Pizzen", "披萨", "Eine Pizza Margherita bitte.", "请来一份玛格丽特披萨。"),
            ("die Pasta", "die", "n.", "-", "意面", "Frische Pasta schmeckt wunderbar.", "新鲜意面味道绝佳。"),
            ("die Rechnung", "die", "n.", "-en", "账单", "Die Rechnung bitte!", "请拿账单来！"),
            ("kochen", "", "v.", "kocht, kochte, gekocht", "烹饪，做饭", "Mein Vater kocht am Sonntag gerne.", "我父亲喜欢在周日做饭。"),
            ("braten", "", "v.", "brät, briet, gebraten", "煎，炸，烤", "Den Fisch in der Pfanne braten.", "在平底锅里煎鱼。"),
            ("backen", "", "v.", "bäckt, backte, gebacken", "烘焙，烤制", "Oma bäckt frischen Kuchen.", "奶奶正在烘烤新鲜蛋糕。"),
            ("die Bar", "die", "n.", "-s", "酒吧，吧台", "Wir trinken nach dem Essen noch etwas an der Bar.", "饭后我们在吧台再喝点东西。")
        ]
    },

    # LESSON 5
    {
        "id": "A1_L05",
        "title": "第5课：居住房型、租房与家具 (Wohnen, Wohnung & Möbel)",
        "summary": "掌握第三格与格(Dativ)基础、房型格局、家具词汇与看房咨询",
        "grammar": {
            "title": "第三格 (Dativ) 与居住方位介词",
            "sections": [
                {
                    "heading": "1. 第三格冠词变化表",
                    "content": "• 阳性 (Maskulinum): der -> dem / einem / keinem / meinem\n• 阴性 (Femininum): die -> der / einer / keiner / meiner\n• 中性 (Neutrum): das -> dem / einem / keinem / meinem\n• 复数 (Plural): die -> den / -- / keinen / meinen (+n词尾)\n口诀：阳中同 dem，阴变 der，复数带 den 词尾补 n！"
                },
                {
                    "heading": "2. 固定接第三格的常用介词",
                    "content": "mit, nach, von, zu, aus, bei, seit。\n例：Ich wohne bei meinen Eltern. / Er fährt mit dem Bus."
                }
            ]
        },
        "quiz": [
            {
                "id": "A1_L05_Q1",
                "type": "GRAMMAR_FILL",
                "question": "Ich fahre mit ______ (der Zug, 介词 mit 接第三格) nach Berlin.",
                "options": ["dem Zug", "den Zug", "der Zug", "des Zuges"],
                "correctIndex": 0,
                "explanation": "mit 支配第三格，阳性名词 der Zug 变为 dem Zug。"
            },
            {
                "id": "A1_L05_Q2",
                "type": "ARTICLE",
                "question": "家具名词 'Sofa'（沙发）在德语中的定冠词是：",
                "options": ["der", "die", "das", "den"],
                "correctIndex": 2,
                "explanation": "Sofa 是中性名词，定冠词是 das (das Sofa)。"
            }
        ],
        "words": [
            ("das Haus", "das", "n.", "Häuser", "房屋，房子", "Wir wohnen in einem kleinen Haus.", "我们住在一所小房子里。"),
            ("die Wohnung", "die", "n.", "-en", "公寓，住宅", "Sie sucht eine 3-Zimmer-Wohnung.", "她在找一套三居室公寓。"),
            ("das Zimmer", "das", "n.", "-", "房间，屋子", "Mein Zimmer hat ein großes Fenster.", "我的房间有一扇大窗户。"),
            ("das Wohnzimmer", "das", "n.", "-", "客厅，起居室", "Im Wohnzimmer steht ein gemütliches Sofa.", "客厅里放着一张舒适的沙发。"),
            ("das Schlafzimmer", "das", "n.", "-", "卧室", "Das Schlafzimmer liegt sehr ruhig.", "卧室环境非常安静。"),
            ("die Küche", "die", "n.", "-n", "厨房", "In der Küche kochen wir zusammen.", "我们在厨房里一起做饭。"),
            ("das Badezimmer", "das", "n.", "-", "浴室，卫生间", "Das Badezimmer hat eine Dusche.", "浴室里配有淋浴。"),
            ("das Bad", "das", "n.", "Bäder", "浴室", "Ich nehme ein warmes Bad.", "我泡一个热水澡。"),
            ("die Toilette", "die", "n.", "-n", "厕所，盥洗室", "Wo ist bitte die Toilette?", "请问洗手间在哪里？"),
            ("das WC", "das", "n.", "-s", "抽水马桶，洗手间", "Das WC ist am Ende des Flurs.", "洗手间在走廊尽头。"),
            ("der Flur", "der", "n.", "-e", "走廊，过道，玄关", "Hänge deine Jacke im Flur auf!", "把你的外套挂在玄关处！"),
            ("der Balkon", "der", "n.", "-e", "阳台", "Im Sommer frühstücken wir auf dem Balkon.", "夏天我们在阳台上吃早餐。"),
            ("die Terrasse", "die", "n.", "-n", "露台，平台", "Wir sitzen abends auf der Terrasse.", "晚上我们坐在露台上。"),
            ("der Garten", "der", "n.", "Gärten", "花园，院子", "Im Garten blühen schöne Rosen.", "花园里盛开着美丽的玫瑰。"),
            ("der Keller", "der", "n.", "-", "地下室", "Die Fahrräder stehen im Keller.", "自行车停在地下室里。"),
            ("die Garage", "die", "n.", "-n", "车库", "Das Auto steht sicher in der Garage.", "车安全地停在车库里。"),
            ("die Miete", "die", "n.", "-n", "房租，租金", "Wie hoch ist die monatliche Miete?", "每月房租是多少？"),
            ("die Warmmiete", "die", "n.", "-n", "暖租（含物业暖气费）", "Die Warmmiete beträgt 850 Euro.", "暖租一共是850欧元。"),
            ("die Kaltmiete", "die", "n.", "-n", "冷租（净租金）", "Die Kaltmiete ist 700 Euro.", "冷租是700欧元。"),
            ("die Nebenkosten", "die", "n.pl.", "-", "附加费用，物业暖气水电费", "Nebenkosten sind extra zu zahlen.", "物业附加费需要另算。"),
            ("die Kaution", "die", "n.", "-en", "押金", "Die Kaution beträgt drei Monatsmieten.", "押金为三个月房租。"),
            ("der Vermieter", "der", "n.", "-", "房东，出租人", "Der Vermieter ist sehr freundlich.", "房东人非常友好。"),
            ("die Vermieterin", "die", "n.", "-nen", "女房东", "Die Vermieterin repariert die Heizung.", "女房东找人修暖气。"),
            ("der Mieter", "der", "n.", "-", "租客，房客", "Die neuen Mieter ziehen morgen ein.", "新租客明天搬进来。"),
            ("der Mietvertrag", "der", "n.", "Mietverträge", "租赁合同", "Haben Sie den Mietvertrag unterschrieben?", "您签署租房合同了吗？"),
            ("mieten", "", "v.", "mietet, mietete, gemietet", "租入，租用", "Wir möchten ein Haus am See mieten.", "我们想在湖边租一栋房子。"),
            ("vermieten", "", "v.", "vermietet, vermietete, vermietet", "出租", "Das Zimmer wird ab sofort vermietet.", "该房间即日起对外出租。"),
            ("umziehen", "", "v.", "zieht um, zog um, ist umgezogen", "搬家", "Wir ziehen nächste Woche nach Hamburg um.", "我们下周搬家去汉堡。"),
            ("der Umzug", "der", "n.", "Umzüge", "搬迁，搬家", "Der Umzug war sehr anstrengend.", "这次搬家非常辛苦劳累。"),
            ("renovieren", "", "v.", "renoviert, renovierte, renoviert", "翻新，装修", "Sie renovieren die alte Wohnung.", "他们正在装修这套旧公寓。"),
            ("die Möbel", "die", "n.pl.", "-", "家具", "Wir brauchen neue Möbel fürs Zimmer.", "我们房间需要买新家具。"),
            ("möbliert", "", "adj.", "", "带家具的", "Die Wohnung ist komplett möbliert.", "这套公寓家具设施齐全。"),
            ("der Tisch", "der", "n.", "-e", "桌子", "Ein großer Tisch steht in der Mitte.", "一张大桌子摆在中间。"),
            ("der Schreibtisch", "der", "n.", "-e", "书桌，办公桌", "Auf dem Schreibtisch steht ein Laptop.", "书桌上放着一台笔记本电脑。"),
            ("der Stuhl", "der", "n.", "Stühle", "椅子", "Nehmen Sie bitte auf dem Stuhl Platz!", "请在这把椅子上坐下！"),
            ("der Sessel", "der", "n.", "-", "扶手软椅，单人沙发", "Großvater liest im Sessel.", "祖父坐在扶手椅上看书。"),
            ("das Sofa", "das", "n.", "-s", "沙发", "Wir sitzen abends gemütlich auf dem Sofa.", "晚上我们舒适地坐在沙发上。"),
            ("die Couch", "die", "n.", "-s", "长沙发", "Die Couch ist sehr bequem.", "这张长沙发非常舒服。"),
            ("das Bett", "das", "n.", "-en", "床", "Das Bett hat eine weiche Matratze.", "这张床有一张柔软的床垫。"),
            ("der Schrank", "der", "n.", "Schränke", "柜子，衣柜", "Der Schrank bietet viel Platz für Kleider.", "这个衣柜有很多放衣服的空间。"),
            ("der Kleiderschrank", "der", "n.", "Kleiderschränke", "衣柜", "Hänge die Hemden in den Kleiderschrank!", "把衬衫挂进衣柜里！"),
            ("das Regal", "das", "n.", "-e", "架子，书架", "Das Regal steht voll mit Büchern.", "书架上摆满了各种书籍。"),
            ("das Bücherregal", "das", "n.", "-e", "书架", "Ein stabiles Bücherregal aus Holz.", "一个结实的木质书架。"),
            ("der Teppich", "der", "n.", "-e", "地毯", "Ein bunter Teppich liegt auf dem Boden.", "地上铺着一块彩色的地毯。"),
            ("die Lampe", "die", "n.", "-n", "台灯，灯具", "Schalte bitte die Lampe an!", "请把台灯打开！"),
            ("das Licht", "das", "n.", "-er", "灯光，光线", "Mach bitte das Licht aus!", "请把灯关掉！"),
            ("das Fenster", "das", "n.", "-", "窗户", "Mach bitte das Fenster auf, es ist warm.", "请把窗户开一下，太热了。"),
            ("die Tür", "die", "n.", "-en", "门", "Schließe bitte die Haustür ab!", "请把入户大门锁上！"),
            ("die Wand", "die", "n.", "Wände", "墙壁", "An der Wand hängt ein schönes Bild.", "墙上挂着一幅漂亮的画。"),
            ("das Bild", "das", "n.", "-er", "画，图画", "Das Bild gefällt mir sehr gut.", "我很喜欢这幅画。"),
            ("der Spiegel", "der", "n.", "-", "镜子", "Im Badezimmer hängt ein großer Spiegel.", "浴室里挂着一面大镜子。"),
            ("die Heizung", "die", "n.", "-en", "暖气", "Die Heizung funktioniert gut.", "暖气运转正常。"),
            ("die Dusche", "die", "n.", "-n", "淋浴", "Ich nehme morgens eine kurze Dusche.", "我早上冲个简短的淋浴。"),
            ("die Badewanne", "die", "n.", "-n", "浴缸", "Die Kinder planschen in der Badewanne.", "孩子们在浴缸里玩水。"),
            ("der Herd", "der", "n.", "-e", "炉灶", "Auf dem Herd kocht die Suppe.", "炉灶上煮着汤。"),
            ("der Ofen", "der", "n.", "Öfen", "烤箱；炉子", "Die Pizza bäckt im Ofen.", "披萨正在烤箱里烤着。"),
            ("der Kühlschrank", "der", "n.", "Kühlschränke", "冰箱", "Stell die Milch bitte in den Kühlschrank!", "请把牛奶放进冰箱里！"),
            ("die Spülmaschine", "die", "n.", "-n", "洗碗机", "Die Spülmaschine spart viel Zeit.", "洗碗机能节省很多时间。"),
            ("die Waschmaschine", "die", "n.", "-en", "洗衣机", "Die Waschmaschine steht im Keller.", "洗衣机放在地下室里。"),
            ("hell", "", "adj.", "heller, am hellsten", "明亮的", "Das Zimmer ist sehr hell und sonnig.", "这个房间非常明亮且阳光充足。"),
            ("dunkel", "", "adj.", "dunkler, am dunkelsten", "昏暗的，阴暗的", "Im Winter wird es früh dunkel.", "冬天天黑得很早。"),
            ("groß", "", "adj.", "größer, am größten", "宽敞的，大的", "Die Wohnung ist 80 Quadratmeter groß.", "这套公寓面积有80平方米。"),
            ("klein", "", "adj.", "kleiner, am kleinsten", "狭小的，小的", "Die Küche ist etwas klein.", "厨房稍微有点小。"),
            ("ruhig", "", "adj.", "ruhiger, am ruhigsten", "安静的", "Wir wohnen in einer ruhigen Gegend.", "我们住在一个安静的街区。"),
            ("laut", "", "adj.", "lauter, am lautesten", "嘈杂的，大声的", "Die Straße vor dem Haus ist sehr laut.", "门前的马路非常嘈杂吵闹。"),
            ("gemütlich", "", "adj.", "gemütlicher, am gemütlichsten", "舒适惬意的", "Die Wohnung ist klein, aber sehr gemütlich.", "公寓不大，但十分温馨惬意。"),
            ("modern", "", "adj.", "moderner, am modernsten", "现代化的", "Das Bad ist neu und modern eingerichtet.", "浴室是全新且现代化的装修。"),
            ("der Quadratmeter", "der", "n.", "-", "平方米", "Das Wohnzimmer hat 25 Quadratmeter.", "客厅面积有25平方米。"),
            ("der Stock", "der", "n.", "-", "楼层", "Ich wohne im dritten Stock.", "我住在三楼。"),
            ("der Aufzug", "der", "n.", "Aufzüge", "电梯", "Gibt es im Haus einen Aufzug?", "这栋楼里有电梯吗？")
        ]
    }
]
