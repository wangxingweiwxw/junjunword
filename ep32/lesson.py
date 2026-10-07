import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep32", "time words", "时间词", 32, "today")
L.node("past", "past", "/pæst/", "过去")
L.node("yesterday", "yesterday", "/ˈjestərdeɪ/", "昨天")
L.node("today", "today", "/təˈdeɪ/", "今天")
L.node("tomorrow", "tomorrow", "/təˈmɑːroʊ/", "明天")
L.node("future", "future", "/ˈfjuːtʃər/", "未来")
L.node("tonight", "tonight", "/təˈnaɪt/", "今晚")
L.node("daily", "daily", "/ˈdeɪli/", "每天的", kind="adj", alt="everyday", altLabel="也说")
L.node("allday", "all day", "/ɔːl deɪ/", "一整天")
L.node("since", "since", "/sɪns/", "自从", kind="prep")
L.node("until", "until", "/ənˈtɪl/", "直到", kind="prep", alt="till", altLabel="也说")
L.grid([". past .",
        "daily yesterday since",
        "allday today tonight",
        ". tomorrow until",
        ". future ."], dy=330)
for id, x, y in [("past", 180, 470), ("yesterday", 540, 470), ("today", 900, 470), ("tomorrow", 1260, 470), ("future", 1620, 470),
                 ("daily", 540, 150), ("tonight", 900, 150), ("allday", 1260, 150), ("since", 540, 790), ("until", 1260, 790)]:
    L.byid[id]["at"] = [x, y]
L.edge("past", "yesterday"); L.edge("yesterday", "today"); L.edge("today", "tomorrow"); L.edge("tomorrow", "future")
L.edge("today", "tonight", "晚上"); L.edge("since", "today", dashed=True); L.edge("today", "until", dashed=True)

L.seg("title", zh("小朋友们好！时间像一条长长的线，一直往前走。今天，我们来学时间词。"))
L.seg("map show:today focus:today", zh("我们就站在这条线的中间，今天："), en("today"),
      zh("还记得第十四集的天吗？to 加上 day。"), en("What day is it today?"))
L.seg("show:yesterday edge:yesterday>today focus:yesterday", zh("今天往前一天，是昨天："), en("yesterday"))
L.seg("show:tomorrow edge:today>tomorrow focus:tomorrow", zh("今天往后一天，是明天："), en("tomorrow"),
      zh("小提示：一个 m，两个 r。"), en("See you tomorrow!"))
L.seg("show:past edge:past>yesterday focus:past", zh("昨天、前天、去年，已经过去的时间，都叫过去："), en("past"))
L.seg("show:future edge:tomorrow>future focus:future", zh("明天、后天、明年，还没有来的时间，叫未来："), en("future"), en("in the future"))
L.seg("focus:past,yesterday,today,tomorrow,future", zh("我们沿着时间线，从过去走到未来："),
      *[en(w, "focus:" + w) for w in ["past", "yesterday", "today", "tomorrow", "future"]])
L.seg("show:tonight edge:today>tonight focus:tonight", zh("今天的晚上，就是今晚。to 加上夜晚："), en("tonight"), en("See you tonight."))
L.seg("show:daily focus:daily", zh("每一天都要做的事，是每天的："), en("daily"),
      zh("也可以说", "alt:daily"), en("everyday"), en("my daily life"))
L.seg("show:allday focus:allday", zh("从早到晚，整整一天，是"), en("all day"), en("I play all day."))
L.seg("show:since edge:since>today focus:since", zh("从过去的某个时候开始，一直到现在，用"), en("since"),
      en("since yesterday"))
L.seg("show:until edge:today>until focus:until", zh("一直到将来的某个时候才结束，用"), en("until"),
      zh("短一点的说法是", "alt:until"), en("till"), en("Wait until tomorrow."))
L.seg("focus:since,until", zh("一个从……开始，一个到……为止："), en("since", "focus:since"), en("until", "focus:until"))
L.seg("focus:none", zh("说一说你的一天吧！"))
L.seg("", en("Yesterday, I went to the park.", "focus:yesterday"), en("Today, I am at school.", "focus:today"),
      en("Tomorrow, I will visit Grandma.", "focus:tomorrow"))
L.review([("today", "today"), ("yesterday", "yesterday"), ("tomorrow", "tomorrow"), ("past", "past"), ("future", "future"),
          ("tonight", "tonight"), ("daily", "daily, everyday"), ("allday", "all day"), ("since", "since"), ("until", "until, till")],
         "太棒了！睡觉前，用英语说一说今天做了什么，明天想做什么吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
