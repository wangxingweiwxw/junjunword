import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep81", "time", "时间（二）", 81, "century")
A, P = dict(kind="adj"), dict(kind="prep")
L.node("year", "year", "/jɪr/", "年")
L.node("recent", "recent", "/ˈriːsnt/", "最近的", **A)
L.node("ago", "ago", "/əˈɡoʊ/", "……以前", kind="adv")
L.node("century", "century", "/ˈsentʃəri/", "世纪")
L.node("ancient", "ancient", "/ˈeɪnʃənt/", "古代的", **A)
L.node("upon", "upon", "/əˈpɑːn/", "在……之上", **P)
L.node("while", "while", "/waɪl/", "在……的时候", kind="adv")
L.node("period", "period", "/ˈpɪriəd/", "时期")
L.node("age", "age", "/eɪdʒ/", "时代", icon="era")
L.node("begin", "begin", "/bɪˈɡɪn/", "开始", kind="verb")
L.node("beginning", "beginning", "/bɪˈɡɪnɪŋ/", "开头")
L.node("end", "end", "/end/", "结束", kind="verb")
L.node("ending", "ending", "/ˈendɪŋ/", "结尾")
L.grid(["recent year ago",
        "upon century ancient",
        "while period age",
        "begin . end",
        "beginning . ending"], dy=330)
L.edge("year", "recent"); L.edge("year", "ago"); L.edge("year", "century", "×100"); L.edge("century", "ancient", dashed=True); L.edge("ancient", "upon", dashed=True)
L.edge("ancient", "period", dashed=True); L.edge("period", "age"); L.edge("period", "while", dashed=True); L.edge("begin", "beginning", "+ning"); L.edge("end", "ending", "+ing")

L.seg("title", zh("小朋友们好！时间过得真快。今天，我们来学和时间有关的更多单词。"), en("time"))
L.seg("map show:year focus:year", zh("一年，英语是"), en("year"), en("This year, I am eight."))
L.seg("show:recent edge:year>recent focus:recent", zh("最近的，英语是"), en("recent"))
L.seg("show:ago edge:year>ago focus:ago", zh("……以前，放在时间的后面："), en("ago"), en("two years ago"))
L.seg("show:century edge:year>century focus:century", zh("一百年，是一个世纪："), en("century"), zh("开头的 cent，和一百有关，就像一百分 per cent。"))
L.seg("show:ancient edge:century>ancient focus:ancient", zh("很多很多个世纪以前，是古代的："), en("ancient"), en("ancient China"))
L.seg("show:upon edge:ancient>upon focus:upon", zh("讲古老的故事时，常常这样开头："), en("Once upon a time…"), zh("upon 的意思和 on 差不多。"))
L.seg("show:period edge:ancient>period focus:period", zh("一段时间，是时期："), en("period"))
L.seg("show:age edge:period>age focus:age", zh("一个很长很长的时期，叫时代："), en("age"), zh("还记得第十二集的年龄吗？同一个词！"))
L.seg("show:while edge:period>while focus:while", zh("在……的时候，英语是"), en("while"), en("I listen to music while I read."))
L.seg("show:begin focus:begin", zh("开始，是"), en("begin"))
L.seg("show:beginning edge:begin>beginning focus:beginning", zh("故事的开头。要多写一个 n，再加 i n g："), en("beginning"))
L.seg("show:end focus:end", zh("结束，是"), en("end"))
L.seg("show:ending edge:end>ending focus:ending", zh("故事的结尾："), en("ending"), en("a happy ending"))
L.seg("focus:begin,end", zh("开始和结束："), en("begin, beginning", "focus:begin,beginning"), en("end, ending", "focus:end,ending"))
L.review([("year", "year"), ("recent", "recent"), ("ago", "ago"), ("century", "century"), ("ancient", "ancient"), ("upon", "upon"), ("period", "period"),
          ("age", "age"), ("while", "while"), ("begin", "begin"), ("beginning", "beginning"), ("end", "end"), ("ending", "ending")],
         "太棒了！用 Once upon a time 开头，给爸爸妈妈讲一个小故事吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
