import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep84", "magic", "魔法", 84, "magic")
A, V = dict(kind="adj"), dict(kind="verb")
L.node("magic", "magic", "/ˈmædʒɪk/", "魔法；魔术")
L.node("instruction", "instruction", "/ɪnˈstrʌkʃn/", "指示；说明")
L.node("simple", "simple", "/ˈsɪmpl/", "简单的", **A)
L.node("satisfaction", "satisfaction", "/ˌsætɪsˈfækʃn/", "满意", alt="satisfy", altLabel="来自")
L.node("possible", "possible", "/ˈpɑːsəbl/", "可能的", **A)
L.node("impossible", "impossible", "/ɪmˈpɑːsəbl/", "不可能的", **A)
L.node("appear", "appear", "/əˈpɪr/", "出现", **V)
L.node("disappear", "disappear", "/ˌdɪsəˈpɪr/", "消失", **V)
L.node("rope", "rope", "/roʊp/", "绳子")
L.node("climb", "climb", "/klaɪm/", "爬", **V)
L.node("instead", "instead", "/ɪnˈsted/", "代替；反而", kind="adv")
L.grid(["instruction magic simple",
        "possible . satisfaction",
        "impossible . appear",
        "rope climb disappear",
        ". instead ."], dy=330)
L.edge("magic", "instruction"); L.edge("magic", "simple"); L.edge("simple", "satisfaction", dashed=True); L.edge("instruction", "possible", dashed=True)
L.edge("possible", "impossible", "im+"); L.edge("appear", "disappear", "dis+"); L.edge("satisfaction", "appear", dashed=True); L.edge("rope", "climb"); L.edge("climb", "instead", dashed=True)

L.seg("title", zh("小朋友们好！变——魔术表演开始啦！今天，我们来学和魔术有关的单词。"), en("magic"))
L.seg("map show:magic focus:magic", zh("神奇的魔法、魔术，英语是"), en("magic"))
L.seg("show:instruction edge:magic>instruction focus:instruction", zh("变魔术，先看说明书上的指示："), en("instruction"))
L.seg("show:simple edge:magic>simple focus:simple", zh("这个魔术很简单："), en("simple"), zh("还记得第七十八集的 easy 吗？意思差不多。"))
L.seg("show:possible edge:instruction>possible focus:possible", zh("可能的，英语是"), en("possible"))
L.seg("show:impossible edge:possible>impossible focus:impossible", zh("加上 i m，就是不可能的。还记得第七十四集的 impatient 吗？"), en("impossible"), en("Nothing is impossible!"))
L.seg("show:satisfaction edge:simple>satisfaction focus:satisfaction", zh("魔术成功了，观众很满意。还记得第四十集的 satisfy 吗？"), en("satisfy"), en("satisfaction"))
L.seg("show:appear edge:satisfaction>appear focus:appear", zh("挥一挥魔杖，小兔子出现了："), en("appear"))
L.seg("show:disappear edge:appear>disappear focus:disappear", zh("再挥一下，它又消失了！前面加上 d i s："), en("disappear"))
L.seg("show:rope focus:rope", zh("魔术师拿出一根绳子："), en("rope"))
L.seg("show:climb edge:rope>climb focus:climb", zh("顺着绳子往上爬："), en("climb"), zh("最后的 b 不发音哦。"))
L.seg("show:instead edge:climb>instead focus:instead", zh("我不爬绳子，我走楼梯。代替，英语是"), en("instead"), en("I will use the stairs instead of climbing the rope."))
L.seg("focus:impossible,disappear", zh("两个让意思反过来的头："), en("possible, impossible", "focus:possible,impossible"), en("appear, disappear", "focus:appear,disappear"))
L.review([("magic", "magic"), ("instruction", "instruction"), ("simple", "simple"), ("possible", "possible"), ("impossible", "impossible"), ("satisfaction", "satisfaction"),
          ("appear", "appear"), ("disappear", "disappear"), ("rope", "rope"), ("climb", "climb"), ("instead", "instead")],
         "太棒了！学一个小魔术，表演给家人看吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
