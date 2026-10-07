import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep23", "numbers", "数字 20–100", 23, "n100")
W = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
IPA = ["/ˈtwenti/", "/ˈθɜːrti/", "/ˈfɔːrti/", "/ˈfɪfti/", "/ˈsɪksti/", "/ˈsevnti/", "/ˈeɪti/", "/ˈnaɪnti/"]
ZH = ["二十", "三十", "四十", "五十", "六十", "七十", "八十", "九十"]
TEEN = [None, "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
L.node("zero", "zero", "/ˈzɪroʊ/", "零", icon="n0", kind="num")
for i, w in enumerate(W):
    extra = dict(alt=TEEN[i], altLabel="别混") if TEEN[i] else {}
    L.node(w, w, IPA[i], ZH[i], icon=f"n{(i + 2) * 10}", kind="num", **extra)
L.node("hundred", "one hundred", "/wʌn ˈhʌndrəd/", "一百", icon="n100", kind="num")
L.grid(["zero twenty thirty",
        "sixty fifty forty",
        "seventy eighty ninety",
        ". hundred ."], dy=370)
for id, x, y in [("zero", 180, 190), ("twenty", 540, 190), ("thirty", 900, 190), ("forty", 1260, 190), ("fifty", 1620, 190),
                 ("sixty", 1620, 650), ("seventy", 1260, 650), ("eighty", 900, 650), ("ninety", 540, 650), ("hundred", 180, 650)]:
    L.byid[id]["at"] = [x, y]
seq = ["zero"] + W + ["hundred"]
for a, b in zip(seq, seq[1:]):
    L.edge(a, b, "+10" if a == "twenty" else None)

L.seg("title", zh("小朋友们好！我们已经会从一数到十九了。今天，我们来学更大的数，一直数到一百！"), en("one hundred"))
L.seg("map show:zero focus:zero", zh("先从什么都没有开始。零，英语是"), en("zero"), en("zero apples"))
L.seg("show:twenty edge:zero>twenty focus:twenty", zh("两只手加两只脚，二十根手指脚趾，是二十："), en("twenty"),
      zh("后面的 t y，表示几个十。"))
L.seg("show:thirty edge:twenty>thirty focus:thirty", zh("三十，和十三一样，前面变成 t h i r："), en("thirty"),
      zh("可千万别和十三搞混了：", "alt:thirty"), en("thirteen", "focus:thirty"), en("thirty"),
      zh("十几，后面是长长的 teen，重音在后面；几十，后面是短短的 ty，重音在前面。"))
L.seg("show:forty edge:thirty>forty focus:forty alt:forty", zh("四十要特别小心。四是 f o u r，可四十没有 u："), en("forty"),
      zh("比一比："), en("fourteen, forty"))
L.seg("show:fifty edge:forty>fifty focus:fifty alt:fifty", zh("五十，和十五一样，前面变成 f i f："), en("fifty"), en("fifteen, fifty"))
L.seg("show:sixty edge:fifty>sixty focus:sixty alt:sixty", zh("六十："), en("sixty"), en("sixteen, sixty"))
L.seg("show:seventy edge:sixty>seventy focus:seventy alt:seventy", zh("七十："), en("seventy"), en("seventeen, seventy"))
L.seg("show:eighty edge:seventy>eighty focus:eighty alt:eighty", zh("八十，只有一个字母 t："), en("eighty"), en("eighteen, eighty"))
L.seg("show:ninety edge:eighty>ninety focus:ninety alt:ninety", zh("九十，九后面的 e 要留着："), en("ninety"), en("nineteen, ninety"))
L.seg("show:hundred edge:ninety>hundred focus:hundred", zh("九十再加十，就到了一百！"), en("one hundred"),
      en("one hundred days"))
L.seg("focus:none", zh("我们来整十整十地数一遍吧！"))
L.seg("", *[en(w, "focus:" + w) for w in ["zero"] + W] + [en("one hundred!", "focus:hundred")])
L.seg("focus:thirty,forty,fifty", zh("仔细听，十几和几十的读音不一样："),
      en("thirteen, thirty", "focus:thirty"), en("fourteen, forty", "focus:forty"), en("fifteen, fifty", "focus:fifty"))
L.seg("focus:none", zh("几十和几个合在一起，中间加一个短横线就好啦。比如二十一："), en("twenty-one", "focus:twenty"),
      zh("九十九："), en("ninety-nine", "focus:ninety"))
L.seg("focus:none", zh("考考你：五十加五十，等于几？"))
L.seg("focus:hundred", zh("答对了！是"), en("one hundred"), en("Fifty plus fifty is one hundred."))
L.review([("zero", "zero")] + [(w, w) for w in W] + [("hundred", "one hundred")],
         "太棒了！试着用英语数一数，你能一口气数到一百吗？点一点图上的数字，还能再听一遍发音哦。")
L.save()
