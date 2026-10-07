#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enriched Grammar Content for Level A0 (Lessons 1-5):
German Phonetics, Alphabet, Vowels, Diphthongs, Consonants, Stress and Intonation.
"""

A0_GRAMMAR = {
    "A0_L1": {
        "title": "德语特有字符与发音入门 (Alphabet & Sonderzeichen)",
        "sections": [
            {
                "heading": "一、德语字母表 26 个基础字母与 4 个特殊字符",
                "content": "德语使用拉丁字母，包括 26 个与英语相同的字母，以及 4 个独特的德语特有字符：\n"
                           "┌──────┬──────────────┬──────────────┬─────────────────────────┐\n"
                           "│ 字母 │ 发音名称     │ 国际音标     │ 经典示范单词            │\n"
                           "├──────┼──────────────┼──────────────┼─────────────────────────┤\n"
                           "│ Ä ä  │ A-Umlaut     │ [ɛː] / [ɛ]   │ Äpfel [ˈɛpfl̩] (苹果复数)│\n"
                           "│ Ö ö  │ O-Umlaut     │ [øː] / [œ]   │ Öl [øːl] (油), schön    │\n"
                           "│ Ü ü  │ U-Umlaut     │ [yː] / [ʏ]   │ Tür [tyːɐ̯] (门), über   │\n"
                           "│ ß    │ Eszett       │ [s]          │ Straße [ˈʃtʁaːsə] (街道)│\n"
                           "└──────┴──────────────┴──────────────┴─────────────────────────┘\n\n"
                           "【核心口型要领】：\n"
                           "• ä：舌位在发 [e] 处，下颌微开，口型呈扁平状。\n"
                           "• ö：先摆出 [e] 的发音口型，舌位完全不动，将双唇向前收圆突出。\n"
                           "• ü：舌位保持发 [i]（如中文‘衣’），双唇用力向前收聚成小圆孔（类似拼音 ü）。\n"
                           "• ß (Eszett)：永远发清辅音 [s]，绝不发浊音！"
            },
            {
                "heading": "二、大小写书写铁律 (Groß- und Kleinschreibung)",
                "content": "德语是全球极少数保留名词首字母大写规则的现代语言。必须牢记以下三大铁律：\n\n"
                           "1. 【所有名词首字母必须大写】：\n"
                           "   无论是具体物品、抽象概念、人名、国名还是专有名词，只要是名词，首字母一律大写！\n"
                           "   • 正确：das Buch (书), die Freiheit (自由), der Tisch (桌子)\n"
                           "   • 错误：buch, freiheit, tisch\n\n"
                           "2. 【句首首字母必须大写】：\n"
                           "   每个完整句子的第一个单词的首字母必须大写。\n\n"
                           "3. 【尊称代词必须大写】：\n"
                           "   尊称‘您 / 您们’(Sie) 以及其对应的物主代词 (Ihr / Ihre / Ihrem / Ihren) 和第三格 (Ihnen)，在任何句子位置【首字母必须大写】以示礼貌！\n"
                           "   • Wie heißen Sie? (您叫什么名字？)\n"
                           "   • Ist das Ihr Buch? (这是您的书吗？)"
            },
            {
                "heading": "三、ß 与 ss 的拼写分界与易错辨析",
                "content": "德语正字法改革后，ß 与 ss 的使用有了严格科学的界限，不可混用：\n\n"
                           "• 【规则一】：在【长元音】或【双元音】之后，拼写作 ß！\n"
                           "  例：die Straße (元音 a 发长音), heißen (ei 是双元音), groß (o 发长音), der Fuß (u 发长音)\n\n"
                           "• 【规则二】：在【短元音】之后，拼写作 ss！\n"
                           "  例：küssen (ü 发短音), dass (a 发短音), das Schloss (o 发短音), der Fluss (u 发短音)\n\n"
                           "• 【瑞士德语特别说明】：瑞士德语区已全面废除 ß，一律使用 ss（如 Strasse, heissen）。但在德国和奥地利，此规则必须严格遵守！"
            },
            {
                "heading": "四、高频生活拼读范例与发音对照",
                "content": "练习以下核心例词，感受德语发音的清脆与严谨：\n\n"
                           "1. das Alphabet [alfaˈbeːt]：重音在最后一个音节，ph 发 [f]。\n"
                           "2. buchstabieren [buːxʃtaˈbiːʁən]：ch 在 u 之后发深喉音 [x]，sp 在词中发 [ʃt]。\n"
                           "3. die Aussprache [ˈaʊsˌʃpʁaːxə]：复合前缀 aus- 与主词 sprechen 的元音变异。\n"
                           "4. Guten Tag! [ˌɡuːtn̩ ˈtaːk]：词尾 g 清化发 [k]，Tag 元音 a 读长音。"
            },
            {
                "heading": "五、零基础发音速记口诀与避坑秘籍",
                "content": "【发音速记口诀】：\n"
                           "德语拼读真规整，见词能读心不慌；\n"
                           "所有名词首大写，尊称 Sie 字大写扬；\n"
                           "长音双元后接 ß，短音之后双 s 跟；\n"
                           "口型紧张不滑动，纯正德味脱口出！"
            }
        ]
    },
    "A0_L2": {
        "title": "元音长短音判定铁律 (Vokale: lang und kurz)",
        "sections": [
            {
                "heading": "一、读长元音的三大黄金定律",
                "content": "在德语中，元音是发长音还是短音，具有区别词义的决定性作用！判定长元音有三大铁律：\n\n"
                           "1. 【元音字母重叠】：两个相同元音字母重叠时，必读长音！\n"
                           "   • Tee [teː] (茶), Boot [boːt] (小船), das Paar [paːɐ̯] (一双/一对), das Meer [meːɐ̯] (海洋)\n\n"
                           "2. 【元音后紧跟不发音的延音符 h (Dehnungs-h)】：元音必读长音！\n"
                           "   • der Zahn [tsaːn] (牙齿), die Bahn [baːn] (铁路), wohnen [ˈvoːnən] (居住), die Kuh [kuː] (奶牛)\n\n"
                           "3. 【开音节与相对开音节】：以元音结尾的开音节，或元音后只有一个辅音字母：\n"
                           "   • da [daː] (那里), so [zoː] (这样), der Name [ˈnaːmə] (名字), der Mut [muːt] (勇气)"
            },
            {
                "heading": "二、读短元音的核心特征与双辅音规则",
                "content": "判定短元音的黄金法则简单直接：\n\n"
                           "1. 【双辅音字母前】：元音字母后紧跟两个相同辅音字母时，前面的元音【必须读短音】！\n"
                           "   • das Bett [bɛt] (床), der Kamm [kam] (梳子), hoffen [ˈhɔfn̩] (希望), die Puppe [ˈpʊpə] (洋娃娃)\n\n"
                           "2. 【闭音节与多辅音前】：元音后跟两个或多个不同辅音字母时，通常读短音：\n"
                           "   • das Kind [kɪnt] (孩子), der Tisch [tɪʃ] (桌子), oft [ɔft] (经常), die Lampe [ˈlampə] (台灯)"
            },
            {
                "heading": "三、核心长短音成对词汇对照表 (极易混淆！)",
                "content": "长短音读错会彻底改变单词含义，请对照体会：\n\n"
                           "┌────────────┬─────────────┬────────────┬─────────────┐\n"
                           "│ 长元音单词 │ 词义与音标  │ 短元音单词 │ 词义与音标  │\n"
                           "├────────────┼─────────────┼────────────┼─────────────┤\n"
                           "│ die Bahn   │ 铁路 [baːn] │ der Bann   │ 驱逐 [ban]  │\n"
                           "│ das Beet   │ 花坛 [beːt] │ das Bett   │ 床 [bɛt]    │\n"
                           "│ die Höhle  │ 洞穴 [ˈhøːlə]│ die Hölle  │ 地狱 [ˈhœlə]│\n"
                           "│ fühlen     │ 感觉 [ˈfyːlən]│ füllen    │ 装满 [ˈfʏlən]│\n"
                           "│ der Staat  │ 国家 [ʃtaːt]│ die Stadt  │ 城市 [ʃtat] │\n"
                           "└────────────┴─────────────┴────────────┴─────────────┘"
            },
            {
                "heading": "四、弱读元音 e 的发音位置与词尾弱读规律 (Schwa-Laut)",
                "content": "• 在德语非重读音节及词尾中，字母 e 往往弱化发为央元音 [ə]（倒 e，类似汉语拼音中轻读的 'e'）。\n"
                           "  例：bitte [ˈbɪtə], Name [ˈnaːmə], haben [ˈhaːbn̩]\n\n"
                           "• 【词尾 -er 的特殊弱化】：在非重读词尾，-er 通常弱化为舌根半元音 [ɐ]：\n"
                           "  例：der Vater [ˈfaːtɐ], das Wasser [ˈvasɐ], der Lehrer [ˈleːʁɐ]\n"
                           "  注意切勿将 -er 发成卷舌音 r！德语标准音中词尾 -er 口型微开，自然放松读 [ɐ]。"
            },
            {
                "heading": "五、歌德考试听力辨音秘籍与速记口诀",
                "content": "【长短音辨析速记诀】：\n"
                           "重叠元音与延音 h，稳扎稳打拖长调；\n"
                           "双辅多辅紧跟后，短促有力急收刀；\n"
                           "长音唇紧口形定，短音松弛音速飙；\n"
                           "Staat 与 Stadt 分得清，歌德听力得高招！"
            }
        ]
    },
    "A0_L3": {
        "title": "四大双元音与复合元音拼读要领 (Diphthonge: ei, eu, au, äu)",
        "sections": [
            {
                "heading": "一、德语四大复合双元音及发音要领",
                "content": "德语中有四组高频双元音组合。双元音由前一个元音滑向后一个元音，前重后轻，浑然一体：\n\n"
                           "1. 【ei / ai】发 [aɪ]：\n"
                           "   口型由开元音 [a] 迅速滑向闭元音 [ɪ]，类似英语中的 'eye' 或汉语拼音 'ai'。\n"
                           "   • mein [maɪn] (我的), klein [klaɪn] (小的), der Mai [maɪ] (五月)\n\n"
                           "2. 【au】发 [aʊ]：\n"
                           "   口型由 [a] 滑向收圆的 [ʊ]，类似英语中的 'how' 或汉语拼音 'ao'。\n"
                           "   • das Haus [haʊs] (房屋), die Frau [fʁaʊ] (女士), das Auto [ˈaʊtoː] (汽车)\n\n"
                           "3. 【eu / äu】发 [ɔʏ]：\n"
                           "   口型由半开圆唇的 [ɔ] 滑向闭唇的 [ʏ]，两者完全同音！\n"
                           "   • neu [nɔʏ] (新的), heute [ˈhɔʏtə] (今天), die Bäume [ˈbɔʏmə] (树木复数), die Häuser [ˈhɔʏzɐ] (房屋复数)\n\n"
                           "4. 【ie】发长元音 [iː]：\n"
                           "   【重中之重】：ie 不是双元音，而是长元音组合！i 后面加 e 表示 i 读长音！\n"
                           "   • die Liebe [ˈliːbə] (爱), sieben [ˈziːbn̩] (七), wie [viː] (怎样)"
            },
            {
                "heading": "二、ie [iː] 与 ei [aɪ] 致命混淆深度剖析",
                "content": "中国德语学习者最容易读反的两个字母组合就是 ie 和 ei！请看对立词对比：\n\n"
                           "┌────────────┬─────────────┬────────────┬─────────────┐\n"
                           "│ 字母组合 ie│ 音标与释义  │ 字母组合 ei│ 音标与释义  │\n"
                           "├────────────┼─────────────┼────────────┼─────────────┤\n"
                           "│ das Lied   │ 歌曲 [liːt] │ das Leid   │ 痛苦 [laɪt] │\n"
                           "│ die Miete  │ 租金 [ˈmiːtə]│ die Meite  │ 麦堆 [ˈmaɪtə]│\n"
                           "│ schießen   │ 射击 [ˈʃiːsn̩]│ scheißen   │ 拉屎 [ˈʃaɪsn̩]│\n"
                           "│ Wien       │ 维也纳 [viːn]│ Wein       │ 葡萄酒 [vaɪn]│\n"
                           "└────────────┴─────────────┴────────────┴─────────────┘\n\n"
                           "【防混判定法则】：看第二个字母！\n"
                           "• 后一个是 e (ie) -> 发前一个字母 i 的长音 [iː]！\n"
                           "• 后一个是 i (ei) -> 从 e 往 i 滑动，发 [aɪ]！"
            },
            {
                "heading": "三、eu 与 äu 的变音来源与拼写逻辑",
                "content": "为什么德语中有两套拼写完全相同发音 [ɔʏ] 的符号？\n"
                           "这源自德语词源学中的【元音变音机制 (Umlaut)】：\n\n"
                           "• 词根含有 au 的名词变复数时，au 规则变音为 äu，保持词根亲缘关系：\n"
                           "  - der Baum (树) [baʊm] -> die Bäume (树木复数) [ˈbɔʏmə]\n"
                           "  - das Haus (房子) [haʊs] -> die Häuser (房屋复数) [ˈhɔʏzɐ]\n"
                           "  - die Maus (老鼠) [maʊs] -> die Mäuse (老鼠复数) [ˈmɔʏzə]\n\n"
                           "• 独立词根通常拼写作 eu：\n"
                           "  - Europa [ɔʏˈʁoːpa], der Euro [ˈɔʏʁo], freuen [ˈfʁɔʏən]"
            },
            {
                "heading": "四、双元音在整句中的连贯拼读技巧",
                "content": "在句子连读中，双元音必须保持前音强、后音轻的节奏感，切勿拖泥带水：\n\n"
                           "1. Mein Haus ist neu und klein. [maɪn haʊs ɪst nɔʏ ʊnt klaɪn]\n"
                           "   (我的房子又新又小。——一句话包含全部四大复合元音！)\n"
                           "2. Heute kaufen wir ein weißes Auto.\n"
                           "   (今天我们买一辆白色的汽车。)"
            },
            {
                "heading": "五、双元音极速记忆口诀",
                "content": "【双元音速记顺口溜】：\n"
                           "ei 念 [aɪ] 如爱，au 念 [aʊ] 像嗷；\n"
                           "eu 和 äu 亲兄弟，圆唇滑出 [ɔʏ] 乐陶陶；\n"
                           "见 ie 莫当双元读，拉长纯纯长音 [iː]！"
            }
        ]
    },
    "A0_L4": {
        "title": "特殊辅音组合与软硬音规则 (Konsonanten: ch, sp, st, sch, ig)",
        "sections": [
            {
                "heading": "一、ch 的两大标准发音：ich-Laut [ç] vs ach-Laut [x]",
                "content": "ch 是德语最具代表性的辅音组合，其发音由其【前置元音】严格决定：\n\n"
                           "1. 【ach-Laut [x]（舌根小舌擦音）】：\n"
                           "   当 ch 前面是 a, o, u 或 au 时，发深喉摩擦音 [x]（类似咳痰清理嗓子的位置）：\n"
                           "   • das Buch [buːx] (书), machen [ˈmaxn̩] (做), die Woche [ˈvɔxə] (星期), auch [aʊx] (也)\n\n"
                           "2. 【ich-Laut [ç]（硬腭擦音）】：\n"
                           "   当 ch 前面是 e, i, ä, ö, ü, ei, eu, äu，或在辅音 l, n, r 之后，发软腭摩擦音 [ç]（类似微笑着哈气）：\n"
                           "   • ich [ɪç] (我), sprechen [ˈʃpʁɛçn̩] (说), die Küche [ˈkʏçə] (厨房), welche [ˈvɛlçə] (哪个)"
            },
            {
                "heading": "二、词首 sp- / st- 与 sch- 的读音铁律",
                "content": "1. 【词首及音节开头的 sp / st】：\n"
                           "   在单词或词根开头时，s 必须发成清辅音 [ʃ]（同 sch），即分别读作 [ʃp] 和 [ʃt]：\n"
                           "   • sprechen [ˈʃpʁɛçn̩] (说), der Sport [ʃpɔʁt] (体育), spät [ʃpɛːt] (迟)\n"
                           "   • die Straße [ˈʃtʁaːsə] (街道), die Stadt [ʃtat] (城市), stehen [ˈʃteːən] (站立)\n\n"
                           "2. 【在词中或词尾的 sp / st】：\n"
                           "   不在词根开头时，回归正常清辅音 [sp] 和 [st]：\n"
                           "   • das Fenster [ˈfɛnstɐ] (窗户), der Herbst [hɛʁpst] (秋天), der Gast [ɡast] (客人)\n\n"
                           "3. 【字母组合 sch】：\n"
                           "   永远发清辅音 [ʃ]（双唇向前撅起呈圆筒状）：\n"
                           "   • schön [ʃøːn] (美丽的), die Schule [ˈʃuːlə] (学校), schreiben [ˈʃʁaɪbn̩] (写)"
            },
            {
                "heading": "三、词尾 -ig 的标准发音规则与方言辨析",
                "content": "• 在德语标准高地德语 (Hochdeutsch) 中，词尾的 -ig 必须读作 [ɪç]（同 ich 音）！\n"
                           "  例：richtig [ˈʁɪçtɪç] (正确的), wichtig [ˈvɪçtɪç] (重要的), fleißig [ˈflaɪsɪç] (勤奋的)\n\n"
                           "• 【注意例外】：当 -ig 后面紧跟以元音开头的后缀时，g 恢复发浊音 [ɡ]：\n"
                           "  例：die Wichtigkeit [ˈvɪçtɪçkaɪt] 保持 [ç]；但是 wichtiger [ˈvɪçtɪɡɐ] 读 [ɡ]！\n\n"
                           "• 【特别提示】：在德国南部及奥地利口音中常读成 [ɪk]，但在歌德证书考试中，[ɪç] 是官方标准评分准则！"
            },
            {
                "heading": "四、德语辅音清化律 (Auslautverhärtung) 铁律",
                "content": "德语发音最具金属质感的铁律——末尾辅音清化：\n"
                           "当浊辅音字母 b, d, g, v 位于【单词末尾】或【音节末尾】时，必须完全清化，读作对应的清辅音！\n\n"
                           "• b -> [p]：das Grab [ɡʁaːp] (坟墓), ab [ap] (从...起)\n"
                           "• d -> [t]：das Bad [baːt] (浴室), und [ʊnt] (和), das Bild [bɪlt] (图片)\n"
                           "• g -> [k]：der Tag [taːk] (日子), der Zug [tsuːk] (火车), der Krieg [kʁiːk] (战争)\n"
                           "• v -> [f]：der Vater [ˈfaːtɐ] (父亲), vier [fiːɐ̯] (四)；外来词仍读 [v]（die Vase）"
            },
            {
                "heading": "五、辅音拼读防坑速查口诀",
                "content": "【辅音组合口诀】：\n"
                           "a, o, u, au 遇 ch，深喉咳嗽咳出声 [x]；\n"
                           "其余元音跟其后，咧嘴微笑哈清风 [ç]；\n"
                           "词首 sp, st 不含糊，撅嘴读成 [ʃp] 和 [ʃt]；\n"
                           "词尾 b, d, g 清化走，[p], [t], [k] 清脆干练收！"
            }
        ]
    },
    "A0_L5": {
        "title": "德语重音、词尾弱化与综合拼读实战 (Betonung & Intonation)",
        "sections": [
            {
                "heading": "一、德语词重音判定规律 (Wortakzent)",
                "content": "德语单词重音具有极高的规律性，通常遵循以下判定法则：\n\n"
                           "1. 【原生单根词】：重音通常落在【第一个音节（词根音节）】上！\n"
                           "   • Vater [ˈfaːtɐ], Mutter [ˈmʊtɐ], leben [ˈleːbn̩], lernen [ˈlɛʁnən]\n\n"
                           "2. 【复合词】：重音通常落在【前一个词（修饰词）】的首音节上！\n"
                           "   • das Wörterbuch [ˈvœʁtɐˌbuːx] (Wörter + Buch)\n"
                           "   • das Arbeitszimmer [ˈaʁbaɪtsˌtsɪmɐ] (Arbeit + Zimmer)\n\n"
                           "3. 【外来语词汇】：重音往往落在最后一个音节上：\n"
                           "   • das Telefon [teleˈfoːn], die Musik [muˈziːk], die Universität [univɛʁziˈtɛːt]"
            },
            {
                "heading": "二、前缀重音铁律：可分前缀重读 vs 不可分前缀不重读",
                "content": "这是德语动词体系最核心的发音分水岭：\n\n"
                           "1. 【不可分前缀 8 大金刚】：be-, ge-, er-, ver-, zer-, ent-, emp-, miss-\n"
                           "   【铁律】：这 8 个前缀【永远不重读】！重音必须落在后面的词根音节上！\n"
                           "   • verstehen [fɛɐ̯ˈʃteːən] (理解), beginnen [bəˈɡɪnən] (开始), erzählen [ɛɐ̯ˈtsɛːlən] (讲述)\n\n"
                           "2. 【可分前缀】：auf-, an-, aus-, ein-, mit-, vor-, zu-, ab-\n"
                           "   【铁律】：可分前缀在动词原形中【必须重读】！\n"
                           "   • aufstehen [ˈaʊfˌʃteːən] (起床), anrufen [ˈanˌʁuːfn̩] (打电话), mitkommen [ˈmɪtˌkɔmən] (同来)"
            },
            {
                "heading": "三、句子语调的三大基本模式 (Satzmelodie)",
                "content": "德语语调直接传递句子的语法属性与说话人的交际态度：\n\n"
                           "1. 【降调 ↘ (Fallende Melodie)】：\n"
                           "   • 用于【陈述句】：Ich komme aus Deutschland. ↘\n"
                           "   • 用于【特殊疑问句 (W-Frage)】：Woher kommen Sie? ↘ / Wie heißen Sie? ↘\n"
                           "   • 用于【祈使句】：Kommen Sie bitte herein! ↘\n\n"
                           "2. 【升调 ↗ (Steigende Melodie)】：\n"
                           "   • 用于【是非疑问句 (Ja/Nein-Frage)】：Kommen Sie aus China? ↗ / Trinken Sie Kaffee? ↗\n"
                           "   • 用于表示惊讶、追问或未完结意群。\n\n"
                           "3. 【平调 →】：用于句子前半部分的前置从句，表示后文还有主要信息。"
            },
            {
                "heading": "四、德语喉塞音 (Knacklaut / Glottisschlag) 发音精粹",
                "content": "• 为什么德国人说话听起来铿锵有力、节奏分明？秘密就在于【喉塞音 (Glottisschlag [ʔ])】！\n"
                           "• 当一个单词或词根以【元音开头】时，发音前声带必须紧闭，然后气流冲开声带爆破发声。\n"
                           "  例：ein Apfel -> 读作 [ʔaɪn ˈʔapfl̩]，绝不连读成 'ei-napfel'！\n"
                           "  Verreisen -> ver- + reisen；而 ver- + reisen (辅音开头) 无喉塞音；\n"
                           "  Verantwortung -> ver- + [ʔ]antwortung，中间有极短暂的声带闭锁。\n"
                           "• 掌握喉塞音，就能彻底告别英语腔，读出地道正宗的现代德语！"
            },
            {
                "heading": "五、综合拼读通关速记口诀",
                "content": "【语调与重音总诀】：\n"
                           "词根首音多重读，前部修饰压后头；\n"
                           "可分前缀抢风头，不可分前缀不抬头；\n"
                           "陈述特问往下沉，是非反问向上扬；\n"
                           "字字如珠喉塞音，标准德语响当当！"
            }
        ]
    }
}
