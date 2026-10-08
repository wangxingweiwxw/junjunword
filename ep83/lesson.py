import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep83", "education", "教育", 83, "university")
V, A = dict(kind="verb"), dict(kind="adj")
L.node("education", "education", "/ˌedʒuˈkeɪʃn/", "教育", alt="educate", altLabel="来自")
L.node("college", "college", "/ˈkɑːlɪdʒ/", "学院")
L.node("university", "university", "/ˌjuːnɪˈvɜːrsəti/", "大学")
L.node("graduate", "graduate", "/ˈɡrædʒueɪt/", "毕业", **V)
L.node("graduation", "graduation", "/ˌɡrædʒuˈeɪʃn/", "毕业典礼")
L.node("speaker", "speaker", "/ˈspiːkər/", "演讲者", alt="speak", altLabel="来自")
L.node("congratulate", "congratulate", "/kənˈɡrætʃuleɪt/", "祝贺", **V)
L.node("knowledge", "knowledge", "/ˈnɑːlɪdʒ/", "知识", alt="know", altLabel="来自")
L.node("offer", "offer", "/ˈɔːfər/", "提供；给予", **V)
L.node("provide", "provide", "/prəˈvaɪd/", "提供", **V)
L.node("private", "private", "/ˈpraɪvət/", "私立的", **A)
L.node("public", "public", "/ˈpʌblɪk/", "公立的", **A)
L.node("text", "text", "/tekst/", "课文")
L.node("passage", "passage", "/ˈpæsɪdʒ/", "文章")
L.node("paragraph", "paragraph", "/ˈpærəɡræf/", "段落")
L.grid(["college education university",
        "private knowledge public",
        "graduate graduation speaker",
        "offer provide congratulate",
        "text passage paragraph"], dy=330)
L.edge("education", "college"); L.edge("education", "university"); L.edge("college", "private", dashed=True); L.edge("university", "public", dashed=True)
L.edge("graduate", "graduation", "+ion"); L.edge("graduation", "speaker"); L.edge("speaker", "congratulate", dashed=True); L.edge("offer", "provide", "差不多")
L.edge("text", "passage"); L.edge("passage", "paragraph")

L.seg("title", zh("小朋友们好！小学、中学，然后是大学。今天，我们来学和教育有关的单词。"), en("education"))
L.seg("map show:education focus:education", zh("还记得第四十二集的教育 educate 吗？加上 i o n，就是教育这件事："), en("educate"), en("education"))
L.seg("show:college edge:education>college focus:college", zh("学院，英语是"), en("college"))
L.seg("show:university edge:education>university focus:university", zh("综合性的大学，是"), en("university"))
L.seg("show:private edge:college>private focus:private", zh("私人办的，是私立的："), en("private"))
L.seg("show:public edge:university>public focus:public", zh("国家办的、大家的，是公立的、公共的："), en("public"), en("a public university"))
L.seg("show:knowledge focus:knowledge", zh("在学校里，我们学到知识。还记得 know 吗？"), en("know"), en("knowledge"), zh("k 不发音，o w 读短短的。"))
L.seg("show:offer focus:offer", zh("学校为我们提供好的老师："), en("offer"))
L.seg("show:provide edge:offer>provide focus:provide", zh("提供，还可以说"), en("provide"), en("The school provides lunch."))
L.seg("show:text focus:text", zh("课本里的课文："), en("text"), zh("还记得第六十三集的课本 textbook 吗？"))
L.seg("show:passage edge:text>passage focus:passage", zh("一篇文章："), en("passage"))
L.seg("show:paragraph edge:passage>paragraph focus:paragraph", zh("文章里的一个段落："), en("paragraph"))
L.seg("show:graduate focus:graduate", zh("读完大学，就毕业了："), en("graduate"), en("I will graduate from a public university.", "focus:graduate,public,university"))
L.seg("show:graduation edge:graduate>graduation focus:graduation", zh("毕业那天，有毕业典礼："), en("graduation"))
L.seg("show:speaker edge:graduation>speaker focus:speaker", zh("台上讲话的人，是演讲者："), en("speak"), en("speaker"))
L.seg("show:congratulate edge:speaker>congratulate focus:congratulate", zh("大家互相祝贺："), en("congratulate"), en("Congratulations!"))
L.review([("education", "education"), ("college", "college"), ("university", "university"), ("private", "private"), ("public", "public"), ("knowledge", "knowledge"),
          ("offer", "offer"), ("provide", "provide"), ("text", "text"), ("passage", "passage"), ("paragraph", "paragraph"), ("graduate", "graduate"),
          ("graduation", "graduation"), ("speaker", "speaker"), ("congratulate", "congratulate")],
         "太棒了！你长大想上哪所大学？用英语说一说吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
