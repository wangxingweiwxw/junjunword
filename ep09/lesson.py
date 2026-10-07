import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep09", "sports", "运动", 9, "sports")
L.node("sports", "sports", "/spɔːrts/", "运动；体育")
L.node("run", "run", "/rʌn/", "跑", kind="verb")
L.node("race", "race", "/reɪs/", "赛跑；比赛")
L.node("jump", "jump", "/dʒʌmp/", "跳", kind="verb")
L.node("fall", "fall", "/fɔːl/", "摔倒；落下", kind="verb", alt="fell", altLabel="过去式")
L.node("ball", "ball", "/bɔːl/", "球")
L.node("football", "football", "/ˈfʊtbɔːl/", "足球")
L.node("soccer", "soccer", "/ˈsɑːkər/", "足球（美式）")
L.node("basketball", "basketball", "/ˈbæskɪtbɔːl/", "篮球")
L.node("volleyball", "volleyball", "/ˈvɑːlibɔːl/", "排球")
L.node("tabletennis", "table tennis", "/ˈteɪbl ˌtenɪs/", "乒乓球")
L.node("net", "net", "/net/", "网")
L.grid(["run sports jump",
        "race . fall",
        "football ball basketball",
        "soccer tabletennis volleyball",
        ". net ."])
L.edge("sports", "run"); L.edge("sports", "jump"); L.edge("run", "race", "比一比"); L.edge("jump", "fall", "没站稳")
L.edge("sports", "ball"); L.edge("ball", "football"); L.edge("ball", "basketball"); L.edge("ball", "tabletennis")
L.edge("ball", "volleyball"); L.edge("football", "soccer", "美国叫"); L.edge("tabletennis", "net"); L.edge("volleyball", "net")

L.seg("title", zh("小朋友们好！今天，我们来学运动。"), en("sports"), zh("运动，体育。"))
L.seg("map show:sports focus:sports", zh("跑跑跳跳、打球踢球，这些都是运动："), en("sports"),
      zh("运动有很多很多种，所以这个词常常带着字母 s。"), en("I love sports!"))
L.seg("show:run edge:sports>run focus:run", zh("最简单的运动是跑步。还记得第七集学过的吗？"), en("run"))
L.seg("show:race edge:run>race focus:race", zh("大家站在同一条起跑线上，比一比谁跑得快，就是赛跑："), en("race"), en("Let's have a race!"))
L.seg("show:jump edge:sports>jump focus:jump", zh("两只脚用力一蹬，跳起来："), en("jump"), en("Jump high!"))
L.seg("show:fall edge:jump>fall focus:fall", zh("哎呀，没站稳，摔倒了！摔倒、落下，英语是"), en("fall"),
      zh("如果是已经摔倒了，要说成", "alt:fall"), en("fell"), zh("把字母 a 换成 e，就变成过去发生的事啦。"), en("He fell down."))
L.seg("show:ball edge:sports>ball focus:ball", zh("很多运动，都离不开一个圆圆的球："), en("ball"), en("Catch the ball!"))
L.seg("show:football edge:ball>football focus:football", zh("用脚踢的球，是足球。还记得上一集的脚吗？脚加上球："),
      en("foot"), en("ball"), en("football"))
L.seg("show:soccer edge:football>soccer focus:soccer", zh("在美国，足球还有另外一个名字："), en("soccer"), en("Let's play soccer."))
L.seg("show:basketball edge:ball>basketball focus:basketball", zh("把球投进高高的篮筐里，是篮球。篮子，加上球："),
      en("basket"), en("basketball"))
L.seg("show:volleyball edge:ball>volleyball focus:volleyball", zh("隔着一张网，用手把球拍来拍去，是排球："), en("volleyball"))
L.seg("show:tabletennis edge:ball>tabletennis focus:tabletennis", zh("在桌子上打的小小的球，是乒乓球。桌子，加上网球："),
      en("table"), en("tennis"), en("table tennis"))
L.seg("show:net edge:tabletennis>net edge:volleyball>net focus:net", zh("排球场和乒乓球桌的中间，都拦着一张网："), en("net"),
      en("Hit the ball over the net."))
L.seg("focus:none", zh("你发现了吗？好多球类的名字，都是用小词拼起来的。"))
L.seg("", en("foot, ball, football", "focus:football"), en("basket, ball, basketball", "focus:basketball"),
      en("table, tennis, table tennis", "focus:tabletennis"))
L.seg("focus:none", zh("说打球、踢球，英语里都用同一个词"), en("play"))
L.seg("", en("play football", "focus:football"), en("play basketball", "focus:basketball"),
      en("play table tennis", "focus:tabletennis"), en("My favorite sport is basketball.", "focus:basketball"))
L.review([("sports", "sports"), ("run", "run"), ("race", "race"), ("jump", "jump"), ("fall", "fall, fell"),
          ("ball", "ball"), ("football", "football"), ("soccer", "soccer"), ("basketball", "basketball"),
          ("volleyball", "volleyball"), ("tabletennis", "table tennis"), ("net", "net")],
         "太棒了！你最喜欢哪一项运动？试着用英语告诉爸爸妈妈吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
