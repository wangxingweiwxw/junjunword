import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep53", "directions", "方向", 53, "turn")
P = dict(kind="prep")
L.node("find", "find", "/faɪnd/", "找到", kind="verb")
L.node("way", "way", "/weɪ/", "路；方法")
L.node("towards", "towards", "/təˈwɔːrdz/", "朝着", **P)
L.node("turn", "turn", "/tɜːrn/", "转弯", kind="verb")
L.node("left", "left", "/left/", "左边")
L.node("right", "right", "/raɪt/", "右边", icon="rightdir")
L.node("up", "up", "/ʌp/", "向上", kind="adv")
L.node("down", "down", "/daʊn/", "向下", kind="adv")
L.node("over", "over", "/ˈoʊvər/", "越过", **P)
L.node("through", "through", "/θruː/", "穿过", **P)
L.node("along", "along", "/əˈlɔːŋ/", "沿着", **P)
L.node("into", "into", "/ˈɪntuː/", "进入", **P)
L.grid(["find way towards",
        "left turn right",
        "up . down",
        "over along through",
        ". into ."], dy=330)
L.edge("find", "way"); L.edge("way", "towards"); L.edge("way", "turn", dashed=True); L.edge("turn", "left"); L.edge("turn", "right")
L.edge("up", "down", "反义"); L.edge("along", "over", dashed=True); L.edge("along", "through", dashed=True); L.edge("along", "into")

L.seg("title", zh("小朋友们好！迷路了怎么办？今天，我们来学问路和指路！"), en("directions"))
L.seg("map show:find focus:find", zh("要找到地方，英语是"), en("find"), en("I can't find the library."))
L.seg("show:way edge:find>way focus:way", zh("去一个地方的路，是"), en("way"), en("Can you tell me the way?"))
L.seg("show:towards edge:way>towards focus:towards", zh("朝着一个方向走，是"), en("towards"), en("Walk towards the bank."))
L.seg("show:turn edge:way>turn focus:turn", zh("走到路口，要转弯："), en("turn"))
L.seg("show:left edge:turn>left focus:left", zh("往左转："), en("turn left"), zh("左边，是"), en("left"))
L.seg("show:right edge:turn>right focus:right", zh("往右转："), en("turn right"), zh("右边，是"), en("right"))
L.seg("focus:left,right", zh("一左一右，跟着我伸出手："), en("left!", "focus:left"), en("right!", "focus:right"))
L.seg("show:up focus:up", zh("向上，是"), en("up"), en("Go up the stairs."))
L.seg("show:down edge:up>down focus:down", zh("向下，是"), en("down"), en("Go down the stairs."))
L.seg("show:along focus:along", zh("顺着一条路一直走，是沿着："), en("along"), en("Go along the street."))
L.seg("show:over edge:along>over focus:over", zh("从桥的上面走过去，是越过："), en("over"), en("Go over the bridge."))
L.seg("show:through edge:along>through focus:through", zh("从隧道的里面穿过去，是"), en("through"), en("Go through the tunnel."))
L.seg("show:into edge:along>into focus:into", zh("从外面走进里面，是进入："), en("into"), zh("在……里面，加上到："), en("in"), en("to"), en("into"))
L.seg("focus:over,through", zh("一个从上面过，一个从里面过："), en("over", "focus:over"), en("through", "focus:through"))
L.seg("focus:none", zh("我们来指路吧！"))
L.seg("", en("Go along the street.", "focus:along"), en("Turn left at the corner.", "focus:turn,left"),
      en("Go over the bridge.", "focus:over"), en("Then go into the library!", "focus:into"))
L.review([("find", "find"), ("way", "way"), ("towards", "towards"), ("turn", "turn"), ("left", "left"), ("right", "right"), ("up", "up"),
          ("down", "down"), ("along", "along"), ("over", "over"), ("through", "through"), ("into", "into")],
         "太棒了！下次出门，试着用英语给爸爸妈妈指一指路吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
