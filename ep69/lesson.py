import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep69", "measures", "测量", 69, "meter")
A = dict(kind="adj")
L.node("weight", "weight", "/weɪt/", "重量", alt="weigh", altLabel="来自")
L.node("kilo", "kilo", "/ˈkiːloʊ/", "千克", alt="kg", altLabel="写作")
L.node("ton", "ton", "/tʌn/", "吨")
L.node("height", "height", "/haɪt/", "高度")
L.node("meter", "meter", "/ˈmiːtər/", "米")
L.node("length", "length", "/leŋθ/", "长度", alt="long", altLabel="来自")
L.node("kilometer", "kilometer", "/kɪˈlɑːmɪtər/", "千米；公里")
L.node("mile", "mile", "/maɪl/", "英里")
L.node("hole", "hole", "/hoʊl/", "洞")
L.node("deep", "deep", "/diːp/", "深的", **A)
L.node("wide", "wide", "/waɪd/", "宽的", **A)
L.node("narrow", "narrow", "/ˈnæroʊ/", "窄的", **A)
L.node("atleast", "at least", "/ət liːst/", "至少")
L.node("almost", "almost", "/ˈɔːlmoʊst/", "几乎", kind="adv")
L.grid(["kilo weight ton",
        "meter height .",
        "kilometer length mile",
        "deep hole narrow",
        "wide atleast almost"], dy=330)
L.edge("weight", "kilo"); L.edge("weight", "ton"); L.edge("height", "meter"); L.edge("length", "kilometer"); L.edge("length", "mile")
L.edge("meter", "kilometer", "×1000"); L.edge("hole", "deep"); L.edge("hole", "narrow"); L.edge("deep", "wide", dashed=True); L.edge("atleast", "almost", dashed=True)

L.seg("title", zh("小朋友们好！东西有多重、多高、多长？今天，我们来学测量！还记得第二十八集的大小和多少吗？"))
L.seg("map show:weight focus:weight", zh("东西有多重，是重量："), en("weight"), zh("它来自第二十八集的称重：", "alt:weight"), en("weigh"))
L.seg("show:kilo edge:weight>kilo focus:kilo", zh("重量的单位，千克："), en("kilo"), zh("常常写作 k g。"), en("I weigh thirty kilos."))
L.seg("show:ton edge:weight>ton focus:ton", zh("特别重的东西，用吨来称。一吨等于一千千克："), en("ton"))
L.seg("show:height focus:height", zh("有多高，是高度："), en("height"), zh("小提示：g h 不发音，e i 读成 ai。"))
L.seg("show:meter edge:height>meter focus:meter", zh("长度和高度的单位，米："), en("meter"), en("one meter"))
L.seg("show:length focus:length", zh("有多长，是长度："), en("length"), zh("它来自", "alt:length"), en("long"))
L.seg("show:kilometer edge:length>kilometer edge:meter>kilometer focus:kilometer", zh("一千米，是一公里。千，加上米："), en("kilo"), en("meter"), en("kilometer"))
L.seg("show:mile edge:length>mile focus:mile", zh("英国和美国常用的长度单位，英里："), en("mile"), zh("一英里，比一公里还长一些。"))
L.seg("show:hole focus:hole", zh("地上挖了一个洞："), en("hole"))
L.seg("show:deep edge:hole>deep focus:deep", zh("洞很深："), en("deep"))
L.seg("show:narrow edge:hole>narrow focus:narrow", zh("洞口很窄："), en("narrow"), zh("还记得第五十二集的 narrowly 吗？加上 l y，就是勉强地。"))
L.seg("show:wide edge:deep>wide focus:wide", zh("窄的反面，是宽的。大河又宽又长："), en("wide"), en("The river is wide."))
L.seg("show:atleast focus:atleast", zh("最少也有，英语是"), en("at least"), en("I am at least one meter tall."))
L.seg("show:almost edge:atleast>almost focus:almost", zh("差一点点就到了，是几乎："), en("almost"), en("It's almost nine o'clock."))
L.seg("focus:wide,narrow", zh("一宽一窄："), en("wide", "focus:wide"), en("narrow", "focus:narrow"))
L.review([("weight", "weight"), ("kilo", "kilo"), ("ton", "ton"), ("height", "height"), ("meter", "meter"), ("length", "length"), ("kilometer", "kilometer"),
          ("mile", "mile"), ("hole", "hole"), ("deep", "deep"), ("narrow", "narrow"), ("wide", "wide"), ("atleast", "at least"), ("almost", "almost")],
         "太棒了！回家量一量你有多高、有多重吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
