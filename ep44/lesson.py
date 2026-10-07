import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep44", "restaurant", "餐厅", 44, "restaurant")
A = dict(kind="adj")
L.node("restaurant", "restaurant", "/ˈrestərɑːnt/", "餐厅")
L.node("menu", "menu", "/ˈmenjuː/", "菜单")
L.node("service", "service", "/ˈsɜːrvɪs/", "服务")
L.node("pardon", "pardon", "/ˈpɑːrdn/", "原谅；请再说一遍", alt="Pardon?", altLabel="常说")
L.node("normal", "normal", "/ˈnɔːrml/", "正常的", **A)
L.node("treat", "treat", "/triːt/", "请客；款待", kind="verb")
L.node("make", "make", "/meɪk/", "做；制作", kind="verb")
L.node("dish", "dish", "/dɪʃ/", "一道菜", plural="dishes", pluralIpa="/ˈdɪʃɪz/")
L.node("delicious", "delicious", "/dɪˈlɪʃəs/", "美味的", **A)
L.node("dumpling", "dumpling", "/ˈdʌmplɪŋ/", "饺子", plural="dumplings", pluralIpa="/ˈdʌmplɪŋz/")
L.node("common", "common", "/ˈkɑːmən/", "常见的", **A)
L.node("plenty", "plenty", "/ˈplenti/", "很多；充足")
L.node("piece", "piece", "/piːs/", "一块；一片")
L.node("bit", "bit", "/bɪt/", "一点儿", alt="a bit", altLabel="常说")
L.grid(["treat service normal",
        "menu restaurant pardon",
        "make dish delicious",
        "dumpling common plenty",
        "piece bit ."], dy=330)
L.edge("restaurant", "service"); L.edge("service", "treat", dashed=True); L.edge("service", "normal", dashed=True); L.edge("restaurant", "menu")
L.edge("restaurant", "pardon", dashed=True); L.edge("restaurant", "dish"); L.edge("make", "dish"); L.edge("dish", "delicious")
L.edge("dish", "dumpling"); L.edge("dumpling", "common"); L.edge("dish", "plenty", dashed=True); L.edge("piece", "bit", "更少")

L.seg("title", zh("小朋友们好！还记得第四十三集的餐厅吗？今天，我们走进餐厅点菜！"), en("restaurant"))
L.seg("map show:restaurant focus:restaurant", zh("餐厅，英语是"), en("restaurant"), zh("中间的 a u，读得轻轻的。"))
L.seg("show:menu edge:restaurant>menu focus:menu", zh("坐下来，先看看菜单："), en("menu"), en("Can I see the menu?"))
L.seg("show:service edge:restaurant>service focus:service", zh("服务员来为我们服务："), en("service"), en("Good service!"))
L.seg("show:treat edge:service>treat focus:treat", zh("今天是爸爸请客。请客，英语是"), en("treat"), en("It's my treat!"))
L.seg("show:pardon edge:restaurant>pardon focus:pardon", zh("没听清服务员说什么？可以礼貌地说：", "alt:pardon"), en("Pardon?"),
      zh("意思是，请再说一遍。还记得第十二集的"), en("Excuse me."))
L.seg("show:normal edge:service>normal focus:normal", zh("正常的、普通的，英语是"), en("normal"), en("a normal day"))
L.seg("show:dish edge:restaurant>dish focus:dish", zh("菜单上的每一道菜，叫"), en("dish"),
      zh("很多道菜，加上 e s：", "plural:dish"), en("dishes"))
L.seg("show:make edge:make>dish focus:make", zh("厨师在厨房里做菜："), en("make"), en("The cook makes dishes."))
L.seg("show:delicious edge:dish>delicious focus:delicious", zh("尝一口，真好吃！美味的，英语是"), en("delicious"), en("It's delicious!"))
L.seg("show:dumpling edge:dish>dumpling focus:dumpling", zh("中国人最爱吃的饺子："), en("dumpling"), zh("很多个饺子：", "plural:dumpling"), en("dumplings"))
L.seg("show:common edge:dumpling>common focus:common", zh("饺子在中国很常见："), en("common"), en("Dumplings are a common dish."))
L.seg("show:plenty edge:dish>plenty focus:plenty", zh("菜点得很多，足够吃："), en("plenty"), en("plenty of food"))
L.seg("show:piece focus:piece", zh("一块蛋糕、一片披萨，用"), en("piece"), en("a piece of cake"))
L.seg("show:bit edge:piece>bit focus:bit", zh("比一块还少，只有一点点，是", "alt:bit"), en("a bit"), en("Just a bit, please."))
L.seg("focus:none", zh("我们来演一演点菜吧！"))
L.seg("", en("Can I see the menu, please?", "focus:menu"), en("I want some dumplings.", "focus:dumpling"),
      en("And a piece of cake.", "focus:piece"), en("Mmm, delicious!", "focus:delicious"))
L.review([("restaurant", "restaurant"), ("menu", "menu"), ("service", "service"), ("treat", "treat"), ("pardon", "pardon"), ("normal", "normal"),
          ("dish", "dish, dishes"), ("make", "make"), ("delicious", "delicious"), ("dumpling", "dumpling, dumplings"), ("common", "common"),
          ("plenty", "plenty"), ("piece", "piece"), ("bit", "a bit")],
         "太棒了！下次去餐厅，试着用英语点一道菜吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
