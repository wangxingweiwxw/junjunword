import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep65", "health", "健康", 65, "health")
A, V = dict(kind="adj"), dict(kind="verb")
L.node("health", "health", "/helθ/", "健康")
L.node("healthy", "healthy", "/ˈhelθi/", "健康的", **A)
L.node("advise", "advise", "/ədˈvaɪz/", "建议", **V)
L.node("advice", "advice", "/ədˈvaɪs/", "建议（名词）")
L.node("exercise", "exercise", "/ˈeksərsaɪz/", "锻炼", **V)
L.node("active", "active", "/ˈæktɪv/", "活跃的", **A)
L.node("keep", "keep", "/kiːp/", "保持", **V)
L.node("habit", "habit", "/ˈhæbɪt/", "习惯")
L.node("fat", "fat", "/fæt/", "胖的", **A)
L.node("fit", "fit", "/fɪt/", "健壮的", **A)
L.grid(["advise health healthy",
        "advice . keep",
        "exercise active habit",
        "fat . fit"], dy=360)
L.edge("health", "healthy", "+y"); L.edge("health", "advise"); L.edge("advise", "advice", "s→c"); L.edge("healthy", "keep")
L.edge("advice", "exercise", dashed=True); L.edge("exercise", "active"); L.edge("keep", "habit", dashed=True); L.edge("exercise", "fat", dashed=True); L.edge("active", "fit", dashed=True)

L.seg("title", zh("小朋友们好！身体是最宝贵的。今天，我们来学和健康有关的单词。"), en("health"))
L.seg("map show:health focus:health", zh("健康，英语是"), en("health"), zh("最后的 t h，舌尖放在牙齿中间。"))
L.seg("show:healthy edge:health>healthy focus:healthy", zh("加上 y，就是健康的："), en("healthy"), en("Eat healthy food."))
L.seg("show:advise edge:health>advise focus:advise", zh("医生给我们提建议："), en("advise"))
L.seg("show:advice edge:advise>advice focus:advice", zh("医生说的建议本身，把 s 换成 c："), en("advice"),
      zh("仔细听，一个读 z，一个读 s："), en("advise", "focus:advise"), en("advice", "focus:advice"))
L.seg("show:exercise edge:advice>exercise focus:exercise", zh("医生建议我们多锻炼："), en("exercise"), en("I exercise every evening."))
L.seg("show:active edge:exercise>active focus:active", zh("爱运动、跑来跑去，是活跃的："), en("active"))
L.seg("show:fit edge:active>fit focus:fit", zh("经常锻炼，身体就很健壮："), en("fit"), en("The actor is very fit."))
L.seg("show:fat edge:exercise>fat focus:fat", zh("吃太多、又不运动，就会变胖："), en("fat"), zh("胖和健壮，只差一个字母："), en("fat", "focus:fat"), en("fit", "focus:fit"))
L.seg("show:keep edge:healthy>keep focus:keep", zh("要一直保持健康："), en("keep"), en("Keep healthy!"))
L.seg("show:habit edge:keep>habit focus:habit", zh("每天都坚持做的事，就成了习惯："), en("habit"), en("a good habit"))
L.seg("focus:none", zh("说一说你的好习惯吧！"))
L.seg("", en("I exercise every day.", "focus:exercise"), en("I eat fruit and vegetables.", "focus:healthy"), en("I keep healthy!", "focus:keep,healthy"))
L.review([("health", "health"), ("healthy", "healthy"), ("advise", "advise"), ("advice", "advice"), ("exercise", "exercise"), ("active", "active"),
          ("fit", "fit"), ("fat", "fat"), ("keep", "keep"), ("habit", "habit")],
         "太棒了！每天锻炼一会儿，养成健康的好习惯吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
