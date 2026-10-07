import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep60", "months", "月份", 60, "month")
M = [("january", "January", "/ˈdʒænjueri/"), ("february", "February", "/ˈfebrueri/"), ("march", "March", "/mɑːrtʃ/"), ("april", "April", "/ˈeɪprəl/"),
     ("may", "May", "/meɪ/"), ("june", "June", "/dʒuːn/"), ("july", "July", "/dʒuˈlaɪ/"), ("august", "August", "/ˈɔːɡəst/"),
     ("september", "September", "/sepˈtembər/"), ("october", "October", "/ɑːkˈtoʊbər/"), ("november", "November", "/noʊˈvembər/"), ("december", "December", "/dɪˈsembər/")]
L.node("month", "month", "/mʌnθ/", "月；月份")
L.node("date", "date", "/deɪt/", "日期")
L.node("in", "in", "/ɪn/", "在（某月）", kind="prep", icon="inmonth")
for i, (id, w, ipa) in enumerate(M):
    L.node(id, w, ipa, f"{i + 1}月")
L.grid(["month date in",
        "january february march",
        "april may june",
        "july august september",
        "october november december"], dy=330)
for i, (id, _, _) in enumerate(M):
    L.byid[id]["at"] = [540 + (i % 4) * 360, 150 + (i // 4) * 320]
for id, y in [("month", 150), ("date", 470), ("in", 790)]:
    L.byid[id]["at"] = [170, y]
for i in range(11):
    if i % 4 != 3: L.edge(M[i][0], M[i + 1][0])
L.edge("month", "january", dashed=True); L.edge("in", "september", dashed=True)

L.seg("title", zh("小朋友们好！一年有十二个月。今天，我们来学月份！"), en("months"))
L.seg("map show:month focus:month", zh("一个月，英语是"), en("month"), en("twelve months in a year"),
      zh("小提示：每个月份的名字，开头都要大写。"))
L.seg("show:january edge:month>january focus:january", zh("新年的第一个月，一月："), en("January"))
L.seg("show:february edge:january>february focus:february", zh("二月，中间的第一个 r 常常读得很轻："), en("February"))
L.seg("show:march edge:february>march focus:march", zh("三月，春天来了："), en("March"))
L.seg("show:april edge:march>april focus:april", zh("四月，常常下小雨："), en("April"))
L.seg("show:may edge:april>may focus:may", zh("五月，花儿开了："), en("May"))
L.seg("show:june edge:may>june focus:june", zh("六月，夏天到了："), en("June"))
L.seg("show:july edge:june>july focus:july", zh("七月，重音在后面："), en("July"))
L.seg("show:august edge:july>august focus:august", zh("八月，可以去海边玩水："), en("August"))
L.seg("show:september focus:september", zh("九月，开学啦："), en("September"))
L.seg("show:october edge:september>october focus:october", zh("十月，秋天的南瓜熟了："), en("October"))
L.seg("show:november edge:october>november focus:november", zh("十一月，树叶落下来："), en("November"))
L.seg("show:december edge:november>december focus:december", zh("十二月，一年的最后一个月："), en("December"),
      zh("你发现了吗？九月到十二月，后面都带着 b e r。"))
L.seg("show:date focus:date", zh("几月几号，是日期："), en("date"), en("What's the date today?"), en("It's March tenth.", "focus:date,march"),
      zh("说几号，要用上一集学的序数词哦。"))
L.seg("show:in edge:in>september focus:in", zh("在几月，前面要用小词"), en("in"), en("in September"), en("My birthday is in May.", "focus:in,may"))
L.seg("focus:none", zh("我们从一月读到十二月吧！"))
L.seg("", *[en(w, "focus:" + id) for id, w, _ in M])
L.review([("month", "month"), ("date", "date"), ("in", "in")] + [(id, w) for id, w, _ in M],
         "太棒了！你的生日在几月？用英语告诉爸爸妈妈吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
