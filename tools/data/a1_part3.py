#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A1 Part 3: Lessons 11 to 15 (350 words)
L11: 休闲运动与爱好娱乐 (Freizeit, Hobbys & Sport) - 70 words
L12: 天气气候与自然四季 (Wetter, Klima & Natur) - 70 words
L13: 节日庆祝与社交拜访 (Feste, Feiern & Einladungen) - 70 words
L14: 数字基数序数与度量衡 (Zahlen, Maße & Geld) - 70 words
L15: 歌德 A1 核心冲刺大通关 (Goethe A1 Prüfungstraining) - 70 words
"""

LESSONS_PART3 = [
    # LESSON 11
    {
        "id": "A1_L11",
        "title": "第11课：休闲运动与爱好娱乐 (Freizeit, Hobbys & Sport)",
        "summary": "掌握球类、乐器、户外运动、休闲活动与情态动词 wollen/dürfen",
        "grammar": {
            "title": "爱好表达与情态动词 wollen / dürfen",
            "sections": [
                {
                    "heading": "1. 表达兴趣爱好常用句型",
                    "content": "• Mein Hobby ist / Meine Hobbys sind...\n• Ich spiele gerne Fußball / Gitarre / Schach.\n• In meiner Freizeit gehe ich oft schwimmen oder wandern.\n• Was machst du gern am Wochenende?"
                },
                {
                    "heading": "2. 情态动词 wollen (打算/想要) 与 dürfen (允许)",
                    "content": "• wollen: ich will, du willst, er will, wir wollen, ihr wollt, sie wollen\n• dürfen: ich darf, du darfst, er darf, wir dürfen, ihr dürft, sie dürfen\n• 情态动词占第2位，实义动词原形放在句末！\n例：Hier darf man nicht rauchen. / Ich will am Samstag wandern gehen."
                }
            ]
        },
        "quiz": [
            {
                "id": "A1_L11_Q1",
                "type": "GRAMMAR_FILL",
                "question": "Ich will am Samstag mit Freunden ins Kino ______.",
                "options": ["gehen", "gehe", "ging", "gegangen"],
                "correctIndex": 0,
                "explanation": "情态动词 will 占第二位，句末实义动词必须用原形 gehen。"
            },
            {
                "id": "A1_L11_Q2",
                "type": "VOCAB_MEANING",
                "question": "德语中表达“禁止吸烟”，指示牌上通常写着：",
                "options": ["Rauchen verboten!", "Hier bitte rauchen!", "Keine Musik!", "Vorsicht Hund!"],
                "correctIndex": 0,
                "explanation": "Rauchen verboten! 是德语区公共场所最标准的禁止吸烟警示。"
            }
        ],
        "words": [
            ("die Freizeit", "die", "n.", "-", "闲暇时间，业余时间", "Was machst du in deiner Freizeit?", "你在业余时间做些什么？"),
            ("das Hobby", "das", "n.", "-s", "业余爱好，嗜好", "Meine Hobbys sind Lesen und Reisen.", "我的爱好是阅读和旅游。"),
            ("das Interesse", "das", "n.", "-n", "兴趣，关注", "Ich habe großes Interesse an Kunst.", "我对艺术有着浓厚的兴趣。"),
            ("interessieren", "", "v.", "interessiert, interessierte, interessiert", "使感兴趣", "Fußball interessiert mich sehr.", "我对足球非常感兴趣。"),
            ("der Sport", "der", "n.", "-", "体育，体育运动", "Treibst du regelmäßig Sport?", "你经常做体育运动吗？"),
            ("treiben", "", "v.", "treibt, trieb, getrieben", "从事，进行（运动）", "Sport treiben hält fit und gesund.", "从事体育锻炼保持精力充沛与健康。"),
            ("der Fußball", "der", "n.", "Fußbälle", "足球", "Deutschland ist berühmt für Fußball.", "德国以足球闻名。"),
            ("spielen", "", "v.", "spielt, spielte, gespielt", "玩，踢球，弹奏", "Die Kinder spielen im Park.", "孩子们在公园里玩耍。"),
            ("der Ball", "der", "n.", "Bälle", "球", "Er wirft den Ball ins Tor.", "他把球踢进了球门。"),
            ("das Spiel", "das", "n.", "-e", "比赛，游戏", "Das Spiel endete 2 zu 1.", "比赛以2比1结束。"),
            ("die Mannschaft", "die", "n.", "-en", "球队，运动队", "Unsere Mannschaft hat gewonnen.", "我们球队赢得了胜利。"),
            ("gewinnen", "", "v.", "gewinnt, gewann, gewonnen", "获胜，赢取", "Wer wird das Turnier gewinnen?", "谁将在这场锦标赛中获胜？"),
            ("verlieren", "", "v.", "verliert, verlor, verloren", "输掉；丢失", "Wir haben das Spiel leider verloren.", "很遗憾我们输掉了这场比赛。"),
            ("das Tor", "das", "n.", "-e", "球门；进球，大门", "Er hat drei Tore geschossen!", "他一个人踢进了三个球！"),
            ("das Stadion", "das", "n.", "Stadien", "体育场", "Das Stadion ist ausverkauft.", "体育场门票全部售罄。"),
            ("der Basketball", "der", "n.", "-", "篮球", "Er spielt gern Basketball.", "他喜欢打篮球。"),
            ("das Tennis", "das", "n.", "-", "网球", "Wollen wir am Sonntag Tennis spielen?", "我们周日去打网球好吗？"),
            ("schwimmen", "", "v.", "schwimmt, schwamm, ist geschwommen", "游泳", "Im Sommer schwimme ich im See.", "夏天我在湖里游泳。"),
            ("das Schwimmbad", "das", "n.", "Schwimmbäder", "游泳池，游泳馆", "Das Schwimmbad öffnet um 7 Uhr.", "游泳馆早晨7点开放。"),
            ("das Freibad", "das", "n.", "Freibäder", "露天游泳池", "Bei Hitze gehen wir ins Freibad.", "天热时我们去露天泳池。"),
            ("das Hallenbad", "das", "n.", "Hallenbäder", "室内游泳馆", "Im Winter schwimmen wir im Hallenbad.", "冬天我们在室内游泳馆游泳。"),
            ("joggen", "", "v.", "joggt, joggte, ist gejoggt", "慢跑", "Ich jogge dreimal pro Woche im Park.", "我每周在公园慢跑三次。"),
            ("laufen", "", "v.", "läuft, lief, ist gelaufen", "跑，快跑，步行", "Er kann sehr schnell laufen.", "他能跑得非常快。"),
            ("wandern", "", "v.", "wandert, wanderte, ist gewandert", "徒步远足", "Im Herbst wandern wir in den Bergen.", "秋天我们去山里徒步。"),
            ("die Wanderung", "die", "n.", "-en", "徒步游，远足", "Eine Wanderung durch den Schwarzwald.", "一场穿越黑森林的徒步。"),
            ("das Fahrrad", "das", "n.", "Fahrräder", "自行车", "Am Wochenende fahren wir Fahrrad.", "周末我们骑自行车郊游。"),
            ("radfahren", "", "v.", "fährt Rad, fuhr Rad, ist radgefahren", "骑自行车", "In Münster fahren fast alle Rad.", "在明斯特几乎所有人都骑车。"),
            ("klettern", "", "v.", "klettert, kletterte, ist geklettert", "攀岩，爬山", "Klettern erfordert viel Kraft.", "攀岩需要很大的体力。"),
            ("Ski fahren", "", "phrase", "", "滑雪", "Im Winter fahren wir in den Alpen Ski.", "冬天我们在阿尔卑斯山滑雪。"),
            ("der Ski", "der", "n.", "-er", "滑雪板", "Ich leihe mir Skier für das Wochenende.", "我租了一副滑雪板度周末。"),
            ("die Musik", "die", "n.", "-", "音乐", "Ich höre beim Lernen klassische Musik.", "我学习时听古典音乐。"),
            ("hören", "", "v.", "hört, hörte, gehört", "听，收听", "Hörst du gerne Podcasts?", "你喜欢听播客吗？"),
            ("das Radio", "das", "n.", "-s", "收音机，广播", "Morgens schalte ich das Radio ein.", "早晨我打开收音机。"),
            ("das Lied", "das", "n.", "-er", "歌曲", "Die Kinder singen ein schönes Lied.", "孩子们唱着一首好听的歌。"),
            ("singen", "", "v.", "singt, sang, gesungen", "唱歌", "Sie singt in einem Chor.", "她在合唱团里唱歌。"),
            ("das Instrument", "das", "n.", "-e", "乐器；仪器", "Spielst du ein Musikinstrument?", "你会弹奏某种乐器吗？"),
            ("das Klavier", "das", "n.", "-e", "钢琴", "Er übt jeden Tag zwei Stunden Klavier.", "他每天练两小时钢琴。"),
            ("die Gitarre", "die", "n.", "-n", "吉他", "Sie spielt Gitarre und singt dazu.", "她弹着吉他伴唱。"),
            ("die Geige", "die", "n.", "-n", "小提琴", "Die Geige klingt sehr weich.", "小提琴的声音非常柔和。"),
            ("die Flöte", "die", "n.", "-n", "长笛，笛子", "Das Mädchen lernt Querflöte.", "女孩在学习长笛。"),
            ("das Konzert", "das", "n.", "-e", "音乐会", "Wir gehen am Samstag ins Konzert.", "我们周六去听音乐会。"),
            ("die Band", "die", "n.", "-s", "乐队", "Die Rockband spielt bekannte Hits.", "摇滚乐队演奏着著名金曲。"),
            ("tanzen", "", "v.", "tanzt, tanzte, getanzt", "跳舞", "Wollen wir zusammen tanzen?", "我们一起跳支舞好吗？"),
            ("der Tanz", "der", "n.", "Tänze", "舞蹈", "Tango ist ein leidenschaftlicher Tanz.", "探戈是一种充满激情的舞蹈。"),
            ("das Buch", "das", "n.", "Bücher", "书，书籍", "Ich lese gerne spannende Bücher.", "我喜欢读情节扣人心弦的书。"),
            ("lesen", "", "v.", "liest, las, gelesen", "阅读", "Er liest vor dem Schlafen einen Roman.", "他睡前读一本小说。"),
            ("der Roman", "der", "n.", "-e", "长篇小说", "Ein fesselnder historischer Roman.", "一部扣人心弦的历史长篇小说。"),
            ("der Krimi", "der", "n.", "-s", "侦探小说，悬疑片", "Sonntagabend schauen viele Tatort-Krimis.", "周日晚上许多人看罪案侦探剧。"),
            ("die Zeitung", "die", "n.", "-en", "报纸", "Mein Vater liest morgens die Zeitung.", "我父亲早晨读报纸。"),
            ("die Zeitschrift", "die", "n.", "-en", "杂志，期刊", "Eine Zeitschrift über Reisen und Kultur.", "一本关于旅游与文化的杂志。"),
            ("die Bibliothek", "die", "n.", "-en", "图书馆", "In der Bibliothek kann man ruhig lernen.", "在图书馆里可以安静学习。"),
            ("das Kino", "das", "n.", "-s", "电影院", "Treffen wir uns vor dem Kino!", "我们在电影院门前碰面！"),
            ("der Film", "der", "n.", "-e", "电影", "Der neue deutsche Film ist sehr gut.", "这部新的德国电影非常好。"),
            ("der Schauspieler", "der", "n.", "-", "男演员", "Ein sehr bekannter deutscher Schauspieler.", "一位非常知名的德国男演员。"),
            ("die Schauspielerin", "die", "n.", "-nen", "女演员", "Sie arbeitet als Schauspielerin am Theater.", "她在剧院担任女演员。"),
            ("das Theater", "das", "n.", "-", "话剧院，戏剧", "Heute Abend gehen wir ins Theater.", "今晚我们去剧院看话剧。"),
            ("das Museum", "das", "n.", "Museen", "博物馆", "Die Museumsinsel in Berlin ist weltberühmt.", "柏林的博物馆岛世界闻名。"),
            ("die Ausstellung", "die", "n.", "-en", "展览，博览会", "Eine Ausstellung moderner Malerei.", "一场现代绘画展览。"),
            ("malen", "", "v.", "malt, malte, gemalt", "画画，作画", "Die Kinder malen bunte Bilder.", "孩子们在画五彩斑斓的画。"),
            ("zeichnen", "", "v.", "zeichnet, zeichnete, gezeichnet", "素描，画线图", "Er zeichnet Architekturpläne.", "他画建筑设计图。"),
            ("fotografieren", "", "v.", "fotografiert, fotografierte, fotografiert", "摄影，拍照", "Ich fotografiere gerne alte Häuser.", "我喜欢拍摄老建筑。"),
            ("das Foto", "das", "n.", "-s", "照片", "Darf ich hier ein Foto machen?", "请问我可以在这里拍照吗？"),
            ("die Kamera", "die", "n.", "-s", "照相机", "Er hat eine professionelle Kamera gekauft.", "他买了一台专业相机。"),
            ("das Bild", "das", "n.", "-er", "照片；图画", "Schau dir dieses schöne Bild an!", "看看这张美丽的照片！"),
            ("reisen", "", "v.", "reist, reiste, ist gereist", "旅行，出国旅游", "Ich reise sehr gerne in ferne Länder.", "我非常喜欢去远方国家旅行。"),
            ("die Reise", "die", "n.", "-n", "旅行，旅途", "Gute Reise und viel Spaß!", "旅途愉快，玩得开心！"),
            ("der Urlaub", "der", "n.", "-e", "休假，假期", "Wir haben im August drei Wochen Urlaub.", "我们八月份有三周休假。"),
            ("die Ferien", "die", "n.pl.", "-", "寒暑假，学校假期", "In den Sommerferien fahren wir ans Meer.", "暑假我们去海边度假。"),
            ("das Spiel", "das", "n.", "-e", "桌游，棋牌游戏", "Wir spielen am Abend oft Brettspiele.", "晚上我们经常玩桌面棋盘游戏。"),
            ("das Schach", "das", "n.", "-", "国际象棋", "Schach fördert das logische Denken.", "国际象棋有助于锻炼逻辑思维。")
        ]
    },

    # LESSON 12
    {
        "id": "A1_L12",
        "title": "第12课：天气气候与自然四季 (Wetter, Klima & Natur)",
        "summary": "掌握晴雨雪风天气描述、温度表达、自然风光词汇与非人称代词 es",
        "grammar": {
            "title": "无人称代词 es 与天气句型表达",
            "sections": [
                {
                    "heading": "1. 常见天气句型总结",
                    "content": "• Es regnet. (在下雨) / Es schneit. (在下雪)\n• Die Sonne scheint. (阳光灿烂) / Der Wind weht. (风在吹)\n• Es ist warm / kalt / heiß / kühl / windig / sonnig / bewölkt / neblig.\n• Wie viel Grad haben wir heute? - Heute sind es 22 Grad."
                },
                {
                    "heading": "2. 四季与月份搭配介词 im",
                    "content": "• im Frühling, im Sommer, im Herbst, im Winter\n• im Januar, im Juli, im Oktober"
                }
            ]
        },
        "quiz": [
            {
                "id": "A1_L12_Q1",
                "type": "VOCAB_MEANING",
                "question": "德语中描述“今天在下雪”的标准句子是：",
                "options": ["Es schneit heute.", "Es regnet heute.", "Es scheint heute.", "Es weht heute."],
                "correctIndex": 0,
                "explanation": "schneien 意为“下雪”，无人称主语用 es：Es schneit heute。"
            },
            {
                "id": "A1_L12_Q2",
                "type": "GRAMMAR_FILL",
                "question": "Wir fahren ______ Sommer (介词填空) nach Italien.",
                "options": ["im", "am", "um", "in"],
                "correctIndex": 0,
                "explanation": "季节前使用介词 im (im Sommer)。"
            }
        ],
        "words": [
            ("das Wetter", "das", "n.", "-", "天气", "Wie ist das Wetter heute bei Ihnen?", "您那里今天天气怎么样？"),
            ("der Wetterbericht", "der", "n.", "-e", "天气预报", "Laut Wetterbericht soll es morgen regnen.", "据天气预报说，明天有雨。"),
            ("die Sonne", "die", "n.", "-n", "太阳，阳光", "Die Sonne scheint den ganzen Tag.", "太阳照耀了一整天。"),
            ("scheinen", "", "v.", "scheint, schien, geschienen", "照耀，照拂", "Die Sonne scheint heute warm.", "今天阳光明媚暖和。"),
            ("sonnig", "", "adj.", "sonniger, am sonnigsten", "晴朗的，阳光明媚的", "Am Wochenende wird es wieder sonnig.", "周末天气又将放晴。"),
            ("der Regen", "der", "n.", "-", "雨，雨水", "Der Regen tut den Pflanzen gut.", "这场雨对植物很有益。"),
            ("regnen", "", "v.", "regnet, regnete, geregnet", "下雨", "Es regnet seit zwei Stunden ununterbrochen.", "雨连续下了两小时没停。"),
            ("regnerisch", "", "adj.", "", "下雨的，阴雨的", "Ein kühler und regnerischer Tag.", "一个阴雨凉爽的日子。"),
            ("die Wolke", "die", "n.", "-n", "云，云彩", "Am Himmel stehen dunkle Wolken.", "天空中飘着厚厚的乌云。"),
            ("bewölkt", "", "adj.", "", "多云的，阴天的", "Heute ist es meist bewölkt.", "今天大部地区多云。"),
            ("der Schnee", "der", "n.", "-", "雪，白雪", "Im Januar liegt hier viel Schnee.", "一月份这里积雪很厚。"),
            ("schneien", "", "v.", "schneit, schneite, geschneit", "下雪", "Es schneit dicke Flocken vom Himmel.", "天空飘落下大朵雪花。"),
            ("der Wind", "der", "n.", "-e", "风", "Der Wind bläst kräftig von Norden.", "北风强劲地呼啸吹来。"),
            ("wehen", "", "v.", "weht, wehte, geweht", "吹拂，刮风", "Ein leichter Wind weht durch die Bäume.", "一阵微风拂过树梢。"),
            ("windig", "", "adj.", "windiger, am windigsten", "刮风的，多风的", "An der Nordsee ist es oft sehr windig.", "北海海滨经常刮大风。"),
            ("der Sturm", "der", "n.", "Stürme", "暴风雨，风暴", "Der Sturm hat mehrere Bäume umgeweht.", "暴风雨刮倒了好几棵大树。"),
            ("das Gewitter", "das", "n.", "-", "雷阵雨，雷暴", "Nach der Hitze kommt oft ein Gewitter.", "酷热之后往往伴有雷暴。"),
            ("blitzen", "", "v.", "blitzt, blitzte, geblitzt", "打闪，闪电", "Es blitzt und donnert gewaltig.", "电闪雷鸣势头很猛。"),
            ("der Blitz", "der", "n.", "-e", "闪电", "Ein heller Blitz erleuchtete den Himmel.", "一道明亮的闪电照亮了夜空。"),
            ("der Donner", "der", "n.", "-", "雷声", "Der Donner folgte kurz nach dem Blitz.", "闪电过后紧接着传来雷鸣。"),
            ("der Nebel", "der", "n.", "-", "雾", "Am Morgen lag dichter Nebel über dem Tal.", "清晨浓雾笼罩着山谷。"),
            ("neblig", "", "adj.", "nebliger, am nebligsten", "有雾的，雾蒙蒙的", "Vorsichtig fahren, es ist sehr neblig!", "小心慢行，雾很大！"),
            ("das Eis", "das", "n.", "-", "冰", "Vorsicht, auf den Straßen ist Glatteis!", "小心，路面有地面积冰！"),
            ("kalt", "", "adj.", "kälter, am kältesten", "寒冷的，冷的", "Im Winter ist es in Berlin bitterkalt.", "冬天柏林极其严寒。"),
            ("die Kälte", "die", "n.", "-", "寒冷，低温", "Zieh dich warm an gegen die Kälte!", "穿暖和点抵御严寒！"),
            ("warm", "", "adj.", "wärmer, am wärmsten", "温暖的", "Im Frühling wird es allmählich warm.", "春天天气逐渐回暖。"),
            ("die Wärme", "die", "n.", "-", "温暖，热度", "Ich genieße die Wärme der Frühlingssonne.", "我享受着春日阳光的暖意。"),
            ("heiß", "", "adj.", "heißer, am heißesten", "炎热的，滚烫的", "Im Juli ist es oft über 35 Grad heiß.", "七月份往往热到35度以上。"),
            ("die Hitze", "die", "n.", "-", "酷暑，炎热", "Trinken Sie viel Wasser bei dieser Hitze!", "酷暑天请多喝水！"),
            ("kühl", "", "adj.", "kühler, am kühlsten", "凉爽的，微凉的", "Am Abend weht eine kühle Brise.", "傍晚刮起一阵凉爽的微风。"),
            ("trocken", "", "adj.", "trockener, am trockensten", "干燥的，干爽的", "Dieser Sommer war außergewöhnlich trocken.", "这个夏天异常干旱少雨。"),
            ("nass", "", "adj.", "nasser, am nassesten", "潮湿的，湿漉漉的", "Meine Schuhe sind durch den Regen nass.", "我的鞋被雨水浸湿了。"),
            ("das Grad", "das", "n.", "-e", "度，度数（摄氏度）", "Heute haben wir angenehme 23 Grad.", "今天气温是宜人的23度。"),
            ("die Temperatur", "die", "n.", "-en", "温度，气温", "Die Temperaturen steigen am Nachmittag.", "下午气温开始回升。"),
            ("die Jahreszeit", "die", "n.", "-en", "季节", "Welche Jahreszeit magst du am liebsten?", "你最喜欢哪个季节？"),
            ("der Frühling", "der", "n.", "-", "春天，春季", "Im Frühling erwacht die Natur zu neuem Leben.", "春天大自然复苏焕发生机。"),
            ("das Frühjahr", "das", "n.", "-", "春季", "Im Frühjahr blühen die Apfelbäume.", "春季苹果树开花。"),
            ("der Sommer", "der", "n.", "-", "夏天，夏季", "Im Sommer fahren wir oft ans Meer.", "夏天我们常去海边。"),
            ("der Herbst", "der", "n.", "-", "秋天，秋季", "Im Herbst verfärben sich die Blätter bunt.", "秋天树叶变得五彩斑斓。"),
            ("der Winter", "der", "n.", "-", "冬天，冬季", "Im Winter liegt in den Bergen weißer Schnee.", "冬天高山覆盖着皑皑白雪。"),
            ("die Natur", "die", "n.", "-", "大自然，自然界", "Wir lieben Wanderungen in der freien Natur.", "我们热爱在大自然中徒步远足。"),
            ("die Landschaft", "die", "n.", "-en", "风景，风光，地貌", "Die bayerische Landschaft ist wunderschön.", "巴伐利亚的风光优美迷人。"),
            ("der Baum", "der", "n.", "Bäume", "树，树木", "Unter der alten Eiche ist viel Schatten.", "老橡树下有一大片树荫。"),
            ("das Blatt", "das", "n.", "Blätter", "树叶；纸张", "Im Herbst fallen die Blätter von den Bäumen.", "秋天树叶从树上飘落。"),
            ("die Blume", "die", "n.", "-n", "花，花卉", "Sie schenkt ihrer Mutter schöne Blumen.", "她送给母亲一束漂亮的花。"),
            ("blühen", "", "v.", "blüht, blühte, geblüht", "盛开，开花", "Im Park blühen Tausende Tulpen.", "公园里盛开着成千上万朵郁金香。"),
            ("die Pflanze", "die", "n.", "-n", "植物", "Pflanzen brauchen regelmäßig Wasser.", "植物需要经常浇水。"),
            ("der Wald", "der", "n.", "Wälder", "森林", "Ein Spaziergang durch den stillen Wald.", "在静谧的森林里漫步散心。"),
            ("der Berg", "der", "n.", "-e", "山，高山", "Die Zugspitze ist der höchste Berg Deutschlands.", "楚格峰是德国最高的山峰。"),
            ("die Berge", "die", "n.pl.", "-", "山区，山脉", "Wir fahren zum Wandern in die Berge.", "我们去山区徒步旅行。"),
            ("das Tal", "das", "n.", "Täler", "山谷", "Das kleine Dorf liegt friedlich im Tal.", "小村庄安详地坐落在山谷中。"),
            ("der Fluss", "der", "n.", "Flüsse", "河流", "Schiffe fahren gemächlich auf dem Fluss.", "轮船在河道上缓行。"),
            ("der See", "der", "n.", "-n", "湖泊", "Der Bodensee grenzt an drei Länder.", "博登湖与三个国家接壤。"),
            ("die See", "die", "n.", "-", "海洋，大海", "Urlaub an der stürmischen Ostsee.", "在波浪汹涌的波罗的海度假。"),
            ("das Meer", "das", "n.", "-e", "海，大海", "Das Rauschen des Meeres beruhigt mich.", "大海的浪涛声让我心绪宁静。"),
            ("der Strand", "der", "n.", "Strände", "海滩，沙滩", "Die Kinder bauen Burgen am Sandstrand.", "孩子们在沙滩上堆沙堡。"),
            ("die Insel", "die", "n.", "-n", "岛屿", "Rügen ist die größte Insel Deutschlands.", "吕根岛是德国最大的岛屿。"),
            ("der Himmel", "der", "n.", "-", "天空", "Kein Wölkchen trübt den blauen Himmel.", "万里无云，一片碧空。"),
            ("der Stern", "der", "n.", "-e", "星星，恒星", "In der klaren Nacht sieht man viele Sterne.", "在晴朗的夜晚能看到满天繁星。"),
            ("der Mond", "der", "n.", "-e", "月亮", "Der Vollmond leuchtet hell durchs Fenster.", "满月透过窗户洒下明亮的光。"),
            ("die Luft", "die", "n.", "-", "空气", "Die Bergluft ist wunderbar sauber und frisch.", "山里的空气格外清新纯净。"),
            ("das Tier", "das", "n.", "-e", "动物", "Hunde und Katzen sind beliebte Haustiere.", "猫狗是受人喜爱的宠物。"),
            ("der Vogel", "der", "n.", "Vögel", "鸟，飞禽", "Die Vögel singen fröhlich am frühen Morgen.", "清晨小鸟在欢快地啼叫。"),
            ("das Pferd", "das", "n.", "-e", "马", "Auf dem Bauernhof gibt es zwei Pferde.", "农场里有两匹马。"),
            ("die Kuh", "die", "n.", "Kühe", "奶牛，母牛", "Die Kühe grasen friedlich auf der Wiese.", "奶牛在草地上安详地吃草。"),
            ("das Schwein", "das", "n.", "-e", "猪", "Schweine sind erstaunlich kluge Tiere.", "猪是惊人聪明的动物。"),
            ("das Schaf", "das", "n.", "-e", "绵羊", "Eine Herde weißer Schafe auf dem Deich.", "堤坝上一群洁白的绵羊。"),
            ("die Umwelt", "die", "n.", "-", "环境，生态环境", "Wir müssen unsere Umwelt aktiv schützen.", "我们必须积极保护生态环境。"),
            ("schützen", "", "v.", "schützt, schützte, geschützt", "保护，防护", "Die Mütze schützt die Ohren vor Kälte.", "帽子保护耳朵免受严寒冻伤。"),
            ("das Klima", "das", "n.", "-", "气候", "Das Klima verändert sich weltweit spürbar.", "全球气候正在明显发生改变。")
        ]
    },

    # LESSON 13
    {
        "id": "A1_L13",
        "title": "第13课：节日庆祝与社交拜访 (Feste, Feiern & Einladungen)",
        "summary": "掌握生日、新年、圣诞等节庆词汇、邀请函与道贺祝福礼仪",
        "grammar": {
            "title": "节日问候语与完成时入门",
            "sections": [
                {
                    "heading": "1. 德国高频节日祝福语",
                    "content": "• Herzlichen Glückwunsch zum Geburtstag! (生日快乐！)\n• Frohe Weihnachten! (圣诞快乐！)\n• Ein frohes neues Jahr! / Guten Rutsch! (新年快乐！/ 顺利跨年！)\n• Frohe Ostern! (复活节快乐！)\n• Alles Gute zur Hochzeit! (新婚大喜！)\n• Viel Erfolg! (祝取得圆满成功！)"
                },
                {
                    "heading": "2. 现在完成时入门 (haben / sein + Partizip II)",
                    "content": "• 规则动词第二分词：ge- + 词干 + -(e)t\n  Ich habe gestern gefeiert. / Er hat ein Geschenk gekauft.\n• 移位与状态改变动词助动词用 sein：\n  Wir sind um 20 Uhr gekommen."
                }
            ]
        },
        "quiz": [
            {
                "id": "A1_L13_Q1",
                "type": "EXAM_REAL",
                "question": "德国朋友过生日，送上祝福最地道的表达是：",
                "options": ["Herzlichen Glückwunsch zum Geburtstag!", "Frohe Ostern!", "Gute Reise!", "Guten Appetit!"],
                "correctIndex": 0,
                "explanation": "Herzlichen Glückwunsch zum Geburtstag! 是德语最地道、标准的生日祝福语。"
            },
            {
                "id": "A1_L13_Q2",
                "type": "VOCAB_MEANING",
                "question": "新年除夕夜德国人互相告别时常说的 'Guten Rutsch!' 意思是：",
                "options": ["祝顺利滑入新的一年，新年好！", "小心路滑！", "祝下雪天愉快！", "祝生日快乐！"],
                "correctIndex": 0,
                "explanation": "Guten Rutsch ins neue Jahr! 是德国除夕迎接新年独具文化特色的祝福语。"
            }
        ],
        "words": [
            ("das Fest", "das", "n.", "-e", "节庆，节日", "Weihnachten ist ein großes Fest der Familie.", "圣诞节是家庭团聚的重要节日。"),
            ("die Feier", "die", "n.", "-n", "庆祝活动，庆典", "Die Feier beginnt heute um 19 Uhr.", "庆典活动今晚19点开始。"),
            ("feiern", "", "v.", "feiert, feierte, gefeiert", "庆祝，欢庆", "Wir feiern heute meinen 25. Geburtstag.", "我们今天庆祝我25岁生日。"),
            ("die Party", "die", "n.", "-s", "聚会，派对", "Kommst du am Samstag zu meiner Party?", "你周六来参加我的派对吗？"),
            ("der Geburtstag", "der", "n.", "-e", "生日", "Wann hast du Geburtstag?", "你什么时候过生日？"),
            ("das Geburtsdatum", "das", "n.", "Geburtsdaten", "出生日期", "Geben Sie bitte Ihr Geburtsdatum an!", "请填写您的出生日期！"),
            ("der Geburtsort", "der", "n.", "-e", "出生地点", "Mein Geburtsort ist Shanghai.", "我的出生地是上海。"),
            ("gratulieren", "", "v.", "gratuliert, gratulierte, gratuliert", "祝贺，向...道贺 (接Dativ)", "Ich gratuliere dir von Herzen zum Geburtstag!", "我衷心祝贺你生日快乐！"),
            ("der Glückwunsch", "der", "n.", "Glückwünsche", "祝福，贺词", "Herzlichen Glückwunsch zur Beförderung!", "衷心祝贺你获得晋升！"),
            ("das Geschenk", "das", "n.", "-e", "礼物", "Vielen Dank für das wunderbare Geschenk!", "非常感谢这份美妙的礼物！"),
            ("schenken", "", "v.", "schenkt, schenkte, geschenkt", "赠送，送礼", "Was schenkst du deiner Mutter zu Muttertag?", "母亲节你送母亲什么礼物？"),
            ("die Einladung", "die", "n.", "-en", "邀请，请帖", "Danke für die freundliche Einladung!", "多谢您热情的邀请！"),
            ("einladen", "", "v.", "lädt ein, lud ein, eingeladen", "邀请；请客", "Ich lade euch alle herzlich zum Abendessen ein.", "我热诚邀请大家一起共进晚餐。"),
            ("zusagen", "", "v.", "sagt zu, sagte zu, zugesagt", "答应，确认出席", "Ich freue mich und sage gerne zu.", "我很高兴并欣然确认出席。"),
            ("absagen", "", "v.", "sagt ab, sagte ab, abgesagt", "谢绝，婉拒", "Leider muss ich für morgen absagen.", "很遗憾明天我必须谢绝缺席。"),
            ("mitbringen", "", "v.", "bringt mit, brachte mit, mitgebracht", "随身带来", "Soll ich einen Salat zur Party mitbringen?", "我需要带一份沙拉去派对吗？"),
            ("Weihnachten", "das", "n.", "-", "圣诞节", "Frohe Weihnachten und ein gutes neues Jahr!", "祝圣诞快乐，新年顺意！"),
            ("der Heiligabend", "der", "n.", "-", "平安夜，圣诞前夕", "An Heiligabend gibt es die Bescherung.", "在平安夜大家互换拆开礼物。"),
            ("der Weihnachtsbaum", "der", "n.", "Weihnachtsbäume", "圣诞树", "Wir schmücken gemeinsam den Weihnachtsbaum.", "我们一起装点圣诞树。"),
            ("der Weihnachtsmarkt", "der", "n.", "Weihnachtsmärkte", "圣诞集市", "Auf dem Weihnachtsmarkt trinken wir Glühwein.", "在圣诞集市上我们喝热红酒。"),
            ("der Glühwein", "der", "n.", "-", "热红酒，香料热葡萄酒", "Ein Becher heißer Glühwein wärmt auf.", "一杯滚烫的热红酒暖人身心。"),
            ("Silvester", "das", "n.", "-", "除夕，公历除夕夜", "An Silvester um Mitternacht gibt es Feuerwerk.", "除夕午夜时分有盛大烟花秀。"),
            ("das Feuerwerk", "das", "n.", "-e", "烟花，焰火", "Das Feuerwerk über dem Brandenburger Tor.", "勃兰登堡门上空绚丽的烟火。"),
            ("das Neujahr", "das", "n.", "-", "元旦，新年", "Prosit Neujahr allerseits!", "祝大家新年万事如意！"),
            ("Ostern", "das", "n.", "-", "复活节", "Frohe Ostern wünsche ich deiner Familie!", "祝你的家人复活节快乐！"),
            ("das Osterei", "das", "n.", "-er", "复活节彩蛋", "Die Kinder suchen bunte Ostereier im Garten.", "孩子们在花园里寻找彩色彩蛋。"),
            ("der Osterhase", "der", "n.", "-n", "复活节兔子", "Der Osterhase versteckt die Schokolade.", "复活节兔子把巧克力藏起来。"),
            ("der Karneval", "der", "n.", "-", "狂欢节，谢肉节", "In Köln wird der Karneval groß gefeiert.", "科隆盛大欢庆狂欢节。"),
            ("der Fasching", "der", "n.", "-", "狂欢节（南德称呼）", "Kinder verkleiden sich am Fasching.", "孩子们在狂欢节盛装打扮。"),
            ("das Kostüm", "das", "n.", "-e", "化装服，假面服饰", "Ein lustiges Kostüm für den Karnevalsumzug.", "狂欢节游行穿的一身滑稽行头。"),
            ("die Hochzeit", "die", "n.", "-en", "婚礼", "Die Hochzeit findet in einer Schlosskapelle statt.", "婚礼在一座城堡礼拜堂举行。"),
            ("der Bräutigam", "der", "n.", "-e", "新郎", "Der Bräutigam wartet am Altar.", "新郎在圣坛前等候。"),
            ("die Braut", "die", "n.", "Bräute", "新娘", "Die Braut trägt ein schneeweißes Kleid.", "新娘穿着一身雪白的婚纱。"),
            ("heiraten", "", "v.", "heiratet, heiratete, geheiratet", "结婚", "Sie heiraten im nächsten Frühling.", "他们将在明年春天完婚。"),
            ("verheiratet", "", "adj.", "", "已婚的", "Sind Sie verheiratet oder ledig?", "您是已婚还是单身？"),
            ("ledig", "", "adj.", "", "单身的，未婚的", "Er ist 28 Jahre alt und noch ledig.", "他28岁，目前还是未婚单身。"),
            ("geschieden", "", "adj.", "", "离异的", "Sie ist seit zwei Jahren geschieden.", "她两年前离异了。"),
            ("der Gast", "der", "n.", "Gäste", "客人，宾客", "Die Gäste tanzen ausgelassen im Saal.", "客人们在厅堂里欢快起舞。"),
            ("begrüßen", "", "v.", "begrüßt, begrüßte, begrüßt", "迎接，问候欢迎", "Der Gastgeber begrüßt alle Ankommenden herzlich.", "主人热情迎接所有到访的客人。"),
            ("verabschieden", "", "v.", "verabschiedet, verabschiedete, verabschiedet", "告别，送别", "Wir verabschieden uns von den Gastgebern.", "我们向主人礼貌道别。"),
            ("der Kuchen", "der", "n.", "-", "蛋糕", "Mutter schneidet den Geburtstagskuchen an.", "母亲切开生日蛋糕。"),
            ("die Torte", "die", "n.", "-n", "大圆蛋糕，奶油蛋糕", "Eine festliche Torte mit Erdbeeren.", "一个插满草莓的节日奶油蛋糕。"),
            ("die Kerze", "die", "n.", "-n", "蜡烛", "Puste die Kerzen auf dem Kuchen aus!", "把蛋糕上的蜡烛吹灭吧！"),
            ("anzünden", "", "v.", "zündet an, zündete an, angezündet", "点燃，点着", "Wir zünden die Kerzen am Adventskranz an.", "我们点亮降临节花环上的蜡烛。"),
            ("auspusten", "", "v.", "pustet aus, pustete aus, ausgepustet", "吹灭", "Das Kind pustet alle fünf Kerzen aus.", "小孩一口气吹灭了所有五支蜡烛。"),
            ("wünschen", "", "v.", "wünscht, wünschte, gewünscht", "祝愿，希望", "Ich wünsche dir von Herzen alles Gute!", "我由衷祝愿你万事顺遂！"),
            ("der Wunsch", "der", "n.", "Wünsche", "愿望，祝福", "Haben Sie noch einen besonderen Wunsch?", "您还有什么特别的心愿吗？"),
            ("das Glück", "das", "n.", "-", "幸运，幸福", "Viel Glück für deine Deutschprüfung!", "祝你德语考试好运取得佳绩！"),
            ("der Erfolg", "der", "n.", "-e", "成功", "Viel Erfolg bei der neuen Arbeitsstelle!", "祝你在新工作岗位上取得巨大成功！"),
            ("die Gesundheit", "die", "n.", "-", "健康", "Vor allem wünsche ich dir Gesundheit.", "最重要的，我祝愿你身体健康。"),
            ("das Glas", "das", "n.", "Gläser", "酒杯；玻璃", "Erhebt die Gläser auf das Geburtstagskind!", "让我们举起酒杯为寿星干杯！"),
            ("anstoßen", "", "v.", "stößt an, stieß an, angestoßen", "碰杯，碰响酒杯", "Stoßen wir auf unsere Freundschaft an!", "为我们的友谊干杯碰杯！"),
            ("prost", "", "int.", "", "干杯（啤酒日常）", "Prost zusammen, lasst es euch schmecken!", "大家干杯，祝喝得痛快！"),
            ("zum Wohl", "", "phrase", "", "祝您健康干杯（正式敬酒）", "Zum Wohl, Frau Direktor Müller!", "祝您健康干杯，穆勒董事！"),
            ("die Musik", "die", "n.", "-", "音乐", "Die Musik ist laut und mitreißend.", "音乐声宏亮且极富感染力。"),
            ("die Stimmung", "die", "n.", "-en", "气氛，心情情绪", "Auf dem Fest herrschte tolle Stimmung.", "庆典上洋溢着极佳的欢乐气氛。"),
            ("Spaß machen", "", "phrase", "", "有趣，带来快乐", "Deutsch lernen macht wirklich großen Spaß!", "学习德语真是一件极有趣味的事！"),
            ("lachen", "", "v.", "lacht, lachte, gelacht", "笑，开怀大笑", "Alle Gäste lachten über den lustigen Witz.", "所有客人都被逗人的笑话引得大笑。"),
            ("freuen", "", "v.", "freut, freute, gefreut", "感到高兴", "Ich freue mich sehr über dein Kommen.", "非常高兴你能光临到来。"),
            ("die Überraschung", "die", "n.", "-en", "惊喜，意料之外的事", "Die Feier war eine gelungene Überraschung.", "这场聚会办成了一个成功的惊喜。"),
            ("überraschen", "", "v.", "überrascht, überraschte, überrascht", "使感到惊喜", "Wir wollen ihn zum Jubiläum überraschen.", "我们想在他逢整数周年时给他一个惊喜。"),
            ("die Karte", "die", "n.", "-n", "贺卡；卡片", "Ich schreibe eine Geburtstagskarte an Oma.", "我给祖母写一张生日贺卡。"),
            ("die Postkarte", "die", "n.", "-n", "明信片", "Schöne Grüße aus den Ferien per Postkarte.", "从度假地寄来明信片问候。"),
            ("die Blume", "die", "n.", "-n", "鲜花", "Er brachte einen bunten Blumenstrauß mit.", "他带了一束五彩斑斓的鲜花。"),
            ("der Strauß", "der", "n.", "Sträuße", "花束", "Ein Strauß roter Rosen für die Dame.", "献给这位女士的一束红玫瑰。"),
            ("das Spiel", "das", "n.", "-e", "游戏", "Wir machen ein lustiges Partyspiel.", "我们组织了一场好玩的派对游戏。"),
            ("tanzen", "", "v.", "tanzt, tanzte, getanzt", "跳舞，起舞", "Sie tanzten bis tief in die Nacht.", "他们一直跳舞跳到深夜。"),
            ("vorbereiten", "", "v.", "bereitet vor, bereitete vor, vorbereitet", "筹备，准备", "Wir müssen die Party rechtzeitig vorbereiten.", "我们必须及时筹备好聚会。"),
            ("die Vorbereitung", "die", "n.", "-en", "准备工作，筹划", "Die Vorbereitungen laufen auf Hochtouren.", "各项准备工作正在紧锣密鼓进行中。"),
            ("gemütlich", "", "adj.", "gemütlicher, am gemütlichsten", "惬意舒适的", "Wir hatten einen sehr gemütlichen Abend.", "我们度过了一个非常惬意舒适的夜晚。")
        ]
    },

    # LESSON 14
    {
        "id": "A1_L14",
        "title": "第14课：数字基数序数与度量衡 (Zahlen, Maße & Geld)",
        "summary": "掌握0-1000数字规律、序数词日期、货币单位(Euro/Cent)与度量衡",
        "grammar": {
            "title": "德语数字倒序读法与日期表达",
            "sections": [
                {
                    "heading": "1. 21-99 数字“个位在前，十位在后”读法",
                    "content": "• 21 = einundzwanzig (1 + 和 + 20)\n• 35 = fünfunddreißig (5 + 和 + 30)\n• 68 = achtundsechzig (8 + 和 + 60)\n• 100 = (ein)hundert, 1000 = (ein)tausend"
                },
                {
                    "heading": "2. 日期序数词 am + -(s)ten 结构",
                    "content": "• 1至19加 -ten：am ersten Mai, am dritten Juni\n• 20及以上加 -sten：am zwanzigsten Juli, am einunddreißigsten Dezember\n• 询问日期：Der Wievielte ist heute? / Welches Datum haben wir?"
                }
            ]
        },
        "quiz": [
            {
                "id": "A1_L14_Q1",
                "type": "VOCAB_MEANING",
                "question": "德语复合数字 'vierundfünfzig' 对应的阿拉伯数字是：",
                "options": ["54", "45", "504", "405"],
                "correctIndex": 0,
                "explanation": "vier(4) + und(和) + fünfzig(50) = 54，德语先读个位数后读十位数。"
            },
            {
                "id": "A1_L14_Q2",
                "type": "GRAMMAR_FILL",
                "question": "Wir treffen uns am ______ (der dritte) Mai.",
                "options": ["dritten", "dritte", "dritter", "drittes"],
                "correctIndex": 0,
                "explanation": "在介词 am 之后序数词词尾加 -n (am dritten Mai)。"
            }
        ],
        "words": [
            ("die Zahl", "die", "n.", "-en", "数字，数目", "Können Sie die Zahlen von 1 bis 100?", "您能数出从1到100的数字吗？"),
            ("die Nummer", "die", "n.", "-n", "号码，编号", "Wie lautet Ihre Zimmernummer?", "您的房间号码是多少？"),
            ("zählen", "", "v.", "zählt, zählte, gezählt", "数数，清点", "Das Kind lernt bis zehn zählen.", "小孩在学数数到十。"),
            ("null", "", "num.", "", "零", "Die Vorwahl beginnt mit einer Null.", "区号以一个零开头。"),
            ("eins", "", "num.", "", "一", "Eins, zwei, drei, los geht's!", "一、二、三，出发！"),
            ("zwei", "", "num.", "", "二", "Ich habe zwei jüngere Schwestern.", "我有两个妹妹。"),
            ("drei", "", "num.", "", "三", "Ein Dreieck hat drei Ecken.", "三角形有三个角。"),
            ("vier", "", "num.", "", "四", "Das Auto hat vier Räder.", "轿车有四个轮子。"),
            ("fünf", "", "num.", "", "五", "Die Hand hat fünf Finger.", "一只手有五个手指。"),
            ("sechs", "", "num.", "", "六", "Ein Insekt hat sechs Beine.", "昆虫有六条腿。"),
            ("sieben", "", "num.", "", "七", "Eine Woche besteht aus sieben Tagen.", "一个星期由七天组成。"),
            ("acht", "", "num.", "", "八", "Der Arbeitstag dauert acht Stunden.", "工作日持续八个小时。"),
            ("neun", "", "num.", "", "九", "Sie wohnt in Zimmer Nummer neun.", "她住在九号房间。"),
            ("zehn", "", "num.", "", "十", "Zehn Personen passen an den Tisch.", "十个人能围坐在这张桌旁。"),
            ("elf", "", "num.", "", "十一", "Beim Fußball spielen elf Spieler.", "踢足球有十一名队员。"),
            ("zwölf", "", "num.", "", "十二", "Das Jahr hat zwölf Monate.", "一年有十二个月。"),
            ("zwanzig", "", "num.", "", "二十", "Er wird nächste Woche zwanzig.", "他下周满二十岁。"),
            ("dreißig", "", "num.", "", "三十", "Dieser Monat hat dreißig Tage.", "这个月有三十天。"),
            ("vierzig", "", "num.", "", "四十", "Sie arbeitet vierzig Stunden pro Woche.", "她每周工作四十小时。"),
            ("fünfzig", "", "num.", "", "五十", "Er feiert seinen fünfzigsten Geburtstag.", "他在庆祝他的五十岁生日。"),
            ("sechzig", "", "num.", "", "六十", "Eine Stunde hat sechzig Minuten.", "一小时有六十分钟。"),
            ("siebzig", "", "num.", "", "七十", "Mein Großvater ist siebzig Jahre alt.", "我的祖父今年七十岁。"),
            ("achtzig", "", "num.", "", "八十", "Die Höchstgeschwindigkeit ist achtzig.", "最高限速是每小时八十公里。"),
            ("neunzig", "", "num.", "", "九十", "Ein rechter Winkel hat neunzig Grad.", "直角是九十度。"),
            ("hundert", "", "num.", "", "一百", "Hundert Cent sind ein Euro.", "一百欧分等于一欧元。"),
            ("tausend", "", "num.", "", "一千", "Ein Kilometer sind tausend Meter.", "一公里等于一千米。"),
            ("die Million", "die", "n.", "-en", "百万", "Berlin hat über 3,6 Millionen Einwohner.", "柏林拥有超过360万常住人口。"),
            ("erste", "", "adj./num.", "", "第一，首先的", "Er wohnt im ersten Stock links.", "他住在一楼左手边。"),
            ("zweite", "", "adj./num.", "", "第二", "Nehmen Sie die zweite Straße rechts!", "在第二条路口右拐！"),
            ("dritte", "", "adj./num.", "", "第三", "Heute ist der dritte Tag der Reise.", "今天是旅程的第三天。"),
            ("vierte", "", "adj./num.", "", "第四", "Im vierten Quartal steigen die Umsätze.", "第四季度销售额出现增长。"),
            ("letzte", "", "adj.", "", "最后的，最近的", "Das ist meine letzte Frage.", "这是我的最后一个问题。"),
            ("nächste", "", "adj.", "", "下一个的，接下来的", "Der nächste Bus kommt um 15 Uhr.", "下一班车在15点到站。"),
            ("einmal", "", "adv.", "", "一次", "Ich war schon einmal in Wien.", "我曾经去过一次维也纳。"),
            ("zweimal", "", "adv.", "", "两次", "Putzen Sie zweimal am Tag die Zähne!", "请每天刷牙两次！"),
            ("halb", "", "adj./adv.", "", "一半的", "Es ist halb vier Uhr nachmittags.", "现在是下午三点半。"),
            ("die Hälfte", "die", "n.", "-n", "一半，二分之一", "Er hat die Hälfte des Geldes gespart.", "他存下了这笔钱的一半。"),
            ("das Viertel", "das", "n.", "-", "四分之一；街区", "Es ist Viertel nach fünf.", "现在是五点一刻。"),
            ("das Kilo", "das", "n.", "-s", "千克，公斤", "Ein Kilo Äpfel kostet drei Euro.", "一公斤苹果三欧元。"),
            ("das Kilogramm", "das", "n.", "-e", "公斤，千克", "Das Paket wiegt genau zwei Kilogramm.", "包裹整整两公斤重。"),
            ("das Gramm", "das", "n.", "-e", "克", "Geben Sie mir bitte 150 Gramm Wurst!", "请给我称150克香肠！"),
            ("das Pfund", "das", "n.", "-e", "磅（500克）", "Ein Pfund Erdbeeren bitte!", "请来一磅（500克）草莓！"),
            ("der Liter", "der", "n.", "-", "升", "Der Tank fasst 50 Liter Benzin.", "油箱能容纳50升汽油。"),
            ("der Meter", "der", "n.", "-", "米，公尺", "Der Tisch ist zwei Meter lang.", "这张桌子长两米。"),
            ("der Zentimeter", "der", "n.", "-", "厘米，公分", "Der Stoff ist 90 Zentimeter breit.", "这块布料宽90厘米。"),
            ("der Kilometer", "der", "n.", "-", "公里，千米", "Bis München sind es noch 100 Kilometer.", "距离慕尼黑还有100公里。"),
            ("wiegen", "", "v.", "wiegt, wog, gewogen", "称重；重量为", "Wie viel wiegt das Handgepäck?", "手提行李重多少？"),
            ("das Gewicht", "das", "n.", "-e", "重量，体重", "Das maximale Gewicht beträgt 23 Kilo.", "最高限重为23公斤。"),
            ("schwer", "", "adj.", "schwerer, am schwersten", "沉重的；艰难的", "Der Koffer ist viel zu schwer.", "这个行李箱太沉了。"),
            ("leicht", "", "adj.", "leichter, am leichtesten", "轻盈的；容易的", "Die Prüfung war überraschend leicht.", "考试出人意料地容易。"),
            ("die Länge", "die", "n.", "-n", "长度", "Die Länge des Zimmers beträgt vier Meter.", "房间的进深长度是四米。"),
            ("die Breite", "die", "n.", "-n", "宽度", "Die Straße hat eine Breite von 12 Metern.", "街道宽度为12米。"),
            ("die Höhe", "die", "n.", "-n", "高度", "Der Schrank hat eine Höhe von zwei Metern.", "衣柜高度有两米整。"),
            ("die Größe", "die", "n.", "-n", "尺寸，大小", "Ich brauche Schuhe in Größe 42.", "我需要42码的鞋子。"),
            ("messen", "", "v.", "misst, maß, gemessen", "测量，量度", "Messen Sie bitte die Fensterbreite aus!", "请量一下窗户的宽度！"),
            ("das Geld", "das", "n.", "-", "金钱，货币", "Geld allein macht nicht glücklich.", "金钱本身并不能买来幸福。"),
            ("das Bargeld", "das", "n.", "-", "现金", "Zahlen Sie mit Bargeld oder Karte?", "您付现金还是刷卡？"),
            ("bar", "", "adv.", "", "用现金地", "Kann ich hier bar bezahlen?", "我可以在这里付现金吗？"),
            ("die Bank", "die", "n.", "-en", "银行", "Die Bank hat von 9 bis 16 Uhr geöffnet.", "银行营业时间为9点至16点。"),
            ("das Konto", "das", "n.", "Konten", "银行账户", "Ich möchte ein Girokonto eröffnen.", "我想开立一个银行往来账户。"),
            ("eröffnen", "", "v.", "eröffnet, eröffnete, eröffnet", "开户；开张开业", "Sie eröffnet ein Konto bei der Sparkasse.", "她在储蓄银行开了一个账户。"),
            ("die Karte", "die", "n.", "-n", "银行卡，卡片", "Stecken Sie bitte Ihre Karte in den Schlitz!", "请将您的银行卡插入口内！"),
            ("die EC-Karte", "die", "n.", "-n", "借记卡", "In Deutschland ist die EC-Karte sehr verbreitet.", "借记卡在德国普及率很高。"),
            ("die Kreditkarte", "die", "n.", "-n", "信用卡", "Akzeptieren Sie hier auch Kreditkarten?", "你们这里接受信用卡吗？"),
            ("der Geldautomat", "der", "n.", "-en", "自动取款机，ATM", "Der Geldautomat ist leider defekt.", "这台取款机遗憾故障停用了。"),
            ("abheben", "", "v.", "hebt ab, hob ab, abgehoben", "提款，取钱", "Ich möchte 200 Euro vom Konto abheben.", "我想从账户中支取200欧元。"),
            ("einzahlen", "", "v.", "zahlt ein, zahlte ein, eingezahlt", "存入（现金）", "Er zahlt Geld auf sein Sparbuch ein.", "他把钱存入存折中。"),
            ("überweisen", "", "v.", "überweist, überwies, überwiesen", "转账，汇款", "Ich überweise die Miete jeden Monat pünktlich.", "我每月按时转账缴纳房租。"),
            ("die Überweisung", "die", "n.", "-en", "银行转账汇款", "Die Überweisung dauert einen Werktag.", "转账需要一个工作日到账。"),
            ("die PIN", "die", "n.", "-s", "个人密码", "Geben Sie Ihre vierstellige PIN ein!", "请键入您的四位密码！")
        ]
    },

    # LESSON 15
    {
        "id": "A1_L15",
        "title": "第15课：歌德 A1 核心冲刺大通关 (Goethe A1 Prüfungstraining)",
        "summary": "全面复习歌德A1听说读写四大题型高频核心词汇与全真模拟",
        "grammar": {
            "title": "歌德 A1 考点全景梳理与应试策略",
            "sections": [
                {
                    "heading": "1. 歌德 A1 笔试要领与三大高频文体",
                    "content": "• 听力：抓数字、时间、地点与价格关键核心词。\n• 阅读：广告信息对比、便条便函关键信息点提取。\n• 写作：规范填写报名登记表，能书写30词左右的简短请假信或聚会邀请回复。"
                },
                {
                    "heading": "2. 口语三大模块突破",
                    "content": "• Teil 1: 个人情况自我介绍 (Sich vorstellen: Name, Alter, Land, Wohnort, Sprachen, Beruf, Hobby)\n• Teil 2: 抽取关键词卡片提问与回答 (Thema: Einkaufen, Freizeit, Wohnen)\n• Teil 3: 抽取物品图片发出礼貌请求并应答 (Bitten formulieren und reagieren)"
                }
            ]
        },
        "quiz": [
            {
                "id": "A1_L15_Q1",
                "type": "EXAM_REAL",
                "question": "歌德A1写信给老师请假，开头最适宜的礼貌称呼是：",
                "options": ["Sehr geehrte Frau Müller,", "Hallo Kumpel,", "Liebe Mama,", "Tschüss Lehrer,"],
                "correctIndex": 0,
                "explanation": "给老师、上司或正式机构写信必须使用尊敬称谓：Sehr geehrte Frau Müller / Sehr geehrter Herr..."
            },
            {
                "id": "A1_L15_Q2",
                "type": "EXAM_REAL",
                "question": "歌德A1考试中向考官请求大声重复一遍，最地道礼貌的说法是：",
                "options": ["Können Sie das bitte wiederholen?", "Ich verstehe gar nichts!", "Sprich lauter!", "Was sagst du?"],
                "correctIndex": 0,
                "explanation": "Können Sie das bitte wiederholen? 是德语考试与日常交往中最得体的重复请求句型。"
            }
        ],
        "words": [
            ("die Prüfung", "die", "n.", "-en", "考试，测验", "Viel Erfolg bei der Goethe-Zertifikat-Prüfung!", "祝歌德证书考试旗开得胜！"),
            ("das Zertifikat", "das", "n.", "-e", "证书，合格文凭", "Ich habe das Goethe-Zertifikat A1 bestanden.", "我通过了歌德A1证书考试。"),
            ("bestehen", "", "v.", "besteht, bestand, bestanden", "通过（考试）", "Alle Teilnehmer haben die Prüfung bestanden.", "全体学员都顺利通过了考试。"),
            ("durchfallen", "", "v.", "fällt durch, fiel durch, ist durchgefallen", "考试不及格", "Keine Sorge, du wirst nicht durchfallen!", "别担心，你绝不会考不及格的！"),
            ("das Niveau", "das", "n.", "-s", "语言水准，级别", "Mein Deutschniveau liegt jetzt bei A1.", "我的德语水准现在达到了A1。"),
            ("die Aufgabe", "die", "n.", "-n", "考题，任务", "Lesen Sie die Aufgabenstellung genau durch!", "请仔细把题干要求读一遍！"),
            ("die Frage", "die", "n.", "-n", "问题，疑问", "Haben Sie noch eine Frage dazu?", "关于这个您还有疑问吗？"),
            ("die Antwort", "die", "n.", "-en", "答案，回答", "Welche Antwort ist richtig: A, B oder C?", "哪个答案是正确的：A、B还是C？"),
            ("antworten", "", "v.", "antwortet, antwortete, geantwortet", "回答", "Antworten Sie bitte in ganzen Sätzen!", "请用完整的句子作答！"),
            ("verstehen", "", "v.", "versteht, verstand, verstanden", "理解，听懂", "Haben Sie alles gut verstanden?", "您都听懂理解清楚了吗？"),
            ("erklären", "", "v.", "erklärt, erklärte, erklärt", "解释，说明", "Der Prüfer erklärt die Prüfungsregeln.", "考官在说明考试考场纪律。"),
            ("die Erklärung", "die", "n.", "-en", "解释，说明", "Die Erklärung war sehr klar und deutlich.", "这段解释非常清晰明了。"),
            ("wiederholen", "", "v.", "wiederholt, wiederholte, wiederholt", "重复，复习", "Könnten Sie den Satz bitte wiederholen?", "您能把这个句子再重复一遍吗？"),
            ("die Wiederholung", "die", "n.", "-en", "复习；重复", "Wiederholung ist die Mutter des Lernens.", "温故而知新，复习是学习之母。"),
            ("üben", "", "v.", "übt, übte, geübt", "练习，操练", "Wir üben heute den mündlichen Teil.", "我们今天练习口语考试部分。"),
            ("die Übung", "die", "n.", "-en", "练习题，训练", "Machen Sie bitte die Übungen auf Seite 15!", "请完成第15页上的练习题！"),
            ("der Teil", "der", "n.", "-e", "部分，模块", "Die Prüfung besteht aus vier Teilen.", "考试由听读写说四个模块组成。"),
            ("das Hören", "das", "n.", "-", "听力理解", "Im Teil Hören gibt es kurze Dialoge.", "在听力部分有简短的对话。"),
            ("das Lesen", "das", "n.", "-", "阅读理解", "Im Teil Lesen liest man Briefe und Schilder.", "在阅读部分需要读信件和告示牌。"),
            ("das Schreiben", "das", "n.", "-", "书面表达，写作", "Im Schreiben füllt man ein Formular aus.", "在写作部分需要填写表格并写短文。"),
            ("das Sprechen", "das", "n.", "-", "口语表达", "Im Sprechen stellt man sich kurz vor.", "在口语部分首先做简短自我介绍。"),
            ("die Durchsage", "die", "n.", "-n", "广播通知，播音", "Achten Sie auf die Durchsage am Gleis!", "请注意站台上的广播播音通告！"),
            ("der Dialog", "der", "n.", "-e", "对话", "Hören Sie den Dialog und kreuzen Sie an!", "请听对话并在正确选项上打勾！"),
            ("ankreuzen", "", "v.", "kreuzt an, kreuzte an, angekreuzt", "打叉标记，勾选", "Kreuzen Sie die richtige Lösung an!", "请在正确解法选项上画勾！"),
            ("die Lösung", "die", "n.", "-en", "答案，解答", "Hier ist der Lösungsschlüssel zum Test.", "这是测试题的标准答案。"),
            ("richtig", "", "adj.", "richtiger, am richtigsten", "正确的", "Ist diese Antwort hier richtig?", "这个回答是正确的吗？"),
            ("falsch", "", "adj.", "falscher, am falschsten", "错误的", "Nein, das ist leider falsch.", "不，遗憾这个选项是错误的。"),
            ("der Fehler", "der", "n.", "-", "错误", "Aus Fehlern lernt man am meisten.", "人从错误中学到的东西最多。"),
            ("das Beispiel", "das", "n.", "-e", "范例，例题", "Schauen Sie sich zuerst das Beispiel an!", "请大家首先看一下例题！"),
            ("zum Beispiel", "", "phrase", "", "例如，比如", "Viele Hobbys, zum Beispiel Sport und Musik.", "很多爱好，比如体育和音乐。"),
            ("der Text", "der", "n.", "-e", "文章，文本", "Lesen Sie den Text aufmerksam durch!", "请聚精会神通读文章！"),
            ("die Notiz", "die", "n.", "-en", "便签，简短备忘", "Hinterlassen Sie bitte eine kurze Notiz!", "请留下一张简短便签留言！"),
            ("der Zettel", "der", "n.", "-", "小纸条，便条", "Er schreibt die Nummer auf einen Zettel.", "他把号码记在一张纸条上。"),
            ("die Anzeige", "die", "n.", "-n", "广告，启事", "In der Zeitung steht eine Wohnungsanzeige.", "报纸上刊登着一则租房广告。"),
            ("das Schild", "das", "n.", "-er", "指示牌，告示", "Was bedeutet dieses Schild an der Tür?", "门上的这块指示牌是什么意思？"),
            ("das Formular", "das", "n.", "-e", "表格，报名申请表", "Füllen Sie dieses Formular bitte aus!", "请填写这份申请表格！"),
            ("ausfüllen", "", "v.", "füllt aus, füllte aus, ausgefüllt", "填写（表格各项）", "Name, Vorname und Adresse ausfüllen.", "填写姓名以及家庭住址。"),
            ("die Unterschrift", "die", "n.", "-en", "签名，落款", "Hier unten fehlt noch Ihre Unterschrift.", "这里下方还缺您的亲笔签名。"),
            ("unterschreiben", "", "v.", "unterschreibt, unterschrieb, unterschrieben", "签字，签署", "Bitte unterschreiben Sie mit Datum!", "请签署您的姓名并注明日期！"),
            ("der Absender", "der", "n.", "-", "寄件人，发信人", "Der Absender steht oben links auf dem Brief.", "发件人地址写在信封左上方。"),
            ("der Empfänger", "der", "n.", "-", "收件人，收信人", "Der Empfänger wohnt in Hamburg.", "收件人居住在汉堡市。"),
            ("die Anrede", "die", "n.", "-n", "称呼，抬头称谓", "Die formelle Anrede lautet: Sehr geehrte...", "正式称呼为：尊敬的..."),
            ("der Gruß", "der", "n.", "Grüße", "问候，致意", "Mit freundlichen Grüßen verbleibe ich...", "此致敬礼，我谨致以诚挚问候..."),
            ("die Grüße", "die", "n.pl.", "-", "问候，致意（复数）", "Viele Grüße aus dem schönen Schwarzwald!", "从美丽的黑森林发来热忱问候！"),
            ("die Einladung", "die", "n.", "-en", "邀请信，请柬", "Ich habe eine Einladung zur Hochzeit erhalten.", "我收到了一封婚礼请柬。"),
            ("die Bitte", "die", "n.", "-n", "请求，托付", "Ich habe eine große Bitte an Sie.", "我有一件重要的事请求您帮助。"),
            ("bitten", "", "v.", "bittet, bat, gebeten", "请求，恳请", "Darf ich Sie um einen Gefallen bitten?", "我能请您帮个忙吗？"),
            ("danken", "", "v.", "dankt, dankte, gedankt", "感谢 (接Dativ)", "Ich danke Ihnen für Ihre Unterstützung.", "我非常感谢您的鼎力支持。"),
            ("entschuldigen", "", "v.", "entschuldigt, entschuldigte, entschuldigt", "向...致歉", "Entschuldigen Sie bitte meine Verspätung!", "请原谅我的迟到！"),
            ("die Verspätung", "die", "n.", "-en", "迟到，延误", "Entschuldigung für die zehnminütige Verspätung.", "对迟到了十分钟深表歉意。"),
            ("der Termin", "der", "n.", "-e", "约会，预约时间", "Können wir den Termin auf Freitag verlegen?", "我们能把预约挪到周五吗？"),
            ("vereinbaren", "", "v.", "vereinbart, vereinbarte, vereinbart", "商定，预约", "Einen festen Termin beim Arzt vereinbaren.", "和医生敲定一个确切的就诊时间。"),
            ("verschieben", "", "v.", "verschiebt, verschob, verschoben", "改期，推迟", "Ich muss die Besprechung leider verschieben.", "很遗憾我不得不推迟会议。"),
            ("absagen", "", "v.", "sagt ab, sagte ab, abgesagt", "取消", "Er muss wegen Krankheit leider absagen.", "他因病遗憾必须取消会面。"),
            ("vorstellen", "", "v.", "stellt vor, stellte vor, vorgestellt", "自我介绍；引见", "Darf ich mich kurz vorstellen?", "允许我做个简短的自我介绍吗？"),
            ("die Vorstellung", "die", "n.", "-en", "自我介绍；演出", "Eine kurze persönliche Vorstellung im Kurs.", "在班级里做一个简短的个人自我介绍。"),
            ("das Herkunftsland", "das", "n.", "Herkunftsländer", "籍贯国，祖籍国", "Mein Herkunftsland ist China.", "我的原籍国是中国。"),
            ("der Wohnort", "der", "n.", "-e", "居住地，常住城市", "Mein derzeitiger Wohnort ist Berlin.", "我目前的居住地是柏林。"),
            ("die Muttersprache", "die", "n.", "-n", "母语", "Chinesisch ist meine Muttersprache.", "中文是我的母语。"),
            ("die Fremdsprache", "die", "n.", "-n", "外语", "Deutsch ist meine zweite Fremdsprache.", "德语是我的第二门外语。"),
            ("buchstabieren", "", "v.", "buchstabiert, buchstabierte, buchstabiert", "拼读出字母", "Buchstabieren Sie bitte Ihren Nachnamen!", "请拼读出您的姓氏字母！"),
            ("langsam", "", "adj./adv.", "langsamer, am langsamsten", "慢的，放慢", "Sprechen Sie bitte ein bisschen langsamer!", "请您说话稍微放慢一点点速度！"),
            ("deutlich", "", "adj./adv.", "deutlicher, am deutlichsten", "清晰的，明确的", "Bitte sprechen Sie laut und deutlich!", "请大声且清晰地说话！"),
            ("leise", "", "adj./adv.", "leiser, am leisesten", "小声的，轻柔的", "Im Lesesaal muss man leise sein.", "在阅览室必须保持轻声安静。"),
            ("wichtig", "", "adj.", "wichtiger, am wichtigsten", "重要的，关键的", "Pünktlichkeit ist in Deutschland sehr wichtig.", "守时在德国非常重要。"),
            ("einfach", "", "adj.", "einfacher, am einfachsten", "简单的，简易的", "Die erste Aufgabe war wirklich einfach.", "第一道题确实非常简单。"),
            ("schwierig", "", "adj.", "schwieriger, am schwierigsten", "困难的，复杂的", "Die deutsche Grammatik ist anfangs schwierig.", "德语语法起初阶段比较困难。"),
            ("die Hilfe", "die", "n.", "-", "帮助，援助", "Brauchen Sie bei der Aufgabe Hilfe?", "这道题您需要帮助吗？"),
            ("helfen", "", "v.", "hilft, half, geholfen", "帮助", "Können Sie mir bitte einen Moment helfen?", "您能稍微帮我一下吗？"),
            ("das Wörterbuch", "das", "n.", "Wörterbücher", "词典，字典", "Im Wörterbuch schlage ich unbekannte Vokabeln nach.", "我在词典里查阅生词。")
        ]
    }
]
