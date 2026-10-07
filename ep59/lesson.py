import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep59", "order", "顺序", 59, "ord1")
W = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
IPA = ["/fɜːrst/", "/ˈsekənd/", "/θɜːrd/", "/fɔːrθ/", "/fɪfθ/", "/sɪksθ/", "/ˈsevnθ/", "/eɪtθ/", "/naɪnθ/", "/tenθ/"]
ZH = ["第一", "第二", "第三", "第四", "第五", "第六", "第七", "第八", "第九", "第十"]
BASE = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
L.node("order", "order", "/ˈɔːrdər/", "顺序")
for i, w in enumerate(W):
    L.node(w, w, IPA[i], ZH[i], icon=f"ord{i + 1}", kind="num", alt=BASE[i], altLabel="来自")
L.node("next", "next", "/nekst/", "下一个", kind="adj")
L.node("last", "last", "/læst/", "最后的", kind="adj")
L.grid(["order next last",
        "first second third",
        "sixth fifth fourth",
        "seventh eighth ninth",
        ". tenth ."], dy=360)
for id, x, y in [("order", 180, 120), ("next", 900, 120), ("last", 1620, 120),
                 ("first", 180, 420), ("second", 540, 420), ("third", 900, 420), ("fourth", 1260, 420), ("fifth", 1620, 420),
                 ("sixth", 1620, 780), ("seventh", 1260, 780), ("eighth", 900, 780), ("ninth", 540, 780), ("tenth", 180, 780)]:
    L.byid[id]["at"] = [x, y]
for a, b in zip(W, W[1:]):
    L.edge(a, b)
L.edge("order", "first", dashed=True)

L.seg("title", zh("小朋友们好！赛跑比赛，谁是第一名？今天，我们来学排顺序！"), en("order"))
L.seg("map show:order focus:order", zh("一个接一个地排好，是顺序："), en("order"), en("in order"))
L.seg("focus:none", zh("第一、第二、第三最特别，要单独记住。"))
L.seg("show:first focus:first", zh("第一名，是"), en("first"), zh("它和 one 长得一点也不像。"))
L.seg("show:second edge:first>second focus:second", zh("第二名，是"), en("second"), zh("还记得第十四集吗？它也是秒的意思。"))
L.seg("show:third edge:second>third focus:third", zh("第三名，是"), en("third"))
L.seg("focus:none", zh("从第四开始，就有规律啦：在数字后面加上 t h。"))
L.seg("show:fourth edge:third>fourth focus:fourth alt:fourth", en("four"), en("fourth"))
L.seg("show:fifth edge:fourth>fifth focus:fifth alt:fifth", zh("第五要小心，v e 变成了 f："), en("five"), en("fifth"))
L.seg("show:sixth edge:fifth>sixth focus:sixth alt:sixth", en("six"), en("sixth"))
L.seg("show:seventh edge:sixth>seventh focus:seventh alt:seventh", en("seven"), en("seventh"))
L.seg("show:eighth edge:seventh>eighth focus:eighth alt:eighth", zh("第八，eight 已经有 t 了，只加一个 h："), en("eight"), en("eighth"))
L.seg("show:ninth edge:eighth>ninth focus:ninth alt:ninth", zh("第九，要去掉 nine 最后的 e："), en("nine"), en("ninth"))
L.seg("show:tenth edge:ninth>tenth focus:tenth alt:tenth", en("ten"), en("tenth"))
L.seg("show:next focus:next", zh("下一个，英语是"), en("next"), en("Who's next?"))
L.seg("show:last focus:last", zh("排在最后的，是"), en("last"), en("I'm the last one."))
L.seg("focus:first,second,third", zh("再说一遍最特别的三个："), en("first", "focus:first"), en("second", "focus:second"), en("third", "focus:third"))
L.seg("focus:fifth,eighth,ninth", zh("还有三个要变一变的："), en("fifth", "focus:fifth"), en("eighth", "focus:eighth"), en("ninth", "focus:ninth"))
L.review([("order", "order")] + [(w, w) for w in W] + [("next", "next"), ("last", "last")],
         "太棒了！下次排队的时候，用英语说一说你排第几吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
