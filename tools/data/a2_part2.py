#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A2 Part 2: Lessons 6 to 10 (350 words)
L06: 公共交通、自驾导航与铁路出行 (Mobilität, Verkehr & Bahnreisen) - 70 words
L07: 旅游度假、酒店住宿与行李海关 (Urlaub, Reisen & Hotel) - 70 words
L08: 医疗问诊、健康保险与突发急救 (Arzt, Krankenversicherung & Notfall) - 70 words
L09: 德语区特色美食、餐饮文化与烹饪 (Gastronomie, Spezialitäten & Kochen) - 70 words
L10: 穿衣时尚、外貌性格与人际印象 (Mode, Aussehen & Charakter) - 70 words
"""

LESSONS_A2_PART2 = [
    # LESSON 6
    {
        "id": "A2_L06",
        "title": "第6课：公共交通、自驾导航与铁路出行 (Mobilität & Bahnreisen)",
        "summary": "掌握第二虚拟式(Konjunktiv II: könnte, würde)礼貌请求、德铁系统与自驾导航",
        "grammar": {
            "title": "第二虚拟式 (Konjunktiv II) 礼貌表达与交通出行",
            "sections": [
                {
                    "heading": "1. würde + 动词原形 与 könnte 表达委婉礼貌请求",
                    "content": "• Würden Sie mir bitte helfen? (您能帮帮我吗？比 Helfen Sie mir! 礼貌得多)\n• Könnten Sie mir bitte sagen, wann der Zug abfährt? (您能告诉我火车何时发车吗？)\n• Hätten Sie vielleicht ein Ticket für mich?"
                },
                {
                    "heading": "2. 方位介词通过与沿着",
                    "content": "• durch + Akkusativ: Wir fahren durch den Tunnel / durch die Stadt.\n• entlang + Akkusativ (放在名词后): Gehen Sie die Straße entlang!"
                }
            ]
        },
        "quiz": [
            {
                "id": "A2_L06_Q1",
                "type": "GRAMMAR_FILL",
                "question": "______ (können, 礼貌第二虚拟式) Sie mir bitte den Weg zum Bahnhof erklären?",
                "options": ["Könnten", "Können", "Konnte", "Gekonnt"],
                "correctIndex": 0,
                "explanation": "第二虚拟式 Könnten Sie bitte... 是向陌生人问路最得体尊重的表达。"
            },
            {
                "id": "A2_L06_Q2",
                "type": "VOCAB_MEANING",
                "question": "德铁车票上的 'die Platzreservierung' 意思是：",
                "options": ["座位预订号", "车厢车次", "列车晚点提醒", "车票退款"],
                "correctIndex": 0,
                "explanation": "die Platzreservierung 是德铁预订固定席位/座位的专用词。"
            }
        ],
        "words": [
            ("die Mobilität", "die", "n.", "-", "出行交通能力，移动性", "Nachhaltige Mobilität schützt das Stadtklima.", "绿色低碳出行切实保护了城市环境。"),
            ("der Verkehr", "der", "n.", "-", "交通，交通运输", "Im Berufsverkehr gibt es regelmäßig lange Staus.", "在早晚通勤高峰期常常出现严重拥堵。"),
            ("die Verbindung", "die", "n.", "-en", "列车班次换乘联络", "Gibt es eine direkte Verbindung nach Zürich?", "有直达苏黎世的不换乘班次吗？"),
            ("die Strecke", "die", "n.", "-n", "路段，铁路线路", "Die landschaftlich reizvolle Strecke durchs Rheintal.", "穿越莱茵河谷那条风光秀美的铁路线。"),
            ("die Durchsage", "die", "n.", "-n", "站台播音通告", "Bitte beachten Sie die Durchsagen am Bahnsteig!", "请候车乘客密切留意站台广播通告！"),
            ("die Abfahrt", "die", "n.", "-en", "启程发车，出站", "Die planmäßige Abfahrt ist um 14 Uhr 25.", "按运行图正点发车时间为14点25分。"),
            ("die Ankunft", "die", "n.", "Ankünfte", "到达，进站", "Wegen einer Weichenstörung verzögert sich die Ankunft.", "由于道岔机械故障进站有所延误。"),
            ("die Verspätung", "die", "n.", "-en", "晚点，延误时长", "Der Intercity hat heute 20 Minuten Verspätung.", "城际特快列车今日晚点20分钟。"),
            ("der Ausfall", "der", "n.", "Ausfälle", "列车停运，取消", "Der plötzliche Zugausfall verärgerte viele Reisende.", "突如其来的列车停运令旅客十分气恼。"),
            ("entfallen", "", "v.", "entfällt, entfiel, ist entfallen", "取消，停开", "Der Halt in Heidelberg entfällt heute leider.", "今日该次列车遗憾取消停靠海德堡站。"),
            ("der Fahrgast", "der", "n.", "Fahrgäste", "车客，乘车人", "Wir bitten alle Fahrgäste, vorsichtig einzusteigen.", "我们提示所有乘客请小心稳步上车。"),
            ("der Passagier", "der", "n.", "-e", "客轮机车旅客", "Die Passagiere schnallen sich vor dem Start an.", "起飞起步前全体旅客扣好安全带。"),
            ("der Bahnsteig", "der", "n.", "-e", "候车站台", "Der Zug fährt auf Bahnsteig 3 Abschnitt B ein.", "列车正在驶入3站台B候车分区。"),
            ("das Gleis", "das", "n.", "-e", "站台股道，铁道", "Vorsicht bei der Einfahrt des Zuges an Gleis 7!", "7道有列车进站，请大家注意安全！"),
            ("der Wagen", "der", "n.", "-", "车厢；轿车", "Unser reservierter Sitzplatz ist in Wagen 21.", "我们预订好的指定座席位于21号车厢。"),
            ("die Klasse", "die", "n.", "-n", "车厢坐席等级", "In der 1. Klasse gibt es kostenlose Tageszeitungen.", "一等座车厢内免费配发当日报刊。"),
            ("das Abteil", "das", "n.", "-e", "包厢，隔间车厢", "Wir haben ein ruhiges 6er-Abteil für die Familie.", "我们为全家人预订了一间安静的6人包厢。"),
            ("der Großraumwagen", "der", "n.", "-", "大通铺无隔断大车厢", "Im Großraumwagen ist oft reger Betrieb.", "在大开间敞开式车厢内往往人来人往。"),
            ("der Sitzplatz", "der", "n.", "Sitzplätze", "坐席，座位", "Darf ich mich auf diesen freien Sitzplatz setzen?", "请问我能坐在这个空着的座位上吗？"),
            ("die Reservierung", "die", "n.", "-en", "席位预订", "Eine Sitzplatzreservierung ist am Freitag ratsam.", "周五出行强烈建议提前办理座位预订。"),
            ("reservieren", "", "v.", "reserviert, reservierte, reserviert", "预留，锁定座位", "Ich habe online zwei Fensterplätze reserviert.", "我在网上预留订好了两个靠窗的座位。"),
            ("der Gang", "der", "n.", "Gänge", "走道，过道", "Möchten Sie lieber am Fenster oder am Gang sitzen?", "您更喜欢靠窗户还是靠走廊过道坐？"),
            ("das Fenster", "das", "n.", "-", "窗户，车窗", "Der Blick aus dem Zugfenster ist atemberaubend.", "从列车车窗向外眺望的风景令人屏息。"),
            ("der Fahrschein", "der", "n.", "-e", "车票，行车票证", "Zeigen Sie dem Zugbegleiter bitte Ihren Fahrschein!", "请向列车员主动出示您的有效车票！"),
            ("die Fahrkarte", "die", "n.", "-n", "车票", "Eine einfache Fahrkarte nach München bitte!", "请来一张前往慕尼黑的单程车票！"),
            ("die Hin- und Rückfahrt", "die", "n.", "-en", "往返双程车票", "Eine Fahrkarte für Hin- und Rückfahrt ist günstiger.", "购买往返双程车票价格会更加优惠。"),
            ("die BahnCard", "die", "n.", "-s", "德铁优享打折卡", "Mit der BahnCard 25 spart man ein Viertel des Preises.", "持德铁25折卡购票可享净省四分之一票价。"),
            ("der Tarif", "der", "n.", "-e", "运价，资费标准", "Der Nahverkehrstarif gilt im gesamten Verbund.", "该短途客运票价标准在整个交通联盟通用。"),
            ("der Verbund", "der", "n.", "-e", "区域联合交通网", "Im Verkehrsverbund genügt ein einziges Ticket.", "在大区交通联合网内只需一张单票即可通乘。"),
            ("die Monatskarte", "die", "n.", "-n", "月票", "Für Berufspendler lohnt sich eine Monatskarte.", "对于跨城通勤上班族来说买月票非常划算。"),
            ("das Deutschlandticket", "das", "n.", "-s", "全德49欧通乘通票", "Das Deutschlandticket gilt bundesweit im Nahverkehr.", "全德49欧票在全国所有短途公共交通均通用。"),
            ("umsteigen", "", "v.", "steigt um, stieg um, ist umgestiegen", "中转换乘", "In Hannover haben wir 12 Minuten Zeit zum Umsteigen.", "在汉诺威站我们有12分钟充裕时间完成换乘。"),
            ("der Umstieg", "der", "n.", "-e", "换乘转接", "Der Umstieg am gleichen Bahnsteig ist sehr bequem.", "在同一座站台原站台对面换乘极其轻松便捷。"),
            ("der Anschluss", "der", "n.", "Anschlüsse", "接续车次", "Erreicht unser Zug noch den Anschluss nach Bremen?", "我们的列车还能赶得上接续开往不莱梅的车吗？"),
            ("verpassen", "", "v.", "verpasst, verpasste, verpasst", "误车，错过", "Wenn wir trödeln, verpassen wir den Anschlusszug.", "要是我们磨蹭延误，就会错过换乘接续列车。"),
            ("die Schranke", "die", "n.", "-n", "道口栏木道闸", "Die Schranke am Bahnübergang senkt sich.", "铁路道口的安全起落道闸正缓缓降下。"),
            ("der Bahnübergang", "der", "n.", "Bahnübergänge", "平交道口", "Halten Sie vor dem unbeschrankten Bahnübergang!", "行经无道闸铁路平交道口前务必先停车观望！"),
            ("die Haltestelle", "die", "n.", "-n", "停靠站，乘车点", "Drücken Sie die Stopptaste vor der Haltestelle!", "到站前请提前按下车内的靠站停车按钮！"),
            ("die Endstation", "die", "n.", "-en", "终点总站", "Dieser Bus fährt bis zur Endstation Hauptfriedhof.", "这辆公共汽车一直开到总站中央公墓。"),
            ("der Fahrplan", "der", "n.", "Fahrpläne", "时刻运行表", "Im Fahrplan sind alle Zwischenhalte verzeichnet.", "列车运行时刻表上完整标明了沿途所有经停站。"),
            ("das Auto", "das", "n.", "-s", "机动小轿车", "In Großstädten braucht man kaum ein eigenes Auto.", "在大都市里生活其实几乎不需要买私家小汽车。"),
            ("der Führerschein", "der", "n.", "-e", "机动车驾驶执照", "Mit 18 Jahren darf man den Führerschein machen.", "年满18周岁即有资格报考申领机动车驾照。"),
            ("die Autobahn", "die", "n.", "-en", "高速公路", "Auf deutschen Autobahnen gilt oft Richtgeschwindigkeit.", "德国部分高速公路上推行建议推荐巡航时速。"),
            ("die Raststätte", "die", "n.", "-n", "高速公路服务区", "An der Raststätte tanken wir und trinken Kaffee.", "在高速公路服务区我们给车加油并喝了咖啡。"),
            ("die Tankstelle", "die", "n.", "-n", "加油站", "An der Tankstelle kann man auch nachts Snacks kaufen.", "在加油站便利店夜间也能买到便餐小吃。"),
            ("tanken", "", "v.", "tankt, tankte, getankt", "加注燃油", "Ich muss vor der langen Fahrt unbedingt volltanken.", "在长途奔袭之前我必须将油箱彻底加满。"),
            ("das Benzin", "das", "n.", "-", "汽油", "Die Benzinpreise schwanken im Laufe des Tages.", "汽油零售价格在一天之中常呈现动态波动。"),
            ("der Diesel", "der", "n.", "-", "柴油", "Viele Langstreckenfahrer bevorzugen sparsamen Diesel.", "许多长途驾驶爱好者更偏好省油耐造的柴油车。"),
            ("die Batterie", "die", "n.", "-n", "动力电池，蓄电池", "Die Batterie des Elektroautos reicht für 400 Kilometer.", "该纯电动汽车的电池包续航里程达400公里。"),
            ("laden", "", "v.", "lädt, lud, geladen", "充电；装载", "Das Auto lädt an der Schnellladesäule in 30 Minuten.", "该车在超充充电桩上只需30分钟即可快充完成。"),
            ("die Ladesäule", "die", "n.", "-n", "电动汽车充电桩", "In der Innenstadt entstehen viele neue Ladesäulen.", "市中心核心区正在大规模兴建全新公共充电桩。"),
            ("der Stau", "der", "n.", "-s", "车辆拥堵长龙", "Wegen einer Baustelle stehen wir fünf Kilometer im Stau.", "由于前方道路施工我们在车龙中堵了五公里长。"),
            ("die Baustelle", "die", "n.", "-n", "道路施工作业区", "An Baustellen gilt meist Tempo 60 oder 80.", "途经道路施工受控路段通常限速60或80码。"),
            ("die Umleitung", "die", "n.", "-en", "临时绕行改道", "Folgen Sie der ausgeschilderten Umleitung U3!", "请沿着竖立有明确标牌的U3改道路线绕行！"),
            ("das Navigationssystem", "das", "n.", "-e", "卫星导航定位仪", "Das Navigationssystem warnt vor akuten Behinderungen.", "车载卫星导航定位仪及时对突发拥堵发出告警。"),
            ("das Navi", "das", "n.", "-s", "导航仪（口语简称）", "Stell das Ziel bitte im Navi ein!", "请在手机车载导航仪里设定好目的地！"),
            ("die Ausfahrt", "die", "n.", "-en", "高速匝道出口", "Nehmen Sie an der nächsten Ausfahrt die rechte Spur!", "请在前方下一个高速出口变道并驶入右侧匝道！"),
            ("die Einfahrt", "die", "n.", "-en", "入口处，匝道入口", "Vorsicht beim Beschleunigen auf der Autobahneinfahrt!", "在高速公路加速匝道汇入主道时请注意安全！"),
            ("überholen", "", "v.", "überholt, überholte, überholt", "超车", "Auf der rechten Spur darf man auf der Autobahn nicht überholen.", "在高速公路上法律明令禁止从右侧车道超车。"),
            ("die Spur", "die", "n.", "-en", "行车道，车道线", "Wechseln Sie rechtzeitig auf die linke Fahrspur!", "请提前变道切入左侧快速主行车道！"),
            ("die Höchstgeschwindigkeit", "die", "n.", "-en", "最高法定限速", "Die zulässige Höchstgeschwindigkeit beträgt 100 km/h.", "该路段法定允许的最高巡航时速为100公里。"),
            ("bremsen", "", "v.", "bremst, bremste, gebremst", "踩刹车制动", "Der Fahrer bremste rechtzeitig vor dem Hindernis ab.", "司机在突发障碍物前方极其沉着地及时踩下刹车。"),
            ("die Bremse", "die", "n.", "-n", "制动刹车装置", "Die Bremsen des Fahrrads müssen nachgestellt werden.", "自行车的机械刹车皮需要重新校准紧固。"),
            ("der Reifen", "der", "n.", "-", "汽车轮胎", "Im Oktober wechselt man auf Winterreifen.", "十月份通常要把夏季胎更换为冬季雪地胎。"),
            ("die Panne", "die", "n.", "-n", "抛锚故障", "Wir hatten auf der Landstraße eine Reifenpanne.", "我们在乡间公路上遇到车胎扎钉爆胎抛锚了。"),
            ("der Abschleppdienst", "der", "n.", "-e", "汽车拖车救援服务", "Der Abschleppdienst bringt das Auto in die Werkstatt.", "道路拖车救援机构把故障车辆拖进了修理厂。"),
            ("die Werkstatt", "die", "n.", "Werkstätten", "车辆维修工场", "In der Werkstatt wird der Keilriemen ausgetauscht.", "汽车修理工场内正在为车辆更换老化的皮带。"),
            ("parken", "", "v.", "parkt, parkte, geparkt", "停泊泊车", "Hier darf man maximal zwei Stunden kostenlos parken.", "此处最多可免费停车停放两个小时。"),
            ("der Parkplatz", "der", "n.", "Parkplätze", "停车场，停车泊位", "Hinter dem Supermarkt gibt es reichlich Parkplätze.", "在大型超市背后规划有十分充裕的停车位。"),
            ("das Parkhaus", "das", "n.", "Parkhäuser", "多层室内停车楼", "Das moderne Parkhaus ist videoüberwacht und hell.", "这座现代化的室内停车楼配有全景监控且敞亮。")
        ]
    },

    # LESSON 7
    {
        "id": "A2_L07",
        "title": "第7课：旅游度假、酒店住宿与行李海关 (Urlaub, Reisen & Hotel)",
        "summary": "掌握形容词词尾变化规则、预订酒店客房、机场登机托运与入境海关",
        "grammar": {
            "title": "形容词词尾强弱变化与酒店旅游交际",
            "sections": [
                {
                    "heading": "1. 定冠词后的形容词词尾变化（弱变化）",
                    "content": "• 第一格：der gute Mann / das schöne Hotel / die große Stadt\n• 第四格：den guten Mann / das schöne Hotel / die große Stadt\n• 其余所有格位（第三格、第二格、所有复数）：一律加 -en！\n  in dem modernen Hotel / mit den freundlichen Gästen"
                },
                {
                    "heading": "2. 酒店前台高频登记句型",
                    "content": "• Ich habe ein Doppelzimmer auf den Namen... reserviert.\n• Ist das Frühstück im Preis inbegriffen?\n• Bis wann muss man auschecken? - Bis 11 Uhr bitte."
                }
            ]
        },
        "quiz": [
            {
                "id": "A2_L07_Q1",
                "type": "GRAMMAR_FILL",
                "question": "Wir übernachten in einem ______ (modern) Hotel im Zentrum.",
                "options": ["modernen", "moderne", "modernem", "moderner"],
                "correctIndex": 0,
                "explanation": "不定冠词第三格中性 (einem)，形容词词尾加 -en (in einem modernen Hotel)。"
            },
            {
                "id": "A2_L07_Q2",
                "type": "VOCAB_MEANING",
                "question": "酒店客房预订单上的 'die Halbpension' 意思是：",
                "options": ["半包伙（含早餐及一顿正餐）", "全包伙含三餐", "仅含客房住宿不含早", "半价养老金优惠"],
                "correctIndex": 0,
                "explanation": "die Halbpension 是欧洲酒店餐饮惯例，指房费包含早餐以及午餐或晚餐中的一顿。"
            }
        ],
        "words": [
            ("das Reiseziel", "das", "n.", "-e", "旅行目的地", "Italien gehört zu den beliebtesten Reisezielen.", "意大利一直是深受德国人青睐的度假胜地。"),
            ("die Reise", "die", "n.", "-n", "长途旅行，度假", "Wir planen eine dreiwöchige Reise durch Norwegen.", "我们正在规划一次为期三周的挪威深度自驾游。"),
            ("die Rundreise", "die", "n.", "-n", "环形周游，环线深度游", "Eine geführte Rundreise zu historischen Stätten.", "一次由专业向导领衔的古迹环线深度游。"),
            ("die Pauschalreise", "die", "n.", "-n", "全包式团队跟团游", "Bei einer Pauschalreise sind Flug und Hotel inklusive.", "报全包跟团游往返机票与全程住宿均含在内。"),
            ("die Städtereise", "die", "n.", "-n", "城市文化周游", "Wien und Prag eignen sich ideal für eine Städtereise.", "维也纳和布拉格非常适合安排城市人文漫步游。"),
            ("das Reisebüro", "das", "n.", "-s", "旅行社实操门店", "Im Reisebüro bucht sie einen Flug nach Mallorca.", "她在旅行社实体门店预订了一张飞马略卡的机票。"),
            ("die Buchung", "die", "n.", "-en", "预订确权，下单订位", "Sie erhalten in Kürze Ihre Buchungsbestätigung.", "您稍后即可在手机上查收电子预订确认单。"),
            ("buchen", "", "v.", "bucht, buchte, gebucht", "锁定预订", "Haben Sie die Tickets schon online gebucht?", "您已经在网络平台上把票全订好了吗？"),
            ("stornieren", "", "v.", "storniert, stornierte, storniert", "撤回退订，退保", "Kann ich das Hotelzimmer kostenlos stornieren?", "请问这间酒店客房能否免费申请退订撤单？"),
            ("die Stornierung", "die", "n.", "-en", "取消撤单，退票", "Bei kurzfristiger Stornierung fällt eine Gebühr an.", "临期突发取消预订需要扣除一定比例手续费。"),
            ("die Versicherung", "die", "n.", "-en", "保险单，保险业务", "Eine Reiserücktrittsversicherung ist sehr sinnvoll.", "购买一份旅行取消险对于规避突发损失大有裨益。"),
            ("das Gepäck", "das", "n.", "-", "随行行李（总称）", "Geben Sie Ihr schweres Gepäck am Schalter auf!", "请在托运柜台办理沉重大件行李的交运托运！"),
            ("das Handgepäck", "das", "n.", "-", "随身手提行李", "Im Handgepäck dürfen keine Flüssigkeiten über 100 ml sein.", "随身携带的手提行李内液体单瓶严禁超过100毫升。"),
            ("der Koffer", "der", "n.", "-", "硬壳拉杆旅行箱", "Ich packe meinen Koffer mit warmer Kleidung.", "我正往拉杆箱里打包收拾各种御寒衣物。"),
            ("die Reisetasche", "die", "n.", "-n", "便携旅行软包", "Für das Wochenende genügt eine kleine Reisetasche.", "度个小周末只需要背上一只轻便小旅行包即可。"),
            ("der Rucksack", "der", "n.", "Rucksäcke", "户外双肩背包", "Er wandert mit einem 50-Liter-Rucksack über die Alpen.", "他背着一个50升的专业户外包徒步翻越阿尔卑斯。"),
            ("der Passagier", "der", "n.", "-e", "乘机乘客，航旅客人", "Alle Passagiere für Flug LH 400 begeben sich zu Gate A12.", "请搭乘汉莎LH400航班的乘客立即前往A12登机口。"),
            ("der Flug", "der", "n.", "Flüge", "航空班机，飞行航程", "Der Direktflug nach Tokio dauert elf Stunden.", "直飞东京的直达航班全程空中耗时十一个小时。"),
            ("fliegen", "", "v.", "fliegt, flog, ist geflogen", "乘坐民航客机飞行", "Morgen fliegen wir früh morgens nach Spanien.", "明天清晨一大早我们将乘机飞赴西班牙。"),
            ("die Fluggesellschaft", "die", "n.", "-en", "民用航空公司", "Die Lufthansa ist die größte deutsche Fluggesellschaft.", "汉莎航空是德国本土规模首屈一指的航空公司。"),
            ("die Airline", "die", "n.", "-s", "航空公司", "Billige Airlines verlangen oft extra für das Gepäck.", "廉价航空公司对行李托运往往另外收取高昂运费。"),
            ("der Abflug", "der", "n.", "Abflüge", "客机起飞离港", "Der Abflug verzögert sich witterungsbedingt.", "受恶劣气象条件制约客机起飞时间向后顺延。"),
            ("starten", "", "v.", "startet, startete, ist gestartet", "滑行起飞", "Die Maschine startet pünktlich von der Startbahn.", "飞机从机场主跑道上极其平稳正点滑行升空。"),
            ("landen", "", "v.", "landet, landete, ist gelandet", "着陆降落", "Das Flugzeug landete sanft auf dem Rollfeld.", "客机极其轻盈舒缓地降落在停机坪滑行道上。"),
            ("die Landung", "die", "n.", "-en", "平稳落地降落", "Nach sicherer Landung klatschen manche Passagiere.", "安全平稳着陆后舱内部分乘客情不自禁鼓掌致谢。"),
            ("das Gate", "das", "n.", "-s", "机场登机口", "Das Boarding beginnt in zehn Minuten an Gate B22.", "登机工作将于十分钟后在B22号登机口正式启动。"),
            ("die Bordkarte", "die", "n.", "-n", "登机牌凭证", "Halten Sie Bordkarte und Ausweis griffbereit!", "请将您的登机牌与有效护照身份证件备好随时出示！"),
            ("die Sicherheitskontrolle", "die", "n.", "-n", "机场安全检查", "An der Sicherheitskontrolle legt man Gürtel und Uhr ab.", "在机场安检口需要解下皮带并摘下手表放入安检筐。"),
            ("der Zoll", "der", "n.", "Zölle", "海关检验关税", "Haben Sie am Zoll anmeldepflichtige Waren dabei?", "您在出入境海关处有需要主动申报纳税的物品吗？"),
            ("verzollen", "", "v.", "verzollt, verzollte, verzollt", "主动向海关申报纳税", "Diese wertvolle Ware muss ordnungsgemäß verzollt werden.", "这些高价值的大宗进口物品必须依法足额照章纳税。"),
            ("das Visum", "das", "n.", "Visa", "签证凭证", "Für die Einreise benötigt man ein gültiges Visum.", "入境该国要求当事人必须持有合法有效入境签证。"),
            ("beantragen", "", "v.", "beantragt, beantragte, beantragt", "提交申办，申请", "Sie beantragt das Visum bei der Botschaft.", "她正在该国驻华大使馆签证处积极申请赴外签证。"),
            ("die Unterkunft", "die", "n.", "Unterkünfte", "落脚住所，住宿地", "Wir haben eine gemütliche Unterkunft am See gebucht.", "我们在湖滨小镇预订好了一处极其温馨舒适的住所。"),
            ("das Hotel", "das", "n.", "-s", "涉外高档酒店，宾馆", "Ein traditionsreiches 4-Sterne-Hotel im Schwarzwald.", "黑森林地区一座极富深厚历史底蕴的四星级特色酒店。"),
            ("die Pension", "die", "n.", "-en", "家庭式家庭旅馆", "In der familiären Pension fühlten wir uns wie zu Hause.", "在这家温馨的小客栈里我们体会到了宾至如归的温暖。"),
            ("die Jugendherberge", "die", "n.", "-n", "国际青年旅舍", "Die Jugendherberge bietet günstiges Quartier für Backpacker.", "国际青旅为囊中羞涩的年轻背包客提供了平价床铺。"),
            ("die Ferienwohnung", "die", "n.", "-en", "度假公寓整套出租房", "Die Ferienwohnung hat eine komplett eingerichtete Küche.", "这间度假公寓配有烹饪设施一应俱全的整套厨房。"),
            ("das Ferienhaus", "das", "n.", "Ferienhäuser", "整栋独立度假小木屋", "Wir mieten ein geräumiges Ferienhaus an der Ostsee.", "我们在波罗的海海岸线租下了一栋宽敞独立的木屋。"),
            ("der Campingplatz", "der", "n.", "Campingplätze", "房车露营营地", "Auf dem Campingplatz schlagen wir unser Zelt auf.", "在专业露营地的大草坪上我们兴高采烈扎起了帐篷。"),
            ("das Zelt", "das", "n.", "-e", "野外帐篷", "Ein windfestes und wasserdichtes Zelt für Bergtouren.", "一顶专为高山徒步探险定制的抗风防暴雨专业帐篷。"),
            ("zelten", "", "v.", "zeltet, zeltete, gezeltet", "野营露宿露营", "Im Sommer zelten viele junge Leute an schwedischen Seen.", "夏天许多年轻旅人喜欢在瑞典纯净的湖泊旁露营。"),
            ("das Einzelzimmer", "das", "n.", "-", "单人客房", "Ich möchte ein ruhiges Einzelzimmer mit Dusche.", "我希望预订一间配有独立淋浴设施的安静单人间。"),
            ("das Doppelzimmer", "das", "n.", "-", "双人大床客房", "Ein Doppelzimmer mit herrlichem Blick auf die Berge.", "一间拥有绝美雪山全景推窗视角的豪华双人客房。"),
            ("die Suite", "die", "n.", "-n", "高档豪华套房", "Die Präsidenten-Suite verfügt über eine private Sauna.", "这间总统行政套房内部甚至独家配建有私人桑拿房。"),
            ("das Bett", "das", "n.", "-en", "床铺，卧具", "Das Bett war herrlich breit und bequem bezogen.", "客房里的大床宽大暄软且床品被褥铺得极度舒服。"),
            ("das Bad", "das", "n.", "Bäder", "独立卫生洗浴间", "Jedes Hotelzimmer verfügt über ein eigenes Bad.", "宾馆里的每一间独立客房内部均配有独立私享卫浴。"),
            ("der Meerblick", "der", "n.", "-", "海景全貌", "Ein Zimmer mit direktem Meerblick kostet extra.", "自带直面大海无死角落地海景的客房需加收差价。"),
            ("die Rezeption", "die", "n.", "-en", "前台接待处", "Die Rezeption ist rund um die Uhr freundlich besetzt.", "酒店前台接待处全天二十四小时均有热忱员工值守。"),
            ("der Empfang", "der", "n.", "-", "接待大厅，总服务台", "Melden Sie sich bei der Ankunft bitte am Empfang!", "抵店抵馆后请先移步大堂总服务台办理登记入住！"),
            ("einchecken", "", "v.", "checkt ein, checkte ein, eingecheckt", "办理入住，登机值机", "Ab 15 Uhr kann man im Hotel bequem einchecken.", "下午三点起宾客即可在前台从容办理入住下榻手续。"),
            ("auschecken", "", "v.", "checkt aus, checkte aus, ausgecheckt", "退房结账结算", "Wir müssen bis 11 Uhr das Zimmer geräumt auschecken.", "我们必须在上午十一点前彻底打包退房办结离店。"),
            ("die Schlüsselkarte", "die", "n.", "-n", "电子客房磁卡门卡", "Halten Sie die Schlüsselkarte an das elektronische Schloss!", "请将房门感应磁卡贴近电子门锁刷卡感应区开门！"),
            ("der Gast", "der", "n.", "Gäste", "入住宾客，客人", "Das Hotel verwöhnt seine Gäste mit exzellenter Küche.", "该酒店凭借令人赞不绝口的名厨佳肴款待四方宾朋。"),
            ("die Übernachtung", "die", "n.", "-en", "过夜留宿，住宿晚数", "Im Preis sind zwei Übernachtungen und Spa-Eintritt drin.", "结算总价已包含连住两晚客房及免费水疗馆门票。"),
            ("übernachten", "", "v.", "übernachtet, übernachtete, übernachtet", "过夜留宿", "Wir übernachten auf der Durchreise in Nürnberg.", "在长途行车中途我们选择在纽伦堡市停留住宿一晚。"),
            ("das Frühstück", "das", "n.", "-e", "晨早点，早餐", "Ein reichhaltiges Frühstücksbüfett erwartet Sie morgens.", "清晨丰盛琳琅满目的自助早餐恭候着各位下榻贵宾。"),
            ("das Büfett", "das", "n.", "-s", "自取自助餐台", "Am Büfett gibt es frisches Obst, Müsli und Gebäck.", "自助餐台摆满了新鲜水果、谷物麦片及精致烘焙糕点。"),
            ("die Halbpension", "die", "n.", "-", "半包膳宿体系", "Viele Urlauber buchen bevorzugt Halbpension.", "许多海边度假客倾向于选定半包餐的膳宿套餐。"),
            ("die Vollpension", "die", "n.", "-", "一日三餐全包膳宿", "Vollpension beinhaltet Frühstück, Mittag und Abendessen.", "全膳宿涵盖了从晨早、正午直至傍晚的全套三餐。"),
            ("all-inclusive", "", "adj.", "", "全包一价到底免杂费", "Im All-inclusive-Club sind alle Getränke kostenlos.", "在一价全包式度假村内所有酒水饮料全天畅饮免费。"),
            ("die Kurtaxe", "die", "n.", "-n", "疗养度假调节税", "In anerkannten Kurorten wird eine kleine Kurtaxe fällig.", "在国家认证的疗养休假胜地需按日缴存微薄疗养税。"),
            ("der Zimmerservice", "der", "n.", "-", "客房送餐及内务服务", "Er bestellte Frühstück über den internen Zimmerservice.", "他通过客房专属服务电话订购了送餐上门的早餐。"),
            ("die Klimaanlage", "die", "n.", "-n", "冷暖调温空调", "Im Hochsommer schätzt man eine leise Klimaanlage.", "在盛夏酷暑天大家格外倚重一台低噪给力的好空调。"),
            ("die Minibar", "die", "n.", "-s", "客房微型小冷柜", "Getränke aus der Minibar werden gesondert abgerechnet.", "客房小冰柜内的各类酒水消费将在离店时独立结算。"),
            ("der Safe", "der", "n.", "-s", "客房电子贵重保险箱", "Deponieren Sie Schmuck und Pässe im Zimmersafe!", "请务必将首饰与护照稳妥锁闭在客房专用保险箱内！"),
            ("der Föhn", "der", "n.", "-e", "电吹风吹风机", "Im Badezimmer liegt ein leistungsstarker Föhn bereit.", "客房卫生间内贴心配备有大功率电吹风供您使用。"),
            ("das Handtuch", "das", "n.", "Handtücher", "擦手毛巾面巾", "Frische Handtücher liegen ordentlich auf der Ablage.", "洁净蓬松的全新毛巾已整齐摆放在盥洗台置物架上。"),
            ("der Bademantel", "der", "n.", "Bademäntel", "纯棉洗浴睡袍", "Ein kuscheliger Bademantel für den Besuch im Spa.", "一件厚实亲肤的纯棉浴袍专为宾客前往水疗中心备用。"),
            ("das Souvenir", "das", "n.", "-s", "旅行纪念土特产", "Er kaufte handgemachte Souvenirs für die Verwandtschaft.", "他给家乡各位亲戚购置了独具风韵的手工伴手礼。"),
            ("das Andenken", "das", "n.", "-", "留念凭信，纪念品", "Dieses Holzschnitzwerk ist ein schönes Andenken.", "这尊精美木雕是此番阿尔卑斯山之旅的珍贵留念。")
        ]
    },

    # LESSON 8
    {
        "id": "A2_L08",
        "title": "第8课：医疗问诊、健康保险与突发急救 (Arzt & Notfall)",
        "summary": "掌握情态动词过去时、医疗保险报销体系、描述症状与急救呼叫",
        "grammar": {
            "title": "从属连词 dass (陈述宾语) 与如果 wenn 从句",
            "sections": [
                {
                    "heading": "1. 引导从句连词 dass 与 wenn 框形结构",
                    "content": "从句中的变位动词永远置于句末！\n• dass (引出客观陈述内容)：Der Arzt sagt, dass ich viel Wasser trinken soll.\n• wenn (引出条件假定)：Wenn Sie Schmerzen haben, nehmen Sie diese Tablette!"
                },
                {
                    "heading": "2. 德国紧急呼叫电话常识",
                    "content": "• 112: 消防急救特警火警电话 (Feuerwehr & Rettungsdienst)\n• 110: 治安报警警察热线 (Polizei)\n• 116 117: 非急危重症非执业时间值班医生热线 (Ärztlicher Bereitschaftsdienst)"
                }
            ]
        },
        "quiz": [
            {
                "id": "A2_L08_Q1",
                "type": "GRAMMAR_FILL",
                "question": "Der Arzt hat mir geraten, ______ (连词) ich mich schonen soll.",
                "options": ["dass", "weil", "wenn", "ob"],
                "correctIndex": 0,
                "explanation": "引出医生建议的具体内容从句，使用宾语从句连词 dass。"
            },
            {
                "id": "A2_L08_Q2",
                "type": "EXAM_REAL",
                "question": "在德国遇到突发严重火灾或生命垂危病患，应拨打的欧盟统一急救电话是：",
                "options": ["112", "110", "120", "911"],
                "correctIndex": 0,
                "explanation": "112 是全欧洲统一的急救火警电话 (Rettungsdienst und Feuerwehr)。"
            }
        ],
        "words": [
            ("der Notfall", "der", "n.", "Notfälle", "紧急险情，突发急症", "Im Notfall wählen Sie europaweit die Nummer 112!", "如遇突发紧急险情，请在全欧境内直拨112急救！"),
            ("die Notaufnahme", "die", "n.", "-n", "综合医院急诊大厅", "Schwerverletzte werden sofort in die Notaufnahme gebracht.", "受重伤的伤员被紧急送往综合医院急诊大厅救治。"),
            ("der Rettungsdienst", "der", "n.", "-e", "医疗院前急救机构", "Der Rettungsdienst traf nach sieben Minuten am Unfallort ein.", "院前急救车组在事发七分钟内便雷厉风行抵达现场。"),
            ("der Notarzt", "der", "n.", "Notärzte", "现场急救执业医师", "Der erfahrene Notarzt stabilisierte den Patienten.", "经验老道的随车急救医师迅速稳定住了病患生命体征。"),
            ("der Sanitäter", "der", "n.", "-", "随车急救医学技士", "Die Sanitäter hoben die Trage vorsichtig an.", "急救医疗救护员十分稳当地抬起了担架将伤者运送。"),
            ("der Rettungswagen", "der", "n.", "-", "抢救监护急救车", "Der Rettungswagen raste mit Blaulicht und Martinshorn.", "急救车闪烁着醒目蓝警灯、鸣响笛声在主道极速飞驰。"),
            ("die Erste Hilfe", "die", "n.", "-", "现场徒手应急初级急救", "Jeder Autofahrer muss einen Kurs in Erster Hilfe belegen.", "每位机动车考本驾驶员均需通过初级急救实操认证。"),
            ("der Verbandskasten", "der", "n.", "Verbandskästen", "车载应急急救药箱", "Im Auto muss ein vollständiger Verbandskasten liegen.", "车厢内部依法必须常备一个封条完好的急救包药箱。"),
            ("die Ambulanz", "die", "n.", "-en", "急救流动站；门诊", "In der chirurgischen Ambulanz wird die Platzwunde genäht.", "在急诊外科处置室内医生正在清创缝合头部挫裂创口。"),
            ("die Praxis", "die", "n.", "Praxen", "医生私人执业门诊所", "Die Praxisgemeinschaft umfasst drei Fachärzte.", "该联合执业门诊部汇聚了三位声誉极佳的专科名医。"),
            ("der Hausarzt", "der", "n.", "Hausärzte", "签约家庭全科医生", "Bei ersten Krankheitssymptomen geht man zum Hausarzt.", "身体初现不适病症时通常应首先前往签约全科就诊。"),
            ("der Facharzt", "der", "n.", "Fachärzte", "专科主任医师", "Der Hausarzt stellt eine Überweisung zum Facharzt aus.", "全科医生据病情出具了一张转诊专科的官方转诊单。"),
            ("der Zahnarzt", "der", "n.", "Zahnärzte", "齿科执业牙医", "Zweimal jährlich zur professionellen Kontrolle zum Zahnarzt.", "每年按规矩应前往牙科诊所进行两次常规健康洁牙。"),
            ("der Augenarzt", "der", "n.", "Augenärzte", "眼科主任专科医生", "Der Augenarzt überprüft die Sehschärfe beider Augen.", "眼科医生对当事人的双眼视力水平做了精准验光。"),
            ("der HNO-Arzt", "der", "n.", "-ärzte", "耳鼻喉科专科医师", "Wegen anhaltender Halsschmerzen suche ich den HNO-Arzt auf.", "因咽喉久痛不愈我专程预约挂了耳鼻喉专科门诊。"),
            ("der Kinderarzt", "der", "n.", "Kinderärzte", "儿科主治医生", "Der Kinderarzt führt die vorgeschriebenen U-Untersuchungen durch.", "儿科医生为适龄婴幼童进行国家法定的生长发育筛查。"),
            ("die Krankenkasse", "die", "n.", "-n", "法定医疗健康保险机构", "Die gesetzliche Krankenkasse übernimmt die Behandlungskosten.", "国家法定公立医保基金将全额核销本次医疗全部开支。"),
            ("die Versicherung", "die", "n.", "-en", "社会保险与商业险", "Sind Sie gesetzlich oder privat versichert?", "您参加的是国家法定公立医保还是商业私立高阶医疗险？"),
            ("die Versichertenkarte", "die", "n.", "-n", "电子芯片社保医保卡", "Stecken Sie Ihre elektronische Gesundheitskarte ins Lesegerät!", "请将您的智能电子健康医保卡插入前台读卡机识别！"),
            ("die Zuzahlung", "die", "n.", "-en", "自负共付自缴金额", "In der Apotheke leistet der Patient eine geringe Zuzahlung.", "在药房取处方药时患者本人仅需支付极微薄的自负金。"),
            ("das Rezept", "das", "n.", "-e", "专科医生处方单", "Das rosa Rezept ist für verschreibungspflichtige Medikamente.", "粉红色处方笺专门针对纳入国家医保报销的处方药。"),
            ("die Apotheke", "die", "n.", "-n", "社会执业药房药店", "Die Notdienst-Apotheke hat auch sonntags durchgehend auf.", "负责区域值班轮值的应急药店在星期天也全天营业。"),
            ("das Medikament", "das", "n.", "-e", "制剂药品，医药品", "Nehmen Sie dieses Medikament bitte nach den Mahlzeiten ein!", "请在每日三餐饭后十分钟内就温开水服用这种药品！"),
            ("die Packungsbeilage", "die", "n.", "-n", "药品官方使用说明书", "Lesen Sie die Packungsbeilage und fragen Sie Ihren Arzt!", "请仔细研读包装盒内说明书并谨遵医嘱或咨询药师！"),
            ("die Nebenwirkung", "die", "n.", "-en", "不良药物副反应", "Müdigkeit ist eine bekannte Nebenwirkung dieses Mittels.", "嗜睡疲乏是服用该款抗过敏药极其常见的不良反应。"),
            ("die Dosierung", "die", "n.", "-en", "药物剂量服法", "Überschreiten Sie keinesfalls die empfohlene Dosierung!", "在任何情形下都切莫擅自超量服用超出推荐处方量！"),
            ("die Tablette", "die", "n.", "-n", "药片，压制片剂", "Schlucken Sie täglich eine Tablette mit ausreichend Wasser!", "请每日清晨随大半杯温水整粒吞服下一片降压药片！"),
            ("die Kapsel", "die", "n.", "-n", "肠溶胶囊，胶囊", "Die Kapsel löst sich erst im Magen-Darm-Trakt auf.", "此硬胶囊在进入人体胃肠道后才会缓慢崩解吸收。"),
            ("die Tropfen", "die", "n.pl.", "-", "药水滴剂（复数）", "Geben Sie dreimal täglich zwanzig Tropfen in etwas Wasser!", "每日三次向少许清水中滴加二十滴药水随后饮服。"),
            ("die Salbe", "die", "n.", "-n", "药用外涂软膏", "Tragen Sie die entzündungshemmende Salbe dünn auf die Haut auf!", "将这管消炎镇痛软膏在发红皮损处轻柔涂抹薄薄一层！"),
            ("das Pflaster", "das", "n.", "-", "医用透气创口贴", "Ein steriles Pflaster schützt die Schnittwunde vor Schmutz.", "一张无菌创可贴能阻隔外界脏污灰尘感染细小切口。"),
            ("die Spritze", "die", "n.", "-n", "注射针剂，注射器", "Der Arzt gibt dem Patienten eine schmerzstillende Spritze.", "大夫当机立断给疼痛难耐的病患肌注了一剂止痛针。"),
            ("die Impfung", "die", "n.", "-en", "免疫接种，疫苗针", "Eine jährliche Impfung schützt wirksam gegen echte Grippe.", "每年按时接种流感疫苗能够有效抵御突发流感病毒。"),
            ("die Allergie", "die", "n.", "-n", "变态反应，过敏症", "Er leidet im Frühling an einer heftigen Pollenallergie.", "每逢春暖花开之际他便饱受极其剧烈的花粉过敏折磨。"),
            ("das Symptom", "das", "n.", "-e", "临床表现，病理症状", "Typische Symptome einer Bronchitis sind Husten und Fieber.", "支气管炎的经典典型临床症状表现为剧咳与高烧。"),
            ("die Entzündung", "die", "n.", "-en", "炎性反应，炎症", "Die Mandelentzündung muss mit Antibiotika behandelt werden.", "急性化脓性扁桃体炎通常需按医嘱使用抗生素治疗。"),
            ("die Infektion", "die", "n.", "-en", "病原微生物感染", "Vermeiden Sie den Kontakt, um eine Infektion zu verhindern!", "请尽量减少密切接触以切断并预防交叉飞沫感染！"),
            ("das Fieber", "das", "n.", "-", "病理发热，发烧", "Bei Fieber über 39 Grad sollte man einen Arzt hinzuziehen.", "一旦体温计读数超过39度应果断前往医疗机构就医。"),
            ("messen", "", "v.", "misst, maß, gemessen", "检定测量体征", "Die Krankenschwester misst Puls, Blutdruck und Temperatur.", "当班护士极其专业地测量了心率脉搏、血压及体温。"),
            ("das Thermometer", "das", "n.", "-", "医用电子体温计", "Das digitale Thermometer misst die Körperwärme in Sekunden.", "数字化医用体温计可在短短数秒内读出精准体温。"),
            ("der Blutdruck", "der", "n.", "-", "血管动脉血压", "Regelmäßige Bewegung senkt den zu hohen Blutdruck.", "持之以恒的科学有氧锻炼有助于良性调节高血压。"),
            ("der Puls", "der", "n.", "-e", "脉搏搏动跳动", "Der Puls schlägt ruhig mit siebzig Schlägen pro Minute.", "当事人脉搏跳动极为平稳，每分钟标准跳动七十次。"),
            ("die Schmerzen", "die", "n.pl.", "-", "肢体脏器疼痛感", "Gegen die dumpfen Schmerzen hilft eine Wärmflasche.", "在腹部敷上一个热水袋有助于缓和深层的隐隐钝痛。"),
            ("leiden", "", "v.", "leidet, litt, gelitten", "饱受疾苦 (unter/an + Dat)", "Viele Büroangestellte leiden unter chronischen Rückenschmerzen.", "不少久坐办公室的职员都饱受慢性腰背酸痛的折磨。"),
            ("fehlen", "", "v.", "fehlt, fehlte, gefehlt", "感觉不适；欠缺", "Was fehlt Ihnen denn? Erzählen Sie ganz in Ruhe!", "您究竟是哪里不舒坦？请放轻松慢慢跟我详细道来！"),
            ("untersuchen", "", "v.", "untersucht, untersuchte, untersucht", "体格检查，听诊", "Der Kardiologe untersucht gründlich das Herz mit Ultraschall.", "心脏科专家细致入微地借助彩色超声排查心脏机能。"),
            ("die Untersuchung", "die", "n.", "-en", "医学临床化验检查", "Die labormedizinische Untersuchung ergab keinen Befund.", "全面化验室指标血液检测结果显示未见任何异常。"),
            ("der Befund", "der", "n.", "-e", "临床诊断检验结果", "Der radiologische Befund schließt einen Knochenbruch aus.", "放射科X光诊断意见明确排除了发生骨折的可能性。"),
            ("die Diagnose", "die", "n.", "-n", "疾病正式临床确诊", "Nach der Auswertung aller Daten stellte die Ärztin die Diagnose.", "综合评判所有生化指标后女医生做出了精准的诊断。"),
            ("die Krankschreibung", "die", "n.", "-en", "休假就诊病假单", "Die Ärztin händigt mir eine dreitägige Krankschreibung aus.", "女医生签字开具并递给我一份为期三天的全休病假条。"),
            ("arbeitsunfähig", "", "adj.", "", "丧失工作能力需病休的", "Der Patient ist vorübergehend für zwei Wochen arbeitsunfähig.", "该名病患目前暂时性丧失工作能力需严格居家休养。"),
            ("das Attest", "das", "n.", "-e", "专科医疗诊断鉴定", "Reichen Sie das ärztliche Attest binnen drei Tagen beim Arbeitgeber ein!", "请在三日内将就诊诊断书及时呈报用人单位人事处！"),
            ("der Unfall", "der", "n.", "Unfälle", "意外突发交通事故", "Der Radfahrer hatte Glück im Unglück bei dem schweren Unfall.", "骑行人员在这起恶劣严重车祸中可谓是不幸中的万幸。"),
            ("die Verletzung", "die", "n.", "-en", "机体外伤损伤", "Die Verletzung am Schienbein verheilt dank guter Pflege zügig.", "由于护理得当其小腿迎面骨处的挫裂伤恢复极快。"),
            ("bluten", "", "v.", "blutet, blutete, geblutet", "创面流血渗血", "Die Wunde blutet kaum noch und sieht sauber aus.", "创口已经完全止血不再渗血，外观看起来十分洁净。"),
            ("das Pflaster", "das", "n.", "-", "创口护创胶贴", "Kleben Sie ein wasserdichtes Pflaster über den Einstich!", "在针眼注射穿刺点处贴上一枚医用透气防水小敷贴！"),
            ("der Verband", "der", "n.", "Verbände", "外科缠绕包扎绷带", "Der Pfleger legte einen elastischen Verband um das Gelenk.", "男护士动作十分麻利地在脚踝关节处缠上了弹力绷带。"),
            ("das Röntgenbild", "das", "n.", "-er", "放射科X射线拍片", "Auf dem Röntgenbild ist der glatte Bruch deutlich erkennbar.", "在清晰的X光片上可以明显辨析出那道齐整的骨折线。"),
            ("der Gips", "der", "n.", "-e", "外科固定定型石膏", "Er muss den Gipsverband am Bein sechs Wochen lang tragen.", "他腿部打上的这具定型固定石膏必须持续保留六周。"),
            ("die Krücke", "die", "n.", "-n", "手摇助力拐杖", "Sie geht nach der Knieoperation mühsam an Krücken.", "在实施膝关节镜手术后她拄着一副双拐艰辛慢步行走。"),
            ("die Operation", "die", "n.", "-en", "外科手术，施术", "Die komplizierte Operation verlief ohne jede Komplikation.", "这台耗时长久的复杂大手术实施得极其圆满无并发症。"),
            ("operieren", "", "v.", "operiert, operierte, operiert", "开刀施行手术", "Der erfahrene Chefarzt operiert den Bandscheibenvorfall.", "经验老道的专科大主任亲自挂帅为椎间盘突出开刀。"),
            ("die Narkose", "die", "n.", "-n", "全身或局部麻醉", "Der Anästhesist klärt den Patienten über die Vollnarkose auf.", "麻醉主治医生耐心地向患者详尽交代全麻术前注意事项。"),
            ("das Krankenhaus", "das", "n.", "Krankenhäuser", "大型综合公立医院", "Die Universitätsklinik ist das größte Krankenhaus der Region.", "这座大学附属临床教学医院是大区最具声望的医疗中心。"),
            ("die Station", "die", "n.", "-en", "住院病区，住院部", "Der Patient liegt auf Station 4 im Zimmer 408.", "该住院病患被妥善安置于四病区408号二人病房内。"),
            ("die Krankenschwester", "die", "n.", "-n", "病房执业女护士", "Die Krankenschwester bringt pünktlich die verordneten Tabletten.", "病房值班护士准时将医生开出的处方片剂端到床头。"),
            ("der Krankenpfleger", "der", "n.", "-", "病房执业男护士", "Der Krankenpfleger kontrolliert regelmäßig den Tropf.", "男护师定期进病房巡视并仔细复核静脉输液滴速。"),
            ("die Genesung", "die", "n.", "-", "身体痊愈，康复期", "Wir wünschen Ihnen eine rasche und vollständige Genesung!", "我们由衷祝愿您能够尽快彻底战胜疾病早日完全康复！"),
            ("die Besserung", "die", "n.", "-", "病况好转，起色", "Gute Besserung und schonen Sie sich in den nächsten Tagen!", "祝早日康复，未来这几天请务必彻底放下工作好生静养！"),
            ("schonen", "", "v.", "schont, schonte, geschont", "自我爱护，保重静养", "Schonen Sie nach dem Eingriff bitte Ihren Kreislauf!", "术后请务必注意卧床休息，避免心血管负担过重！")
        ]
    },

    # LESSON 9
    {
        "id": "A2_L09",
        "title": "第9课：德语区特色美食、餐饮文化与烹饪 (Gastronomie & Kochen)",
        "summary": "掌握被动语态现在时入门 (werden + Partizip II)、传统德系烹饪食材与餐桌礼仪",
        "grammar": {
            "title": "过程被动语态 (Vorgangspassiv Präsens) 入门",
            "sections": [
                {
                    "heading": "1. 现在时被动语态构成：werden (变位) + Partizip II (第二分词句末)",
                    "content": "• ich werde, du wirst, er wird, wir werden, ihr werdet, sie/Sie werden\n• 例句：Die Kartoffeln werden geschält und gekocht. (土豆被削皮并被煮熟。)\n• Fleisch wird gebraten. / Suppe wird serviert."
                },
                {
                    "heading": "2. 动作发出者由 von + Dativ 引导",
                    "content": "Das traditionelle Brot wird vom Meisterbäcker gebacken."
                }
            ]
        },
        "quiz": [
            {
                "id": "A2_L09_Q1",
                "type": "GRAMMAR_FILL",
                "question": "Das beliebte Gericht ______ (werden) frisch in der Pfanne zubereitet.",
                "options": ["wird", "werdet", "wurde", "worden"],
                "correctIndex": 0,
                "explanation": "主语 Das Gericht 是单数第三人称，现在时被动助动词形式为 wird。"
            },
            {
                "id": "A2_L09_Q2",
                "type": "VOCAB_MEANING",
                "question": "德语菜谱烹饪指导中的核心动词 'schälen' 意思是：",
                "options": ["剥皮，削皮", "切碎，剁碎", "水煮，炖煮", "油炸，烘焙"],
                "correctIndex": 0,
                "explanation": "schälen 是烹饪中极常用的动词，指给蔬菜、土豆、水果等削皮、剥皮。"
            }
        ],
        "words": [
            ("die Gastronomie", "die", "n.", "-", "餐饮服务行业，美食界", "Die deutsche Gastronomie setzt vermehrt auf Bio-Produkte.", "德国餐饮服务业正日益侧重于甄选优质有机农产。"),
            ("die Spezialität", "die", "n.", "-en", "地方风味特产，名菜", "Käsespätzle sind eine schwäbische Spezialität.", "奶酪碎面条是施瓦本地区名扬四海的风味特色菜肴。"),
            ("das Rezept", "das", "n.", "-e", "烹饪菜谱，食谱", "Das überlieferte Rezept stammt von meiner Urgroßmutter.", "这道原汁原味的历史食谱直接承袭自我曾祖母的手艺。"),
            ("die Zutat", "die", "n.", "-en", "烹饪原料配料，食材", "Für den Kuchen braucht man nur fünf einfache Zutaten.", "烘焙这个家常蛋糕只需要五样普普通通的基础原料。"),
            ("die Zubereitung", "die", "n.", "-en", "烹调加工步骤，制法", "Die Zubereitung dauert kaum länger als zwanzig Minuten.", "整套菜肴的烹调下锅步骤耗时统共超不过二十分钟。"),
            ("zubereiten", "", "v.", "bereitet zu, bereitete zu, zubereitet", "加工烹制，制作", "Er bereitet das Menü mit viel Liebe zum Detail zu.", "他在后厨精益求精地打磨并烹制着全套晚宴餐点。"),
            ("kochen", "", "v.", "kocht, kochte, gekocht", "炖煮；做饭做菜", "Lassen Sie das Gemüse bei geringer Hitze sanft kochen!", "让新鲜时蔬在文火小火中慢慢炖煮收汁入味！"),
            ("backen", "", "v.", "bäckt, backte, gebacken", "烤炉烘焙制成", "Der Bäcker bäckt traditionelles Sauerteigbrot im Steinofen.", "师傅在柴火石窑炉中手工烤制着传统天然酸面团面包。"),
            ("braten", "", "v.", "brät, briet, gebraten", "热油煎，油炸煎炒", "Braten Sie das Steak von jeder Seite zwei Minuten scharf an!", "将上等牛排在热锅中每面以高温大火迅猛干煎两分钟！"),
            ("grillen", "", "v.", "grillt, grillte, gegrillt", "炭火铁板烧烤", "Im sonnigen Sommer grillen wir gerne saftige Würstchen.", "在阳光明媚的夏天大家聚在院里大快朵颐烤多汁香肠。"),
            ("schneiden", "", "v.", "schneidet, schnitt, geschnitten", "用刀切碎，切成块", "Schneiden Sie die Zwiebeln in feine Würfel!", "请拿起厨刀将洋葱手脚麻利地均匀细细切碎成小方丁！"),
            ("schälen", "", "v.", "schält, schälte, geschält", "削皮去皮，剥壳", "Vor dem Kochen muss man die Kartoffeln sorgsam schälen.", "在下锅煮之前必须先细致用削皮刀给土豆剥去表皮。"),
            ("reiben", "", "v.", "reibt, rieb, gerieben", "用擦子磨碎，刨丝", "Frischer Parmesan wird direkt über die heiße Pasta gerieben.", "刚出锅的滚烫意面上直接手磨擦洒上一层细腻帕玛森。"),
            ("mischen", "", "v.", "mischt, mischte, gemischt", "搅拌混合配伍", "Mischen Sie Essig und feines Olivenöl zu einer Vinaigrette!", "将香醋与冷榨橄榄油充分搅打乳化混合成油醋汁调料！"),
            ("rühren", "", "v.", "rührt, rührte, gerührt", "手持勺搅拌翻动", "Rühren Sie die sämige Sauce im Topf ununterbrochen um!", "用木勺在汤锅里不停搅拌酱汁以免粘锅底或出现结块！"),
            ("würzen", "", "v.", "würzt, würzte, gewürzt", "撒料调味加作料", "Würzen Sie das Gericht dezent mit Salz und weißem Pfeffer!", "请用适量食用细盐与现磨白胡椒粉为菜肴画龙点睛调味！"),
            ("das Gewürz", "das", "n.", "-e", "烹饪香辛作料，香料", "Exotische Gewürze verleihen der Speise ein feines Aroma.", "异域特色天然香辛料赋予了这道美食极其曼妙的幽香。"),
            ("das Salz", "das", "n.", "-", "精制食用盐", "Eine Prise Salz hebt den Eigengeschmack des Kuchens.", "烘焙时加入一小撮细盐能奇妙烘托出糕点本身的香甜。"),
            ("der Pfeffer", "der", "n.", "-", "辛香胡椒，胡椒碎", "Schwarzer Pfeffer aus der Mühle schmeckt unvergleichlich aromatisch.", "研磨器现场现碾出的新鲜黑胡椒碎香气极其浓郁芬芳。"),
            ("der Knoblauch", "der", "n.", "-", "大蒜，蒜头蒜泥", "Eine fein zerdrückte Zehe Knoblauch rundet den Geschmack ab.", "一瓣细细压榨成的蒜泥能让整盘意大利面的底味升华。"),
            ("die Petersilie", "die", "n.", "-", "法香，欧芹碎", "Frisch gehackte Petersilie wird als Garnitur darüber gestreut.", "将刚切好的青翠欧芹碎作为精致点缀轻柔撒在汤羹上。"),
            ("das Basilikum", "das", "n.", "-", "甜罗勒叶，罗勒", "Frisches Basilikum harmoniert perfekt mit reifen Tomaten.", "现摘的新鲜罗勒嫩叶与红透成熟的多汁番茄是绝配天作之合。"),
            ("der Senf", "der", "n.", "-e", "黄芥末酱", "Zur originalen Weißwurst gehört süßer bayerischer Senf.", "享用正宗慕尼黑白香肠必须佐以地道巴伐利亚甜芥末酱。"),
            ("die Mayonnaise", "die", "n.", "-n", "蛋黄酱，美乃滋", "Pommes frites werden gerne mit Ketchup und Mayonnaise gegessen.", "炸薯条最普遍也最诱人的标配吃法是蘸番茄酱与美乃滋。"),
            ("der Ketchup", "der", "n.", "-s", "番茄沙司沙司酱", "Kinder essen Nudeln am liebsten mit fruchtigem Ketchup.", "小孩子们吃面条时最钟情于拌上酸酸甜甜的浓稠番茄酱。"),
            ("die Bratwurst", "die", "n.", "Bratwürste", "炭火铁板烤香肠", "Eine Thüringer Bratwurst frisch vom dampfenden Holzkohlegrill.", "一根直接从热气升腾的炭火烤炉上夹出的图林根烤香肠。"),
            ("die Currywurst", "die", "n.", "Currywürste", "柏林特色咖喱香肠", "Die Currywurst ist der unangefochtene Streetfood-Klassiker Berlins.", "咖喱香肠是德国首都柏林街头小吃界毫无争议的头牌经典。"),
            ("das Sauerkraut", "das", "n.", "-", "传统酸椰菜，酸菜", "Traditionelles Sauerkraut wird schonend mit Wacholderbeeren gegart.", "传统腌制酸白菜文火慢炖时常配以几颗杜松子提鲜解腻。"),
            ("die Brezel", "die", "n.", "-n", "碱水面包扭结圈", "Eine frisch gebackene Laugenbrezel mit grobem Meersalz.", "一个刚出炉表面撒着粗粒天然海盐的香脆碱水扭结面包。"),
            ("der Knödel", "der", "n.", "-", "土豆面粉大丸子", "Semmelknödel passen hervorragend zu deftigem Schweinebraten.", "松软的大面包丸子佐以浓油赤酱的烤猪肉堪称无上美味。"),
            ("der Kloß", "der", "n.", "Klöße", "大团子丸子（北德称谓）", "Thüringer Klöße aus rohen und gekochten Kartoffeln.", "用生熟土豆精细配比制成的享誉四方的图林根大土豆团子。"),
            ("der Braten", "der", "n.", "-", "大块慢烤整肉，烤肉", "Am gemütlichen Sonntag duftet das ganze Haus nach Sonntagsbraten.", "在惬意的星期天整栋房子都弥漫着周日传统烤肉的浓郁肉香。"),
            ("das Schnitzel", "das", "n.", "-", "厚切炸肉排", "Ein zartes Schnitzel Wiener Art mit knuspriger Panade.", "一块裹有金黄酥脆面包糠外壳的鲜嫩维也纳风味炸肉排。"),
            ("der Eintopf", "der", "n.", "Eintöpfe", "一锅烩浓汤乱炖", "Ein deftiger Linseneintopf wärmt im tiefsten Winter durch.", "一碗热气腾腾扎实抗饿的扁豆杂烩汤能驱散数九隆冬严寒。"),
            ("die Vorspeise", "die", "n.", "-n", "开胃前菜小碟", "Als leichte Vorspeise servieren wir einen bunten Feldsalat.", "我们率先呈上一道以新鲜野苣菜拌制的爽口轻负担开胃前菜。"),
            ("das Hauptgericht", "das", "n.", "-e", "晚宴主轴主菜", "Das Hauptgericht besteht aus rosa gebratenem Lammrücken.", "正餐的主菜是火候拿捏得恰到好处、内里粉嫩的香烤羊排。"),
            ("das Dessert", "das", "n.", "-s", "精致饭后甜点甜品", "Zum krönenden Dessert empfiehlt die Küche hausgemachtes Tiramisu.", "主厨力荐以自制提拉米苏作为整场完美盛宴压轴收官的甜点。"),
            ("der Nachtisch", "der", "n.", "-e", "甜后点心，甜食", "Die Kinder freuen sich immer riesig auf den süßen Nachtisch.", "小家伙们在餐桌上总是望眼欲穿满心欢喜期盼着饭后甜食。"),
            ("die Nachspeise", "die", "n.", "-n", "餐后甘点", "Rote Grütze mit Vanillesauce ist eine typisch norddeutsche Nachspeise.", "红浆果布丁配浓香香草甜酱是极具北德水乡特色的经典甜品。"),
            ("die Portion", "die", "n.", "-en", "盘份，餐点分量", "Die Portionen im Landgasthof sind traditionell sehr großzügig.", "这家乡间客栈端上来的菜肴分量历来都极其厚道扎实实在。"),
            ("nachbestellen", "", "v.", "bestellt nach, bestellte nach, nachbestellt", "加菜加单，追加", "Darf ich bitte noch einen Korb mit frischem Baguette nachbestellen?", "请问我能劳烦服务员给加点一份新鲜烘烤的面包法棍吗？"),
            ("probieren", "", "v.", "probiert, probierte, probiert", "浅尝，品鉴味道", "Probieren Sie unbedingt ein Stück von diesem würzigen Bergkäse!", "请您务必亲口品尝一块这种风味极其纯正浓醇的高山奶酪！"),
            ("kosten", "", "v.", "kostet, kostete, gekostet", "品尝味道；花费", "Kosten Sie die Sauce, ob noch etwas edler Essig fehlt!", "请您尝尝这勺浓汁，看是否还需要补滴几滴上好陈酿香醋！"),
            ("schmecken", "", "v.", "schmeckt, schmeckte, geschmeckt", "品味，尝起来如何", "Das selbst gekochte Essen schmeckt allen Familienmitgliedern vorzüglich.", "亲手下厨烹制的爱心饭菜让全家老小无一不吃得心满意足。"),
            ("köstlich", "", "adj.", "köstlicher, am köstlichsten", "玉盘珍馐，可口极品", "Der fangfrische Zander schmeckte einfach himmlisch und köstlich.", "刚捕捞上岸的新鲜梭鲈鱼尝起来简直是人间极品鲜美至极。"),
            ("aromatisch", "", "adj.", "aromatischer, am aromatischsten", "香气四溢芳香的", "Der frisch gemahlene Espresso duftet unwiderstehlich aromatisch.", "现磨萃取的意式浓缩咖啡弥漫着令人欲罢不能的浓醇焦香。"),
            ("mild", "", "adj.", "milder, am mildesten", "清淡温和不刺激的", "Für empfindliche Mägen eignet sich milder Früchtetee besonders gut.", "对于肠胃娇弱敏感者来说性质极其温和的花果茶最为适宜。"),
            ("scharf", "", "adj.", "schärfer, am schärfsten", "火辣辛辣的", "Chili und frischer Ingwer machen die asiatische Suppe pikant und scharf.", "小米辣搭配老姜碎赋予了这碗亚洲风味浓汤鲜明热烈的辛辣。"),
            ("bitter", "", "adj.", "bitterer, am bittersten", "苦味微苦的", "Chicorée hat von Natur aus eine angenehm herbe, bittere Note.", "苦苣蔬菜天生便自带一种令人身心愉悦清爽的独特清苦风味。"),
            ("saftig", "", "adj.", "saftiger, am saftigsten", "多汁水润的", "Ein saftiger Pfirsich ist die perfekte Erfrischung im Hochsommer.", "一口咬下汁水四溢的多汁甜桃是盛夏消暑解渴的无上妙品。"),
            ("knusprig", "", "adj.", "knuspriger, am knusprigsten", "嘎嘣酥脆的", "Die Kruste des Steinofenbrotes ist herrlich dunkel und knusprig.", "石炉慢烤欧包的外皮呈现诱人的深琥珀色且嚼起来嘎嘣酥脆。"),
            ("zart", "", "adj.", "zarter, am zartesten", "软嫩化渣的", "Das Fleisch schmort drei Stunden und wird butterweich und zart.", "经过三小时小火慢炖的大块牛腩变得如黄油般软烂化渣鲜嫩。"),
            ("zäh", "", "adj.", "zäher, am zähesten", "老硬咬不动的", "Wenn man das Steak zu lange brät, wird es leider trocken und zäh.", "牛排要是煎得火候过头，内里肉质就会变得柴硬干涩难以下咽。"),
            ("roh", "", "adj.", "roher, am rohesten", "生的，未熟加工的", "Mettbrötchen mit rohem Schweinehackfleisch sind in Deutschland Kult.", "涂满调味生猪肉糜的撒葱圆面包在德国本土是极具情怀的吃法。"),
            ("gekocht", "", "adj.", "", "水煮烹熟的", "Ein hart gekochtes Ei gehört für viele zum perfekten Sonntagsfrühstück.", "一颗全熟的水煮溏心蛋对很多人而言是惬意周末早餐的灵魂标配。"),
            ("gebraten", "", "adj.", "", "香煎烹炒好的", "Gebratene Nudeln mit knackigem Gemüse und geröstetem Sesam.", "一盘镬气十足、拌有爽脆时蔬与烘烤白芝麻喷香的炒面条。"),
            ("gebacken", "", "adj.", "", "炉烤出炉的", "Frisch gebackene Waffeln verbreiten einen Duft von warmer Vanille.", "刚从铁板华夫模具中起锅的华夫饼散发出阵阵温暖的香草气息。"),
            ("vegetarisch", "", "adj.", "", "素食蛋奶素的", "Die Speisekarte weist vegetarische Gerichte mit einem grünen Blatt aus.", "菜单上所有不沾肉类的素食菜品边上都醒目标注了一片绿叶。"),
            ("vegan", "", "adj.", "", "纯素无动物制品的", "Immer mehr Gäste ernähren sich aus ethischen Gründen rein vegan.", "出于动物保护等伦理关怀，越来越多食客推崇全植物纯素饮食。"),
            ("die Unverträglichkeit", "die", "n.", "-en", "食物不耐受症", "Bei einer Laktose-Unverträglichkeit meidet man normale Kuhmilch.", "罹患乳糖不耐受症的群体通常会主动避免饮用普通未经降解的牛奶。"),
            ("das Bier", "das", "n.", "-e", "传统酿造精酿啤酒", "Das deutsche Reinheitsgebot von 1516 regelt streng das Bierbrauen.", "颁布于1516年的德国啤酒纯净法极其严格地规约着纯粮酿造工艺。"),
            ("das Pils", "das", "n.", "-e", "皮尔森下层发酵清啤", "Ein kühles Pils mit einer dichten, weißen Schaumkrone zapfen.", "打出一杯酒体金黄清透、顶着一层绵密雪白泡沫的冰镇皮尔森。"),
            ("das Weizenbier", "das", "n.", "-e", "巴伐利亚小麦白啤酒", "Ein hefetrübes Weizenbier wird traditionell aus dem hohen Glas getrunken.", "未经过滤浑浊浓香的小麦白啤历来习惯倒入细长专用大杯豪饮。"),
            ("der Wein", "der", "n.", "-e", "干红干白高档葡萄酒", "Deutschland ist international für rassigen Riesling-Weißwein berühmt.", "德国在国际酒界享有崇高声望的当属口感清脆凌厉的雷司令白葡萄酒。"),
            ("die Schorle", "die", "n.", "-n", "果汁兑气泡水特调", "Eine kühle Apfelschorle ist der beliebteste Durstlöscher nach dem Sport.", "一杯清凉爽口的苹果汁兑气泡水是德国大众运动后最爱的解渴圣品。"),
            ("der Schnaps", "der", "n.", "Schnäpse", "高烈度粮食果馏烈酒", "Nach dem opulenten Mahl trinkt man zur Verdauung einen Kräuterschnaps.", "在饱餐大快朵颐大鱼大肉之后人们常喝一小盅草本利口烈酒助消化。"),
            ("das Trinkgeld", "das", "n.", "-er", "对周到服务的犒赏小费", "In der Gastronomie sind fünf bis zehn Prozent Trinkgeld üblich.", "在德国餐饮场所通常约定俗成会给服务生留下百分之五至十的小费。"),
            ("stimmen", "", "v.", "stimmt, stimmte, gestimmt", "正确无讹；账实相符", "Geben Sie auf 50 Euro heraus, der Rest stimmt so als Trinkgeld!", "按50欧整找零即可，剩下的零钱权当犒劳您的小费不用再找啦！"),
            ("die Gastfreundschaft", "die", "n.", "-", "宾至如归的待客之道", "Die herzliche Gastfreundschaft der Wirtsleute hat uns tief berührt.", "客栈掌柜夫妇发自肺腑的热忱好客之道深深打动并温暖了我们。"),
            ("einladen", "", "v.", "lädt ein, lud ein, eingeladen", "做东宴请，慷慨请客", "Heute Abend übernehme ich die Zeche und lade euch alle herzlich ein!", "今天晚上这顿算我的由我来做东埋单，诚挚邀请大家敞开痛快吃！")
        ]
    },

    # LESSON 10
    {
        "id": "A2_L10",
        "title": "第10课：穿衣时尚、外貌性格与人际印象 (Mode, Aussehen & Charakter)",
        "summary": "掌握形容词弱变化与混合变化、人物肖像外貌描写与性格特征剖析",
        "grammar": {
            "title": "不定冠词后的形容词词尾变化（混合变化）",
            "sections": [
                {
                    "heading": "1. 不定冠词 (ein/kein/mein) 后的形容词词尾",
                    "content": "• 第一格：ein netter Mann (-er) / eine nette Frau (-e) / ein nettes Kind (-es) / keine netten Leute (-en)\n• 第四格：einen netten Mann (-en) / eine nette Frau (-e) / ein nettes Kind (-es) / keine netten Leute (-en)\n• 第三格与第二格：一律加 -en！(mit einem netten Mann / einer netten Frau)"
                },
                {
                    "heading": "2. 人物外貌与性格高频描写句型",
                    "content": "• Er sieht sympathisch / attraktiv / sportlich aus.\n• Sie hat glatte / lockige blonde Haare und braune Augen.\n• Er ist hilfsbereit, zuverlässig und hat viel Humor."
                }
            ]
        },
        "quiz": [
            {
                "id": "A2_L10_Q1",
                "type": "GRAMMAR_FILL",
                "question": "Er ist ein ______ (zuverlässig, 第一格阳性混合变化) Kollege.",
                "options": ["zuverlässiger", "zuverlässigen", "zuverlässige", "zuverlässiges"],
                "correctIndex": 0,
                "explanation": "不定冠词第一格阳性 (ein)，形容词加上格标记 -er：ein zuverlässiger Kollege。"
            },
            {
                "id": "A2_L10_Q2",
                "type": "VOCAB_MEANING",
                "question": "形容一个人极其“靠谱守信、值得托付”，德语最核心的高频词是：",
                "options": ["zuverlässig", "arrogant", "faul", "pünktlich"],
                "correctIndex": 0,
                "explanation": "zuverlässig 意为“可靠的、信得过的”，是德语人际评价中使用频率极高的褒义词。"
            }
        ],
        "words": [
            ("das Aussehen", "das", "n.", "-", "容貌外表，仪态形象", "Ein gepflegtes Aussehen öffnet im Berufsleben viele Türen.", "整洁得体的个人仪容外表在职场交际中能开启许多大门。"),
            ("aussehen", "", "v.", "sieht aus, sah aus, ausgesehen", "看起来面相显出", "Du siehst heute wirklich blendend und erholt aus!", "你今天看起来气色简直太棒了，显得格外容光焕发！"),
            ("die Figur", "die", "n.", "-en", "身材骨架，体态", "Durch regelmäßiges Schwimmen hält er seine athletische Figur.", "依靠长年持之以恒的游泳锻炼他保持了矫健匀称的好身材。"),
            ("schlank", "", "adj.", "schlanker, am schlanksten", "苗条纤瘦挺拔的", "Sie ist groß gewachsen und hat eine schlanke Silhouette.", "她个头生得十分高挑，拥有轻盈苗条的优美身体轮廓线条。"),
            ("dünn", "", "adj.", "dünner, am dünnsten", "干瘪薄弱削瘦的", "Nach der langen Krankheit sah er besorgniserregend dünn aus.", "在大病初愈后他整个人看起来削瘦得令人感到揪心担忧。"),
            ("dick", "", "adj.", "dicker, am dicksten", "粗大厚实肥硕的", "Im Winter zieht man dicke Wollpullover und feste Stiefel an.", "在数九严寒的冬日里人们套上厚厚的羊毛大套头衫与厚底靴。"),
            ("hübsch", "", "adj.", "hübscher, am hübschesten", "清秀俏丽漂亮的", "Ein hübsches Gesicht mit zwei fröhlichen Grübchen in den Wangen.", "一张清秀标致的面孔，笑起来两颊泛着一对可爱的酒窝。"),
            ("schön", "", "adj.", "schöner, am schönsten", "美丽的，俊美的", "Wahre innere Schönheit strahlt von innen nach außen.", "真正深邃的内在精神美会自然而然由内向外散发出耀眼光芒。"),
            ("attraktiv", "", "adj.", "attraktiver, am attraktivsten", "富有性魅力吸引力的", "Er wirkt auf seine Mitmenschen ungemein attraktiv und charmant.", "他在周围人群眼中展现出了无与伦比的超凡魅力与人格吸引力。"),
            ("hässlich", "", "adj.", "hässlicher, am hässlichsten", "丑陋不堪丑相的", "Wahres Glück hängt nicht von oberflächlichen Äußerlichkeiten ab.", "真正的幸福从来都不取决于皮相层面肤浅的长相美丑。"),
            ("das Gesicht", "das", "n.", "-er", "脸庞面庞，面容", "Ein markantes Gesicht mit ausdrucksstarken, tiefen Augen.", "一张棱角分明、生有一双深邃极富表现力大眼的硬朗面庞。"),
            ("die Haut", "die", "n.", "Häute", "皮肤肌肤，表皮", "Schützen Sie Ihre empfindliche Haut vor intensiver Sonnenstrahlung!", "在强紫外线暴晒下请务必保护好娇嫩敏感的面部肌肤！"),
            ("die Haare", "die", "n.pl.", "-", "秀发，头发（复数）", "Sie trägt ihre langen braunen Haare gerne offen über den Schultern.", "她喜欢将自己那一头飘逸的棕色大长发随性披散在肩头。"),
            ("blond", "", "adj.", "blonder, am blondesten", "金黄色发色的", "In den nordischen Ländern sind sehr viele Menschen von Natur aus blond.", "在北欧沿海诸国天然拥有金黄色头发的人口比例极高。"),
            ("braun", "", "adj.", "brauner, am braunsten", "棕褐色头发肌肤的", "Dunkelbraune Augen und glänzendes, welliges Haar.", "一双深邃乌黑的棕褐色眼眸配上一头充满光泽感的波浪卷发。"),
            ("schwarz", "", "adj.", "schwärzer, am schwärzesten", "乌黑发亮的", "Pechschwarzes Haar bildet einen reizvollen Kontrast zu heller Haut.", "乌黑如漆的长发与白皙胜雪的肌肤形成了鲜明悦目的视觉反差。"),
            ("grau", "", "adj.", "grauer, am grausten", "花白银灰头发的", "Im Alter werden die Haare an den Schläfen langsam silbergrau.", "步入老年之后两鬓处的发丝渐渐染上了岁月的点点银白。"),
            ("die Glatze", "die", "n.", "-n", "光头头皮，脱发秃顶", "Er rasiert sich aus modischen Gründen eine glatte Glatze.", "出于追逐潮流个性考量，他索性把自己剃成了一个干净的大光头。"),
            ("der Bart", "der", "n.", "Bärte", "胡须面部胡子", "Ein gepflegter Vollbart liegt bei jungen Männern voll im Trend.", "蓄上一把精心打理修剪齐整的络腮胡在年轻男性中蔚然成风。"),
            ("rasieren", "", "v.", "rasiert, rasierte, rasiert", "剃刮面部胡须", "Morgens rasiert er sich gründlich mit einem scharfen Nassrasierer.", "清晨他习惯用一把锋利的湿剃剃须刀将下巴胡茬刮得干干净净。"),
            ("die Brille", "die", "n.", "-n", "近视远视框架眼镜", "Die modische Hornbrille verleiht ihr ein intellektuelles Aussehen.", "一副时髦复古的玳瑁框近视眼镜赋予了她知性儒雅的学者气质。"),
            ("die Kontaktlinsen", "die", "n.pl.", "-", "隐形眼镜角膜镜片", "Beim intensiven Sport trägt er viel lieber weiche Kontaktlinsen.", "在参与对抗激烈的剧烈体育运动时他更偏好佩戴隐形眼镜。"),
            ("der Charakter", "der", "n.", "Charaktere", "品格品性，性格特征", "Man erkennt den wahren Charakter eines Menschen in der Not.", "唯有在患难困顿之际方能真正识破一个人骨子里的真实品性。"),
            ("die Persönlichkeit", "die", "n.", "-en", "健全人格，个性面貌", "Sie besitzt eine starke, unabhängige und souveräne Persönlichkeit.", "她拥有独立自信、气场强大且沉稳从容的卓越健全人格。"),
            ("sympathisch", "", "adj.", "sympathischer, am sympathischsten", "讨人喜欢极具亲和力的", "Der neue Kollege im Büro machte sofort einen überaus sympathischen Eindruck.", "办公室新入职的那位同事一打照面便给人留下了极富亲和力的好印象。"),
            ("unsympathisch", "", "adj.", "unsympathischer, am unsympathischsten", "冷若冰霜招人反感的", "Ein arrogantes Auftreten wirkt auf die meisten Mitmenschen unsympathisch.", "傲慢自大、目中无人的言谈举止在绝大多数人看来都极为惹人生厌。"),
            ("freundlich", "", "adj.", "freundlicher, am freundlichsten", "友善客气的", "Ein freundliches Lächeln erleichtert den Einstieg in jedes Gespräch.", "一抹真诚友善的微笑能在举手投足间化解陌生人初次交流的尴尬。"),
            ("höflich", "", "adj.", "höflicher, am höflichsten", "知书达礼彬彬有礼的", "Er bedankte sich mit einer ausgesprochen höflichen Verbeugung.", "他极有教养地微微欠身鞠躬，用极其得体客气的言辞表达了谢意。"),
            ("unhöflich", "", "adj.", "unhöflicher, am unhöflichsten", "粗野无礼不讲礼貌的", "Es ist unhöflich, anderen mitten im Satz ins Wort zu fallen.", "当别人话还没说完便贸然中途出声打断是极其不礼貌无教养的。"),
            ("hilfsbereit", "", "adj.", "hilfsbereiter, am hilfsbereitesten", "乐于助人乐善好施的", "Hilfsbereite Bürger unterstützten die Rettungskräfte tatkräftig vor Ort.", "热心肠乐于助人的市民群众在事发现场全力协助救援人员开展工作。"),
            ("zuverlässig", "", "adj.", "zuverlässiger, am zuverlässigsten", "一诺千金极其靠谱的", "Auf meinen zuverlässigen Freund kann ich mich zu jeder Sekunde verlassen.", "对于我那位相交多年的铁哥们我可以把后背托付给他，百分之百信赖。"),
            ("pünktlich", "", "adj.", "pünktlicher, am pünktlichsten", "恪守时刻守时严谨的", "In Deutschland wird Pünktlichkeit als Zeichen des Respekts gewertet.", "在德国社会文化中守时被普遍视作对他人时间最崇高的尊重体现。"),
            ("ehrlich", "", "adj.", "ehrlicher, am ehrlichsten", "襟怀坦白诚实守正的", "Ehrlichkeit ist die unumstößliche Basis für jede echte Freundschaft.", "坦诚真挚是一切长久坚固的真正友谊不可动摇的核心基石与底线。"),
            ("fleißig", "", "adj.", "fleißiger, am fleißigsten", "勤学笃行勤奋刻苦的", "Fleißige Studenten bereiten den Lernstoff akribisch vor und nach.", "勤奋好学的学子们总会雷打不动地提前细致预习并巩固课后知识。"),
            ("faul", "", "adj.", "fauler, am faulsten", "懒惰怠工好吃懒做的", "Sonntags darf man auch mal ganz faul auf dem Sofa faulenzen.", "在万事皆休的星期天大可以心安理得瘫在沙发上彻底懒散放松一天。"),
            ("klug", "", "adj.", "klüger, am klügsten", "机敏睿智聪颖过人的", "Sie traf in der kniffligen Situation eine überaus kluge Entscheidung.", "在这起万分棘手的复杂局面下她做出了一个极其睿智果决的决断。"),
            ("intelligent", "", "adj.", "intelligenter, am intelligentesten", "智商超群聪明绝顶的", "Ein intelligenter Schachzug brachte ihm die gewinnbringende Führung.", "一步构思极度精妙的聪明棋招瞬间帮助他在整盘对局中奠定胜势。"),
            ("dumm", "", "adj.", "dümmer, am dümmsten", "愚钝荒谬愚蠢无知的", "Aus dummen Leichtsinnsfehlern sollte man zügig die richtigen Lehren ziehen.", "人应当尽快从那些因愚蠢粗心导致的低级失误中痛定思痛吸取教训。"),
            ("geduldig", "", "adj.", "geduldiger, am geduldigsten", "极富耐性循循善诱的", "Die Lehrerin erklärte dem Kind die Rechenaufgabe mit unendlicher Geduld.", "女老师怀着极其博大的耐心一遍又一遍启发引导孩子解答算术题。"),
            ("ungeduldig", "", "adj.", "ungeduldiger, am ungeduldigsten", "急躁难耐按捺不住的", "Die ungeduldigen Fahrgäste blickten im Stau ständig auf die Uhr.", "困在拥堵长龙里的焦急乘客们开始按捺不住性子频频低头看表看点。"),
            ("ruhig", "", "adj.", "ruhiger, am ruhigsten", "沉着镇静泰然处之的", "Bleiben Sie bei einem Erdbeben ruhig und verlassen Sie das Gebäude!", "遭遇突发地震险情时务必保持沉着镇静，有条不紊疏散撤离建筑！"),
            ("nervös", "", "adj.", "nervöser, am nervösesten", "手足无措局促紧张的", "Vor dem Vorstellungsgespräch war sie begreiflicherweise etwas nervös.", "在面临关乎职业前途的重大面试前夕，她难免略感到有些手心冒汗。"),
            ("mutig", "", "adj.", "mutiger, am mutigsten", "见义勇为勇敢无畏的", "Ein mutiger Zeuge griff sofort ein und überwältigte den Dieb.", "一位英勇无畏的热心目击者当机立断挺身而出合力制服了行窃小偷。"),
            ("feige", "", "adj.", "feiger, am feigsten", "懦弱怯懦胆小怕事的", "Es ist feige, wegzuschauen, wenn jemand unverschuldet in Not gerät.", "当无辜之人陷入水深火热困境时装聋作哑掉头离开是怯懦可耻的。"),
            ("lustig", "", "adj.", "lustiger, am lustigsten", "风趣幽默滑稽好笑的", "Er erzählte eine unglaublich lustige Anekdote, über die alle lachten.", "他生动讲述了一则令人捧腹大笑的幽默轶事，逗得满堂宾客大笑。"),
            ("humorvoll", "", "adj.", "humorvoller, am humorvollsten", "深具幽默豁达感悟的", "Ein humorvoller Mensch meistert schwierige Lebensphasen leichter.", "一个深具幽默风趣感的人能以更为旷达的心境跨越生命中的险滩。"),
            ("ernst", "", "adj.", "ernster, am ernstesten", "庄重严肃不苟言笑的", "Die wirtschaftliche Lage erfordert ernste und durchdachte Maßnahmen.", "严峻复杂的宏观经济现实态势倒逼各方必须出台严肃周密的举措。"),
            ("traurig", "", "adj.", "trauriger, am traurigsten", "黯然神伤悲伤痛惜的", "Die traurige Nachricht vom Tode des Künstlers löste Betroffenheit aus.", "那位伟大艺术家溘然长逝的悲痛噩耗在全社会引发了广泛的哀思。"),
            ("fröhlich", "", "adj.", "fröhlicher, am fröhlichsten", "欢呼雀跃兴高采烈的", "Kinder singen und spielen fröhlich im sonnendurchfluteten Hof.", "孩童们在洒满煦暖阳光的绿草如茵庭院里欢呼雀跃地蹦跳唱歌。"),
            ("glücklich", "", "adj.", "glücklicher, am glücklichsten", "幸福美满万事遂心的", "Sie blickt glücklich auf dreißig gemeinsame Ehejahre zurück.", "她满怀幸福深情地回首夫妻二人同甘共苦携手走过的三十载光阴。"),
            ("wütend", "", "adj.", "wütender, am wütendsten", "怒发冲冠勃然大怒的", "Der wütende Kunde verlangte lautstark die Geschäftsführung zu sprechen.", "怒气冲冲的消费者当场拍桌子疾言厉色要求直接找总店总经理对话。"),
            ("ärgerlich", "", "adj.", "ärgerlicher, am ärgerlichsten", "懊恼恼火令人扫兴的", "Es ist extrem ärgerlich, wenn der gebuchte Zug kurzfristig ausfällt.", "眼看提前订好座的列车临发车前突遭取消，搁谁身上都倍感恼火。"),
            ("stolz", "", "adj.", "stolzer, am stolzesten", "由衷自豪感到骄傲的", "Die Eltern sind unendlich stolz auf die akademischen Erfolge der Tochter.", "看到女儿在学术领域取得的斐然建树，父母心中涌起由衷的骄傲。"),
            ("bescheiden", "", "adj.", "bescheidener, am bescheidensten", "谦逊低调不事张扬的", "Trotz seines immensen Reichtums lebt er bemerkenswert bescheiden.", "尽管坐拥亿万家财，他在日常起居餐饮上却过得异乎寻常的简朴。"),
            ("arrogant", "", "adj.", "arroganter, am arrogantesten", "不可一世狂妄自大的", "Ein arrogantes Auftreten schadet dem eigenen Ansehen nachhaltig.", "平日里不可一世颐指气使的傲慢姿态势必长期损害自身社会风评。"),
            ("die Mode", "die", "n.", "-n", "服装时尚流行浪潮", "Mode ist vergänglich, wahrer Stil hingegen bleibt ewig bestehen.", "时尚潮流瞬息万变各领风骚，然而骨子里散发出的风格却能恒久。"),
            ("modisch", "", "adj.", "modischer, am modischsten", "入时前卫赶潮流的", "Sie kleidet sich stets modisch, ohne jeden flüchtigen Trend mitzumachen.", "她平素穿着打扮极为入时摩登，却从不盲目跟从每一波浮躁风潮。"),
            ("der Stil", "der", "n.", "-e", "品位风格，格调剪裁", "Ein schlichter, klassischer Stil kommt niemals aus der Mode.", "那种删繁就简的大气极简经典风尚，在任何时代都不会退出潮流。"),
            ("das Outfit", "das", "n.", "-s", "整套出行穿搭着装", "Ihr elegantes Outfit zog am Festabend alle bewundernden Blicke an.", "她那一身裁剪妥帖的高级晚宴行头在宴会当晚引得全场目光聚焦。"),
            ("kombinieren", "", "v.", "kombiniert, kombinierte, kombiniert", "色彩搭配，巧妙穿搭", "Sie kombiniert die blaue Seidenbluse geschickt mit einer weißen Hose.", "她极其高明地将深蓝真丝衬衫与利落合身的白色阔腿长裤做搭配。"),
            ("passen", "", "v.", "passt, passte, gepasst", "款式协调；合身 (zu + Dat)", "Dieser sportliche Sneaker passt hervorragend zu lockeren Jeans.", "这双线条流畅的休闲老爹鞋与宽松款牛仔阔腿裤搭起来相得益彰。"),
            ("stehen", "", "v.", "steht, stand, gestanden", "极其衬托气色 (接 Dativ)", "Dieser edle marineblaue Farbton steht Ihnen ganz ausgezeichnet!", "这种自带高级感的贵族海军蓝纯色调真的极其衬托您白皙的气色！"),
            ("gefallen", "", "v.", "gefällt, gefiel, gefallen", "深合心意 (接 Dativ)", "Wie gefällt dir der neu geschnittene Mantel im Schaufenster dort?", "橱窗里模特身上那件最新立体剪裁的风衣大衣你看合不合你心意？"),
            ("anprobieren", "", "v.", "probiert an, probierte an, anprobiert", "在试衣间试穿样衣", "Ich möchte dieses Kleid vor dem Kauf unbedingt noch anprobieren.", "在掏钱刷卡买单之前我务必先进试衣间亲自将这条裙子试穿一下。"),
            ("tragen", "", "v.", "trägt, trug, getragen", "穿戴在身上，佩戴", "Er trägt im harten Arbeitsalltag stets bequeme und robuste Kleidung.", "在繁重的工作日程中他始终恪守穿着亲肤舒适且经磨耐造的服饰。"),
            ("anziehen", "", "v.", "zieht an, zog an, angezogen", "穿好衣物，梳妆打扮", "Zieh dich schnell an, wir müssen in zehn Minuten pünktlich los!", "动作快点把外套衣服穿好，我们还有十分钟必须准时下楼出门！"),
            ("ausziehen", "", "v.", "zieht aus, zog aus, ausgezogen", "脱掉外衣脱鞋", "Zieh bitte die nassen Schuhe im beheizten Vorraum aus!", "进门后请先在温暖玄关处把被雨水浸湿的外层鞋子彻底换脱下来！"),
            ("umziehen", "", "v.", "zieht um, zog um, umgezogen", "更换衣服换装", "Nach der Arbeit zieht er sich sofort in bequeme Freizeitkleidung um.", "下班一回到家他便立刻换上一套宽松轻便的居家休闲起居服。"),
            ("der Schmuck", "der", "n.", "-", "金银珠宝，首饰挂件", "Dezenter Schmuck aus mattem Gold unterstreicht die Eleganz.", "佩戴在腕间的哑光磨砂纯金极简首饰将低调奢华的雅致体现无遗。"),
            ("das Parfüm", "das", "n.", "-s", "香水精油，名贵芳香", "Ein Hauch von edlem Parfüm verströmt eine unaufdringliche Note.", "喷洒在锁骨与耳后的一抹淡雅高级小众香水散发着若隐若现的芬芳。")
        ]
    }
]
