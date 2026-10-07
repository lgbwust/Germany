#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B1 Part 3: Lessons 11 to 15 (350 words)
L11: 文学经典、戏剧艺术与影视鉴赏 (Literatur, Theater & Filmkunst) - 70 words
L12: 未来交通出行、城市规划与绿色出行变革 (Verkehrswende, Mobilität & Städtebau) - 70 words
L13: 情绪心理学、心理健康与压力管理 (Psychologie, Emotionen & Stressbewältigung) - 70 words
L14: 德语区近现代历史、政经格局与国情 (Geschichte, Politik & Gesellschaft) - 70 words
L15: 歌德 B1 综合应试冲刺与高分通关 (Goethe B1 Prüfungstraining & Redemittel) - 70 words
"""

LESSONS_B1_PART3 = [
    # LESSON 11
    {
        "id": "B1_L11",
        "title": "第11课：文学经典、戏剧艺术与影视鉴赏 (Literatur & Kunst)",
        "summary": "掌握第一分词 (Partizip I) 与第二分词 (Partizip II) 作定语修饰名词的语法与德语艺术文学核心词汇",
        "grammar": {
            "title": "分词作定语 (Partizip I und Partizip II als Adjektiv)",
            "sections": [
                {
                    "heading": "1. 第一分词 (Partizip I: 动词不定式 + d): 表示主动与正在进行：",
                    "content": "• das spielende Kind (正在玩耍的孩子 = das Kind, das spielt)\n• die steigenden Preise (不断上涨的物价 = die Preise, die steigen)\n• 变格规则与普通形容词完全相同（如 ein lesender Schüler, der lesende Schüler）。"
                },
                {
                    "heading": "2. 第二分词 (Partizip II: ge-...-(e)t / ge-...-en): 表示及物动词的被动或不及物动词的完成：",
                    "content": "• das gelesene Buch (被读过的书 = das Buch, das gelesen wurde)\n• der angekommene Zug (已经到达的列车 = der Zug, der angekommen ist)\n• 不及物表示完成的动词必须与 sein 搭配构成完成时。"
                }
            ]
        },
        "quiz": [
            {
                "id": "B1_L11_Q1",
                "type": "GRAMMAR_FILL",
                "question": "Das ______ (singen) Mädchen beeindruckte das gesamte Theaterpublikum.",
                "options": ["singende", "gesungene", "singt", "gesungen"],
                "correctIndex": 0,
                "explanation": "女孩自己发出唱歌动作且正在发生，使用第一分词定语形式 das singende Mädchen。"
            },
            {
                "id": "B1_L11_Q2",
                "type": "MEANING_SELECT",
                "question": "“die Aufführung” 在艺术戏剧领域的精确中文含义是：",
                "options": ["演出，上演", "画展", "雕塑作品", "剧本出版"],
                "correctIndex": 0,
                "explanation": "die Aufführung 表示“演出，上演，上演的剧目”。"
            },
            {
                "id": "B1_L11_Q3",
                "type": "GRAMMAR_FILL",
                "question": "Der vom Regisseur neu ______ (verfilmen) Roman feierte Premiere.",
                "options": ["verfilmte", "verfilmende", "verfilmt", "verfilmtet"],
                "correctIndex": 0,
                "explanation": "小说被电影化，表示被动与完成，用第二分词 verfilmt + 阳性一格弱变化词尾 -e: der verfilmte Roman。"
            },
            {
                "id": "B1_L11_Q4",
                "type": "LISTENING_MCQ",
                "question": "“Das Bühnenbild schuf eine geheimnisvolle Atmosphäre.” 的中文含义是：",
                "options": ["舞台布景营造出神秘的氛围。", "演员的声音极富感染力。", "导演在谢幕时发言。", "剧本的情节十分荒诞。"],
                "correctIndex": 0,
                "explanation": "Bühnenbild = 舞台布景，Atmosphäre = 氛围。"
            },
            {
                "id": "B1_L11_Q5",
                "type": "SENTENCE_BUILDER",
                "question": "将下列语块组合为规范陈述句：“begeisterte / Das Stück / das gesamte / Publikum”",
                "options": ["Das Stück begeisterte das gesamte Publikum.", "Begeisterte das gesamte Publikum das Stück.", "Das gesamte Stück das Publikum begeisterte.", "Das Stück das gesamte Publikum begeisterte."],
                "correctIndex": 0,
                "explanation": "标准德语语序：主语(Das Stück) + 谓语动词(begeisterte) + 宾语(das gesamte Publikum)。"
            }
        ],
        "words": [
            ("die Literatur", "die", "Nomen", "-en", "文学", "Die deutsche Literatur des 18. Jahrhunderts ist weltweit bekannt.", "18世纪的德国文学闻名遐迩。"),
            ("der Roman", "der", "Nomen", "-e", "长篇小说", "Er liest gern historische Romane.", "他喜欢读历史小说。"),
            ("das Drama", "das", "Nomen", "Dramen", "戏剧，惨剧", "Goethes 'Faust' ist ein weltberühmtes Drama.", "歌德的《浮士德》是举世闻名的戏剧。"),
            ("die Tragödie", "die", "Nomen", "-n", "悲剧", "Die Aufführung der Tragödie berührte die Zuschauer tief.", "这部悲剧的演出深深触动了观众。"),
            ("die Komödie", "die", "Nomen", "-n", "喜剧", "Am Freitagabend sehen wir eine amüsante Komödie.", "周五晚上我们看了一部有趣的喜剧。"),
            ("das Gedicht", "das", "Nomen", "-e", "诗歌", "Schüler lernen dieses berühmte Gedicht auswendig.", "学生们背诵这首著名的诗歌。"),
            ("die Poesie", "die", "Nomen", "unz.", "诗意，诗歌", "In seinen Texten steckt viel Poesie.", "他的文字充满了诗意。"),
            ("der Schriftsteller", "der", "Nomen", "-", "作家（男）", "Der Schriftsteller erhielt für sein Werk einen Literaturpreis.", "这位作家因其作品获得了文学奖。"),
            ("die Autorin", "die", "Nomen", "-nen", "作者，作家（女）", "Die Autorin stellte ihr neues Buch auf der Frankfurter Buchmesse vor.", "这位女作家在法兰克福书展上介绍了她的新书。"),
            ("das Werk", "das", "Nomen", "-e", "作品，著作", "Das gesamte Werk des Künstlers wird hier ausgestellt.", "这位艺术家的全部作品在此展出。"),
            ("der Dichter", "der", "Nomen", "-", "诗人", "Heinrich Heine war ein bedeutender deutscher Dichter.", "海因里希·海涅是一位杰出的德国诗人。"),
            ("die Biografie", "die", "Nomen", "-n", "传记", "Ich habe eine spannende Biografie über Albert Einstein gelesen.", "我读了一本关于爱因斯坦的引人入胜的传记。"),
            ("die Erzählung", "die", "Nomen", "-en", "短篇小说，叙事故事", "Kafka schrieb faszinierende Erzählungen.", "卡夫卡写了许多引人入胜的中短篇故事。"),
            ("das Kapitel", "das", "Nomen", "-", "章节", "Das letzte Kapitel beantwortet alle offenen Fragen.", "最后一章回答了所有悬而未决的问题。"),
            ("die Handlung", "die", "Nomen", "-en", "剧情，故事情节", "Die Handlung des Films ist voller unerwarteter Wendungen.", "这部电影的情节充满了出人意料的转折。"),
            ("der Charakter", "der", "Nomen", "Charaktere", "性格，人物角色", "Die Hauptfigur hat einen sehr komplexen Charakter.", "主角拥有非常复杂的性格特质。"),
            ("die Figur", "die", "Nomen", "-en", "人物，形象", "Er spielt eine geheimnisvolle Figur im Theaterstück.", "他在话剧中扮演一个神秘的人物。"),
            ("die Rolle", "die", "Nomen", "-n", "角色", "Sie übernimmt die Hauptrolle in der Oper.", "她在歌剧中担纲主角。"),
            ("das Theater", "das", "Nomen", "-", "剧院，戏剧", "Wir gehen am Wochenende ins Deutsche Theater.", "我们周末去德意志剧院。"),
            ("die Bühne", "die", "Nomen", "-n", "舞台", "Die Schauspieler betreten die Bühne.", "演员们走上舞台。"),
            ("der Schauspieler", "der", "Nomen", "-", "男演员", "Er ist ein bekannter Theater- und Filmschauspieler.", "他是一位知名的话剧和电影演员。"),
            ("die Darstellerin", "die", "Nomen", "-nen", "女演员", "Die Darstellerin überzeugte durch ihr emotionales Spiel.", "这位女演员以富有感染力的表演打动了全场。"),
            ("die Inszenierung", "die", "Nomen", "-en", "排演，导演呈现", "Die moderne Inszenierung des Klassikers spaltete die Kritik.", "这部经典作品的现代版排演引发了批评界的两极分化。"),
            ("die Regie", "die", "Nomen", "-n", "导演，执导", "Wer führt bei diesem Kinofilm Regie?", "谁执导这部院线电影？"),
            ("der Regisseur", "der", "Nomen", "-e", "导演", "Der Regisseur erklärte den Darstellern jede Szene im Detail.", "导演详细地向演员解释每个镜头场景。"),
            ("die Aufführung", "die", "Nomen", "-en", "演出，上演", "Wegen des großen Erfolgs gibt es eine zusätzliche Aufführung.", "鉴于取得巨大成功，剧院增加了一场演出。"),
            ("das Publikum", "das", "Nomen", "unz.", "观众，受众", "Das Publikum applaudierte minutenlang im Stehen.", "观众起立鼓掌长达数分钟。"),
            ("der Beifall", "der", "Nomen", "unz.", "喝彩，掌声", "Die gelungene Vorstellung erntete tosenden Beifall.", "精彩的演出赢得了雷鸣般的掌声。"),
            ("die Premiere", "die", "Nomen", "-n", "首映，首演", "Karten für die morgige Premiere waren sofort vergriffen.", "明晚首映式的门票瞬间售罄。"),
            ("die Kritik", "die", "Nomen", "-en", "评论，批评", "Die Zeitung veröffentlichte eine begeisterte Kritik.", "报纸发表了一篇赞不绝口的好评。"),
            ("der Kritiker", "der", "Nomen", "-", "评论家", "Die Kritiker lobten die visuelle Gestaltung des Films.", "评论家们盛赞了这部电影的视觉设计。"),
            ("der Film", "der", "Nomen", "-e", "电影", "Dieser Dokumentarfilm behandelt den Schutz der Ozeane.", "这部纪录片探讨了海洋保护问题。"),
            ("das Kino", "das", "Nomen", "-s", "电影院", "Wir verabreden uns vor dem Kino am Potsdamer Platz.", "我们约在波茨坦广场的电影院前碰头。"),
            ("der Regisseur", "der", "Nomen", "-e", "导演", "Der junge Regisseur gewann den Goldenen Bären.", "年轻导演荣获了金熊奖。"),
            ("die Leinwand", "die", "Nomen", "-e", "银幕，画布", "Auf der großen Leinwand wirken die Bilder überwältigend.", "在大银幕上，画面呈现得令人震撼。"),
            ("das Drehbuch", "das", "Nomen", "-er", "剧本", "Das Drehbuch basiert auf Tatsachenberichten.", "这部剧本改编自真实新闻报道。"),
            ("der Soundtrack", "der", "Nomen", "-s", "原声配乐", "Die Musik des Soundtracks erzeugt echte Gänsehaut.", "配乐原声让人起了一身鸡皮疙瘩。"),
            ("das Meisterwerk", "das", "Nomen", "-e", "杰作，巨著", "Beethovens neunte Sinfonie ist ein unvergängliches Meisterwerk.", "贝多芬第九交响曲是一部不朽的传世杰作。"),
            ("das Museum", "das", "Nomen", "Museen", "博物馆", "Die Berliner Museumsinsel gehört zum UNESCO-Weltkulturerbe.", "柏林博物馆岛属于联合国教科文组织世界文化遗产。"),
            ("die Ausstellung", "die", "Nomen", "-en", "展览，博览会", "Die Ausstellung zeitgenössischer Kunst lockt viele Gäste an.", "当代艺术展览吸引了众多参观者。"),
            ("das Gemälde", "das", "Nomen", "-", "油画，画作", "Das berühmte Gemälde hängt im Louvre.", "这幅传世名画悬挂在卢浮宫内。"),
            ("der Künstler", "der", "Nomen", "-", "艺术家", "Künstler aus aller Welt stellen ihre Werke in Leipzig aus.", "来自世界各地的艺术家在莱比锡展出作品。"),
            ("die Skulptur", "die", "Nomen", "-en", "雕塑，雕像", "Die bronzene Skulptur steht auf dem Marktplatz.", "青铜雕塑矗立在集市广场上。"),
            ("die Architektur", "die", "Nomen", "-en", "建筑风格，建筑学", "Das Bauhaus prägte die moderne Architektur des 20. Jahrhunderts.", "包豪斯学派深刻塑造了20世纪的现代建筑风貌。"),
            ("das Denkmal", "das", "Nomen", "-er", "纪念碑，名胜古迹", "Historische Denkmäler müssen unter Denkmalschutz gestellt werden.", "历史纪念建筑必须列入文物保护名录。"),
            ("das Kulturerbe", "das", "Nomen", "unz.", "文化遗产", "Historische Altstädte sind ein kostbares Kulturerbe.", "历史老城是宝贵的文化遗产。"),
            ("die Inspiration", "die", "Nomen", "-en", "灵感，启迪", "Natur und Reisen dienen dem Maler als Inspiration.", "大自然和旅行是这位画家的灵感源泉。"),
            ("die Fantasie", "die", "Nomen", "-n", "想象力", "Kinderbücher regen die Fantasie der Kleinen an.", "儿童图书激发孩子们的想象力。"),
            ("der Geschmack", "der", "Nomen", "-er", "品味，鉴赏力", "Über Geschmack lässt sich bekanntlich nicht streiten.", "众所周知，关于个人品味无需争论。"),
            ("das Genre", "das", "Nomen", "-s", "体裁，类型", "Science-Fiction ist sein bevorzugtes literarisches Genre.", "科幻小说是他最喜爱的文学体裁。"),
            ("der Bestseller", "der", "Nomen", "-", "畅销书", "Der Thriller wurde innerhalb einer Woche zum Bestseller.", "这部惊悚小说在一周内跃居畅销书榜首。"),
            ("die Bibliothek", "die", "Nomen", "-en", "图书馆", "Die Universitätsbibliothek bietet Tausende digitaler Fachbücher.", "大学图书馆提供数以千计的数字化专业图书。"),
            ("das Manuskript", "das", "Nomen", "-e", "手稿，底稿", "Der Verlag prüft das eingereichte Manuskript gründlich.", "出版社正在仔细审核提交的手稿。"),
            ("der Verlag", "der", "Nomen", "-e", "出版社", "Der Suhrkamp Verlag verlegt anspruchsvolle Literatur.", "苏尔坎普出版社出版高品位文学作品。"),
            ("die Metapher", "die", "Nomen", "-n", "隐喻，暗喻", "Die 'Mauer im Kopf' ist eine bekannte deutsche Metapher.", "“头脑中的柏林墙”是一个著名的德语隐喻。"),
            ("das Zitat", "das", "Nomen", "-e", "引语，名言", "Der Vortragende begann seine Rede mit einem Zitat von Goethe.", "演讲者以一句歌德的名言开启了他的发言。"),
            ("zitieren", "kein", "Verb", "zitierte, zitiert", "引用，引述", "In wissenschaftlichen Arbeiten muss man Quellen exakt zitieren.", "在学术论文中必须准确引用参考文献。"),
            ("verfassen", "kein", "Verb", "verfasste, verfasst", "撰写，起草", "Er verfasste einen kritischen Kommentar zum neuen Film.", "他为这部新电影撰写了一篇犀利的评论。"),
            ("verfilmen", "kein", "Verb", "verfilmte, verfilmt", "把…拍成电影", "Der preisgekrönte Roman wird demnächst in Berlin verfilmt.", "这部获奖小说即将在柏林被搬上银幕。"),
            ("aufführen", "kein", "Verb", "führte auf, aufgeführt", "上演，演出", "Das Ensemble führt ein dramatisches Werk von Schiller auf.", "剧团上演了席勒的一部戏剧作品。"),
            ("darstellen", "kein", "Verb", "stellte dar, dargestellt", "表现，扮演", "Die Schauspielerin stellt eine mutige Widerstandskämpferin dar.", "女演员扮演了一位勇敢的反抗战士。"),
            ("faszinieren", "kein", "Verb", "faszinierte, fasziniert", "深深吸引，迷住", "Die magische Bildsprache des Films fasziniert das Publikum.", "电影魔幻般的画面语言深深迷住了观众。"),
            ("berühren", "kein", "Verb", "berührte, berührt", "感动，触动", "Seine Abschiedsrede hat alle Anwesenden zu Tränen berührt.", "他的告别演讲让在场的所有人感动落泪。"),
            ("begeistern", "kein", "Verb", "begeisterte, begeistert", "使振奋，使狂热", "Die meisterhafte Aufführung begeisterte Jung und Alt.", "精湛的演出令老少观众无不拍手称快。"),
            ("kreativ", "kein", "Adjektiv", "-", "有创造力的", "Sie fand eine kreative Lösung für das knifflige Problem.", "她为这个棘手的问题找到了极具创意的解法。"),
            ("originell", "kein", "Adjektiv", "-", "新颖独创的", "Seine Idee zur Inszenierung ist überaus originell.", "他的剧目排演构思极为新颖独特。"),
            ("eindrucksvoll", "kein", "Adjektiv", "-", "令人印象深刻的", "Die historische Kulisse bot einen eindrucksvollen Anblick.", "历史建筑布景展现出令人叹为观止的壮观景象。"),
            ("anspruchsvoll", "kein", "Adjektiv", "-", "高要求的，高品位的", "Klassische Musik ist ein sehr anspruchsvolles Kunstgenre.", "古典音乐是一门门槛与品位极高的艺术流派。"),
            ("umstritten", "kein", "Adjektiv", "-", "有争议的", "Das provokante Theaterstück war bei der Kritik umstritten.", "这部挑衅性的话剧在评论界备受争议。"),
            ("zeitgenössisch", "kein", "Adjektiv", "-", "当代的", "In Berlin kann man überall zeitgenössische Kunst entdecken.", "在柏林，人们随处都能发现当代前沿艺术。")
        ]
    },

    # LESSON 12
    {
        "id": "B1_L12",
        "title": "第12课：未来交通出行、城市规划与绿色出行变革 (Verkehrswende)",
        "summary": "掌握无人称被动态与 man 结构转换、绿色公共交通系统与未来智慧城市建设核心词汇",
        "grammar": {
            "title": "无人称被动态 (Unpersönliches Passiv) 与 man 替换",
            "sections": [
                {
                    "heading": "1. 无人称被动态：无宾语的不及物动词构成被动态，强调事件发生：",
                    "content": "• Hier wird fleißig gebaut. (这里正在火热施工。)\n• In Deutschland wird sonntags nicht gearbeitet. (在德国周日不工作。)\n• 若 es 置于句首充当形式主语：Es wird viel über die Verkehrswende diskutiert.（若其他成分放句首，es 必须省略：Über die Verkehrswende wird viel diskutiert）。"
                },
                {
                    "heading": "2. 被动态与 man 的互换：",
                    "content": "• Man baut eine neue Fahrradstraße. = Eine neue Fahrradstraße wird gebaut.\n• Man darf hier nicht parken. = Hier darf nicht geparkt werden."
                }
            ]
        },
        "quiz": [
            {
                "id": "B1_L12_Q1",
                "type": "GRAMMAR_FILL",
                "question": "In dieser Fußgängerzone ______ (dürfen) nicht mit dem Auto gefahren werden.",
                "options": ["darf", "dürfen", "wird", "kann"],
                "correctIndex": 0,
                "explanation": "无人称被动态中，若没有真正主语，助动词永远用单数第三人称 darf。"
            },
            {
                "id": "B1_L12_Q2",
                "type": "MEANING_SELECT",
                "question": "“der Berufsverkehr” 的德语含义是：",
                "options": ["上下班高峰交通", "职业物流货运", "专业驾驶资格考试", "跨国航班调度"],
                "correctIndex": 0,
                "explanation": "der Berufsverkehr 指早晚通勤时段的“上下班高峰交通”。"
            },
            {
                "id": "B1_L12_Q3",
                "type": "GRAMMAR_FILL",
                "question": "______ wird im Stadtzentrum ein neues U-Bahn-Netz gebaut.",
                "options": ["Zurzeit", "Es zurzeit", "Weil", "Dass"],
                "correctIndex": 0,
                "explanation": "当句首已有状语 Zurzeit 时，无人称被动态的形式主语 es 必须省略，动词直接位于第二位。"
            },
            {
                "id": "B1_L12_Q4",
                "type": "LISTENING_MCQ",
                "question": "“Der Ausbau des Radwegenetzes entlastet die Innenstadt.” 的正确理解是：",
                "options": ["自行车道网络的扩建缓解了市中心的交通压力。", "市中心禁止骑行自行车。", "私家车道路正在全面拓宽。", "公共交通票价即将大幅上调。"],
                "correctIndex": 0,
                "explanation": "Ausbau = 扩建，entlasten = 减轻…的负担，Radwegenetz = 自行车道路网。"
            },
            {
                "id": "B1_L12_Q5",
                "type": "SENTENCE_BUILDER",
                "question": "重组语块：“auf umweltfreundliche Mobilität / setzt / Die moderne Stadt”",
                "options": ["Die moderne Stadt setzt auf umweltfreundliche Mobilität.", "Setzt auf umweltfreundliche Mobilität die moderne Stadt.", "Die moderne Stadt auf umweltfreundliche Mobilität setzt.", "Umweltfreundliche Mobilität die moderne Stadt setzt auf."],
                "correctIndex": 0,
                "explanation": "动词短语 setzen auf (+Akk.) 表示“寄望于/致力于…”，主语后接谓语动词。"
            }
        ],
        "words": [
            ("der Verkehr", "der", "Nomen", "unz.", "交通，通行", "Im Berufsverkehr kommt es regelmäßig zu Verzögerungen.", "在上下班交通高峰期经常发生延误。"),
            ("die Mobilität", "die", "Nomen", "unz.", "流动性，出行方式", "Nachhaltige Mobilität schont die Umwelt und spart Energie.", "可持续出行保护环境并节约能源。"),
            ("die Verkehrswende", "die", "Nomen", "unz.", "交通出行绿色转型", "Die Verkehrswende erfordert Investitionen in Bus und Bahn.", "交通绿色转型需要向公共汽电车与铁路大量注资。"),
            ("das Verkehrsmittel", "das", "Nomen", "-", "交通工具", "Das Fahrrad ist in Großstädten oft das schnellste Verkehrsmittel.", "在各大城市，自行车往往是最快捷的交通工具。"),
            ("der Nahverkehr", "der", "Nomen", "unz.", "近程公共交通", "Der öffentliche Personennahverkehr muss pünktlicher werden.", "城市近程公共客运必须更加守时准点。"),
            ("der Fernverkehr", "der", "Nomen", "unz.", "长途交通", "Im Fernverkehr setzt die Deutsche Bahn moderne ICE-Züge ein.", "在长途客运中，德国铁路投入了现代化的ICE高速列车。"),
            ("die Straßenbahn", "die", "Nomen", "-en", "有轨电车", "Die Straßenbahn fährt alle fünf Minuten direkt zum Hauptbahnhof.", "有轨电车每五分钟一趟直达火车总站。"),
            ("die U-Bahn", "die", "Nomen", "-en", "地铁", "In Hamburg und Berlin nutzt man täglich die U-Bahn.", "在汉堡和柏林，人们每天都乘坐地铁出行。"),
            ("die S-Bahn", "die", "Nomen", "-en", "城市快铁", "Die S-Bahn verbindet die Vororte mit dem Stadtzentrum.", "城市轻轨快铁将郊区与市中心紧密相连。"),
            ("das Ticket", "das", "Nomen", "-s", "车票，车券", "Das 49-Euro-Deutschlandticket gilt bundesweit im Nahverkehr.", "49欧元德国通票可在全国近程公共交通中使用。"),
            ("der Fahrschein", "der", "Nomen", "-e", "车票", "Bitte entwerten Sie Ihren Fahrschein vor dem Einsteigen.", "请在上车前将您的车票在打卡机上打孔生效。"),
            ("die Monatskarte", "die", "Nomen", "-n", "月票", "Studenten bekommen die Monatskarte zu einem ermäßigten Preis.", "大学生可以凭优惠价格购买公交月票。"),
            ("der Fahrgast", "der", "Nomen", "-e", "乘客", "Die Fahrgäste warten geduldig auf dem Bahnsteig.", "乘客们在站台上耐心地等待列车进站。"),
            ("der Pendler", "der", "Nomen", "-", "通勤者", "Tausende Pendler fahren täglich aus dem Umland zur Arbeit.", "成千上万的通勤族每天从城市周边郊区赶往市区上班。"),
            ("der Stau", "der", "Nomen", "-s", "堵车，交通拥堵", "Auf der Autobahn A8 gibt es zehn Kilometer Stau.", "在A8高速公路上出现了长达十公里的交通拥堵。"),
            ("die Verspätung", "die", "Nomen", "-en", "晚点，延误", "Wegen einer Stellwerkstörung hat der Zug 20 Minuten Verspätung.", "由于信号机房故障，列车延误了20分钟。"),
            ("der Ausfall", "der", "Nomen", "-e", "停运，取消", "Wegen des Streiks kommt es zu zahlreichen Zugausfällen.", "由于罢工，导致大量车次被迫停运取消。"),
            ("die Umleitung", "die", "Nomen", "-en", "绕行路线，改道", "Wegen einer Baustelle ist eine Umleitung eingerichtet.", "由于道路施工，现场设置了车辆绕行路线。"),
            ("die Baustelle", "die", "Nomen", "-n", "工地，道路施工区", "An der Baustelle gilt ein Tempolimit von 30 Stundenkilometern.", "在施工路段实行每小时30公里的限速。"),
            ("das Tempolimit", "das", "Nomen", "-s", "最高限速", "Umweltschützer fordern ein Tempolimit auf deutschen Autobahnen.", "环保人士呼吁在德国高速公路上设立法定限速标准。"),
            ("die Autobahn", "die", "Nomen", "-en", "高速公路", "Auf bestimmten Abschnitten der Autobahn gibt es keine Geschwindigkeitsbegrenzung.", "在德国高速公路的某些路段没有硬性速度限制。"),
            ("der Radweg", "der", "Nomen", "-e", "自行车道", "Die Stadt baut breite und sichere Radwege.", "市政府正在修建宽阔且安全的专用自行车道。"),
            ("die Fahrradstraße", "die", "Nomen", "-n", "自行车优先街道", "In der Fahrradstraße haben Radfahrer Vorrang vor Autos.", "在自行车专用街道上，骑行者相较于机动车拥有绝对优先权。"),
            ("das E-Bike", "das", "Nomen", "-s", "电动助力自行车", "Viele Bürger steigen für den Arbeitsweg auf das E-Bike um.", "许多市民在上下班通勤时转而选择骑乘电助力自行车。"),
            ("der E-Scooter", "der", "Nomen", "-", "电动滑板车", "E-Scooter dürfen nur auf Radwegen gefahren werden.", "电动滑板车仅允许在自行车专用车道上骑行。"),
            ("das Carsharing", "das", "Nomen", "unz.", "汽车共享", "Carsharing ist eine praktische Alternative zum eigenen Auto.", "共享汽车是替代购买私家车的一种极其便利的方案。"),
            ("der Fuhrpark", "der", "Nomen", "-s", "车队，机动车辆总成", "Das Unternehmen rüstet seinen Fuhrpark auf Elektroautos um.", "该企业正在将其全部公务车队改换为纯电动汽车。"),
            ("das Elektroauto", "das", "Nomen", "-s", "电动汽车", "Elektroautos stoßen beim Fahren keine schädlichen Abgase aus.", "电动汽车在行驶过程中不会排放有害尾气。"),
            ("die Ladestation", "die", "Nomen", "-en", "充电站，充电桩", "Entlang der Autobahn gibt es zahlreiche Schnellladestationen.", "沿高速公路沿线配备有大量的直流快速充电站。"),
            ("die Reichweite", "die", "Nomen", "-n", "续航里程，覆盖范围", "Moderne Akkus erhöhen die Reichweite von Elektrofahrzeugen.", "现代电池技术大幅提升了电动汽车的续航里程。"),
            ("die Batterie", "die", "Nomen", "-n", "蓄电池", "Die Lebensdauer der Batterie beträgt über acht Jahre.", "电池的使用寿命超过八年之久。"),
            ("die Emission", "die", "Nomen", "-en", "排放，废气排放", "Die Reduzierung von CO2-Emissionen ist ein globales Klimaziel.", "减少二氧化碳排放是一项全球气候行动目标。"),
            ("das Abgas", "das", "Nomen", "-e", "尾气，废气", "Strenge Abgasnormen verbessern die Luftqualität in Großstädten.", "严苛的尾气排放标准改善了大城市的环境空气质量。"),
            ("die Umweltzone", "die", "Nomen", "-n", "低排放环保区", "Alte Dieselfahrzeuge dürfen nicht in die grüne Umweltzone fahren.", "老旧柴油车不得驶入绿色低排放环保区。"),
            ("die Feinstaubbelastung", "die", "Nomen", "unz.", "细颗粒物/PM2.5污染负荷", "Im Winter steigt die Feinstaubbelastung in Talbecken stark an.", "在冬季，盆地地形内的细颗粒物污染负荷往往急剧飙升。"),
            ("die Lärmbelästigung", "die", "Nomen", "-en", "噪音骚扰，噪音污染", "Schallschutzwände schützen Anwohner vor Lärmbelästigung.", "隔音降噪墙有效保护了沿线居民免受噪音侵扰。"),
            ("die Fußgängerzone", "die", "Nomen", "-n", "步行街区", "In der Fußgängerzone darf man ungestört einkaufen und flanieren.", "在步行商业街上，人们可以不受车辆打扰地购物与闲逛。"),
            ("das Stadtzentrum", "das", "Nomen", "Stadtzentren", "市中心", "Das historische Stadtzentrum ist für Autos gesperrt.", "历史老城核心区已对机动车全面封闭。"),
            ("die Infrastruktur", "die", "Nomen", "-en", "基础设施", "Eine moderne Infrastruktur ist das Rückgrat der Wirtschaft.", "现代化的基础设施是国民经济运行的强劲脊梁。"),
            ("die Stadtplanung", "die", "Nomen", "unz.", "城市规划", "Moderne Stadtplanung setzt auf kurze Wege und Grünflächen.", "现代城市规划主张“15分钟生活圈”与广阔绿地相辅相成。"),
            ("die Grünfläche", "die", "Nomen", "-n", "绿地，公园绿化区", "Mehr Grünflächen senken die Temperatur in Hitzeperioden.", "更多的城市绿地能够在酷暑酷热期显著降低环境气温。"),
            ("der Parkplatz", "der", "Nomen", "-e", "停车位，停车场", "In Großstädten ist die Suche nach einem freien Parkplatz mühsam.", "在大城市里寻找空闲停车位极其费时费力。"),
            ("das Parkhaus", "das", "Nomen", "-er", "多层室内立体车库", "Das Parkhaus am Bahnhof ist rund um die Uhr geöffnet.", "火车站旁的立体停车楼全天24小时对外开放。"),
            ("das Parkticket", "das", "Nomen", "-s", "停车小票", "Vergessen Sie nicht, das Parkticket am Kassenautomaten zu bezahlen.", "请切记在自动缴费机上结清您的停车小票。"),
            ("die Maut", "die", "Nomen", "-en", "道路通行费，过路费", "Für Lastkraftwagen gilt in Deutschland eine streckenbezogene Maut.", "在德国，重型载货卡车按行驶里程缴纳道路通行费。"),
            ("der Zebrastreifen", "der", "Nomen", "-", "斑马线", "Fußgänger haben am Zebrastreifen absoluten Vorrang.", "行人在斑马线上享有绝对的道路通行先行权。"),
            ("die Ampel", "die", "Nomen", "-n", "交通信号灯", "Die Ampel schaltet von Rot auf Grün.", "交通信号灯由红灯变为了绿灯。"),
            ("die Kreuzung", "die", "Nomen", "-en", "十字路口", "An der gefährlichen Kreuzung ereigneten sich oft Unfälle.", "在这个危险的十字路口过去经常发生交通事故。"),
            ("der Kreisverkehr", "der", "Nomen", "-e", "环岛，环形交叉路口", "Im Kreisverkehr hat der im Kreis fahrende Verkehr Vorfahrt.", "在环岛交叉路口内，正在环岛内行驶的车辆拥有先行权。"),
            ("die Vorfahrt", "die", "Nomen", "unz.", "先行权，优先通行权", "Rechts vor Links ist die Grundregel für die Vorfahrt.", "“右侧来车先行”是德国没有信号灯时的基础优先原则。"),
            ("die Panne", "die", "Nomen", "-n", "车辆故障，抛锚", "Wegen einer Reifenpanne mussten wir auf dem Seitenstreifen anhalten.", "因为轮胎爆胎故障，我们不得不紧急停靠在应急车道上。"),
            ("der Abschleppdienst", "der", "Nomen", "-e", "汽车拖车救援服务", "Der Abschleppdienst brachte das defekte Auto in die Werkstatt.", "拖车救援队将故障车辆运送到了汽车修理厂。"),
            ("der Führerschein", "der", "Nomen", "-e", "驾照", "Mit 18 Jahren kann man in Deutschland den Führerschein machen.", "在德国，年满18周岁即可考取正式机动车驾驶执照。"),
            ("die Hauptuntersuchung", "die", "Nomen", "-en", "机动车年检 (TÜV)", "Jedes Fahrzeug muss alle zwei Jahre zur Hauptuntersuchung.", "所有机动车辆必须每两年参加一次法定的年检审查。"),
            ("der Bürgersteig", "der", "Nomen", "-e", "人行道", "Fahrräder dürfen nicht auf dem Gehweg oder Bürgersteig fahren.", "自行车绝对不允许在行人专用的人行道上骑行。"),
            ("die Geschwindigkeit", "die", "Nomen", "-en", "速度，行车时速", "Überhöhte Geschwindigkeit ist die Hauptursache schwerer Unfälle.", "超速行驶是诱发重大恶性交通事故的首要根源。"),
            ("die Trasse", "die", "Nomen", "-n", "铁路/公路规划线位", "Für den Hochgeschwindigkeitszug wird eine neue Trasse gebaut.", "正在为城际高速列车修建一条崭新的规划铁路专线。"),
            ("die Schiene", "die", "Nomen", "-n", "铁轨，钢轨", "Güter sollten verstärkt von der Straße auf die Schiene verlagert werden.", "大宗大件货物运输应当大力从公路分流转移至铁路轨道。"),
            ("das Streckennetz", "das", "Nomen", "-e", "线路网，航线网", "Das Streckennetz der S-Bahn wird kontinuierlich modernisiert.", "城市快铁的整体路网架构正在得到持续全面的升级改造。"),
            ("der Bahnhof", "der", "Nomen", "-e", "火车站", "Der Berliner Hauptbahnhof ist der größte Turmbahnhof Europas.", "柏林中央火车站是欧洲规模最大的立体十字枢纽火车站。"),
            ("der Bahnsteig", "der", "Nomen", "-e", "站台", "Vorsicht an Bahnsteig 3! Ein Zug fährt durch.", "3站台请注意！有一趟列车正在快速正线通过。"),
            ("umsteigen", "kein", "Verb", "stieg um, umgestiegen", "换乘，转乘", "In Frankfurt müssen Sie in den Zug nach München umsteigen.", "在法兰克福您需要换乘前往慕尼黑方向的列车。"),
            ("pendeln", "kein", "Verb", "pendelte, gependelt", "往返通勤", "Viele Menschen pendeln täglich zwischen Potsdam und Berlin.", "成千上万的人每天在波茨坦与柏林两座城市之间通勤往返。"),
            ("entlasten", "kein", "Verb", "entlastete, entlastet", "减轻负荷，缓解压力", "Eine neue Umgehungsstraße entlastet das Stadtzentrum spürbar.", "一条崭新的城市绕城外环公路显著缓解了老城中心的交通压力。"),
            ("stauen", "kein", "Verb", "staute, gestaut", "积聚，拥堵 (sich)", "Wegen Glatteis staut sich der Verkehr auf über 15 Kilometern.", "由于路面结冰打滑，道路交通严重拥堵积压超过15公里。"),
            ("überholen", "kein", "Verb", "überholte, überholt", "超车", "Auf zweispurigen Landstraßen ist das Überholen oft riskant.", "在双向两车道的乡间公路上超车往往伴随着极高的风险。"),
            ("ausbauen", "kein", "Verb", "baute aus, ausgebaut", "扩建，改善", "Die Stadtverwaltung baut das Schnellradnetz zügig aus.", "市政府正在开足马力高标准快速扩建城市快速自行车通勤通道。"),
            ("barrierefrei", "kein", "Adjektiv", "-", "无障碍的", "Alle Bahnhöfe der Stadt sollen bis 2026 barrierefrei sein.", "全市所有轨道车站计划在2026年之前全面完成无障碍适老化改造。"),
            ("effizient", "kein", "Adjektiv", "-", "高效的", "Ein integriertes Bussystem sorgt für effizienten Transport.", "高度一体化的公交专线系统确保了市民出行的高效快捷。"),
            ("überlastet", "kein", "Adjektiv", "-", "超负荷的，不堪重负的", "Zu den Stoßzeiten sind die Metrolinien völlig überlastet.", "在客流早晚高峰期，各条地铁主干线几乎处于极度超载饱和状态。")
        ]
    },

    # LESSON 13
    {
        "id": "B1_L13",
        "title": "第13课：情绪心理学、心理健康与压力管理 (Psychologie & Emotionen)",
        "summary": "掌握介词与关系代词搭配、情绪词汇表达与现代心理健康疏导核心词汇",
        "grammar": {
            "title": "介词与关系代词连用 (Relativsätze mit Präpositionen) 与介词副词",
            "sections": [
                {
                    "heading": "1. 关系从句中包含介词结构：介词置于关系代词之前，格由介词决定：",
                    "content": "• 指人：Das ist die Kollegin, mit der ich täglich spreche. (mit + Dat. -> der)\n• 指物：Das ist das Problem, über das alle diskutieren. (über + Akk. -> das)"
                },
                {
                    "heading": "2. 介词副词与不定代词连用：",
                    "content": "• Alles, worüber wir uns Sorgen machen, ist lösbar. (worüber = über + alles)\n• Das ist etwas, woran ich mich gern erinnere. (woran = an + etwas)"
                }
            ]
        },
        "quiz": [
            {
                "id": "B1_L13_Q1",
                "type": "GRAMMAR_FILL",
                "question": "Die Therapeutin, ______ (an die / mit der / auf die) er regelmäßig spricht, ist sehr kompetent.",
                "options": ["mit der", "an die", "für wen", "woran"],
                "correctIndex": 0,
                "explanation": "动词搭配为 sprechen mit (+Dat.)，先行词是阴性名词 die Therapeutin，故用 mit der。"
            },
            {
                "id": "B1_L13_Q2",
                "type": "MEANING_SELECT",
                "question": "“das Selbstwertgefühl” 的精准中文翻译是：",
                "options": ["自尊心，自我价值感", "虚荣心", "自私自利", "责任感"],
                "correctIndex": 0,
                "explanation": "das Selbstwertgefühl = 自我价值感、自尊感。"
            },
            {
                "id": "B1_L13_Q3",
                "type": "GRAMMAR_FILL",
                "question": "Gibt es etwas, ______ du dich besonders fürchtest?",
                "options": ["wovor", "über das", "an wen", "damit"],
                "correctIndex": 0,
                "explanation": "动词搭配为 sich fürchten vor (+Dat.)，指代不定代词 etwas 时，使用疑问介词复合代词 wovor。"
            },
            {
                "id": "B1_L13_Q4",
                "type": "LISTENING_MCQ",
                "question": "“Achtsamkeitsübungen helfen dabei, den Alltagsstress abzubauen.” 表达的核心内容是：",
                "options": ["正念冥想练习有助于化解日常压力。", "日常压力可以通过药物完全治愈。", "运动会导致身体过度疲倦。", "逃避问题能够改善心理健康。"],
                "correctIndex": 0,
                "explanation": "Achtsamkeitsübung = 正念练习，Stress abbauen = 疏导化解压力。"
            },
            {
                "id": "B1_L13_Q5",
                "type": "SENTENCE_BUILDER",
                "question": "重组规范语块：“seine Gefühle / offen / äußern / Er lernte”",
                "options": ["Er lernte, seine Gefühle offen zu äußern.", "Lernte er offen seine Gefühle zu äußern.", "Seine Gefühle zu äußern er lernte offen.", "Er lernte offen seine Gefühle äußern."],
                "correctIndex": 0,
                "explanation": "lernen 后接带 zu 不定式从句：Er lernte, seine Gefühle offen zu äußern。"
            }
        ],
        "words": [
            ("die Psyche", "die", "Nomen", "-n", "心理，心灵", "Körper und Psyche beeinflussen sich gegenseitig.", "生理与心理状态之间相互深刻影响。"),
            ("die Psychologie", "die", "Nomen", "unz.", "心理学", "Sie studiert klinische Psychologie an der Humboldt-Universität.", "她在柏林洪堡大学攻读临床心理学专业。"),
            ("der Psychologe", "der", "Nomen", "-n", "心理学家，心理咨询师（男）", "Der Psychologe half ihm, seine Prüfungsangst zu überwinden.", "心理咨询师帮助他成功克服了考试焦虑。"),
            ("die Therapeutin", "die", "Nomen", "-nen", "治疗师，心理咨询师（女）", "Die Therapeutin wendet moderne Verhaltenstherapie an.", "女治疗师采用了现代行为认知疗法。"),
            ("die Emotion", "die", "Nomen", "-en", "情绪，情感", "Musik kann intensive Emotionen in uns wecken.", "美妙的音乐能在我们心底唤起极其强烈的情感共鸣。"),
            ("das Gefühl", "das", "Nomen", "-e", "感觉，情感", "Ich habe das Gefühl, dass wir auf dem richtigen Weg sind.", "我有一种感觉，我们正走在完全正确的轨道上。"),
            ("die Stimmung", "die", "Nomen", "-en", "心情，情绪气氛", "Im Team herrscht eine überaus positive Stimmung.", "团队内部洋溢着极其乐观向上的良好氛围。"),
            ("die Freude", "die", "Nomen", "-n", "喜悦，快乐", "Seine Augen strahlten vor Freude über das Geschenk.", "收到礼物时，他的双眼闪烁着喜不自胜的光彩。"),
            ("die Begeisterung", "die", "Nomen", "unz.", "热情，狂热赞赏", "Das neue Projekt stieß auf große Begeisterung bei den Mitarbeitern.", "新项目在全体员工中引发了极大的热情支持。"),
            ("die Zufriedenheit", "die", "Nomen", "unz.", "满意度，知足", "Innere Zufriedenheit ist wichtiger als materieller Reichtum.", "内心的知足与安宁比物质财富更加弥足珍贵。"),
            ("die Gelassenheit", "die", "Nomen", "unz.", "从容，镇定沉着", "Mit Gelassenheit meistert man auch schwierige Krisensituationen.", "保持沉着从容的心态能让人从容应对严峻的危机情境。"),
            ("die Hoffnung", "die", "Nomen", "-en", "希望", "Wir dürfen die Hoffnung auf eine friedliche Zukunft nie aufgeben.", "我们绝不能放弃对和平未来的美好希望。"),
            ("die Zuversicht", "die", "Nomen", "unz.", "信心，乐观笃定", "Trotz der Rückschläge blickt sie mit Zuversicht nach vorn.", "尽管遭遇了波折，她依然信心满满地展望未来。"),
            ("das Mitgefühl", "das", "Nomen", "unz.", "同情心，同理心", "Sie drückte den Opfern ihr tiefes Mitgefühl aus.", "她向受害者表达了深切的同情与慰问。"),
            ("die Empathie", "die", "Nomen", "unz.", "共情能力，移情", "Empathie ist eine wesentliche soziale Schlüsselkompetenz.", "共情能力是一项至关重要的核心人际交往能力。"),
            ("die Trauer", "die", "Nomen", "unz.", "悲伤，哀悼", "Nach dem Verlust des Freundes war die Trauer groß.", "痛失挚友之后，内心的悲痛难以言表。"),
            ("der Kummer", "der", "Nomen", "unz.", "忧愁，苦恼", "Liebeskummer kann jungen Menschen sehr zusetzen.", "失恋的烦恼往往会给年轻人带来巨大的心理打击。"),
            ("die Wut", "die", "Nomen", "unz.", "愤怒，暴怒", "Vor lauter Wut schlug er mit der Faust auf den Schreibtisch.", "盛怒之下，他狠狠地用拳头砸向办公桌。"),
            ("der Zorn", "der", "Nomen", "unz.", "狂怒，义愤", "Gerechter Zorn trieb die Demonstranten auf die Straße.", "满腔义愤驱使示威抗议者勇敢地走上街头。"),
            ("die Angst", "die", "Nomen", "-e", "恐惧，害怕", "Man muss lernen, Ängste zu erkennen und zu bewältigen.", "人必须学会正视内心的恐惧并予以有效疏导克服。"),
            ("die Panik", "die", "Nomen", "unz.", "恐慌，惊慌失措", "Bei Feueralarm darf keine Panik ausbrechen.", "当火警拉响时，绝对不可发生混乱的恐慌拥挤。"),
            ("die Furcht", "die", "Nomen", "unz.", "畏惧，忧惧", "Furcht vor dem Scheitern hindert viele am beruflichen Erfolg.", "对失败的无端畏惧阻碍了许多人走向职业成功。"),
            ("die Einsamkeit", "die", "Nomen", "unz.", "孤独，孤单", "Einsamkeit im Alter ist eine gesellschaftliche Herausforderung.", "老年人的精神孤独已成为严峻的现代社会挑战。"),
            ("die Verzweiflung", "die", "Nomen", "unz.", "绝望", "In seiner tiefen Verzweiflung bat er Freunde um Beistand.", "在深切的绝望之中，他向挚友们发出了求助呼请。"),
            ("die Eifersucht", "die", "Nomen", "unz.", "嫉妒，醋意", "Unbegründete Eifersucht kann eine glückliche Beziehung zerstören.", "毫无根据的捕风捉影与嫉妒会彻底摧毁一段美满的感情。"),
            ("der Neid", "der", "Nomen", "unz.", "羡慕，嫉恨", "Neid auf den beruflichen Erfolg vergiftet das Betriebsklima.", "对同事职场晋升的嫉恨会严重毒化整个办公室氛围。"),
            ("die Scham", "die", "Nomen", "unz.", "羞耻感，惭愧", "Scham hinderte ihn daran, seinen gravierenden Fehler einzugestehen.", "强烈的羞耻心妨碍了他坦诚承认自己的严重过失。"),
            ("die Schuld", "die", "Nomen", "-en", "内疚，罪责", "Schuldgefühle belasten das menschliche Gewissen schwer.", "沉重的内疚感与负罪感会给人的良知带来沉重压迫。"),
            ("der Stress", "der", "Nomen", "unz.", "压力，应激反应", "Chronischer Stress schwächt auf Dauer das Immunsystem.", "长期的慢性心理压力最终会彻底削弱人体免疫系统。"),
            ("das Burnout", "das", "Nomen", "unz.", "职业倦怠，耗竭综合征", "Wegen Überarbeitung litt der Manager unter einem Burnout-Syndrom.", "由于长期严重超负荷运转，这位高管罹患了职业倦怠综合征。"),
            ("die Depression", "die", "Nomen", "-en", "抑郁，抑郁症", "Depressionen sind ernsthafte, aber gut behandelbare Krankheiten.", "抑郁症是严肃的疾病，但通过科学干预是可以被治愈的。"),
            ("die Krise", "die", "Nomen", "-n", "心理危机，危机", "Aus einer Lebenskrise kann man gestärkt hervorgehen.", "人完全可以从人生低谷危机中蜕变得更加坚韧成熟。"),
            ("die Belastung", "die", "Nomen", "-en", "负担，承受重压", "Psychische Belastung am Arbeitsplatz muss verringert werden.", "工作场所的心理重压必须通过制度性举措予以切实减轻。"),
            ("die Erschöpfung", "die", "Nomen", "unz.", "筋疲力尽，极度耗竭", "Nach den stressigen Prüfungen spürte er tiefe Erschöpfung.", "在漫长高压的考试结束后，他感到了深入骨髓的极度疲惫。"),
            ("die Entspannung", "die", "Nomen", "-en", "放松，舒缓", "Autogenes Training dient der gezielten körperlichen Entspannung.", "自律舒缓训练有助于实现针对性的躯体肌肉深度放松。"),
            ("die Erholung", "die", "Nomen", "unz.", "休养，休假恢复", "Am Wochenende brauche ich dringend Ruhe und Erholung.", "周末期间我迫切需要绝对的安静与身心调养。"),
            ("die Achtsamkeit", "die", "Nomen", "unz.", "正念，专注当下", "Achtsamkeit hilft, den gegenwärtigen Moment bewusst zu erleben.", "正念能够帮助人们清醒觉察并体验当下的每一瞬间。"),
            ("die Meditation", "die", "Nomen", "-en", "冥想，静坐", "Tägliche Meditation beruhigt das aufgewühlte Nervensystem.", "每日坚持冥想能有效安抚平息躁动不安的中枢神经系统。"),
            ("das Selbstvertrauen", "das", "Nomen", "unz.", "自信心", "Erfolge im Beruf stärken das persönliche Selbstvertrauen.", "职业生涯中取得的成绩能够显著强化个人的自信心。"),
            ("das Selbstwertgefühl", "das", "Nomen", "unz.", "自我价值感，自尊", "Ein gesundes Selbstwertgefühl schützt vor emotionaler Ausbeutung.", "健康的自我价值认同能有效防止个体在情感交往中被侵害。"),
            ("die Motivation", "die", "Nomen", "-en", "动机，动力", "Klare Zielsetzungen steigern die Lern- und Arbeitsmotivation.", "清晰的目标规划能够极大激发学习与工作的源动力。"),
            ("die Frustration", "die", "Nomen", "-en", "挫败感，沮丧", "Misserfolge führten anfangs zu großer Frustration.", "初期的连番失败一度带来了极大的挫败感。"),
            ("die Resilienz", "die", "Nomen", "unz.", "心理韧性，复原力", "Resilienz bezeichnet die Fähigkeit, Schicksalsschläge zu überwinden.", "心理韧性指的是个体克服重大命运打击与逆境复原的能力。"),
            ("das Wohlbefinden", "das", "Nomen", "unz.", "身心健康，幸福安康", "Sport und gesunde Ernährung fördern das allgemeine Wohlbefinden.", "规律运动与营养膳食能够全面促进身心健康与幸福感。"),
            ("die Balance", "die", "Nomen", "-n", "平衡，协调", "Eine ausgeglichene Work-Life-Balance beugt Krankheiten vor.", "协调良好的工作与生活平衡能够有效预防各种职业身心疾病。"),
            ("die Verhaltensweise", "die", "Nomen", "-n", "行为方式，举止习惯", "Durch Therapie kann man schädliche Verhaltensweisen ablegen.", "通过专业心理咨询干预，人们可以摒弃不良的行为模式。"),
            ("das Unterbewusstsein", "das", "Nomen", "unz.", "潜意识", "Viele Ängste sind tief im menschlichen Unterbewusstsein verankert.", "许多恐惧其实深深植根于人类潜意识的最底层。"),
            ("das Trauma", "das", "Nomen", "Traumen", "心理创伤，创伤", "Kriegskinder leiden oft noch Jahrzehnte später an schweren Traumen.", "战争经历者甚至在数十年之后依然深受严重创伤后应激困扰。"),
            ("die Beratung", "die", "Nomen", "-en", "咨询，指导", "Kostenlose psychologische Beratung steht Studenten jederzeit offen.", "免费的专业心理辅导向在校高校大学生全天候开放。"),
            ("die Bewältigung", "die", "Nomen", "unz.", "克服，应对化解", "Zur Bewältigung von Konflikten braucht man Geduld und Diplomatie.", "化解人际冲突需要足够的耐性以及高超的沟通协调智慧。"),
            ("beruhigen", "kein", "Verb", "beruhigte, beruhigt", "使平静，安抚 (sich)", "Tiefes Einatmen hilft dabei, die Nerven rasch zu beruhigen.", "深长呼吸有助于让人在短时间内迅速平息紧张的神经。"),
            ("überwinden", "kein", "Verb", "überwand, überwunden", "克服，战胜", "Gemeinsam können wir diese schwierige emotionale Phase überwinden.", "齐心协力之下我们完全能够跨越这段艰难的情感关卡。"),
            ("aufregen", "kein", "Verb", "regte auf, aufgeregt", "使激动，使生气 (sich)", "Reg dich bitte nicht über belanglose Kleinigkeiten auf!", "请千万不要为了微不足道的小事而大动肝火、气坏身体！"),
            ("abbauen", "kein", "Verb", "baute ab, abgebaut", "化解，消除，减少", "Ausdauersport ist ideal, um aufgestauten Stress abzubauen.", "有氧耐力运动是彻底化解疏导体内积聚压力的绝佳手段。"),
            ("verkraften", "kein", "Verb", "verkraftete, verkraftet", "承受，经受住", "Er konnte die bittere Niederlage nur sehr schwer verkraften.", "他极难承受住那场惨痛失败所带来的沉重打击。"),
            ("verarbeiten", "kein", "Verb", "verarbeitete, verarbeitet", "消化，心理加工处理", "Es braucht Zeit, um den schweren Schicksalsschlag zu verarbeiten.", "消化并走出如此重大的命运变故需要充足的时间。"),
            ("beeinflussen", "kein", "Verb", "beeinflusste, beeinflusst", "影响", "Schlafmangel beeinflusst unsere Konzentration negativ.", "长期睡眠不足会对我们的大脑专注力和认知表现造成负面影响。"),
            ("leiden", "kein", "Verb", "litt, gelitten", "受折磨，患病 (unter/an)", "Viele Arbeitnehmer leiden unter ständigem Zeit- und Termindruck.", "许多职场员工都在承受着永无休止的时间催赶与期限压迫。"),
            ("schätzen", "kein", "Verb", "schätzte, geschätzt", "看重，赏识，估量", "Ich schätze deine ehrliche Meinung und deine Loyalität sehr.", "我非常珍视你看待问题时的坦诚见解以及你的忠诚品格。"),
            ("empfinden", "kein", "Verb", "empfand, empfunden", "感到，觉察出", "Sie empfand tiefes Mitleid für das verletzte Tier.", "面对受伤的小动物，她心底涌起了深切的怜悯与同情。"),
            ("ausdrücken", "kein", "Verb", "drückte aus, ausgedrückt", "表达，表现 (sich)", "Er kann seine Gefühle in Worten nur schwer ausdrücken.", "他很难用准确的言辞来完整表达自己内心的复杂感受。"),
            ("klagen", "kein", "Verb", "klagte, geklagt", "抱怨，诉苦 (über)", "Der Patient klagt über Schlafstörungen und Kopfschmerzen.", "患者向医生主诉自己长期存在严重的失眠障碍与顽固偏头痛。"),
            ("optimistisch", "kein", "Adjektiv", "-", "乐观的", "Trotz aller Widrigkeiten bleibt sie stets optimistisch.", "尽管前路荆棘遍布，她依然始终保持着昂扬乐观的心态。"),
            ("pessimistisch", "kein", "Adjektiv", "-", "悲观的", "Eine zu pessimistische Haltung blockiert neue Chancen.", "过度消极悲观的心态会彻底扼杀迎接崭新机遇的可能。"),
            ("nervös", "kein", "Adjektiv", "-", "紧张不安的", "Vor der mündlichen B1-Prüfung war sie furchtbar nervös.", "在歌德B1口语考场门外，她曾紧张得心怦怦直跳。"),
            ("gelassen", "kein", "Adjektiv", "-", "从容镇定的", "Ein gelassener Geist trifft in Krisen die klügsten Entscheidungen.", "唯有保持处变不惊的从容心境，方能在危局中做出最明智抉择。"),
            ("ängstlich", "kein", "Adjektiv", "-", "胆怯的，焦虑不安的", "Das Kind klammerte sich ängstlich an die Hand der Mutter.", "受到惊吓的孩子满脸胆怯地死死拉住妈妈的手不肯松开。"),
            ("einfühlsam", "kein", "Adjektiv", "-", "善解人意的，富于同理心的", "Die Ärztin führte ein sehr einfühlsames Beratungsgespräch.", "女医生以极其善解人意的方式开展了深度心理沟通咨询。"),
            ("belastbar", "kein", "Adjektiv", "-", "抗压能力强的", "In Führungsberufen muss man psychisch enorm belastbar sein.", "在各类企业高管岗位上，必须具备极其强大的抗压心理素质。"),
            ("erschöpft", "kein", "Adjektiv", "-", "精疲力竭的", "Nach dem langen Arbeitstag fiel er völlig erschöpft ins Bett.", "结束了整整一天繁重的工作，他筋疲力竭地倒头栽倒在床上。")
        ]
    },

    # LESSON 14
    {
        "id": "B1_L14",
        "title": "第14课：德语区近现代历史、政经格局与国情 (Geschichte & Politik)",
        "summary": "掌握第一虚拟式 (Konjunktiv I) 与间接引语基础、联邦德国政治体制与欧洲一体化核心词汇",
        "grammar": {
            "title": "间接引语与第一虚拟式 (Indirekte Rede & Konjunktiv I)",
            "sections": [
                {
                    "heading": "1. 间接引语 (Indirekte Rede)：转述他人话语，体现新闻客观性：",
                    "content": "• 动词词干 + 虚拟式词尾 (-e, -est, -e, -en, -et, -en)\n• sein 特殊变位：ich sei, du seiest, er sei, wir seien, ihr seiet, sie seien。\n• 例句：Der Bundeskanzler erklärte, die Regierung sei zu Reformen bereit. (总理声明政府已做好改革准备。)"
                },
                {
                    "heading": "2. 第一虚拟式与现在时同形时代替方案：",
                    "content": "• 若第一虚拟式与现在时直陈式完全一致（如 wir haben, sie sagen），必须用第二虚拟式 (hätten, sagten / würden sagen) 代替以示区分。"
                }
            ]
        },
        "quiz": [
            {
                "id": "B1_L14_Q1",
                "type": "GRAMMAR_FILL",
                "question": "Die Ministerin sagte in der Tagesschau, das Gesetz ______ (sein) ein Meilenstein.",
                "options": ["sei", "ist", "wäre", "seien"],
                "correctIndex": 0,
                "explanation": "新闻间接引语第三人称单数使用第一虚拟式：er/sie/es sei。"
            },
            {
                "id": "B1_L14_Q2",
                "type": "MEANING_SELECT",
                "question": "“der Bundesrat” 在德国宪政体制中的确切法律定位是：",
                "options": ["联邦参议院（代表16个联邦州）", "联邦众议院", "联邦宪法法院", "联邦审计署"],
                "correctIndex": 0,
                "explanation": "der Bundesrat 代表十六个联邦州利益，参与联邦立法审查与表决。"
            },
            {
                "id": "B1_L14_Q3",
                "type": "GRAMMAR_FILL",
                "question": "Die Sprecherin teilte mit, die Verhandlungen ______ (haben) begonnen.",
                "options": ["hätten", "haben", "habe", "hat"],
                "correctIndex": 0,
                "explanation": "复数第三人称 haben 与直陈式同形，根据语法规则改用第二虚拟式 hätten 代替。"
            },
            {
                "id": "B1_L14_Q4",
                "type": "LISTENING_MCQ",
                "question": "“Der Mauerfall am 9. November 1989 markierte das Ende des Kalten Krieges.” 的核心主旨是：",
                "options": ["1989年11月9日柏林墙倒塌标志着冷战时代的终结。", "柏林墙建于1989年冬季。", "冷战在1989年正式爆发。", "两德统一条约于1989年被废止。"],
                "correctIndex": 0,
                "explanation": "Mauerfall = 柏林墙倒塌，markierte das Ende = 标志着终结。"
            },
            {
                "id": "B1_L14_Q5",
                "type": "SENTENCE_BUILDER",
                "question": "重组新闻陈述句：“trat / am 3. Oktober 1990 / in Kraft / Die deutsche Wiedervereinigung”",
                "options": ["Die deutsche Wiedervereinigung trat am 3. Oktober 1990 in Kraft.", "Am 3. Oktober 1990 die deutsche Wiedervereinigung trat in Kraft.", "Die deutsche Wiedervereinigung am 3. Oktober 1990 trat in Kraft.", "In Kraft trat die deutsche Wiedervereinigung am 3. Oktober 1990."],
                "correctIndex": 0,
                "explanation": "固定词组 in Kraft treten (生效实施)，动词在陈述句居第二位。"
            }
        ],
        "words": [
            ("die Geschichte", "die", "Nomen", "-n", "历史，故事", "Die deutsche Geschichte des 20. Jahrhunderts war ereignisreich.", "20世纪的德国历史风云变幻、波澜起伏。"),
            ("die Politik", "die", "Nomen", "unz.", "政治，方针政策", "Er interessiert sich brennend für europäische Außenpolitik.", "他对欧洲对外外交事务与地缘战略抱有极其浓厚的兴趣。"),
            ("der Staat", "der", "Nomen", "-en", "国家", "Die Bundesrepublik Deutschland ist ein demokratischer Bundesstaat.", "德意志联邦共和国是一个实行民主制度的联邦制国家。"),
            ("die Verfassung", "die", "Nomen", "-en", "宪法", "Das Grundgesetz ist die Verfassung der Bundesrepublik Deutschland.", "《基本法》是德意志联邦共和国的现行根本大法。"),
            ("das Grundgesetz", "das", "Nomen", "-e", "基本法（德国宪法）", "Artikel 1 des Grundgesetzes besagt: Die Würde des Menschen ist unantastbar.", "德国基本法第一条庄严宣告：人的尊严神圣不可侵犯。"),
            ("die Demokratie", "die", "Nomen", "-n", "民主制度", "Freie Wahlen sind das unverzichtbare Fundament jeder Demokratie.", "自由平等的普选投票是任何现代宪政民主体制的立身之本。"),
            ("die Republik", "die", "Nomen", "-en", "共和国", "Deutschland ist seit 1919 eine parlamentarische Republik.", "德国自1919年魏玛宪法以来即确立为议会制共和国。"),
            ("der Bundestag", "der", "Nomen", "unz.", "联邦议院（德国下议院）", "Der Deutsche Bundestag tagt im historischen Reichstagsgebäude.", "德意志联邦议院在著名的历史建筑帝国国会大厦内召开大会。"),
            ("der Bundesrat", "der", "Nomen", "unz.", "联邦参议院（代表各州）", "Der Bundesrat vertritt die Interessen der 16 deutschen Bundesländer.", "联邦参议院代表德国16个联邦州的最高地方利益。"),
            ("die Regierung", "die", "Nomen", "-en", "政府", "Die Regierung plant umfangreiche Reformen im Bildungssystem.", "联邦内阁政府正在紧锣密鼓地制定全面的教育体制改革方案。"),
            ("das Parlament", "das", "Nomen", "-e", "议会，国会", "Das Parlament verabschiedete das neue Haushaltsgesetz.", "议会正式审议并通过了全新的国家年度财政预算案。"),
            ("der Abgeordnete", "der", "Nomen", "-n", "议会议员", "Die Abgeordneten debattierten kontrovers über den Gesetzentwurf.", "议员们在辩论大厅就该法案草案展开了激烈交锋。"),
            ("der Bundeskanzler", "der", "Nomen", "-", "联邦总理", "Der Bundeskanzler leitet die Regierungsgeschäfte.", "联邦总理总揽国家行政权力并领导政府内阁运作。"),
            ("der Bundespräsident", "der", "Nomen", "-en", "联邦总统（国家元首）", "Der Bundespräsident vertritt Deutschland völkerrechtlich.", "联邦总统作为国家元首在国际法层面上代表德国行使主权。"),
            ("das Ministerium", "das", "Nomen", "Ministerien", "部，政府各部委", "Das Bundesministerium der Finanzen hat seinen Sitz in Berlin.", "联邦财政部本部设在首都柏林。"),
            ("die Partei", "die", "Nomen", "-en", "政党", "In Deutschland gibt es ein vielfältiges Mehrparteiensystem.", "德国实行高度多元竞争与协同执政的多党联合组阁制度。"),
            ("die Koalition", "die", "Nomen", "-en", "执政联盟", "Nach der Wahl bildeten drei Parteien eine gemeinsame Koalition.", "大选尘埃落定之后，三个政党达成一致组成了联合执政联盟。"),
            ("die Opposition", "die", "Nomen", "-en", "在野党，反对派", "Die parlamentarische Opposition kontrolliert das Handeln der Regierung.", "议会内部的在野反对党对执政内阁的行为实施严格民主监督。"),
            ("die Wahl", "die", "Nomen", "-en", "选举，大选", "Alle vier Jahre finden die Wahlen zum Deutschen Bundestag statt.", "德国联邦议院全国大选每隔四年举行一次。"),
            ("der Wähler", "der", "Nomen", "-", "选民", "Millionen Wähler gaben am Sonntag ihre Stimme im Wahllokal ab.", "数以百万计的合法选民在周日前往各个投票站投下了神圣的一票。"),
            ("die Stimme", "die", "Nomen", "-n", "选票，嗓音", "Jeder wahlberechtigte Bürger verfügt über Erst- und Zweitstimme.", "每位拥有投票权的德国公民在大选中同时享有第一与第二选票。"),
            ("das Gesetz", "das", "Nomen", "-e", "法律，法案", "Niemand steht über dem Gesetz; alle sind vor dem Gesetz gleich.", "任何人都无权凌驾于法律之上；法律面前人人一律平等。"),
            ("die Reform", "die", "Nomen", "-en", "改革", "Wirtschaftliche Reformen sollen den Arbeitsmarkt zukunftsfest machen.", "经济结构的深度改革旨在让劳动力就业市场更能应对未来风险。"),
            ("das Recht", "das", "Nomen", "-e", "权利，法权", "Das Recht auf freie Meinungsäußerung ist ein hohes Gut.", "公民依法享有的言论自由权利是不可剥夺的崇高法益。"),
            ("die Pflicht", "die", "Nomen", "-en", "义务，职责", "Jeder Staatsbürger hat Rechte und verfassungsrechtliche Pflichten.", "每一位合法国家公民在享有权利的同时亦须恪守宪政义务。"),
            ("das Gericht", "das", "Nomen", "-e", "法院，法庭", "Das Bundesverfassungsgericht wacht über die Einhaltung des Grundgesetzes.", "联邦宪法法院在卡尔斯鲁厄负责捍卫并监督基本法的全面践行。"),
            ("der Bürger", "der", "Nomen", "-", "公民，市民", "Aktive Bürger engagieren sich in Vereinen und Bürgerinitiativen.", "热心公益的公民积极投身于各类民间社团组织与公民倡议行动。"),
            ("die Wiedervereinigung", "die", "Nomen", "unz.", "国家统一，两德统一", "Die deutsche Wiedervereinigung vollzog sich friedlich im Jahr 1990.", "两德统一大业在1990年以完全和平的历史方式宣告圆满达成。"),
            ("die Mauer", "die", "Nomen", "-n", "墙，柏林墙", "Der Fall der Berliner Mauer veränderte die politische Weltkarte.", "柏林墙的轰然倒塌彻底改写了世界地缘政治版图格局。"),
            ("die Grenze", "die", "Nomen", "-n", "边界，边境", "Im Schengen-Raum sind die Binnengrenzen frei passierbar.", "在申根框架协定区内，成员国内部国界边境均可完全自由通行。"),
            ("die Teilung", "die", "Nomen", "-en", "分裂，割裂", "Die jahrzehntelange Teilung Deutschlands hinterließ tiefe Spuren.", "德国长达数十年之久的分裂与对峙留下了难以磨灭的时代印记。"),
            ("der Weltkrieg", "der", "Nomen", "-e", "世界大战", "Die verheerenden Folgen des Zweiten Weltkrieges mahnen zum Frieden.", "第二次世界大战带来的毁灭性浩劫永远警醒着世人必须捍卫和平。"),
            ("der Frieden", "der", "Nomen", "unz.", "和平", "Europas Einigung sicherte dem Kontinent Jahrzehnte des Friedens.", "欧洲一体化进程为整个欧罗巴大陆奠定了数十年的持久和平基石。"),
            ("der Krieg", "der", "Nomen", "-e", "战争", "Diplomaten versuchen mit allen Mitteln, einen Krieg abzuwenden.", "外交使节正竭尽一切政治手段与谈判渠道试图阻止战争的爆发。"),
            ("der Vertrag", "der", "Nomen", "-e", "条约，合同", "Die Unterzeichnung des Staatsvertrages war ein historischer Akt.", "国家间双边条约的正式签字仪式是一项载入史册的壮举。"),
            ("das Bündnis", "das", "Nomen", "-se", "盟约，同盟", "Die NATO ist ein politisch-militärisches Verteidigungsbündnis.", "北大西洋公约组织是一个政治兼军事性质的多边集体防御同盟。"),
            ("die Europäische Union", "die", "Eigenname", "unz.", "欧洲联盟", "Die Europäische Union umfasst mittlerweile 27 Mitgliedstaaten.", "欧洲联盟迄今已发展壮大为涵盖27个主权成员国的庞大共同体。"),
            ("das Abkommen", "das", "Nomen", "-", "协定，协议", "Das Pariser Klimaabkommen verpflichtet Staaten zur CO2-Minderung.", "《巴黎气候协定》对世界各主权国家规定了严格的减排法定义务。"),
            ("die Verhandlung", "die", "Nomen", "-en", "谈判，磋商", "Nach zähen Verhandlungen erzielten beide Seiten einen Kompromiss.", "经过多轮极其艰苦拉锯的谈判，双方最终达成了妥协方案。"),
            ("der Kompromiss", "der", "Nomen", "-e", "妥协，折中方案", "Ein tragfähiger Kompromiss ist das Markenzeichen der Demokratie.", "达成经得起推敲的各方妥协方案正是现代民主政治运作的鲜明特征。"),
            ("der Konflikt", "der", "Nomen", "-e", "冲突，争端", "Internationale Konflikte müssen auf friedlichem Wege gelöst werden.", "一切错综复杂的国际争端都必须依据联合国宪章以和平途径化解。"),
            ("die Krise", "die", "Nomen", "-n", "政治危机，经济危机", "Die Finanzkrise erforderte entschlossenes Handeln der Notenbanken.", "全球金融风暴的肆虐迫使各大国央行采取了雷厉风行的救市举措。"),
            ("der Fortschritt", "der", "Nomen", "-e", "进步，发展", "Wissenschaftlicher Fortschritt muss immer dem Wohle der Menschheit dienen.", "自然科学探索的一切重大进步都应当造福于全人类的共同福祉。"),
            ("die Epoche", "die", "Nomen", "-n", "时代，纪元", "Das Zeitalter der Aufklärung war eine prägende europäische Epoche.", "启蒙运动时代是深深塑造了欧洲近代人文思想脉络的划时代纪元。"),
            ("das Denkmal", "das", "Nomen", "-er", "纪念碑", "In Berlin erinnert das Holocaust-Mahnmal an die ermordeten Juden.", "坐落于柏林市中心的大屠杀纪念群雕永远警示世人铭记被杀害的同胞。"),
            ("die Demonstration", "die", "Nomen", "-en", "示威，游行", "Tausende Menschen nahmen an der friedlichen Friedensdemonstration teil.", "数以万计的民众走上街头参加了声势浩大的反战和平游行。"),
            ("der Protest", "der", "Nomen", "-e", "抗议", "Bürger äußerten lautstarken Protest gegen das geplante Großprojekt.", "广大市民对该规划中的巨型市政项目表达了强烈而公开的抗议。"),
            ("das Bürgerrecht", "das", "Nomen", "-e", "公民权利", "Bürgerrechte dürfen auch in Notzeiten nicht willkürlich beschnitten werden.", "即便处于紧急危机状态，宪法赋予的公民基本权利亦不可被任意剥夺。"),
            ("die Solidarität", "die", "Nomen", "unz.", "团结一致，守望相助", "Internationale Solidarität rettet Menschenleben in Katastrophen.", "当特大自然灾害来临时，国际人道主义的守望相助能拯救无数生命。"),
            ("die Gerechtigkeit", "die", "Nomen", "unz.", "正义，社会公平", "Soziale Gerechtigkeit ist die Voraussetzung für dauerhaften inneren Frieden.", "促进社会分配公平与正义是维护国家长治久安与社会和谐的前提。"),
            ("regieren", "kein", "Verb", "regierte, regiert", "执政，统治", "Die neu gewählte Koalition regiert mit einer stabilen Parlamentsmehrheit.", "新当选的执政联盟凭借在联邦议院中拥有的稳定多数席位行使执政权。"),
            ("wählen", "kein", "Verb", "wählte, gewählt", "投票选举，推选", "Die Bürger wählen ihre Volksvertreter in allgemeiner und freier Wahl.", "广大公民依照普遍、平等、直接、自由的原则依法行使投票推选权。"),
            ("abstimmen", "kein", "Verb", "stimmte ab, abgestimmt", "表决，投票 (über)", "Die Abgeordneten stimmen heute über das umstrittene Rentenpaket ab.", "全体议员于今天下午就备受舆论瞩目的养老金揽子改革法案进行逐项表决。"),
            ("beschließen", "kein", "Verb", "beschloss, beschlossen", "决议，决定", "Das Kabinett beschloss weitreichende Maßnahmen zur Wirtschaftsförderung.", "联邦内阁审议决定了一系列影响深远的促经济稳增长一揽子举措。"),
            ("einführen", "kein", "Verb", "führte ein, eingeführt", "推行，出台", "Die EU plant, ein einheitliches digitales Bezahlsystem einzuführen.", "欧盟正拟定路线图，计划在成员国全境推行统一规范的数字支付体系。"),
            ("abschaffen", "kein", "Verb", "schaffte ab, abgeschafft", "废除，取缔", "Vor vielen Jahren wurde die Visumpflicht zwischen den Nachbarländern abgeschafft.", "早在数年之前，邻国之间繁琐的人员往来出入境签证要求便已被依法废止。"),
            ("unterzeichnen", "kein", "Verb", "unterzeichnete, unterzeichnet", "签署，签字", "Die Staatschefs unterzeichneten das bilaterale Handelsabkommen feierlich.", "两国国家元首在首脑峰会上庄重签署了双边自由贸易与投资战略协定。"),
            ("demonstrieren", "kein", "Verb", "demonstrierte, demonstriert", "游行示威", "Umweltaktivisten demonstrieren vor dem Tagungszentrum gegen Kohleverstromung.", "环保行动主义者在峰会会议中心大门前举行示威反对燃煤火电项目。"),
            ("vertreten", "kein", "Verb", "vertrat, vertreten", "代表，维护", "Der Botschafter vertritt die diplomatischen Interessen seines Heimatlandes.", "特命全权大使在派驻国坚决维护并代表其祖国的崇高外交利益与尊严。"),
            ("verhandeln", "kein", "Verb", "verhandelte, verhandelt", "协商谈判 (über)", "Die Gewerkschaft verhandelt mit den Arbeitgebern über höhere Löhne.", "工会正就提高基层产业工人最低薪酬待遇与资方雇主展开艰苦博弈磋商。"),
            ("demokratisch", "kein", "Adjektiv", "-", "民主的", "Deutschland ist ein demokratischer und sozialer Bundesstaat.", "德国是一个建立在宪政法治与社会福利原则之上的民主联邦制国家。"),
            ("politisch", "kein", "Adjektiv", "-", "政治的", "Er analysiert die politischen Entwicklungen in Osteuropa messerscharf.", "他对整个东欧地区的最新政治局势走向与地缘裂变进行了入木三分的剖析。"),
            ("historisch", "kein", "Adjektiv", "-", "历史性的，具有历史意义的", "Der Fall der Berliner Mauer war ein historisches Jahrhundertereignis.", "柏林墙的轰然倒塌是一项具有划时代里程碑意义的历史性世纪事件。"),
            ("öffentlich", "kein", "Adjektiv", "-", "公共的，公开的", "Die Ministerin stellte den Gesetzentwurf auf einer öffentlichen Pressekonferenz vor.", "部长在面向中外媒体的公开新闻发布会上详细通报了该项立法草案。"),
            ("staatlich", "kein", "Adjektiv", "-", "国家的，公立的", "Universitäten in Deutschland werden zum Großteil durch staatliche Mittel finanziert.", "德国绝大多数高等公立大学的办学运转均由国家公共财政予以全额资助。"),
            ("sozial", "kein", "Adjektiv", "-", "社会的，社会福利的", "Die soziale Marktwirtschaft verbindet freies Unternehmertum mit Sozialschutz.", "社会市场经济模式将企业自由竞争活力与全方位的社会兜底保障完美结合。"),
            ("neutral", "kein", "Adjektiv", "-", "中立的", "Die Schweiz verfolgt in der Außenpolitik eine traditionell neutrale Linie.", "瑞士在其百年对外国际交往中始终奉行坚守传统的中立国外交国策。"),
            ("unabhängig", "kein", "Adjektiv", "-", "独立的，司法独立的", "Richter sind in ihren Urteilen unabhängig und nur dem Gesetz unterworfen.", "全体法官在行使司法独立裁量时不受任何干预，唯一遵循的准绳便是法律。"),
            ("solidarisch", "kein", "Adjektiv", "-", "团结一致的", "In Notlagen stehen die europäischen Nachbarn solidarisch zusammen.", "每当遭遇重大外部危机挑战，欧洲各邻邦均能休戚与共、携手团结共克时艰。"),
            ("fortschrittlich", "kein", "Adjektiv", "-", "进步的，开明的", "Die Gesellschaft vertritt in vielen Fragen fortschrittliche und liberale Werte.", "当代社会在对待诸多前沿价值议题时普遍秉持极为包容进步与开明的观念。")
        ]
    },

    # LESSON 15
    {
        "id": "B1_L15",
        "title": "第15课：歌德 B1 综合应试冲刺与高分通关 (Goethe B1 Prüfungstraining)",
        "summary": "掌握动名词搭配 (Funktionsverbgefüge)、高分论证连接词与歌德B1听说读写通关大纲核心词汇",
        "grammar": {
            "title": "功能动词短语 (Funktionsverbgefüge) 与学术论证逻辑连接词",
            "sections": [
                {
                    "heading": "1. 歌德 B1 写作与口语高级得分利器——功能动词搭配：",
                    "content": "• eine Entscheidung treffen (= sich entscheiden): 做出决定\n• zur Verfügung stehen (= verfügbar sein): 可供使用\n• in Frage kommen (= möglich sein): 列入考虑，可能\n• zur Sprache bringen (= ansprechen): 提出讨论\n• Rücksicht nehmen auf (+Akk.) (= berücksichtigen): 顾及，体谅"
                },
                {
                    "heading": "2. 口语与写作中表达观点与论证的逻辑连接词：",
                    "content": "• Meiner Auffassung nach... (依我之见……，动词放第三位)\n• Einerseits ..., andererseits ... (一方面……，另一方面……)\n• Nicht nur ..., sondern auch ... (不仅……而且……)\n• Aus diesem Grund... (基于这一原因……)"
                }
            ]
        },
        "quiz": [
            {
                "id": "B1_L15_Q1",
                "type": "GRAMMAR_FILL",
                "question": "Dieses Angebot kommt für mich leider überhaupt nicht ______ Frage.",
                "options": ["in", "an", "zur", "unter"],
                "correctIndex": 0,
                "explanation": "固定功能动词搭配：in Frage kommen (列入考虑范围/可行)。"
            },
            {
                "id": "B1_L15_Q2",
                "type": "MEANING_SELECT",
                "question": "歌德口语高级表达 “eine Entscheidung treffen” 的标准近义动词是：",
                "options": ["sich entscheiden", "entschuldigen", "sich erkundigen", "erklären"],
                "correctIndex": 0,
                "explanation": "eine Entscheidung treffen = sich entscheiden (做出抉择/做出决议)。"
            },
            {
                "id": "B1_L15_Q3",
                "type": "GRAMMAR_FILL",
                "question": "Für weitere Fragen ______ ich Ihnen gern zur Verfügung.",
                "options": ["stehe", "gebe", "habe", "bringe"],
                "correctIndex": 0,
                "explanation": "固定功能动词搭配：jemandem zur Verfügung stehen (随时效劳/供某人调遣使用)。"
            },
            {
                "id": "B1_L15_Q4",
                "type": "LISTENING_MCQ",
                "question": "“Einerseits ist das Projekt kostspielig, andererseits sichert es Arbeitsplätze.” 的论证逻辑是：",
                "options": ["一方面项目耗资巨大，但另一方面它切实保障了就业岗位。", "项目因缺乏资金已被迫取消。", "只有削减岗位才能节约项目开支。", "所有各方一致反对该项目。"],
                "correctIndex": 0,
                "explanation": "Einerseits ..., andererseits ... 表示“一方面……，另一方面……”的双向辩证论证逻辑。"
            },
            {
                "id": "B1_L15_Q5",
                "type": "SENTENCE_BUILDER",
                "question": "重组歌德B1口语陈述观点句：“bin ich / Meiner festen Überzeugung / für diesen Vorschlag / nach”",
                "options": ["Meiner festen Überzeugung nach bin ich für diesen Vorschlag.", "Ich bin nach meiner festen Überzeugung für diesen Vorschlag.", "Für diesen Vorschlag meiner festen Überzeugung bin ich nach.", "Meiner festen Überzeugung nach für diesen Vorschlag ich bin."],
                "correctIndex": 0,
                "explanation": "常用口语开头：Meiner festen Überzeugung nach + 动词(bin) + 主语(ich) + 补足语。"
            }
        ],
        "words": [
            ("das Zertifikat", "das", "Nomen", "-e", "证书，凭证", "Das Goethe-Zertifikat B1 bescheinigt solide Deutschkenntnisse.", "歌德B1等级证书官方认证持有人具备扎实健全的德语交际运用能力。"),
            ("die Prüfung", "die", "Nomen", "-en", "考试，测试", "Die B1-Prüfung gliedert sich in die vier Module Lesen, Hören, Schreiben und Sprechen.", "歌德B1全国统考严密划分为阅读、听力、写作与口语四大核心模块。"),
            ("das Modul", "das", "Nomen", "-e", "模块，测试单元", "Alle vier Module können gemeinsam oder einzeln abgelegt werden.", "全部四个应试模块既支持一次性联合报考，亦可按需分拆单独应试。"),
            ("der Prüfling", "der", "Nomen", "-e", "应试考生", "Der Prüfling beantwortete alle Fragen des Prüfers souverän.", "这位考生在面对考官的所有追问时均给出了游刃有余的精彩应答。"),
            ("der Prüfer", "der", "Nomen", "-", "考官", "Die Prüfer bewerten Ausdrucksvermögen, Flüssigkeit und Grammatik.", "考官从语言词汇表达丰富度、流利连贯性以及语法规范度等多维度综合赋分。"),
            ("das Leseverstehen", "das", "Nomen", "unz.", "阅读理解", "Im Modul Leseverstehen muss man Texte zügig erfassen.", "在阅读理解模块中，考生必须在限定时间内迅捷抓住各语篇的核心脉络。"),
            ("das Hörverstehen", "das", "Nomen", "unz.", "听力理解", "Im Hörverstehen hören die Kandidaten Dialoge und Radiobeiträge.", "在听力理解环节，考生将听到贴近德国真实生活的多场景对话与广播节目。"),
            ("der schriftliche Ausdruck", "der", "Nomen", "unz.", "书面表达，写作", "Der schriftliche Ausdruck erfordert einen klaren logischen Aufbau.", "书面表达写作测试特别看重段落之间条理分明的逻辑层层递进与衔接。"),
            ("der mündliche Ausdruck", "der", "Nomen", "unz.", "口头表达，口语", "Im mündlichen Ausdruck hält man einen kurzen Vortrag.", "在口语测试中，考生须依据给定议题进行即兴短篇专题学术陈述。"),
            ("die Präsentation", "die", "Nomen", "-en", "演示报告，口语展示", "Die Präsentation sollte eine prägnante Einleitung und ein Fazit haben.", "口语展示必须具备短小精悍的开头导入以及画龙点睛的总结陈词。"),
            ("die Einleitung", "die", "Nomen", "-en", "导言，引言", "In der Einleitung nennt man das Thema und den eigenen Standpunkt.", "在开头引言部分应当明确开门见山点出本次演讲的主题与个人基本立场。"),
            ("der Hauptteil", "der", "Nomen", "-e", "主体段落，正文部分", "Im Hauptteil führt man Argumente und anschauliche Beispiele an.", "在正文主体段落中应深入列举多维度的论据以及生动翔实的生活实例。"),
            ("der Schluss", "der", "Nomen", "-e", "结尾，结论", "Zum Schluss bedankt man sich herzlich bei den Zuhörern.", "在演讲步入尾声之际，应当礼貌得体地向全场聆听的听众致以诚挚谢意。"),
            ("das Argument", "das", "Nomen", "-e", "论据，论辩理由", "Dieses überzeugende Argument lässt sich kaum widerlegen.", "这个极其过硬且极具说服力的论据几乎令人无法提出任何有效反驳。"),
            ("der Standpunkt", "der", "Nomen", "-e", "立场，视点", "Aus meinem Standpunkt überwiegen die praktischen Vorteile.", "从我的立场审视出发，此项方案所展现出的实际优势显而易见占据压倒性上风。"),
            ("die Meinung", "die", "Nomen", "-en", "看法，见解", "Zu diesem kontroversen Thema gehen die Meinungen stark auseinander.", "围绕这一充满争议的话题，社会各界人士的看法见解存在着巨大的分歧。"),
            ("die Ansicht", "die", "Nomen", "-en", "观点", "Ich bin der Ansicht, dass man den Umweltschutz priorisieren muss.", "我始终持有明确观点，即全社会应当将环境保护置于首要优先级位置。"),
            ("die Auffassung", "die", "Nomen", "-en", "认识，观点", "Nach meiner Auffassung bietet die Digitalisierung gewaltige Chancen.", "依我之见，全方位的数字化转型为当代年轻一代提供了无限的发展契机。"),
            ("das Fazit", "das", "Nomen", "-s", "结语，总论", "Als Fazit lässt sich festhalten, dass Bildung der Schlüssel zur Zukunft ist.", "作为最终的归纳总结我们可以得出定论：教育是通向未来之门的金钥匙。"),
            ("der Vorteil", "der", "Nomen", "-e", "优势，长处", "Ein großer Vorteil des Deutschlandtickets ist die unbegrenzte Mobilität.", "德国通票最引人注目的巨大优势便在于它所赋予的长距离无拘束出行自由。"),
            ("der Nachteil", "der", "Nomen", "-e", "弊端，劣势", "Der größte Nachteil dieses Plans sind die enormen finanziellen Kosten.", "这项宏伟工程目前最致命的弊端便在于前期所需投入的资金成本过于庞大。"),
            ("der Kompromiss", "der", "Nomen", "-e", "折中妥协方案", "Im Prüfungsgespräch müssen beide Partner einen tragfähigen Kompromiss finden.", "在口语搭档双人讨论环节，两位考生必须通过商讨达成一项务实的折中方案。"),
            ("die Vereinbarung", "die", "Nomen", "-en", "约定，协议", "Wir trafen eine feste Vereinbarung über die gemeinsame Vorbereitung.", "我们围绕接下来的联合模拟应试备考工作达成了条理明晰的协作约定。"),
            ("der Vorschlag", "der", "Nomen", "-e", "提议，建议", "Darf ich Ihnen zu diesem Plan einen konstruktiven Vorschlag unterbreiten?", "请允许我针对该项实施方案向您谨提出一条极具建设性的改进建议好吗？"),
            ("der Widerspruch", "der", "Nomen", "-e", "矛盾，异议", "Zwischen Theorie und beruflicher Praxis besteht oft ein spürbarer Widerspruch.", "在书本理论推演与错综复杂的职场实务操作之间往往横亘着显著的矛盾。"),
            ("der Zweifel", "der", "Nomen", "-", "怀疑，困惑", "An der Richtigkeit dieser amtlichen Statistik gibt es berechtigte Zweifel.", "针对官方所公布的这组统计数据的真实严谨性，公众提出了合情合理的质疑。"),
            ("die Begründung", "die", "Nomen", "-en", "阐释理由，论据", "Ihre Begründung klang für alle Anwesenden vollkommen schlüssig.", "她所给出的深层理由阐释在全场所有与会者听来都显得逻辑无懈可击。"),
            ("die Zusammenfassung", "die", "Nomen", "-en", "摘要，概述", "Geben Sie bitte eine kurze Zusammenfassung des soeben gehörten Textes!", "请您对刚才这段听力语篇的核心主旨大意做一份凝练简明的话语概括！"),
            ("die Struktur", "die", "Nomen", "-en", "结构，脉络", "Ein strukturierter Aufsatz erleichtert dem Leser das Textverständnis.", "结构清晰、条理井然的议论文写作能够极大降低读者的理解与认知负荷。"),
            ("der rote Faden", "der", "Nomen", "unz.", "主线，红线", "Ein roter Faden zog sich durch ihren gesamten Vortrag.", "一条贯穿始终的清晰思维主线严丝合缝地支撑起了她整场演讲的严密框架。"),
            ("der Wortschatz", "der", "Nomen", "-e", "词汇，词汇量", "Ein differenzierter Wortschatz ist die Eintrittskarte zur B1-Bestnote.", "掌握丰富精炼的差异化高阶词汇正是斩获歌德B1优异高分的坚实入场券。"),
            ("die Redemittel", "die", "Nomen (Pl.)", "Pl.", "固定表达语块，句式", "Prägen Sie sich feste Redemittel für Diskussionen gut ein!", "请大家务必将这些口语辩论高频高分固定句式与表达语块熟记于心！"),
            ("die Formulierung", "die", "Nomen", "-en", "措辞，行文表达", "Achten Sie beim Schreiben auf höfliche und präzise Formulierungen!", "在撰写各类正式德语文书信件时请务必留心使用得体有礼且精准规范的措辞！"),
            ("der Rechtschreibfehler", "der", "Nomen", "-", "拼写错误", "Korrigieren Sie den Brief sorgfältig, um Rechtschreibfehler zu vermeiden!", "请务必一丝不苟地复核校对书信，以彻底规避任何低级的正字法拼写硬伤！"),
            ("die Grammatik", "die", "Nomen", "-en", "语法体系", "Solide Kenntnisse der deutschen Grammatik geben beim Sprechen Sicherheit.", "扎实过硬的德语语法功底能够在临场即兴开口表达时赋予你无限的底气。"),
            ("das Zeitmanagement", "das", "Nomen", "unz.", "时间管理能力", "Gutes Zeitmanagement ist in der schriftlichen Prüfung die halbe Miete.", "在书面笔试考场上，科学严谨的答题答卷时间管控策略等同于成功了一半。"),
            ("die Konzentration", "die", "Nomen", "unz.", "注意力，专注度", "Vor der Prüfung sollte man tief durchatmen, um die Konzentration zu bündeln.", "在正式进入考场发卷之前应当深呼吸数次，以迅速将注意力收拢凝聚起来。"),
            ("das Selbstvertrauen", "das", "Nomen", "unz.", "自信力", "Mit kontinuierlicher Übung gewinnt man großes Selbstvertrauen.", "通过持之以恒的高效模块化实战演练，你必将收获坚不可摧的强大自信。"),
            ("die Nervosität", "die", "Nomen", "unz.", "紧张心理", "Lampenfieber und Nervosität lassen sich durch gute Vorbereitung besiegen.", "考前心慌与轻度紧张完全可以通过胸有成竹的充足备考而彻底烟消云散。"),
            ("das Ergebnis", "das", "Nomen", "-se", "成绩，考分结果", "Zwei Wochen nach der Prüfung trafen die erfreulichen Prüfungsergebnisse ein.", "在考试结束两周之后，令人欣喜万分的官方成绩单正式寄送到了考生手中。"),
            ("die Note", "die", "Nomen", "-n", "成绩等级，分数", "Sie schloss das Zertifikat B1 mit der hervorragenden Note 'Sehr gut' ab.", "她最终以全优的傲人成绩“Sehr gut”顺利斩获了歌德B1等级水平证书。"),
            ("das Bestehen", "das", "Nomen", "unz.", "通过，及格通关", "Wir gratulieren dir von ganzem Herzen zum erfolgreichen Bestehen der Prüfung!", "我们发自肺腑地衷心祝贺你以优异出色的综合表现顺利通关此次严峻考试！"),
            ("zustimmen", "kein", "Verb", "stimmte zu, zugestimmt", "赞同，同意 (Dat.)", "Ich stimme deinen überzeugenden Ausführungen voll und ganz zu.", "对于你刚才所作出的这番极具洞察力的阐释剖析，我表示完完全全赞同。"),
            ("widersprechen", "kein", "Verb", "widersprach, widersprochen", "反驳，提出异议 (Dat.)", "Da muss ich Ihnen aus triftigen Gründen leider widersprechen.", "在这一点上，出于某些极其充分客观的关键理由，我恐怕必须提出异议。"),
            ("bezweifeln", "kein", "Verb", "bezweifelte, bezweifelt", "质疑，怀疑", "Ich bezweifle, dass dieser teure Ansatz auf Dauer funktioniert.", "我十分怀疑这种耗资巨大的激进做法在漫长岁月里是否真能行得通。"),
            ("begründen", "kein", "Verb", "begründete, begründet", "论证，阐明理由", "Könnten Sie Ihre persönliche Sichtweise bitte noch genauer begründen?", "能否请您结合实际情况将您刚才提出的个人视角再予以更深入的论证？"),
            ("vergleichen", "kein", "Verb", "verglich, verglichen", "比较，对比", "Vergleichen Sie die Vor- und Nachteile beider Lösungsmöglichkeiten!", "请您将这两项备选解决方案各自所蕴含的优势与弊端做一番全面对比！"),
            ("abwägen", "kein", "Verb", "wog ab, abgewogen", "权衡，仔细斟酌", "Man muss alle Risiken und Chancen vor einer Entscheidung sorgfältig abwägen.", "在最终拍板定案之前，决策者必须对一切潜在风险与战略机遇做细致权衡。"),
            ("überzeugen", "kein", "Verb", "überzeugte, überzeugt", "使信服，说服", "Ihre stichhaltigen Argumente konnten das gesamte Prüfungsgremium überzeugen.", "她所列出的无可辩驳的坚实论据彻底说服了考评委员会的全体考官专家。"),
            ("unterbrechen", "kein", "Verb", "unterbrach, unterbrochen", "打断发言", "Entschuldigen Sie bitte, wenn ich Sie an dieser Stelle kurz unterbreche!", "非常抱歉，如果在此时此刻我不得不冒昧稍稍打断一下您的长篇发言！"),
            ("zusammenfassen", "kein", "Verb", "fasste zusammen, zusammengefasst", "概括，综述", "Lassen Sie mich die wichtigsten Kernpunkte nochmals kurz zusammenfassen!", "请允许我将方才讨论中涉及的这几项最核心的要点再做一次精炼的归纳！"),
            ("beurteilen", "kein", "Verb", "beurteilte, beurteilt", "评估，裁判评价", "Es ist schwierig, die langfristigen gesellschaftlichen Folgen exakt zu beurteilen.", "想要在此时此刻便对极其深远的长期社会涟漪效应做出精准定性绝非易事。"),
            ("verdeutlichen", "kein", "Verb", "verdeutlichte, verdeutlicht", "阐明，使清晰", "Ein praktisches Alltagsbeispiel kann diesen komplexen Sachverhalt verdeutlichen.", "一个生动形象的生活日常案例便足以将这桩错综复杂的深奥法理阐明透彻。"),
            ("hervorheben", "kein", "Verb", "hob hervor, hervorgehoben", "强调，着重突出", "Der Referent hob die herausragende Bedeutung des interkulturellen Dialogs hervor.", "主讲报告人在发言中着重强调了推进跨文化沟通对话所具备的重大意义。"),
            ("formulieren", "kein", "Verb", "formulierte, formuliert", "起草，用言语表述", "Formulieren Sie Ihre Thesen stets prägnant, klar und unmissverständlich!", "请始终以言简意赅、清晰明了且毫无歧义的方式来表述你的核心学术论点！"),
            ("berücksichtigen", "kein", "Verb", "berücksichtigte, berücksichtigt", "顾及，充分考虑", "Bei der Planung muss man die Bedürfnisse aller Beteiligten berücksichtigen.", "在制定总规划时必须将所有相关参与主体的正当现实诉求全部顾及在内。"),
            ("meistern", "kein", "Verb", "meisterte, gemeistert", "驾驭，成功攻克", "Mit Fleiß und eiserner Disziplin wirst auch du diese Prüfung bravourös meistern.", "只要倾注辛勤汗水并恪守钢铁般的自律，你也必将极其出色地攻克这场大考。"),
            ("nachhaken", "kein", "Verb", "hakte nach, nachgehakt", "追问，深入探究", "Der Prüfer hakte bei einer unklaren Formulierung nochmals freundlich nach.", "针对考生方才一处含混不清的措辞，考官十分和蔼地再次进行了深入追问。"),
            ("punkten", "kein", "Verb", "punktete, gepunktet", "拿分，脱颖而出", "Mit einem abwechslungsreichen Satzbau kann man in der Prüfung voll punkten.", "凭借错落有致、变化多端的高阶长短句型结构，考生完全可以在考场强势拿分。"),
            ("bestehen", "kein", "Verb", "bestand, bestanden", "通过，及格", "Alle Teilnehmer unseres intensiven Vorbereitungskurses bestanden die B1-Prüfung.", "参加我们强化突击集训备考班的全体学员最终全员通过了歌德B1等级大考。"),
            ("überzeugend", "kein", "Adjektiv", "-", "令人信服的，有说服力的", "Ihre Argumentation war logisch durchdacht und absolut überzeugend.", "她的全篇论述思维缜密、逻辑自洽，展现出了令人心悦诚服的强大力量。"),
            ("präzise", "kein", "Adjektiv", "-", "精确的，严密的", "Eine präzise Wortwahl verhindert Missverständnisse im Fachgespräch.", "在专业学术探讨交谈中，严密精准的遣词造句能够彻底杜绝任何误解歧义。"),
            ("flüssig", "kein", "Adjektiv", "-", "流利的，通畅的", "Sie spricht flüssig und fast fehlerfrei Deutsch im Alltag.", "她在日常生活交际中能够讲一口流利连贯且几乎挑不出语法硬伤的德语。"),
            ("angemessen", "kein", "Adjektiv", "-", "恰当的，得体的", "Wählen Sie stets ein der jeweiligen Situation angemessenes Sprachregister!", "请大家在交际中务必结合具体的社交场合与语境选用恰如其分的语言风格！"),
            ("wesentlich", "kein", "Adjektiv", "-", "本质的，根本的", "Das ist ein ganz wesentlicher Punkt, den wir keinesfalls übersehen dürfen.", "这是一个我们无论如何也绝对不可草率忽略的最为关键本质的核心要害所在。"),
            ("anschaulich", "kein", "Adjektiv", "-", "生动的，直观易懂的", "Mit anschaulichen Grafiken gestaltete sie ihre Präsentation spannend.", "通过穿插运用直观易懂的数据图表，她将自己的学术展示打造得引人入胜。"),
            ("kontrovers", "kein", "Adjektiv", "-", "有争议的，针锋相对的", "Über die Vor- und Nachteile von Homeoffice wird nach wie vor kontrovers debattiert.", "关于居家远程办公模式的利弊得失，各界目前依然在进行针锋相对的争辩。"),
            ("schlüssig", "kein", "Adjektiv", "-", "逻辑严密的，顺理成章的", "Sein Entwurf bietet ein in sich vollkommen schlüssiges und realistisches Gesamtkonzept.", "他的方案呈现了一套内在逻辑高度自洽严密且切实可行的宏观整体规划构想。"),
            ("stichhaltig", "kein", "Adjektiv", "-", "站得住脚的，有真凭实据的", "Ohne stichhaltige Beweise sollte man derartige Behauptungen nicht aufstellen.", "在缺乏站得住脚的确凿真凭实据之前，任何人都不应当妄下此类断言。"),
            ("erfolgreich", "kein", "Adjektiv", "-", "成功的，胜利的", "Wir wünschen Ihnen eine erfolgreiche und erkenntnisreiche B1-Prüfung!", "我们衷心预祝各位在即将到来的歌德B1等级大考中旗开得胜、斩获佳绩！")
        ]
    }
]
