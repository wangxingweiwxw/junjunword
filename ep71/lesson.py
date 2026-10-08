import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep71", "maths", "数学", 71, "add")
V, AD = dict(kind="verb"), dict(kind="adv")
L.node("thousand", "thousand", "/ˈθaʊznd/", "千", kind="num")
L.node("million", "million", "/ˈmɪljən/", "百万", kind="num")
L.node("add", "add", "/æd/", "加", **V)
L.node("total", "total", "/ˈtoʊtl/", "总数；总共")
L.node("double", "double", "/ˈdʌbl/", "加倍；两倍", **V)
L.node("reduce", "reduce", "/rɪˈduːs/", "减少", **V)
L.node("divide", "divide", "/dɪˈvaɪd/", "除；分开", **V)
L.node("percent", "percent", "/pərˈsent/", "百分之……")
L.node("about", "about", "/əˈbaʊt/", "大约", **AD)
L.node("once", "once", "/wʌns/", "一次", **AD)
L.node("twice", "twice", "/twaɪs/", "两次", **AD)
L.node("dozen", "dozen", "/ˈdʌzn/", "一打（十二个）")
L.grid(["thousand million about",
        "add total double",
        "reduce divide percent",
        "once twice dozen"], dy=350)
L.edge("thousand", "million", "×1000"); L.edge("million", "about", dashed=True); L.edge("add", "total", "得到"); L.edge("add", "double", dashed=True)
L.edge("reduce", "divide", dashed=True); L.edge("divide", "percent", dashed=True); L.edge("once", "twice")

L.seg("title", zh("小朋友们好！数学课开始啦！今天，我们用英语来算一算。"), en("maths"))
L.seg("map show:thousand focus:thousand", zh("还记得第二十三集的一百吗？十个一百，就是一千："), en("thousand"), en("one thousand"))
L.seg("show:million edge:thousand>million focus:million", zh("一千个一千，就是一百万："), en("million"), en("one million"))
L.seg("show:about edge:million>about focus:about", zh("九百九十九乘以九百九十九，大约是一百万。大约，英语是"), en("about"), en("about a million"))
L.seg("show:add focus:add", zh("加法的加，是"), en("add"), en("One thousand add one thousand is two thousand."))
L.seg("show:total edge:add>total focus:total", zh("加起来的总数，是"), en("total"), en("The total is seven."))
L.seg("show:double edge:add>double focus:double", zh("一个变成两个一样的，是加倍："), en("double"), en("Double one thousand is two thousand."))
L.seg("show:reduce focus:reduce", zh("减少，英语是"), en("reduce"), en("Reduce two thousand by one thousand."))
L.seg("show:divide edge:reduce>divide focus:divide", zh("除法的除，也是分开的意思："), en("divide"), en("One divided by two is zero point five."))
L.seg("show:percent edge:divide>percent focus:percent", zh("零点五，也就是百分之五十："), en("percent"), en("fifty percent"))
L.seg("show:once focus:once", zh("一次，英语是"), en("once"), zh("它可不是 one times 哦。"))
L.seg("show:twice edge:once>twice focus:twice", zh("两次，是"), en("twice"), en("I brush my teeth twice a day."))
L.seg("show:dozen focus:dozen", zh("十二个一组，叫一打："), en("dozen"), en("a dozen eggs"))
L.seg("focus:none", zh("来做几道口算题吧！"))
L.seg("", en("Five add five is ten.", "focus:add"), en("Double ten is twenty.", "focus:double"), en("A dozen is twelve.", "focus:dozen"))
L.review([("thousand", "thousand"), ("million", "million"), ("about", "about"), ("add", "add"), ("total", "total"), ("double", "double"),
          ("reduce", "reduce"), ("divide", "divide"), ("percent", "percent"), ("once", "once"), ("twice", "twice"), ("dozen", "dozen")],
         "太棒了！做数学作业的时候，试着用英语读一读算式吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
