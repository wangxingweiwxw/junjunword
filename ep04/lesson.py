import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep04", "birthday", "生日", 4, "birthday")
L.node("birthday", "birthday", "/ˈbɜːrθdeɪ/", "生日")
L.node("party", "party", "/ˈpɑːrti/", "聚会；派对")
L.node("cake", "cake", "/keɪk/", "蛋糕")
L.node("candle", "candle", "/ˈkændl/", "蜡烛", plural="candles", pluralIpa="/ˈkændlz/")
L.node("match", "match", "/mætʃ/", "火柴")
L.node("wish", "wish", "/wɪʃ/", "愿望；许愿")
L.node("blow", "blow", "/bloʊ/", "吹", kind="verb")
L.node("balloon", "balloon", "/bəˈluːn/", "气球", plural="balloons", pluralIpa="/bəˈluːnz/")
L.node("present", "present", "/ˈpreznt/", "礼物", alt="gift", plural="presents", pluralIpa="/ˈpreznts/")
L.node("give", "give", "/ɡɪv/", "给；送", kind="verb")
L.node("get", "get", "/ɡet/", "得到；收到", kind="verb")
L.node("for", "for", "/fɔːr/", "为了；给…的", kind="prep")
L.grid(["birthday party cake",
        "present match candle",
        "give get blow",
        "for wish balloon"], dy=330)
L.edge("birthday", "party"); L.edge("party", "cake"); L.edge("party", "present")
L.edge("cake", "candle", "插上"); L.edge("match", "candle", "点燃")
L.edge("candle", "blow", "吹灭"); L.edge("blow", "balloon", "吹"); L.edge("wish", "blow", "许完愿", dashed=True)
L.edge("present", "give"); L.edge("present", "get"); L.edge("give", "for", dashed=True)

L.seg("title", zh("小朋友们好！今天的单词，和一年里最开心的一天有关。"), en("birthday"), zh("生日。"))
L.seg("map show:birthday focus:birthday", zh("你出生的那一天，每年都会再来一次，它就是你的生日："), en("birthday"), en("Happy birthday!"))
L.seg("show:party edge:birthday>party focus:party", zh("过生日，最开心的就是开一个热热闹闹的聚会："), en("party"), en("a birthday party"))
L.seg("show:cake edge:party>cake focus:cake", zh("聚会上，怎么能少了甜甜的蛋糕？蛋糕，英语是"), en("cake"), en("a big cake"))
L.seg("show:candle edge:cake>candle focus:candle", zh("蛋糕上要插上蜡烛，几岁就插几根："), en("candle"))
L.seg("show:match edge:match>candle focus:match", zh("蜡烛要点亮，就要用到火柴："), en("match"),
      zh("火柴有危险，一定要请大人帮忙点哦。"))
L.seg("show:wish focus:wish,candle", zh("蜡烛亮起来啦！先闭上眼睛，在心里许一个愿望："), en("wish"), en("Make a wish!"))
L.seg("show:blow edge:candle>blow edge:wish>blow focus:blow", zh("许完愿，深吸一口气，呼——把蜡烛吹灭！吹，英语是"), en("blow"),
      en("Blow out the candles!"))
L.seg("show:balloon edge:blow>balloon focus:balloon", zh("嘴巴还能吹什么？对啦，吹气球！气球是"), en("balloon"),
      zh("小提示：它中间有两个字母 l，还有两个字母 o。"), en("Let's blow up a balloon!"))
L.seg("show:present edge:party>present focus:present", zh("朋友们来参加聚会，还会带来礼物："), en("present"),
      zh("礼物还有一个更短的说法，叫", "alt:present"), en("gift"))
L.seg("show:give edge:present>give focus:give", zh("把礼物送给别人，是给："), en("give"), en("I give you a present."))
L.seg("show:get edge:present>get focus:get", zh("收到别人送来的礼物，就是得到："), en("get"), en("I get a present!"))
L.seg("show:for edge:give>for focus:for", zh("这份礼物，是专门为你准备的。说给谁的、为了谁，就用这个小小的词："), en("for"),
      en("This present is for you."))
L.seg("focus:none", zh("生日聚会上，很多东西都不止一个。一个变成很多个，后面加上字母 s 就好啦。"))
L.seg("focus:candle", en("candle", "focus:candle"), en("candles", "plural:candle"),
      en("balloon", "focus:balloon"), en("balloons", "plural:balloon"),
      en("present", "focus:present"), en("presents", "plural:present"))
L.seg("focus:give,get", zh("给和得到，正好是一对。我送出去，是"), en("give", "focus:give"),
      zh("我收进来，是", "focus:get"), en("get"))
L.seg("focus:birthday", zh("最后，我们一起来唱一句生日歌吧！"), en("Happy birthday to you!"))
L.review([("birthday", "birthday"), ("party", "party"), ("cake", "cake"), ("candle", "candle, candles"),
          ("match", "match"), ("wish", "wish"), ("blow", "blow"), ("balloon", "balloon, balloons"),
          ("present", "present, gift"), ("give", "give"), ("get", "get"), ("for", "for")],
         "太棒了！下次过生日的时候，记得用英语许一个愿哦。点一点图上的单词，还能再听一遍发音。")
L.save()
