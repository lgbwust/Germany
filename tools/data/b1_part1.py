#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B1 Part 1: Lessons 1 to 5 (350 words)
L01: 人际交往、社会心理与矛盾沟通 (Beziehungen & Konflikte) - 70 words
L02: 大学学术生活、学科研究与高等教育 (Hochschule & Studium) - 70 words
L03: 职场求职、面试技巧与职业生涯规划 (Bewerbung & Karriere) - 70 words
L04: 现代居住形态、租房法与社区治理 (Wohnformen & Mietrecht) - 70 words
L05: 深度环球旅行、跨文化交际与文化休克 (Reisen & Interkulturalität) - 70 words
"""

LESSONS_B1_PART1 = [
    # LESSON 1
    {
        "id": "B1_L01",
        "title": "第1课：人际交往、社会心理与矛盾沟通 (Beziehungen & Konflikte)",
        "summary": "掌握二分从句 (obwohl, trotzdem, zwar... aber)、人际心理与非暴力沟通策略",
        "grammar": {
            "title": "让步连词 obwohl 与转折副词 trotzdem 的辨析运用",
            "sections": [
                {
                    "heading": "1. obwohl (尽管) 从句 vs trotzdem (尽管如此) 副词",
                    "content": "• obwohl 引导从属从句，变位动词置于句末：\n  Obwohl wir unterschiedlicher Meinung sind, respektieren wir uns.\n• trotzdem 为连词性副词，占第1位，动词紧随其后占第2位：\n  Wir sind unterschiedlicher Meinung. Trotzdem respektieren wir uns."
                },
                {
                    "heading": "2. 双重连词 zwar... aber (虽然...但是)",
                    "content": "• Er hat zwar wenig Freizeit, aber er treibt regelmäßig Sport."
                }
            ]
        },
        "quiz": [
            {
                "id": "B1_L01_Q1",
                "type": "GRAMMAR_FILL",
                "question": "______ (obwohl/trotzdem) es in Strömen regnete, machten sie einen langen Waldspaziergang.",
                "options": ["Obwohl", "Trotzdem", "Weil", "Deshalb"],
                "correctIndex": 0,
                "explanation": "从句动词 regnete 位于句末，引导从属从句使用让步连词 Obwohl。"
            },
            {
                "id": "B1_L01_Q2",
                "type": "VOCAB_MEANING",
                "question": "德语人际矛盾沟通中 'einen Kompromiss schließen' 意思是：",
                "options": ["达成妥协与折中方案", "断绝朋友关系", "发生肢体冲突", "签订劳动合同"],
                "correctIndex": 0,
                "explanation": "einen Kompromiss schließen 是德语高频固定搭配，意为“达成妥协、和解”。"
            }
        ],
        "words": [
            ("die Beziehung", "die", "n.", "-en", "人际关系，情感纽带", "Eine stabile Beziehung basiert auf gegenseitigem Vertrauen.", "稳固的人际关系建立在彼此相互信任的基础之上。"),
            ("das Verhältnis", "das", "n.", "-se", "相处状态，交往关系", "Sie pflegt ein enges Verhältnis zu ihren Großeltern.", "她同祖父母之间保持着极其亲密深厚的相处关系。"),
            ("die Freundschaft", "die", "n.", "-en", "至真友谊，朋友情谊", "Echte Freundschaft erweist sich in stürmischen Zeiten.", "唯有在风雨飘摇的艰难时刻方能检验出真挚友谊的纯度。"),
            ("die Partnerschaft", "die", "n.", "-en", "伴侣关系，伙伴关系", "Eine gleichberechtigte Partnerschaft erfordert ständige Kommunikation.", "平等的伴侣关系需要双方在日积月累中不间断地坦诚沟通。"),
            ("der Partner", "der", "n.", "-", "人生伴侣；合作伙伴", "Er fand in ihr eine verständnisvolle Partnerin fürs Leben.", "他在她身上找到了能够相濡以沫相伴一生的知心人生伴侣。"),
            ("die Partnerin", "die", "n.", "-nen", "女性伴侣，女合伙人", "Sie leitet die Kanzlei gemeinsam mit einer Partnerin.", "她与一位女合伙人共同执掌并打理着这间知名律师事务所。"),
            ("die Gemeinschaft", "die", "n.", "-en", "社群共同体，集体", "Das Gefühl der Gemeinschaft stärkt den inneren Zusammenhalt.", "休戚与共的集体归属感极大增强了团队内生的强大凝聚力。"),
            ("der Zusammenhalt", "der", "n.", "-", "团结一心，紧密凝聚", "Der familiäre Zusammenhalt trug sie durch die schwere Krise.", "家庭成员风雨同舟的紧密团结支撑着全家跨越了重大危机。"),
            ("das Vertrauen", "das", "n.", "-", "笃定信赖，信任", "Vertrauen gewinnt man schwer, verliert es jedoch rasch.", "建立起深厚互信往往耗费经年，而毁掉信任却往往在弹指间。"),
            ("vertrauen", "", "v.", "vertraut, vertraute, vertraut", "信赖，信任 (接 Dativ)", "Ich vertraue meinem besten Freund blindlings in jeder Lage.", "在任何情形下我都毫无保留、百分之百信赖我最好的挚友。"),
            ("zuverlässig", "", "adj.", "zuverlässiger, am zuverlässigsten", "言出必行靠谱笃信的", "Zuverlässige Freunde sind wie ein sicherer Anker im Leben.", "言出必行靠谱的朋友就如同生活中一座坚如磐石的避风锚碇。"),
            ("die Zuverlässigkeit", "die", "n.", "-", "靠谱品格，可靠性", "Seine Zuverlässigkeit wird von allen Geschäftspartnern geschätzt.", "他那一言九鼎的过硬品格赢得了全体商务合作伙伴交口称赞。"),
            ("die Ehrlichkeit", "die", "n.", "-", "襟怀坦荡，诚实守信", "Ehrlichkeit währt am längsten, mahnt ein altes Sprichwort.", "一句经典民间谚语意味深长地告诫后人：唯有诚实方能行稳致远。"),
            ("ehrlich", "", "adj.", "ehrlicher, am ehrlichsten", "坦荡诚恳讲真话的", "Ein ehrliches Feedback hilft bei der persönlichen Weiterentwicklung.", "一份不掺水分、坦诚中肯的反馈能切实助益个人的内省与进阶。"),
            ("die Offenheit", "die", "n.", "-", "开明豁达，坦率赤诚", "Offenheit gegenüber anderen Kulturen bereichert den eigenen Horizont.", "对异质文明抱持开明包容的赤诚心胸能极大拓展自身精神视野。"),
            ("offen", "", "adj.", "offener, am offensten", "直言不讳开诚布公的", "In einer guten Beziehung spricht man offen über Wünsche und Ängste.", "在一段健康的感情中，双方总能毫无顾忌地敞开心扉畅谈希冀。"),
            ("das Mitgefühl", "das", "n.", "-", "同理心，深切共情", "Echtes Mitgefühl tröstet Trauernde mehr als leere Worte.", "发自肺腑的真切同理与共情，远比苍白客套的言辞更能抚慰悲痛。"),
            ("die Empathie", "die", "n.", "-", "共情能力，移情同理", "Empathie ist die Schlüsselkompetenz für friedliche Konfliktlösung.", "敏锐的共情能力是和平化解人际矛盾争端不可或缺的核心素养。"),
            ("die Rücksicht", "die", "n.", "-", "体恤体谅，设身处地", "Nehmen Sie bitte Rücksicht auf kranke und ältere Mitmenschen!", "在公共场所请务必推己及人，处处体恤病弱长者的实际不便！"),
            ("rücksichtsvoll", "", "adj.", "rücksichtsvoller, am rücksichtsvollsten", "体贴入微处处着想的", "Ein rücksichtsvoller Umgangston verhindert Missverständnisse.", "体贴温润、顾及他人感受的措辞谈吐能够从源头规避误会丛生。"),
            ("der Respekt", "der", "n.", "-", "敬重心态，尊崇敬重", "Gegenseitiger Respekt bildet das Fundament jeder Debattenkultur.", "彼此敬重对方的人格与观点构成了健康文明辩论文化的基石。"),
            ("respektieren", "", "v.", "respektiert, respektierte, respektiert", "敬重，尊重对方立场", "Wir müssen die Privatsphäre jedes Einzelnen strikt respektieren.", "我们必须以最坚决的态度严格尊重并保障每个公民的私人空间。"),
            ("die Toleranz", "die", "n.", "-", "求同存异，包容雅量", "Gelebte Toleranz ist der Kern einer pluralistischen Demokratie.", "身体力行求同存异的宽容雅量是多元开放现代民主社会的核心。"),
            ("tolerieren", "", "v.", "toleriert, tolerierte, toleriert", "包容，容许异见存在", "In einer pluralen Gesellschaft toleriert man abweichende Ansichten.", "身处价值多元的人民社会，理应涵养包容不同见解存在的雅量。"),
            ("der Konflikt", "der", "n.", "-e", "针锋相对的利益冲突", "Konflikte sind unvermeidlich, entscheidend ist die Art ihrer Lösung.", "矛盾冲突在所难免，关键在于当事各方以何种智慧加以化解。"),
            ("der Streit", "der", "n.", "Streitigkeiten", "口角之争，争吵纷争", "Ein banaler Streit über Kleinigkeiten eskalierte völlig unnötig.", "一场原本因鸡毛蒜皮微末小事引发的口角争吵发生了不测升级。"),
            ("streiten", "", "v.", "streitet, stritt, gestritten", "争吵论争 (über/um + Akk)", "Sie stritten erbittert um die gerechte Aufteilung des Erbes.", "兄弟二人为了家族遗产的公平分割在公堂之上争论得不可开交。"),
            ("das Missverständnis", "das", "n.", "-se", "由沟通不畅导致的误会", "Viele Konflikte beruhen schlicht auf sprachlichen Missverständnissen.", "很多看似激烈的矛盾分歧其实纯粹源于语言信息传递中的误会。"),
            ("missverstehen", "", "v.", "missversteht, missverstand, missverstanden", "曲解，产生误解", "Ich befürchte, Sie haben meine Absicht völlig missverstanden.", "我十分担忧您在某种程度上彻底误解了我此番肺腑之言的初衷。"),
            ("klären", "", "v.", "klärt, klärte, geklärt", "厘清事实，澄清误会", "Lassen Sie uns den Vorfall in einem ruhigen Vier-Augen-Gespräch klären!", "让我们在心平气和的闭门私下长谈中把这桩误会原委彻底厘清！"),
            ("die Klärung", "die", "n.", "-en", "澄清真相，厘清是非", "Die sachliche Klärung der Fakten beruhigte die erregten Gemüter.", "对客观事实冷静中肯的澄清说明让现场群情激愤的情绪平复下来。"),
            ("der Kompromiss", "der", "n.", "-e", "互谅互让折中妥协", "Ein tragfähiger Kompromiss verlangt Zugeständnisse von beiden Seiten.", "一个立得住的务实折中方案必然要求争端各方相向而行做出让步。"),
            ("die Einigung", "die", "n.", "-en", "握手言和达成共识", "Nach zähem Ringen erzielten die Verhandlungspartner eine Einigung.", "经过艰苦卓绝的拉锯博弈，谈判各方最终握手言和达成全面共识。"),
            ("einigen", "", "v.", "einigt, einigte, geeinigt", "就争议达成一致", "Die Parteien einigten sich außergerichtlich auf Schadensersatz.", "争议双方在开庭前达成庭外和解，就民事侵权赔偿额达成一致。"),
            ("die Versöhnung", "die", "n.", "-en", "泯灭恩仇和好如初", "Die historische Versöhnung der beiden Nachbarvölker nach dem Kriege.", "交战两国人民在硝烟散尽后跨越仇恨、实现历史性和解与拥抱。"),
            ("versöhnen", "", "v.", "versöhnt, versöhnte, versöhnt", "和解，化解前嫌", "Nach jahrelangem Schweigen versöhnten sich die zerstrittenen Brüder.", "在经历长达数年的形同陌路后，反目成仇的兄弟俩最终冰释前嫌。"),
            ("verzeihen", "", "v.", "verzeiht, verzieh, verziehen", "大度原谅，宽恕罪过", "Wer wahrhaft liebt, findet auch die Kraft zu verzeihen.", "内心深处真正懂得去爱的人，自能生发出大度宽恕过错的胸襟。"),
            ("die Verzeihung", "die", "n.", "-", "宽恕原宥，海涵见谅", "Ich bitte vielmals um Verzeihung für mein unbedachtes Verhalten.", "我谨为自己日前未经大脑深思熟虑的莽撞鲁莽举止向您乞求原谅。"),
            ("die Schuld", "die", "n.", "-en", "过咎过错；金钱债务", "Schieben Sie die Schuld bitte nicht vorschnell auf andere ab!", "遇事切莫一味急于甩锅、轻率把过错与责任全推到别人头上！"),
            ("schuldig", "", "adj.", "", "负有罪责内疚亏欠的", "Er fühlte sich schuldig an dem Scheitern des gemeinsamen Plans.", "看到原本构想宏大的共同蓝图功亏一篑，他内心深感内疚自责。"),
            ("die Entschuldigung", "die", "n.", "-en", "诚恳致歉，赔罪说明", "Eine aufrichtige Entschuldigung glättet selbst hohe Wellen.", "一次发自肺腑的诚挚道歉足以抚平哪怕掀起轩然大波的怒海狂澜。"),
            ("akzeptieren", "", "v.", "akzeptiert, akzeptierte, akzeptiert", "认可接纳，欣然接受", "Wir müssen die veränderten Rahmenbedingungen realistisch akzeptieren.", "我们必须以实事求是的务实眼光接纳业已发生深刻改变的环境。"),
            ("ablehnen", "", "v.", "lehnt ab, lehnte ab, abgelehnt", "严词拒绝，回绝请求", "Aus ethischen Gründen lehnte die Forscherin das Angebot strikt ab.", "出于崇高的科研伦理操守，这位女科学家严词拒绝了巨额诱惑。"),
            ("die Ablehnung", "die", "n.", "-en", "否定回绝，抵触态度", "Sein radikaler Vorschlag stieß auf einhellige Ablehnung im Gremium.", "他提出的激进倡议在委员会全体委员中遭遇了一致否决与回绝。"),
            ("die Kritik", "die", "n.", "-en", "中肯批评，书评剧评", "Konstruktive Kritik dient der stetigen Optimierung der Arbeitsabläufe.", "抱持善意的建设性批评能够有力推动各项工作流程的持续优化。"),
            ("kritisieren", "", "v.", "kritisiert, kritisierte, kritisiert", "提出严肃批评批驳", "Die Opposition kritisiert die unzureichenden Reformmaßnahmen scharf.", "在野党阵营对近期出台的隔靴搔痒式改革举措提出了极其严厉的批评。"),
            ("kritisierbar", "", "adj.", "", "有待商榷可被批评的", "Diese Vorgehensweise ist aus juristischer Sicht durchaus kritisierbar.", "从严谨法理视角审视，这种暗箱操作的行径完全是有待推敲批评的。"),
            ("loben", "", "v.", "lobt, lobte, gelobt", "击节赞赏，当面夸奖", "Der Projektleiter lobte die beispielhafte Einsatzbereitschaft aller Beteiligten.", "项目负责人高度评价并当众嘉奖了全体参研人员展现出的奉献精神。"),
            ("das Lob", "das", "n.", "-", "赞扬由衷肯定之辞", "Aufrichtiges Lob spornt Mitarbeiter zu noch höheren Leistungen an.", "管理者发自真心的肯定褒奖能极大激发全体员工攀登新高峰的士气。"),
            ("die Anerkennung", "die", "n.", "-", "社会认可，高度首肯", "Er erhielt breite gesellschaftliche Anerkennung für sein Lebenswerk.", "他为公益奉献毕生的崇高义举赢得了全社会各界发自肺腑的崇高认可。"),
            ("anerkennen", "", "v.", "erkennt an, erkannte an, anerkannt", "权威正式核验认可", "Die Behörde erkennt ausländische Berufsabschlüsse nach Prüfung an.", "行政审批机关在严谨履行专家评审程序后依法对海外文凭予以认证。"),
            ("schätzen", "", "v.", "schätzt, schätzte, geschätzt", "珍视器重；推算估价", "Ich schätze ihre loyale und aufrichtige Art ganz ungemein.", "我打心底里极其器重并珍视她身上那种忠诚赤胆、光明磊落的气度。"),
            ("die Wertschätzung", "die", "n.", "-", "温情体恤，敬重关爱", "Mitarbeiter brauchen Wertschätzung und ein faires Gehalt.", "广大一线打工人既需要温情脉脉的尊重认可，更需要体面的薪酬。"),
            ("enttäuschen", "", "v.", "enttäuscht, enttäuschte, enttäuscht", "使大失所望，辜负信任", "Ich wollte dich mit meiner unbedachten Entscheidung keinesfalls enttäuschen.", "我当初做出那个冒进决断时，绝对没有半点想要让你寒心失望的意思。"),
            ("die Enttäuschung", "die", "n.", "-en", "大失所望令人沮丧之事", "Die bittere Niederlage im Finale war eine herbe Enttäuschung für das Team.", "在终极决赛中遭逢惨败对整支拼搏已久的球队而言是一场沉重的打击。"),
            ("wütend", "", "adj.", "wütender, am wütendsten", "义愤填膺怒不可遏的", "Bürger reagierten wütend auf die drastische Erhöhung der Gebühren.", "广大市民对管理部门未经听证便强行大幅上调收费政策感到义愤填膺。"),
            ("die Wut", "die", "n.", "-", "冲天狂怒暴怒之气", "Man sollte wichtige Weichenstellungen niemals in blinder Wut treffen.", "人在被冲天怒火蒙蔽心智的失控关头，切莫轻率做出关乎人生的抉择。"),
            ("der Ärger", "der", "n.", "-", "烦心糟心恼火之事", "Vermeiden Sie unnötigen Ärger durch vorausschauende Planung!", "遇事凡事提前留有余地、周密筹谋规划便能规避日后无数无谓的糟心事。"),
            ("ärgern", "", "v.", "ärgert, ärgerte, geärgert", "惹人懊恼生闷气", "Es ärgert mich maßlos, wenn Absprachen nicht eingehalten werden.", "一旦先前白纸黑字敲定的共识被当事人肆意毁约，实在令人气不打一处来。"),
            ("die Eifersucht", "die", "n.", "-", "患得患失之嫉妒猜忌", "Krankhafte Eifersucht zerstört selbst die innigste Zuneigung.", "病态偏执的疑神疑鬼与莫名嫉妒，足以将哪怕最深沉的爱意消磨殆尽。"),
            ("eifersüchtig", "", "adj.", "eifersüchtiger, am eifersüchtigsten", "嫉妒心重爱吃醋的", "Er reagierte eifersüchtig auf die beruflichen Erfolge seiner Kollegin.", "每当看到女同事在业务攻坚上拔得头筹，他内心深处便泛起酸溜溜的嫉妒。"),
            ("der Neid", "der", "n.", "-", "红眼病，嫉贤妒能", "Neid entsteht oft dort, wo der eigene Mangel spürbar wird.", "毫无节制的嫉恨往往滋生自当事人照镜子照出自身匮乏与平庸的阴暗角落。"),
            ("neidisch", "", "adj.", "neidischer, am neidischsten", "眼红嫉妒见不得人好的", "Man sollte nicht neidisch auf das vermeintliche Glück anderer blicken.", "人没有必要去盲目艳羡甚至眼红别人橱窗里光鲜亮丽展示出来的所谓幸福。"),
            ("einsam", "", "adj.", "einsamer, am einsamsten", "孤单寂寥孑然一身的", "Viele ältere Großstadtbewohner fühlen sich in den Wintermonaten einsam.", "许多长年独居在钢筋水泥大都市的高龄老人每逢严冬时节倍感形单影只。"),
            ("die Einsamkeit", "die", "n.", "-", "寂寞落寞幽闭独处", "Chronische Einsamkeit kann nachweislich der seelischen Gesundheit schaden.", "长期与世隔绝、无处话凄凉的深层孤独感已被现代医学证实有害身心。"),
            ("die Zuneigung", "die", "n.", "-en", "深情厚谊，由衷倾慕", "Ihre tiefe Zuneigung zueinander wuchs mit jedem überstandenen Hindernis.", "两人之间相濡以沫的真挚深情，伴随着一次次并肩跨越坎坷而愈发坚不可摧。"),
            ("die Leidenschaft", "die", "n.", "-en", "如火热情，狂热挚爱", "Er widmet sich der Erforschung historischer Manuskripte mit wahrer Leidenschaft.", "他怀着近乎狂热的炽热执念与毕生激情投身于中世纪古籍善本的考据中。"),
            ("leidenschaftlich", "", "adj.", "leidenschaftlicher, am leidenschaftlichsten", "充满火般激情的", "Sie hielt ein leidenschaftliches Plädoyer für weltweite Bildungsgerechtigkeit.", "她在世界大会讲台上发表了一篇激情澎湃、旨在呼吁教育普惠的演说。"),
            ("das Miteinander", "das", "n.", "-", "携手共融，休戚相处", "Ein respektvolles Miteinander bereichert die bunte Nachbarschaft ungemein.", "秉持彼此尊重、守望相助的共处之道，让多元文化社区展现出勃勃生机。"),
            ("die Harmonie", "die", "n.", "-n", "和谐融洽，天作合一", "Das Orchester spielte mit atemberaubender klanglicher Harmonie zusammen.", "在名指点拨下，整座交响乐团的管弦器乐配合展现出令人屏息的和谐。")
        ]
    },

    # LESSON 2
    {
        "id": "B1_L02",
        "title": "第2课：大学学术生活、学科研究与高等教育 (Hochschule & Studium)",
        "summary": "掌握带 zu 不定式短语 (Infinitiv mit zu)、大学学术研究、选课考核与论文写作",
        "grammar": {
            "title": "带 zu 不定式结构 (Infinitiv mit zu) 与动词/形容词/名词搭配",
            "sections": [
                {
                    "heading": "1. 不定式句末原则：zu + 动词原形（可分动词插入中间：einzuschreiben）",
                    "content": "• 与动词搭配：Es beginnt zu regnen. / Ich plane, in München zu studieren.\n• 与形容词搭配：Es ist wichtig, regelmäßig Vokabeln zu wiederholen.\n• 与名词搭配：Ich habe die Absicht, eine Promotion anzufangen."
                },
                {
                    "heading": "2. 固定不需要 zu 的动词（牢记！）",
                    "content": "情态动词 (können, müssen...), 感官动词 (sehen, hören), 行走位移动词 (gehen, fahren), 助动词 (werden, lassen)。"
                }
            ]
        },
        "quiz": [
            {
                "id": "B1_L02_Q1",
                "type": "GRAMMAR_FILL",
                "question": "Er hat die feste Absicht, sich für das Wintersemester ______ (einschreiben, 带zu不定式).",
                "options": ["einzuschreiben", "zu einschreiben", "eingeschrieben", "einschreiben"],
                "correctIndex": 0,
                "explanation": "可分动词 einschreiben 的带 zu 不定式形式为 einzuschreiben。"
            },
            {
                "id": "B1_L02_Q2",
                "type": "VOCAB_MEANING",
                "question": "德国大学里的 'die Immatrikulation' 意思是：",
                "options": ["大学正式注册入学手续", "毕业典礼答辩", "期末考试挂科重考", "申请助学贷款"],
                "correctIndex": 0,
                "explanation": "die Immatrikulation 是德国大学官方新生“注册入学”的法定专业词汇。"
            }
        ],
        "words": [
            ("die Hochschule", "die", "n.", "-n", "全日制高等学府高校", "Die Hochschule bietet praxisorientierte Studiengänge in Mechatronik an.", "这所高等学府在机电一体化等前沿工科开设了极具实操导向的优质专业。"),
            ("die Akademie", "die", "n.", "-n", "科学艺术研究院学院", "Er wurde als ordentliches Mitglied in die renommierte Akademie berufen.", "他凭借在量子力学方面的开创性建树被破格选聘为国家科学院正院士。"),
            ("der Campus", "der", "n.", "-", "现代化大学校园区", "Auf dem modernen Campus finden Studenten Wohnheime, Labore und Sportstätten.", "在规划一流的现代大学校园内，宿舍、实验大楼与体育场馆鳞次栉比。"),
            ("die Fakultät", "die", "n.", "-en", "大学二级学院院系", "Die Juristische Fakultät der Universität Heidelberg blickt auf Tradition.", "海德堡大学法学院作为欧洲法学摇篮，坐拥数百载深厚卓越法学学术积淀。"),
            ("der Fachbereich", "der", "n.", "-e", "学科专业集群学部", "Der Fachbereich Informatik kooperiert eng mit innovativen Tech-Startups.", "计算机学部与多家极富创新活力的人工智能初创企业保持深度产教融合。"),
            ("das Institut", "das", "n.", "-e", "大学专业研究所机构", "Das Max-Planck-Institut für Physik betreibt weltweit anerkannte Spitzenforschung.", "马克斯·普朗克物理研究所夜以继日向人类认知边缘进军开展全球顶尖科研。"),
            ("der Studiengang", "der", "n.", "Studiengänge", "大学专业方向课程体系", "Dieser interdisziplinäre Studiengang verknüpft Biologie mit maschinellem Lernen.", "这个高度前沿的交叉学科专业将微观分子生物学与大数据机器学习紧密贯通。"),
            ("das Studienfach", "das", "n.", "Studienfächer", "在读专业门类学科", "Ihr primäres Studienfach ist Psychologie mit dem Nebenfach Soziologie.", "她的主修在读专业为认知心理学，同时辅修攻读社会学与统计分析。"),
            ("der Bachelor", "der", "n.", "-s", "学士学位本科学历", "Nach sechs Semestern Regelstudienzeit schließt man mit dem Bachelor of Science ab.", "在完成法定的六个学期标准学制修业后，学子即可荣获理学学士文凭。"),
            ("der Master", "der", "n.", "-s", "硕士学位研究生阶段", "Ein forschungsorientierter Master vertieft die erworbenen Fachkenntnisse.", "以学术探究为导向的硕士培养阶段能够极大深化夯实前期所打下的理论底盘。"),
            ("die Promotion", "die", "n.", "-en", "攻读博士学位获博士头衔", "Er arbeitet intensiv an seiner Promotion auf dem Gebiet der Nanotechnologie.", "他正全身心埋头扑在纳米科技前沿课题的博士论文撰写与实验攻坚中。"),
            ("die Dissertation", "die", "n.", "-en", "博士毕业大论文", "Ihre Dissertation wurde mit dem Prädikat 'summa cum laude' bewertet.", "她的博士毕业学位论文被盲审答辩委员会全票裁定授予最高荣誉级评定。"),
            ("der Doktorand", "der", "n.", "-en", "在读攻博博士生", "Der Doktorand betreut neben eigenen Experimenten auch Bachelor-Studenten.", "这位在读博士生在推进自身课题之余，还担负起指导低年级本科生实验之责。"),
            ("die Doktorandin", "die", "n.", "-nen", "女性在读博士生", "Die engagierte Doktorandin publizierte bereits mehrere viel beachtete Paper.", "这位勤勉敏思的在读女博士生已在国际权威期刊上以一作发表了数篇顶刊论文。"),
            ("der Professor", "der", "n.", "-en", "大学正教授博士生导师", "Der Professor leitet den Lehrstuhl für Angewandte Mathematik seit zehn Jahren.", "这位知名资深正教授执掌应用数学核心讲席教席已有整整十年之久。"),
            ("der Dozent", "der", "n.", "-en", "高校授课讲师教师", "Der Dozent veranschaulicht theoretische Modelle mit praxisnahen Beispielen.", "主讲讲师善于信手拈来生动鲜活的行业案例化解深奥晦涩的纯数学模型。"),
            ("die Dozentin", "die", "n.", "-nen", "高校女性授课讲师", "Die Dozentin bietet wöchentlich eine persönliche Sprechstunde für Studenten an.", "该位女讲师每周都在办公室专门开辟专门的答疑咨询时段为学子答疑解惑。"),
            ("der Kommilitone", "der", "n.", "-n", "大学同届同窗同学", "Gemeinsam mit ihren Kommilitonen bereitete sie sich auf die Klausur vor.", "她与同进同退的大学同届同窗伙伴们结成复习小组全力备战期末闭卷硬仗。"),
            ("die Kommilitonin", "die", "n.", "-nen", "大学女性同窗同学", "Eine hilfsbereite Kommilitonin stellte mir ihre Vorlesungsmitschrift bereit.", "一位热心慷慨的女同窗主动将自己字迹娟秀的高质量大课笔记借我复印。"),
            ("die Immatrikulation", "die", "n.", "-en", "大学正式学籍注册登记", "Mit der feierlichen Immatrikulation beginnt der neue Lebensabschnitt.", "伴随着庄重的新生入学注册仪式的落幕，一段崭新的人生征程鸣锣启程。"),
            ("immatrikulieren", "", "v.", "immatrikuliert, immatrikulierte, immatrikuliert", "办理正式学籍注册", "Sie hat sich an der Technischen Universität München erfolgreich immatrikuliert.", "她已顺利办妥了慕尼黑工业大学机械工程专业的新生正式入学注册手续。"),
            ("die Exmatrikulation", "die", "n.", "-en", "大学结业注销学籍退学", "Nach dem erfolgreichen Bestehen der Masterprüfung erfolgte die Exmatrikulation.", "在圆满考取并通过硕士毕业终审答辩后，校方按章程办理了毕业学籍注销。"),
            ("die Zulassung", "die", "n.", "-en", "高校录取资格确认通知书", "Er erhielt die lang ersehnte Zulassung für das anspruchsvolle Medizinstudium.", "经过漫长等待他终于收到了梦寐以求的医学专业全国统招正式录取通知书。"),
            ("der Numerus Clausus", "der", "n.", "-", "分数线受限专业选拔门槛", "Für beliebte Fächer wie Psychologie gilt ein strenger Numerus Clausus.", "针对心理学等炙手可热的爆款专业，全德各校普遍设置了极严的高考绩点红线。"),
            ("der NC", "der", "n.", "-s", "录取门槛绩点（口语简称）", "Mit einem Abiturschnitt von 1,2 erfüllte sie den NC für Medizin mühelos.", "凭借高达1.2分的优异高中毕业绩点，她毫不费力便越过了医学院的分数门槛。"),
            ("die Einschreibung", "die", "n.", "-en", "在线确认选课注册选修", "Die Frist für die offizielle Einschreibung endet pünktlich zum Semesterbeginn.", "各科新学期正式选修报名的网上窗口将在开学第一天零点准时彻底关闭。"),
            ("der Semesterbeitrag", "der", "n.", "Semesterbeiträge", "学期公共事务杂费车票费", "Der Semesterbeitrag finanziert die studentische Selbstverwaltung und das Ticket.", "每学期缴纳的数百欧学杂费主要用于维持学生会公共运转并包含学期通乘车票。"),
            ("das Semesterticket", "das", "n.", "-s", "大学生学期免费通乘车票", "Mit dem Semesterticket nutzen Studenten alle Busse und Bahnen der Region.", "持有学期车票的大学生在整个学期内可无限次免费刷乘该大区所有公交地铁。"),
            ("das BAföG", "das", "n.", "-", "国家法定大学生助学金体系", "Viele bedürftige Studierende finanzieren ihren Lebensunterhalt über das BAföG.", "无数家庭经济条件欠佳的贫困学子依靠申请国家法定助学金解决求学温饱。"),
            ("das Stipendium", "das", "n.", "Stipendien", "奖学金资助计划", "Sie bewarb sich erfolgreich um ein renommiertes Begabtenstipendium.", "她凭借过人的学术潜质成功斩获了一项含金量极高的一流英才深造奖学金。"),
            ("die Vorlesung", "die", "n.", "-en", "大阶梯教室学术讲授大课", "Die Vorlesung zur Theoretischen Philosophie beginnt pünktlich um 10 Uhr c.t.", "思辨哲学校级大课将于上午十点一刻（高校习惯延后十五分钟）准时开讲。"),
            ("das Seminar", "das", "n.", "-e", "师生互动专题研讨研习班", "Im Hauptseminar diskutieren die Teilnehmer über postmoderne Gesellschaftstheorien.", "在高级研讨课上，师生共同就后现代社会结构批判理论展开了针锋相对的交锋。"),
            ("das Proseminar", "das", "n.", "-e", "低年级基础入门导论班", "Im Proseminar erlernen Erstsemester das Handwerkszeug wissenschaftlichen Arbeitens.", "在大一基础研讨导论班上，刚入校的新生系统打磨学术规范与考据基础功夫。"),
            ("die Übung", "die", "n.", "-en", "随堂课后演算习题实训课", "In der begleitenden Übung werden wöchentlich anspruchsvolle Rechenaufgaben gelöst.", "在配套的随堂习题课上，助教带着大家逐题拆解演算难度颇高的高等数学习题。"),
            ("das Tutorium", "das", "n.", "Tutorien", "高年级学长导学辅导班", "Das Tutorium bietet den Erstsemestern Orientierung und wertvolle Lerntipps.", "学长导学辅导班为初来乍到的大一懵懂新生提供了极有针对性的备考秘籍。"),
            ("der Tutor", "der", "n.", "-en", "助教学长，导学辅导员", "Der erfahrene Tutor erklärt die Laborgeräte geduldig Schritt für Schritt.", "经验丰富的高年级助教学长耐心地手把手指导学弟学妹操作昂贵实验设备。"),
            ("die Tutorin", "die", "n.", "-nen", "女性高年级导学助教", "Die engagierte Tutorin korrigiert die wöchentlichen Übungsblätter gewissenhaft.", "勤勉负责的女助教每周都极其认真细致地批阅大家提交的整整一叠实验报告。"),
            ("die Klausur", "die", "n.", "-en", "闭卷限时书面笔试统考", "Die zweistündige Klausur am Semesterende entscheidet über den Scheinerwerb.", "学期末那场长达两小时的闭卷综合大统考直接关乎能否顺利拿到该科结业学分。"),
            ("die Hausarbeit", "die", "n.", "-en", "期末学期学术小论文", "In den Semesterferien muss er eine zwanzigseitige Hausarbeit anfertigen.", "在别人放松度假的假期里，他必须按期熬夜打磨出一篇二十页的学术期末论文。"),
            ("das Referat", "das", "n.", "-e", "课堂专题口头汇报展示", "Sie hält ein überzeugendes Referat über den Strukturwandel im Ruhrgebiet.", "她在课堂上做了一场数据翔实、立论严密的鲁尔区传统工业转型专题汇报。"),
            ("das Protokoll", "das", "n.", "-e", "理化实验过程详实记录报告", "Jeder Student muss nach dem Chemiepraktikum ein lückenloses Protokoll abgeben.", "在完成全套无机化学实验后，每位学生均须依规提交一份无懈可击的过程记录。"),
            ("der Schein", "der", "n.", "-e", "科目成绩及格结业证明", "Um zur Prüfung zugelassen zu werden, benötigt er alle Scheine der Grundstufe.", "为了获得报考资格，他必须先出示集齐初级阶段所有必修科目的结业学分单。"),
            ("der Credit Point", "der", "n.", "-s", "欧洲学分互认学分绩点", "Für das bestandene Seminar werden fünf europäische Credit Points gutgeschrieben.", "顺利结业通过这门专题研讨班即可在个人学籍卡上累积计入五个欧洲通用学分。"),
            ("das Modulhandbuch", "das", "n.", "Modulhandbücher", "大学专业培养方案培养指南", "Im Modulhandbuch sind alle Lehrinhalte und Prüfungsformen exakt definiert.", "在专业培养方案指南中，对每门课程的教学大纲与终结考核形式作了权威界定。"),
            ("die Bachelorarbeit", "die", "n.", "-en", "学士本科毕业学位论文", "Er forschte drei Monate lang im Labor für seine empirische Bachelorarbeit.", "为了完成基于真实一手数据的本科毕业论文，他在实验室里整整泡了三个月。"),
            ("die Masterarbeit", "die", "n.", "-en", "硕士研究生毕业学位论文", "Die Masterarbeit bildet den krönenden wissenschaftlichen Abschluss des Studiums.", "硕士毕业论文的撰写与终审构成了全套高等专业研究生深造最关键的试金石。"),
            ("das Kolloquium", "das", "n.", "Kolloquien", "学术研讨答辩答辩会", "Im mündlichen Kolloquium verteidigte sie ihre Forschungsthesen souverän.", "在公开学术答辩会上，她从容笃定地逐一回应了答辩委员提出的苛刻学术质询。"),
            ("verteidigen", "", "v.", "verteidigt, verteidigte, verteidigt", "捍卫学术观点；毕业答辩", "Sie verteidigte ihre These mit stichhaltigen empirischen Argumenten.", "她援引大量经过严苛统计检验的实证数据，坚决有力地捍卫了自己的核心论点。"),
            ("die Verteidigung", "die", "n.", "-en", "毕业论文终期答辩", "Die erfolgreiche Verteidigung der Dissertation beendet die Promotionsphase.", "博士学位论文公开答辩的圆满落幕，宣告着这段艰辛而壮丽的读博征程终抵彼岸。"),
            ("die Wissenschaft", "die", "n.", "-en", "严谨求真之现代科学", "Die moderne Wissenschaft basiert auf überprüfbaren und reproduzierbaren Experimenten.", "现代自然科学的立身之本，在于任何理论结论都必须经得起可重复性实验检验。"),
            ("wissenschaftlich", "", "adj.", "", "合乎学术学术规范严谨的", "Wissenschaftliches Arbeiten erfordert absolute Präzision und intellektuelle Redlichkeit.", "开展严谨的学术科研要求学者具备毫米级的思维精确度与不可动摇的治学诚信。"),
            ("die Methode", "die", "n.", "-n", "科学研究方法论，范式", "Die qualitative Methode liefert tiefe Einblicke in komplexe soziale Dynamiken.", "质性实地研究方法能够为探寻错综复杂的社会群体动态提供极其深邃的洞察。"),
            ("die Hypothese", "die", "n.", "-n", "待证学术预设，假说", "Die aufgestellte Hypothese wurde durch die Datenreihe eindeutig widerlegt.", "研究团队先前提出的大胆假说被最新测得的一整串客观观测数据明确证伪推翻。"),
            ("die Theorie", "die", "n.", "-n", "系统化科学理论，学说", "Einsteins Allgemeine Relativitätstheorie veränderte unser Verständnis von Raum und Zeit.", "爱因斯坦创立的广义相对论在根本上彻底颠覆了人类此前对时空与引力的认知。"),
            ("das Experiment", "das", "n.", "-e", "受控实验化验实测", "Das physikalische Experiment am Teilchenbeschleuniger dauerte mehrere Monate.", "在大型强子对撞机深处开展的高能粒子物理受控实验整整昼夜不歇持续了数月。"),
            ("die Studie", "die", "n.", "-n", "专项学术实证研究报告", "Eine breit angelegte klinische Studie belegt die Wirksamkeit des neuen Wirkstoffs.", "一项样本量庞大的多中心双盲临床实证研究无可辩驳地证实了该新药的卓越疗效。"),
            ("die Quelle", "die", "n.", "-n", "考据源头，参考文献史料", "Geben Sie für jedes Zitat stets die exakte wissenschaftliche Quelle an!", "引用他人的任何一段观点或原句时，必须在文后用标准格式标注权威参考文献！"),
            ("zitieren", "", "v.", "zitiert, zitierte, zitiert", "引证引述先贤论断", "Er zitiert in seiner Einleitung berühmte Denker der Aufklärung.", "他在大作的开篇引言部分广征博引了数位启蒙运动时期泰斗级思想家的名言金句。"),
            ("das Zitat", "das", "n.", "-e", "直接引用之原话引言", "Wörtliche Zitate müssen im Text durch Anführungszeichen deutlich markiert werden.", "论文中一字不差直接原样引用的段落，正文中必须打上双引号并注明具体页码。"),
            ("das Plagiat", "das", "n.", "-e", "抄袭剽窃学术不端行为", "Das Verschleiern fremder geistiger Urheberschaft gilt als schweres Plagiat.", "企图掩盖并侵吞他人独创性智力成果的行为在学术界被统一定性为恶劣学术不端。"),
            ("der Betrug", "der", "n.", "-", "学术欺诈造假，舞弊", "Datenfälschung in wissenschaftlichen Publikationen ist strafbarer Betrug.", "在权威科研刊物论文中恶意伪造窜改实验原始数据属不可饶恕的违法学术欺诈。"),
            ("die Bibliothek", "die", "n.", "-en", "大学浩瀚知识殿堂图书馆", "In der Universitätsbibliothek stehen Millionen Bände für die Forschung bereit.", "在这所历史名校的中央图书馆中，数以百万册计的珍贵典籍静候着学者探微索隐。"),
            ("der Lesesaal", "der", "n.", "Lesesäle", "沉静肃穆的大阅览大厅", "Im stillen Lesesaal herrscht eine konzentrierte, ehrfürchtige Arbeitsatmosphäre.", "在悄无声息的古籍善本大阅览室里，弥漫着一种令人心生敬畏的专注治学氛围。"),
            ("die Ausleihe", "die", "n.", "-en", "图书文献外借业务借阅处", "Die elektronische Ausleihe erfolgt unkompliziert mit dem Studierendenausweis.", "只需刷一下芯片学生卡，读者便可在自助借还机上丝滑办结图书外借出库。"),
            ("die Fernleihe", "die", "n.", "-n", "跨校跨国文献馆际互借", "Seltene Werke aus anderen Städten beschafft die Bibliothek per Fernleihe.", "针对本馆暂缺的偏门古旧孤本，馆员能够极其迅捷地借助馆际互借系统异地调拨。"),
            ("die Recherche", "die", "n.", "-n", "深度学术检索资料搜寻", "Eine gründliche Literaturrecherche bildet den Auftakt jeder wissenschaftlichen Arbeit.", "穷尽式的中外文献纵深大检索是构筑任何一项严谨学术研究大厦的奠基起手式。"),
            ("recherchieren", "", "v.", "recherchiert, recherchierte, recherchiert", "多方排查检索考据", "Die Wissenschaftlerin recherchierte wochenlang in geheimen Staatsarchiven.", "这位女历史学家在国家绝密历史档案库的浩繁卷帙中潜心披沙拣金检索了数周。"),
            ("die Publikation", "die", "n.", "-en", "公开出版发行学术专著", "Seine bahnbrechende Publikation in 'Nature' fand weltweit größte Beachtung.", "他在顶级权威学术刊物《自然》上发表的里程碑式大作在全球科技界引起轰动。"),
            ("publizieren", "", "v.", "publiziert, publizierte, publiziert", "出版印刷，发表大作", "Wissenschaftler müssen publizieren, um in ihrer akademischen Laufbahn voranzukommen.", "正所谓不发表便出局，青年科研人员唯有不断斩获高水平学术发表方能脱颖而出。"),
            ("die Karriere", "die", "n.", "-n", "登峰造极之学术进阶路", "Eine akademische Karriere erfordert unermüdlichen Fleiß, Neugier und Frustrationstoleranz.", "走通象牙塔尖的学术通途，既要求百折不挠的求知好奇心，更需要超常的抗挫力。")
        ]
    },

    # LESSON 3
    {
        "id": "B1_L03",
        "title": "第3课：职场求职、面试技巧与职业生涯规划 (Bewerbung & Karriere)",
        "summary": "掌握被动语态现在完成时与过去时 (Passiv Perfekt/Präteritum)、面试自我推介与职业谈判",
        "grammar": {
            "title": "被动语态完成时与过去时 (Passiv im Präteritum und Perfekt)",
            "sections": [
                {
                    "heading": "1. 过去时被动：wurden + Partizip II",
                    "content": "• Der Vertrag wurde gestern von beiden Parteien unterschrieben.\n• Die Bewerbungsunterlagen wurden bereits geprüft."
                },
                {
                    "heading": "2. 现在完成时被动：ist... Partizip II + worden (注意没有 ge-!)",
                    "content": "• Meine Bewerbung ist gestern abgeschickt worden.\n• Die Stelle ist bereits besetzt worden."
                }
            ]
        },
        "quiz": [
            {
                "id": "B1_L03_Q1",
                "type": "GRAMMAR_FILL",
                "question": "Die Bewerbungsmappe ______ (sein/haben) gestern an die Personalabteilung geschickt worden.",
                "options": ["ist", "hat", "wird", "wurde"],
                "correctIndex": 0,
                "explanation": "被动语态现在完成时助动词必须用 sein (ist ... geschickt worden)。"
            },
            {
                "id": "B1_L03_Q2",
                "type": "VOCAB_MEANING",
                "question": "求职面试信末尾的 'die Gehaltserwartung' 意思是：",
                "options": ["薪资期望要求", "离职理由陈述", "学历学位认证", "工作实习经历"],
                "correctIndex": 0,
                "explanation": "die Gehaltserwartung 指求职者向用人单位提出的“税前年薪预期要求”。"
            }
        ],
        "words": [
            ("der Arbeitsmarkt", "der", "n.", "Arbeitsmärkte", "劳动力就业市场", "Auf dem modernen Arbeitsmarkt sind IT-Spezialisten heiß begehrt.", "在当前的劳动力就业市场上，高精尖软件架构师与数据专家可谓极度炙手可热。"),
            ("der Fachkräftemangel", "der", "n.", "-", "高素质专业人才荒", "Der akute Fachkräftemangel bremst das Wachstum in vielen Branchen.", "尖端专业技术人才的结构性紧缺在客观上制约着诸多实体支柱产业的扩张升级。"),
            ("die Stellenanzeige", "die", "n.", "-n", "招聘启事招聘广告", "Ich habe eine passende Stellenanzeige in der Zeitung entdeckt.", "我在主流全国性财经报纸招聘版面上偶然觅得了一则极其契合自身背景的招聘启事。"),
            ("das Stellenangebot", "das", "n.", "-e", "岗位虚席供给邀约", "Attraktive Stellenangebote locken gut ausgebildete Fachkräfte an.", "充满诚意与发展前景的高薪岗位邀约能够持续吸引功底扎实的高层次人才加盟。"),
            ("das Gesuch", "das", "n.", "-e", "求职求官自荐书", "Sein Stellengesuch im Internet führte zu mehreren Vorstellungsgesprächen.", "他在专业人才库平台上挂出的求职自荐档案为他迅速赢得了数个高规格面试机会。"),
            ("die Stellenausschreibung", "die", "n.", "-en", "正式职位公开竞聘公告", "Die interne Stellenausschreibung richtet sich an fest angestellte Mitarbeiter.", "这则企业内部公开竞聘通知专门面向集团内部所有已签订长期合同的在册骨干。"),
            ("das Anforderungsprofil", "das", "n.", "-e", "岗位胜任力任职要求画像", "Mein Werdegang passt exakt auf das geforderte Anforderungsprofil.", "我过往这些年的实战履历与操盘业绩与贵司岗位的胜任力画像简直是严丝合缝。"),
            ("die Voraussetzung", "die", "n.", "-en", "硬性任职前置必备条件", "Verhandlungssicheres Englisch ist eine zwingende Voraussetzung für den Job.", "能够无障碍使用商务英语进行高端商业谈判是入职该国际岗位的硬性刚需门槛。"),
            ("die Qualifikation", "die", "n.", "-en", "胜任力资质与证书背书", "Zusätzliche Qualifikationen erhöhen die Chancen im Auswahlverfahren.", "持有含金量十足的跨学科复合资质证书能显著拔高你在层层遴选面试中的胜率。"),
            ("die Bewerbung", "die", "n.", "-en", "求职投递，应聘申请", "Eine überzeugende Bewerbung zeichnet sich durch Individualität aus.", "一份真正能打动挑剔HR的硬核求职材料，其灵魂在于鲜明独特的个性化定制。"),
            ("die Bewerbungsunterlagen", "die", "n.pl.", "-", "全套求职申请材料包", "Vollständige Bewerbungsunterlagen enthalten Anschreiben, Lebenslauf und Zeugnisse.", "一份完整规范的应聘材料包必须齐备求职自荐信、个人履历表及权威鉴定成绩单。"),
            ("das Anschreiben", "das", "n.", "-", "求职自荐第一求职信", "Im Anschreiben begründen Sie Ihre Motivation für diese Position.", "在篇幅精炼的求职信中，你需要极其有力地阐述你竞逐该岗位的底层职业动机。"),
            ("die Motivation", "die", "n.", "-en", "自驱力，职业追求心", "Hohe intrinsische Motivation und Lernbereitschaft zeichnen ihn aus.", "极高的内驱力与如饥似渴的拥抱学习新事物的热忱是他身上最闪耀的职场品格。"),
            ("das Motivationsschreiben", "das", "n.", "-", "求职自白信动机阐述函", "Das Motivationsschreiben sollte maximal eine DIN-A4-Seite umfassen.", "动机阐述函的篇幅结构应当极尽精炼，严格控制在单张A4纸版面之内为宜。"),
            ("der Lebenslauf", "der", "n.", "Lebensläufe", "时间倒序式个人简历", "Der Lebenslauf sollte lückenlos und übersichtlich strukturiert sein.", "个人职业履历表在时间线排布上务必做到严丝合缝无空白断档且视觉层级清晰。"),
            ("lückenlos", "", "adj.", "", "天衣无缝无时间断档的", "Er konnte einen lückenlosen beruflichen Werdegang vorweisen.", "他能够向背景调查机构出示一份没有任何职业空白断档、步步为营的亮眼履历。"),
            ("chronologisch", "", "adj.", "", "依时间先后顺序顺列的", "Der tabellarische Lebenslauf wird meist antichronologisch verfasst.", "当代表格式简历普遍遵循倒叙法排布，即最新最近的工作经历置于最前端。"),
            ("das Foto", "das", "n.", "-s", "职业正装高清商务肖像照", "In Deutschland ist ein professionelles Bewerbungsfoto üblich.", "在德意志职场文化习俗中，附上一张拍摄精良的商务正装大头照已成约定俗成。"),
            ("das Zeugnis", "das", "n.", "-se", "前雇主工作表现鉴定证书", "Ein hervorragendes qualifiziertes Arbeitszeugnis ist Gold wert.", "一份由上一任外企雇主出具的高评语正式工作鉴定书在跳槽时堪称无价之宝。"),
            ("das Arbeitszeugnis", "das", "n.", "-se", "前雇主离职工作表现鉴定", "Im Arbeitszeugnis werden Leistung und Sozialverhalten beurteilt.", "在这份由公司签字盖章的鉴定书中，对员工的业务攻坚战绩与人际协作做公允评定。"),
            ("die Referenz", "die", "n.", "-en", "业内权威背书推荐信", "Als Referenz nannte er seinen früheren Vorgesetzten bei Siemens.", "在背调联系人一栏他庄重留下了自己在西门子任职期间那位直接大部门总监的名讳。"),
            ("das Vorstellungsgespräch", "das", "n.", "-e", "正式现场求职面试", "Sie bereitet sich akribisch auf das morgige Vorstellungsgespräch vor.", "她正在对照企业财报与行业研报一丝不苟地精心备战明天上午的终极求职面试。"),
            ("das Bewerbungsgespräch", "das", "n.", "-e", "求职现场深谈面试", "Im Bewerbungsgespräch punktete er mit Fachkompetenz und Humor.", "在那场气氛融洽的深度求职面试中，他凭借过硬的专业底蕴与幽默谈吐技惊四座。"),
            ("der Personalleiter", "der", "n.", "-", "集团人力资源部总监", "Der Personalleiter führte das Interview gemeinsam mit der Teamleiterin.", "集团HR总监协同用人业务部门女主管共同主导实施了这场全面深度的候选人终面。"),
            ("der Kandidat", "der", "n.", "-en", "竞聘候选人，应征者", "Von hundert Bewerbern wurden die drei besten Kandidaten eingeladen.", "在数百名海投的应聘大军中，唯有实力最拔尖的三位候选人获邀进入最终面试圈。"),
            ("die Kandidatin", "die", "n.", "-nen", "女性终极竞聘候选人", "Die Kandidatin überzeugte auf ganzer Linie durch ihr Auftreten.", "这位出类拔萃的女候选人凭借落落大方、不卑不亢的沉稳台风全方位征服了评委。"),
            ("der Stärken-Schwächen-Abgleich", "der", "n.", "-", "个人优劣势客观对撞盘点", "Kennen Sie Ihre Stärken und Schwächen und stehen Sie dazu!", "清醒看清自己的长板优势与短板软肋，并在提问时坦然从容承认、不遮不掩！"),
            ("die Gehaltsvorstellung", "die", "n.", "-en", "个人薪资报酬心理底线", "Nennen Sie eine realistische, marktgerechte Gehaltsvorstellung!", "在沟通薪资期望时请亮出一个符合行业公允行情与自身身价的成熟期望值！"),
            ("die Gehaltserwartung", "die", "n.", "-en", "年薪期望值与薪酬要求", "Seine Gehaltserwartung lag bei 65.000 Euro brutto im Jahr.", "他向对方开出了税前年薪六万五千欧元并附带项目绩效分红的合理薪资要求。"),
            ("das Einstiegsgehalt", "das", "n.", "Einstiegsgehälter", "职场新人首份起薪", "Akademiker erzielen in der Chemieindustrie ein hohes Einstiegsgehalt.", "名校工科硕士毕业生在大型化工外企能够斩获令人艳羡的高标准起步起薪。"),
            ("das Bruttogehalt", "das", "n.", "Bruttogehälter", "未扣税费五险一金之税前薪水", "Das vereinbarte Bruttogehalt wird monatlich auf das Bankkonto überwiesen.", "劳资双方合同白纸黑字敲定的税前工资将在每月最后一个工作日准时打卡。"),
            ("das Nettogehalt", "das", "n.", "Nettogehälter", "扣除税费后实际到手净工资", "Vom Brutto bleibt nach Abzug von Steuern und Abgaben das Netto übrig.", "在扣缴了法定个人所得税与各项社会强制保障金后，剩下的才是真金白银到手净薪。"),
            ("die Sozialabgaben", "die", "n.pl.", "-", "法定强制五险一金社保缴费", "Arbeitgeber und Arbeitnehmer teilen sich die Sozialabgaben paritätisch.", "在德意志社会保障体系框架下，雇主与雇员各自按二分之一比例对等承担社保缴费。"),
            ("die Rentenversicherung", "die", "n.", "-en", "国家法定法定养老金保险", "Beiträge zur Rentenversicherung sichern das spätere Alterseinkommen.", "年轻工作时每月足额缴纳的法定养老保险金构成了晚年有尊严生活的最硬核防线。"),
            ("die Arbeitslosenversicherung", "die", "n.", "-en", "失业社会救济保险体系", "Die Arbeitslosenversicherung springt bei unfreiwilligem Jobverlust ein.", "在遭遇非因自身意愿突遭辞退裁员失业时，失业保险金将如期托底维持生活运转。"),
            ("der Arbeitsvertrag", "der", "n.", "Arbeitsverträge", "劳动用工正式法律合同", "Vor dem ersten Arbeitstag unterschreiben beide Seiten den Arbeitsvertrag.", "在正式报到入职第一天之前，劳资双方将共同在厚实的劳动合同文本上签字盖章。"),
            ("befristet", "", "adj.", "", "附带固定履约期限有期限的", "Die Stelle ist zunächst als Elternzeitvertretung auf zwei Jahre befristet.", "作为产假期间的临时顶岗代班人员，该岗位起初暂定签署为期两年的固定期合同。"),
            ("unbefristet", "", "adj.", "", "无固定期限终身长期的", "Nach der Bewährungszeit winkt ein unbefristeter Festvertrag.", "只要在试用期内充分展现出业务担当与战力，迎接你的将是一张无固定期的铁饭碗。"),
            ("die Probezeit", "die", "n.", "-en", "试用考察考核期", "Die gesetzliche Probezeit beträgt im Betrieb meist sechs Monate.", "在德国企业中普遍依惯例约定为期半年的试用考察期，期间离职双向门槛极低。"),
            ("die Kündigungsfrist", "die", "n.", "-en", "解除劳动关系预先通知期", "Nach fünf Dienstjahren verlängert sich die Kündigungsfrist spürbar.", "伴随着工龄迈过五年大关，法定的解聘与辞职预先书面通知告知期将大幅拉长。"),
            ("die Kündigung", "die", "n.", "-en", "正式提出离职解约辞职", "Er reichte seine schriftliche Kündigung fristgerecht zum Monatsende ein.", "他在月底前严格依规向人事部呈递了附有本人亲笔签名的纸质正式辞职告知书。"),
            ("kündigen", "", "v.", "kündigt, kündigte, gekündigt", "炒鱿鱼解除雇佣；主动辞职", "Wegen grober Pflichtverletzung wurde dem Mitarbeiter fristlos gekündigt.", "因该名员工严重触犯商业道德底线违规，用人单位当机立断对其予以即时开除。"),
            ("die Abfindung", "die", "n.", "-en", "离职经济补偿金买断金", "Bei betriebsbedingter Kündigung verhandelte der Betriebsrat eine hohe Abfindung.", "面对经营性重大关停裁员，工会代表劳方据理力争为下岗员工争取到了巨额经济补偿。"),
            ("der Betriebsrat", "der", "n.", "Betriebsräte", "企业工会职工委员会", "Der Betriebsrat vertritt die Interessen der Belegschaft gegenüber der Chefetage.", "企业职工委员会挺身而出在管理层高管面前捍卫全体基层一线打工人的合法权益。"),
            ("die Gewerkschaft", "die", "n.", "-en", "全行业产业工会联合会", "Die Gewerkschaft ruft die Beschäftigten zum befristeten Warnstreik auf.", "产业工会联合会向全行业在册产业工人发出了举行为期一天的警告性大罢工号召。"),
            ("der Streik", "der", "n.", "-s", "停工大罢工维权行动", "Der tagelange Streik im Schienenverkehr legte viele Züge still.", "铁路系统持续数日的大罢工导致全德绝大多数长途旅客列车陷入停摆瘫痪。"),
            ("streiken", "", "v.", "streikt, streikte, gestreikt", "举行大罢工争取权益", "Die Piloten streiken für bessere Arbeitsbedingungen und höhere Tabellenlöhne.", "民航机长与飞行员群体愤而举行全线罢工，旨在争取更为合理的工时排班与涨薪。"),
            ("der Tarifvertrag", "der", "n.", "Tarifverträge", "全行业劳资集体谈判协议", "Der Tarifvertrag regelt Urlaubsanspruch, Arbeitszeit und Mindestlöhne bindend.", "全行业劳资集体协议对带薪年假天数、每周工时上限及行业底薪作出了刚性规约。"),
            ("die Arbeitszeit", "die", "n.", "-en", "每日工作工时规定", "Die wöchentliche Arbeitszeit beträgt laut Vereinbarung 38,5 Stunden.", "依双方合同条文规定，每周基准标准工时折合下来整整为三十八点五小时。"),
            ("die Gleitzeit", "die", "n.", "-", "弹性弹性上下班打卡制", "Dank Gleitzeit kann sie ihre Arbeitszeit flexibel an die Familie anpassen.", "得益于公司推行的人性化弹性打卡工时制，她能极其从容地平衡接送孩子与工作。"),
            ("die Kernarbeitszeit", "die", "n.", "-en", "必须在岗核心公干时段", "Während der Kernarbeitszeit von 10 bis 15 Uhr müssen alle erreichbar sein.", "在上午十点至下午三点这一核心在岗时段内，全体员工原则上必须保持全时在线。"),
            ("die Überstunde", "die", "n.", "-n", "超出法定工时之加班工时", "Er baut seine angesammelten Überstunden durch freie Tage ab.", "他将前期几个月攻坚硬仗累积攒下的多余加班工时逐步兑换为连休年假消化掉。"),
            ("der Urlaub", "der", "n.", "-e", "法定带薪年休假", "Der gesetzliche Mindesturlaub beträgt 20 Tage bei einer Fünf-Tage-Woche.", "在每周标准五天工作制下，德国法律所保障的法定最低带薪休假天数为二十天。"),
            ("der Urlaubsanspruch", "der", "n.", "Urlaubsansprüche", "受法律保护之年假权益", "Viele tarifgebundene Arbeitnehmer genießen 30 Tage Urlaubsanspruch im Jahr.", "许多受集体协议庇护的企业职工每年享有高达整整三十天的带薪法定年休假期。"),
            ("der Bildungsurlaub", "der", "n.", "-", "脱产带薪进修培训假期", "In den meisten Bundesländern haben Angestellte Recht auf Bildungsurlaub.", "在德国绝大多数联邦州，企业在职在编员工依法享有每年五天的脱产带薪进修假。"),
            ("die Weiterbildung", "die", "n.", "-en", "业务深造与职业再充电", "Lebensbegleitende Weiterbildung ist die beste Absicherung gegen Jobverlust.", "伴随一生的业务深造与持续知识更新，是对抗被时代洪流淘汰下岗的最佳铠甲。"),
            ("die Schulung", "die", "n.", "-en", "技能集训提升实操班", "Das Team besucht eine zweitägige Schulung zur Cybersicherheit.", "项目团队全员脱产参加了为期两天的网络数据安全攻防专题技能闭门提升集训。"),
            ("die Beförderung", "die", "n.", "-en", "职位官阶擢升升职晋升", "Nach dem erfolgreichen Projektabschluss winkt ihr eine wohlverdiente Beförderung.", "在主导的项目取得现象级辉煌大捷后，等待她的将是众望所归的职级薪酬大跃升。"),
            ("befördern", "", "v.", "befördert, beförderte, befördert", "提拔任用；运输运送", "Der Vorstand beschloss einstimmig, sie zur Prokuristin zu befördern.", "公司董事会开会全票通过重磅人事任命，决议擢升其为拥有签署权的集团副总裁。"),
            ("die Karriereleiter", "die", "n.", "-", "职场晋升阶梯升迁之路", "Er kletterte die Karriereleiter mit Fleiß und diplomatischem Geschick hinauf.", "他凭借常人莫及的勤勉与高超圆融的处世智慧一步一个脚印爬上了职场高阶权力榜。"),
            ("die Führungskraft", "die", "n.", "Führungskräfte", "大兵团管理高管管理者", "Eine moderne Führungskraft agiert als Mentor und Coach für ihr Team.", "一位优秀的当代高管领军者，更应当躬身充当整个团队的引路导师与成长教练。"),
            ("die Kompetenz", "die", "n.", "-en", "综合专业硬核胜任力", "Soziale Kompetenz ist ebenso erfolgsentscheidend wie fachliches Wissen.", "为人处世的情商与社交协作软实力，其重要性丝毫不亚于纯业务层面的硬技能。"),
            ("die Selbstständigkeit", "die", "n.", "-", "自主创业独当一面单干", "Der mutige Schritt in die berufliche Selbstständigkeit barg erhebliche Risiken.", "辞别大厂旱涝保收的温床断然迈向自主创业之路，虽然暗流涌动却也充满无限可能。"),
            ("selbstständig", "", "adj.", "", "自由职业独立创业的", "Seit drei Jahren arbeitet sie als selbstständige Software-Architektin.", "三年前她便选择彻底独立单干，作为高薪自由执业者承接各跨国大厂系统架构。"),
            ("das Start-up", "das", "n.", "-s", "初创科技型研发企业", "Das Berliner Start-up sicherte sich eine Millionenförderung von Investoren.", "这家脱胎自柏林高校实验室的AI初创企业成功斩获了硅谷头部风投的千万级融资。"),
            ("der Gründer", "der", "n.", "-", "创办发起人创始人", "Die visionären Gründer revolutionierten mit ihrer Plattform den Markt.", "这两位极具前瞻战略眼光的极客创始团队成员用其平台彻底重塑了整个行业版图。"),
            ("die Gründerin", "die", "n.", "-nen", "女性创业领袖创始人", "Die Gründerin wurde als Unternehmerin des Jahres feierlich ausgezeichnet.", "这位勇于破局的青年女性创业领袖在年终风云人物盛典上荣膺年度最佳企业家。"),
            ("das Unternehmen", "das", "n.", "-", "现代化商业企业实体", "Das mittelständische Familienunternehmen beschäftigt weltweit 2.000 Menschen.", "这家深耕实体经济的隐形冠军中型家族企业在全球多地工厂吸纳了两千名员工。"),
            ("der Erfolg", "der", "n.", "-e", "大功告成取得重大突破", "Harte Vorbereitung im Vorfeld ist das Geheimnis für den beruflichen Erfolg.", "在一切大战拉开帷幕前潜心做好极致充分的暗中准备，是斩获一切大胜的底层秘密。"),
            ("die Zufriedenheit", "die", "n.", "-", "职业与生活满意度", "Hohe Arbeitszufriedenheit senkt die Fluktuation im Betrieb.", "极高的员工工作满意度能够显著降低企业的离职率。")
        ]
    },

    # LESSON 4
    {
        "id": "B1_L04",
        "title": "第4课：现代居住形态、租房法与社区治理 (Wohnformen & Mietrecht)",
        "summary": "掌握第二格介词 (während, wegen, trotz, statt)、德国租客保护法、合租房(WG)与邻里纠纷调解",
        "grammar": {
            "title": "四大支配第二格 (Genitiv) 的核心介词",
            "sections": [
                {
                    "heading": "1. 四大高频第二格介词 (während, wegen, trotz, statt)",
                    "content": "• während des Studiums (在求学期间)\n• wegen des schlechten Wetters (因为坏天气)\n• trotz des hohen Preises (尽管价格昂贵)\n• statt eines Briefes (代替一封信，以邮件形式)\n注意：阳性/中性名词词尾补加 -(e)s！"
                },
                {
                    "heading": "2. 口语中替代方案 (von / Dativ) 与正式书面语区别",
                    "content": "书面语和歌德考试写作必须严格使用第二格 Genitiv 以体现语言水准！"
                }
            ]
        },
        "quiz": [
            {
                "id": "B1_L04_Q1",
                "type": "GRAMMAR_FILL",
                "question": "______ (während, 支配第二格) des Sommers wohnte er in einer WG in Hamburg.",
                "options": ["Während", "Wegen", "Trotz", "Statt"],
                "correctIndex": 0,
                "explanation": "表达在...时间跨度期间，使用第二格介词 Während des Sommers。"
            },
            {
                "id": "B1_L04_Q2",
                "type": "VOCAB_MEANING",
                "question": "德国著名的特色青年居住形式 'die WG'（Wohngemeinschaft）是指：",
                "options": ["多人各住单间、共用厨卫的合租公寓", "老年人专属养老院", "一人独居独栋别墅", "酒店长租客房"],
                "correctIndex": 0,
                "explanation": "die Wohngemeinschaft (WG) 是德语区年轻人最经典的合租形态：每人一间独立卧室，共用厨房卫浴。"
            }
        ],
        "words": [
            ("die Wohnform", "die", "n.", "-en", "多样化居住生活形态", "Flexible Wohnformen gewinnen bei jungen Stadtbewohnern an Beliebtheit.", "多元灵活的新型居住生活形态在当代年轻都市青年群体中正蔚然成风。"),
            ("die Wohngemeinschaft", "die", "n.", "-en", "多人合租生活公寓(WG)", "In einer studentischen Wohngemeinschaft teilt man sich Miete und Küche.", "在一间温馨的大学生合租公寓里，室友们分摊昂贵房租并共享厨房客厅。"),
            ("die WG", "die", "n.", "-s", "合租公寓（日常口语统称）", "Ich bin vor zwei Monaten in eine gemütliche 3er-WG gezogen.", "两个月前我搬进了一套三室一厅、三位好友同住的其乐融融合租公寓。"),
            ("der Mitbewohner", "der", "n.", "-", "同住一屋檐下合租室友", "Mein Mitbewohner kümmert sich immer zuverlässig um den Putzplan.", "我的合租室友总是极其靠谱负责地带头把值日清扫排期打理得井井有条。"),
            ("die Mitbewohnerin", "die", "n.", "-nen", "女性合租生活室友", "Meine Mitbewohnerin kocht am Wochenende gerne für die ganze WG.", "我的女室友每逢周末都很乐意系上围裙为全屋所有室友精心烹制大餐。"),
            ("das WG-Casting", "das", "n.", "-s", "合租室友集体线下面试试选", "Beim WG-Casting lernt man potenzielle neue Mitbewohner persönlich kennen.", "在合租室友集体线下面试选拔中，老住客借此深度考察候选人的脾气秉性。"),
            ("das Wohnheim", "das", "n.", "-e", "大学配建大学生集体宿舍", "Das Studentenwohnheim liegt in unmittelbarer Nähe zur Universitätsbibliothek.", "由高校后勤服务集团统建的学生公寓坐落在紧挨中央图书馆的黄金地段。"),
            ("das Appartement", "das", "n.", "-s", "单人独享精品独立小公寓", "Ein voll möbliertes Ein-Zimmer-Appartement mit Pantry-Küche.", "一间配备全套高档品牌家具家电、自带独立微型开放式小厨卫的单身公寓。"),
            ("das Studio", "das", "n.", "-s", "无隔断大开间艺术公寓", "Er richtete sich ein helles Studio mit großem Atelier im Dachgeschoss ein.", "他在顶楼跃层给自己精心布置了一间采光绝佳、连带宽敞大画室的艺术开间。"),
            ("das Mehrgenerationenhaus", "das", "n.", "-häuser", "三代同堂多世代共融居所", "Im Mehrgenerationenhaus helfen Senioren und junge Familien einander.", "在多世代老幼共融示范社区大楼里，古稀长者与年轻育儿家庭互帮互助。"),
            ("das Betreute Wohnen", "das", "n.", "-", "适老化受照护医养公寓", "Viele ältere Menschen wählen betreutes Wohnen für mehr Sicherheit im Alter.", "许多高龄老人为了晚年起居拥有二十四小时紧急医疗照护而入住医养公寓。"),
            ("das Altenheim", "das", "n.", "-e", "专业医护常驻养老院", "Die Pflegefachkräfte im Altenheim leisten täglich schwere Arbeit.", "长驻养老护理院的一线专业护理人员日复一日承担着极其繁重的照料劳作。"),
            ("das Pflegeheim", "das", "n.", "-e", "失能重度失能特护疗养院", "Auf der Spezialstation des Pflegeheims werden Demenzpatienten versorgt.", "在专业特护院的封闭专护病区，医护团队细致入微地照管着阿尔茨海默病患。"),
            ("die Eigentumswohnung", "die", "n.", "-en", "拥有完全产权的私产商品房", "Der Kauf einer eigenen Eigentumswohnung dient der Altersvorsorge.", "咬牙按揭购置一套属于自己的完全产权商品住宅，是极稳妥的晚年抗通胀资产。"),
            ("das Wohneigentum", "das", "n.", "-", "自主个人房屋不动产私产", "Die Schaffung von Wohneigentum wird durch zinsgünstige Kredite gefördert.", "国家金融财税部门出台贴息低息房贷新政，大力扶持刚需工薪阶层购房置业。"),
            ("die Immobilie", "die", "n.", "-n", "土地附着不动产房产", "Investitionen in hochwertige Immobilien gelten als krisenfester Sachwert.", "投资核心地段的高品质优质不动产历来被公认为对抗金融海啸的硬核资产。"),
            ("der Quadratmeterpreis", "der", "n.", "-e", "单位平米房屋买卖单价", "Der durchschnittliche Quadratmeterpreis in München hat Rekordhöhen erreicht.", "慕尼黑核心城区的每平米房屋销售均价已飙升至屡破历史极值的惊人高位。"),
            ("die Gentrifizierung", "die", "n.", "-", "老旧城区中产阶级化贵族化", "Kritiker warnen vor der rasanten Gentrifizierung historischer Arbeiterviertel.", "城市社会学家敲响警钟，呼吁警惕传统产业工人聚居区遭资本狂暴贵族化。"),
            ("die Verdrängung", "die", "n.", "-", "租金倒逼原住民被迫迁离", "Steigende Mieten führen zur schleichenden Verdrängung einkommensschwacher Bürger.", "暴涨的租金不可避免地导致原本在此世居的低收入底层原住民被迫搬离主城。"),
            ("der Mietspiegel", "der", "n.", "-e", "官方公允基准指导租金谱系", "Der amtliche Mietspiegel begrenzt überzogene Mieterhöhungen im Bestand.", "市政当局发布的法定义务基准租金指导标准有力遏制了房东肆意单方面暴涨房租。"),
            ("die Mietpreisbremse", "die", "n.", "-n", "法定义务房租涨幅封顶刹车", "Die gesetzliche Mietpreisbremse soll bezahlbaren Wohnraum sichern.", "国家出台严苛的房租刚性限涨刹车令，旨在捍卫普通百姓能够承受的居住权。"),
            ("der Mieterverein", "der", "n.", "-e", "地方租客公益维权互助协会", "Der Deutsche Mieterverein berät Mitglieder bei juristischen Streitigkeiten.", "德国租户维权协会为在册会员就各类租房合同陷阱与维权诉讼提供免费法援。"),
            ("der Mieterschutz", "der", "n.", "-", "国家法定承租人倾斜保护制度", "Der Mieterschutz hat in Deutschland historisch einen sehr hohen Stellenwert.", "保护弱势承租人的法定制度在德国民法典与立法体系中享有极其崇高的地位。"),
            ("das Mietrecht", "das", "n.", "-", "房屋租赁相关民事法条体系", "Ein Fachanwalt für Mietrecht klärt komplizierte Fragen zur Nebenkostenabrechnung.", "一名专攻房屋租赁纠纷的资深诉讼律师条分缕析厘清了物业杂费账单漏洞。"),
            ("der Mietvertrag", "der", "n.", "Mietverträge", "房屋租赁约束性民事合同", "Ein unbefristeter Mietvertrag bietet Mietern ein Höchstmaß an Stabilität.", "一份没有附加期限限制的长约租房协议赋予了租客遮风避雨的最大安全感。"),
            ("die Klausel", "die", "n.", "-n", "合同内附具体细则条款", "Ungültige Klauseln im Mietvertrag benachteiligen den Mieter einseitig.", "租房合同中隐藏的霸王霸王条款往往单方面侵害了租客依法享有的知情权。"),
            ("die Kaution", "die", "n.", "-en", "法定上限三个月租金押金", "Die Kaution darf maximal drei monatliche Kaltmieten betragen.", "法律明文严令规定：房东向承租人预先收取的租房押金上限严禁超过三月净租。"),
            ("das Kautionskonto", "das", "n.", "Kautionskonten", "银行设立的押金共管托管专户", "Die Mietkaution wird insolvenzsicher auf einem Kautionskonto angelegt.", "租客缴纳的押金必须依法存入专设的银行破产隔离共管托管账户生息。"),
            ("die Warmmiete", "die", "n.", "-n", "供暖物业杂费全包月租金", "Die monatliche Warmmiete überweist er pünktlich zum dritten Werktag.", "每逢月初第三个银行营业日之前，他总会雷打不动准时转账汇出全包暖租。"),
            ("die Kaltmiete", "die", "n.", "-n", "不含任何附加能源之净基准租", "Die vertraglich festgeschriebene Kaltmiete beträgt 800 Euro netto.", "租约文本中白纸黑字盖章锁定的净基准基础租金经核算整整为八百欧元。"),
            ("die Nebenkosten", "die", "n.pl.", "-", "大楼物业能源杂费附加摊派", "Die gestiegenen Nebenkosten für Heizung und Warmwasser belasten das Budget.", "由于国际大宗天然气能源暴涨导致的暖气杂费飙升严重挤占了家庭开支预算。"),
            ("die Abrechnung", "die", "n.", "-en", "年度能耗物业分摊核算决算", "Die jährliche Nebenkostenabrechnung muss dem Mieter fristgerecht zugehen.", "上一自然年度的供暖能耗细化决算清单必须依法在次年年底前寄达承租人。"),
            ("die Nachzahlung", "die", "n.", "-en", "年终清算后的差额补缴款项", "Wegen des strengen Winters fordert der Vermieter eine Nachzahlung von 300 Euro.", "由于去年严冬酷寒导致取暖用量剧增，房东寄来了一纸补缴三百欧差额的账单。"),
            ("das Guthaben", "das", "n.", "-", "预缴多退少补结余资金额度", "Dank sparsamen Heizverhaltens wies die Abrechnung ein schönes Guthaben auf.", "得益于平日随手调低温控阀节约供暖，决算清单上赫然显示出一笔可观退费。"),
            ("die Mieterhöhung", "die", "n.", "-en", "房东依法提出的房租递增涨价", "Eine rechtmäßige Mieterhöhung muss formell korrekt begründet werden.", "一纸具有法律效力的涨房租通告必须在实体要件与程序形式上均经得起严查。"),
            ("die Kündigung", "die", "n.", "-en", "解除房屋租赁关系通知文书", "Eine Kündigung des Mietverhältnisses durch den Vermieter bedarf triftiger Gründe.", "房东若想单方面依法解除房屋租赁关系，必须依法出示法律认可的重大刚性事由。"),
            ("der Eigenbedarf", "der", "n.", "-", "房东直系亲属自住刚需收房", "Der Vermieter kündigte die Wohnung wegen dringenden Eigenbedarfs für seinen Sohn.", "房东以自己的亲生骨肉大学毕业返乡成家急需收回房屋自住为由下达收房令。"),
            ("die Räumungsklage", "die", "n.", "-n", "法院诉请强制腾退腾房诉讼", "Der Eigentümer reichte vor dem Amtsgericht eine Räumungsklage ein.", "因屡遭无理拖欠严重租金，业主无奈之下向属地初级法院提起了强制搬迁诉讼。"),
            ("die Frist", "die", "n.", "-en", "法定恪守之履行期限时限", "Die dreimonatige Kündigungsfrist ist von beiden Vertragspartnern zu wahren.", "长达三个月的法定法定解除租约预先通知时限，买卖租赁双方均须严格恪守。"),
            ("der Mangel", "der", "n.", "Mängel", "房屋设施受损出现的瑕疵隐患", "Der Mieter muss gravierende Mängel der Wohnung unverzüglich anzeigen.", "一旦发现房屋存在水管爆裂或屋顶漏水等严重瑕疵隐患，租客必须即刻报修。"),
            ("die Mängelanzeige", "die", "n.", "-n", "向房东正式呈递的书面报修单", "Mit der schriftlichen Mängelanzeige forderte er die zügige Beseitigung des Schimmels.", "通过亲笔挂号寄出的书面报修函，租客义正辞严限期敦促对方根除墙壁黑霉。"),
            ("die Mietminderung", "die", "n.", "-en", "因设施故障依法行使租金克减", "Bei einem totalen Heizungsausfall im eiskalten Winter steht dem Mieter Mietminderung zu.", "数九寒冬遭遇大楼暖气机组彻底瘫痪彻底断供，租客依法享有拒付扣减租金权利。"),
            ("der Schimmel", "der", "n.", "-", "墙壁潮湿孳生的有毒黑霉斑", "Schimmel an den Wänden stellt ein ernsthaftes Gesundheitsrisiko für Asthmatiker dar.", "内墙阴暗角落密布的有毒黑霉孢子对于哮喘与易感人群构成了致命健康隐患。"),
            ("lüften", "", "v.", "lüftet, lüftete, gelüftet", "开窗通风彻底换气", "Regelmäßiges Stoßlüften verhindert die Entstehung von gefährlichem Schimmel.", "坚持每天数次将全屋窗户彻底敞开对流五分钟，能从根本上阻绝霉菌的孳生。"),
            ("das Stoßlüften", "das", "n.", "-", "全开窗对流冲击式强效换气", "Zweimal tägliches Stoßlüften sorgt für frischen Sauerstoff und senkt Feuchtigkeit.", "早晚各进行一次短促而彻底的穿堂风开窗通风，既补充富氧又大幅驱散湿气。"),
            ("die Feuchtigkeit", "die", "n.", "-", "室内相对空气湿度潮气", "Zu hohe Feuchtigkeit in den Schlafräumen begünstigt Pilzwachstum.", "卧室内部空气相对湿度若长期超标高居不下，将极大催生肉眼难辨的真菌滋生。"),
            ("die Hausordnung", "die", "n.", "-en", "大楼公约住户行为共同守则", "Die Hausordnung untersagt ruhestörenden Lärm während der Mittagsstunden.", "大楼业主公约明文严厉禁绝在午休静息时段内实施任何敲打电钻等扰民噪运行为。"),
            ("die Ruhezeit", "die", "n.", "-en", "全楼法定免打扰静息时段", "Während der gesetzlichen Ruhezeiten zwischen 22 und 6 Uhr darf keine laute Musik laufen.", "在入夜二十二点至次日清晨六点的法定全楼静息期内，严禁将音响低音炮开大。"),
            ("die Nachtruhe", "die", "n.", "-", "神圣不可侵犯之夜间安宁", "Bei beharrlicher Störung der Nachtruhe kann die Polizei wegen Ruhestörung gerufen werden.", "若隔壁邻舍在深更半夜屡遭劝阻仍顽固狂欢扰民，居民有权直接报警传唤治安警。"),
            ("der Lärm", "der", "n.", "-", "刺耳喧嚣有害噪音", "Anhaltender Straßenlärm vor dem Schlafzimmerfenster verursacht dauerhaften Stress.", "卧榻窗外车水马龙终日不绝于耳的高分贝交通噪音会导致机体长期的神经衰弱。"),
            ("die Lärmbelästigung", "die", "n.", "-en", "侵犯公民安宁权的噪音骚扰", "Wiederholte Lärmbelästigung durch bellende Hunde kann zur Abmahnung führen.", "因放任家养烈犬在深更半夜无休止狂吠对邻里造成的恶劣噪音滋扰将招致警告。"),
            ("die Abmahnung", "die", "n.", "-en", "用人单位或房东出具的书面警告函", "Nach der zweiten schriftlichen Abmahnung droht die fristlose Kündigung der Wohnung.", "在相继收到两封言辞激烈的正式红头警告函后，租客将直接面临被强行扫地出门。"),
            ("der Nachbarschaftsstreit", "der", "n.", "-e", "左邻右舍邻里边界纠纷争端", "Banaler Nachbarschaftsstreit um überhängende Baumäste landete vor Gericht.", "因院落篱笆边缘越界伸展出的一截果树枝桠引发的恶性邻里争端最终闹上法庭。"),
            ("das Schiedsgericht", "das", "n.", "-e", "民间纠纷调解仲裁法庭机构", "Ein unparteiisches Schiedsgericht schlichtete den Konflikt einvernehmlich und zügig.", "一个居中持平客观公允的民间睦邻调解仲裁所快刀斩乱麻促成了双方握手言和。"),
            ("der Schiedsmann", "der", "n.", "Schiedsleute", "社区德高望重纠纷调解员", "Der ehrenamtliche Schiedsmann fand eine für beide Seiten tragbare Lösung.", "这位在社区德高望重、不取分文的公益调解老爷爷为两家拿出了互有体面的方案。"),
            ("schlichten", "", "v.", "schlichtet, schlichtete, geschlichtet", "居中说和，平息争端", "Der Schiedsmann half den Streitenden, den Nachbarschaftskonflikt gütlich zu schlichten.", "在调解员动之以情晓之以理的苦口婆心规劝下，宿怨已深的两家人终于化干戈为玉帛。"),
            ("die Schlichtung", "die", "n.", "-en", "矛盾纠纷非诉说和调停机制", "Eine außergerichtliche Schlichtung spart beiden Parteien Zeit, Nerven und Gerichtsgebühren.", "通过非诉调解渠道平息纷争能替对抗各方极大节约高昂的诉讼律师费与精力损耗。"),
            ("die Gemeinschaft", "die", "n.", "-en", "大楼业主睦邻命运共同体", "Eine funktionierende Hausgemeinschaft hilft sich gegenseitig bei der Paketannahme.", "一个和谐有爱、守望相助的大楼邻里集体，邻里间总会毫无芥蒂帮彼此代收快递。"),
            ("die Hausverwaltung", "die", "n.", "-en", "大楼常年签约职业物业公司", "Die Hausverwaltung organisiert den Winterdienst und die Treppenhausreinigung.", "受聘的大楼职业物业管理公司统筹负责门前道路除雪融冰及公共楼道的专业保洁。"),
            ("der Hausmeister", "der", "n.", "-", "全天候常驻大楼物业工程管家", "Der Hausmeister kümmert sich zuverlässig um Mülltonnen, Heizung und Schließanlagen.", "常驻小区的万能工程大管家兢兢业业监管着垃圾分类转运、锅炉运行与电子门禁。"),
            ("die Renovierung", "die", "n.", "-en", "老房腾退全要素装修与修缮", "Beim Auszug verlangt der Vermieter eine fachgerechte Renovierung der Wände.", "按旧规在退租交房时，业主往往要求前任房客履行对室内发黄墙面专业粉刷义务。"),
            ("die Schönheitsreparatur", "die", "n.", "-en", "法定义务常规表面墙漆小修补", "Starre Fristenpläne für Schönheitsreparaturen wurden vom Bundesgerichtshof gekippt.", "联邦最高法院做出划时代判例，彻底废除了早先强加在租客头上死板的小修条款。"),
            ("streichen", "", "v.", "streicht, strich, gestrichen", "用滚筒粉刷墙面，油漆", "Vor der Schlüsselübergabe strich er alle Zimmer sorgfältig mit weißer Dispersionsfarbe.", "在正式将钥匙当面回交物业前，他一丝不苟地将所有房间用雪白环保乳胶漆滚刷一新。"),
            ("die Übergabe", "die", "n.", "-en", "房屋当面勘验清点交割交房", "Bei der Wohnungsübergabe wird der genaue Zustand detailliert protokolliert.", "在办理交房验房的庄重交接现场，房屋目力所及的全部细部品相均被拍照笔录。"),
            ("das Übergabeprotokoll", "das", "n.", "-e", "房屋移交书面现场勘验记录单", "Halten Sie alle bestehenden Vorschäden penibel im Übergabeprotokoll fest!", "请务必将进驻前早已存在的细微划痕与历史暗疾全数巨细靡遗写进现场移交验房单！"),
            ("der Zählerstand", "der", "n.", "Zählerstände", "水电气表原始底数度数读数", "Notieren Sie am Tag des Einzugs die Zählerstände für Strom, Wasser und Gas!", "在拎包入住大吉当日，第一时间拍照并记下入户电表、水表及燃气表的底数读数！"),
            ("der Schlüssel", "der", "n.", "-", "入户大门机械或磁控原装钥匙", "Verlorene Sicherheitsschlüssel können den teuren Austausch der gesamten Schließanlage erfordern.", "如果不慎遗失了特种防盗防撬子母钥匙，很可能招致自掏腰包更换整栋大楼门禁总锁。"),
            ("die Wohnqualität", "die", "n.", "-", "综合人居宜居生活品质质量", "Ein begrünter Innenhof steigert die Wohnqualität der Mieter spürbar.", "推窗见绿、鸟语花香的花园内庭院能立竿见影大幅提升全体住客的人居幸福感。"),
            ("das Zuhause", "das", "n.", "-", "温暖港湾精神寄托之避风港家", "Ein liebevoll eingerichtetes Zuhause schenkt Geborgenheit und Ruhe nach harter Arbeit.", "一个用心精心装点打理的温馨港湾，能让归客在结束繁重奔波后收获无尽踏实与温存。"),
            ("die Geborgenheit", "die", "n.", "-", "踏实安详由内而生的安全感", "In den eigenen vier Wänden sucht der Mensch Schutz, Wärme und Geborgenheit.", "在属于自己的这一方遮风挡雨天地里，每个游子都能觅得至深的精神慰藉与安详。")
        ]
    },

    # LESSON 5
    {
        "id": "B1_L05",
        "title": "第5课：深度环球旅行、跨文化交际与文化休克 (Reisen & Interkulturalität)",
        "summary": "掌握第二虚拟式过去时 (hätte/wäre + Partizip II)、跨文化交际禁忌与文化休克阶段论",
        "grammar": {
            "title": "第二虚拟式过去时 (Konjunktiv II der Vergangenheit) 与跨文化反思",
            "sections": [
                {
                    "heading": "1. 表达对过去未发生事实的悔恨与假想 (hätte / wäre + Partizip II)",
                    "content": "• wäre + Partizip II (位移/状态变化)：Wenn ich früher losgefahren wäre, hätte ich den Flug nicht verpasst.\n• hätte + Partizip II (及物/大多数动词)：Hätte ich mich besser informiert, wäre das Missverständnis nicht passiert."
                },
                {
                    "heading": "2. 文化休克四阶段 (Der Kulturschock in vier Phasen)",
                    "content": "1. Honeymoon-Phase (蜜月期好奇)\n2. Krisenphase / Kulturschock (矛盾震荡期)\n3. Erholungsphase (适应调整期)\n4. Anpassung / Bulturalität (双文化融入成熟期)"
                }
            ]
        },
        "quiz": [
            {
                "id": "B1_L05_Q1",
                "type": "GRAMMAR_FILL",
                "question": "Wenn ich das gewusst ______ (haben, 第二虚拟式过去时), wäre ich vorsichtiger gewesen.",
                "options": ["hätte", "hatte", "habe", "gehabt"],
                "correctIndex": 0,
                "explanation": "对过去的假想，助动词 haben 的第二虚拟式形式为 hätte (gewusst hätte)。"
            },
            {
                "id": "B1_L05_Q2",
                "type": "VOCAB_MEANING",
                "question": "跨文化交际学中极核心的概念 'der Kulturschock' 意思是：",
                "options": ["文化休克，异域文化冲击", "文化大革命", "被闪电电击", "文化遗产保护"],
                "correctIndex": 0,
                "explanation": "der Kulturschock 指人踏入崭新异质文化环境时因价值观碰撞而产生的不适、震荡与困惑。"
            }
        ],
        "words": [
            ("die Fernreise", "die", "n.", "-n", "跨大洲长途深度环球旅行", "Eine Fernreise nach Asien verlangt sorgfältige Vorbereitung und Impfungen.", "前往远隔重洋的亚洲开展长途深度游，必须提前数月周密谋划并接种疫苗。"),
            ("das Abenteuer", "das", "n.", "-", "惊险跌宕的异域冒险探险", "Die Reise abseits ausgetretener Pfade wurde zu einem unvergesslichen Abenteuer.", "告别千篇一律的游人如织打卡路线，深入秘境之旅演变为终生难忘的探险。"),
            ("der Weltenbummler", "der", "n.", "-", "走南闯北见多识广的旅行家", "Als unermüdlicher Weltenbummler hat er bereits über achtzig Staaten bereist.", "作为一名不知疲倦的环球行者，他的足迹已深深刻在八十余个主权国家的土地上。"),
            ("die Weltoffenheit", "die", "n.", "-", "包容天下海纳百川的世界眼光", "Weltoffenheit und Neugier sind die besten Begleiter für jeden Reisenden.", "海纳百川的天下情怀与对未知的热忱好奇，是每位四海旅人行囊中最珍贵的向导。"),
            ("der Kulturschock", "der", "n.", "-s", "跨文化碰撞震荡之文化休克", "Der plötzliche Kulturschock traf ihn in den ersten Wochen im fremden Land unerwartet.", "初来乍到身处异国他乡的前几个星期，突如其来的文化休克令他一度感到手足无措。"),
            ("die Interkulturalität", "die", "n.", "-", "多元文化跨文化交融性", "Interkulturalität bedeutet den Dialog und das gegenseitige Lernen auf Augenhöhe.", "跨文化交融的精髓在于不同文化主体在平等尊重的基准线上彼此对话、互学互鉴。"),
            ("interkulturell", "", "adj.", "", "跨越不同文化文明维度的", "Interkulturelle Kompetenz ist in multinationalen Konzernen eine Schlüsselqualifikation.", "具备高水准的跨文化协同交往素养，是跨国集团选拔国际化高管的硬核考核项。"),
            ("die Kompetenz", "die", "n.", "-en", "处变不惊跨文化驾驭素养", "Kulturelle Sensibilität und kommunikative Kompetenz verhindern fatale Missverständnisse.", "深沉敏锐的文化体察力与高超的外交沟通素养能有效化解致命的战略误判。"),
            ("die Sensibilität", "die", "n.", "-", "体察入微之敏锐同理洞察力", "Im Umgang mit religiösen Bräuchen ist höchste Sensibilität geboten.", "在面对异域源远流长的宗教禁忌与岁时习俗时，必须抱持最崇高的敏感与敬畏。"),
            ("das Stereotyp", "das", "n.", "-en", "先入为主刻板定型化成见", "Reisen hilft wirksam dabei, unreflektierte Stereotype im Kopf abzubauen.", "亲自走出国门迈向远方，是打碎脑海中那些未经审视的刻板刻板成见的最猛良药。"),
            ("das Vorurteil", "das", "n.", "-e", "未经深究的偏狭偏见成见", "Wer fremde Kulturen vor Ort erlebt, überwindet rasch vorgefasste Vorurteile.", "唯有亲身沉浸式感受原汁原味异域人文，方能迅速跨越无知催生的狭隘偏见。"),
            ("das Klischee", "das", "n.", "-s", "陈腔滥调刻板符号脸谱化", "Deutsche Trinken nur Bier - dieses Klischee wird der Realität längst nicht gerecht.", "所谓德国人只喝啤酒这一老掉牙的符号化脸谱陈词滥调，早已不符合当今现实。"),
            ("die Sitte", "die", "n.", "-n", "深入骨髓的风土习惯规约", "Vor dem Betreten des Tempels zieht man aus Respekt vor der Sitte die Schuhe aus.", "在踏入庄严静谧的古刹庙宇山门前，出于恪守当地古礼仪轨必须恭敬脱下鞋履。"),
            ("der Brauch", "der", "n.", "Bräuche", "代代相沿民间节日风俗", "Ein uralter Brauch besagt, dass Fremde stets als Gäste willkommen zu heißen sind.", "当地相沿成习的一则古老遗风谆谆教诲世人：远道而来的行者皆应作为贵客款待。"),
            ("das Tabu", "das", "n.", "-s", "碰不得的社会禁忌红线", "In manchen Ländern gilt es als striktes Tabu, den Kopf eines Kindes zu berühren.", "在部分特定国度与地区，用手随意抚摸摩挲儿童的头部被视作极其严重的社交禁忌。"),
            ("die Gepflogenheit", "die", "n.", "-en", "约定俗成日常惯例行为举止", "Informieren Sie sich vor der Abreise über die geschäftlichen Gepflogenheiten im Zielland!", "在启程奔赴异国公干前，务必全方位吃透东道国商务谈判桌上的约定俗成潜规则！"),
            ("das Fettnäpfchen", "das", "n.", "-", "因冒失失礼踩中的社交雷区", "Wer unvorbereitet verhandelt, tritt leicht in ein peinliches diplomatisches Fettnäpfchen.", "若事前不做功课便贸然登台交锋，极容易在无知中一脚踩中令人尴尬的社交大雷区。"),
            ("die Gastfreundschaft", "die", "n.", "-", "宾至如归倾囊相授好客之道", "Die überwältigende Gastfreundschaft der einheimischen Nomadenfamilie rührte ihn zu Tränen.", "游牧家庭萍水相逢却倾其所有杀羊备宴的质朴热诚好客之道，感动得他热泪盈眶。"),
            ("der Gastgeber", "der", "n.", "-", "招待远客的男主人东道主", "Der aufmerksame Gastgeber bot dem durstigen Wanderer kühlen Minztee an.", "体贴周到的东道主立即端上一大碗浮着冰块与新鲜薄荷嫩叶的甘洌清茶为旅人解渴。"),
            ("die Gastgeberin", "die", "n.", "-nen", "热情洋溢照料周全女主人", "Die Gastgeberin verwöhnte die Reisenden mit traditionellen landestypischen Gerichten.", "女主人使出看家本领，用一道道地道正宗的民族家常佳肴款待这几位远涉重洋的客人。"),
            ("der Einheimische", "der", "n.", "-n", "土生土长生于斯长于斯原住民", "Tipps von Einheimischen führen oft zu den spektakulärsten unberührten Naturwundern.", "多方虚心请教土生土长的当地老乡，往往能指引你探寻到地图未标明的绝美世外桃源。"),
            ("die Mentalität", "die", "n.", "-en", "深入骨髓的国民心智性格", "Die mediterrane Mentalität ist geprägt von Gelassenheit, Spontaneität und Lebensfreude.", "地中海沿岸原住民身上流淌的心智性格，无处不散发着云淡风轻、从容豁达与乐天。"),
            ("die Verhaltenskodex", "der", "n.", "-kodizes", "公开自律的文明行为规范", "Ein respektvoller Verhaltenskodex schützt sensible Ökosysteme und indigene Völker.", "恪守文明生态旅游行为准则，才能真正有效护佑脆弱的自然生境与原住民生活方式。"),
            ("der Respekt", "der", "n.", "-", "对神圣异质文明由衷敬畏", "Begegnen Sie der fremden Lebensweise mit aufrichtigem Respekt und Zurückhaltung!", "在直面截然迥异的异国生存图景时，请务必怀揣由衷的敬意与克制的谦恭审视！"),
            ("die Anpassung", "die", "n.", "-en", "入乡随俗适者生存适应期", "Die schrittweise Anpassung an das ungewohnte tropische Klima erforderte viel Geduld.", "身体与作息逐步调适顺应湿热难耐的热带季风气候，需要历经长达数周的耐受。"),
            ("anpassen", "", "v.", "passt an, passte an, angepasst", "入乡随俗，主动调适自我", "Reisende sollten sich den lokalen Kleidervorschriften und Verhaltensnormen anpassen.", "出门在外的背包客应当明智尊重当地关于着装严实程度与言谈举止的公序良俗。"),
            ("das Heimweh", "das", "n.", "-", "魂牵梦萦催人泪下的想家病", "Trotz all der exotischen Eindrücke überkam ihn abends quälendes Heimweh.", "尽管窗外异域风情旖旎万千，每当暮色四合他心中仍难免泛起阵阵揪心的思乡之情。"),
            ("die Einsamkeit", "die", "n.", "-", "天地辽阔唯我一人的孤寂感", "Die Einsamkeit in der endlosen Weite der Sahara-Wüste lehrte ihn Demut.", "孑然一人置身于茫茫无际、死一般沉寂的撒哈拉大沙漠深处，让他彻底学会了谦卑。"),
            ("die Isolation", "die", "n.", "-", "语言不通造成的隔绝孤立感", "Ohne grundlegende Sprachkenntnisse droht im Alltag die soziale Isolation.", "若在异国连哪怕最基础的生活口语对话都无法掌握，极易在日常中沦为孤岛孤立。"),
            ("die Sprachbarriere", "die", "n.", "-n", "语言沟通不畅横亘之语障", "Mit Gestik, Mimik und einem Lächeln überwindet man selbst hohe Sprachbarrieren.", "借助夸张生动的手势、真诚丰富的面部表情与善意微笑，再高耸的语言壁垒也能融化。"),
            ("die Verständigung", "die", "n.", "-en", "心领神会跨越阻隔达成沟通", "Die Verständigung mit Händen und Füßen funktionierte überraschend reibungslos.", "靠着连说带比画、手脚并用的肢体语言沟通，双方意图的传递竟出奇的顺畅无碍。"),
            ("die Gebärde", "die", "n.", "-n", "肢体语言手势手印符号", "Bestimmte Handgebärden haben in unterschiedlichen Kulturen völlig gegensätzliche Bedeutungen.", "某些司空见惯的手势语言在不同文化语境下所承载的含义甚至完全南辕北辙相反。"),
            ("die Körpersprache", "die", "n.", "-n", "潜意识流露的身体语言", "Körpersprache verrät Emotionen oft ehrlicher und unmittelbarer als geschliffene Worte.", "微妙的肢体体态语言往往比精心雕琢推敲的客套词藻更为真实直接地泄露内心真实。"),
            ("der Blickkontakt", "der", "n.", "-e", "四目相对眼神交流规矩", "Dauerhafter Blickkontakt wird in manchen asiatischen Kulturen als unhöflich empfunden.", "在部分东亚传统礼制文化圈中，长时间直勾勾死盯对方眼睛被视作不敬与冒犯。"),
            ("die Distanz", "die", "n.", "-en", "人际相处物理心理社交安全距离", "Das persönliche Bedürfnis nach räumlicher Distanz variiert von Land zu Land erheblich.", "不同国度居民在排队聊天时所本能渴求的肢体物理安全距离存在着天壤之别。"),
            ("die Intimsphäre", "die", "n.", "-", "个人不可侵犯之私密空间", "Dringen Sie niemals ungefragt in die geschützte Intimsphäre anderer Menschen ein!", "在任何情境下都切莫未经允许冒失侵入他人神圣受庇护的绝对私人私密领地！"),
            ("das Reisefieber", "das", "n.", "-", "临行前兴奋忐忑之行前亢奋", "Am Vorabend der großen Expedition packte das gesamte Team das fiebrige Reisefieber.", "在极地科考队即将拔锚启航开拔的前夜，整座基地营房所有队员被行前亢奋席卷。"),
            ("die Reiselust", "die", "n.", "-", "向往辽阔远方的漫游癖好", "Die unbändige Reiselust treibt ihn jedes Jahr in entlegene Winkel unseres Planeten.", "那股奔腾在骨子里想要丈量大地的躁动漫游热望，每年都驱使他踏足地球荒蛮角落。"),
            ("das Fernweh", "das", "n.", "-", "渴盼挣脱日常奔赴远方的渴望", "Wenn der Herbstnebel die Stadt einhüllt, packt mich regelmäßig das Fernweh.", "每当深秋阴冷的浓雾笼罩整座城市天际线，我胸膛深处便翻涌起想要出逃的远方渴望。"),
            ("die Faszination", "die", "n.", "-en", "令人沉醉着魔的无上魅力", "Die Faszination der schneebedeckten Gipfel des Himalaya ist zeitlos und magisch.", "喜马拉雅山脉常年白雪皑皑、直插云霄的崇高雪山巅峰散发着超越时空的魔幻魅力。"),
            ("faszinieren", "", "v.", "fasziniert, faszinierte, fasziniert", "深深吸引令人着迷倾倒", "Fremde Sprachen und alte Schriftsysteme faszinieren Archäologen seit jeher.", "流传千百载的异国古老语言与泥板铭文刻辞自古以来便深深吸引着一代代考古巨擘。"),
            ("die Attraktion", "die", "n.", "-en", "世界级标志性文旅名胜景观", "Die Felsenstadt Petra in Jordanien zählt zu den weltweit spektakulärsten Attraktionen.", "伫立在约旦崇山岩壁间的佩特拉玫瑰古城跻身全球公认最叹为观止的历史奇观之列。"),
            ("das Weltkulturerbe", "das", "n.", "-", "联合国教科文组织世界文化遗产", "Die UNESCO erklärte das historische Altstadt-Ensemble zum geschützten Weltkulturerbe.", "联合国教科文组织正式批准将该座保存完好的中世纪古城街区列入世界文化遗产。"),
            ("das Monument", "das", "n.", "-e", "巍峨雄浑的历史不朽纪念丰碑", "Das monumentale Bauwerk überstand Erdbeben, Kriege und Jahrhunderte des Verfalls.", "这座拔地而起的宏伟丰碑奇迹般跨越了多次大地震、惨烈战火与漫长岁月的风化。"),
            ("die Ruine", "die", "n.", "-n", "断壁残垣古代历史城池遗址", "Die malerischen Ruinen einer antiken Festung thronen hoch über dem tosenden Meer.", "一座古罗马沿海要塞的断壁残垣风景如画般孤傲高悬在波涛汹涌的万顷碧波之上。"),
            ("die Ausgrabung", "die", "n.", "-en", "科学考古发掘田野工地", "Bei den Ausgrabungen im Nildelta stießen Archäologen auf sensationelle Königsgräber.", "在尼罗河三角洲开展的田野发掘工程中，多国联合考古队发现了轰动世界的法老王陵。"),
            ("das Relikt", "das", "n.", "-e", "历尽沧桑遗存的历史遗存孑遗", "Das verrostete Schiffswrack am Strand ist ein stummes Relikt vergangener Kolonialzeiten.", "半掩埋在沙滩礁石间锈迹斑斑的远洋沉船残骸，是昔日殖民扩张时期一具无声的遗存。"),
            ("das Ritual", "das", "n.", "-e", "神圣庄严之宗教祭祀仪式", "Täglich bei Sonnenaufgang vollziehen die Mönche ihr stilles, meditatives Feuerritual.", "每天东方既白红日初升之际，众僧侣便虔诚肃穆地开始举行古老打坐的静心火祭仪式。"),
            ("rituell", "", "adj.", "", "依循古老仪轨举行的", "Die rituelle Waschung vor dem Gebet ist eine symbolische Reinigung von Körper und Geist.", "在祈祷布道前举行的仪式性净水沐手，象征着荡涤尘垢、使肉身与灵魂重归纯洁。"),
            ("die Pilgerreise", "die", "n.", "-n", "虔诚跋涉千里的精神朝圣之旅", "Eine monatelange Pilgerreise auf dem berühmten Jakobsweg nach Santiago de Compostela.", "历经数月艰苦卓绝风餐露宿、徒步丈量圣地亚哥朝圣古道的灵魂洗礼朝圣漫漫长途。"),
            ("der Pilger", "der", "n.", "-", "风尘仆仆的虔诚朝圣行者", "Mit festem Schuhwerk und schwerem Rucksack wandern die Pilger Tag für Tag gen Westen.", "脚踩厚底徒步登山靴、背负沉重行囊的朝圣行者们日复一日义无反顾迎着夕阳西行。"),
            ("die Spiritualität", "die", "n.", "-", "超越尘俗的精神灵性追求", "Viele gestresste Europäer suchen in fernen Klöstern nach innerer Ruhe und Spiritualität.", "身心俱疲的欧洲都市白领纷纷前往隐秘禅修古刹，祈求寻觅久违的心灵宁静与灵性。"),
            ("der Rucksacktourist", "der", "n.", "-en", "穷游四海年轻背包客", "Als sparsamer Rucksacktourist übernachtete er in einfachen Schlafsälen und zeltete frei.", "作为一名克勤克俭的青年背包客，他一路住最便宜的青年旅舍大通铺并随地扎营露宿。"),
            ("das Trekking", "das", "n.", "-", "高难度高海拔徒步探险远足", "Das anspruchsvolle Trekking durch den Himalaya erforderte höchste körperliche Fitness.", "穿越喜马拉雅山脉高海拔缺氧垭口的高难度徒步探险，对心肺功能提出了极限大考。"),
            ("die Expedition", "die", "n.", "-en", "科学考察国家级极地探险队", "Die wissenschaftliche Expedition in die Antarktis sammelte wertvolle Eisbohrkerne.", "奔赴南极内陆冰盖极端极寒腹地的国家级科学探险队成功钻取到了珍贵深层冰芯。"),
            ("das Basislager", "das", "n.", "-", "登山大本营后勤保障基地", "Im Basislager auf 5.300 Metern Höhe akklimatisierten sich die Bergsteiger tagelang.", "在海拔高达五千三百米的高山大本营账内，登山队员用了足足数日才完成高海拔适应。"),
            ("die Höhenkrankheit", "die", "n.", "-", "急性高原缺氧反应高反", "Symptome der gefährlichen Höhenkrankheit dürfen niemals ignoriert werden.", "遭遇突如其来的剧烈头痛等急性高原反应危险信号时，切莫硬撑必须果断下撤！"),
            ("der Guide", "der", "n.", "-s", "野外向导，带路探路向导", "Ohne ortskundigen Guide sollte man sich keinesfalls in das Dschungelgebiet wagen.", "若缺乏对地形地貌了如指掌的资深本地土著向导引路，绝不可贸然孤身深入雨林。"),
            ("die Safari", "die", "n.", "-s", "非洲大草原荒野野生动物科考", "Auf der Foto-Safari im Serengeti-Nationalpark beobachteten wir jagende Löwen.", "在坦桑尼亚塞伦盖蒂大草原开展的追兽野生动物摄影中，我们亲眼目击了雄狮捕食。"),
            ("der Nationalpark", "der", "n.", "-s", "受最高规格保护之国家公园", "Im Nationalpark gelten strengste Schutzvorschriften für Flora, Fauna und Geologie.", "在国家公园法定红线控制区内，对植被、野生动物群落与地质地貌实行顶级封育。"),
            ("das Schutzgebiet", "das", "n.", "-e", "划定红线的自然生态保护区", "Das Meeres-Schutzgebiet ist für industrielle Schleppnetzfischerei gesperrt.", "该海洋特种生态功能保护区全域常年严密布控，严禁任何大型底拖网渔船驶入作业。"),
            ("die Nachhaltigkeit", "die", "n.", "-", "负责任且不损生态之永续发展", "Sanfter Tourismus setzt konsequent auf soziale und ökologische Nachhaltigkeit.", "倡导轻装上阵、润物无声的生态慢游哲学，矢志不渝追求全产业链绿色永续发展。"),
            ("der Ökotourismus", "der", "n.", "-", "低碳少痕之原生态绿色旅游", "Ökotourismus schafft Einkommen für die lokale Bevölkerung und schützt den Regenwald.", "大力培植低碳生态原生态旅游业态，既让周边山民脱贫致富又守护了连绵雨林。"),
            ("der Massentourismus", "der", "n.", "-", "泛滥成灾破坏景观之过度过量旅游", "Historische Lagunenstädte stöhnen unter den immensen Belastungen des Massentourismus.", "威尼斯等古老水乡历史名城在巨无霸邮轮与过度旅游客流的重压践踏之下苦不堪言。"),
            ("die Überfüllung", "die", "n.", "-", "游人如织超负荷人满为患", "Wegen massiver Überfüllung regulieren viele Sehenswürdigkeiten den täglichen Zutritt.", "由于景区常态化人满为患超负荷承载，诸多世界名胜不得不启动每日严格分时限流。"),
            ("das Visum", "das", "n.", "Visa", "合法入境查验准入出入境签证", "Prüfen Sie rechtzeitig vor dem Ticketkauf die Einreisebestimmungen und Visa-Fristen!", "在点击付款下单国际航线机票前，务必审慎复核中转国与目的地国的入境签证门槛！"),
            ("die Gültigkeit", "die", "n.", "-", "证件法律有效性与有效期", "Der Reisepass muss bei der Einreise noch mindestens sechs Monate Gültigkeit haben.", "按照多数主权国法律红线，当事人护照自入境当日起算剩余有效期严禁少于六个月。"),
            ("die Zollbestimmungen", "die", "n.pl.", "-", "海关出入境物品验放检疫法规", "Verstöße gegen strengste Zollbestimmungen werden mit drakonischen Strafen geahndet.", "任何企图夹带违禁濒危动植物标本闯关偷渡海关的行为，都将招致刑律最严厉惩处。"),
            ("der Währungskurs", "der", "n.", "-e", "国际外汇外币挂牌兑换牌价", "Informieren Sie sich vor Ort über faire Währungskurse und vermeiden Sie Wechselbetrug!", "在异国他乡兑换当地货币时请选择正规网点紧盯实时汇率，切莫贪小便宜误入汇兑骗局！"),
            ("das Souvenir", "das", "n.", "-s", "承载异域记忆的纪念伴手礼", "Ein kunstvoll handgewebter Wollteppich als unvergängliches Souvenir an den Orient.", "一块由古城名匠用老织布机一梭一线精心编织而成的羊毛挂毯，定格了东方之旅。")
        ]
    }
]
