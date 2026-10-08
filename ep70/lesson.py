import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep70", "positions", "位置", 70, "position")
P = dict(kind="prep")
L.node("position", "position", "/pəˈzɪʃn/", "位置")
L.node("on", "on", "/ɑːn/", "在……上面", icon="onpos", **P)
L.node("under", "under", "/ˈʌndər/", "在……下面", **P)
L.node("below", "below", "/bɪˈloʊ/", "在……下方", **P)
L.node("inside", "inside", "/ˌɪnˈsaɪd/", "在……里面", **P)
L.node("outside", "outside", "/ˌaʊtˈsaɪd/", "在……外面", **P)
L.node("front", "front", "/frʌnt/", "前面")
L.node("back", "back", "/bæk/", "后面")
L.node("infront", "in front of", "/ɪn frʌnt əv/", "在……前面", icon="infront", **P)
L.node("behind", "behind", "/bɪˈhaɪnd/", "在……后面", **P)
L.node("beside", "beside", "/bɪˈsaɪd/", "在……旁边", **P)
L.node("between", "between", "/bɪˈtwiːn/", "在……中间", **P)
L.node("around", "around", "/əˈraʊnd/", "在……周围", **P)
L.node("against", "against", "/əˈɡenst/", "靠着", **P)
L.grid(["on position under",
        "inside . below",
        "outside . .",
        "front infront back",
        "behind beside between",
        "around . against"], dy=320)
for id, x, y in [("position", 170, 470), ("on", 470, 150), ("under", 770, 150), ("below", 1070, 150), ("inside", 1370, 150), ("outside", 1670, 150),
                 ("front", 470, 470), ("back", 770, 470), ("infront", 1070, 470), ("behind", 1370, 470), ("beside", 1670, 470),
                 ("between", 770, 790), ("around", 1070, 790), ("against", 1370, 790)]:
    L.byid[id]["at"] = [x, y]
L.edge("on", "under", "反义"); L.edge("under", "below", dashed=True); L.edge("inside", "outside", "反义"); L.edge("front", "back", "反义")
L.edge("infront", "behind", "反义"); L.edge("position", "front", dashed=True)

L.seg("title", zh("小朋友们好！小红球藏在哪里？今天，我们来学表示位置的小词！"), en("position"))
L.seg("map show:position focus:position", zh("东西所在的地方，是位置："), en("position"))
L.seg("show:on focus:on", zh("小球在箱子上面："), en("on"), en("The ball is on the box."))
L.seg("show:under edge:on>under focus:under", zh("小球在桌子下面："), en("under"), en("The ball is under the table."))
L.seg("show:below edge:under>below focus:below", zh("在……下方，还可以说"), en("below"))
L.seg("show:inside focus:inside", zh("小球在箱子里面："), en("inside"), zh("还记得 in 吗？in 加上旁边 side。"))
L.seg("show:outside edge:inside>outside focus:outside", zh("小球跑到外面去了："), en("outside"), zh("out 加上 side。"))
L.seg("show:front focus:front", zh("箱子的前面，是"), en("front"))
L.seg("show:back edge:front>back focus:back", zh("箱子的后面，是"), en("back"))
L.seg("show:infront focus:infront", zh("小球在箱子的前面，要说"), en("in front of"), en("My car is in front of the supermarket."))
L.seg("show:behind edge:infront>behind focus:behind", zh("小球躲在箱子的后面："), en("behind"))
L.seg("show:beside focus:beside", zh("小球挨着箱子，在旁边："), en("beside"))
L.seg("show:between focus:between", zh("小球夹在两个箱子中间："), en("between"))
L.seg("show:around focus:around", zh("好多小球围着箱子，在周围："), en("around"))
L.seg("show:against focus:against", zh("一根小棍斜斜地靠着箱子："), en("against"))
L.seg("focus:on,under", zh("上和下："), en("on", "focus:on"), en("under", "focus:under"))
L.seg("focus:inside,outside", zh("里和外："), en("inside", "focus:inside"), en("outside", "focus:outside"))
L.seg("focus:infront,behind", zh("前和后："), en("in front of", "focus:infront"), en("behind", "focus:behind"))
L.seg("focus:none", zh("来玩藏球游戏！小球在哪里？"))
L.seg("", en("It's under the table!", "focus:under"), en("It's behind the box!", "focus:behind"), en("It's between the boxes!", "focus:between"))
L.review([("position", "position"), ("on", "on"), ("under", "under"), ("below", "below"), ("inside", "inside"), ("outside", "outside"), ("front", "front"),
          ("back", "back"), ("infront", "in front of"), ("behind", "behind"), ("beside", "beside"), ("between", "between"), ("around", "around"), ("against", "against")],
         "太棒了！和爸爸妈妈玩一玩藏东西的游戏，用英语说出它在哪里吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
