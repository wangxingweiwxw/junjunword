import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep34", "family tree", "家族", 34, "relationship")
L.node("ancestor", "ancestor", "/ˈænsestər/", "祖先")
L.node("parents", "parents", "/ˈperənts/", "父母")
L.node("brother", "brother", "/ˈbrʌðər/", "兄弟")
L.node("sister", "sister", "/ˈsɪstər/", "姐妹")
L.node("twins", "twins", "/twɪnz/", "双胞胎")
L.node("husband", "husband", "/ˈhʌzbənd/", "丈夫")
L.node("wife", "wife", "/waɪf/", "妻子", plural="wives", pluralIpa="/waɪvz/")
L.node("couple", "couple", "/ˈkʌpl/", "夫妻；一对")
L.node("blood", "blood", "/blʌd/", "血；血缘")
L.node("relation", "relation", "/rɪˈleɪʃn/", "关系；亲属")
L.node("relationship", "relationship", "/rɪˈleɪʃnʃɪp/", "关系")
L.node("although", "although", "/ɔːlˈðoʊ/", "虽然", kind="adv")
L.grid(["husband couple wife",
        "ancestor parents .",
        "brother twins sister",
        "blood relation relationship",
        ". although ."], dy=330)
L.edge("husband", "couple"); L.edge("wife", "couple"); L.edge("couple", "parents", "有了孩子"); L.edge("ancestor", "parents", "很久以前")
L.edge("parents", "brother"); L.edge("parents", "sister"); L.edge("brother", "twins", dashed=True); L.edge("sister", "twins", dashed=True)
L.edge("blood", "relation"); L.edge("relation", "relationship", "+ship")

L.seg("title", zh("小朋友们好！我们的家，就像一棵大树。今天，我们来画一画家族树。"), en("family tree"))
L.seg("map show:husband focus:husband", zh("一个男人结婚了，他就是丈夫："), en("husband"))
L.seg("show:wife focus:wife", zh("和他结婚的女人，是妻子："), en("wife"))
L.seg("show:couple edge:husband>couple edge:wife>couple focus:couple", zh("丈夫和妻子在一起，是一对夫妻："), en("couple"),
      zh("这个词也可以表示一对："), en("a couple of apples"))
L.seg("show:parents edge:couple>parents focus:parents", zh("他们有了孩子，就成了孩子的父母。还记得第二集吗？"), en("parents"))
L.seg("show:ancestor edge:ancestor>parents focus:ancestor", zh("爸爸的爸爸的爸爸……很久很久以前的老祖宗，是祖先："), en("ancestor"))
L.seg("show:brother edge:parents>brother focus:brother", zh("同一对父母的男孩子，是兄弟："), en("brother"), en("my big brother"))
L.seg("show:sister edge:parents>sister focus:sister", zh("女孩子，是姐妹："), en("sister"), en("my little sister"))
L.seg("show:twins edge:brother>twins edge:sister>twins focus:twins", zh("同一天出生、长得几乎一样的两个孩子，是双胞胎："), en("twins"),
      zh("还记得第三十一集吗？"), en("They look the same!"))
L.seg("show:blood focus:blood", zh("家人之间，流着一样的血，这叫血缘："), en("blood"), zh("中间的两个 o，读短短的 a。"))
L.seg("show:relation edge:blood>relation focus:relation", zh("家人之间的联系，叫"), en("relation"))
L.seg("show:relationship edge:relation>relationship focus:relationship", zh("在后面加上 s h i p，就是关系："), en("relationship"),
      en("a good relationship"))
L.seg("show:although focus:although", zh("最后学一个小词：虽然。"), en("although"),
      en("Although we are not twins, we look the same."))
L.seg("focus:wife", zh("一个妻子是"), en("wife"), zh("很多个，要把 f 变成 v e s：", "plural:wife"), en("wives"))
L.seg("focus:none", zh("我们来介绍一下家族树吧！"))
L.seg("", en("My father and mother are a couple.", "focus:couple"), en("I have a brother and a sister.", "focus:brother,sister"),
      en("We are a happy family!", "focus:relationship"))
L.review([("husband", "husband"), ("wife", "wife, wives"), ("couple", "couple"), ("parents", "parents"), ("ancestor", "ancestor"),
          ("brother", "brother"), ("sister", "sister"), ("twins", "twins"), ("blood", "blood"), ("relation", "relation"),
          ("relationship", "relationship"), ("although", "although")],
         "太棒了！试着画一棵你自己的家族树，用英语标上每个人吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
