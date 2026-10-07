import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep15", "sports", "运动（二）", 15, "spirit")
V, A = dict(kind="verb"), dict(kind="adj")
L.node("sports", "sports", "/spɔːrts/", "运动")
L.node("choose", "choose", "/tʃuːz/", "选择", alt="choice", altLabel="名词", **V)
L.node("baseball", "baseball", "/ˈbeɪsbɔːl/", "棒球")
L.node("throw", "throw", "/θroʊ/", "扔；投", **V)
L.node("hit", "hit", "/hɪt/", "打；击", **V)
L.node("swimming", "swimming", "/ˈswɪmɪŋ/", "游泳（运动）")
L.node("swim", "swim", "/swɪm/", "游泳", **V)
L.node("training", "training", "/ˈtreɪnɪŋ/", "训练")
L.node("strong", "strong", "/strɔːŋ/", "强壮的", **A)
L.node("weak", "weak", "/wiːk/", "虚弱的", **A)
L.node("quick", "quick", "/kwɪk/", "快的", **A)
L.node("coach", "coach", "/koʊtʃ/", "教练")
L.node("encourage", "encourage", "/ɪnˈkɜːrɪdʒ/", "鼓励", **V)
L.node("spirit", "spirit", "/ˈspɪrɪt/", "精神；勇气")
L.grid(["coach encourage spirit",
        "throw baseball hit",
        "choose sports training",
        "swimming quick strong",
        "swim . weak"])
L.edge("coach", "encourage"); L.edge("encourage", "spirit")
L.edge("sports", "baseball"); L.edge("baseball", "throw", "投"); L.edge("baseball", "hit", "击")
L.edge("choose", "sports"); L.edge("sports", "training"); L.edge("sports", "swimming")
L.edge("swim", "swimming", "+ming"); L.edge("training", "strong"); L.edge("strong", "weak", "反义"); L.edge("training", "quick")

L.seg("title", zh("小朋友们好！第九集，我们认识了很多运动。今天，我们接着学！"), en("sports"))
L.seg("map show:sports focus:sports", zh("运动的种类可多啦。今天，我们来学更多和运动有关的词。"), en("sports"))
L.seg("show:choose edge:choose>sports focus:choose", zh("这么多运动，先选一个你最喜欢的吧！选择，英语是"), en("choose"),
      zh("它变成名词，就是", "alt:choose"), en("choice"), en("Choose a sport!"))
L.seg("show:baseball edge:sports>baseball focus:baseball", zh("我选棒球！棒球场上有四个垒，垒加上球："), en("base"), en("ball"), en("baseball"))
L.seg("show:throw edge:baseball>throw focus:throw", zh("打棒球，先要把球用力扔出去："), en("throw"), en("Throw the ball!"))
L.seg("show:hit edge:baseball>hit focus:hit", zh("举起球棒，砰的一声，把球打得远远的："), en("hit"), en("Hit the ball!"))
L.seg("show:swimming edge:sports>swimming focus:swimming", zh("夏天，最凉快的运动是游泳："), en("swimming"), en("I like swimming."))
L.seg("show:swim edge:swim>swimming focus:swim", zh("游这个动作，是"), en("swim"),
      zh("变成游泳这项运动，要多写一个字母 m，再加上 i n g："), en("swim", "focus:swim"), en("swimming", "focus:swimming"))
L.seg("show:training edge:sports>training focus:training", zh("想在比赛里赢，平时就要刻苦训练："), en("training"), en("We have training every day."))
L.seg("show:strong edge:training>strong focus:strong", zh("训练多了，身体就变得很强壮："), en("strong"), en("I am strong!"))
L.seg("show:weak edge:strong>weak focus:weak", zh("强壮的反面，是虚弱、没力气："), en("weak"), en("I feel weak."))
L.seg("show:quick edge:training>quick focus:quick", zh("多练习，动作就会变得又快又灵活："), en("quick"), en("Be quick!"))
L.seg("show:coach focus:coach", zh("带着我们训练的人，是教练："), en("coach"), en("Our coach is great."))
L.seg("show:encourage edge:coach>encourage focus:encourage", zh("我们累了的时候，教练会给我们加油，鼓励我们："), en("encourage"),
      en("The coach encourages us."))
L.seg("show:spirit edge:encourage>spirit focus:spirit", zh("被鼓励以后，我们心里就充满了勇气和精神："), en("spirit"), en("team spirit"))
L.seg("focus:strong,weak", zh("比一比这两个相反的词："), en("strong", "focus:strong"), en("weak", "focus:weak"))
L.seg("focus:none", zh("今天也有拼出来、变出来的词："), en("base, ball, baseball", "focus:baseball"), en("swim, swimming", "focus:swim,swimming"))
L.seg("focus:none", zh("我们一起来喊加油口号吧！"))
L.seg("", en("Be strong!", "focus:strong"), en("Be quick!", "focus:quick"), en("Go, go, go!", "focus:spirit"))
L.review([("sports", "sports"), ("choose", "choose, choice"), ("baseball", "baseball"), ("throw", "throw"), ("hit", "hit"),
          ("swimming", "swimming"), ("swim", "swim"), ("training", "training"), ("strong", "strong"), ("weak", "weak"),
          ("quick", "quick"), ("coach", "coach"), ("encourage", "encourage"), ("spirit", "spirit")],
         "太棒了！运动的时候，记得给你的队友加油鼓励哦。点一点图上的单词，还能再听一遍发音。")
L.save()
