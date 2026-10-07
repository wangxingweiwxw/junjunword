import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep41", "chores", "家务", 41, "chore")
V, A = dict(kind="verb"), dict(kind="adj")
L.node("chore", "chore", "/tʃɔːr/", "家务活", plural="chores", pluralIpa="/tʃɔːrz/")
L.node("mess", "mess", "/mes/", "乱七八糟", alt="messy", altLabel="加 y →")
L.node("tidy", "tidy", "/ˈtaɪdi/", "整理；整齐的", **V)
L.node("dirty", "dirty", "/ˈdɜːrti/", "脏的", **A)
L.node("wash", "wash", "/wɑːʃ/", "洗", **V)
L.node("clean", "clean", "/kliːn/", "干净的；打扫", **A)
L.node("floor", "floor", "/flɔːr/", "地板")
L.node("sweep", "sweep", "/swiːp/", "扫", **V)
L.node("brush", "brush", "/brʌʃ/", "刷子；刷", alt="toothbrush", altLabel="想起")
L.node("rubbish", "rubbish", "/ˈrʌbɪʃ/", "垃圾")
L.node("bin", "bin", "/bɪn/", "垃圾桶")
L.node("basket", "basket", "/ˈbæskɪt/", "篮子")
L.grid(["mess chore tidy",
        "dirty wash clean",
        "floor sweep brush",
        "rubbish bin basket"], dy=350)
L.edge("chore", "mess"); L.edge("mess", "tidy", dashed=True); L.edge("chore", "tidy"); L.edge("dirty", "wash"); L.edge("wash", "clean", "洗完")
L.edge("floor", "sweep"); L.edge("sweep", "brush", dashed=True); L.edge("rubbish", "bin", "扔进")

L.seg("title", zh("小朋友们好！今天放假，我们来帮爸爸妈妈做家务吧！"), en("chores"))
L.seg("map show:chore focus:chore", zh("家里要做的扫地、洗碗这些活儿，叫家务："), en("chore"),
      zh("家务有很多样：", "plural:chore"), en("chores"), en("I help with the chores."))
L.seg("show:mess edge:chore>mess focus:mess", zh("哎呀，房间里乱七八糟的！"), en("mess"),
      zh("加上 y，就是乱糟糟的：", "alt:mess"), en("messy"), en("My room is a mess."))
L.seg("show:tidy edge:chore>tidy edge:mess>tidy focus:tidy", zh("快把东西收拾好，整理得整整齐齐："), en("tidy"), en("Tidy your room!"))
L.seg("show:dirty focus:dirty", zh("衣服弄得脏兮兮的，是"), en("dirty"))
L.seg("show:wash edge:dirty>wash focus:wash", zh("脏了就要洗："), en("wash"), en("Wash your hands."))
L.seg("show:clean edge:wash>clean focus:clean", zh("洗完了，就干干净净的："), en("clean"), zh("脏和干净，正好相反。"),
      en("dirty", "focus:dirty"), en("clean", "focus:clean"))
L.seg("show:floor focus:floor", zh("我们脚下踩的，是地板："), en("floor"))
L.seg("show:sweep edge:floor>sweep focus:sweep", zh("拿起扫帚，扫一扫地："), en("sweep"), en("Sweep the floor."))
L.seg("show:brush edge:sweep>brush focus:brush", zh("刷子，英语是"), en("brush"),
      zh("还记得第三十八集的牙刷吗？", "alt:brush"), en("tooth, brush, toothbrush"))
L.seg("show:rubbish focus:rubbish", zh("扫出来的垃圾，英语是"), en("rubbish"))
L.seg("show:bin edge:rubbish>bin focus:bin", zh("垃圾要扔进垃圾桶："), en("bin"), en("Put the rubbish in the bin."))
L.seg("show:basket focus:basket", zh("脏衣服，先放进篮子里："), en("basket"), zh("还记得第九集的篮球吗？篮子加上球："), en("basketball"))
L.seg("focus:none", zh("今天我们做了这些家务："))
L.seg("", en("I tidy my room.", "focus:tidy"), en("I sweep the floor.", "focus:sweep"), en("I wash the dishes.", "focus:wash"),
      en("Now everything is clean!", "focus:clean"))
L.review([("chore", "chore, chores"), ("mess", "mess, messy"), ("tidy", "tidy"), ("dirty", "dirty"), ("wash", "wash"), ("clean", "clean"),
          ("floor", "floor"), ("sweep", "sweep"), ("brush", "brush"), ("rubbish", "rubbish"), ("bin", "bin"), ("basket", "basket")],
         "太棒了！今天回家，主动帮爸爸妈妈做一件家务吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
