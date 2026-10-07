#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A2 Part 3: Lessons 11 to 15 (350 words)
L11: 文化艺术、博物馆与闲暇娱乐 (Kultur, Freizeit & Unterhaltung) - 70 words
L12: 环境保护、垃圾分类与气候变化 (Umwelt, Mülltrennung & Klima) - 70 words
L13: 社交网络、大众传媒与数字化生活 (Medien, Internet & Kommunikation) - 70 words
L14: 传统节庆、民间习俗与社交礼仪 (Bräuche, Feste & Höflichkeit) - 70 words
L15: 歌德 A2 全真模拟与应试冲刺 (Goethe A2 Prüfungstraining & Modelltest) - 70 words
"""

LESSONS_A2_PART3 = [
    # LESSON 11
    {
        "id": "A2_L11",
        "title": "第11课：文化艺术、博物馆与闲暇娱乐 (Kultur & Freizeit)",
        "summary": "掌握关系从句入门 (Relativsätze im Nominativ/Akkusativ)、德语区著名艺术文化与演艺场馆",
        "grammar": {
            "title": "关系从句 (Relativsätze) 第一格与第四格",
            "sections": [
                {
                    "heading": "1. 关系代词形态（等同于定冠词，唯第三格复数等特殊）：",
                    "content": "• 第一格：der Mann, der... / die Frau, die... / das Kind, das... / die Leute, die...\n• 第四格：der Mann, den... / die Frau, die... / das Kind, das... / die Leute, die...\n• 从句语序：变位动词永远置于从句句末！\n例：Das ist der Film, den ich gestern im Kino gesehen habe."
                },
                {
                    "heading": "2. 文化娱乐常用评价句型",
                    "content": "• Das Theaterstück hat mich tief beeindruckt / bewegt.\n• Die Ausstellung moderner Kunst ist absolut sehenswert."
                }
            ]
        },
        "quiz": [
            {
                "id": "A2_L11_Q1",
                "type": "GRAMMAR_FILL",
                "question": "Hier ist das Museum, ______ (关系代词，中性第一格) montags geschlossen ist.",
                "options": ["das", "der", "die", "dem"],
                "correctIndex": 0,
                "explanation": "先行词 das Museum 是中性，在从句中作主语（第一格），关系代词为 das。"
            },
            {
                "id": "A2_L11_Q2",
                "type": "VOCAB_MEANING",
                "question": "德国文化海报上常出现的 'sehenswert' 意思是：",
                "options": ["值得一看的，不容错过的", "门票昂贵的", "看不清楚的", "视力受损的"],
                "correctIndex": 0,
                "explanation": "sehenswert 意为“值得一览、非常值得观看欣赏的”。"
            }
        ],
        "words": [
            ("die Kultur", "die", "n.", "-en", "文化艺术，人类文明", "Deutschland verfügt über eine reiche literarische Kultur.", "德国拥有极其丰富璀璨的文学与哲学文化遗产。"),
            ("kulturell", "", "adj.", "", "文化范畴的人文的", "Ein kultureller Abend mit Oper und Kammermusik.", "一个沉浸在歌剧与室内交响乐之中的高雅文化之夜。"),
            ("die Kunst", "die", "n.", "Künste", "造型表现艺术，美术", "Zeitgenössische Kunst regt zum Nachdenken und Diskutieren an.", "发人深省的当代艺术激发了大众持续的哲思与论辩。"),
            ("der Künstler", "der", "n.", "-", "艺术家，创作者", "Der Künstler stellt seine Skulpturen in einer Galerie aus.", "这位创作者在一家知名独立艺术画廊展出其雕塑。"),
            ("die Künstlerin", "die", "n.", "-nen", "女艺术家", "Die Künstlerin verbindet traditionelle Malerei mit Fotografie.", "女艺术家将传统布面油画技法与先锋纪实摄影相融。"),
            ("das Kunstwerk", "das", "n.", "-e", "传世艺术珍品，杰作", "Das berühmte Kunstwerk wird streng bewacht und gesichert.", "这件举世闻名的传世艺术瑰宝受到了全天候严密安保。"),
            ("das Museum", "das", "n.", "Museen", "综合性博物馆，陈列馆", "Die Staatlichen Museen zu Berlin besitzen Weltrang.", "柏林国家博物馆群在世界各大文博机构中享有一流声誉。"),
            ("die Galerie", "die", "n.", "-n", "美术画廊，陈列走廊", "In der Galerie werden Werke junger Talente gezeigt.", "在这间前沿画廊里正集中展示青年新秀艺术家的力作。"),
            ("die Ausstellung", "die", "n.", "-en", "专题博览展览展会", "Die Ausstellung über den Expressionismus ist sehenswert.", "这场以表现主义流派为轴心的专题大展极其值得一观。"),
            ("ausstellen", "", "v.", "stellt aus, stellte aus, ausgestellt", "公开展出，陈列展出", "Mehrere Museen stellen ihre Schätze gemeinsam aus.", "数家博物馆强强联合将其镇馆之宝共同公开展出。"),
            ("das Exponat", "das", "n.", "-e", "参展展品，展陈实物", "Das älteste Exponat ist über fünftausend Jahre alt.", "全场历史最为悠久的珍贵展品距今已有五千余年历史。"),
            ("die Führung", "die", "n.", "-en", "人工导览解说，带团", "Wir nehmen an einer einstündigen Führung durch den Dom teil.", "我们报名参加了一场时长一小时的大教堂专家导览。"),
            ("der Museumsführer", "der", "n.", "-", "博物馆专业讲解员", "Der Museumsführer erläutert detailreich die Historie.", "博物馆专业讲解员极其详尽生动地向游客阐发历史。"),
            ("der Audioguide", "der", "n.", "-s", "电子语音导览机", "Der Audioguide ist in zehn verschiedenen Sprachen verfügbar.", "便携式电子语音导览设备支持十种国际语言自由切换。"),
            ("der Eintritt", "der", "n.", "-", "准入入场，入内权限", "Für Kinder unter zwölf Jahren ist der Eintritt frei.", "凡十二周岁以下未成年孩童进馆均可免收任何门票。"),
            ("die Eintrittskarte", "die", "n.", "-n", "入场券，参观纸质门票", "Kaufen Sie die Eintrittskarten vorab online ohne Anstehen!", "提前在线订购电子门票入馆即可免去现场排队长龙！"),
            ("der Rabatt", "der", "n.", "-e", "票价折让，优惠幅度", "Mit dem Familienpass erhalten Eltern und Kinder Rabatt.", "凭当地家庭优待卡父母携子女购票可享专项票折优惠。"),
            ("die Ermäßigung", "die", "n.", "-en", "教育折扣减免，优待", "Senioren und Studenten erhalten eine ermäßigte Karte.", "年满六旬老人与在读大学生皆可依法申领优待优惠票。"),
            ("das Theater", "das", "n.", "-", "话剧剧院，表演殿堂", "Das Deutsche Theater in Berlin inszeniert klassische Dramen.", "柏林德意志剧院时常排演极富深厚意蕴的经典传世大戏。"),
            ("das Theaterstück", "das", "n.", "-e", "舞台戏剧作品，话剧", "Ein ergreifendes Theaterstück über Freiheit und Mut.", "一部关于捍卫自由意志与人类非凡勇气的感人话剧。"),
            ("das Drama", "das", "n.", "Dramen", "正剧戏剧文学，悲剧", "Goethes 'Faust' gilt als das bedeutendste Drama deutscher Zunge.", "歌德笔下的巨著《浮士德》被公认为德语戏剧文学巅峰。"),
            ("die Bühne", "die", "n.", "-n", "演艺舞台，台前演出", "Die Schauspieler betreten unter tosendem Applaus die Bühne.", "一众杰出演员在全场雷鸣般的喝彩掌声中缓步走上舞台。"),
            ("die Aufführung", "die", "n.", "-en", "现场公开演艺公演", "Die Premiere der neuen Aufführung war restlos ausverkauft.", "这出新剧的首演场次全部坐席早早被热心戏迷抢购一空。"),
            ("die Premiere", "die", "n.", "-n", "全球全剧首度公演", "Zur Premiere erschienen zahlreiche Prominente und Kritiker.", "首映与首演礼当晚云集了数不胜数的各界名流与犀利剧评家。"),
            ("die Probe", "die", "n.", "-n", "舞台排练；样品化验", "Die Generalprobe vor der großen Premiere verlief fehlerfrei.", "正式盛大首演前最后一次全要素总彩排进行得天衣无缝。"),
            ("proben", "", "v.", "probt, probte, geprobt", "演练剧目，排练", "Das Orchester probt täglich stundenlang an der Sinfonie.", "管弦交响乐团每天都要耗费数小时潜心演练这部交响乐。"),
            ("der Regisseur", "der", "n.", "-e", "剧目影视总导演", "Der Regisseur wählte eine moderne und mutige Interpretation.", "总导演极其大胆地选用了极具现代主义张力的前卫诠释。"),
            ("die Regisseurin", "die", "n.", "-nen", "女性总导演", "Die Regisseurin gewann den Goldenen Bären auf der Berlinale.", "这位杰出的女导演在柏林国际电影节上斩获了最高金熊奖。"),
            ("die Rolle", "die", "n.", "-n", "舞台扮演角色，戏份", "Er schlüpft meisterhaft in die Rolle des Bösewichts.", "他极其出神入化地将剧中大反派的险恶与挣扎演绎得淋漓。"),
            ("spielen", "", "v.", "spielt, spielte, gespielt", "登台出演，弹奏乐曲", "Wer spielt heute Abend die anspruchsvolle Hauptrolle?", "今晚究竟由谁来挑大梁出演这个难度极高的人格分裂主角？"),
            ("die Oper", "die", "n.", "-n", "高雅西洋歌剧，歌剧院", "Die Wiener Staatsoper zählt zu den besten Häusern weltweit.", "维也纳国家歌剧院跻身全球公认最顶尖的艺术圣殿之列。"),
            ("das Ballett", "das", "n.", "-s", "古典足尖芭蕾舞剧", "Tschaikowskis 'Schwanensee' ist das bekannteste Ballett.", "柴可夫斯基谱写的经典《天鹅湖》堪称流传最广的芭蕾。"),
            ("das Orchester", "das", "n.", "-", "大型交响管弦乐团", "Die Berliner Philharmoniker sind ein weltberühmtes Orchester.", "柏林爱乐乐团是一支享誉全球国际乐坛的顶级交响乐团。"),
            ("der Dirigent", "der", "n.", "-en", "交响乐团总指挥", "Der Dirigent hebt den Taktstock und das Konzert beginnt.", "总指挥缓缓扬起指挥棒，全场宏大的交响篇章随即鸣响。"),
            ("die Philharmonie", "die", "n.", "-n", "管弦交响爱乐音乐厅", "Die markante Philharmonie in Berlin besticht durch Akustik.", "柏林标志性的爱乐音乐厅凭借登峰造极的声学效果闻名。"),
            ("das Konzert", "das", "n.", "-e", "现场音乐会，演奏会", "Ein klassisches Konzert mit Meisterwerken von Ludwig van Beethoven.", "一场倾情呈现路德维希·凡·贝多芬传世神作的古典音乐盛宴。"),
            ("der Applaus", "der", "n.", "-", "全场欢呼掌声雷鸣", "Minutenlanger, begeisterter Applaus für die Pianistin.", "全场观众为台上才华横溢的女钢琴家奉献了经久不息的掌声。"),
            ("klatschen", "", "v.", "klatscht, klatschte, geklatscht", "鼓掌致意，拍手拍击", "Das Publikum stand auf und klatschte im stürmischen Rhythmus.", "全场听众激动得全员起立，合着热烈奔放的节拍击节叫好。"),
            ("die Zugabe", "die", "n.", "-n", "返场加演加唱曲目", "Auf lauten Wunsch des Publikums spielte er noch zwei Zugaben.", "在全场热忱挽留呼喊声中他再度返场加演了两首返场小品。"),
            ("die Leinwand", "die", "n.", "Leinwände", "影院大银幕；画布", "Die Hollywood-Produktion flimmert über die riesige Leinwand.", "好莱坞大制作巨片在影城巨幅激光IMAX银幕上震撼放映。"),
            ("der Spielfilm", "der", "n.", "-e", "剧情长片，故事片", "Ein packender Spielfilm über historische Begebenheiten.", "一部根据重大真实历史历史事件改编的情节跌宕剧情故事片。"),
            ("der Dokumentarfilm", "der", "n.", "-e", "真实人文纪录片", "Ein preisgekrönter Dokumentarfilm über den Klimawandel in der Arktis.", "一部荣获国际大奖、深度聚焦北极冰川气候危机的纪实纪录片。"),
            ("die Serie", "die", "n.", "-n", "电视网络剧集，连续剧", "Er schaut am Wochenende gerne ganze Staffeln einer Serie an.", "每逢周末他最喜欢一口气刷完一整季跌宕起伏的悬疑连续剧。"),
            ("die Folge", "die", "n.", "-n", "剧集单集单回，后果", "Heute Abend läuft die spannende letzte Folge der Krimiserie.", "今晚将迎来这部扣人心弦的刑侦罪案剧集大结局最后一集。"),
            ("der Trailer", "der", "n.", "-", "影视预告宣传片", "Der Trailer verrät bereits erste dramatische Szenen der Handlung.", "先行预告片中已经提前揭晓了本剧部分剑拔弩张的高潮戏码。"),
            ("die Untertitel", "die", "n.pl.", "-", "影视剧原声翻译字幕", "Ich schaue deutsche Filme gerne mit deutschen Untertiteln.", "我看德国原声电影时最喜欢同步挂上精准的德语原生双字幕。"),
            ("die Synchronisation", "die", "n.", "-en", "译制片专业原声配音", "In Deutschland haben Synchronisationen ein sehr hohes Niveau.", "德国译制片在角色情绪对口型与专业台词配音上水准极高。"),
            ("das Kino", "das", "n.", "-s", "商业影城，放映厅", "Das Programmkino zeigt anspruchsvolle Arthouse-Produktionen.", "这间艺术影院专门长线排映极富思想艺术深度的文艺片。"),
            ("die Vorstellung", "die", "n.", "-en", "电影场次放映，演出", "Die Spätvorstellung am Freitagabend um 22 Uhr 30.", "周五深夜十点半排映的那场极受年轻情侣追捧的午夜场次。"),
            ("das Popcorn", "das", "n.", "-", "影院膨化爆米花", "Eine große Tüte süßes oder salziges Popcorn zum Film.", "看电影必不可少的大桶香甜或咸香口味现爆大颗爆米花。"),
            ("das Ticket", "das", "n.", "-s", "入场凭证电子影票", "Wir haben die Kinotickets bequem per App reserviert.", "我们通过手机应用程序极其丝滑顺畅地提前锁定了电影票。"),
            ("die Reihe", "die", "n.", "-n", "影院排号座席排", "Zwei Plätze in Reihe 8 genau in der perfekten Mitte.", "位于第八排正中央黄金观影视角绝佳位置的两个连座。"),
            ("das Festival", "das", "n.", "-s", "盛大艺术节，电影节", "Die Berlinale ist eines der weltweit wichtigsten Filmfestivals.", "柏林国际电影节堪称全球最具国际行业影响力三大电影节之一。"),
            ("der Preis", "der", "n.", "-e", "评审团大奖，奖项", "Der Film wurde mit mehreren begehrten Preisen ausgezeichnet.", "该部佳作在颁奖礼上一举斩获了多座含金量十足的评审团大奖。"),
            ("auszeichnen", "", "v.", "zeichnet aus, zeichnete aus, ausgezeichnet", "表彰嘉奖授勋", "Sie wurde für ihr außergewöhnliches Lebenswerk feierlich ausgezeichnet.", "鉴于她为电影艺术做出的卓越毕生贡献，组委会为她颁发终身成就大奖。"),
            ("die Auszeichnung", "die", "n.", "-en", "荣誉勋章，嘉奖", "Die Auszeichnung erfüllt die gesamte Filmcrew mit Stolz.", "这项沉甸甸的殊荣令参与影片摄制的全体主创人员倍感自豪。"),
            ("begeistert", "", "adj.", "begeisterter, am begeistertsten", "狂热迷恋赞叹不已的", "Die Zuschauer verließen begeistert und tief berührt den Saal.", "终场亮灯时观众无一不怀着满腔赞叹与深深动容缓缓离场。"),
            ("die Begeisterung", "die", "n.", "-", "全场狂热激情澎湃", "Die Begeisterung für Live-Konzerte ist ungebrochen groß.", "大众对亲临现场聆听万人室内外音乐节的热情始终未减。"),
            ("beeindrucken", "", "v.", "beeindruckt, beeindruckte, beeindruckt", "深深震撼打动", "Seine herausragende Gesangsstimme beeindruckte das Publikum.", "他那充满穿透力与金属质感的非凡歌喉深深震撼了全场。"),
            ("beeindruckend", "", "adj.", "beeindruckender, am beeindruckendsten", "叹为观止令人震撼的", "Die Akustik der Elbphilharmonie in Hamburg ist beeindruckend.", "汉堡易北爱乐音乐厅内部极其精湛绝伦的声场设计令人叹为观止。"),
            ("langweilig", "", "adj.", "langweiliger, am langweiligsten", "枯燥乏味令人昏昏欲睡的", "Das Buch war derart langweilig, dass ich dabei einschlief.", "那本小说的行文与剧情实在是枯燥平庸，读着读着我便睡着了。"),
            ("die Langeweile", "die", "n.", "-", "百无聊赖乏味虚无感", "Gegen Langeweile an Regentagen hilft ein gutes Buch.", "在阴雨连绵被困在家的日子里，读本好书能彻底驱散无聊感。"),
            ("spannend", "", "adj.", "spannender, am spannendsten", "扣人心弦悬念迭起的", "Ein extrem spannender Kriminalroman, den man nicht weglegen kann.", "一部扣人心弦、案情扑朔迷离让人一旦拿起来便舍不得放下的悬疑小说。"),
            ("die Spannung", "die", "n.", "-en", "戏剧张力，紧绷悬念", "Der Regisseur baut die dramatische Spannung bis zur Spitze auf.", "导演极其老练地将整部戏的剧情冲突与悬疑张力一步步推向顶点。"),
            ("sehenswert", "", "adj.", "", "极富观赏价值值得一览的", "Das historische Schloss ist unbedingt und jederzeit sehenswert.", "这座保存完好的百年历史皇家古堡在任何季节都极其值得一览。"),
            ("empfehlenswert", "", "adj.", "empfehlenswerter, am empfehlenswertesten", "非常值得推荐打卡的", "Ein Besuch dieses traditionellen Lokals ist überaus empfehlenswert.", "去这家承载着百年风味的特色传统老店打卡是一项极受推崇的体验。"),
            ("besuchen", "", "v.", "besucht, besuchte, besucht", "登门参观，探访", "Wir besuchten während unseres Aufenthalts drei bekannte Theater.", "在当地旅居期间我们一口气登门探访并观摩了三座知名大剧院。"),
            ("teilnehmen", "", "v.", "nimmt teil, nahm teil, teilgenommen", "投身参与 (an + Dat)", "Er nimmt an einem dreitägigen kreativen Malkurs teil.", "他专程报名参加了一个为期三天的油画艺术创作实训班。"),
            ("das Vergnügen", "das", "n.", "-", "欢娱怡情，极大乐事", "Es war mir ein ganz außerordentliches Vergnügen, Sie kennenzulernen.", "今日能有幸在此与您相识交谈，对我而言实乃莫大的荣幸与乐事。"),
            ("unterhaltsam", "", "adj.", "unterhaltsamer, am unterhaltsamsten", "寓教于乐生动有趣的", "Ein heiterer und ungemein unterhaltsamer Abend im Kabarett.", "在政治讽刺喜剧小品秀剧场里度过了一个捧腹且妙趣横生的欢快夜晚。")
        ]
    },

    # LESSON 12
    {
        "id": "A2_L12",
        "title": "第12课：环境保护、垃圾分类与气候变化 (Umwelt & Klima)",
        "summary": "掌握情态动词第二虚拟式 (sollte 提建议)、德国家庭五色分类垃圾系统与低碳环保",
        "grammar": {
            "title": "情态动词 sollte 表达建议与环保生态",
            "sections": [
                {
                    "heading": "1. should 对应德语：sollte + 动词原形提出忠告建议",
                    "content": "• ich sollte, du solltest, er sollte, wir sollten, ihr solltet, sie sollten\n• 例句：Wir sollten weniger Plastik verbrauchen und mehr Müll trennen.\n• Man sollte öfter das Fahrrad statt des Autos nutzen."
                },
                {
                    "heading": "2. 德国著名的环保押金回收系统 (Pfandsystem)",
                    "content": "塑料瓶 (Einwegpfand: 0,25 €) 与玻璃瓶 (Mehrwegpfand: 0,08 € - 0,15 €) 可在超市自动回收机 (Pfandautomat) 投币打印押金代金券。"
                }
            ]
        },
        "quiz": [
            {
                "id": "A2_L12_Q1",
                "type": "GRAMMAR_FILL",
                "question": "Umweltbewusste Bürger ______ (sollen, 虚拟式提建议) mehr Energie sparen.",
                "options": ["sollten", "sollen", "sollte", "gesollt"],
                "correctIndex": 0,
                "explanation": "表达倡议与诚恳建议，复数主语使用第二虚拟式 sollten。"
            },
            {
                "id": "A2_L12_Q2",
                "type": "EXAM_REAL",
                "question": "在德国超市把喝完的带环保标志的饮料塑料瓶投入机器，打印出来的凭条叫：",
                "options": ["der Pfandbon", "der Fahrplan", "die Fahrkarte", "der Mietvertrag"],
                "correctIndex": 0,
                "explanation": "der Pfandbon 是饮料瓶押金返还机打印出的押金抵用代金小票。"
            }
        ],
        "words": [
            ("die Umwelt", "die", "n.", "-", "生态自然环境", "Der Schutz unserer Umwelt muss höchste politische Priorität haben.", "保护我们赖以生存的生态自然环境必须置于施政首要最高优先级。"),
            ("der Umweltschutz", "der", "n.", "-", "环境保护，生态保育", "Jeder Einzelne kann im Alltag einen Beitrag zum Umweltschutz leisten.", "我们每个人都完全能够在柴米油盐的日常起居中为环保贡献一份力量。"),
            ("umweltfreundlich", "", "adj.", "umweltfreundlicher, am umweltfreundlichsten", "环境友好型绿色的", "Fahrradfahren ist das umweltfreundlichste Fortbewegungsmittel in der Stadt.", "骑行自行车毫无疑问是穿梭于城市大街小巷最为环保绿色的出行方式。"),
            ("das Klima", "das", "n.", "-", "全球宏观气候", "Das weltweite Klima verändert sich durch Treibhausgase dramatisch.", "受过量温室气体排放温室效应裹挟，全球宏观气候正发生剧烈变异。"),
            ("der Klimawandel", "der", "n.", "-", "全球气候变暖变化", "Der Klimawandel führt weltweit zu mehr Wetterextremen und Dürren.", "全球气候变暖恶化直接导致极端灾害性天气与干旱肆虐频发。"),
            ("die Erwärmung", "die", "n.", "-", "气温攀升，变暖效应", "Die globale Erwärmung lässt die Polkappen und Alpengletscher schmelzen.", "全球地表平均气温的持续攀升正加速两极极地冰冠与冰川的消融。"),
            ("das Treibhausgas", "das", "n.", "-e", "温室效应有害气体", "Industrienationen müssen den Ausstoß von Treibhausgasen drastisch senken.", "各大工业化国家有道义责任将工业生产活动中的温室气体排放断崖削减。"),
            ("die Emission", "die", "n.", "-en", "废气碳排放，排污量", "Moderne Filtersysteme verringern die schädlichen Emissionen der Fabriken.", "加装先进的多级静电除尘脱硫系统能将工厂烟囱有害排放降至最低。"),
            ("der Ausstoß", "der", "n.", "-", "废气直接排放量", "Der Ausstoß von CO2 muss bis 2030 halbiert werden.", "到2030年全社会二氧化碳的直接碳排放量必须依法实现削减过半。"),
            ("das Kohlendioxid", "das", "n.", "-", "二氧化碳气体", "Wälder binden gigantische Mengen des Treibhausgases Kohlendioxid.", "连绵广袤的原生原始森林作为绿肺能够固化吸收天量二氧化碳。"),
            ("die Energie", "die", "n.", "-n", "电能能源，动力动力源", "Die Zukunft gehört den sauberen, erneuerbaren Energien.", "整个人类社会的明天与未来必将完完全全属于清洁安全的可再生能源。"),
            ("erneuerbar", "", "adj.", "", "可持续循环再生的", "Erneuerbare Energien wie Wind und Sonne schonen endliche Ressourcen.", "风力与太阳能等可再生自然禀赋能源能够有效涵养不可再生的宝贵矿产。"),
            ("die Solarenergie", "die", "n.", "-", "太阳能光伏发电", "Auf vielen Dächern wandelt Solarenergie Sonnenlicht direkt in Strom um.", "越来越多民居屋顶铺装光伏瓦板，将灿烂太阳光能就地直接转化为绿色电力。"),
            ("die Solaranlage", "die", "n.", "-n", "光伏太阳能发电阵列", "Die Investition in eine moderne Solaranlage amortisiert sich nach Jahren.", "投资装配一套顶配高转化率的家庭光伏系统数年内即可完全实现成本摊平收回。"),
            ("die Windkraft", "die", "n.", "-", "风电风力能源资源", "An der windreichen Nordseeküste liefert die Windkraft sauberen Strom.", "在大风呼啸不绝的北海开阔沿海，风电机组夜以继日向大网输送清洁电能。"),
            ("das Windrad", "das", "n.", "Windräder", "大型风力发电机大风车", "Immer mehr moderne Windräder prägen die deutsche Kulturlandschaft.", "一座座拔地而起的大型现代风力发电机正在重塑德国原野的田园风景线。"),
            ("die Wasserkraft", "die", "n.", "-", "水库水电水力能源", "Wasserkraftwerke nutzen die kinetische Energie strömender Gebirgsflüsse.", "梯级水电枢纽工程科学利用崇山峻岭高山河流下泄蕴藏的奔腾水能。"),
            ("der Ökostrom", "der", "n.", "-", "绿色清洁认证电力", "Viele Verbraucher wechseln bewusst zu Anbietern von reinem Ökostrom.", "广大家庭消费者秉持环保初衷主动改签全部采购百分百绿电的电网服务套餐。"),
            ("die Kohle", "die", "n.", "-", "地质煤炭矿石", "Deutschland hat den schrittweisen Ausstieg aus der Braunkohle beschlossen.", "德国国家层面已通过立法形式敲定有序彻底退出褐煤火力发电历史大幕。"),
            ("der Ausstieg", "der", "n.", "-e", "彻底退役关停退出", "Der Beschluss über den endgültigen Ausstieg aus der Atomkraft steht fest.", "国家彻底全面关停淘汰所有民用核裂变核电反应堆的历史决议已尘埃落定。"),
            ("die Atomkraft", "die", "n.", "-", "核裂变核能能源", "Die Diskussion über die Risiken der Atomkraft dauerte viele Jahrzehnte an.", "在德意志土地上关于核电运行隐患与核废料安全的大争论整整持续了数十年。"),
            ("das Kernkraftwerk", "das", "n.", "-e", "商用核能发电厂", "Das letzte deutsche Kernkraftwerk ging im Frühjahr 2023 endgültig vom Netz.", "德国本土运行的最后一座核电厂机组已于2023年春彻底断网解列停运。"),
            ("der Atommüll", "der", "n.", "-", "高放射性危险核废料", "Die sichere Endlagerung für gefährlichen Atommüll ist weltweit ungelöst.", "为致命高放射性核废料寻找一个能确保数十万年绝对安全的地质深处封存地。"),
            ("die Ressource", "die", "n.", "-n", "天然矿产资源财富", "Der sparsame Umgang mit natürlichen Ressourcen sichert unser Überleben.", "对大自然馈赠的天然资源厉行节约与高效循环是我们人类代际生存的命脉。"),
            ("sparen", "", "v.", "spart, sparte, gespart", "开源节流，节约耗费", "Schalten Sie das Licht aus, um im Haushalt wertvollen Strom zu sparen!", "离开屋子顺手关灯，从小事做起在日常起居中为全家节约宝贵的度数电费！"),
            ("die Verschwendung", "die", "n.", "-en", "大肆暴殄天物挥霍浪费", "Die Vermeidung von Lebensmittelverschwendung spart Milliarden Euro.", "从源头坚决杜绝粮食与生鲜食材的大肆浪费每年能替社会挽回巨额财富。"),
            ("verschwenden", "", "v.", "verschwendet, verschwendete, verschwendet", "挥霍浪掷，滥用", "Lassen Sie das Wasser beim Einseifen nicht ungenutzt verschwenden!", "在涂抹沐浴露起泡清洗时切莫任凭水龙头哗哗空流浪费珍贵水资源！"),
            ("der Müll", "der", "n.", "-", "生活各类废弃物，垃圾", "In deutschen Städten liegt im Vergleich zu anderen Metropolen wenig Müll.", "相较于全球诸多国际化大都会，德国城市街头巷尾的废弃物遗撒极少。"),
            ("der Abfall", "der", "n.", "Abfälle", "工业生活残渣废弃料", "Gefährlicher chemischer Abfall muss als Sondermüll entsorgt werden.", "含有剧毒与重金属的工业化学废料必须严格作为特种危废施行专业无害处置。"),
            ("der Biomüll", "der", "n.", "-", "厨余果皮有机易腐垃圾", "In die braune Biotonne gehören Kaffeesatz, Obstschalen und Speisereste.", "棕色专用厨余桶专门用来定点收集咖啡残渣渣滓、果皮及剩饭剩菜。"),
            ("der Restmüll", "der", "n.", "-", "无法分类杂质其他垃圾", "Asche und Staubsaugerbeutel gehören in den grauen Restmüllbehälter.", "打扫出的细微炉灰、碎渣及吸尘器集尘纸袋应丢入灰色其他垃圾桶。"),
            ("das Altpapier", "das", "n.", "-", "废旧报章纸板纸质包装", "Zeitungen und saubere Kartons werden in der blauen Papiertonne gesammelt.", "旧报刊、信封与干净未受油污浸染的包装硬纸箱应分类归入蓝色纸类桶。"),
            ("das Altglas", "das", "n.", "-", "各类废弃玻璃瓶玻璃器皿", "Altglas wird an Containern streng nach Weiß-, Grün- und Braunglas getrennt.", "在社区公共回收站投弃废玻璃瓶时必须严格依白、绿、棕三色投掷。"),
            ("der Glascontainer", "der", "n.", "-", "公共大型玻璃分类箱", "Bitte werfen Sie Flaschen nur außerhalb der Ruhezeiten in den Container!", "为了体恤周边居民，严禁在午间与夜间法定居民静息时段向玻璃箱扔瓶！"),
            ("das Plastik", "das", "n.", "-", "人工聚合物塑料", "Plastik zersetzt sich in der Natur erst nach vielen hundert Jahren.", "丢入自然界的塑料高分子材料需要历经数百年岁月洗礼方能缓慢降解。"),
            ("der Kunststoff", "der", "n.", "-e", "高分子人工合成材料塑料", "Recycelter Kunststoff wird für neue Verpackungen wiederverwertet.", "经过专业分选洗净的再生塑料颗粒被源源不断循环制成全新包装材料。"),
            ("die Verpackung", "die", "n.", "-en", "各类商品外层包装材料", "Kaufen Sie lose Früchte, um unnötige Plastikverpackungen zu vermeiden!", "尽量多选购散装生鲜水果，从源头坚决谢绝层层不必要的过度塑料裹包！"),
            ("die Plastiktüte", "die", "n.", "-n", "一次性塑料购物袋", "Verwenden Sie einen robusten Stoffbeutel statt einer neuen Plastiktüte!", "出门买菜带上一只结实耐用的纯棉布袋，彻底告别单次即抛塑料袋！"),
            ("der Stoffbeutel", "der", "n.", "-", "天然环保耐用布袋帆布袋", "Ein bunter Stoffbeutel lässt sich klein zusammenfalten und einstecken.", "一只印染漂亮的帆布布袋可以折叠得极小随身塞进外套口袋以备采买。"),
            ("die Dose", "die", "n.", "-n", "马口铁铝制易拉罐罐头", "Auf Aluminiumdosen für Getränke wird in Deutschland Pfand erhoben.", "在德国境内几乎所有装盛碳酸饮料的金属铝制易拉罐均依法强制征缴押金。"),
            ("das Pfand", "das", "n.", "-", "包装循环押金退费", "Vergessen Sie nicht, das Pfand für die leeren Wasserflaschen einzulösen!", "去超市时切记顺便带上积攒的空水瓶把抵押金在自动收瓶机前退换掉！"),
            ("das Pfandsystem", "das", "n.", "-e", "押金强制返还循环体系", "Das deutsche Pfandsystem erreicht eine vorbildliche Recyclingquote.", "德国推行的饮料容器押金退返运转机制实现了令人惊叹的高效回收率。"),
            ("der Pfandautomat", "der", "n.", "-en", "超市自动空瓶回收机", "Schieben Sie die leeren Flaschen mit dem Strichcode voran in den Automaten!", "请将喝空的干净瓶子条形码朝上平稳缓缓推入超市自动识别回收口中！"),
            ("recyceln", "", "v.", "recycelt, recycelte, recycelt", "再生循环利用处理", "Aluminium lässt sich mit geringem Energieaufwand beliebig oft recyceln.", "金属铝在工业冶炼回收中可以耗费极低电能近乎无限次重复回炉再生。"),
            ("das Recycling", "das", "n.", "-", "资源再生循环回收利用", "Effizientes Recycling schützt Gewässer und schont die Deponien.", "高效精密的再生循环加工能有效保护河流湖泊水体并减轻填埋场负荷。"),
            ("wiederverwenden", "", "v.", "verwendet wieder, verwendete wieder, wiederverwendet", "再次投入使用复用", "Mehrwegflaschen aus Glas werden bis zu fünfzig Mal wiederverwendet.", "用厚玻璃烧制成的多次循环周转瓶其平均复用周转寿命高达整整五十次。"),
            ("die Mehrwegflasche", "die", "n.", "-n", "多次循环周转流通瓶", "Entscheiden Sie sich beim Einkauf bewusst für umweltschonende Mehrwegflaschen!", "在酒水货架前选购时请明智偏向于支持绿色环保的多次周转玻璃瓶！"),
            ("die Einwegflasche", "die", "n.", "-n", "单次即抛一次性塑料瓶", "Einwegflaschen aus dünnem Plastik werden nach dem Schreddern recycelt.", "薄壁一次性塑料瓶在被回收机吞噬并就地绞碎压扁后送入化纤厂造粒。"),
            ("vermeiden", "", "v.", "vermeidet, vermied, vermieden", "从源头避免杜绝", "Müllvermeidung steht in der Hierarchie stets vor der Müllverwertung.", "在现代固体废物治理金字塔顶端，源头减量减废永远高于事后废料回收。"),
            ("entsorgen", "", "v.", "entsorgt, entsorgte, entsorgt", "合规专业清运弃置处理", "Alte Elektrogeräte darf man keinesfalls im Hausmüll entsorgen!", "报废的废旧小家电绝对严禁直接丢弃在普通生活垃圾收集箱里！"),
            ("die Entsorgung", "die", "n.", "-en", "废旧物品无害化清运处置", "Der Wertstoffhof kümmert sich um die fachgerechte Entsorgung von Giftstoffen.", "城市绿色生态循环中心专职统筹各类大件与有害有毒危废的专业分拣处置。"),
            ("der Wertstoffhof", "der", "n.", "Wertstoffhöfe", "大型再生资源分拣回收站", "Am Samstagvormittag bringen viele Bürger ihren Sperrmüll zum Wertstoffhof.", "周六清晨不少市民自己开车把家里淘汰的大件废旧桌椅运送到回收站。"),
            ("der Sperrmüll", "der", "n.", "-", "大件大型废旧家具杂物", "Alte Matratzen und ausgediente Holzschränke zählen zum Sperrmüll.", "塌陷的废弃弹簧床垫与拆烂的旧木质大衣柜均归入大件废弃垃圾类别。"),
            ("die Natur", "die", "n.", "-", "生机勃勃的大自然", "In unberührter Natur tankt der erschöpfte Stadtmensch neue Lebenskraft.", "在未经人工雕琢的原始野性大自然腹地，疲惫的都市客重新汲满能量。"),
            ("schützen", "", "v.", "schützt, schützte, geschützt", "悉心关爱保护卫护", "Wir müssen bedrohte Tier- und Pflanzenarten vor dem Aussterben schützen.", "全人类有不可推卸的责任关爱濒危野生物种免于在地球上永远彻底灭绝。"),
            ("der Wald", "der", "n.", "Wälder", "天然林区，林海", "Der Wald leidet unter langen Dürreperioden und dem Borkenkäfer.", "连绵的茂密天然林区正饱受近年来持续旷日持久的干旱与树皮蛀虫啃食。"),
            ("die Luft", "die", "n.", "-", "大气层，呼吸空气", "Die Luft in vielen Innenstädten hat sich erfreulich verbessert.", "得益于严格限行与新能源替代，许多城市中心区的空气质量明显改善。"),
            ("die Verschmutzung", "die", "n.", "-en", "有害排污，环境污染", "Die Verschmutzung der Meere durch Mikroplastik ist eine globale Katastrophe.", "微塑料颗粒对全球各大洋生态造成的无孔不入的污染堪称一场生态浩劫。"),
            ("verschmutzen", "", "v.", "verschmutzt, verschmutzte, verschmutzt", "污染环境，弄脏", "Industrieabwässer dürfen die Flüsse nicht länger ungestraft verschmutzen.", "工业有毒有害未经深度净化达标的废水源头直排必须受到国家法律严惩。"),
            ("das Trinkwasser", "das", "n.", "-", "高标准安全饮用水", "Leitungswasser in Deutschland hat eine exzellente Trinkwasserqualität.", "在全德境内直接从自家自来水龙头接出的自来水已达直饮水严苛指标。"),
            ("die Sparsamkeit", "die", "n.", "-", "克勤克俭，节用度", "Sparsamkeit beim Heizen senkt die Nebenkostenabrechnung drastisch.", "在秋冬供暖季合理调节温控阀门能将年终的物业能源暖气账单大幅压减。"),
            ("der Fußabdruck", "der", "n.", "Fußabdrücke", "生态足迹，碳足迹", "Wie groß ist dein persönlicher ökologischer Fußabdruck auf der Erde?", "你有没有算过自己在衣食住行日常中给地球留下的个人碳足迹有多大？"),
            ("nachhaltig", "", "adj.", "nachhaltiger, am nachhaltigsten", "经久不衰可持续发展的", "Nachhaltige Forstwirtschaft schlägt nur so viel Holz, wie nachwächst.", "秉持永续发展的林业经营采伐原则规定，采伐木材量严禁超过新生量。"),
            ("die Nachhaltigkeit", "die", "n.", "-", "可持续性，永续发展", "Nachhaltigkeit bedeutet Verantwortung für nachfolgende Generationen.", "可持续发展理念的本质就是对生活在未来的子孙后代肩负起庄严的历史责任。"),
            ("das Bio-Produkt", "das", "n.", "-e", "有机绿色认证农副产品", "Bio-Produkte stammen aus ökologisch kontrolliertem Anbau ohne Chemie.", "带有欧盟有机绿叶标的农产品产自全程不施加任何化学农药的生态农场。"),
            ("das Siegel", "das", "n.", "-", "官方品质认证印章标识", "Achten Sie beim Einkauf auf anerkannte staatliche Fairtrade-Siegel!", "在选购南美咖啡可可时请认准有公信力的官方公平贸易与有机认证印章！"),
            ("regional", "", "adj.", "", "当地就地取材本地的", "Regionale Produkte haben extrem kurze Transportwege und sind frisch.", "主打本地自产自销的时令果蔬拥有极短的物流半径且口感鲜美纯正。"),
            ("die Saison", "die", "n.", "-s", "时令农时，果蔬当造季", "Erdbeeren und Spargel schmecken am besten während ihrer natürlichen Saison.", "新鲜草莓与鲜嫩芦笋唯有在自然大地应季成熟的时令采摘品尝才最为甘美。"),
            ("saisonal", "", "adj.", "", "顺随时令当季应时的", "Kochen mit saisonalem Gemüse schont die Umwelt und den Geldbeutel.", "顺应时令节气取材下厨不仅大幅节省家庭伙食开支而且极为低碳环保。"),
            ("das Bewusstsein", "das", "n.", "-", "公众心智认知，认同感", "Das Umweltbewusstsein in der Bevölkerung ist in den letzten Jahren gewachsen.", "全社会普通百姓心中对绿色低碳与环境保护的心智认同感近年来显著跃升。")
        ]
    },

    # LESSON 13
    {
        "id": "A2_L13",
        "title": "第13课：社交网络、大众传媒与数字化生活 (Medien & Internet)",
        "summary": "掌握第三格与第四格人称代词双宾语语序法则、社交网络交际与数字隐私",
        "grammar": {
            "title": "双宾语语序规则 (Dativ- und Akkusativobjekt)",
            "sections": [
                {
                    "heading": "1. 名词双宾语规则：人前 (Dat) 物后 (Akk)",
                    "content": "• Ich schenke meinem Vater (Dat, 人) ein Buch (Akk, 物).\n• Er schickt der Kollegin eine wichtige E-Mail."
                },
                {
                    "heading": "2. 代词双宾语铁律：代词永远居先，若同为代词则物前 (Akk) 人后 (Dat)！",
                    "content": "• 口诀：代词永远往前抢，双代词时它 (Akk) 陪你 (Dat)！\n• Ich schenke es (das Buch, Akk) ihm (dem Vater, Dat).\n• Er schickt sie (die Mail, Akk) ihr (der Kollegin, Dat)."
                }
            ]
        },
        "quiz": [
            {
                "id": "A2_L13_Q1",
                "type": "GRAMMAR_FILL",
                "question": "Hast du dem Kollegen die Datei geschickt? - Ja, ich habe ______ (sie/ihm) vorhin geschickt.",
                "options": ["sie ihm", "ihm sie", "es ihm", "ihm es"],
                "correctIndex": 0,
                "explanation": "当宾语同为代词时，第四格代词必须置于第三格代词之前（sie ihm）。"
            },
            {
                "id": "A2_L13_Q2",
                "type": "VOCAB_MEANING",
                "question": "德语网络中针对个人隐私的法定义务词汇 'der Datenschutz' 意思是：",
                "options": ["数据安全与个人隐私保护", "电脑硬件防尘罩", "网络流量套餐", "数据下载加速"],
                "correctIndex": 0,
                "explanation": "der Datenschutz 是德国乃至全欧盟极其重视的“个人数据隐私保护”专业词汇。"
            }
        ],
        "words": [
            ("das Medium", "das", "n.", "Medien", "信息传播介质，媒体", "Die Medien prägen maßgeblich das Bild der öffentlichen Meinung.", "新闻大众媒体在极大层面上形塑着全社会公共舆论的基本走向。"),
            ("die Massenmedien", "die", "n.pl.", "-", "大众传播机构大众媒体", "Fernsehen, Radio und Zeitungen zählen zu den klassischen Massenmedien.", "电视广播、调频电台与纸质报章均隶属于最经典的传统大众媒体。"),
            ("das Internet", "das", "n.", "-", "万维网互联网世界", "Das Internet hat die globale Kommunikation revolutioniert.", "互联网的诞生在根本上彻底重塑了全人类信息交换与沟通的形态。"),
            ("das Netz", "das", "n.", "-e", "网络，互联网络", "Man findet heute fast jede Information blitzschnell im Netz.", "如今人们在互联网络上海量检索任何知识几乎都在弹指一瞬间。"),
            ("die Website", "die", "n.", "-s", "互联网站点，主页", "Die offizielle Website der Stadtverwaltung bietet viele Onlinedienste.", "市政府官方网站提供了便民利民的政务一网通办线上办理服务。"),
            ("die Homepage", "die", "n.", "-s", "机构个人门面主页", "Auf unserer Homepage finden Sie alle Kontaktdaten.", "在我们的机构门户主页上能够一目了然查看到全部办公联络电话。"),
            ("das Portal", "das", "n.", "-e", "综合性数字化门户", "Über das Bildungsportal laden Schüler ihre Materialien herunter.", "借助省属教育公共服务门户，广大学生可以按需免费下载教辅。"),
            ("die Suchmaschine", "die", "n.", "-n", "网络搜索引擎", "Geben Sie die Schlüsselbegriffe in eine moderne Suchmaschine ein!", "请将核心关键词键入高效的搜索引擎框中以便精准筛选海量网页！"),
            ("googeln", "", "v.", "googelt, googelte, gegoogelt", "通过网络引擎检索", "Wenn du das Wort nicht kennst, google es doch einfach kurz!", "要是你拿不准这个新概念的含义，不妨直接用手机引擎检索一下！"),
            ("surfen", "", "v.", "surft, surfte, gesurft", "网上冲浪浏览；冲浪", "Jugendliche surfen täglich mehrere Stunden im weltweiten Internet.", "现在的年轻群体平均每天都要在网络虚拟世界中流连冲浪数小时。"),
            ("online", "", "adj./adv.", "", "在网在线互联的", "Sind Sie zurzeit online oder haben Sie gerade kein Netz?", "您现在正保持在线状态吗，还是恰巧手机信号盲区处于离线脱网？"),
            ("offline", "", "adj./adv.", "", "离线单机无网的", "Um ungestört zu arbeiten, gehe ich bewusst für zwei Stunden offline.", "为了能够集中精力心无旁骛赶工，我主动把所有聊天软件断网离线两小时。"),
            ("das Smartphone", "das", "n.", "-s", "多功能智能移动手机", "Ein modernes Smartphone vereint Kamera, Computer und Telefon in einem.", "一部当代智能手机完美集成了高像素相机、微型电脑及移动电话。"),
            ("das Tablet", "das", "n.", "-s", "便携触控平板电脑", "Auf dem Tablet liest er abends im Bett digitale Magazine.", "临睡前他习惯靠在床头手捧轻薄的平板电脑翻阅当期电子杂志。"),
            ("die App", "die", "n.", "-s", "智能手机应用程序", "Mit der DeutschMeister-App lernt man spielend leicht deutsche Vokabeln.", "借助DeutschMeister这款精心打磨的学习APP，攻克德语词汇变得轻而易举。"),
            ("installieren", "", "v.", "installiert, installierte, installiert", "安装软件，布设", "Installieren Sie die Sicherheits-App aus dem offiziellen Store!", "请务必从官方应用商店下载安装这款经过权威认证的安全防护APP！"),
            ("aktualisieren", "", "v.", "aktualisiert, aktualisierte, aktualisiert", "更新版本，刷新", "Vergessen Sie nicht, das Betriebssystem regelmäßig zu aktualisieren!", "切莫忘记定期对手机操作系统进行安全补丁更新与大版本迭代升级！"),
            ("das Update", "das", "n.", "-s", "软件升级包补丁更新", "Das neueste Update behebt mehrere störende Softwarefehler.", "最新推送的这个系统更新包彻底修复了先前遗留的数个软件运行Bug。"),
            ("die Sprachnachricht", "die", "n.", "-en", "即时通讯语音条留言", "Sie schickte mir eine kurze Sprachnachricht via Messenger.", "她通过即时通讯聊天工具给我发送过来了一条十余秒的简短语音。"),
            ("tippen", "", "v.", "tippt, tippte, getippt", "手指击键打字，键入", "Mit zehn Fingern tippt er Texte rasant auf der Tastatur.", "他十指翻飞在全尺寸实体键盘上运指如飞极其迅捷地盲打录入文本。"),
            ("der Chat", "der", "n.", "-s", "即时文本在线畅聊", "Wir besprechen die Details schnell im Gruppen-Chat.", "我们在项目群聊工作组里三言两语便将具体细节商量敲定妥当。"),
            ("chatten", "", "v.", "chattet, chattete, gechattet", "文字在线聊天沟通", "Sie chattet täglich mit ihren Freundinnen in aller Welt.", "她每天都要跟散布在世界天南海北的闺蜜们在网上开心地侃大山。"),
            ("die sozialen Medien", "die", "n.pl.", "-", "社交媒体网络平台", "Soziale Medien verbinden Menschen über Kontinente hinweg.", "大型社交媒体网络打破空间阻隔将五大洲不同国度的人们连结在一起。"),
            ("das Netzwerk", "das", "n.", "-e", "人际人脉圈，网络", "LinkedIn ist ein berufliches Netzwerk für Karriere und Kontakte.", "领英是全球职场精英用于人脉拓展与求职猎聘的专业职业社交网络。"),
            ("die Plattform", "die", "n.", "-en", "互联网公共运营平台", "Die Video-Plattform bietet unzählige kostenlose Lernvideos.", "该大型视频分享平台上汇聚了数以千万计的高质量免费公益教学讲座。"),
            ("das Profil", "das", "n.", "-e", "个人展示主页，档案", "Er hat sein berufliches Profil mit aktuellen Zertifikaten ergänzt.", "他把最新考取的专业技能认证证书悉数增补进了自己的个人展示主页。"),
            ("das Profilbild", "das", "n.", "-er", "社交账号个人头像", "Wählen Sie ein professionelles Profilbild für Bewerbungsportale!", "在求职招聘门户网站上请务必上传一张落落大方、着正装的职场头像照！"),
            ("der Account", "der", "n.", "-s", "平台注册账号，账户", "Ich habe meinen alten Social-Media-Account endgültig gelöscht.", "我下定决心把自己多年前注册的那个老旧社交平台账号彻底注销删除了。"),
            ("das Konto", "das", "n.", "Konten", "线上用户账户，账号", "Sie richtet sich ein sicheres Benutzerkonto mit Zwei-Faktor-Schutz ein.", "她给自己开通了一个绑定双重身份动态验证的高安全级用户账号。"),
            ("registrieren", "", "v.", "registriert, registrierte, registriert", "注册登记，实名开户", "Registrieren Sie sich kostenlos mit einer gültigen E-Mail-Adresse!", "只需填入一个真实有效的电子邮箱，即可免费注册开启全部功能！"),
            ("einloggen", "", "v.", "loggt ein, loggte ein, eingeloggt", "扫码登录，登录", "Loggen Sie sich mit Passwort und Bestätigungscode ein!", "请凭借个人复杂密码与手机短信接收到的六位动态验证码登录！"),
            ("ausloggen", "", "v.", "loggt aus, loggte aus, ausgeloggt", "退出登录，下线", "Vergessen Sie am fremden Computer nicht, sich sofort auszuloggen!", "在公共网吧或他人电脑上使用完毕后，千万记得立刻点击安全退出下线！"),
            ("der Nutzer", "der", "n.", "-", "注册用户，网络使用者", "Die Plattform zählt bereits über zwanzig Millionen aktive Nutzer.", "该互动平台目前拥有的高粘性日活跃实名注册用户数已突破两千万大关。"),
            ("die Nutzerin", "die", "n.", "-nen", "女性网络用户", "Viele Nutzerinnen schätzen den respektvollen Ton in diesem Forum.", "无数女性用户极度赞赏该专业垂直论坛内部理性质朴、互相尊重的讨论氛围。"),
            ("der Beitrag", "der", "n.", "Beiträge", "博文帖子，稿件贡献", "Ihr Beitrag zum Thema Umweltschutz wurde tausendfach geteilt.", "她撰写发布的那篇关于垃圾分类的深度长帖在全网被转发展阅了数千次。"),
            ("posten", "", "v.", "postet, postete, gepostet", "发帖，在网上公开发布", "Er postet regelmäßig Fotos von seinen abenteuerlichen Bergtouren.", "他经常性地在个人动态主页上晒出自己在崇山峻岭间惊险探险的绝美大片。"),
            ("teilen", "", "v.", "teilt, teilte, geteilt", "转发分享；均分", "Teilen Sie diesen nützlichen Lerntipp mit Ihren Freunden!", "欢迎将这个极其硬核好用的德语通关高分秘籍一键转发给身边的考友！"),
            ("liken", "", "v.", "likt, likte, gelikt", "点赞，给好评点亮小红心", "Viele Leute liken das Foto des süßen kleinen Hundewelpen.", "那张憨态可掬、毛茸茸小奶狗的高清萌照瞬间引来了成千上万网友疯狂点赞。"),
            ("das Like", "das", "n.", "-s", "点赞数，红心赞", "Das Video sammelte innerhalb von nur einer Stunde über 50.000 Likes.", "这支自制短视频上线仅短短一个小时便疯狂收割了超过五万个点赞红心。"),
            ("kommentieren", "", "v.", "kommentiert, kommentierte, kommentiert", "撰写评论，评析", "Nutzer kommentieren hitzig die jüngste politische Entscheidung.", "热心网民们在各大社媒评论区对这项最新出台的公共政策展开了热烈论辩。"),
            ("der Kommentar", "der", "n.", "-e", "跟帖留言，用户评论", "Unter dem Artikel sammeln sich hunderte konstruktive Kommentare.", "在这篇精辟长文下方汇聚了数百条由广大读者留下的极具建设性的真知灼见。"),
            ("folgen", "", "v.", "folgt, folgte, ist gefolgt", "关注博主，关注 (接 Dat)", "Ich folge diesem informativen Kanal für deutsche Redewendungen schon lange.", "我很早以前就一直持续关注这个专讲地道德语俗语典故的高质量博主了。"),
            ("der Follower", "der", "n.", "-", "社媒粉丝关注者", "Die Influencerin hat auf Instagram mehr als eine halbe Million Follower.", "这位颇具带货口碑的时尚大V在社交平台上坐拥超过五十万忠实黏性铁粉。"),
            ("die Nachricht", "die", "n.", "-en", "私信留言；新闻通告", "Schreib mir eine private Nachricht, wenn du Fragen zum Kurs hast!", "要是你对课程安排还有任何具体疑问，随时欢迎直接给我发送后台私信！"),
            ("die Benachrichtigung", "die", "n.", "-en", "系统推送通知提醒", "Schalten Sie die Benachrichtigungen stumm, um konzentriert zu lernen!", "建议你在沉下心刷题学习期间将手机所有无谓的应用推送提醒一律设为静音！"),
            ("stumm", "", "adj.", "", "静音无声哑口的", "Das Smartphone ist während der Vorlesung im Hörsaal strikt stumm zu schalten.", "在大学阶梯大课进行当中，现场全体听课人员的手机均须自觉调至完全静音。"),
            ("vibrieren", "", "v.", "vibriert, vibrierte, vibriert", "机身马达震动振鸣", "Das Telefon vibriert leise in der Jackentasche.", "揣在大衣内袋里的手机伴随着来电提示发出了极其轻微的沉闷震动嗡鸣。"),
            ("die Privatsphäre", "die", "n.", "-", "个人隐私生活空间", "Der Schutz der eigenen Privatsphäre im digitalen Zeitalter ist essenziell.", "在无孔不入的数字化信息化时代守护好公民个人的私人隐私生活空间至关重要。"),
            ("der Datenschutz", "der", "n.", "-", "数据主权与隐私保护法", "Die europäische Datenschutz-Grundverordnung (DSGVO) setzt weltweit Maßstäbe.", "全欧盟全面推行的通用数据保护条例在全人类隐私立法史上树立起崭新标杆。"),
            ("die Daten", "die", "n.pl.", "-", "原始数据，个人敏感资料", "Geben Sie Ihre sensiblen persönlichen Daten niemals an Fremde weiter!", "切勿在网络上轻易将您包含银行卡号身份证在内的核心敏感个人数据泄露给外人！"),
            ("das Passwort", "das", "n.", "Passwörter", "安全验证口令密码", "Ein sicheres Passwort besteht aus Groß- und Kleinbuchstaben, Ziffern und Zeichen.", "一个牢不可破的高强度密码应当巧妙融合大小写英文字母、阿拉伯数字及特殊字符。"),
            ("sichern", "", "v.", "sichert, sicherte, gesichert", "备份数据，加固防护", "Sichern Sie die Festplatte mit einem automatischen wöchentlichen Backup!", "请在电脑上配置好定时自动化脚本，每周对重要工作磁盘进行深度冗余备份！"),
            ("die Sicherung", "die", "n.", "-en", "灾备备份；安全保险丝", "Dank der Cloud-Sicherung gingen bei dem Computercrash keine Daten verloren.", "万幸事前开启了云端异地灾备同步，电脑即使死机蓝屏也未曾丢失半点珍贵文稿。"),
            ("die Cloud", "die", "n.", "-s", "分布式云计算云盘", "Alle Teammitglieder greifen gemeinsam auf die geteilten Cloud-Ordner zu.", "团队全员借助权限受控的云盘共享文件夹协同办公，实现了实时多人文档编辑。"),
            ("der Speicherplatz", "der", "n.", "-", "物理或云端存储空间", "Mein Smartphone meldet, dass der interne Speicherplatz fast voll ist.", "手机屏幕弹出系统告警黄条，提示内部存储芯片容量告急已接近彻底占满。"),
            ("das Virus", "das", "n.", "Viren", "破坏性计算机病毒", "Ein tückischer Computervirus legte das gesamte Netzwerk des Betriebs lahm.", "一种极具隐蔽潜伏性的恶意计算机病毒瞬间导致整间公司的内部网络全面瘫痪。"),
            ("das Antivirenprogramm", "das", "n.", "-e", "病毒查杀杀毒软件", "Ein aktuelles Antivirenprogramm schützt das System vor Trojanern.", "一套版本保持最新的正版杀毒软件能够有效阻击各类木马后门病毒入侵偷袭。"),
            ("die Firewall", "die", "n.", "-s", "网络安全防御防火墙", "Die Firewall blockiert verdächtige Zugriffsversuche von außen ab.", "部署在边界的硬件防火墙能够精准识别并拦截外部黑客恶意端口扫描与渗透。"),
            ("hacken", "", "v.", "hackt, hackte, gehackt", "黑客非法侵入破译", "Kriminelle versuchten vergeblich, das System der Bank zu hacken.", "不法网络犯罪分子妄图非法侵入该商业银行核心结算主机系统的图谋终告破产。"),
            ("der Hacker", "der", "n.", "-", "计算机顶级黑客入侵者", "Ethische Hacker spüren Sicherheitslücken im Auftrag von Firmen auf.", "白帽白客受各大企业重金聘请，专门替系统安全防御排查潜藏的漏洞与后门。"),
            ("die Nachrichten", "die", "n.pl.", "-", "电视新闻广播，每日简报", "Um 20 Uhr schaut ganz Deutschland traditionell die 'Tagesschau'.", "晚八点整收看公共第一电视台权威严谨的《每日新闻》是全德千家万户的默契。"),
            ("die Zeitung", "die", "n.", "-en", "传统实体纸媒日报报刊", "Viele ältere Bürger lesen morgens beim Frühstück eine gedruckte Zeitung.", "很多上了年纪的长者依然保留着清晨一边喝咖啡一边翻阅油墨飘香大报的习惯。"),
            ("das E-Paper", "das", "n.", "-s", "数字高清电子版报刊", "Ich habe das E-Paper abonniert und lese es bequem auf dem Tablet.", "我在线订阅了全彩高清电子报，每天清晨在平板电脑上便能阅览全部原版版面。"),
            ("abonnieren", "", "v.", "abonniert, abonnierte, abonniert", "长期付费征订，订阅", "Abonnieren Sie unseren kostenlosen Newsletter für aktuelle Deutsch-Tipps!", "欢迎免费订阅我们的官方周报通讯，每周准时获取新鲜出炉的德语实用干货！"),
            ("das Abonnement", "das", "n.", "-s", "订阅契约周期，长期订单", "Das Abonnement der renommierten Fachzeitschrift verlängert sich jährlich.", "这份业内知名专业核心学术期刊的年度订阅在期满后将自动按年平稳顺延。"),
            ("die Sendung", "die", "n.", "-en", "电台电视台播送栏目", "Eine humorvolle und lehrreiche Sendung für die ganze Familie.", "一档老少咸宜、寓教于乐且在广大观众中口碑极佳的大型家庭科普综艺节目。"),
            ("der Moderator", "der", "n.", "-en", "电视电台知名节目主持人", "Der bekannte Moderator führt souverän und charmant durch den Abend.", "那位家喻户晓的王牌金牌主持人以极其稳健且充满魅力的台风掌控着整场晚会。"),
            ("das Interview", "das", "n.", "-s", "深度面对面新闻专访", "Der Minister gab dem renommierten Journalisten ein langes Exklusiv-Interview.", "该部部长就近期社会广泛关注的焦点热点问题破例接受了资深记者的独家深度专访。"),
            ("interviewen", "", "v.", "interviewt, interviewte, interviewt", "对重点人物进行专访", "Die Reporterin interviewt Passanten in der Fußgängerzone zu den Preisen.", "出镜女记者正在热闹繁华的商业步行街头就物价变动随机拦下过往行人做街采。"),
            ("die Presse", "die", "n.", "-", "全行业新闻出版舆论界", "Die freie Presse erfüllt als vierte Gewalt eine unverzichtbare Kontrollfunktion.", "崇尚独立客观的自由新闻舆论界作为社会公器担负着不可或缺的监督把关之职。")
        ]
    },

    # LESSON 14
    {
        "id": "A2_L14",
        "title": "第14课：传统节庆、民间习俗与社交礼仪 (Bräuche & Höflichkeit)",
        "summary": "掌握第二虚拟式愿望表达 (Ich wünschte, ich hätte/wäre)、德语区特色民俗与社交送礼待客礼仪",
        "grammar": {
            "title": "第二虚拟式表达非现实愿望 (Irreale Wünsche) 与礼仪文化",
            "sections": [
                {
                    "heading": "1. 第二虚拟式表达非现实愿望结构：hätte gern / wäre gern / würde gern",
                    "content": "• Ich hätte gern ein Glas Weißwein. (我想要一杯白葡萄酒)\n• Wenn ich doch mehr Zeit hätte! (要是我有更多时间该多好啊！)\n• Ich wäre jetzt so gern am Meer! (我现在要是能在海边度假该多惬意啊！)"
                },
                {
                    "heading": "2. 德国做客社交礼仪铁律",
                    "content": "• 受邀去德国人家做客必须守时（迟到超15分钟被视作不敬）。\n• 礼品文化：通常送花（忌送单数玫瑰花束红玫瑰、忌送黄菊花）、一瓶上乘葡萄酒或精美巧克力。\n• 进门脱鞋：主动询问是否需要换鞋 (Soll ich die Schuhe ausziehen?)。"
                }
            ]
        },
        "quiz": [
            {
                "id": "A2_L14_Q1",
                "type": "GRAMMAR_FILL",
                "question": "Ach, wenn ich doch jetzt reich ______ (sein, 第二虚拟式非现实愿望)!",
                "options": ["wäre", "bin", "war", "gewesen"],
                "correctIndex": 0,
                "explanation": "表达如果我现在...该多好的非现实假想愿望，sein 的第二虚拟式第一人称单数为 wäre。"
            },
            {
                "id": "A2_L14_Q2",
                "type": "EXAM_REAL",
                "question": "受邀前往德国朋友家共进晚餐，最得体周到的伴手礼通常是：",
                "options": ["一瓶精选葡萄酒或一束鲜花/巧克力", "贵重黄金首饰", "不用带任何东西两手空空", "带一大包大蒜和洋葱"],
                "correctIndex": 0,
                "explanation": "在德国做客，带一瓶好酒、一小束鲜花或一盒高档巧克力（Pralinen）是得体不失礼貌的黄金标准。"
            }
        ],
        "words": [
            ("der Brauch", "der", "n.", "Bräuche", "民间传统习俗风俗", "Alte Bräuche und Traditionen werden im ländlichen Raum sorgsam gepflegt.", "古老悠久的民间岁时风俗在德语区广袤乡土社会依旧得到极其虔诚的呵护传承。"),
            ("die Sitte", "die", "n.", "-n", "世俗风尚风规道德", "Andere Länder, andere Sitten, sagt ein weises und wahres deutsches Sprichwort.", "常言道百里不同风千里不同俗，这句德国古老谚语道尽了跨文化交往真谛。"),
            ("die Tradition", "die", "n.", "-en", "薪火相传的历史传统", "Das Oktoberfest in München blickt auf eine über 200-jährige Tradition zurück.", "举世瞩目的慕尼黑十月啤酒节坐拥超越两个世纪之久的深厚积淀与节庆传统。"),
            ("traditionell", "", "adj.", "traditioneller, am traditionellsten", "遵从古法传统的", "Zur traditionellen Tracht gehört die bayerische Lederhose für Herren.", "在巴伐利亚传统民族服饰盛装中，男士皮短裤是一件标志性核心文化符号。"),
            ("die Tracht", "die", "n.", "-en", "地区民族特色盛装", "Frauen tragen im Festzelt ein farbenfrohes, handgesticktes Dirndl.", "在人声鼎沸的巨大啤酒大篷内，姑娘们纷纷身着色彩娇艳的手工刺绣紧身连衣裙。"),
            ("das Oktoberfest", "das", "n.", "-", "慕尼黑十月啤酒节", "Millionen Gäste aus aller Welt strömen alljährlich zum Oktoberfest.", "每年秋天全球有数百万海内外游客涌向慕尼黑特蕾莎广场共襄啤酒节狂欢。"),
            ("die Wiesn", "die", "n.", "-", "十月节草坪广场（巴伐利亚口语）", "Auf geht's zur Wiesn! ruft man fröhlich im goldenen Herbst in München.", "在金风送爽的秋季慕尼黑街头到处都能听到呼朋引伴共赴啤酒草坪狂欢的口号。"),
            ("die Maß", "die", "n.", "-", "一升标准特大扎啤杯", "Eine Maß frisch gezapftes Festbier bitte!", "酒保，请给我来一大升刚打出来的泡沫雪白香气四溢的特酿节庆大扎啤！"),
            ("das Festzelt", "das", "n.", "-e", "庆典巨型狂欢大篷", "Im riesigen Festzelt herrscht mitreißende Blasmusik und ausgelassene Stimmung.", "在容纳万人的巨型啤酒大篷内，欢快的铜管交响乐将整场狂欢气氛推向高潮。"),
            ("die Blasmusik", "die", "n.", "-", "民间欢庆管乐吹奏", "Die Musikkapelle in Tracht spielt traditionelle bayerische Blasmusik.", "身着传统盛装的民间管乐乐团鼓乐齐鸣，奏响了极富浓郁乡土韵味的管乐篇章。"),
            ("der Advent", "der", "n.", "-e", "圣诞前夕降临节期", "Der Advent beginnt vier Sonntage vor dem Heiligen Abend.", "在平安夜降临前的四个星期天，全德境内正式拉开了神圣温馨的降临节序幕。"),
            ("der Adventskranz", "der", "n.", "Adventskränze", "降临节常青松柏花环", "Auf dem geflochtenen Adventskranz aus Tannengrün stehen vier dicke Kerzen.", "在用新鲜翠绿松柏枝编织而成的精致花环上，插有四支粗大饱满的烛台蜡烛。"),
            ("der Adventskalender", "der", "n.", "-", "降临节惊喜日历盒", "Kinder öffnen jeden Morgen voller Vorfreude ein Türchen im Adventskalender.", "整个十二月里孩子们每天清晨都会迫不及待抠开日历小门收获甜蜜惊喜小礼物。"),
            ("der Nikolaus", "der", "n.", "-", "圣尼古拉斯赠礼老人", "Am Vorabend des 6. Dezember putzen die Kinder ihre Stiefel für den Nikolaus.", "在12月6日圣尼古拉斯日前夜，孩子们会把冬靴擦得锃亮放在门外期待装满糖果。"),
            ("der Nikolaustag", "der", "n.", "-", "圣尼古拉斯儿童赠礼日", "Am Nikolaustag finden brave Kinder Schokolade und Nüsse in ihren Stiefeln.", "在圣尼古拉斯节当天清晨，懂事听话的好孩子会在靴筒里惊喜发现核桃与巧克力。"),
            ("der Christkind", "das", "n.", "-", "圣婴降福送礼小童", "In Süddeutschland bringt das Christkind an Heiligabend die Geschenke.", "在德国南部与奥地利民间传统里，给全家悄悄分发圣诞礼物的不是圣诞老人而是圣婴。"),
            ("der Weihnachtsmann", "der", "n.", "Weihnachtsmänner", "白须红袍圣诞老人", "Im Norden glaubt der Nachwuchs an den gütigen Weihnachtsmann mit dem Schlitten.", "在德国北部地区，孩子们坚信慈祥的白胡子红袍圣诞老人会驾着驯鹿雪橇从天而降。"),
            ("der Lebkuchen", "der", "n.", "-", "香料蜂蜜姜饼糕点", "Nürnberger Lebkuchen sind weltweit geschätzte Spezialitäten zur Weihnachtszeit.", "表面裹着巧克力或糖霜的纽伦堡传统蜂蜜香料姜饼是圣诞季享誉国际的极品名点。"),
            ("der Stollen", "der", "n.", "-", "德累斯顿圣诞雪霜果脯面包", "Dresdner Christstollen wird nach geheimem Rezept mit feinsten Rosinen gebacken.", "享誉全球的德累斯顿传统圣诞大蛋糕依循严格保密古方加入足量果脯与黄油烘烤。"),
            ("der Glühwein", "der", "n.", "-", "冬日香料热红葡萄酒", "Auf dem eisigen Weihnachtsmarkt wärmt eine Tasse dampfender Glühwein.", "在银装素裹寒风凛冽的圣诞集市上，捧上一杯热气腾腾的肉桂香料红酒堪称人间至福。"),
            ("das Osterfest", "das", "n.", "-e", "春分复活佳节盛典", "Das Osterfest steht im Zeichen von Auferstehung, Hoffnung und neuem Leben.", "复活节象征着万物复苏、万象更新以及大自然在严冬过后焕发出的蓬勃新生希望。"),
            ("das Osterfeuer", "das", "n.", "-", "复活节驱邪春之篝火", "Am Karsamstag entzünden die Dorfbewohner ein großes, weithin sichtbares Osterfeuer.", "在圣周六黄昏全村老幼齐聚一堂，点燃熊熊燃烧象征驱散黑暗迎来春天的盛大篝火。"),
            ("der Pfingsten", "das", "n.", "-", "圣灵降临五旬节", "An Pfingsten nutzen viele das lange Pfingstwochenende für Kurztrips.", "借助五旬节延长的法定长周末小长假，无数家庭选择踏青出游度过惬意假期。"),
            ("der Tag der Deutschen Einheit", "der", "n.", "-", "十月三日德国统一日国庆", "Am 3. Oktober feiert ganz Deutschland den Tag der Deutschen Einheit als Nationalfeiertag.", "每逢十月三日德国举国同庆，隆重纪念两德和平统一这一伟大历史节点并设为法定国庆。"),
            ("die Wiedervereinigung", "die", "n.", "-", "东西德历史和平统一", "Die friedliche deutsche Wiedervereinigung jährt sich dieses Jahr erneut.", "东西两德在柏林墙倒塌后顺应历史潮流实现的和平国家再统一今年迎来了新的周年。"),
            ("die Mauer", "die", "n.", "-n", "阻隔分裂之墙柏林墙", "Der historische Fall der Berliner Mauer am 9. November 1989 veränderte die Welt.", "1989年11月9日柏林墙在万众欢呼声中被彻底推倒的壮丽时刻永远改变了世界格局。"),
            ("der Karneval", "der", "n.", "-", "莱茵河畔科隆狂欢节", "Der Kölner Karneval erreicht seinen frenetischen Höhepunkt am Rosenmontag.", "名扬天下的科隆狂欢节在狂欢星期一盛大花车巡游当天迎来全城万人空巷的最高潮。"),
            ("der Rosenmontag", "der", "n.", "-", "狂欢星期一狂欢日", "Am Rosenmontag ziehen farbenfrohe Motivwagen durch die Kölner Innenstadt.", "在狂欢星期一当天，载着讽刺时政造型雕塑的巨型彩车车队浩浩荡荡开过科隆市中心。"),
            ("der Fasching", "der", "n.", "-", "南德奥地利狂欢节", "In München und Wien wird der Fasching mit eleganten Bällen zelebriert.", "在慕尼黑与维也纳，狂欢季则往往伴随着一场接一场衣香鬓影的高雅交戈华尔兹舞会。"),
            ("die Fastnacht", "der", "n.", "-", "黑森林阿勒曼尼古狂欢节", "Die schwäbisch-alemannische Fastnacht besticht durch geschnitzte Holzmasken.", "施瓦本与阿勒曼尼地区的传统古节以街头巡游者佩戴的面目狰狞的手工雕刻木面具著称。"),
            ("die Maske", "die", "n.", "-n", "鬼神恶灵传统面具", "Dämonische Holzmasken sollen die Geister des kalten Winters vertreiben.", "相传巡游者佩戴这种刻有獠牙恶鬼神态的古朴面具能以毒攻毒彻底驱赶严冬的恶灵。"),
            ("verkleiden", "", "v.", "verkleidet, verkleidete, verkleidet", "乔装化装打扮变身", "Kinder lieben es, sich als mutige Piraten oder zauberhafte Prinzessinnen zu verkleiden.", "天真烂漫的小朋友最喜欢把自己盛装打扮成英勇无畏的加勒比海盗或优雅的小公主。"),
            ("die Einladung", "die", "n.", "-en", "盛情邀请请柬邀请信", "Wir haben eine herzliche Einladung zum runden Geburtstag meines Onkels erhalten.", "我们收到了一封措辞极度诚挚的热情请柬，受邀赴宴出席我叔叔六十大寿的隆重晚宴。"),
            ("der Gastgeber", "der", "n.", "-", "款待宾客的男主人", "Der Gastgeber öffnet die Haustür und heißt jeden Ankommenden willkommen.", "热情好客的男主人敞开大门，亲切迎接着每一位风尘仆仆如约而至的尊贵好友客人。"),
            ("die Gastgeberin", "die", "n.", "-nen", "款待宾朋的女主人", "Die Gastgeberin hat für das Festbankett ein vorzügliches Fünf-Gänge-Menü gezaubert.", "心灵手巧的女掌柜为这场私享宴席倾情准备了一整套精致考究的五道式西餐大餐。"),
            ("der Gast", "der", "n.", "Gäste", "赴宴宾客，登门贵客", "Ein aufmerksamer Gast bringt immer eine kleine Aufmerksamkeit für das Haus mit.", "一位知书达礼、深谙社交教养的体贴客人登门时绝不会忘记携带一份伴手心意。"),
            ("die Aufmerksamkeit", "die", "n.", "-en", "微薄心意伴手小礼物", "Als kleine Aufmerksamkeit überreichte er der Dame eine Schachtel feinste Pralinen.", "作为登门做客的一点微薄心意，他极其绅士地双手向女主人呈递上一盒手工生巧。"),
            ("das Gastgeschenk", "das", "n.", "-e", "拜访主人呈递的伴手礼", "Ein guter Jahrgangswein aus der Heimat eignet sich perfekt als Gastgeschenk.", "一瓶出自自己家乡知名酒庄出产的高品质陈酿葡萄酒堪称登门做客最得体的伴手礼。"),
            ("überreichen", "", "v.", "überreicht, überreichte, überreicht", "郑重呈送亲手转交", "Der Bürgermeister überreicht der Jubilarin einen prächtigen Blumenstrauß.", "市长先生在全场见证下庄重地亲手向这位寿星老寿星递上了一大束极其娇艳的鲜花。"),
            ("der Blumenstrauß", "der", "n.", "Blumensträuße", "包装精巧的芬芳花束", "Ein herrlich duftender Blumenstrauß aus gelben Sonnenblumen und rosa Rosen.", "一束散发着幽雅阵阵芳香、由金灿灿向日葵与粉嫩玫瑰巧妙扎制而成的花艺花束。"),
            ("die Schokolade", "die", "n.", "-n", "醇香巧克力可可脂糖", "Zartbitterschokolade mit einem Kakaoanteil von siebzig Prozent schmeckt herb.", "可可固形物含量高达百分之七十的优质特级黑巧尝起来微苦却带着悠长回甘。"),
            ("die Praline", "die", "n.", "-n", "高档手工夹心精制软糖", "Belgische und Schweizer Pralinen sind ein weltweit begehrtes Luxusgeschenk.", "来自比利时与瑞士工匠名师亲手制作的夹心软质巧克力是极受推崇的奢华馈赠礼品。"),
            ("ausziehen", "", "v.", "zieht aus, zog aus, ausgezogen", "在玄关换脱外套鞋子", "Darf ich mir die Straßenschuhe ausziehen und Hausschuhe anziehen?", "请问我可以把外出的户外鞋脱在门厅玄关换上一双室内防滑居家便鞋吗？"),
            ("die Hausschuhe", "die", "n.pl.", "-", "居室防滑室内拖鞋", "Die Gastgeberin reichte den eingetroffenen Gästen bequeme Hausschuhe.", "体贴入微的女主人早已为陆续登门进屋的各位客人们备好了干净松软的室内拖鞋。"),
            ("begrüßen", "", "v.", "begrüßt, begrüßte, begrüßt", "拱手相迎热忱问候", "Man begrüßt sich in Deutschland traditionell mit einem festen Händedruck.", "在德国严谨的社交文化中，初次见面通常恪守伸出右手给予对方一次沉稳有力的握手。"),
            ("der Händedruck", "der", "n.", "-", "礼貌沉稳的握手礼节", "Ein fester, verbindlicher Händedruck signalisiert Verlässlichkeit und Aufrichtigkeit.", "一次坚定有力、落落大方的标准握手向对方无声传递着自信笃定与诚恳靠谱的信号。"),
            ("der Blickkontakt", "der", "n.", "-e", "四目相交眼神交流接触", "Halten Sie beim Zuprosten und Händeschütteln stets freundlichen Blickkontakt!", "在双手交握或举杯向同桌敬酒时请切记务必与对方的眼睛保持坦荡真诚的眼神接触！"),
            ("die Höflichkeit", "die", "n.", "-", "谦恭有礼知书达礼", "Höflichkeit ist wie ein unsichtbares Schmiermittel für das soziale Zusammenleben.", "真诚得体的知书达礼就如同社交和谐生活运转中一瓶润物细无声的高级润滑油。"),
            ("die Pünktlichkeit", "die", "n.", "-", "恪守时刻极度守时", "Fünf Minuten vor der Zeit ist des Deutschen Pünktlichkeit, besagt der Spruch.", "有一句诙谐的名言在德语民间广为流传：提前五分钟到达才是德国人眼中的真正守时。"),
            ("bedanken", "", "v.", "bedankt, bedankte, bedankt", "由衷深表感激谢忱 (bei/für)", "Ich möchte mich bei Ihnen von ganzem Herzen für die Hilfe bedanken.", "我谨借此机会发自肺腑地向您在危难关头向我施以的鼎力无私援助表达无尽谢意。"),
            ("die Dankbarkeit", "die", "n.", "-", "感恩怀德之情", "Wahre Dankbarkeit zeigt sich nicht nur in warmen Worten, sondern in Taten.", "真正深沉的感恩之情从来都绝不仅仅浮于口头客套辞令，更体现在实实在在的行动。"),
            ("loben", "", "v.", "lobt, lobte, gelobt", "不吝褒奖由衷赞赏", "Die Gäste lobten einhellig die Kochkünste und die Gastfreundschaft der Wirtin.", "全体在座宾朋交口称赞女主人的超凡精湛烹饪厨艺与无微不至的热诚待客之道。"),
            ("das Kompliment", "das", "n.", "-e", "得体称颂溢美之词", "Er machte seiner charmanten Tischdame ein elegantes und dezentes Kompliment.", "他十分得体、恰如其分地向身边与他同席而坐的优雅女士送上了一句优雅的赞美。"),
            ("die Tischmanieren", "die", "n.pl.", "-", "餐桌用餐就餐礼仪修养", "Gute Tischmanieren werden Kindern von klein auf im Elternhaus vermittelt.", "良好的西餐就餐礼仪与餐具拿捏教养从孩提时代起便在家庭餐桌上耳濡目染养成。"),
            ("anstoßen", "", "v.", "stößt an, stieß an, angestoßen", "端起酒杯清脆相碰", "Beim feierlichen Anstoßen schaut man seinem Gegenüber direkt in die Augen.", "在举杯郑重与他人碰杯祝酒的瞬间，必须直视对方的眼眸以示坦诚与最高的敬意。"),
            ("die Trinksprüche", "die", "n.pl.", "-", "祝酒辞敬酒令（复数）", "Auf die Gesundheit, auf das Wohl und auf unsere langlebige Freundschaft!", "为了彼此的身体康健，为了家庭的福泽延绵，更为了我们经得起考验的恒久友谊干杯！"),
            ("der Toast", "der", "n.", "-s", "正式敬酒祝酒辞；吐司", "Der Trauzeuge sprach einen bewegenden und humorvollen Toast auf das Brautpaar.", "婚礼男傧相代表伴郎团向新婚燕尔的一对璧人发表了一段感人肺腑又妙趣横生的祝酒词。"),
            ("verabschieden", "", "v.", "verabschiedet, verabschiedete, verabschiedet", "作揖道别拱手辞行", "Es ist schon Mitternacht, wir müssen uns nun leider schweren Herzens verabschieden.", "不知不觉墙上钟摆已过午夜零点，天下没有不散的筵席，我们只得恋恋不舍向主人道别。"),
            ("der Abschied", "der", "n.", "-e", "依依不舍之惜别", "Der Abschied nach den gemeinsamen Ferientagen fiel allen Beteiligten sichtlich schwer.", "经过数日无忧无虑结伴同游的假期后，离别的一刻在场所有人眼中都写满了依依不舍。"),
            ("das Wiedersehen", "das", "n.", "-", "久别重逢，后会有期", "Auf ein baldiges und frohes Wiedersehen im nächsten Sommer in den Bergen!", "让我们共同期待来年盛夏在高山深处迎来下一次欢快畅快的久别重逢，后会有期！"),
            ("die Geselligkeit", "die", "n.", "-", "高朋满座的融洽社交", "Die Gemütlichkeit und Geselligkeit dieses langen Festabends bleibt unvergessen.", "今晚整场聚会所洋溢出的这种宾至如归的安详惬意与高朋满座的融洽，注定令人终生难忘。"),
            ("feiern", "", "v.", "feiert, feierte, gefeiert", "欢天喜地共度欢庆", "Familienmitglieder reisen von weit her an, um diesen runden Ehrentag gemeinsam zu feiern.", "天各一方的家族血亲不惜跨越千山万水赶回老家团圆，就是为了能聚在一起共襄盛典。"),
            ("das Jubiläum", "das", "n.", "Jubiläen", "逢整十逢百重大周年庆", "Das traditionsreiche Traditionsunternehmen feiert stolz sein hundertjähriges Jubiläum.", "这家百年老字号民族制造企业怀着无比自豪的心情迎来了其建厂一百周年逢整纪念大庆。"),
            ("der Glückwunsch", "der", "n.", "Glückwünsche", "真挚热烈的美好祝愿", "Übermitteln Sie dem Jubilar bitte unsere allerherzlichsten und aufrichtigsten Glückwünsche!", "请代为向今天的大寿星老先生转达我们全体同仁最热烈、最由衷诚挚的美好祝福！"),
            ("alles Gute", "", "phrase", "", "祝万事顺遂一切安好", "Ich wünsche dir für deinen weiteren persönlichen Lebensweg alles erdenklich Gute!", "我谨由衷祝愿你在未来的人生征途中乘风破浪前程似锦，事事顺心皆得所愿！"),
            ("viel Erfolg", "", "phrase", "", "祝圆满斩获成功", "Viel Erfolg und das nötige Quäntchen Glück für die anstehende Zertifikatsprüfung!", "祝你在即将到来的语言等级终极大考中发挥出真实硬核水平，顺利斩获优异成功！"),
            ("gute Besserung", "", "phrase", "", "祝早日战胜疾恙康复", "Wir denken an dich in der Reha und wünschen dir eine rasche, vollkommene gute Besserung!", "全科室的兄弟姐妹们时刻挂念着正在术后康复休养的你，盼你早日满血归队平安康复！"),
            ("herzlich willkommen", "", "phrase", "", "热烈欢迎四方宾朋光临", "Ein herzliches Willkommen in unserem geschichtsträchtigen und gastfreundlichen Hause!", "以最热忱深厚的敬意，热烈欢迎各位尊贵远道而来的中外宾朋莅临我们这座百年老宅！"),
            ("guten Rutsch", "", "phrase", "", "祝新年除夕顺利跨入新年", "Guten Rutsch ins neue Jahr und viel Gesundheit, Schaffenskraft und inneren Frieden!", "祝各位在除夕夜顺顺当当滑入充满希望的崭新一年，阖家安康幸福，万事吉祥如意！"),
            ("frohe Festtage", "", "phrase", "", "祝度过祥和欢快的节期", "Wir wünschen unserer geschätzten Kundschaft und ihren Familien besinnliche und frohe Festtage!", "我们向长期以来给予信任支持的尊贵广大客户及其家人致以最祥和幸福的节日问候！")
        ]
    },

    # LESSON 15
    {
        "id": "A2_L15",
        "title": "第15课：歌德 A2 全真模拟与应试冲刺 (Goethe A2 Prüfungstraining)",
        "summary": "全方位精解歌德 A2 听说读写四大试卷真题结构、核心应试策略与满分范文模板",
        "grammar": {
            "title": "歌德 A2 笔试与口试全景通关法则",
            "sections": [
                {
                    "heading": "1. 歌德 A2 核心应试四大板块拆解",
                    "content": "• Lesen (阅读 30分钟): 报刊短文、分类广告、指示标牌、便条长邮件。\n• Hören (听力 30分钟): 日常短对话（抓场景与地点）、电话留言（数字与时刻）、火车站/商场播音（提取核心指令）。\n• Schreiben (写作 30分钟): 撰写一封约30-40词的日常便条/私人邮件，以及一封约30-40词的正式公函/预约信。\n• Sprechen (口语 15分钟): Teil 1 提问回答个人信息；Teil 2 从自身实际出发讲述主题；Teil 3 现场抽卡与搭档协商商定共同计划。"
                },
                {
                    "heading": "2. 口试 Teil 3 协商商讨黄金句式",
                    "content": "• Was hältst du davon, wenn wir...? (如果我们...你觉得如何？)\n• Das ist eine gute Idee, aber ich hätte einen anderen Vorschlag.\n• Wann und wo wollen wir uns treffen?"
                }
            ]
        },
        "quiz": [
            {
                "id": "A2_L15_Q1",
                "type": "EXAM_REAL",
                "question": "歌德A2口试第三部分与搭档共同商定周末活动，礼貌征求搭档意见的高分句型是：",
                "options": ["Was hältst du davon, wenn wir ins Museum gehen?", "Ich will ins Kino, du musst mitkommen!", "Gehen wir jetzt sofort!", "Ich habe keine Lust auf dich."],
                "correctIndex": 0,
                "explanation": "Was hältst du davon, wenn wir... 是歌德A2/B1口语协商部分考官最青睐的地道协商征询句型。"
            },
            {
                "id": "A2_L15_Q2",
                "type": "EXAM_REAL",
                "question": "歌德A2写作中，向房东写信礼貌请求派技工上门检修暖气，正文结尾最得体的结语是：",
                "options": ["Ich bitte Sie um eine baldige Rückmeldung und bedanke mich im Voraus.", "Kommen Sie sofort hierher!", "Ich bezahle keine Miete mehr.", "Auf Wiedersehen und tschüss!"],
                "correctIndex": 0,
                "explanation": "Ich bitte Sie um eine baldige Rückmeldung und bedanke mich im Voraus. 是正式商务公函请求处理的规范标准结语。"
            }
        ],
        "words": [
            ("das Prüfungstraining", "das", "n.", "-s", "考前全真强化实操冲刺", "Ein intensives Prüfungstraining nimmt Prüflingen die Angst vor dem Examen.", "系统规范的全真模考高强度冲刺能彻底消除广大应试者内心的怯场与顾虑。"),
            ("die Prüfung", "die", "n.", "-en", "正式语言认证考试", "Die Prüfung für das Goethe-Zertifikat A2 findet am kommenden Samstag statt.", "本期歌德A2证书等级认证统考定于本周星期六上午在考点正式开考。"),
            ("das Goethe-Zertifikat", "das", "n.", "-e", "歌德学院官方语言等级证书", "Das Goethe-Zertifikat ist ein weltweit anerkannter Nachweis von Sprachkenntnissen.", "歌德学院权威认证证书是全球所有企事业单位公认通行的德语水平凭证。"),
            ("das Niveau", "das", "n.", "-s", "欧标通用语言水准层级", "Mit erfolgreicher A2-Prüfung erreicht man die Stufe der elementaren Sprachverwendung.", "顺利通过A2等级评定标志着考生具备了欧洲共同语言参考框架下的基础运用水准。"),
            ("der Prüfling", "der", "n.", "-e", "赶考应试考生，考生", "Alle Prüflinge müssen ihren amtlichen Lichtbildausweis vor der Tür bereithalten.", "请考场门外等候的所有参考考生提前拿出带有本人清晰近照的有效法定身份证件。"),
            ("der Prüfer", "der", "n.", "-", "认证资深考官，评卷人", "Der Prüfer erklärt den Ablauf ruhig, sachlich und in leicht verständlichen Worten.", "资深考官以极其平易近人、和蔼沉稳的口吻向在座考生说明全场考试规则要领。"),
            ("die Prüferin", "die", "n.", "-nen", "女性认证考评考官", "Die Prüferin bewertet Aussprache, Wortschatz, Grammatik und Flüssigkeit im Sprechen.", "考官在口语模块将全面综合评判考生的标准发音、词汇广度、语法及流利程度。"),
            ("die Prüfungsordnung", "die", "n.", "-en", "考场纪律与考试守则", "Täuschungsversuche führen gemäß Prüfungsordnung zum sofortigen Ausschluss.", "依据考场纪律红线规定，考场内任何形式的舞弊企图都将被当场取消考试资格。"),
            ("die Punktzahl", "die", "n.", "-en", "卷面测算综合得分点数", "Um die Prüfung zu bestehen, muss man mindestens sechzig von hundert Punkten erzielen.", "想要稳稳通过本次等级考试，考生卷面综合得分必须达到最低六十分基准线。"),
            ("das Modul", "das", "n.", "-e", "考核大类模块，单元", "Die A2-Prüfung gliedert sich in die vier Module Lesen, Hören, Schreiben und Sprechen.", "歌德A2考试整体科学划分并涵盖阅读、听力、书面写作以及现场口试四大模块。"),
            ("das Bestehen", "das", "n.", "-", "达标过线及格通过", "Das Bestehen der A2-Prüfung ist oft die Voraussetzung für ein Visum zum Ehegattennachzug.", "考取并出示A2及格证书往往是外籍配偶赴德办理家庭团聚签证的硬性法律门槛。"),
            ("das Ergebnis", "das", "n.", "-se", "评卷最终结果成绩单", "Das offizielle Ergebnis wird online innerhalb von zwei Wochen bekannt gegeben.", "官方最终阅卷成绩单将于考试结束两周之内在考生个人系统门户后台开放查询。"),
            ("die Bestätigung", "die", "n.", "-en", "正式成绩证明单据", "Eine vorläufige Bestätigung kann im Prüfungszentrum beantragt werden.", "在正式羊皮纸证书下发前，可在考点申请开具加盖公章的预先临时通过证明。"),
            ("die Aufgabenstellung", "die", "n.", "-en", "题干审题要求，要求", "Lesen Sie die Aufgabenstellung konzentriert und markieren Sie Schlüsselwörter!", "请凝神静气细致研读审清题干文字要求，并在关键线索词下方划线作标记！"),
            ("die Anweisung", "die", "n.", "-en", "卷面答题操作指令", "Befolgen Sie exakt die Anweisungen auf dem offiziellen Antwortbogen!", "请严格遵循答题卡上印刷的答题填涂与书写规范指引，切勿违规逾界涂抹！"),
            ("der Antwortbogen", "der", "n.", "Antwortbögen", "机读专用主客观答题卡", "Übertragen Sie Ihre Lösungen unbedingt rechtzeitig auf den finalen Antwortbogen!", "务必合理分配掌控考场作答时间，提前将全部答案精准誊抄至最终正式答题卡！"),
            ("der Fragebogen", "der", "n.", "Fragebögen", "试题问卷，题册", "Im Fragebogen dürfen Sie sich persönliche Notizen und Unterstreichungen machen.", "在下发的试卷草稿纸与问卷试题纸上，考生完全可以自由圈点勾画并记录心得。"),
            ("der Teil", "der", "n.", "-e", "试卷组成大题部分", "Teil 1 der Leseaufgabe erfordert das genaue Abgleichen von Aussagen in Zeitungsartikeln.", "阅读模块第一大题主要考查考生细致比对报纸短文事实细节并做正误判断的能力。"),
            ("die Multiple-Choice-Aufgabe", "die", "n.", "-n", "三选一单项客观选择题", "Bei jeder Multiple-Choice-Aufgabe gibt es genau eine zutreffende Antwortoption.", "在单项选择题型中，题目给出的A、B、C三个备选选项中有且仅有一项符合题意。"),
            ("auswählen", "", "v.", "wählt aus, wählte aus, ausgewählt", "审慎挑选，选定正确项", "Wählen Sie aus den drei Optionen A, B und C die richtige Lösung aus!", "请在A、B、C三个备选答案中抽丝剥茧精准挑选出符合题意的那一个正解！"),
            ("ankreuzen", "", "v.", "kreuzt an, kreuzte an, angekreuzt", "在选项字母处勾选填涂", "Kreuzen Sie auf dem Auswertungsbogen deutlich mit schwarzem Kugelschreiber an!", "请使用黑色油性圆珠笔在专用评卷卡对应字母方框内清晰规范地填涂打叉勾选！"),
            ("die Korrektur", "die", "n.", "-en", "笔误涂改纠错标记", "Wenn Sie sich geirrt haben, schwärzen Sie das falsche Feld und kreuzen neu an!", "如果发现误选填错，请将错误方框彻底涂黑作废，并在正确字母方块重新打叉！"),
            ("die Richtigkeit", "die", "n.", "-", "推断判断的正确准确性", "Überprüfen Sie die grammatikalische Richtigkeit Ihrer verfassten Sätze!", "完成短文写作后务必从头至尾通读一遍，复核确认词尾变位等语法维度的准确性！"),
            ("richtig", "", "adj.", "", "选项相符正确的", "Diese Aussage stimmt vollkommen mit den Angaben im Text überein und ist richtig.", "该项陈述在文意逻辑上与原文段落披露的信息分毫不差，因此属正确表述。"),
            ("falsch", "", "adj.", "", "与事实相悖错误的", "Diese Behauptung widerspricht dem Zeitungsbericht und ist dementsprechend falsch.", "该项言之凿凿的推断直接与新闻报道披露的客观事实相悖，理所当然判为错误。"),
            ("der Textabschnitt", "der", "n.", "-e", "文章局部自然段落", "Im zweiten Textabschnitt finden Sie die Lösung für Frage Nummer vier.", "移步文章第二自然段，大家便能极其容易地锁定第四道考题的核心解题依据。"),
            ("die Zeile", "die", "n.", "-n", "排版印刷行数行距", "Notieren Sie die genaue Zeilennummer als Nachweis für Ihre Antwort!", "请将答案直接对应的具体正文行号在草稿纸上顺手记下一笔以便回溯核验！"),
            ("überfliegen", "", "v.", "überfliegt, überflog, überflogen", "扫读略读快速浏览", "Überfliegen Sie den Text zunächst oberflächlich, um das Hauptthema zu erfassen!", "动笔前请先花半分钟自上而下快速通篇扫读一遍，迅速提炼捕捉文章宏观主旨！"),
            ("das Detail", "das", "n.", "-s", "细节微末事实要素", "Lesen Sie nun ein zweites Mal selektiv, um gezielt nach relevanten Details zu suchen!", "接下来请带着具体问题展开第二遍针对性精读，地毯式搜寻所有相关细节要素！"),
            ("der Kontext", "der", "n.", "-e", "语境上下文行文逻辑", "Erschließen Sie die Bedeutung unbekannter Wörter aus dem logischen Gesamtkontext!", "即便遇上偶尔几个生词也切莫慌乱，完全可以借助上下文行文逻辑从容推断。"),
            ("verstehen", "", "v.", "versteht, verstand, verstanden", "领会主旨洞察文意", "Wichtig ist, dass Sie den Sinnzusammenhang im Kern zuverlässig verstehen.", "最关键的在于，你必须能够从全局上笃定把握整段文字内在的核心语义连贯。"),
            ("die Hördatei", "die", "n.", "-en", "听力录音音频文件", "Die Hördatei wird bei einigen Aufgaben zweimal, bei anderen nur einmal abgespielt.", "听力音频按照题型要求不同，有的仅单次播音，有的则依规连续播音两遍。"),
            ("der Sprecher", "der", "n.", "-", "标准普通话播音男声", "Der Sprecher artikuliert die Vokabeln mit klarer und akzentfreier Aussprache.", "录音中的专业播音员吐字归音清晰醇厚，通篇采用标准无口音的标准德语录制。"),
            ("die Sprecherin", "die", "n.", "-nen", "标准普通话播音女声", "Die Sprecherin kündigt den Beginn des nächsten Prüfungsteils an.", "女播音员极其专业严谨地宣读播报着下一大题听力理解正式开考的指令通告。"),
            ("der Dialog", "der", "n.", "-e", "双人情境日常对话", "Im Dialog zwischen Verkäufer und Kundin geht es um eine Reklamation.", "在这段发生在营业员与顾客之间的日常对话里，焦点集中在商品售后质量退赔。"),
            ("das Monolog", "das", "n.", "-e", "独白短文，个人陈述", "Im Monolog auf der Mailbox hinterlässt der Vermieter eine Nachricht.", "在电话语音信箱留言独白里，房东详细说明了有关下周上门抄水表的时间约定。"),
            ("die Telefonansage", "die", "n.", "-en", "客服热线自动语音导航", "Die automatische Telefonansage informiert über geänderte Öffnungszeiten der Praxis.", "诊所总机自动应答语音导航在电话中通报了本周医生坐诊出诊时间的临时变动。"),
            ("die Ansage", "die", "n.", "-n", "公共站场广播通报", "Achten Sie bei der Ansage am Gleis auf die Ziffern der Bahnsteige und Wagen!", "在收听站台大喇叭广播时，请全神贯注抓取所报列车停靠站台股道与对应车厢号！"),
            ("die Notiz", "die", "n.", "-en", "要点提纲简短备忘", "Machen Sie sich während des Hörens schnelle stichpunktartige Notizen!", "在录音播放期间，请拿起铅笔在试卷空白处飞速记录下关键时间节点与数字！"),
            ("mitschreiben", "", "v.", "schreibt mit, schrieb mit, mitgeschrieben", "随听速记要点信息", "Schreiben Sie entscheidende Ziffern, Namen und Ortsangaben sofort mit!", "听到决定解题走向的日期钟点、人名地名及价格金额时务必眼疾手快顺手记下！"),
            ("das Schreiben", "das", "n.", "-", "书面表达写作测试", "Im Prüfungsteil Schreiben müssen Sie zwei kurze, präzise Texte verfassen.", "在写作大题环节，考生需在短短半小时内行云流水拟写两篇地道规范的实用短文。"),
            ("die Textsorte", "die", "n.", "-n", "文体体裁应用文分类", "Unterscheiden Sie strikt zwischen informellen und formellen Textsorten!", "在落笔构思前必须准确区分：此篇究竟是写给挚友的随性便条还是致函公立机构的公函！"),
            ("die E-Mail", "die", "n.", "-s", "电子书信，电子邮件", "Verfassen Sie eine E-Mail an Ihren Sprachlehrer und bitten Sie um Entschuldigung!", "请给您的德语主讲老师起草一封简明扼要的请假信，就您昨日的缺席诚恳致歉！"),
            ("die Anrede", "die", "n.", "-n", "开头起首称谓称呼", "Wählen Sie für Freunde 'Lieber / Liebe...' und für Institutionen 'Sehr geehrte...'!", "致亲近友人信头称呼请用Lieber/Liebe，而在正式商务公函中必须严格使用Sehr geehrte...！"),
            ("die Grußformel", "die", "n.", "-n", "篇末致意落款客套语", "Beenden Sie formelle Briefe ausnahmslos mit 'Mit freundlichen Grüßen'!", "写给公司或主管机关的正式文书中篇末致敬语无一例外应使用Mit freundlichen Grüßen！"),
            ("die Einleitung", "die", "n.", "-en", "破题首句，开篇引言", "In der Einleitung nennen Sie knapp und unmissverständlich den Grund Ihres Schreibens.", "在公函首段破题引言部分，请开门见山用一句话清晰交代你本次去信的直接诉求。"),
            ("der Hauptteil", "der", "n.", "-e", "核心正文推演主体", "Behandeln Sie im Hauptteil zwingend alle in der Aufgabenstellung geforderten Leitpunkte!", "在正文主体部分，题干所明示给出的每一个核心要点均须予以充分呼应与阐述！"),
            ("der Leitpunkt", "der", "n.", "-e", "考核大纲必须涵盖的要点", "Wenn ein Leitpunkt im Text völlig fehlt, führt dies zu drastischem Punktabzug.", "如果在作文正文里将题干要求的某个必备采分点遗漏未提，将招致严厉扣分。"),
            ("der Schluss", "der", "n.", "Schlüsse", "收束尾段，结论", "Im Schlusssatz formulieren Sie eine höfliche Bitte um baldige Rückmeldung.", "在正文结尾句中，极其得体地向对方提出期待尽快收到答复或确认函的礼貌请求。"),
            ("die Wortanzahl", "die", "n.", "-", "作文正文字数规模", "Die geforderte Wortanzahl liegt bei etwa 30 bis 40 Wörtern pro Schreibaufgabe.", "歌德A2每篇作文规定的字数通常在30至40词之间，多写无益精练达意最为关键。"),
            ("der Satzbau", "der", "n.", "-", "句式构造型态语法语序", "Achten Sie auf korrekten Satzbau mit dem Verb an zweiter Position im Hauptsatz!", "在草拟每一个陈述句时时刻牢记德语第一铁律：主句中的变位动词永远占第二位！"),
            ("die Konnektoren", "die", "n.pl.", "-", "篇章逻辑连接纽带词", "Verknüpfen Sie Sätze sinnvoll mit Konnektoren wie weil, dass, wenn oder deshalb!", "巧妙借助weil、dass、wenn或deshalb等从属及副词性连词，使整篇文章逻辑缜密。"),
            ("das Sprechen", "das", "n.", "-", "现场口语口头表达", "Im Prüfungsteil Sprechen treten Sie als Paar vor die zwei Prüfungspersonen.", "在口试阶段，考生将以二人结对为组的形式共同走入考场直面两位主考教师。"),
            ("die Partnerarbeit", "die", "n.", "-en", "搭档协同演练配合", "In Teil 3 wird eine partnerschaftliche Kooperation auf Augenhöhe erwartet.", "在口语第三节互动协商环节中，考官期待看到双方平起平坐、有来有回的默契互动。"),
            ("sich vorstellen", "", "v.", "stellt sich vor, stellte sich vor, sich vorgestellt", "落落大方做自我介绍", "In Teil 1 stellt sich jeder Kandidat anhand von Stichwortkarten kurz vor.", "在第一部分，每位考生需对照写有姓名职业年龄等要点的题卡落落大方做自我陈述。"),
            ("die Rückfrage", "die", "n.", "-n", "就细节追问反问提问", "Der Prüfer stellt nach Ihrer Vorstellung ein oder zwei spontane Rückfragen.", "在你流畅完成自我介绍后，主考官会微笑着就某个具体细节即兴向你抛出一两个追问。"),
            ("buchstabieren", "", "v.", "buchstabiert, buchstabierte, buchstabiert", "口头拼读姓名字母", "Können Sie bitte Ihren Wohnort oder Ihren Familiennamen buchstabieren?", "您能把您目前居住所在城市的名字或您本人的姓氏字母清晰拼读一下吗？"),
            ("die Ziffer", "die", "n.", "-n", "数字阿拉伯数码", "Sagen Sie Ihre Telefonnummer Ziffer für Ziffer auf Deutsch auf!", "请用标准的德语把您手机号码的一位位阿拉伯数字沉稳清晰地念出来！"),
            ("das Thema", "das", "n.", "Themen", "口试抽卡主题板块", "In Teil 2 ziehen Sie eine Bild- oder Textkarte zu einem alltäglichen Thema.", "在第二部分，考生将随机抽取一张描摹日常生活日常场景的话题卡展开个人口头陈述。"),
            ("erzählen", "", "v.", "erzählt, erzählte, erzählt", "娓娓道来叙述见闻", "Erzählen Sie etwas über Ihre Freizeitbeschäftigungen am Wochenende!", "请联系您自身的真实生活，向考官娓娓道来您通常在周末是如何度过休闲时光的！"),
            ("die Karte", "die", "n.", "-n", "考官提供的抽卡题卡", "Auf der gezogenen Karte steht ein zentraler Begriff wie 'Einkaufen' oder 'Wohnen'.", "抽取的题卡中央印着一个鲜明的生活场景核心词，诸如“商场采买”或“租房起居”。"),
            ("der Vorschlag", "der", "n.", "Vorschläge", "建设性协商提议建议", "Machen Sie Ihrem Partner einen Vorschlag zur gemeinsamen Freizeitgestaltung!", "请向你的考场搭档主动抛出一个关于本周末结伴出游共同开展活动的建设性提议！"),
            ("vorschlagen", "", "v.", "schlägt vor, schlug vor, vorgeschlagen", "主动提议，建议", "Ich schlage vor, dass wir uns am Samstag um 10 Uhr am Hauptbahnhof treffen.", "我建议咱们本周六上午十点整在市中心的火车总站大钟下碰头，你看怎么样？"),
            ("reagieren", "", "v.", "reagiert, reagierte, reagiert", "对搭档发言做出应答", "Reagieren Sie spontan und höflich auf den Einwand Ihres Gesprächspartners!", "当同桌搭档对你的出游提议面露难色或提出异议时，请务必从容礼貌做出灵动应答！"),
            ("die Einigung", "die", "n.", "-en", "求同存异达成共识", "Am Ende des Dialogs müssen Sie und Ihr Partner zu einer Einigung kommen.", "在协商对话结束前，你和搭档必须最终就具体的碰头活动时间与地点达成一致共识。"),
            ("einigen", "", "v.", "einigt, einigte, geeinigt", "在某事上达成完全一致", "Wir haben uns darauf geeinigt, gemeinsam ins städtische Museum zu gehen.", "经过友好商讨，我们两人最终欣然达成一致意见：周日结伴去市博物馆看特展。"),
            ("die Flüssigkeit", "die", "n.", "-", "语言表达流利连贯度", "Flüssigkeit im Sprechen wird höher bewertet als übertriebene Perfektion.", "考官在评分时极其看重语流连贯与敢于开口，其权重远胜过因追求绝对完美而不断卡顿。"),
            ("das Selbstvertrauen", "das", "n.", "-", "自信笃定必胜从容信念", "Mit solidem Wortschatz und gründlicher Vorbereitung haben Sie volles Selbstvertrauen.", "只要肚里有了扎实浑厚的词汇储备并吃透应试规律，你自能胸有成竹、气定神闲跨入考场。"),
            ("die Konzentration", "die", "n.", "-", "全神贯注临场专注力", "Halten Sie die Konzentration über die gesamte Prüfungsdauer konsequent hoch!", "在长达两个多小时的整场应试拉锯战中，始终将注意力与专注力紧紧锚定在试卷卷面上！"),
            ("der Erfolg", "der", "n.", "-e", "高分夺魁斩获大捷", "Mit Gelassenheit, Ausdauer und diesem Training ist Ihnen der Erfolg sicher!", "凭借这种沉着从容的心态、滴水穿石的坚毅与这套全真冲刺秘籍，你必将高分斩获大捷！")
        ]
    }
]
