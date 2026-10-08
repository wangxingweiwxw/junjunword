import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep73", "location", "位置（二）", 73, "location")
A = dict(kind="adj")
L.node("location", "location", "/loʊˈkeɪʃn/", "位置；地点")
L.node("front", "front", "/frʌnt/", "前面")
L.node("side", "side", "/saɪd/", "侧面；旁边")
L.node("top", "top", "/tɑːp/", "顶部")
L.node("surface", "surface", "/ˈsɜːrfɪs/", "表面")
L.node("above", "above", "/əˈbʌv/", "在……上方", kind="prep")
L.node("part", "part", "/pɑːrt/", "部分")
L.node("middle", "middle", "/ˈmɪdl/", "中间")
L.node("center", "center", "/ˈsentər/", "中心")
L.node("central", "central", "/ˈsentrəl/", "中心的", **A)
L.node("high", "high", "/haɪ/", "高的", **A)
L.node("low", "low", "/loʊ/", "低的", **A)
L.grid(["front location side",
        "surface top above",
        "part middle center",
        "high low central"], dy=350)
L.edge("location", "front"); L.edge("location", "side"); L.edge("location", "top"); L.edge("top", "surface", dashed=True); L.edge("top", "above", dashed=True)
L.edge("middle", "part", dashed=True); L.edge("middle", "center", dashed=True); L.edge("center", "central", "+al"); L.edge("high", "low", "反义")

L.seg("title", zh("小朋友们好！还记得第七十集的位置吗？今天，我们学更多描述位置的词。"), en("location"))
L.seg("map show:location focus:location", zh("东西所在的地方，是位置、地点："), en("location"))
L.seg("show:front edge:location>front focus:front", zh("箱子的前面："), en("front"))
L.seg("show:side edge:location>side focus:side", zh("箱子的侧面："), en("side"), zh("还记得 inside、outside 吗？都有它。"))
L.seg("show:top edge:location>top focus:top", zh("箱子的最上面，是顶部："), en("top"), en("The top of the bridge is very high."))
L.seg("show:surface edge:top>surface focus:surface", zh("东西的最外面一层，是表面："), en("surface"))
L.seg("show:above edge:top>above focus:above", zh("在上方，不挨着，是"), en("above"), zh("还记得 below 吗？正好相反。"))
L.seg("show:middle focus:middle", zh("排在中间的，是"), en("middle"))
L.seg("show:part edge:middle>part focus:part", zh("一样东西的一部分，是"), en("part"), en("I like the middle part of the song."))
L.seg("show:center edge:middle>center focus:center", zh("圆的正中心，是"), en("center"))
L.seg("show:central edge:center>central focus:central", zh("变成形容词，中心的："), en("central"), en("Central Park"))
L.seg("show:high focus:high", zh("高高的山，是"), en("high"), zh("还记得第二十八集的 tall 吗？人用 tall，山和楼常常用 high。"))
L.seg("show:low edge:high>low focus:low", zh("矮矮的、低低的，是"), en("low"))
L.seg("focus:above", zh("上方和下方："), en("above", "focus:above"), en("below"))
L.review([("location", "location"), ("front", "front"), ("side", "side"), ("top", "top"), ("surface", "surface"), ("above", "above"), ("middle", "middle"),
          ("part", "part"), ("center", "center"), ("central", "central"), ("high", "high"), ("low", "low")],
         "太棒了！用英语说一说你的书包放在哪里吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
