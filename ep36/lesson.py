import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep36", "week", "星期", 36, "week")
L.node("week", "week", "/wiːk/", "星期；周")
D = [("monday", "Monday", "/ˈmʌndeɪ/", "星期一"), ("tuesday", "Tuesday", "/ˈtuːzdeɪ/", "星期二"), ("wednesday", "Wednesday", "/ˈwenzdeɪ/", "星期三"),
     ("thursday", "Thursday", "/ˈθɜːrzdeɪ/", "星期四"), ("friday", "Friday", "/ˈfraɪdeɪ/", "星期五"), ("saturday", "Saturday", "/ˈsætərdeɪ/", "星期六"),
     ("sunday", "Sunday", "/ˈsʌndeɪ/", "星期日")]
for id, w, ipa, z in D:
    L.node(id, w, ipa, z)
L.node("weekday", "weekday", "/ˈwiːkdeɪ/", "工作日")
L.node("weekend", "weekend", "/ˈwiːkend/", "周末")
L.node("before", "before", "/bɪˈfɔːr/", "在……之前", kind="prep")
L.node("after", "after", "/ˈæftər/", "在……之后", kind="prep")
L.node("on", "on", "/ɑːn/", "在（某天）", kind="prep")
L.grid(["monday tuesday wednesday",
        "thursday friday weekday",
        "saturday sunday weekend",
        "on week .",
        "before . after"], dy=330)
for id, x, y in [("monday", 200, 120), ("tuesday", 470, 120), ("wednesday", 740, 120), ("thursday", 1010, 120), ("friday", 1280, 120),
                 ("saturday", 1010, 440), ("sunday", 1280, 440), ("weekday", 1600, 120), ("weekend", 1600, 440),
                 ("week", 470, 440), ("on", 200, 440), ("before", 470, 780), ("after", 1010, 780)]:
    L.byid[id]["at"] = [x, y]
seq = [d[0] for d in D]
for a, b in zip(seq, seq[1:]):
    if (a, b) != ("friday", "saturday"): L.edge(a, b)
L.edge("friday", "weekday"); L.edge("sunday", "weekend"); L.edge("week", "on", dashed=True)

L.seg("title", zh("小朋友们好！一个星期有七天。今天，我们来学星期！"), en("week"))
L.seg("map show:week focus:week", zh("七天，就是一个星期："), en("week"), en("seven days in a week"),
      zh("小提示：英语里每一天的名字，开头都要大写，后面都有一个"), en("day"))
L.seg("show:monday focus:monday", zh("新的一周，从星期一开始："), en("Monday"))
L.seg("show:tuesday edge:monday>tuesday focus:tuesday", zh("星期二："), en("Tuesday"))
L.seg("show:wednesday edge:tuesday>wednesday focus:wednesday", zh("星期三，它最难拼。中间的 d 不发音哦："), en("Wednesday"))
L.seg("show:thursday edge:wednesday>thursday focus:thursday", zh("星期四，开头的 t h，舌尖放在牙齿中间："), en("Thursday"))
L.seg("show:friday edge:thursday>friday focus:friday", zh("星期五："), en("Friday"))
L.seg("show:weekday edge:friday>weekday focus:weekday", zh("星期一到星期五，大人上班、小朋友上学，叫工作日。星期，加上天："),
      en("week"), en("day"), en("weekday"))
L.seg("show:saturday focus:saturday", zh("星期六："), en("Saturday"))
L.seg("show:sunday edge:saturday>sunday focus:sunday", zh("星期日。还记得太阳 sun 吗？太阳的一天："), en("Sunday"))
L.seg("show:weekend edge:sunday>weekend focus:weekend", zh("星期六和星期日，是周末。星期，加上结尾："), en("week"), en("end"), en("weekend"),
      en("Happy weekend!"))
L.seg("show:on edge:week>on focus:on", zh("说在星期几做什么，前面要用小词"), en("on"), en("on Monday"), en("on Sunday"))
L.seg("show:before focus:before", zh("在……之前，英语是"), en("before"), en("Tuesday is before Wednesday."))
L.seg("show:after focus:after", zh("在……之后，英语是"), en("after"), en("Saturday is after Friday."))
L.seg("focus:none", zh("我们从星期一读到星期日吧！"))
L.seg("", *[en(w, "focus:" + id) for id, w, _, _ in D])
L.seg("focus:none", zh("考考你：星期三的后面是星期几？"))
L.seg("focus:thursday", zh("是"), en("Thursday!"), en("Thursday is after Wednesday."))
L.review([("week", "week")] + [(id, w) for id, w, _, _ in D] + [("weekday", "weekday"), ("weekend", "weekend"), ("on", "on"),
          ("before", "before"), ("after", "after")],
         "太棒了！每天早上，用英语说一说今天是星期几吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
