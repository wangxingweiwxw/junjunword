import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep98", "countries", "国家", 98, "international")
L.node("country", "country", "/ˈkʌntri/", "国家", plural="countries", pluralIpa="/ˈkʌntriz/")
L.node("value", "value", "/ˈvæljuː/", "价值")
L.node("valuable", "valuable", "/ˈvæljuəbl/", "珍贵的", kind="adj")
L.node("wealth", "wealth", "/welθ/", "财富")
L.node("war", "war", "/wɔːr/", "战争")
L.node("international", "international", "/ˌɪntərˈnæʃnəl/", "国际的", kind="adj")
for id, w, ipa, z in [("america", "America", "/əˈmerɪkə/", "美国；美洲"), ("american", "American", "/əˈmerɪkən/", "美国人"),
                      ("australia", "Australia", "/ɔːˈstreɪliə/", "澳大利亚"), ("australian", "Australian", "/ɔːˈstreɪliən/", "澳大利亚人"),
                      ("africa", "Africa", "/ˈæfrɪkə/", "非洲"), ("african", "African", "/ˈæfrɪkən/", "非洲人")]:
    L.node(id, w, ipa, z)
L.grid(["valuable value wealth",
        "war country international",
        "america american .",
        "australia australian .",
        "africa african ."], dy=330)
for id, x, y in [("valuable", 170, 150), ("value", 520, 150), ("wealth", 870, 150), ("war", 170, 470), ("country", 520, 470), ("international", 870, 470),
                 ("america", 1220, 150), ("american", 1570, 150), ("australia", 1220, 470), ("australian", 1570, 470), ("africa", 1220, 790), ("african", 1570, 790)]:
    L.byid[id]["at"] = [x, y]
L.edge("country", "value"); L.edge("value", "valuable", "+able"); L.edge("country", "wealth"); L.edge("war", "country", dashed=True); L.edge("country", "international")
L.edge("international", "america", dashed=True); L.edge("international", "australia", dashed=True); L.edge("international", "africa", dashed=True)
L.edge("america", "american", "+n"); L.edge("australia", "australian", "+n"); L.edge("africa", "african", "+n")

L.seg("title", zh("小朋友们好！世界上有两百多个国家。今天，我们继续环游世界！"), en("countries"))
L.seg("map show:country focus:country", zh("国家，英语是"), en("country"), zh("很多国家，y 变成 i e s：", "plural:country"), en("countries"))
L.seg("show:value edge:country>value focus:value", zh("东西值多少，是价值："), en("value"))
L.seg("show:valuable edge:value>valuable focus:valuable", zh("很有价值的，是珍贵的。去掉 e，加上 a b l e："), en("valuable"))
L.seg("show:wealth edge:country>wealth focus:wealth", zh("一个国家拥有的金钱和资源，是财富："), en("wealth"))
L.seg("show:war edge:war>country focus:war", zh("国家之间打仗，是战争："), en("war"), zh("我们都希望世界和平，不要战争。"), en("peace"))
L.seg("show:international edge:country>international focus:international", zh("国家和国家之间的，是国际的："), en("international"), en("an international school"))
L.seg("show:america edge:international>america focus:america", zh("美国，英语是"), en("America"))
L.seg("show:american edge:america>american focus:american", zh("美国人，加上 n："), en("American"))
L.seg("show:australia edge:international>australia focus:australia", zh("有袋鼠的澳大利亚："), en("Australia"))
L.seg("show:australian edge:australia>australian focus:australian", zh("澳大利亚人，加上 n："), en("Australian"))
L.seg("show:africa edge:international>africa focus:africa", zh("有大象和狮子的非洲："), en("Africa"))
L.seg("show:african edge:africa>african focus:african", zh("非洲人，也加上 n："), en("African"))
L.seg("focus:american,australian,african", zh("你发现了吗？以 a 结尾的，都是直接加 n："),
      en("America, American", "focus:america,american"), en("Australia, Australian", "focus:australia,australian"), en("Africa, African", "focus:africa,african"))
L.review([("country", "country, countries"), ("value", "value"), ("valuable", "valuable"), ("wealth", "wealth"), ("war", "war"), ("international", "international"),
          ("america", "America"), ("american", "American"), ("australia", "Australia"), ("australian", "Australian"), ("africa", "Africa"), ("african", "African")],
         "太棒了！你最想去哪个国家旅行？用英语说一说吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
