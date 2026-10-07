#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B1 Part 2: Lessons 6 to 10 (350 words)
L06: 现代健康管理、预防医学与营养学 (Gesundheit, Prävention & Ernährung) - 70 words
L07: 数字时代、信息安全与数据隐私规范 (Digitalisierung, Medien & Datenschutz) - 70 words
L08: 气候保护、生态文明与新能源革命 (Klimaschutz, Energiewende & Ökologie) - 70 words
L09: 公民社会、志愿服务与社会参与 (Zivilgesellschaft, Ehrenamt & Engagement) - 70 words
L10: 消费心理、个人财务理财与反思消费 (Konsumverhalten, Finanzen & Schulden) - 70 words
"""

LESSONS_B1_PART2 = [
    # LESSON 6
    {
        "id": "B1_L06",
        "title": "第6课：现代健康管理、预防医学与营养学 (Gesundheit & Ernährung)",
        "summary": "掌握带 um... zu / damit 目的从句结构、现代生活方式病防范与营养均衡科学",
        "grammar": {
            "title": "目的表达：um... zu (同主语) vs damit (不同主语)",
            "sections": [
                {
                    "heading": "1. um... zu + 不定式（主从句主语完全一致时，省略从句主语）：",
                    "content": "• Er ernährt sich gesund, um fit zu bleiben. (主语同为 er)\n• Wir treiben Sport, um Stress abzubauen."
                },
                {
                    "heading": "2. damit 引导目的从句（主语不同，或强调目的从句）：",
                    "content": "• Die Ärztin erklärt die Therapie, damit der Patient keine Angst hat.\n• Ich koche gesund, damit meine Kinder viele Vitamine bekommen."
                }
            ]
        },
        "quiz": [
            {
                "id": "B1_L06_Q1",
                "type": "GRAMMAR_FILL",
                "question": "Er geht jeden Tag joggen, ______ (um...zu / damit) sein Herz zu stärken.",
                "options": ["um", "damit", "weil", "sodass"],
                "correctIndex": 0,
                "explanation": "主句与不定式结构主语一致且后接带 zu 不定式，使用 um ... zu。"
            },
            {
                "id": "B1_L06_Q2",
                "type": "VOCAB_MEANING",
                "question": "德国健康医学中极推崇的 'die Vorsorgeuntersuchung' 意思是：",
                "options": ["疾病早期预防性体检筛查", "急诊大抢救手术", "购买住院高档轮椅", "申请残疾人抚恤金"],
                "correctIndex": 0,
                "explanation": "die Vorsorgeuntersuchung 是德国公立医保免费覆盖的“疾病预防筛查、早癌筛查健康体检”。"
            }
        ],
        "words": [
            ("die Gesundheit", "die", "n.", "-", "身心全生命周期健康", "Gesundheit ist ein Zustand vollkommenen körperlichen und geistigen Wohlbefindens.", "真正的健康是肉身健全与精神充盈高度统一的至善生命状态。"),
            ("das Wohlbefinden", "das", "n.", "-", "愉悦充盈舒适度", "Ausreichender Schlaf und gesunde Ernährung fördern das tägliche Wohlbefinden.", "每晚保证充沛深沉的高质量睡眠是维系机体充盈活力的不二法门。"),
            ("die Lebensqualität", "die", "n.", "-", "人居综合生命生活质量", "Chronische Schmerzen beeinträchtigen die individuelle Lebensqualität massiv.", "日复一日挥之不去的顽固性神经性病痛会极大蚕食摧毁人的生活质量。"),
            ("die Prävention", "die", "n.", "-", "未病先防治未病预防医学", "Prävention ist stets wirksamer und kostengünstiger als eine späte Therapie.", "在现代临床医学共识中，未病先防的预防医学永远胜过病入膏肓后的重度救治。"),
            ("die Vorbeugung", "die", "n.", "-en", "未雨绸缪防范化解", "Tägliche Bewegung an der frischen Luft dient der wirksamen Vorbeugung von Herzleiden.", "每日雷打不动去户外天然大氧吧快走半小时是对抗心脑血管隐患的最佳防范。"),
            ("vorbeugen", "", "v.", "beugt vor, beugte vor, vorgebeugt", "防患于未然，预防 (接 Dativ)", "Mit einer ausgewogenen Ernährung beugt man Zivilisationskrankheiten gezielt vor.", "践行低油低糖的科学均衡膳食能够靶向预防困扰现代人的诸多富贵生活方式病。"),
            ("die Vorsorgeuntersuchung", "die", "n.", "-en", "公费早期健康预防筛查体检", "Regelmäßige Vorsorgeuntersuchungen ermöglichen die Früherkennung von Tumoren.", "坚持每年如期参加公立医保筛查体检能够在萌芽状态下精准揪出早期微小肿瘤。"),
            ("die Früherkennung", "die", "n.", "-", "肿瘤早诊早筛早治机制", "Die Früherkennung von Darmkrebs rettet nachweislich tausende Menschenleben jährlich.", "结直肠癌早筛早诊技术的全社会大面积普及每年挽救了成千上万条鲜活生命。"),
            ("das Screening", "das", "n.", "-s", "大规模群体医学仪器筛查", "Das Mammografie-Screening richtet sich an Frauen ab dem fünfzigsten Lebensjahr.", "针对年满五十周岁适龄女性群体的乳腺专项X光筛查由国家统筹定期免费开出。"),
            ("der Check-up", "der", "n.", "-s", "周期性全身体格大检阅体检", "Ab 35 Jahren bezahlt die gesetzliche Krankenkasse alle drei Jahre einen Check-up.", "年满三十五周岁的参保职工依法每隔三年即可无偿享有一次全面的深度全身体检。"),
            ("das Labor", "das", "n.", "-e", "高精尖现代医学检验实验室", "Das klinische Labor analysiert die Blutwerte auf Entzündungsmarker und Cholesterin.", "中心检验科在无菌环境下对采集送检的静脉全血标本做炎性因子与血脂精密分析。"),
            ("das Blutbild", "das", "n.", "-er", "生化常规全套血象检验单", "Ein großes Blutbild gibt präzise Auskunft über Nieren, Leber und Schilddrüse.", "一份详实严密的生化大血象报告能够对肝胆胰肾与甲状腺脏器功能作出精准画像。"),
            ("der Cholesterinspiegel", "der", "n.", "-", "血液中低密度胆固醇浓度指标", "Ein dauerhaft überhöhter Cholesterinspiegel verkalkt die Herzkranzgefäße.", "血液中低密度脂蛋白坏胆固醇水平长期超标蓄积会导致冠状动脉硬化斑块丛生。"),
            ("der Blutzucker", "der", "n.", "-", "血液空腹葡萄糖浓度血糖", "Der Nüchtern-Blutzucker sollte im Normalbereich unter hundert Milligramm liegen.", "晨起空腹状态下静脉血糖正常生理波动阈值应当严格控制在一百毫克安全线以下。"),
            ("der Diabetes", "der", "n.", "-", "胰岛素抵抗内分泌糖尿病", "Typ-2-Diabetes lässt sich im Frühstadium oft durch Gewichtsabnahme umkehren.", "二型早期糖尿病通过科学严格的生活方式干预与减重甚至能够实现临床临床逆转。"),
            ("die Zuckerkrankheit", "die", "n.", "-", "糖尿病（德语本土通俗俗名）", "Die Zuckerkrankheit erfordert disziplinierte Ernährung und Blutzuckermessung.", "饱受糖尿病困扰的糖友必须终身恪守极其自律的低升糖饮食并定时扎针测糖。"),
            ("der Bluthochdruck", "der", "n.", "-", "动脉血管阻力升高高血压症", "Bluthochdruck gilt als der gefährlichste lautlose Killer für das Gefäßsystem.", "原发性高血压因其发病隐匿常年不痛不痒而被医学界公认为血管最阴险的隐形杀手。"),
            ("die Hypertonie", "die", "n.", "-", "高血压病（严谨医学学名）", "Unbehandelte arterielle Hypertonie vervielfacht das Schlaganfall-Risiko.", "放任失控的原发性动脉高血压不予干预会将突发致残脑卒中的概率翻倍推高。"),
            ("der Herzinfarkt", "der", "n.", "-e", "冠状动脉闭塞心肌大梗死", "Bei akutem Brustschmerz mit Ausstrahlung in den linken Arm sofort 112 anrufen!", "一旦突发伴随左臂后背放射性绞痛的压榨性胸骨后剧痛，必须当机立断拨打112！"),
            ("der Schlaganfall", "der", "n.", "Schlaganfälle", "脑血管栓塞破裂脑卒中中风", "Schnelles Handeln nach dem FAST-Schema rettet Gehirnzellen beim Schlaganfall.", "在疑似中风突发黄金时间窗内依FAST脑卒中口诀争分夺秒抢救能保护脑神经元。"),
            ("das Übergewicht", "das", "n.", "-", "脂肪过量超重体态超标", "Starkes Übergewicht belastet Wirbelsäule, Hüftgelenke und Herz-Kreislauf-System.", "长期严重的重度肥胖会给机体颈腰椎骨关节韧带以及心血管泵血造成沉重负荷。"),
            ("die Fettleibigkeit", "die", "n.", "-", "病理临床重度肥胖症", "Fettleibigkeit ist eine chronische Stoffwechselerkrankung, keine bloße Willensschwäche.", "临床重度肥胖症是一种错综复杂的慢性代谢内分泌紊乱，绝非单纯轻飘飘意志力薄弱。"),
            ("der Body-Mass-Index", "der", "n.", "-", "身体质量指数BMI指标", "Ein Body-Mass-Index zwischen 18,5 und 24,9 gilt als optimales Normalgewicht.", "身体质量指数介于十八点五至二十四点九之间被公认为最健康的成年人标准体态。"),
            ("der BMI", "der", "n.", "-s", "BMI指数（缩略英德简称）", "Der Rechner ermittelt aus Körpergröße und Gewicht den persönlichen BMI.", "只需输入实测净身高与净体重，便能自动换算出受试者精准的BMI健康体态数值。"),
            ("die Ernährung", "die", "n.", "-", "营养摄入，日常饮食结构", "Eine pflanzenbasierte Ernährung schützt das Herz und die planetaren Grenzen.", "以全谷物与新鲜果蔬为核心的植物基膳食结构既呵护心脏又善待地球生态承载力。"),
            ("die Ernährungsweise", "die", "n.", "-n", "饮食作风与进食生活模式", "Die traditionelle mediterrane Ernährungsweise senkt die Gesamtsterblichkeit.", "以海鱼、坚果、优质初榨橄榄油为特色的传统地中海膳食范式能显著降低全因死亡率。"),
            ("die Diät", "die", "n.", "-en", "控制卡路里特定调养节食", "Einseitige Crash-Diäten führen unweigerlich zum gefürchteten Jo-Jo-Effekt.", "盲目跟风、戒断某类营养素的极端口碑节食断食法，无一例外都会触发反弹噩梦。"),
            ("die Kalorie", "die", "n.", "-n", "能量热量度量单位卡路里", "Um gesund abzunehmen, genügt ein moderates tägliches Kaloriendefizit von 300 kcal.", "若想达成科学持久的温和瘦身，每日维持三百千卡左右的温和能量缺口足矣。"),
            ("der Kalorienbedarf", "der", "n.", "-", "人体维持全天代谢所需热量", "Der individuelle Kalorienbedarf hängt von Muskelmasse und körperlicher Aktivität ab.", "每个人全天实际所需的热量摄入总盘子取决于自身瘦肌肉含量与全天实际运动量。"),
            ("der Nährstoff", "der", "n.", "-e", "人体必需各类生命营养素", "Vollkorngetreide liefert komplexe Kohlenhydrate, Mineralien und essenzielle Nährstoffe.", "全麦谷物不仅饱腹感持久，更能源源不断输出慢碳水化合物与不可或缺的微量元素。"),
            ("das Kohlenhydrat", "das", "n.", "-e", "能量来源主要大类碳水化合物", "Vermeiden Sie einfache Kohlenhydrate aus Weißmehl und industriellem Zucker!", "在日常采购进食中尽量远离由精制白面粉与深加工游离添加糖构成的劣质快碳！"),
            ("das Eiweiß", "das", "n.", "-e", "肌肉脏器构筑基石蛋白质", "Sportler benötigen hochwertiges Eiweiß zur Regeneration und für den Muskelaufbau.", "经常进行抗阻力量训练的健身人士必须补充足额高生物价优质蛋白质以修复肌纤维。"),
            ("das Protein", "das", "n.", "-e", "蛋白质（现代国际通用名）", "Hülsenfrüchte wie Linsen, Kichererbsen und Bohnen sind hervorragende pflanzliche Proteine.", "扁豆、鹰嘴豆与各类杂豆是素食主义者日常食谱中不可多得的优质植物蛋白宝库。"),
            ("das Fett", "das", "n.", "-e", "人体三大产能供能营养素脂肪", "Ungesättigte Fettsäuren aus Avocados und Nüssen wirken entzündungshemmend im Körper.", "富集在牛油果与深海鱼油当中的不饱和脂肪酸在人体微循环体系中发挥着抗炎作用。"),
            ("die Fettsäure", "die", "n.", "-n", "构成脂肪的分子单元脂肪酸", "Omega-3-Fettsäuren aus fettem Seefisch stärken die kognitive Gehirnleistung.", "从深海野生三文鱼油脂中萃取的欧米伽三脂肪酸对延缓大脑认知退化大有裨益。"),
            ("das Vitamin", "das", "n.", "-e", "维持微量生理机能的维生素", "Vitamin D wird im Körper vor allem durch direkte Sonneneinstrahlung auf der Haut gebildet.", "被誉为阳光荷尔蒙的维生素D绝大部分依靠裸露皮肤沐浴在温暖阳光照射下自主合成。"),
            ("der Vitaminmangel", "der", "n.", "Vitaminmängel", "维生素摄入不足之缺乏症", "Im dunklen mitteleuropäischen Winter leiden viele Menschen an akutem Vitamin-D-Mangel.", "在中欧漫长阴冷的冬春时节，相当比例的人口普遍罹患着隐匿的重度维生素D缺乏。"),
            ("das Mineral", "das", "n.", "-ien", "机体不可或缺的无机矿物质", "Mineralien wie Magnesium und Calcium sind unentbehrlich für Knochen und Muskeln.", "镁、钙与钾等无机矿物质微量元素是构筑强健骨骼与维持心肌规律搏动的基石。"),
            ("das Spurenelement", "das", "n.", "-e", "微量发挥巨大功效之微量元素", "Eisen, Zink und Selen sind lebenswichtige Spurenelemente für ein schlagkräftiges Immunsystem.", "铁、锌与硒等微量元素是维持人体庞大免疫淋巴防御系统正常高效运转的底盘。"),
            ("der Ballaststoff", "der", "n.", "-e", "调节肠道菌群的膳食纤维", "Eine Ernährung reich an Ballaststoffen füttert das nützliche Mikrobiom im Darm.", "大量摄入富含非水溶性膳食纤维的绿叶蔬菜能够极大滋养肠道内壁的共生益生菌群。"),
            ("die Verdauung", "die", "n.", "-", "肠胃道消化与吸收代谢", "Gründliches Kauen im Mund entlastet die nachgelagerte Verdauung im Magen.", "在口腔中将每一口饭菜细嚼慢咽充分咀嚼能大幅卸下胃窦部消化研磨的沉重负荷。"),
            ("der Stoffwechsel", "der", "n.", "-", "生生不息之机体新陈代谢", "Regelmäßiges Krafttraining kurbelt den basalen Stoffwechsel nachhaltig an.", "长年坚持规范的大肌群抗阻力量训练能将人体的基础代谢率维持在旺盛高位水平。"),
            ("die Verbrennung", "die", "n.", "-", "机体脂肪热量氧化代谢燃烧", "Intervalltraining treibt die Fettverbrennung auch Stunden nach dem Sport in die Höhe.", "高强度间歇性冲刺训练能触发神奇的后燃效应，在运动结束后数小时持续燃脂。"),
            ("die Flüssigkeit", "die", "n.", "-en", "维持体液循环平衡之水分", "Trinken Sie über den Tag verteilt mindestens zwei Liter kalorienfreie Flüssigkeit!", "请在全天不同时段均匀小口缀饮足额两升以上的纯白开水或无糖清淡花草茶！"),
            ("die Dehydrierung", "die", "n.", "-", "体液失衡危及生命的脱水症", "Kopfschmerzen und Schwindel sind frühe Alarmsignale für eine beginnende Dehydrierung.", "午后突发的太阳穴胀痛与莫名眩晕感，往往是身体内部细胞开始缺水脱水的信号。"),
            ("die Bewegung", "die", "n.", "-", "强身健体有氧无氧体育运动", "Tägliche körperliche Bewegung ist das wirksamste und billigste Medikament der Welt.", "把每天半小时身体主动运动融入生命节拍，是这世界上疗效最神效且廉价的灵丹。"),
            ("der Bewegungsmangel", "der", "n.", "-", "久坐少动缺乏体育锻炼", "Chronischer Bewegungsmangel am Schreibtisch schwächt den gesamten Halteapparat.", "常年久坐电脑前不动弹的运动严重匮乏作风，会使得人体核心支撑肌肉群萎缩。"),
            ("das Ausdauertraining", "das", "n.", "-s", "增强心肺储备耐力性训练", "Regelmäßiges Ausdauertraining wie Joggen, Radfahren oder Schwimmen stärkt das Herz.", "慢跑、公路骑行或长距离自由泳等经典耐力训练能使人体心肌泵血功能成倍增强。"),
            ("das Krafttraining", "das", "n.", "-s", "增肌强体抗阻重力力量训练", "Krafttraining schützt ältere Menschen vor Muskelabbau und gefährlichen Stürzen.", "指导中老年群体科学开展力量训练能够极大延缓肌肉流失衰减并预防跌倒骨折。"),
            ("die Muskelmasse", "die", "n.", "-n", "全身骨骼肌净肌肉组织总重", "Ab dem 30. Lebensjahr verliert der inaktive Mensch pro Jahrzehnt wertvolle Muskelmasse.", "人在迈过三十周岁门槛后若不加主动抗阻干预，每十年肌肉质量都将不可避免缩水。"),
            ("die Fitness", "die", "n.", "-", "体适能指标与充沛体能水准", "Körperliche Fitness steigert die geistige Konzentrationsfähigkeit im Berufsalltag.", "保持良好的体能储备与体适能状态能反哺提升人在繁复职场事务中的专注力。"),
            ("das Wohlbefinden", "das", "n.", "-", "内心充实由衷散发的舒适安详", "Ein Spaziergang im Nadelwald schenkt tiefe innere Ruhe und ganzheitliches Wohlbefinden.", "在松涛阵阵的冷杉林间深呼吸漫步，能给人带来深度宁静与身心灵的全面滋养。"),
            ("die Regeneration", "die", "n.", "-", "机体组织修复期与超量恢复", "Nach einem harten Workout benötigt der erschöpfte Körper 48 Stunden zur Regeneration.", "在一场竭尽全力的暴汗大练后，疲惫的机体需要整整两天时间完成修复与超量恢复。"),
            ("der Schlaf", "der", "n.", "-", "深层无干扰黄金优质睡眠", "Tiefer, ununterbrochener Schlaf ist die wichtigste Phase für neuronale Reparaturprozesse.", "深层且不做恶梦的黄金整宿睡眠是中枢神经系统进行细胞级代谢修复的专属时间。"),
            ("die Schlaflosigkeit", "die", "n.", "-", "辗转反侧难以成眠之失眠症", "Chronische Schlaflosigkeit sollte ärztlich abgeklärt und nicht ignoriert werden.", "长期辗转反侧难以入睡的慢性顽固性失眠应当及时就医排查，切不可视作儿戏硬扛。"),
            ("die Schlafstörung", "die", "n.", "-en", "入睡困难早醒之睡眠障碍", "Bildschirmlicht vor dem Zubettgehen ist eine häufige Ursache für nächtliche Schlafstörungen.", "睡前半小时依然抱着手机平板猛刷屏幕是诱发夜间频繁惊醒与睡眠障碍的罪魁祸首。"),
            ("die Melatonin", "das", "n.", "-", "调节昼夜生物节律褪黑素", "Das Hormon Melatonin signalisiert dem Körper das Eintreten der biologischen Nacht.", "在脑下垂体分泌的褪黑素浓度激增时，向全身细胞敲响了夜幕降临应当歇息的钟声。"),
            ("der Stress", "der", "n.", "-", "神经紧绷持续承压之心理压力", "Chronischer unbewältigter Stress schüttet permanent toxische Mengen Cortisol aus.", "长期处于失控状态下的慢性重度精神压力会导致体内皮质醇激素水平居高不下。"),
            ("das Cortisol", "das", "n.", "-", "肾上腺皮质应激分泌皮质醇", "Ein dauerhaft erhöhter Cortisolspiegel schwächt die Immunabwehr gegen Viren.", "长期高浓度的应激压力激素皮质醇会严重压制人体免疫细胞对抗外来病毒的战力。"),
            ("der Stressabbau", "der", "n.", "-", "排解郁结压力舒缓神经负荷", "Meditation, Yoga und autogenes Training sind bewährte Methoden zum gezielten Stressabbau.", "正念冥想、瑜伽拉伸与自主神经调控训练已被实证为排遣身心压力的成熟有效途径。"),
            ("die Entspannung", "die", "n.", "-en", "放下戒备完全松弛身心放松", "Gönnen Sie sich im hektischen Berufsalltag bewusst kleine Inseln der Entspannung!", "在节奏快得令人窒息的职场打拼中，学会忙里偷闲给自己开辟出一座座放松小孤岛！"),
            ("die Meditation", "die", "n.", "-en", "闭目敛神内观正念打坐冥想", "Tägliche zehnminütige Meditation beruhigt die Aktivität des überreizten Mandelkerns.", "每天坚持十分钟的静心正念冥想能够有效抚平大脑中杏仁核区域的过度惊恐应激。"),
            ("das Yoga", "das", "n.", "-", "身心合一体式呼吸引导瑜伽", "Yoga verbindet achtsame Atemübungen mit kraftvollen statischen Dehnpositionen.", "瑜伽体式训练将绵柔细长的呼吸调息法与充满力量感与平衡感的人体拉伸完美融汇。"),
            ("die Achtsamkeit", "die", "n.", "-", "专注当下不作评判的正念觉察", "Achtsamkeit lehrt uns, den gegenwärtigen Moment ohne Vorverurteilung wahrzunehmen.", "正念之道的精义在于教导我们全神贯注临在于当下时空，对万事万物不起分别批判。"),
            ("das Immunsystem", "das", "n.", "-e", "人体天然免疫卫士防御系统", "Ausreichend Schlaf, Bewegung und Vitalstoffe halten das Immunsystem schlagkräftig.", "充足安稳的深度睡眠、有规律的运动与全面均衡的营养是守卫免疫长城的底牌。"),
            ("die Abwehrkräfte", "die", "n.pl.", "-", "抵御外邪入侵之自身抵抗力", "Kneipp-Güsse und Saunagänge trainieren die körpereigenen Abwehrkräfte wirksam.", "克奈普水疗冷水淋浴与北欧桑拿冷热交替能够极好地锤炼锻炼人体的自身免疫抵抗力。"),
            ("die Sucht", "die", "n.", "Süchte", "沉湎不可自拔之病态瘾癖依赖", "Die schleichende Sucht nach Nikotin, Alkohol oder Zucker beginnt oft unbemerkt.", "对尼古丁、酒精或精制糖分产生的心理与生理病态成瘾依赖往往在不知不觉间深种。"),
            ("die Abhängigkeit", "die", "n.", "-en", "躯体与精神性药物药物依赖", "Aus einem gelegentlichen Konsum zur Beruhigung entwickelte sich eine schwere Abhängigkeit.", "起初原本只是为了缓解焦虑而偶尔服药，久而久之却演变出难以自拔的重度依赖。"),
            ("der Verzicht", "der", "n.", "-", "戒绝坏习惯主动克制放弃", "Der freiwillige Verzicht auf Alkohol im sogenannten 'Dry January' entlastet die Leber.", "在所谓无酒一月中主动选择滴酒不沾，能给日夜劳作解毒的肝脏提供宝贵喘息生机。"),
            ("die Vitalität", "die", "n.", "-", "元气淋漓充沛昂扬的生命活力", "Ein gesunder Lebensstil belohnt den Menschen mit Vitalität bis ins hohe Greisenalter.", "恪守科学理性的健康生活方式，回馈给人类的将是直至耄耋之年依旧昂扬的元气活力。")
        ]
    },

    # LESSON 7
    {
        "id": "B1_L07",
        "title": "第7课：数字时代、信息安全与数据隐私规范 (Digitalisierung & Medien)",
        "summary": "掌握情态动词客观表达与代词性副词 (worüber, darüber)、网络安全攻防与人工智能浪潮",
        "grammar": {
            "title": "代词性副词 (Pronominaladverbien: wo(r)- / da(r)-) 结构",
            "sections": [
                {
                    "heading": "1. 疑问代词性副词 wo(r) + 介词（问物！针对事物问句）：",
                    "content": "• Worüber sprecht ihr? (你们在谈论什么？指事物)\n• 比较针对人：Über wen sprecht ihr? (你们在谈论谁？指人)\n• 介词以元音开头插入 r：wo + r + über = worüber / wo + r + an = woran"
                },
                {
                    "heading": "2. 指示代词性副词 da(r) + 介词（回指上文事物）：",
                    "content": "• Wir sprechen über Datenschutz. -> Wir sprechen darüber.\n• Ich habe nicht daran gedacht."
                }
            ]
        },
        "quiz": [
            {
                "id": "B1_L07_Q1",
                "type": "GRAMMAR_FILL",
                "question": "______ (woran / an wen) denkst du gerade? - An meine neue Software-Entwicklung.",
                "options": ["Woran", "An wen", "Worüber", "Wofür"],
                "correctIndex": 0,
                "explanation": "答句是事物 (Software-Entwicklung)，动词搭配 denken an，问事物使用代词性副词 Woran。"
            },
            {
                "id": "B1_L07_Q2",
                "type": "VOCAB_MEANING",
                "question": "计算机科技界大热的核心概念 'die Künstliche Intelligenz' 意思是：",
                "options": ["人工智能 (AI)", "虚拟内存条", "量子加密狗", "太空卫星天线"],
                "correctIndex": 0,
                "explanation": "die Künstliche Intelligenz (KI) 是德语中“人工智能 (Artificial Intelligence)”的规范标准用词。"
            }
        ],
        "words": [
            ("die Digitalisierung", "die", "n.", "-", "全社会全要素全面数字化转型", "Die fortschreitende Digitalisierung verändert Arbeitswelt und Alltag von Grund auf.", "日新月异、纵深推进的全社会数字化转型正在从底层根本上颠覆整个职场与生活。"),
            ("die Technologie", "die", "n.", "-n", "高精尖现代尖端技术", "Zukunftsweisende Technologien bieten innovative Lösungen für die Energiekrise.", "前沿先导性现代尖端科技为破解全人类共同面临的能源危机提供了破局新范式。"),
            ("der Fortschritt", "der", "n.", "-e", "日新月异的历史科技进步", "Technologischer Fortschritt muss immer ethischen Leitplanken unterworfen sein.", "任何领域的科技狂飙突进在任何时代都必须置于伦理道德刚性红线的约束之下。"),
            ("fortschrittlich", "", "adj.", "fortschrittlicher, am fortschrittlichsten", "锐意革新先进前沿的", "Eine fortschrittliche Gesellschaft investiert massiv in Bildung, Forschung und Glasfaser.", "一个勇于立在潮头的开明先进社会，总会毫不吝啬砸重金投资基础教育与光纤网络。"),
            ("die Künstliche Intelligenz", "die", "n.", "-", "计算机人工智能学派(KI)", "Künstliche Intelligenz kann komplexe Muster in gigantischen Datenmengen aufspüren.", "先进的人工智能算法模型能够从浩瀚如烟海的大数据池中精准揪出深层规律特征。"),
            ("die KI", "die", "n.", "-", "人工智能（权威官方德语缩写）", "Die Integration von KI in die Medizintechnik revolutioniert die Krebserkennung.", "将AI大模型前沿成果融入现代医学影像诊疗，使得早期病灶识别发生了革命性飞跃。"),
            ("der Algorithmus", "der", "n.", "Algorithmen", "精密计算执行步骤算法", "Intelligente Algorithmen steuern den Newsfeed und filtern unerwünschten Spam heraus.", "高精度智能推荐算法实时分发精准定制的资讯流，并在后台将垃圾广告清洗过滤。"),
            ("die Automatisierung", "die", "n.", "-", "机械智能高度自动化流程", "Die Automatisierung monotoner Routineprozesse entlastet hoch qualifizierte Fachkräfte.", "借助自动化工具接管那些机械死板的重复性繁琐流程，能够把专家骨干彻底解放出来。"),
            ("der Roboter", "der", "n.", "-", "智能工业特种作业机器人", "Industrieroboter montieren Autokarossen in modernen Fabriken im Sekundentakt.", "重载六轴工业机器人在现代智能黑灯工厂车间内以秒级节拍精准焊装轿车车身。"),
            ("die Robotik", "die", "n.", "-", "控制工程智能机器人学", "Die Robotik macht rasante Fortschritte bei der Entwicklung feinfühliger Prothesen.", "机器人学在研发具备高精度力控触觉感知能力的仿生智能义肢领域取得了突飞猛进。"),
            ("das Big Data", "das", "n.", "-", "海量异构多元巨量大数据", "Big Data eröffnet ungeahnte Möglichkeiten für die präzise Wetter- und Klimavorhersage.", "海量大数据的实时融合运算为超精准极端气候模拟研判开拓出了前所未有的视界。"),
            ("die Cloud", "die", "n.", "-s", "分布式弹性云计算系统", "Immer mehr Betriebe migrieren ihre Unternehmensdaten in die hochsichere Cloud.", "越来越多传统重度实体企业正坚定将核心企业数据底座向高安全级云平台迁移。"),
            ("das Cloud-Computing", "das", "n.", "-", "弹性算力调度云计算", "Cloud-Computing ermöglicht ortsunabhängiges, hochflexibles Arbeiten im Homeoffice.", "基于云原生的计算与算力调度为广大员工随时随地居家远程办公提供了无缝支撑。"),
            ("das Internet der Dinge", "das", "n.", "-", "万物互联万物智能物联网(IoT)", "Im Internet der Dinge kommunizieren smarte Haushaltsgeräte autonom miteinander.", "在万物互联的物联网全景生态中，智能家电彼此之间能够实现高度自组织协同联动。"),
            ("das Smart Home", "das", "n.", "-s", "全屋智能互联智慧家居", "Ein Smart Home regelt Heizung, Beleuchtung und Belüftung energieeffizient.", "全屋智能中枢能够根据居室主人起居习惯将照明采暖与新风调控在最佳节能工况。"),
            ("die Cybersicherheit", "die", "n.", "-", "网络空间国防级数字安全", "Cybersicherheit ist zu einer Überlebensfrage für moderne Staaten und Konzerne geworden.", "构筑坚不可摧的网络安全防线已上升为关乎现代国家主权与跨国巨头生死存亡的命脉。"),
            ("die IT-Sicherheit", "die", "n.", "-", "信息系统底层架构IT安全", "Regelmäßige Sicherheitsaudits und Penetrationstests stärken die betriebliche IT-Sicherheit.", "定期延聘第三方安全攻防团队实施渗透测试与红蓝对抗，能极大加固企业IT防波堤。"),
            ("der Hackerangriff", "der", "n.", "-e", "黑客有组织恶意网络突袭攻击", "Ein koordinierter Hackerangriff legte die IT-Infrastruktur des Universitätsklinikums lahm.", "一场蓄谋已久的多源分布式黑客恶意突袭瞬间瘫痪了该大学医学院的全部就诊系统。"),
            ("der Cyberangriff", "der", "n.", "-e", "网络空间破坏性敌对袭击", "Kritische Infrastrukturen wie Strom- und Wassernetze müssen vor Cyberangriffen geschützt werden.", "水电气等直接关乎亿万民生福祉的底层关键信息基础设施必须严防死守一切网络袭击。"),
            ("die Ransomware", "die", "n.", "-s", "敲诈勒索磁盘高强度加密病毒", "Erpresserische Ransomware verschlüsselt Firmendaten und fordert Millionensummen in Krypto.", "穷凶极恶的勒索病毒瞬间锁死全盘商业机密底账，并在弹窗中叫嚣索要巨额加密货币。"),
            ("die Schadsoftware", "die", "n.", "-s", "恶意流氓间谍有害木马程序", "Tückische Schadsoftware gelangt oft über getarnte E-Mail-Anhänge in das System.", "披着羊皮的各类恶意木马后门往往正是借由伪装成发票的钓鱼邮件附件悄然植入系统。"),
            ("die Malware", "die", "n.", "-", "全品类有害恶意软件总称", "Moderne Virenscanner erkennen polymorphe Malware anhand von Verhaltensmustern.", "新一代智能杀毒软件能够凭借异常行为指纹特征精准识别千变万化的变种恶意软件。"),
            ("das Phishing", "das", "n.", "-", "伪造高仿网页套取密码网络钓鱼", "Beim Phishing fälschen Kriminelle Bank-Websites, um an vertrauliche Passwörter zu gelangen.", "网络钓鱼黑产通过像素级高仿各大网上银行登录界面，诱骗毫无防备的受害人输入密码。"),
            ("die Phishing-Mail", "die", "n.", "-s", "伪装官方发出的欺诈钓鱼假邮件", "Klicken Sie niemals unüberlegt auf verdächtige Verlinkungen in einer Phishing-Mail!", "凡是收到催缴欠费等来路可疑的钓鱼欺诈邮件，切记严禁盲目手欠点击其中任何网址！"),
            ("der Betrug", "der", "n.", "-", "蓄谋已久线上电信网络欺诈", "Online-Betrug verursacht Jahr für Jahr volkswirtschaftliche Schäden in Milliardenhöhe.", "层出不穷、花样翻新的电信网络新型违法诈骗每年在全社会撕开数十亿巨额财富创口。"),
            ("die Schwachstelle", "die", "n.", "-n", "软件代码漏洞未修补安全短板", "Entwickler müssen entdeckte Schwachstellen durch sofortige Sicherheitsupdates schließen.", "软件研发团队在接到零日漏洞预警后，必须以战时状态连夜编译推送安全补丁堵住短板。"),
            ("die Sicherheitslücke", "die", "n.", "-n", "系统被黑客打穿破译之安全漏洞", "Kriminelle nutzten eine bekannte Sicherheitslücke aus, um sensible Kundendaten abzugreifen.", "网络犯罪分子正是精准利用了这一尚未修复的知名后门漏洞，瞬间盗取了海量客户资料。"),
            ("das Patch", "das", "n.", "-es", "官方紧急热修复补丁程序", "Installieren Sie das offizielle Sicherheitspatch sofort nach der Veröffentlichung!", "在官方紧急漏洞修补公告发布的同一时刻，请立即在所有生产服务器上打好热修复补丁！"),
            ("die Verschlüsselung", "die", "n.", "-en", "非对称端到端密文加密技术", "Die lückenlose Ende-zu-Ende-Verschlüsselung schützt vertrauliche Chats vor fremden Blicken.", "全天候无死角的底层端到端强加密技术确保了私密聊天记录绝不可能被中间人偷窥窃听。"),
            ("verschlüsseln", "", "v.", "verschlüsselt, verschlüsselte, verschlüsselt", "将明文编译转化为密文", "Moderne Messenger-Dienste verschlüsseln sämtliche versendeten Daten automatisch.", "当下一流的安全即时通讯工具默认会将用户发送的所有图文音视频全部打乱强力加密。"),
            ("entschlüsseln", "", "v.", "entschlüsselt, entschlüsselte, entschlüsselt", "凭借密钥解密还原明文", "Nur der rechtmäßige Empfänger mit dem passenden privaten Schlüssel kann die Nachricht entschlüsseln.", "唯有持有与之严格匹配的私钥证书的合法收件人终端，方能将这封绝密公函解密还原。"),
            ("die Authentifizierung", "die", "n.", "-en", "严格身份认证确权鉴权机制", "Die Zwei-Faktor-Authentifizierung bietet einen exzellenten Schutz gegen Kontodiebstahl.", "开启双因子多重身份核验鉴权，是彻底杜绝网络社交与银行账号惨遭盗号的最强护身符。"),
            ("das Passwort", "das", "n.", "Passwörter", "访问系统通行凭据密钥密码", "Verwenden Sie für jeden Online-Dienst ein einzigartiges, langes und komplexes Passwort!", "请务必改掉多平台套用同一个简单密码的陋习，为每一个核心软件单独设置复杂独立密码！"),
            ("der Passwortmanager", "der", "n.", "-", "高安全加密密码管理软件箱", "Ein zuverlässiger Passwortmanager generiert und speichert hochkomplexe Passphrasen.", "一款经过开源审计的靠谱密码管理器能自动生成并安全托管上百位超高强度无规律口令。"),
            ("die Privatsphäre", "die", "n.", "-", "公民个人私密生活绝对安宁", "Die Privatsphäre ist ein fundamentales Menschenrecht, das auch digital verteidigt werden muss.", "公民的私密个人生活空间是神圣不可侵犯的基本人权，在虚拟数字世界同样理应受到捍卫。"),
            ("der Datenschutz", "der", "n.", "-", "全要素个人信息数据保护制度", "Strenger Datenschutz verhindert den gläsernen Bürger und schützt vor digitaler Überwachung.", "健全严苛的个人信息数据立法保护，坚决阻击全透明透明人现象与算法无死角全面监控。"),
            ("die DSGVO", "die", "n.", "-", "欧盟通用数据保护条例大宪章", "Die europäische DSGVO räumt Bürgern das Recht auf Auskunft und Datenlöschung ein.", "欧盟颁布实施的通用数据保护条例明确赋予了广大网民至关重要的知情查阅权与被遗忘权。"),
            ("die Einwilligung", "die", "n.", "-en", "用户明示授权知情同意书", "Websites müssen vor dem Setzen von Werbe-Cookies die ausdrückliche Einwilligung einholen.", "各大互联网站在向访客电脑悄悄植入商业广告追踪标签前，必须依法取得用户明示同意。"),
            ("die Cookie", "das", "n.", "-s", "浏览器本地缓存追踪小型文本", "Viele Nutzer lehnen das Tracking durch Cookies auf modernen Websites konsequent ab.", "越来越多具有敏锐安全意识的网民在弹出弹窗时，会坚定选择全选拒绝非必要追踪标签。"),
            ("das Tracking", "das", "n.", "-", "跨网页全天候用户行为追踪跟踪", "Kommerzielles Tracking analysiert das Klickverhalten, um personalisierte Werbung auszuspielen.", "商业化全网跨站行为轨迹追踪旨在全景刻画网民浏览偏好，以便精准投喂个性化弹窗广告。"),
            ("der Server", "der", "n.", "-", "数据中心主机高负荷服务器", "Die hochmodernen Server der Plattform stehen in einem klimaneutralen Rechenzentrum.", "该平台集群部署的数万台顶配计算节点全部安置在一座百分之百绿电驱动的零碳数据中心。"),
            ("das Rechenzentrum", "das", "n.", "Rechenzentren", "海量服务器集群数据中心机房", "Ein unterirdisches Rechenzentrum mit mehrfacher Notstromversorgung gegen Totalausfall.", "一座修筑在地底防空洞深处、配有四重重叠柴油机组应急备用供电的顶级抗震数据中心。"),
            ("die Festplatte", "die", "n.", "-n", "高转速机械或固态工作硬盘", "Eine blitzschnelle SSD-Festplatte beschleunigt den Systemstart und Ladezeiten enorm.", "换装一块读写性能拔群的NVMe高速固态硬盘能将整部电脑的开机与大型工程加载时间腰斩。"),
            ("der Speicher", "der", "n.", "-", "数据存储器，运行内存", "Ein Arbeitsspeicher von 32 Gigabyte erlaubt flüssiges Rendern von hochauflösenden Videos.", "高达三十二吉字节的双通道大运存能够确保在多任务并轨剪辑4K高清视频时丝滑顺畅。"),
            ("die Schnittstelle", "die", "n.", "-n", "软件通信程序交互接口(API)", "Über eine standardisierte API-Schnittstelle tauschen die beiden Softwaresysteme Daten aus.", "借助标准化的通用软件开放应用程序通信接口，两套独立的异构业务系统实现了秒级同步。"),
            ("die Software", "die", "n.", "-s", "计算机操作系统与应用软件", "Open-Source-Software gewährt volle Einsicht in den Quellcode und fördert Transparenz.", "崇尚自由开源理念的优质开源软件将底层代码全量开源供天下极客审计，彰显透明性。"),
            ("die Hardware", "die", "n.", "-", "计算机主板机箱物理硬件设备", "Die Hardware muss leistungsfähig genug sein, um komplexe neuronale Netze zu trainieren.", "支撑本地大模型训练深度微调的物理硬件底座必须具备极其恐怖的高密度并发吞吐算力。"),
            ("der Prozessor", "der", "n.", "-en", "核心微处理器芯片CPU", "Ein energieeffizienter Mehrkern-Prozessor meistert anspruchsvollste Berechnungen spielend.", "一枚制程顶尖、超低功耗的先进制程多核心中央处理器能够游刃有余化解天量科学算力大考。"),
            ("der Chip", "der", "n.", "-s", "纳米级超大规模集成电路芯片", "Der weltweite Mangel an Halbleiter-Chips bremste zeitweise die gesamte Automobilindustrie.", "全球汽车规级高精尖半导体纳米芯片的偶发性断供，曾一度将各大跨国车企生产线逼停。"),
            ("die Halbleiter", "die", "n.pl.", "-", "微电子工业粮食半导体元器件", "Investitionen in heimische Halbleiter-Fabriken stärken die technologische Souveränität.", "国家战略层面下大力气在本土扶持先进制程半导体晶圆代工厂，旨在牢牢筑牢科技主权。"),
            ("das Breitband", "das", "n.", "-", "千兆高速宽带接入网络体系", "Der flächendeckende Ausbau mit schnellem Breitband ist die Basis für ländliche Entwicklung.", "在广大偏远乡野实现光纤千兆超宽带全覆盖，是吸引数字游民归巢并振兴乡村经济的底座。"),
            ("das Glasfaser", "das", "n.", "-", "超高速光导纤维通信网络", "Ein direkter Glasfaseranschluss bis ins Haus garantiert symmetrische Gigabit-Geschwindigkeiten.", "千兆光纤入户工程能够为住户提供上行下行极其对称澎湃、毫无延迟的高清数字传输体验。"),
            ("die Bandbreite", "die", "n.", "-n", "网络数据吞吐传输带宽", "Für reibungsloses Streaming in Ultra-HD-Qualität benötigt man eine stabile, hohe Bandbreite.", "想要在客厅电视大屏上毫无卡顿丝滑畅享8K超高清流媒体，必须有稳定宽裕的高带宽保驾。"),
            ("die Latenz", "die", "n.", "-en", "网络数据来回收发延迟时延", "Echtzeit-Anwendungen wie Telemedizin und autonomes Fahren verlangen eine extrem niedrige Latenz.", "远程手术指导与无人全自动驾驶等极限工业级应用，对网络端到端往返时延有着毫秒级苛求。"),
            ("das Mobilfunknetz", "das", "n.", "-e", "移动无线蜂窝通信基站网", "Der rasche Ausbau des modernen 5G-Mobilfunknetzes schließt die letzten Funklöcher.", "伴随着第五代蜂窝移动通信5G网络的纵深铺开，昔日山区令人抓狂的信号盲区被逐一消除。"),
            ("das Funkloch", "das", "n.", "Funklöcher", "无手机蜂窝网络覆盖盲区死角", "Im dichten Wald geriet das Auto in ein Funkloch, und das Navi verlor die Verbindung.", "当车辆一头扎进深山密林深处的信号盲区死角时，车载在线卫星导航瞬间失去了实时路况。"),
            ("das WLAN", "das", "n.", "-s", "无线局域网接入Wi-Fi网络", "Kostenloses und schnelles WLAN steht den Reisenden im ICE-Zug flächendeckend zur Verfügung.", "在德铁全系高铁动车组车厢内，全域覆盖的高速免费无线局域网随时恭候广大旅人畅连。"),
            ("der Hotspot", "der", "n.", "-s", "公共免密接入无线热点", "In der Innenstadt verbinden sich Touristen automatisch mit dem städtischen WLAN-Hotspot.", "漫步在市中心步行街头，游客手机便能自动无缝握手连入市政当局铺设的公共免费无线热点。"),
            ("das Endgerät", "das", "n.", "-e", "用户移动桌面终端设备", "Ein responsives Webdesign passt sich flexibel an die Bildschirmgröße jedes Endgeräts an.", "采用流式响应式排版的前沿网页能够根据访客手中手机、平板或台式机的屏幕尺寸智能自适应。"),
            ("das Betriebssystem", "das", "n.", "-e", "计算机硬件调度操作系统", "Ein sicheres und quelloffenes Betriebssystem schützt die Privatsphäre vor neugierigen Blicken.", "一套经受过全球顶级极客严苛代码审计的开源操作系统能够为用户筑牢抵御窥探的数字堡垒。"),
            ("die Anwendung", "die", "n.", "-en", "业务应用软件与实操落地", "Kryptografische Anwendungen sichern den elektronischen Zahlungsverkehr verlässlich ab.", "高强度前沿密码学数学工具的实操落地运用，为全人类电子跨国金融转账结算保驾护航。"),
            ("der Nutzer", "der", "n.", "-", "系统实名注册使用操作者", "Der Nutzer kann in den Sicherheitseinstellungen selbst bestimmen, welche Daten geteilt werden.", "每位注册用户均拥有在后台安全控制台里自主勾选裁定何种非核心数据允许共享的绝对权利。"),
            ("das Interface", "das", "n.", "-s", "人机交互图形用户操作界面", "Ein intuitives, barrierefreies Interface erleichtert auch Senioren den Zugang zur digitalen Welt.", "一套遵循人性化人体工学设计的无障碍图形操作界面，能让古稀长者也毫无门槛拥抱数字生活。"),
            ("die Benutzeroberfläche", "die", "n.", "-n", "系统交互视窗图形界面", "Die aufgeräumte Benutzeroberfläche besticht durch Eleganz, Übersichtlichkeit und Schnelligkeit.", "整洁素雅、删繁就简的系统交互操作界面，在极简审美、层次清晰与飞速响应上令人眼前一亮。"),
            ("die Usability", "die", "n.", "-", "交互可用性与用户易用度", "Hohe Usability sorgt dafür, dass sich Neukunden ohne langes Studium der Anleitung zurechtfinden.", "卓越的软件易用度能确保哪怕此前毫无经验的纯新手也无需翻阅枯燥手册即可直接上手实操。"),
            ("der Bug", "der", "n.", "-s", "代码深处潜伏之运行故障", "Die Programmierer arbeiteten die ganze Nacht durch, um den kritischen Bug rechtzeitig zu beheben.", "核心研发工程师在机房挑灯夜战通宵达旦地排查调试，终于在天亮正式上线前扑灭了致命Bug。"),
            ("das Programmieren", "das", "n.", "-", "编写机器指令代码编程", "Programmieren sollte an modernen Schulen genauso selbstverständlich wie Fremdsprachen gelehrt werden.", "在数字化浪潮席卷全球的当代，代码编程思维的普及应当像外语教学一样被列入基础必修大纲。"),
            ("der Programmierer", "der", "n.", "-", "软件开发代码编写程序员", "Als talentierter Programmierer entwickelt er elegante Algorithmen für autonome Fahrzeuge.", "作为一名天赋异禀的资深软件工程师，他正夜以继日为无人全自动驾驶整车编写神经网络算法。"),
            ("die Programmiersprache", "die", "n.", "-n", "人机对话编程语言体系", "Python gilt aufgrund seiner klaren Syntax als die weltweit beliebteste Programmiersprache für KI.", "Python凭借其优雅近乎自然语言的极简语法，无可争议当选为全球人工智能科研开发第一语言。"),
            ("die Zukunft", "die", "n.", "-", "充满无限遐想科技未来", "Die Zukunft der Menschheit entscheidet sich daran, ob wir die Technik zum Wohle aller einsetzen.", "人类社会走向何方，在根本上取决于我们是否有足够的政治智慧与道德担当将科技导向造福苍生。")
        ]
    },

    # LESSON 8
    {
        "id": "B1_L08",
        "title": "第8课：气候保护、生态文明与新能源革命 (Klimaschutz & Ökologie)",
        "summary": "掌握带 zu 不定式替代被动 (sein + zu + Infinitiv)、碳中和承诺与生物多样性保护",
        "grammar": {
            "title": "sein + zu + 不定式 替代情态动词被动语态 (Passiversatz)",
            "sections": [
                {
                    "heading": "1. sein + zu + Infinitiv 表必须 (muss... werden) 或能够 (kann... werden)：",
                    "content": "• Diese Aufgabe ist bis Freitag zu erledigen. (= muss erledigt werden)\n• Der Klimawandel ist nicht mehr zu leugnen. (= kann nicht mehr geleugnet werden)"
                },
                {
                    "heading": "2. 环保政治核心词汇",
                    "content": "• die Klimaneutralität (碳中和)\n• die Energiewende (能源革命转型)\n• der ökologische Wandel (绿色生态转型)"
                }
            ]
        },
        "quiz": [
            {
                "id": "B1_L08_Q1",
                "type": "GRAMMAR_FILL",
                "question": "Der CO2-Ausstoß ______ (sein + zu + Infinitiv) weltweit drastisch zu senken.",
                "options": ["ist", "wird", "hat", "muss"],
                "correctIndex": 0,
                "explanation": "表必须被做（muss gesenkt werden），被动替代句式为 ist ... zu senken。"
            },
            {
                "id": "B1_L08_Q2",
                "type": "VOCAB_MEANING",
                "question": "德国举世瞩目的能源转型核心口号 'die Energiewende' 意思是：",
                "options": ["能源战略彻底大转型（废核退煤转向可再生绿电）", "拉闸限电停电事故", "油价暴涨补贴政策", "新建十座火力发电厂"],
                "correctIndex": 0,
                "explanation": "die Energiewende 是德国向绿色、低碳、可再生能源与彻底淘汰核能煤炭转型的国家大战略专属词汇。"
            }
        ],
        "words": [
            ("der Klimaschutz", "der", "n.", "-", "全人类协同应对气候保护", "Effektiver Klimaschutz verlangt mutige globale Abkommen und verbindliche Reduktionsziele.", "落实行之有效的全球气候保护迫切呼唤国际社会达成展现担当的刚性减排协定。"),
            ("die Klimaneutralität", "die", "n.", "-", "净零排放碳中和最高愿景", "Die Europäische Union strebt bis zum Jahr 2050 die vollständige Klimaneutralität an.", "欧盟通过立法形式确立起庄严宏伟目标：到2050年全域率先实现全部经济活动的碳中和。"),
            ("klimaneutral", "", "adj.", "", "实现二氧化碳净零排放的", "Immer mehr innovative Betriebe produzieren ihre Waren bilanziell völlig klimaneutral.", "越来越多勇立潮头的创新型制造龙头通过绿电消纳实现了全生命周期完全碳中和生产。"),
            ("die Erderwärmung", "die", "n.", "-", "全球地表平均气温上升", "Die Begrenzung der globalen Erderwärmung auf 1,5 Grad ist das Ziel des Pariser Abkommens.", "将全球平均升温幅度咬死在工业化前一点五度安全红线以内，是巴黎气候协定的定海神针。"),
            ("die Treibhausgase", "die", "n.pl.", "-", "致全球变暖之温室气体", "Zu den gefährlichsten Treibhausgasen zählen neben Kohlendioxid vor allem Methan und Lachgas.", "在造成温室效应的元凶中，除了耳熟能详的二氧化碳，更有威力数倍于它的甲烷与氧化亚氮。"),
            ("das Methan", "das", "n.", "-", "强效温室气体甲烷气体", "Auftauende Permafrostböden in der Tundra setzen unkontrollierbare Mengen Methan frei.", "西伯利亚冻原带深处永久冻土层的剧烈融化，正向大气层不受控地释放天量沉睡万年的甲烷。"),
            ("der Kohlenstoff", "der", "n.", "-", "自然界基本生命元素碳", "Moore und Ozeane sind riesige natürliche Senken für die Speicherung von Kohlenstoff.", "连绵广袤的原生态泥炭湿地与汪洋大海是地球自然生态系统中吞吐固化巨量碳元素的水库。"),
            ("die Energiewende", "die", "n.", "-", "德国国家能源根本性转型大战略", "Die historische Energiewende hin zu Wind und Sonne erfordert den massiven Ausbau der Netze.", "向彻底摆脱化石燃料转向风光绿电的伟大能源大转型，倒逼全欧超高压输电走廊全线扩容。"),
            ("der Atomausstieg", "der", "n.", "-", "彻底终结民用核电时代退出", "Mit dem Atomausstieg verabschiedete sich Deutschland endgültig von der Kernenergie.", "伴随着境内最后一座商业核电机组的彻底解列退役，德国向核裂变发电时代挥手告别。"),
            ("der Kohleausstieg", "der", "n.", "-", "有序淘汰燃煤火力发电退煤", "Der beschlossene Kohleausstieg sichert den schrittweisen Abschied von der CO2-Schleuder.", "国家立法层面的有序淘汰燃煤火电决议，确保了逐步向高排放、高污染的烟囱时代说再见。"),
            ("der Strukturwandel", "der", "n.", "-", "产业格局脱胎换骨式结构转型", "Die traditionellen Braunkohlereviere stehen mitten in einem tief greifenden Strukturwandel.", "昔日仰赖挖煤发电的传统传统老工业采掘矿区，如今正经历着脱胎换骨式的经济结构重塑。"),
            ("die Ökologie", "die", "n.", "-", "生态文明大系统生态学", "Die wissenschaftliche Ökologie erforscht die komplexen Wechselwirkungen zwischen Arten und Umwelt.", "现代系统生态学致力于穷尽考掘万物生灵、生物群落与其生存周边环境之间的错综交互。"),
            ("das Ökosystem", "das", "n.", "-e", "自然平衡生态生命系统", "Intakte Ökosysteme reinigen das Wasser, regulieren das Wetter und schenken Nahrung.", "保存完好未遭人类粗暴践踏的自然生态系统能够自我净化水源、调节微气候并滋养众生。"),
            ("die Biodiversität", "die", "n.", "-", "地球生命多样性物种多样性", "Der dramatische Verlust an globaler Biodiversität bedroht die Grundlagen unserer Zivilisation.", "全球生物多样性的断崖式雪崩衰减正在从底层动摇维系人类文明繁衍生息的生态根基。"),
            ("die Artenvielfalt", "die", "n.", "-", "大千世界物种丰富多样性", "Pestizide in der industriellen Landwirtschaft gefährden die heimische Artenvielfalt massiv.", "在集约化单一农田中大剂量滥用农药化肥，对本地昆虫与鸟类的物种丰富度造成了毁灭打击。"),
            ("das Artensterben", "das", "n.", "-", "物种灭绝第六次生命大浩劫", "Forscher warnen vor einem beispiellosen Artensterben, das durch menschliche Eingriffe beschleunigt wird.", "古生物学家与生态学家警告：受人类贪婪盲目扩张所驱使，地球正滑向第六次物种大灭绝。"),
            ("das Insektensterben", "die", "n.", "-", "授粉昆虫种群大范围暴跌消亡", "Das Insektensterben hat verheerende Folgen für die Bestäubung von Obstbäumen.", "蜜蜂与野蜂等传粉昆虫种群的大规模凋敝消亡，给全球果园与农作物的自然授粉拉响了警报。"),
            ("das Bienensterben", "das", "n.", "-", "蜜蜂群落集体崩溃倒毙", "Parasiten und Monokulturen tragen maßgeblich zum weltweiten Bienensterben bei.", "外来寄生虫感染侵袭与连绵数千里的单一机械化连作种植，被证实是导致蜂群崩溃的推手。"),
            ("der Lebensraum", "der", "n.", "Lebensräume", "野生物种自然栖息繁衍地", "Die Zersiedelung der Landschaft zerstört den natürlichen Lebensraum seltener Wildtiere.", "城市无节制的粗放式摊大饼摊开扩张，将珍稀野生动物赖以生存割裂的生境栖息地碾碎。"),
            ("das Biotop", "das", "n.", "-e", "特种动植物微观群落生境", "Ein renaturierter Flusslauf bildet ein wertvolles Biotop für Amphibien und Wasservögel.", "退耕退牧后重回大自然怀抱、重现蜿蜒水态的自然河道，成了两栖动物与涉禽的水上家园。"),
            ("die Renaturierung", "die", "n.", "-en", "还荒还野退耕还湿生态修复", "Die kostspielige Renaturierung ehemaliger Moore leistet einen fantastischen Beitrag zum Klimaschutz.", "耗费巨资对昔日遭过度人工排干的干涸泥炭地实施再湿润生态修复，对锁死碳源贡献卓绝。"),
            ("das Moor", "das", "n.", "-e", "高寒原生态泥炭沼泽湿地", "Nasse Moore binden pro Hektar weitaus mehr Kohlenstoff als die gleiche Fläche Mischwald.", "积水饱满的原生泥炭沼泽湿地每公顷锁住并封存的碳总量，竟远胜同等面积的繁茂温带森林。"),
            ("die Trockenlegung", "die", "n.", "-en", "人工排干沼泽抽水干化", "Die historische Trockenlegung feuchter Böden für Äcker setzt jahrtausendealte Treibhausgase frei.", "历史上为开垦粮田而盲目大规模开凿水渠排干湿地的鲁莽举措，将地底封存千年的陈年碳释放。"),
            ("die Entwaldung", "die", "n.", "-", "大面积原始热带雨林滥伐", "Die rücksichtslose Entwaldung des Amazonas-Regenwaldes muss sofort gestoppt werden.", "针对被誉为地球之肺的亚马孙原始热带原始雨林所实施的野蛮滥砍滥伐，必须即刻被叫停。"),
            ("der Urwald", "der", "n.", "Urwälder", "亘古未遭斧斤之原始远古巨林", "In den letzten intakten Urwäldern Europas leben noch scheue Wölfe und Bären.", "在欧洲大陆极少数硕果仅存的原始巨林深处，依旧隐现着生性警觉机敏的灰狼与棕熊踪迹。"),
            ("der Regenwald", "der", "n.", "Regenwälder", "热带常绿阔叶高冠雨林", "Tropische Regenwälder beherbergen mehr als die Hälfte aller bekannten Tier- und Pflanzenarten.", "终年高温多雨的热带阔叶雨林庇护着整颗蓝色星球上已知全部动植物物种半数以上的宝库。"),
            ("die Aufforstung", "die", "n.", "-en", "植树造林生态筑屏大造林", "Globale Aufforstungsprojekte mit klimaresistenten Baumarten sind ein Hoffnungsträger.", "在荒漠化退化边缘甄选耐旱抗虫的特选先锋树种开展规模化植树造林，是点亮绿色的希望。"),
            ("die Monokultur", "die", "n.", "-en", "大面积单一品种连作农林", "Ausgedehnte Fichten-Monokulturen fielen dem Borkenkäfer in Massen zum Opfer.", "连绵成片、缺乏生态抗性的单一品种纯云杉人工林，在干旱年景遭松皮小蠢虫一网打尽覆灭。"),
            ("der Mischwald", "der", "n.", "Mischwälder", "针阔混交健康原生复合森林", "Ein stabiler Mischwald aus Eichen, Buchen und Tannen ist widerstandsfähig gegen Stürme.", "由深根系橡树、山毛榉与冷杉错落搭建的针阔混交林在面对咆哮的十二级大风暴时坚不可摧。"),
            ("die Dürre", "die", "n.", "-n", "赤地千里田间龟裂大旱灾", "Anhaltende sommerliche Dürre lässt Flusspegel sinken und behindert die Binnenschifffahrt.", "酷夏旷日持久的干旱少雨使得内陆航运大河水位暴跌至见底，导致大宗水运航道陷入瘫痪。"),
            ("die Hitzeperiode", "die", "n.", "-n", "连月热浪肆虐持久高温酷暑", "Während der Hitzewelle starben viele dehydrierte ältere Mitbürger in überhitzten Dachwohnungen.", "在无休止的持久极端高温热浪肆虐期间，不少困在密闭顶楼闷罐房内的虚弱独居老人不幸中暑。"),
            ("das Hochwasser", "das", "n.", "-", "江河暴涨倾盆暴雨洪峰洪水", "Sintflutartige Regenfälle lösten in den engen Flusstälern verheerendes Hochwasser aus.", "天漏一般的极端倾盆短时特大强降雨在崇山峻岭峡谷河道内催生了具有毁灭性冲击力的特大山洪。"),
            ("die Überschwemmung", "die", "n.", "-en", "江堤溃决漫灌大水漫溢成灾", "Die schlammige Überschwemmung riss Brücken, Straßen und ganze Häuserzeilen mit sich.", "浊浪排空、裹挟着泥沙巨石的凶猛洪峰无情将沿途桥梁防线与整片依水而建的民居夷为废墟。"),
            ("die Katastrophe", "die", "n.", "-n", "生灵涂炭惨烈自然大灾变", "Die Flutkatastrophe im Ahrtal zeigte schmerzhaft die verletzliche Seite unserer Infrastruktur.", "德国阿尔河谷当年突遭的毁灭性特大洪水泥石流浩劫，血淋淋揭示出基础设施在天灾前的脆弱。"),
            ("der Katastrophenschutz", "der", "n.", "-", "国家级防灾减灾应急救援防线", "Freiwillige Helfer des Technischen Hilfswerks bilden das Rückgrat im Katastrophenschutz.", "由民间热心群众广泛投身参与的联邦技术救援署志愿大军，构筑起防灾应急救援的铜墙铁壁。"),
            ("das Extremwetter", "das", "n.", "-", "偏离正轨的极端恶劣灾害气候", "Wissenschaftler führen die Häufung von Extremwetter direkt auf den Klimawandel zurück.", "气象科学界在复核了海量超算气候模拟推演后断言：极端天气的成倍激增与全球变暖直接挂钩。"),
            ("die Ressource", "die", "n.", "-n", "大自然赋存之宝贵天然资源", "Wasser wird im 21. Jahrhundert zu einer der wertvollsten und am heißesten umkämpften Ressourcen.", "在波澜壮阔的二十一世纪，清澈甘洌的淡水资源正日益上升为各大地缘大国博弈争夺的命脉。"),
            ("die Wasserknappheit", "die", "n.", "-", "饮用及灌溉水源极度匮乏短缺", "Viele südeuropäische Regionen leiden im Hochsommer unter akuter Wasserknappheit.", "在艳阳高照的盛夏酷暑时节，南欧多个农业大省常常因极度缺水被迫向农田实施灌溉限流。"),
            ("die Ernte", "die", "n.", "-n", "五谷丰登农业大田秋收收成", "Trockenheit vernichtete fast die Hälfte der diesjährigen Weizenernte.", "无情的久旱不雨导致全省大田里原本沉甸甸的冬小麦收成几近腰斩，损失惨重。"),
            ("der Ernteausfall", "der", "n.", "Ernteausfälle", "大田绝收大面积颗粒无收", "Versicherungen federn die finanziellen Verluste der Landwirte bei Ernteausfall ab.", "政策性农业气象灾害保险能够在暴雨或大旱导致大田绝收颗粒无收时为农户撑起兜底防护网。"),
            ("die Wende", "die", "n.", "-", "时代根本性分野大拐点大转折", "Wir stehen vor der Jahrhundertaufgabe einer ökologischen und gesellschaftlichen Wende.", "全人类此时此刻正屹立在一场关乎人类文明兴衰存亡的宏大生态与社会大转折的分水岭前。"),
            ("die Nachhaltigkeit", "die", "n.", "-", "永续代际公平之全面可持续性", "Nachhaltigkeit verlangt ein Wirtschaften innerhalb der planetaren Belastungsgrenzen.", "所谓可持续发展的真谛，就是要求全人类的一切经济生产活动决不能逾越地球生态红线。"),
            ("nachhaltig", "", "adj.", "nachhaltiger, am nachhaltigsten", "经久不息利在千秋可持续的", "Investieren Sie in nachhaltige Unternehmen, die ökologische Verantwortung leben!", "将资本要素坚定配置引导注入那些将生态环保深植入企业血脉中的真正可持续优质实体！"),
            ("die Kreislaufwirtschaft", "die", "n.", "-", "吃干榨净资源全循环闭环经济", "Die Kreislaufwirtschaft schließt Materialkreisläufe und vermeidet giftige Abfallströme.", "全面构建循环经济体系能够实现全部大宗工业物料内部高效内循环，从根本上终结排污。"),
            ("die Wiederverwertung", "die", "n.", "-en", "废旧物品深度回炉再资源化", "Die Wiederverwertung von Elektroschrott schont die weltweiten Vorkommen an seltenen Erden.", "针对淘汰废弃电子垃圾开展精细化拆解与再资源化提纯，能极大拯救全球告急的稀土资源。"),
            ("das Recycling", "das", "n.", "-", "垃圾分类循环再生加工工程", "Modernes Recycling von Industriemetallen spart bis zu 95 Prozent der Primärenergie.", "利用精湛冶炼工艺对工业废旧金属废料实施深加工循环再生，能较原矿冶炼节约百分之九十五电力。"),
            ("der Rohstoff", "der", "n.", "-e", "未经深加工的工业原材料矿产", "Der unersättliche Hunger nach knappen Rohstoffen treibt den Tiefseebergbau an.", "工业资本对极度稀缺关键战略矿产资源的贪婪狂渴，正荒谬地将野蛮采掘推向脆弱的大洋深海。"),
            ("die Ressourcenschonung", "die", "n.", "-", "厉行集约节约资源节约涵养", "Leichtbau und modulares Design leisten einen unschätzbaren Beitrag zur Ressourcenschonung.", "在新一代高端装备制造中推行超轻量化结构与模块化设计，是对节约涵养战略资源的巨大贡献。"),
            ("der Ökostrom", "der", "n.", "-", "纯绿色零碳核发清洁电能", "Durch den Bezug von hundert Prozent Ökostrom senkt der Haushalt seinen CO2-Ausstoß drastisch.", "通过在用电合同中主动选定全绿电消纳方案，每个普通普通工薪家庭都能将碳排放大幅压低。"),
            ("die Windenergie", "die", "n.", "-", "巨大叶轮捕捉的绿色风力能源", "Offshore-Windparks auf hoher See liefern gigantische Mengen zuverlässiger Windenergie.", "挺拔巍峨屹立在狂风巨浪外海深处的庞大海上风电集群，正昼夜不歇泵送出巨量无尽清洁电能。"),
            ("der Windpark", "der", "n.", "-s", "成片排布风力发电机集群阵列", "Bürgerwindparks beteiligen die lokale Bevölkerung direkt am finanziellen Ertrag.", "由全村村民集资入股合建的社区绿色风力发电阵列，让绿色转型的经济红利直接造福当地乡亲。"),
            ("die Photovoltaik", "die", "n.", "-", "半导体光生伏特效应光伏发电", "Photovoltaik-Module auf Lagerhallen machen Gewerbegebiete zu echten Stromerzeugern.", "在数万平米物流仓储中心巨型屋顶全量铺设光伏电站，让昔日工业用电大户摇身变为绿电发电商。"),
            ("die Geothermie", "die", "n.", "-", "地心深处蕴藏滚烫地热热能", "Tiefengeothermie heizt im Winter ganze Stadtviertel emissionsfrei und dauerhaft.", "钻探开采地壳深处的数千米高热地热循环水，能在寒冬为整片大型城区提供取之不尽的零碳供暖。"),
            ("die Wärmepumpe", "die", "n.", "-n", "逆卡诺循环高效节能热泵机组", "Eine moderne Wärmepumpe gewinnt Heizenergie aus der Umgebungsluft oder dem Erdreich.", "一台能效优异的新型变频热泵机组能够极其聪明地将周围空气或土壤中蕴含的低品位热能搬运入室。"),
            ("die Biomasse", "die", "n.", "-", "农林有机废料秸秆生物质能", "Biomasse aus Reststoffen der Holzwirtschaft liefert flexibel regelbare Spitzenenergie.", "对林业伐木下脚料与农田秸秆开展生物质颗粒气化发电，是电网平抑风光波动的最佳调峰压舱石。"),
            ("der Wasserstoff", "der", "n.", "-", "元素周期表第一号清洁能源氢", "Grüner Wasserstoff gilt als der entscheidende Energieträger für die CO2-freie Stahlproduktion.", "利用可再生绿电电解纯水制备的真正零碳绿氢，是实现重工业钢铁高炉彻底零碳脱碳的终极圣杯。"),
            ("die Brennstoffzelle", "die", "n.", "-n", "氢氧结合发电之质子交换膜电堆", "Brennstoffzellen wandeln Wasserstoff geräuschlos und hocheffizient in elektrischen Strom um.", "质子交换膜燃料电池通过氢氧电化学反应将氢气蕴含的能量以极高热效率、悄无声息转化为电流。"),
            ("die Batterie", "die", "n.", "-n", "高比能高功率物理化学动力电池", "Feststoffbatterien versprechen höhere Reichweiten, kürzere Ladezeiten und mehr Sicherheit.", "下一代全固态锂金属电池在实验室大放异彩，有望赋予新能源车千公里超长续航与极速快充体验。"),
            ("die Speicherung", "die", "n.", "-en", "大容量调频调峰物理电化学储能", "Die großtechnische Speicherung von Solarstrom im Sommer für den Winter bleibt eine Hürde.", "如何将盛夏漫山遍野白白浪费的过剩光伏绿电跨季节长时储能封存至数九寒冬，是世界级科研大关。"),
            ("der Speicher", "der", "n.", "-", "电网侧或户用大容量储能电站", "Batteriespeicher stabilisieren das Stromnetz bei plötzlichen Schwankungen der Einspeisung.", "部署在特高压变电站旁的大型集装箱储能电站能在毫秒级响应调频，守护全网大电网平稳运行。"),
            ("die Netzkapazität", "die", "n.", "-en", "大电网干线外送承载转输能力", "Der zügige Ausbau der Netzkapazitäten hinkt dem Neubau von Windkraftanlagen hinterher.", "跨省跨区特高压交直流大动脉输电干线走廊的建设落地，在推进节奏上亟需打破审批藩篱全面提速。"),
            ("die Trasse", "die", "n.", "-n", "贯穿南北的大容量输电线路走廊", "Die Stromtrasse 'SuedLink' soll den Nordsee-Windstrom in den industriellen Süden transportieren.", "承载着国家能源大动脉重任的南下特高压直流输电超级走廊，旨在把北海海风绿电稳定输抵南德工业心脏。"),
            ("der Umweltschützer", "der", "n.", "-", "躬身入局执着奉献民间环保卫士", "Mutige Umweltschützer stellten sich den Baggern im bedrohten Urwald entgegen.", "在连绵古林即将遭伐木重型推土机野蛮碾压的紧要关头，英勇的民间环保卫士用血肉之躯筑起人墙。"),
            ("die Aktivistin", "die", "n.", "-nen", "挺身而出捍卫理念女性青年行动派", "Die junge Aktivistin sprach vor den Delegierten des UN-Klimagipfels mahnende Worte.", "这位一身孤胆的青年女性环保先锋站在联合国全球气候雄心峰会讲台向各国首脑发出震耳警钟。"),
            ("der Verzicht", "der", "n.", "-", "克制物欲回归本真的自觉放弃", "Verzicht auf unnötige Flugreisen und Fleischberge wird als Gewinn an Lebensqualität empfunden.", "主动戒断动辄短途乱飞的铺张虚荣与狂吃肉类，被越来越多清醒的大众体味为回归从容生命的解脱。"),
            ("das Bewusstsein", "das", "n.", "-", "触及灵魂反思觉悟的心智认知", "Ein geschärftes Umweltbewusstsein verändert die Kaufentscheidungen an der Supermarktkasse.", "一旦真正把绿水青山就是金山银山的觉悟刻入骨髓，每次在商超选购商品时都会做出截然不同的抉择。"),
            ("die Gerechtigkeit", "die", "n.", "-", "惠及后世子孙代际制度正义", "Klimagerechtigkeit bedeutet, dass die Hauptverursacher der Erwärmung die Lasten tragen müssen.", "真正意义上的气候正义与代际公平，要求在历史上占据绝大部分累计碳排放的发达国承担实质出资。"),
            ("die Generation", "die", "n.", "-en", "承前启后生生不息历史世代", "Wir haben die Erde von unseren Vorfahren nicht geerbt, sondern von unseren Kindern geliehen.", "我们脚下踩着的这片苍茫大地，从来都不是我们从父辈手中继承的遗产，而是预先向子孙后代预借的。"),
            ("die Verantwortung", "die", "n.", "-en", "重逾千钧经得起历史检验的担当", "Die historische Verantwortung für den Erhalt unseres blauen Heimatplaneten duldet keinen Aufschub.", "捍卫我们赖以安身立命的唯一蓝色美丽母星生态底线这一历史千钧重担，绝不容许任何推诿与借口！"),
            ("der Umweltschutz", "der", "Nomen", "unz.", "环境保护", "Der Umweltschutz ist eine gesamtgesellschaftliche Aufgabe für Generationen.", "环境保护是一项需要代代相传的全社会共同使命。")
        ]
    },

    # LESSON 9
    {
        "id": "B1_L09",
        "title": "第9课：公民社会、志愿服务与社会参与 (Zivilgesellschaft & Engagement)",
        "summary": "掌握第二虚拟式过去时表达对过去的虚拟非现实条件从句、德国注册协会文化(e.V.)与志愿服务",
        "grammar": {
            "title": "过去非现实条件句 (Irreale Bedingungssätze der Vergangenheit)",
            "sections": [
                {
                    "heading": "1. 过去非现实条件句构成：Wenn... hätte/wäre + Part. II, hätte/wäre... + Part. II",
                    "content": "• Wenn ich Zeit gehabt hätte, hätte ich mich ehrenamtlich engagiert.\n• Wären die Helfer nicht so schnell gekommen, wäre die Katastrophe noch größer gewesen."
                },
                {
                    "heading": "2. 德国著名的“注册协会文化” (Vereinsleben & e. V.)",
                    "content": "德国拥有近60万个经法院登记的非营利协会 (eingetragener Verein, 缩写 e. V.)，涵盖体育、救灾、慈善、音乐与邻里互助。"
                }
            ]
        },
        "quiz": [
            {
                "id": "B1_L09_Q1",
                "type": "GRAMMAR_FILL",
                "question": "Wenn die freiwillige Feuerwehr nicht rechtzeitig eingegriffen ______ (haben), wäre das Haus abgebrannt.",
                "options": ["hätte", "hatte", "habe", "hätten"],
                "correctIndex": 0,
                "explanation": "主语 die freiwillige Feuerwehr 是单数，过去非现实条件从句助动词为 hätte。"
            },
            {
                "id": "B1_L09_Q2",
                "type": "VOCAB_MEANING",
                "question": "德国社会生活中随处可见的机构后缀 'e. V.' 代表的意思是：",
                "options": ["法院正式登记的公益注册协会 (eingetragener Verein)", "有限责任跨国公司", "纯商业股份制财团", "国家直属军事机关"],
                "correctIndex": 0,
                "explanation": "e. V. 是 eingetragener Verein 的缩写，是德国公民社会极为核心的注册协会形式。"
            }
        ],
        "words": [
            ("die Zivilgesellschaft", "die", "n.", "-", "活跃有担当之现代公民社会", "Eine lebendige Zivilgesellschaft ist das Herz und der Garant einer wehrhaften Demokratie.", "生机勃勃、有担当善作为的现代公民社会是构筑坚不可摧的法治民主政体最坚韧的压舱石。"),
            ("die Demokratie", "die", "n.", "-n", "以人为本人民当家作主民主政制", "Demokratie lebt von Partizipation, Widerspruch, Diskurs und dem Ringen um den besten Weg.", "健康的民主政治生生不息的活水源头，正在于全体公众全过程的深度参与、监督与思想交锋。"),
            ("das Engagement", "das", "n.", "-s", "投身公共事务社会奉献情怀", "Bürgerschaftliches Engagement hält das Gefüge unseres Gemeinwesens zusammen.", "广大平民百姓不求回报、无私投身公共公益事业的奉献情怀，紧紧维系着整个社会的良性运转。"),
            ("engagieren", "", "v.", "engagiert, engagierte, engagiert", "躬身入局投身于 (für + Akk)", "Sie engagiert sich seit vielen Jahren mit Herzblut für benachteiligte Jugendliche.", "十数年如一日，她倾注全部心血无怨无悔地投身为来自底层困境家庭的边缘青少年铺路搭桥。"),
            ("das Ehrenamt", "das", "n.", "Ehrenämter", "不取分文不谋私利的崇高公益义工", "Rund dreißig Millionen Deutsche üben ein freiwilliges und unbezahltes Ehrenamt aus.", "在全德范围内有近三千万各行各业普通公民在业余时间常年无偿承担着各项公益义工职责。"),
            ("ehrenamtlich", "", "adj./adv.", "", "义务奉献不取薪酬的", "Er trainiert die Jugendmannschaft des örtlichen Sportvereins rein ehrenamtlich.", "他纯粹出于对体育后备幼苗的呵护，常年完全义务、不取分文担任家乡青少年足球队总教头。"),
            ("der Freiwillige", "der", "n.", "-n", "义无反顾挺身而出的志愿奉献者", "Hunderte Freiwillige packten mit an, um Sandsäcke gegen die herannahende Flutwelle zu füllen.", "数百名素不相识的志愿者争先恐后奔赴江堤一线，通宵达旦铲沙装袋阻击逼近的滔天洪峰。"),
            ("die Freiwillige", "die", "n.", "-nen", "投身志愿服务奉献女性志愿者", "Die junge Freiwillige betreut demenzkranke Senioren im städtischen Wohnstift.", "这位年轻富有朝气的女志愿者在市属老年公寓里极其细致体贴地陪伴照顾失智失能老者。"),
            ("der Bundesfreiwilligendienst", "der", "n.", "-", "全德联邦自愿志愿服务制度", "Der Bundesfreiwilligendienst bietet Schulabgängern ein Jahr praktischer Lebenserfahrung.", "国家级联邦自愿服务制度为高中毕业生在跨入大学或职场前提供了整整一年的社会淬炼平台。"),
            ("der BFD", "der", "n.", "-", "联邦志愿服务制度（口语常用缩写）", "Nach dem Abitur leistete er zwölf Monate BFD im örtlichen Naturschutzzentrum.", "高中毕业考甫一尘埃落定，他便毫不犹豫在当地自然生态环保站认认真真服了一整年全勤BFD。"),
            ("das Freiwillige Soziale Jahr", "das", "n.", "-", "自愿服务青年社会实践年(FSJ)", "Das Freiwillige Soziale Jahr erfreut sich bei jungen Menschen ungebrochener Beliebtheit.", "专为青年群体量身打造的自愿社会年实践项目在广大高中毕业生群体中备受热捧与高度青睐。"),
            ("das FSJ", "das", "n.", "-", "青年社会自愿服务年（简称）", "Während ihres FSJ im Krankenhaus entdeckte sie ihre wahre Berufung zur Ärztin.", "正是在医院病房一线作为FSJ志愿者近距离照料病患的一年里，她顿悟了立志学医救人的初心。"),
            ("das Freiwillige Ökologische Jahr", "das", "n.", "-", "全天候投身生态志愿服务年(FÖJ)", "Im FÖJ pflanzte er Hecken, renaturierte Bäche und zählte bedrohte Fledermausbestände.", "在投身全职生态志愿服务的一整年时光里，他顶风冒雨植树筑篱、清淤疏浚河流并保护蝙蝠。"),
            ("der Verein", "der", "n.", "-e", "依法发起正式登记非营利公益协会", "In fast jedem Dorf gibt es einen Gesangverein, eine Feuerwehr und einen Turnverein.", "在德语区几乎每一个偏远村庄里，都必定建有历史悠久的歌咏社、民间消防队与全民体操社。"),
            ("das Vereinsleben", "das", "n.", "-", "生机勃勃多元的德式社团协会文化", "Das rege deutsche Vereinsleben stiftet Identität, Sinn und feste soziale Bindungen.", "充满烟火气与人情味的德式社团协会文化为全社会普通百姓提供了身份认同与深厚羁绊。"),
            ("der e.V.", "der", "n.", "-", "经地方法院登记的注册协会(缩写)", "Der Tierschutzverein ist als gemeinnütziger e. V. beim Amtsgericht registriert.", "该野生动物保护协会作为具有免税资质的公益注册协会在属地初级法院完成了依法备案。"),
            ("die Mitgliedschaft", "die", "n.", "-en", "正式会员正式社员资格", "Mit der Mitgliedschaft im Alpenverein ist ein weltweiter Bergrettungsschutz verbunden.", "办理并获得阿尔卑斯山登山协会的正式会员资格，将自动享有覆盖全球的高额山岳意外搜救险。"),
            ("der Beitrag", "der", "n.", "Beiträge", "维持协会运转的例行会员会费", "Der jährliche Mitgliedsbeitrag wird für den Erhalt der vereinseigenen Sportanlagen verwendet.", "全体会员每年象征性缴纳的会费主要用于支持协会名下室内田径馆与绿茵场的翻新修缮。"),
            ("der Vorstand", "der", "n.", "Vorstände", "社团协会执委会董事会领导集体", "Die Mitgliederversammlung wählt den Vorstand turnusmäßig alle zwei Jahre neu.", "全体在册会员代表大会按照法定协会章程规定每隔两年开会直接选举产生新一届执委会。"),
            ("die Satzung", "die", "n.", "-en", "协会根本组织大法正式章程", "Gemäß der Satzung verfolgt der Verein ausschließlich gemeinnützige und mildtätige Zwecke.", "依据协会章程第一条大纲的刚性界定，本社团全心全意矢志不渝服务于非营利慈善公益宗旨。"),
            ("die Mitgliederversammlung", "die", "n.", "-en", "最高权力机构全体会员代表大会", "Auf der jährlichen Mitgliederversammlung wird der Kassenbericht entlastet.", "在每年岁末召开的全体会员代表大会上，由全体会员代表对执委会年度财务决算听证并核销。"),
            ("die Gemeinnützigkeit", "die", "n.", "-", "享受税收豁免国家认证之公益性", "Das Finanzamt prüfte die satzungsgemäße Gemeinnützigkeit der Hilfsorganisation penibel.", "税务稽征主管部门依据税法对该跨国慈善救援基金会每一笔账目往来的公益性做穿透式核验。"),
            ("gemeinnützig", "", "adj.", "", "非营利性惠及全民不谋私利的", "Gemeinnützige Stiftungen fördern Wissenschaft, Kultur, Völkerverständigung und Naturschutz.", "享有免税身份的公益性慈善基金会常年资助前沿基础科研、高雅戏剧艺术与动植物生境保育。"),
            ("die Spende", "die", "n.", "-n", "善款爱心捐资，慈善捐赠", "Dank einer großzügigen Spende konnte ein neuer Rettungswagen angeschafft werden.", "得益于某位匿名爱心人士在危难时刻的慷慨捐资，急救站终于全款添置了一台重症监护车。"),
            ("spenden", "", "v.", "spendet, spendete, gespendet", "慷慨解囊施以援手捐助", "Die Bürger spendeten spontan hunderttausende Euro für die betroffenen Flutopfer.", "在洪峰过境造成良田淹没的紧急关头，各界群众义无反顾为灾民自发捐助了数十万救灾款。"),
            ("der Spender", "der", "n.", "-", "行善不求留名爱心捐款人", "Der anonyme Spender legte keinen Wert auf öffentliche Nennung seines Namens.", "这位捐出半副身家的匿名慈善家坚决谢绝了任何媒体报道与在公众场所刻石留名的虚礼。"),
            ("die Spenderin", "die", "n.", "-nen", "女性爱心慈善捐资人", "Die Mäzenin unterstützt junge, hochbegabte Musiker mit maßgeschneiderten Instrumentenstipendien.", "这位慷慨典雅的女慈善家为一批才华横溢但出身寒微的青年学子全资定制了顶级大提琴。"),
            ("die Spendenaktion", "die", "n.", "-en", "大范围爱心集结募捐倡议行动", "Die bundesweite Spendenaktion erbrachte eine Rekordsumme für die Krebsforschung.", "在全德境内发起的这场为期一个月的防癌攻关爱心大募捐刷新了历史最高善款汇集纪录。"),
            ("die Hilfsorganisation", "die", "n.", "-en", "人道主义应急救援跨国组织", "Internationale Hilfsorganisationen versorgen Erdbebenopfer mit Zelten, Trinkwasser und Decken.", "跨国专业人道主义救援力量以闪电速度为在强震中无家可归的灾民空投帐篷、净水与防寒棉被。"),
            ("das Rote Kreuz", "das", "n.", "-", "享誉全球的日内瓦红十字会", "Das Deutsche Rote Kreuz übernimmt Katastrophenschutz, Rettungsdienst und den Blutspendedienst.", "德国红十字会在全国救灾大网中挑起大梁，统筹担负国家级应急搜救与无偿献血保供重任。"),
            ("die Feuerwehr", "die", "n.", "-en", "赴汤蹈火赴难前线消防队伍", "Die örtliche Feuerwehr rückte aus, um einen brennenden Dachstuhl zu löschen.", "接到紧急火警警报的那一刻，当地消防救援站指战员火速出动扑灭了吞噬房顶的熊熊烈火。"),
            ("die freiwillige Feuerwehr", "die", "n.", "-", "全由平民组成的志愿消防队", "Ohne die freiwillige Feuerwehr wäre der flächendeckende Brandschutz auf dem Lande undenkbar.", "若缺乏各乡镇基层由农夫、教师、店主组成的志愿消防救援队，乡间消防安全将成无源之水。"),
            ("die Berufsfeuerwehr", "die", "n.", "-en", "特大型大都会常备职业消防总队", "In Millionenstädten ist die Berufsfeuerwehr rund um die Uhr in permanenter Alarmbereitschaft.", "在超大型大都会核心城区，全职业化配置的专业消防总队全天候处于分秒必争的高等级战备。"),
            ("das Technische Hilfswerk", "das", "n.", "-", "联邦技术应急救援总署(THW)", "Das THW leistet mit schwerem Spezialgerät technische Hilfe bei Dammbrüchen und Gebäudeeinstürzen.", "联邦技术应急救援总署调配大型特种破拆重装备，在溃堤决口与楼房坍塌废墟中开展生命营救。"),
            ("das THW", "das", "n.", "-", "联邦技术救援署（官方简称）", "Einsatzkräfte des THW bauten über den reißenden Fluss binnen Stunden eine Notbrücke.", "在原桥被山洪彻底冲垮冲毁后，THW的硬核工兵队员在湍急激流之上只用了数小时便架好便桥。"),
            ("die Tafel", "die", "n.", "-n", "济困爱心食物银行配给站", "Die Tafeln retten tonnenweise noch genießbare Lebensmittel und verteilen sie an Bedürftige.", "在德语区各大都会常设的食物救济站，志愿者将商超即将下架的临期良品免费分发给特困群众。"),
            ("die Bürgerinitiative", "die", "n.", "-n", "市民自发自组织联合维权联盟", "Eine Bürgerinitiative formierte sich erfolgreich gegen den Bau einer umstrittenen Müllverbrennungsanlage.", "广大深受废气隐患威胁的业主们自发结成维权联盟，有理有利有节挫败了垃圾焚烧厂项目上马。"),
            ("die Petition", "die", "n.", "-en", "正式呈递代议机关公民请愿书", "Die Online-Petition für bezahlbare Mieten erreichte innerhalb weniger Tage hunderttausend Unterschriften.", "呼吁严厉平抑城市房租的线上网络公民请愿大联署在短短数日内便汇聚了十余万合法签名。"),
            ("unterschreiben", "", "v.", "unterschreibt, unterschrieb, unterschrieben", "在请愿书或协约上郑重签名", "Hunderttausende Bürger unterschrieben den dringenden Appell an den Deutschen Bundestag.", "数十万普通选民郑重在呈递联邦议院的紧急立法呼吁请愿书下方签署上了自己的真实姓名。"),
            ("die Unterschriftenaktion", "die", "n.", "-en", "街头现场地毯式签名大动员", "Mit einer Unterschriftenaktion in der Fußgängerzone warben sie für den Erhalt des alten Stadtparks.", "青年志愿者在市中心人潮涌动的步行街搭起展台发起签名大动员，全力抢救即将遭开发的古老公园。"),
            ("die Demonstration", "die", "n.", "-en", "行使宪法权利和平抗议大游行", "Eine friedliche Demonstration von 50.000 Menschen zog durch das Berliner Regierungsviertel.", "由五万名热心市民自发组成的一支浩浩荡荡的和平游行队伍，秩序井然走过柏林联邦政府区大道。"),
            ("die Demo", "die", "n.", "-s", "街头抗议大游行（口语常用简称）", "Am Samstagnachmittag gingen zehntausende Bürger zur Demo gegen Rassismus auf die Straße.", "在周六晴朗的午后，成千上万名来自各行各业的市民走上街头参加声势浩大的反对种族歧视大游行。"),
            ("demonstrieren", "", "v.", "demonstriert, demonstrierte, demonstriert", "走上街头举行合法抗议游行", "Studenten und Arbeiter demonstrieren gemeinsam für gerechtere Bildungschancen und bessere Löhne.", "青年学子与产业工人并肩走上宽阔大道，齐声为捍卫教育公平普惠与上调最低工时薪资高呼口号。"),
            ("das Plakat", "das", "n.", "-e", "写有鲜明政治抗议标语大横幅", "Auf ihren selbst gemalten Plakaten forderten die Demonstranten einen sofortigen Waffenstillstand.", "在自己通宵手绘制作的醒目宣传展板标语上，游行队伍旗帜鲜明敦促交战各方即刻停火止战。"),
            ("der Streik", "der", "n.", "-s", "依法组织实施产业同盟大罢工", "Der Generalstreik im gesamten öffentlichen Nahverkehr legte U-Bahnen und Busse still.", "全行业全产业链公共交通系统发起的总罢工，导致全城所有地铁班列与地面公交全线趴窝。"),
            ("streiken", "", "v.", "streikt, streikte, gestreikt", "行使法定公民权利以罢工维权", "Die Pflegerinnen streiken mutig für spürbare Entlastung und faire Personalschlüssel im Krankenhaus.", "白衣天使与护士们团结一致举行罢工，旨在敦促资方在病房彻底增补护士人手、大幅压减工作强度。"),
            ("die Solidarität", "die", "n.", "-", "休戚与共风雨同舟阶级阶层团结", "Solidarität mit den Schwächsten ist der wahre Prüfstein für den moralischen Zustand eines Volkes.", "在困难时期是否能对社会最无助边缘的弱势群体做到休戚与共，是考量一个民族道德良知的试金石。"),
            ("solidarisch", "", "adj.", "", "坚定不移站在一起同呼吸共命运的", "Die Belegschaft zeigte sich vollkommen solidarisch mit den von Entlassung bedrohten Kollegen.", "在面对资方恶意的裁员大棒时，全体在册职工展现出高度的阶级团结，誓与被裁兄弟共进退。"),
            ("der Zusammenhalt", "der", "n.", "-", "牢不可破风雨同舟社会向心力", "Sozialer Zusammenhalt schützt eine Gesellschaft vor Spaltung, Polarisierung und Radikalisierung.", "紧密坚固、坚如磐石的社会大向心力与凝聚力，能有效庇护整个国家免于滑向撕裂与极端对立。"),
            ("die Integration", "die", "n.", "-", "包容并蓄让异质文明生根融合", "Erfolgreiche Integration setzt Sprachförderung und faire Chancen auf dem Arbeitsmarkt voraus.", "实现移民群体真正心悦诚服的良性社会深度融入，其底层前提在于强力推行语言扫盲与就业公平。"),
            ("integrieren", "", "v.", "integriert, integrierte, integriert", "使之有机融入社群落地生根", "Sportvereine leisten einen unverzichtbaren Beitrag, um Geflüchtete schnell zu integrieren.", "各大基层体育俱乐部在帮助逃离战火的难民青年迅速融入当地主流圈子中立下了汗马功劳。"),
            ("die Inklusion", "die", "n.", "-", "不抛弃不放弃全纳融合理念", "Inklusion verlangt den barrierefreien Umbau von Schulen, Bahnhöfen und öffentlichen Gebäuden.", "全面推行全纳融合教育理念，刚性要求对所有中小学、火车站与市政大厅实行无死角无障碍改造。"),
            ("die Barrierefreiheit", "die", "n.", "-", "彻底消除物理出行障碍无障碍化", "Barrierefreiheit nützt nicht nur Rollstuhlfahrern, sondern auch Eltern mit Kinderwagen und Senioren.", "下大气力拆除台阶打通坡道不仅造福坐轮椅的残疾朋友，也让推着婴儿车的新生儿父母与老人受益。"),
            ("die Chancengleichheit", "die", "n.", "-", "人生起点制度保障机会公平均等", "Wahre Chancengleichheit bedeutet, dass der familiäre Hintergrund nicht über den Bildungserfolg entscheidet.", "追求绝对制度正义的机会公平均等，其终极目标就是决不能让原生家庭的穷富焊死孩子的上升通道。"),
            ("die Gerechtigkeit", "die", "n.", "-", "朗朗乾坤昭昭日月之社会正义", "Soziale Gerechtigkeit erfordert eine faire Besteuerung von extremem Reichtum und großen Erbschaften.", "实现真正名副其实的社会公平正义，必然要求政府对极度畸形的超级寡头财富与跨代巨额遗产开征重税。"),
            ("die Ungerechtigkeit", "die", "n.", "-en", "令人发指的分配不公与不公允", "Die wachsende Ungerechtigkeit bei Einkommen und Vermögen spaltet die Gesellschaft weltweit.", "在财富与收入二次分配环节日益拉大的贫富悬殊与令人发指的不公，正在多国撕开巨大的贫富鸿沟。"),
            ("die Menschenrechte", "die", "n.pl.", "-", "天赋神圣不可让渡基本人权", "Die Allgemeine Erklärung der Menschenrechte von 1948 ist ein Meilenstein der Menschheitsgeschichte.", "联合国大会在1948年庄严表决通过的《世界人权宣言》，是全人类数千年文明史上一座不朽里程碑。"),
            ("die Würde", "die", "n.", "-", "至高无上不可侵犯人之尊严", "Die Würde des Menschen ist unantastbar - so lautet der unumstößliche Artikel 1 des deutschen Grundgesetzes.", "德意志联邦共和国根本大法宪法第一条开宗明义庄严宣示：人的尊严神圣不可侵犯，不容践踏！"),
            ("das Grundgesetz", "das", "n.", "-", "立国之本最高根本大法宪法", "Das deutsche Grundgesetz garantiert Meinungsfreiheit, Versammlungsfreiheit und die Unverletzlichkeit der Wohnung.", "德国根本大法宪法以最严密法条坚决捍卫保障公民的言论自由、集会结社自由以及住宅不受侵犯权。"),
            ("die Verfassung", "die", "n.", "-en", "国家法统基石根本大宪章", "Der Verfassungsschutz wacht darüber, dass Extremisten die freiheitliche Ordnung nicht untergraben.", "宪法保卫局担负起崇高的国家安全守夜人之责，严防任何极端主义思潮企图从内部颠覆自由宪制。"),
            ("die Meinungsfreiheit", "die", "n.", "-", "知无不言言无不尽之言论自由", "Meinungsfreiheit erlaubt auch scharfe, unbequeme und provokante Kritik an den herrschenden Zuständen.", "受宪法庇护的言论自由权利，包容并允许大众对现实施政方针提出针针见血、令人如芒在背的尖锐批评。"),
            ("die Pressefreiheit", "die", "n.", "-", "独立不阿揭露内幕之新闻自由", "Ohne unabhängige Pressefreiheit degeneriert jede gewählte Demokratie zu einer leeren Fassade.", "倘若缺乏不畏强权、敢于独立发声调查的新闻自由，任何一人一票选举出的制度都将沦为虚伪空壳。"),
            ("die Versammlungsfreiheit", "die", "n.", "-", "公民自发和平集会合法权利", "Das Recht, sich friedlich und ohne Waffen zu versammeln, ist ein Eckpfeiler der bürgerlichen Freiheit.", "公民依法享有和平、手无寸铁集会结社发表政见的权利，是自由宪政大厦四梁八柱不可替代的柱石。"),
            ("die Wahl", "die", "n.", "-en", "神圣庄严之全民全国大选投票", "Freie, gleiche, geheime und unmittelbare Wahlen sind das Lebenselixier des parlamentarischen Systems.", "坚持推行自由、普遍、平等、秘密且直接的普选大选，是维系现代议会代议制度运转的生命源泉。"),
            ("wählen", "", "v.", "wählt, wählte, gewählt", "走进密闭投票间投下神圣选票", "Am kommenden Sonntag sind über sechzig Millionen wahlberechtigte Bürger aufgerufen, zu wählen.", "在即将到来的星期天，全德境内六千余万名享有法定投票权的选民将郑重走进投票点行使神圣权利。"),
            ("die Beteiligung", "die", "n.", "-en", "公众深度投身公共事务治理参与", "Bürgerbeteiligung bei großen Infrastrukturprojekten verhindert spätere wütende Proteste.", "在规划立项重大民生交通工程初期便早早引入市民全过程听证参与，能将后期的对立情绪化解于无形。"),
            ("die Mitbestimmung", "die", "n.", "-", "劳资共治职工参与企业决策权", "Die betriebliche Mitbestimmung durch Arbeitnehmervertreter im Aufsichtsrat hat den Betriebsfrieden gesichert.", "职工董事代表在监事会中依法行使企业决策共治参与权，为德国战后数十年劳资和谐立下了汗马功劳。"),
            ("die Partizipation", "die", "n.", "-", "全社会各阶层全面政治参与", "Digitale Plattformen eröffnen neue, unkomplizierte Wege für die demokratische Partizipation.", "移动互联与前沿数字技术为普通市井大众开辟了更加低门槛、多维度参与公共治理的全新通道。"),
            ("der Dialog", "der", "n.", "-e", "心平气和求同存异之平等对话", "Nur ein ehrlicher und vorurteilsfreier Dialog kann tiefe gesellschaftliche Gräben überbrücken.", "唯有展开卸下傲慢与偏见的真诚平等深长对话，方能真正跨越全社会因阶层撕裂而拉开的万丈鸿沟。"),
            ("die Zukunft", "die", "n.", "-", "由我们亲手书写的明日中国世界", "Die Zukunft einer Demokratie liegt nicht in den Händen weniger Eliten, sondern im Engagement aller Bürger.", "一个民主社会的明天与希望，从来都不操纵在极少数精英寡头指缝间，而永远掌握在奋起参与的全民手中！")
        ]
    },

    # LESSON 10
    {
        "id": "B1_L10",
        "title": "第10课：消费心理、个人财务理财与反思消费 (Konsumverhalten & Finanzen)",
        "summary": "掌握第二虚拟式过去时表达虚拟愿望、过度消费陷阱、个人破产与极简主义生活方式",
        "grammar": {
            "title": "第二虚拟式过去时表达悔恨与反省 (Hätte ich doch nur...)",
            "sections": [
                {
                    "heading": "1. 表达未实现过去的悔恨：Hätte/Wäre + Subjekt + doch nur + Partizip II!",
                    "content": "• Hätte ich doch nur nicht so viele Schulden gemacht! (要是我当初没欠这么多债该多好啊！)\n• Wäre ich damals bloß sparsamer gewesen!"
                },
                {
                    "heading": "2. 德国著名的债务咨询机制 (Schuldnerberatung)",
                    "content": "陷入资不抵债陷阱的个人可向公立救济机构申请债务咨询 (Schuldnerberatung)，通过法定个人破产程序 (Privatinsolvenz) 在三年内依法免除剩余债务、重新出发。"
                }
            ]
        },
        "quiz": [
            {
                "id": "B1_L10_Q1",
                "type": "GRAMMAR_FILL",
                "question": "Ach, ______ (haben, 第二虚拟式过去时) ich doch bloß dieses teure Auto nicht auf Kredit gekauft!",
                "options": ["hätte", "hatte", "habe", "hätten"],
                "correctIndex": 0,
                "explanation": "表达对过去行为的悔恨叹息：Hätte ich doch bloß ... gekauft!"
            },
            {
                "id": "B1_L10_Q2",
                "type": "VOCAB_MEANING",
                "question": "德国著名的反消费主义生活方式 'der Minimalismus' 核心倡导是：",
                "options": ["极简主义（断舍离物欲，专注于真正有价值之物）", "每天买十件名牌奢侈品", "拒绝使用任何电子产品", "只住五星级豪华酒店"],
                "correctIndex": 0,
                "explanation": "der Minimalismus 指反思消费主义、崇尚断舍离、减少不必要物欲的“极简主义生活方式”。"
            }
        ],
        "words": [
            ("das Konsumverhalten", "das", "n.", "-", "全社会大众综合消费行为心理", "Das Konsumverhalten der jungen Generation ist stark durch Social-Media-Trends geprägt.", "年轻一代在商超与网络上的即时消费行为心理，在极大层面上受到短视频带货种草的驱使摆布。"),
            ("die Konsumgesellschaft", "die", "n.", "-en", "物质极大丰盈之现代消费社会", "Kritiker werfen der modernen Konsumgesellschaft vor, künstliche Bedürfnisse zu wecken.", "犀利的社会学家痛斥当代消费主义社会最大的恶，就是靠着无孔不入的算法广告制造虚假物欲。"),
            ("der Konsumrausch", "der", "n.", "-", "非理性盲目买买买消费狂热狂欢", "Rabattaktionen wie der 'Black Friday' versetzen Millionen Schnäppchenjäger in einen Konsumrausch.", "黑五等电商大促通过倒计时制造人为焦虑，瞬间将数以千万计的抢购网民卷入买买买的失控狂热中。"),
            ("der Kaufrausch", "der", "n.", "-", "多巴胺上头失控剁手狂购", "Im emotionalen Kaufrausch gab er sein halbes Monatsgehalt für Designer-Klamotten aus.", "在多巴胺疯狂分泌的非理性狂热催化下，他冲动之下竟将半个月的薪水在名牌专柜挥霍一空。"),
            ("der Spontankauf", "der", "n.", "Spontankäufe", "未经深思熟虑随性冲动消费", "Platzierungen an der Supermarktkasse verführen gezielt zu unüberlegten Spontankäufen.", "大型超市在收银台前精心布置口香糖巧克力的货架陈列，正是精准瞄准了顾客排队时的冲动消费。"),
            ("verführen", "", "v.", "verführt, verführte, verführt", "巧言诱惑使其上钩消费", "Gekonnte Werbespots verführen unbedarfte Verbraucher zum Kauf unnützer Luxusgüter.", "剪辑炫目的话术广告无所不用其极地诱惑懵懂单纯的年轻消费者自掏腰包埋单无用的奢侈品。"),
            ("die Verführung", "die", "n.", "-en", "无孔不入的物欲诱惑陷阱", "Der glitzernde Konsumtempel birgt an jeder Ecke teure Verführungen für den Geldbeutel.", "在这座装点得金碧辉煌的现代巨型消费主义神殿里，每一个转角都暗藏着掏空钱包的致命诱惑。"),
            ("das Schnäppchen", "das", "n.", "-", "自以为占了大便宜的平价甩卖货", "Nicht jedes angebliche Schnäppchen im Ausverkauf entpuppt sich als echter Glücksgriff.", "商场跳楼甩卖大牌子上标榜的那些所谓跳楼价大便宜，十有八九拆穿开来都不过是清库存的劣质货。"),
            ("der Schnäppchenjäger", "der", "n.", "-", "全网比价薅羊毛猎手", "Der ehrgeizige Schnäppchenjäger vergleicht tagelang Preise auf unzähligen Portalen.", "这位极具钻研精神的薅羊毛狂热爱好者连日通宵泡在数十个比价网站上，就为了抢出几块钱差价。"),
            ("der Überfluss", "der", "n.", "-", "物质极大繁复充斥过剩过剩", "Wir ersticken im materiellen Überfluss, während die seelische Leere oft zunimmt.", "当我们在琳琅满目、多到堆不下的物质过剩垃圾中被压得喘不过气时，内心的虚无空洞却与日俱增。"),
            ("die Verschwendung", "die", "n.", "-", "暴殄天物大肆浪掷挥霍", "Die Vernichtung neuwertiger Retouren durch Großhändler ist ein Paradebeispiel für Verschwendung.", "大型跨国电商平台将退回的完好商品直接就地成吨焚烧填埋，是对人类劳动成果的大肆践踏浪掷。"),
            ("die Wegwerfgesellschaft", "die", "n.", "-", "用完即弃即抛型消费社会", "Die moderne Wegwerfgesellschaft muss durch langlebige, reparierbare Produkte abgelöst werden.", "那种倡导用完即扔、坏了就换的即抛型消费社会，必须被全面追求经久耐用与易于修理的范式替代。"),
            ("die Obsoleszenz", "die", "n.", "-", "人为蓄意让家电提前报废的老化", "Geplante Obsoleszenz sorgt dafür, dass Geräte kurz nach Ablauf der Garantiezeit kaputtgehen.", "消费电子厂商在产品主板中蓄意植入预设报废隐患，确保机器在熬过法定保修期的一瞬间精准坏掉。"),
            ("die Langlebigkeit", "die", "n.", "-", "结实耐造传承百年经久耐用性", "Die sprichwörtliche Langlebigkeit deutscher Maschinen beruht auf meisterhafter Präzision.", "德国机械设备之所以享誉国际、能长年经久耐用的底层秘密，就在于工匠们近乎强迫症的精密。"),
            ("reparieren", "", "v.", "repariert, reparierte, repariert", "起死回生巧手修缮维修", "Ein defektes Gerät zu reparieren, schont die Umwelt und spart bares Geld.", "花点心思将故障坏掉的小家电亲手修缮一新，既拯救了地球生境，更省下了真金白银的血汗钱。"),
            ("das Repair-Café", "das", "n.", "-s", "社区互助免费家电维修咖啡馆", "Im ehrenamtlich geführten Repair-Café tüfteln geschickte Nachbarn an alten Kaffeemaschinen.", "在这间由民间热心匠人自发运营的公益维修咖啡馆里，巧手的邻舍正聚精会神拆解修复旧咖啡机。"),
            ("die Finanzen", "die", "n.pl.", "-", "家庭与个人财务账目资金链", "Wer seine Finanzen nicht diszipliniert im Blick behält, verliert rasch die Kontrolle über sein Leben.", "倘若一个人连自己兜里进出账目的财务收支都做不到心中有数，他的人生也将以极快速度失控。"),
            ("das Budget", "das", "n.", "-s", "刚性框定的财务预算盘子", "Erstellte ein strenges monatliches Haushaltsbudget, um die Fixkosten im Griff zu haben.", "他为自己的小家庭拟定了一份极其严苛的月度生活开支刚性预算清单，死死摁住各项固定支出。"),
            ("der Haushaltsplan", "der", "n.", "Haushaltspläne", "开源节流收支家庭流水台账", "Ein altmodisches Haushaltsbuch hilft vielen Familien, versteckte Ausgabenfresser aufzudecken.", "一本看似老派传统的家庭收支流水手账，能帮助许多迷茫的新生代家庭精准揪出吞噬积蓄的暗洞。"),
            ("die Einnahmen", "die", "n.pl.", "-", "每月到账全部真金白银进账收入", "In Krisenzeiten sollten die monatlichen Ausgaben niemals die tatsächlichen Einnahmen übersteigen.", "在外部风雨飘摇的危机岁月里，全家每月的实际总支出决不可冲动冒进超出真实的到手净收入。"),
            ("die Ausgaben", "die", "n.pl.", "-", "柴米油盐各项开支流水支出", "Feste monatliche Ausgaben für Miete, Strom und Versicherungen lassen sich kaum drücken.", "每月雷打不动划扣的住房房租、水电暖气及各类法定义务保险费用，构成了无法压缩的刚性支出。"),
            ("die Fixkosten", "die", "n.pl.", "-", "每月雷打不动恒定硬性刚需支出", "Zu den unvermeidlichen Fixkosten zählen Krankenversicherung, Kaltmiete und Fahrkarten.", "在每一个打工人的每张工资条后，医疗保险、住房净租金与公共交通通票构成了最硬核的固定开支。"),
            ("die Konsumschulden", "die", "n.pl.", "-", "盲目超前借贷消费欠下之消费贷", "Konsumschulden für Urlaube oder Unterhaltungselektronik treiben junge Menschen in die Armutsfalle.", "为了打肿脸充胖子贷款度假或分期购买超大尺寸智能电视所背负的消费贷，正把青年推入深渊。"),
            ("die Schulden", "die", "n.pl.", "-", "令人喘不过气沉重外债债务", "Er geriet durch unbedachte Kreditkartennutzung tief in die verhängnisvolle Schuldenspirale.", "由于无节制疯狂挥霍透支多张高额度商业信用卡，他身不由己深陷进了利滚利的债务恶性漩涡。"),
            ("die Schuldenspirale", "die", "n.", "-", "利滚利越滚越大之债务死循环", "Aus der tückischen Schuldenspirale findet man ohne professionelle Hilfe selten allein heraus.", "一旦不幸滑入由高利贷分期手续费织就的债务死循环罗网，单凭个人微薄力量几乎已无力自拔。"),
            ("die Überschuldung", "die", "n.", "-", "资产归零彻底无力清偿之资不抵债", "Akute Arbeitslosigkeit und Scheidungen sind die Hauptursachen für private Überschuldung.", "突遭猝不及防的大厂裁员失业下岗或旷日持久的离婚官司撕扯，是触发个人资不抵债的最主要诱因。"),
            ("die Schuldnerberatung", "die", "n.", "-en", "公立公益债务救济化解咨询处", "Die kostenlose Schuldnerberatung der Caritas hilft verschuldeten Bürgern bei Verhandlungen mit Gläubigern.", "德国天主教明爱会常年开设的免费债务化解咨询窗口，帮助身处绝境的负债人出面同债权人磋商。"),
            ("der Schuldner", "der", "n.", "-", "被催收追索债务人欠债人", "Der verzweifelte Schuldner suchte Rat bei einer staatlich anerkannten Beratungsstelle.", "走投无路、夜不能寐的欠债人最终鼓起勇气，走进了国家正式认证的非营利债务化解咨询所。"),
            ("der Gläubiger", "der", "n.", "-", "持有借据欠条之原告债权人", "Die Gläubiger einigten sich mit dem Treuhänder auf einen prozentualen Teilerlass der Forderungen.", "各路债权人在专业破产清算信托律师的主持斡旋下，终于同意就核心本息债务达成部分豁免妥协。"),
            ("die Mahnung", "die", "n.", "-en", "盖有红印催告履约之催款函", "Nach der dritten Mahnung schaltete das Inkassobüro das zuständige Amtsgericht ein.", "在当事人对连续寄达的三封正式挂号催缴函充耳不闻后，催收追偿机构向基层法院申请支付令。"),
            ("das Mahnverfahren", "das", "n.", "-", "司法快速追讨欠款督促程序", "Das gerichtliche Mahnverfahren ermöglicht Gläubigern die rasche Durchsetzung ihrer Geldforderungen.", "启动司法级别的简易督促追索程序，能够让手握确凿借据的合法债权人迅速获得强制执行名义。"),
            ("die Pfändung", "die", "n.", "-en", "法院法警强制冻结扣押划扣", "Das Pfändungsschutzkonto (P-Konto) sichert das Existenzminimum vor dem Zugriff von Gläubigern.", "法律强制推行的防查封特别保护个人银行账户（P账户），能够替负债当事人死守住最低生活开支。"),
            ("das Existenzminimum", "das", "n.", "-", "维持生命体征最低温饱底线", "Der Staat garantiert jedem Bürger die Auszahlung des gesetzlich geschützten Existenzminimums.", "法治国家通过立法形式以铁的意志庄严保障：任何债权人皆严禁触碰侵吞公民最低温饱生存金。"),
            ("die Insolvenz", "die", "n.", "-en", "财务崩盘依法清盘破产清算", "Das Unternehmen musste wegen Zahlungsunfähigkeit einen Antrag auf Eröffnung der Insolvenz stellen.", "由于现金流彻底断裂陷入无力支付窘境，企业法人代表依法向法院正式提出了商业破产清算。"),
            ("die Privatinsolvenz", "die", "n.", "-en", "自然人重获新生个人破产程序", "Nach erfolgreichem Abschluss der dreijährigen Privatinsolvenz winkt die vollständige Restschuldbefreiung.", "只要严格遵规履行长达三年的个人破产重整考验期，当事人便能依法斩获剩余债务彻底一笔勾销。"),
            ("die Restschuldbefreiung", "die", "n.", "-", "司法最终免除剩余无力偿还债务", "Die Restschuldbefreiung ermöglicht gescheiterten Bürgern einen echten wirtschaftlichen Neuanfang.", "由破产法庭法官正式敲下法槌准予的剩余债务终身免责裁定，让跌入谷底的失败者拥抱全新起点。"),
            ("der Neuanfang", "der", "n.", "-", "放下沉重包袱轻装上阵重获新生", "Ein mutiger Neuanfang erfordert den ehrlichen Abschied von alten, zerstörerischen Verhaltensweisen.", "想要在一个干干净净的起点上拥抱崭新的人生，必然要求当事人与过往自毁式的消费作风割袍断义。"),
            ("die Ratenzahlung", "die", "n.", "-en", "分期逐期小额摊销分期付款", "Die Verlockung der zinslosen Ratenzahlung verleitet dazu, den Überblick über die Gesamtkosten zu verlieren.", "零首付分期还款的甜蜜陷阱极容易让人产生错觉，从而彻底丧失对数笔借贷累加真实规模的掌控。"),
            ("die Zinsen", "die", "n.pl.", "-", "借贷资本衍生利息高额利钱", "Wucherzinsen beim Dispokredit auf dem Girokonto fressen das Ersparte in kürzester Zeit auf.", "普通往来银行卡若常年处于透支授信状态，其高达年化百分之十以上的暴利息钱能瞬间吃光积蓄。"),
            ("der Dispokredit", "der", "n.", "-s", "银行卡循环透支授信额度", "Vermeiden Sie es, den teuren Dispokredit dauerhaft als zusätzliches Einkommen zu betrachten!", "切莫将银行卡上那笔看似随时可刷、实则利息昂贵至极的循环透支授信额度自欺欺人看作进项！"),
            ("das Girokonto", "das", "n.", "Girokonten", "个人高频资金往来结算账户", "Auf dem Girokonto gehen das Gehalt ein und die laufenden Abbuchungen für Miete ab.", "每个月辛苦打工挣来的血汗工资先是打入这张往来银行卡，随后又被房租水电自动扣缴代扣走。"),
            ("das Sparkonto", "das", "n.", "Sparkonten", "专款专用长期计息储蓄账户", "Überweisen Sie zu Monatsbeginn einen festen Betrag auf das unberührte Sparkonto!", "在每月刚发工资的第一时间，强制性将一笔预设金额自动划拨转入绝不轻易动用的储蓄备用金账户！"),
            ("der Notgroschen", "der", "n.", "-", "以备不时之需之应急救急钱", "Ein solider Notgroschen von drei Monatsgehältern fängt unvorhergesehene Reparaturen ab.", "在手头常备一笔相当于全家三个月总开销的应急救急私房钱，能在汽车突发抛锚或大病时稳住大局。"),
            ("das Ersparte", "das", "n.", "-", "省吃俭用日积月累积攒积蓄", "In Zeiten hoher Inflation verliert das mühsam Ersparte auf dem Sparbuch stetig an Kaufkraft.", "在恶性通货膨胀肆虐的特殊岁月里，辛辛苦苦省吃俭用积攒下的银行死期存款正日复一日贬值。"),
            ("die Geldanlage", "die", "n.", "-n", "科学资产配置理财稳健投资", "Eine breit gestreute Geldanlage in weltweite Aktien-ETFs schützt vor Geldentwertung.", "将个人闲钱分散配置并长期定投锚定全球龙头核心企业的股票指数基金，是抵御通胀的利器。"),
            ("die Aktie", "die", "n.", "-n", "上市公众企业股份权益股票", "Aktien repräsentieren reale Unternehmensbeteiligungen mit Chancen auf attraktive Dividenden.", "购入优质上市蓝筹股代表着你在法律层面持有了企业的底层资产，享有分享其分红增长的红利。"),
            ("der Fonds", "der", "n.", "-s", "专家打理分散风险集合投资基金", "Ein aktiv gemanagter Fonds verlangt oft hohe Ausgabeaufschläge und jährliche Verwaltungsgebühren.", "由公募基金经理主动操盘打理的传统投资基金，往往每年向基民无情收取高昂的管理费与申购费。"),
            ("der ETF", "der", "n.", "-s", "低费率被动跟踪指数基金", "Passive ETFs bilden einen Börsenindex transparent, fehlerarm und extrem kostengünstig nach.", "被动跟踪大盘的指数型ETF基金以极度透明、低摩擦成本的方式将一揽子全球巨头一网打尽。"),
            ("die Rendite", "die", "n.", "-n", "扣除通胀后真实资本年化收益率", "Ohne das Eingehen kalkulierter Risiken ist am Kapitalmarkt keine reale Rendite zu erzielen.", "在资本金融市场上，不愿承担任何合理计算后波动风险的人，注定不可能奢求任何实质收益率。"),
            ("das Risiko", "das", "n.", "Risiken", "充满不确定性金融投资波动风险", "Wer sein gesamtes Geld auf eine einzige Karte setzt, geht ein unverantwortliches Risiko ein.", "把全部身家赌注孤注一掷全部压在单一一支妖股或单一加密币上的人，是在拿自己的前途进行豪赌。"),
            ("die Risikostreuung", "die", "n.", "-", "决不把鸡蛋放同一篮子之分散化", "Breite Risikostreuung über verschiedene Anlageklassen ist die goldene Regel für jeden Investor.", "跨行业、跨国别、跨大类资产进行充分的风险大分散，是横跨百年金融投资界雷打不动的黄金铁律。"),
            ("die Diversifikation", "die", "n.", "-", "全方位多维度资产横向多角化", "Diversifikation schützt das Portfolio vor den verheerenden Folgen des Zusammenbruchs einzelner Branchen.", "严格贯彻资产多元化多角化配置原则，能确保你在某一个产业突遭行业性雪崩时不至于伤筋动骨。"),
            ("die Altersvorsorge", "die", "n.", "-", "有尊严安度晚年自主养老规划", "Eine private Altersvorsorge ist für die junge Generation angesichts des demografischen Wandels unverzichtbar.", "直面老龄化少子化的严峻人口大势，年轻一代尽早启动自主商业养老储备已是不容犹豫的自救。"),
            ("die Rente", "die", "n.", "-n", "国家基本法定每月养老金月钱", "Die gesetzliche Rente wird künftig allein kaum mehr ausreichen, um den gewohnten Lebensstandard zu halten.", "单靠将来领取的国家基本法定养老金，届时将极难奢望能够完全维持住退休前的生活体面。"),
            ("der Minimalismus", "der", "n.", "-", "崇尚断舍离清爽极简主义生活方式", "Minimalismus ist die bewusste Befreiung vom Zwang, immer mehr besitzen zu müssen.", "极简主义的核心内核，在于让人从必须永无止境占有更多身外之物的病态消费主义枷锁中彻底解脱。"),
            ("der Minimalist", "der", "n.", "-en", "清爽生活断舍离极简主义行者", "Als überzeugter Minimalist besitzt er weniger als hundert ausgewählte Gegenstände.", "作为一名矢志不渝的极简主义行者，他随身拥有的全部物什加在一起统共超不过精挑细选的一百件。"),
            ("die Minimalistin", "die", "n.", "-nen", "女性极简主义践行者", "Die Minimalistin mistete ihre Schränke radikal aus und verschenkte alles Überflüssige.", "这位女极简践行者大刀阔斧将塞满家中大柜子的闲置衣物彻底清理一空，悉数打包捐赠给需要的人。"),
            ("ausmisten", "", "v.", "mistet aus, mistete aus, ausgemistet", "彻底大扫除彻底断舍离扔扔扔", "Regelmäßiges Ausmisten befreit nicht nur den Kleiderschrank, sondern vor allem die Seele.", "每隔半年对家中无用杂物来一场彻底的断舍离清空，洗涤净化的不仅是物理衣柜，更是蒙尘的心灵。"),
            ("das Entrümpeln", "das", "n.", "-", "清理破烂堆积杂物扫除扫空", "Das radikale Entrümpeln des Kellers schuf endlich wieder Platz für das Wesentliche.", "把常年阴暗堆积成山的地下室杂物彻底腾空清理一净，终于为真正具有长远价值的核心腾出空间。"),
            ("verzichten", "", "v.", "verzichtet, verzichtete, verzichtet", "主动看淡放下放弃 (auf + Akk)", "Ich verzichte bewusst auf ein eigenes Auto und nutze stattdessen Carsharing und Bahn.", "我主动放弃了购买私家车的执念，平日出行一概潇洒选择随开随停的共享汽车与德铁大动脉。"),
            ("die Genügsamkeit", "die", "n.", "-", "知足常乐克己知止清心寡欲", "Genügsamkeit ist kein bitterer Mangel, sondern die edle Kunst, mit wenigem reich zu sein.", "真正的知足常乐从来都绝非寒酸的匮乏受苦，而是一门只借由极少外物便能富足四海的至高艺术。"),
            ("die Zufriedenheit", "die", "n.", "-", "发自肺腑平静祥和之幸福知足感", "Wahre Zufriedenheit erwächst aus tiefen menschlichen Beziehungen, nicht aus teuren Besitztümern.", "发自骨子里的平静祥和与幸福感，从来都滋养生发自深厚真挚的人性交融羁绊，而非昂贵的奢侈死物。"),
            ("der Wohlstand", "der", "n.", "-", "超越单一金钱物质之内在综合富足", "Echter Wohlstand bemisst sich an freier Zeit, stabiler Gesundheit und innerem Seelenfrieden.", "真正衡量一个生命是否富足的硬核尺度，在于其自主支配的时间、强健的体魄与不为物役的灵魂宁静。"),
            ("die Wertvorstellung", "die", "n.", "-en", "决定人生方向之底层核心价值观", "Ein Wandel der persönlichen Wertvorstellungen führt oft zu einem achtsameren Umgang mit Geld.", "一旦一个人的底层核心价值观发生了从攀比向内观的升华，随之而来的必然是对每一分金钱的敬畏。"),
            ("die Achtsamkeit", "die", "n.", "-", "凝神内省不被世俗裹挟的觉察力", "Achtsamkeit beim Einkaufen bedeutet, sich vor jedem Kauf zu fragen: Brauche ich das wirklich?", "在掏钱结账的千钧一发之际保持一丝正念觉察，就是冷静扣问自己一句：我当真非买这件东西不可吗？"),
            ("die Freiheit", "die", "n.", "-", "摆脱身外物役财务精神大自由", "Finanzielle Unabhängigkeit schenkt die unvergleichliche Freiheit, selbstbestimmt über seine Zeit zu verfügen.", "实现理财自立与精神觉醒的最大奖赏，是赋予了你无与伦比的底气，能够百分之百自主掌舵自己的光阴！"),
            ("das Sparen", "das", "n.", "-", "居安思危细水长流理性储蓄", "Kluges Sparen ist die Brücke zwischen gegenwärtigen Wünschen und zukunftsfähiger Sicherheit.", "富有远见的理性储蓄，是在眼前转瞬即逝的即时快感消费与未来风雨飘摇的安全感之间架起的坚固拱桥。"),
            ("das Auskommen", "das", "n.", "-", "收支相抵自给自足之生活维持", "Mit seinem soliden Einkommen hat der sparsame Haushalt ein gutes und sorgenfreies Auskommen.", "凭借稳定的工薪收入与勤俭持家的优良作风，这个克勤克俭的家庭在任何风浪面前都能从容自如立足。"),
            ("die Unabhängigkeit", "die", "n.", "-", "不仰人鼻息自立自强经济独立", "Ökonomische Unabhängigkeit bewahrt den Menschen vor ungesunden Kompromissen im Leben.", "捍卫并保持自身在经济层面的彻底独立，能让一个人在人生的任何重大十字路口免受屈辱与苟且妥协。"),
            ("die Lebenskunst", "die", "n.", "-", "举重若轻看透浮华之人生生存哲学", "Die hohe Lebenskunst besteht darin, im Alltäglichen das Besondere zu erkennen und dankbar zu sein.", "人世间最最高深的大智慧与生存艺术，莫过于学会在最最平淡如水的寻常烟火中捕捉神圣并永远感恩。")
        ]
    }
]
