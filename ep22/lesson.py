import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep22", "friends", "朋友", 22, "friend")
V, A = dict(kind="verb"), dict(kind="adj")
L.node("friend", "friend", "/frend/", "朋友", plural="friends", pluralIpa="/frendz/")
L.node("let", "let", "/let/", "让；允许", **V)
L.node("play", "play", "/pleɪ/", "玩", **V)
L.node("with", "with", "/wɪð/", "和……一起", kind="prep")
L.node("game", "game", "/ɡeɪm/", "游戏；比赛")
L.node("toy", "toy", "/tɔɪ/", "玩具", plural="toys", pluralIpa="/tɔɪz/")
L.node("share", "share", "/ʃer/", "分享", **V)
L.node("greet", "greet", "/ɡriːt/", "打招呼", **V)
L.node("wave", "wave", "/weɪv/", "挥手", **V)
L.node("shy", "shy", "/ʃaɪ/", "害羞的", **A)
L.node("nervous", "nervous", "/ˈnɜːrvəs/", "紧张的", **A)
L.node("promise", "promise", "/ˈprɑːmɪs/", "承诺；保证", **V)
L.grid(["let play game",
        "with toy share",
        "friend greet wave",
        "promise shy nervous"], dy=340)
L.edge("let", "play"); L.edge("play", "with"); L.edge("play", "game"); L.edge("with", "friend")
L.edge("share", "toy", dashed=True); L.edge("play", "toy"); L.edge("friend", "greet"); L.edge("greet", "wave", "用手")
L.edge("shy", "nervous", "有点像"); L.edge("friend", "promise")

L.seg("title", zh("小朋友们好！你有好朋友吗？今天，我们来学和朋友有关的单词。"), en("friends"), zh("朋友。"))
L.seg("map show:let focus:let", zh("周末到了，妈妈说：去玩吧！让、允许，英语是"), en("let"),
      en("My mother lets me play."))
L.seg("show:play edge:let>play focus:play", zh("玩，英语是"), en("play"), en("Let's play!"))
L.seg("show:with edge:play>with focus:with", zh("一个人玩没意思，要和别人一起玩。和……一起，英语是"), en("with"),
      zh("还记得第十二集的没有吗？with，加上 out，就是没有。"))
L.seg("show:friend edge:with>friend focus:friend", zh("和谁一起玩呢？和好朋友！朋友，英语是"), en("friend"),
      zh("小提示：中间的 i 不发音哦。"), en("I play with my friends.", "plural:friend"))
L.seg("show:game edge:play>game focus:game", zh("我们一起玩游戏："), en("game"), en("Let's play a game!"))
L.seg("show:toy edge:play>toy focus:toy", zh("还可以一起玩玩具："), en("toy"), zh("很多玩具：", "plural:toy"), en("toys"))
L.seg("show:share edge:share>toy focus:share", zh("好朋友会把自己的玩具拿出来，和大家一起玩。分享，英语是"), en("share"),
      en("We can share toys."))
L.seg("show:greet edge:friend>greet focus:greet", zh("见到朋友，先要打个招呼："), en("greet"), en("Hello, friend!"))
L.seg("show:wave edge:greet>wave focus:wave", zh("离得远，就举起手来挥一挥："), en("wave"), en("Wave goodbye!"))
L.seg("show:shy focus:shy", zh("有的小朋友见到新朋友，会脸红，不好意思说话，那是害羞："), en("shy"), en("Don't be shy!"))
L.seg("show:nervous edge:shy>nervous focus:nervous", zh("心里怦怦跳，手心冒汗，是紧张："), en("nervous"),
      zh("别紧张，笑一笑，主动打个招呼就好啦。"))
L.seg("show:promise edge:friend>promise focus:promise", zh("好朋友之间，说到就要做到。我们勾勾手指，做一个承诺："), en("promise"),
      en("I promise!"))
L.seg("focus:greet,wave", zh("打招呼的两种方式："), en("greet", "focus:greet"), en("wave", "focus:wave"))
L.seg("focus:shy,nervous", zh("两种不好意思的感觉："), en("shy", "focus:shy"), en("nervous", "focus:nervous"))
L.seg("focus:none", zh("我们来演一演，交一个新朋友吧！"))
L.seg("", en("Hi! I'm Lele. What's your name?", "focus:greet"), en("Do you want to play with me?", "focus:play,with"),
      en("We can share my toys.", "focus:share,toy"), en("Let's be friends!", "focus:friend"))
L.review([("let", "let"), ("play", "play"), ("with", "with"), ("friend", "friend, friends"), ("game", "game"), ("toy", "toy, toys"),
          ("share", "share"), ("greet", "greet"), ("wave", "wave"), ("shy", "shy"), ("nervous", "nervous"), ("promise", "promise")],
         "太棒了！明天，用英语和你的好朋友打个招呼吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
