import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep74", "describing animals", "形容动物", 74, "famous")
A = dict(kind="adj")
L.node("animals", "animals", "/ˈænɪmlz/", "动物", icon="animal")
L.node("panda", "panda", "/ˈpændə/", "熊猫")
L.node("famous", "famous", "/ˈfeɪməs/", "著名的", **A)
L.node("special", "special", "/ˈspeʃl/", "特别的", **A)
L.node("treasure", "treasure", "/ˈtreʒər/", "宝藏；珍宝")
L.node("monkey", "monkey", "/ˈmʌŋki/", "猴子")
L.node("creative", "creative", "/kriˈeɪtɪv/", "有创造力的", **A)
L.node("wolf", "wolf", "/wʊlf/", "狼")
L.node("patient", "patient", "/ˈpeɪʃnt/", "有耐心的", **A)
L.node("impatient", "impatient", "/ɪmˈpeɪʃnt/", "没耐心的", **A)
L.node("pig", "pig", "/pɪɡ/", "猪")
L.node("ugly", "ugly", "/ˈʌɡli/", "丑的", **A)
L.node("bird", "bird", "/bɜːrd/", "鸟")
L.node("pretty", "pretty", "/ˈprɪti/", "漂亮的", **A)
L.node("beautiful", "beautiful", "/ˈbjuːtɪfl/", "美丽的", **A, alt="beauty", altLabel="来自")
L.node("owl", "owl", "/aʊl/", "猫头鹰")
L.node("silent", "silent", "/ˈsaɪlənt/", "安静的", **A)
L.node("wise", "wise", "/waɪz/", "聪明的；有智慧的", **A)
L.grid(["panda animals monkey",
        "famous special creative",
        "treasure wolf patient",
        "pig ugly impatient",
        "bird pretty beautiful",
        "owl silent wise"], dy=310)
L.edge("animals", "panda"); L.edge("animals", "monkey"); L.edge("panda", "famous"); L.edge("panda", "special"); L.edge("monkey", "creative")
L.edge("panda", "treasure", dashed=True); L.edge("wolf", "patient"); L.edge("patient", "impatient", "im+"); L.edge("pig", "ugly", dashed=True)
L.edge("bird", "pretty"); L.edge("pretty", "beautiful", "更美"); L.edge("owl", "silent"); L.edge("silent", "wise", dashed=True)

L.seg("title", zh("小朋友们好！还记得第五十四集的形容词吗？今天，我们再学一些形容动物的词。"))
L.seg("map show:animals focus:animals", zh("动物们："), en("animals"))
L.seg("show:panda edge:animals>panda focus:panda", zh("中国的熊猫："), en("panda"))
L.seg("show:famous edge:panda>famous focus:famous", zh("熊猫全世界都很有名。著名的，英语是"), en("famous"))
L.seg("show:special edge:panda>special focus:special", zh("它是很特别的动物："), en("special"), en("Pandas are famous because they are special.", "focus:panda,famous,special"))
L.seg("show:treasure edge:panda>treasure focus:treasure", zh("熊猫是我们国家的宝贝。宝藏、珍宝，英语是"), en("treasure"))
L.seg("show:monkey edge:animals>monkey focus:monkey", zh("聪明的猴子："), en("monkey"))
L.seg("show:creative edge:monkey>creative focus:creative", zh("猴子会想出新办法，很有创造力："), en("creative"))
L.seg("show:wolf focus:wolf", zh("狼："), en("wolf"))
L.seg("show:patient edge:wolf>patient focus:patient", zh("狼静静地等猎物，很有耐心："), en("patient"))
L.seg("show:impatient edge:patient>impatient focus:impatient", zh("前面加上 i m，就是没耐心："), en("impatient"), zh("就像 un 一样，im 也让意思反过来。"))
L.seg("show:pig focus:pig", zh("胖乎乎的猪："), en("pig"))
L.seg("show:ugly edge:pig>ugly focus:ugly", zh("有人说猪很丑，英语是"), en("ugly"), zh("其实每种动物都有自己的美哦。"))
L.seg("show:bird focus:bird", zh("小鸟："), en("bird"))
L.seg("show:pretty edge:bird>pretty focus:pretty", zh("羽毛五颜六色，真漂亮："), en("pretty"))
L.seg("show:beautiful edge:pretty>beautiful focus:beautiful", zh("比漂亮更美，是美丽的。美，加上 f u l："), en("beauty"), en("beautiful"))
L.seg("show:owl focus:owl", zh("夜里的猫头鹰："), en("owl"))
L.seg("show:silent edge:owl>silent focus:silent", zh("它飞起来静悄悄的："), en("silent"))
L.seg("show:wise edge:silent>wise focus:wise", zh("人们常说猫头鹰很有智慧："), en("wise"), en("Owls are wise and beautiful."))
L.seg("focus:patient,impatient", zh("有耐心和没耐心："), en("patient", "focus:patient"), en("impatient", "focus:impatient"))
L.review([("animals", "animals"), ("panda", "panda"), ("famous", "famous"), ("special", "special"), ("treasure", "treasure"), ("monkey", "monkey"),
          ("creative", "creative"), ("wolf", "wolf"), ("patient", "patient"), ("impatient", "impatient"), ("pig", "pig"), ("ugly", "ugly"),
          ("bird", "bird"), ("pretty", "pretty"), ("beautiful", "beautiful"), ("owl", "owl"), ("silent", "silent"), ("wise", "wise")],
         "太棒了！用英语说一说你最喜欢的动物有什么特点吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
