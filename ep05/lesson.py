import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep05", "home", "家", 5, "home")
L.node("home", "home", "/hoʊm/", "家")
L.node("house", "house", "/haʊs/", "房子")
L.node("address", "address", "/ˈædres/", "地址")
L.node("door", "door", "/dɔːr/", "门")
L.node("lock", "lock", "/lɑːk/", "锁")
L.node("key", "key", "/kiː/", "钥匙")
L.node("window", "window", "/ˈwɪndoʊ/", "窗户")
L.node("stairs", "stairs", "/sterz/", "楼梯")
L.node("step", "step", "/step/", "台阶；一步", plural="steps", pluralIpa="/steps/")
L.node("gate", "gate", "/ɡeɪt/", "大门")
L.node("yard", "yard", "/jɑːrd/", "院子")
L.node("flower", "flower", "/ˈflaʊər/", "花", plural="flowers", pluralIpa="/ˈflaʊərz/")
L.node("pool", "pool", "/puːl/", "游泳池")
L.grid(["address home window",
        "door house stairs",
        "lock gate step",
        "key yard pool",
        ". flower ."], dy=345)
L.edge("home", "address"); L.edge("home", "house")
L.edge("house", "door"); L.edge("door", "lock"); L.edge("key", "lock", "打开")
L.edge("house", "window"); L.edge("house", "stairs"); L.edge("stairs", "step", "每一级")
L.edge("house", "gate"); L.edge("gate", "yard", "走进"); L.edge("yard", "flower"); L.edge("yard", "pool")

L.seg("title", zh("小朋友们好！今天我们来认识自己的家。英语里，有两个词都和家有关。"), en("home"), en("house"))
L.seg("map show:home focus:home", zh("第一个是"), en("home"),
      zh("它是有爸爸妈妈、让你觉得温暖的那个家。"), en("I love my home."))
L.seg("show:house edge:home>house focus:house", zh("第二个是"), en("house"),
      zh("它说的是房子本身，是用砖头和木头盖起来、看得见摸得着的建筑。"), en("This is my house."))
L.seg("focus:home,house", zh("一个是温暖的家，一个是盖好的房子。放学了，我们要说："), en("Let's go home!"))
L.seg("show:address edge:home>address focus:address", zh("要让快递叔叔找到你的家，就要写清楚地址："), en("address"),
      zh("小提示：它有两个字母 d，最后还有两个字母 s。"), en("What's your address?"))
L.seg("show:door edge:house>door focus:door", zh("走到房子跟前，先看到的是门："), en("door"), en("Open the door, please."))
L.seg("show:lock edge:door>lock focus:lock", zh("门上有一把锁，锁好了，家里就安全啦："), en("lock"))
L.seg("show:key edge:key>lock focus:key", zh("要打开这把锁，就得用钥匙："), en("key"), en("Where is my key?"))
L.seg("show:window edge:house>window focus:window", zh("房子上还有窗户，阳光从这里照进来："), en("window"), en("Look out of the window."))
L.seg("show:stairs edge:house>stairs focus:stairs", zh("上楼下楼，要走楼梯："), en("stairs"),
      zh("楼梯有很多级，所以这个词的最后，总是带着字母 s。"))
L.seg("show:step edge:stairs>step focus:step", zh("楼梯上的每一级是台阶；迈出去的一步，也用这个词："), en("step"),
      en("one step"), en("two steps", "plural:step"))
L.seg("show:gate edge:house>gate focus:gate", zh("房子外面的围墙上，还有一扇大门："), en("gate"),
      zh("房子上的门和院子外的大门，可不是同一个词哦。"), en("door", "focus:door"), en("gate", "focus:gate"))
L.seg("show:yard edge:gate>yard focus:yard", zh("走进大门，就是院子："), en("yard"), en("We play in the yard."))
L.seg("show:flower edge:yard>flower focus:flower", zh("院子里，开满了漂亮的花："), en("flower"), en("flowers", "plural:flower"))
L.seg("show:pool edge:yard>pool focus:pool", zh("要是院子很大，说不定还有一个游泳池："), en("pool"), en("Let's swim in the pool!"))
L.seg("focus:none", zh("现在，我们从外面一路走回家里，再说一遍吧！"))
L.seg("", *[en(w, "focus:" + w) for w in ["gate", "yard", "door", "stairs", "house", "home"]])
L.review([("home", "home"), ("house", "house"), ("address", "address"), ("door", "door"), ("lock", "lock"),
          ("key", "key"), ("window", "window"), ("stairs", "stairs"), ("step", "step, steps"), ("gate", "gate"),
          ("yard", "yard"), ("flower", "flower, flowers"), ("pool", "pool")],
         "太棒了！回家的路上，试着用英语说一说你看到的东西。点一点图上的单词，还能再听一遍发音哦。")
L.save()
