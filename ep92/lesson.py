import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep92", "tools", "工具", 92, "tool")
V = dict(kind="verb")
L.node("tool", "tool", "/tuːl/", "工具")
L.node("use", "use", "/juːz/", "使用", **V)
L.node("useful", "useful", "/ˈjuːsfl/", "有用的", kind="adj")
L.node("spare", "spare", "/sper/", "备用的；空闲的", kind="adj")
L.node("flashlight", "flashlight", "/ˈflæʃlaɪt/", "手电筒", alt="torch", altLabel="英式")
L.node("repair", "repair", "/rɪˈper/", "修理", **V)
L.node("fix", "fix", "/fɪks/", "修好", **V)
L.node("mend", "mend", "/mend/", "修补", **V)
L.node("tape", "tape", "/teɪp/", "胶带")
L.grid(["use tool useful",
        "spare . flashlight",
        "repair fix mend",
        ". tape ."], dy=350)
L.edge("use", "tool"); L.edge("tool", "useful"); L.edge("tool", "spare", dashed=True); L.edge("tool", "flashlight"); L.edge("tool", "fix")
L.edge("repair", "fix", "差不多"); L.edge("fix", "mend", "差不多"); L.edge("fix", "tape", dashed=True)

L.seg("title", zh("小朋友们好！东西坏了怎么办？拿出工具箱，我们来修一修！"), en("tools"))
L.seg("map show:tool focus:tool", zh("扳手、螺丝刀，都是工具："), en("tool"))
L.seg("show:use edge:use>tool focus:use", zh("使用工具，英语是"), en("use"))
L.seg("show:useful edge:tool>useful focus:useful", zh("工具很有用。还记得第八十集吗？use 加上 f u l："), en("useful"))
L.seg("show:spare edge:tool>spare focus:spare", zh("多准备一个，以备不时之需，是备用的："), en("spare"), en("a spare tire"))
L.seg("show:flashlight edge:tool>flashlight focus:flashlight", zh("黑暗里照亮的手电筒。闪光，加上光："), en("flash"), en("light"), en("flashlight"),
      zh("在英国，它叫", "alt:flashlight"), en("torch"))
L.seg("show:fix edge:tool>fix focus:fix", zh("把坏了的东西修好："), en("fix"), en("Dad can fix my bike."))
L.seg("show:repair edge:repair>fix focus:repair", zh("修理，还可以说"), en("repair"))
L.seg("show:mend edge:fix>mend focus:mend", zh("把破了的地方补好，是修补："), en("mend"), en("mend the fence"))
L.seg("show:tape edge:fix>tape focus:tape", zh("书撕破了，用胶带粘一粘："), en("tape"))
L.seg("focus:fix,repair,mend", zh("三个都有修的意思："), en("fix", "focus:fix"), en("repair", "focus:repair"), en("mend", "focus:mend"))
L.review([("tool", "tool"), ("use", "use"), ("useful", "useful"), ("spare", "spare"), ("flashlight", "flashlight, torch"), ("fix", "fix"), ("repair", "repair"),
          ("mend", "mend"), ("tape", "tape")],
         "太棒了！东西坏了，和爸爸一起试着修一修吧。用工具时要注意安全哦。点一点图上的单词，还能再听一遍发音。")
L.save()
