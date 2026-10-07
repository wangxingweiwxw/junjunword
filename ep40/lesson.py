import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep40", "drinks", "饮品", 40, "juice")
L.node("thirsty", "thirsty", "/ˈθɜːrsti/", "口渴的", kind="adj", alt="thirst", altLabel="名词")
L.node("drink", "drink", "/drɪŋk/", "喝；饮料", kind="verb")
L.node("water", "water", "/ˈwɔːtər/", "水")
L.node("milk", "milk", "/mɪlk/", "牛奶")
L.node("juice", "juice", "/dʒuːs/", "果汁")
L.node("coffee", "coffee", "/ˈkɔːfi/", "咖啡")
L.node("beer", "beer", "/bɪr/", "啤酒")
L.node("soup", "soup", "/suːp/", "汤")
L.node("cup", "cup", "/kʌp/", "杯子")
L.node("enough", "enough", "/ɪˈnʌf/", "足够的", kind="adj")
L.node("satisfy", "satisfy", "/ˈsætɪsfaɪ/", "使满足", kind="verb")
L.grid(["water milk juice",
        "thirsty drink coffee",
        "cup soup beer",
        ". enough satisfy"], dy=350)
L.edge("thirsty", "drink"); L.edge("drink", "water"); L.edge("drink", "milk"); L.edge("drink", "juice"); L.edge("drink", "coffee")
L.edge("drink", "soup"); L.edge("drink", "beer"); L.edge("cup", "drink", "用…喝", dashed=True); L.edge("enough", "satisfy")

L.seg("title", zh("小朋友们好！刚跑完步，嗓子干干的。今天，我们来学喝的东西！"), en("drinks"))
L.seg("map show:thirsty focus:thirsty", zh("嗓子干干的，想喝水，是口渴的："), en("thirsty"),
      zh("去掉最后的 y，就是口渴这件事：", "alt:thirsty"), en("thirst"), en("I'm thirsty!"))
L.seg("show:drink edge:thirsty>drink focus:drink", zh("口渴了，就要喝东西："), en("drink"),
      zh("这个词也可以表示饮料。"), en("Let's have a drink."))
L.seg("show:water edge:drink>water focus:water", zh("最健康的，是白开水："), en("water"))
L.seg("show:milk edge:drink>milk focus:milk", zh("白白的牛奶："), en("milk"), en("I drink milk every morning."))
L.seg("show:juice edge:drink>juice focus:juice", zh("用水果榨的果汁："), en("juice"), en("orange juice"))
L.seg("show:coffee edge:drink>coffee focus:coffee", zh("爸爸妈妈早上爱喝咖啡："), en("coffee"), zh("两个 f，两个 e。"))
L.seg("show:beer edge:drink>beer focus:beer", zh("这个是啤酒："), en("beer"), zh("它是大人喝的，小朋友可不能喝哦。"))
L.seg("show:soup edge:drink>soup focus:soup", zh("热乎乎的汤，也可以喝："), en("soup"), en("hot soup"))
L.seg("show:cup edge:cup>drink focus:cup", zh("喝东西，要用杯子："), en("cup"), en("a cup of milk", "focus:cup,milk"))
L.seg("show:enough focus:enough", zh("喝够了，就是足够的："), en("enough"), zh("最后的 g h，读成 f。"), en("That's enough."))
L.seg("show:satisfy edge:enough>satisfy focus:satisfy", zh("喝饱了，心里很满足。使满足，英语是"), en("satisfy"))
L.seg("focus:none", zh("我们来演一演，去饮品店点饮料吧！"))
L.seg("", en("I'm thirsty.", "focus:thirsty"), en("What would you like to drink?", "focus:drink"),
      en("A cup of orange juice, please.", "focus:cup,juice"), en("Thank you! That's enough.", "focus:enough"))
L.review([("thirsty", "thirsty, thirst"), ("drink", "drink"), ("water", "water"), ("milk", "milk"), ("juice", "juice"),
          ("coffee", "coffee"), ("beer", "beer"), ("soup", "soup"), ("cup", "cup"), ("enough", "enough"), ("satisfy", "satisfy")],
         "太棒了！口渴的时候，记得多喝水哦。点一点图上的单词，还能再听一遍发音。")
L.save()
