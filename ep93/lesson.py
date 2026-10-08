import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep93", "safety", "安全", 93, "safety")
A = dict(kind="adj")
L.node("safety", "safety", "/ˈseɪfti/", "安全", alt="safe", altLabel="来自")
L.node("careful", "careful", "/ˈkerfl/", "小心的", **A)
L.node("careless", "careless", "/ˈkerləs/", "粗心的", **A)
L.node("drop", "drop", "/drɑːp/", "掉落", kind="verb")
L.node("danger", "danger", "/ˈdeɪndʒər/", "危险")
L.node("dangerous", "dangerous", "/ˈdeɪndʒərəs/", "危险的", **A)
L.node("accident", "accident", "/ˈæksɪdənt/", "事故；意外")
L.node("notice", "notice", "/ˈnoʊtɪs/", "注意到；告示", kind="verb")
L.node("realise", "realise", "/ˈriːəlaɪz/", "意识到", kind="verb", alt="realize", altLabel="美式")
L.node("fool", "fool", "/fuːl/", "傻瓜")
L.node("foolish", "foolish", "/ˈfuːlɪʃ/", "愚蠢的", **A)
L.grid(["careful safety fool",
        "careless . foolish",
        "drop danger dangerous",
        "accident notice realise"], dy=350)
L.edge("safety", "careful"); L.edge("careful", "careless", "ful↔less"); L.edge("careless", "drop"); L.edge("safety", "fool", dashed=True); L.edge("fool", "foolish", "+ish")
L.edge("careless", "danger", dashed=True); L.edge("danger", "dangerous", "+ous"); L.edge("danger", "accident", dashed=True); L.edge("accident", "notice", dashed=True); L.edge("notice", "realise", dashed=True)

L.seg("title", zh("小朋友们好！安全第一！今天，我们来学和安全有关的单词。"), en("safety"))
L.seg("map show:safety focus:safety", zh("安全的，是 safe，加上 t y，就是安全："), en("safe"), en("safety"), en("Safety first!"))
L.seg("show:careful edge:safety>careful focus:careful", zh("做事小心，英语是"), en("careful"), en("Be careful!"))
L.seg("show:careless edge:careful>careless focus:careless", zh("把 f u l 换成 l e s s，就是粗心的。还记得第八十集的规律吗？"), en("careless"))
L.seg("show:drop edge:careless>drop focus:drop", zh("一粗心，东西就掉了："), en("drop"), en("I dropped the flashlight."))
L.seg("show:danger edge:careless>danger focus:danger", zh("危险，英语是"), en("danger"))
L.seg("show:dangerous edge:danger>dangerous focus:dangerous", zh("加上 o u s，就是危险的："), en("dangerous"), en("Fire is dangerous."))
L.seg("show:accident edge:danger>accident focus:accident", zh("意外发生的坏事，是事故："), en("accident"))
L.seg("show:notice edge:accident>notice focus:notice", zh("过马路时，要注意到来往的车。注意到，英语是"), en("notice"), zh("它也是告示的意思。"))
L.seg("show:realise edge:notice>realise focus:realise", zh("突然明白过来，是意识到："), en("realise"), zh("在美国，写成", "alt:realise"), en("realize"))
L.seg("show:fool edge:safety>fool focus:fool", zh("做危险的事，就像个傻瓜："), en("fool"))
L.seg("show:foolish edge:fool>foolish focus:foolish", zh("加上 i s h，就是愚蠢的："), en("foolish"), en("Don't be foolish."))
L.seg("focus:careful,careless", zh("小心和粗心："), en("careful", "focus:careful"), en("careless", "focus:careless"))
L.review([("safety", "safety"), ("careful", "careful"), ("careless", "careless"), ("drop", "drop"), ("danger", "danger"), ("dangerous", "dangerous"),
          ("accident", "accident"), ("notice", "notice"), ("realise", "realise, realize"), ("fool", "fool"), ("foolish", "foolish")],
         "太棒了！记住，安全第一，做事要小心哦。点一点图上的单词，还能再听一遍发音。")
L.save()
