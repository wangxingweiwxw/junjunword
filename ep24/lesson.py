import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep24", "colours", "颜色", 24, "colour")
A = dict(kind="adj")
L.node("colour", "colour", "/ˈkʌlər/", "颜色", alt="color", altLabel="美式")
for id, ipa, z in [("red", "/red/", "红色"), ("orange", "/ˈɔːrɪndʒ/", "橙色"), ("yellow", "/ˈjeloʊ/", "黄色"), ("green", "/ɡriːn/", "绿色"),
                   ("blue", "/bluː/", "蓝色"), ("purple", "/ˈpɜːrpl/", "紫色"), ("pink", "/pɪŋk/", "粉色"), ("white", "/waɪt/", "白色"),
                   ("gold", "/ɡoʊld/", "金色"), ("silver", "/ˈsɪlvər/", "银色"), ("black", "/blæk/", "黑色"), ("brown", "/braʊn/", "棕色")]:
    L.node(id, id, ipa, z)
L.node("bright", "bright", "/braɪt/", "明亮的", **A)
L.node("dark", "dark", "/dɑːrk/", "深色的；黑暗的", **A)
L.grid(["red orange yellow",
        "purple blue green",
        "pink colour brown",
        "bright . dark",
        "white gold black",
        ". silver ."], dy=320)
for a, b in [("red", "orange"), ("orange", "yellow"), ("yellow", "green"), ("green", "blue"), ("blue", "purple")]:
    L.edge(a, b)
L.edge("bright", "white"); L.edge("bright", "gold"); L.edge("gold", "silver", "还有"); L.edge("dark", "black"); L.edge("dark", "brown")

L.seg("title", zh("小朋友们好！雨过天晴，天上挂着一道彩虹。今天，我们来学颜色！"), en("colours"))
L.seg("map show:colour focus:colour", zh("颜色，英语是"), en("colour"),
      zh("在美国，它写作 c o l o r，少了一个字母 u，读音一样。", "alt:colour"), en("What colour is it?"))
L.seg("focus:none", zh("我们沿着彩虹，一个颜色一个颜色地认。"))
L.seg("show:red focus:red", zh("彩虹最外面，是红色，像红红的苹果："), en("red"))
L.seg("show:orange edge:red>orange focus:orange", zh("橙色，和橙子是同一个词："), en("orange"), en("an orange orange!"))
L.seg("show:yellow edge:orange>yellow focus:yellow", zh("黄色，像香蕉："), en("yellow"))
L.seg("show:green edge:yellow>green focus:green", zh("绿色，像树叶："), en("green"))
L.seg("show:blue edge:green>blue focus:blue", zh("蓝色，像大海和天空："), en("blue"))
L.seg("show:purple edge:blue>purple focus:purple", zh("紫色，像一串葡萄："), en("purple"))
L.seg("show:pink focus:pink", zh("红色里加上白色，就变成了可爱的粉色："), en("pink"))
L.seg("show:brown focus:brown", zh("小熊身上，是棕色的："), en("brown"), en("a brown bear"))
L.seg("show:bright focus:bright", zh("阳光照着，颜色亮亮的，是明亮的："), en("bright"))
L.seg("show:white edge:bright>white focus:white", zh("最亮的颜色，是白色，像天上的白云："), en("white"),
      zh("开头的 w 后面跟着一个 h，这个 h 不发音。"))
L.seg("show:gold edge:bright>gold focus:gold", zh("闪闪发光的金色，像金牌："), en("gold"))
L.seg("show:silver edge:gold>silver focus:silver", zh("比金色淡一点的，是银色，像银币："), en("silver"), en("gold and silver"))
L.seg("show:dark focus:dark", zh("天黑了，颜色暗暗的，是深色的、黑暗的："), en("dark"), en("dark blue", "focus:dark,blue"))
L.seg("show:black edge:dark>black focus:black", zh("最深的颜色，是黑色，像夜里的小黑猫："), en("black"))
L.seg("edge:dark>brown focus:dark,brown", zh("棕色，也是深深的颜色："), en("brown"))
L.seg("focus:red,orange,yellow,green,blue,purple", zh("我们把彩虹的颜色，从外到里读一遍："),
      *[en(c, "focus:" + c) for c in ["red", "orange", "yellow", "green", "blue", "purple"]])
L.seg("focus:white,black", zh("一白一黑，正好相反："), en("white", "focus:white"), en("black", "focus:black"))
L.seg("focus:none", zh("猜一猜，它们是什么颜色？"))
L.seg("", zh("香蕉："), en("Yellow!", "focus:yellow"), zh("天空："), en("Blue!", "focus:blue"),
      zh("雪："), en("White!", "focus:white"), zh("我的书包："), en("My schoolbag is orange.", "focus:orange"))
L.review([("colour", "colour")] + [(c, c) for c in ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "bright",
          "white", "gold", "silver", "dark", "black"]],
         "太棒了！你最喜欢什么颜色？用英语告诉爸爸妈妈吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
