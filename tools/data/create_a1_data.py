#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates tools/data/vocab_a1_data.py containing Lessons 2 to 15 (14 lessons x 70 words = 980 words).
Combined with Lesson 1 (70 words), Level A1 has exactly 1050 words.
"""

import os

def generate():
    content = '''# -*- coding: utf-8 -*-
# Lessons 2 to 15 for Level A1, each having exactly 70 words.

def get_a1_remaining_lessons():
    return [
'''
    # We will append the specifications for Lessons 2 to 15
    # Let's define the lessons programmatically
    lessons = []

    # Lesson 2: Familie & Verwandtschaft (70 words)
    l02_words = [
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

    return l02_words

if __name__ == "__main__":
    generate()
