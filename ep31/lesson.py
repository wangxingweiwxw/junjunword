import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep31", "compare", "比较", 31, "compare")
A, AD = dict(kind="adj"), dict(kind="adv")
L.node("compare", "compare", "/kəmˈper/", "比较", kind="verb")
L.node("same", "same", "/seɪm/", "相同的", **A)
L.node("different", "different", "/ˈdɪfrənt/", "不同的", **A)
L.node("as", "as", "/æz/", "和……一样", kind="prep", alt="as…as", altLabel="句型")
L.node("good", "good", "/ɡʊd/", "好的", **A)
L.node("well", "well", "/wel/", "好地", **AD)
L.node("bad", "bad", "/bæd/", "坏的；差的", **A)
L.node("badly", "badly", "/ˈbædli/", "差地", **AD)
L.node("quite", "quite", "/kwaɪt/", "相当", **AD)
L.node("cool", "cool", "/kuːl/", "酷的；凉爽的", **A)
L.node("great", "great", "/ɡreɪt/", "棒极了", **A)
L.grid(["same compare different",
        ". as .",
        "great good cool",
        "well quite bad",
        ". . badly"], dy=330)
L.edge("compare", "same"); L.edge("compare", "different"); L.edge("compare", "as")
L.edge("good", "well", "+做事"); L.edge("bad", "badly", "+ly"); L.edge("quite", "good", dashed=True); L.edge("quite", "bad", dashed=True)
L.edge("good", "great", "更好"); L.edge("good", "cool", "也可以说")

L.seg("title", zh("小朋友们好！两只小狗站在一起，它们一样吗？今天，我们来学比较。"), en("compare"))
L.seg("map show:compare focus:compare", zh("把两样东西放在一起，看一看哪里一样、哪里不一样，就是比较："), en("compare"))
L.seg("show:same edge:compare>same focus:same", zh("长得一模一样，是相同的："), en("same"), en("They look the same."))
L.seg("show:different edge:compare>different focus:different", zh("颜色不一样，是不同的："), en("different"), en("They are different."))
L.seg("focus:same,different", zh("一样，和不一样："), en("same", "focus:same"), en("different", "focus:different"))
L.seg("show:as edge:compare>as focus:as", zh("说两样东西一样高、一样好，要用小词"), en("as"),
      zh("两个 as 中间夹一个词：", "alt:as"), en("as tall as"), en("I am as tall as you."))
L.seg("show:good focus:good", zh("夸一样东西，最常说好的："), en("good"), en("a good book"))
L.seg("show:well edge:good>well focus:well", zh("说一个人把事情做得好，要换成"), en("well"), zh("这个词很特别，它不加 l y。"),
      en("I sing well."), en("I play guitar as well as you do.", "focus:well,as"))
L.seg("show:bad focus:bad", zh("好的反面，是坏的、差的："), en("bad"), en("a bad day"))
L.seg("show:badly edge:bad>badly focus:badly", zh("事情做得差，在后面加上 l y："), en("badly"), en("I sing badly."))
L.seg("focus:good,well,bad,badly", zh("比一比："), en("good, well", "focus:good,well"), en("bad, badly", "focus:bad,badly"))
L.seg("show:quite edge:quite>good edge:quite>bad focus:quite", zh("说一样东西挺好、相当好，可以在前面加上"), en("quite"),
      en("quite good"), zh("小心，别和安静 quiet 搞混了，字母的顺序不一样。"))
L.seg("show:great edge:good>great focus:great", zh("比好还要好，是棒极了："), en("great"), en("Great job!"))
L.seg("show:cool edge:good>cool focus:cool", zh("酷的，英语是"), en("cool"), zh("它也是凉爽的意思。"), en("That's so cool!"))
L.seg("focus:good,great,cool", zh("夸奖别人的话，一起来喊："), en("Good!", "focus:good"), en("Great!", "focus:great"), en("Cool!", "focus:cool"))
L.review([("compare", "compare"), ("same", "same"), ("different", "different"), ("as", "as"), ("good", "good"), ("well", "well"),
          ("bad", "bad"), ("badly", "badly"), ("quite", "quite"), ("great", "great"), ("cool", "cool")],
         "太棒了！找两样东西，用英语比一比它们一样还是不一样吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
