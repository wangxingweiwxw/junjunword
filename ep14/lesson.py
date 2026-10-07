import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep14", "time", "时间", 14, "clock")
L.node("day", "day", "/deɪ/", "一天；白天", plural="days", pluralIpa="/deɪz/")
L.node("morning", "morning", "/ˈmɔːrnɪŋ/", "早上；上午")
L.node("noon", "noon", "/nuːn/", "中午")
L.node("afternoon", "afternoon", "/ˌæftərˈnuːn/", "下午", alt="after + noon", altLabel="=")
L.node("evening", "evening", "/ˈiːvnɪŋ/", "傍晚；晚上")
L.node("night", "night", "/naɪt/", "夜晚")
L.node("midnight", "midnight", "/ˈmɪdnaɪt/", "半夜", alt="mid + night", altLabel="=")
L.node("time", "time", "/taɪm/", "时间")
L.node("clock", "clock", "/klɑːk/", "钟")
L.node("oclock", "o'clock", "/əˈklɑːk/", "……点钟", kind="adv")
L.node("at", "at", "/æt/", "在（某时刻）", kind="prep")
L.node("hour", "hour", "/ˈaʊər/", "小时", plural="hours", pluralIpa="/ˈaʊərz/")
L.node("minute", "minute", "/ˈmɪnɪt/", "分钟", plural="minutes", pluralIpa="/ˈmɪnɪts/")
L.node("second", "second", "/ˈsekənd/", "秒", plural="seconds", pluralIpa="/ˈsekəndz/")
L.grid(["day morning noon",
        "evening . afternoon",
        "night midnight at",
        "time clock oclock",
        "hour minute second"], dy=340)
# landscape: the day cycle runs along the top two rows, the clock family underneath
for id, x, y in [("day", 180, 150), ("morning", 540, 150), ("noon", 900, 150), ("afternoon", 1260, 150), ("evening", 1620, 150),
                 ("time", 180, 470), ("clock", 540, 470), ("oclock", 900, 470), ("midnight", 1260, 470), ("night", 1620, 470),
                 ("hour", 180, 790), ("minute", 540, 790), ("second", 900, 790), ("at", 1260, 790)]:
    L.byid[id]["at"] = [x, y]
L.edge("day", "morning"); L.edge("morning", "noon"); L.edge("noon", "afternoon", "after"); L.edge("afternoon", "evening")
L.edge("evening", "night"); L.edge("night", "midnight", "mid")
L.edge("time", "clock"); L.edge("clock", "oclock"); L.edge("clock", "hour"); L.edge("clock", "minute"); L.edge("clock", "second")
L.edge("at", "oclock", dashed=True); L.edge("at", "midnight", dashed=True)

L.seg("title", zh("小朋友们好！嘀嗒嘀嗒，你听，是什么在响？今天，我们来学时间。"), en("time"), zh("时间。"))
L.seg("map show:day focus:day", zh("太阳升起又落下，就是一天："), en("day"), en("Have a nice day!"))
L.seg("show:morning edge:day>morning focus:morning", zh("太阳刚刚升起，是早上："), en("morning"), en("Good morning!"))
L.seg("show:noon edge:morning>noon focus:noon", zh("太阳升到头顶，影子变得最短，是中午："), en("noon"), zh("中间是两个字母 o。"))
L.seg("show:afternoon edge:noon>afternoon focus:afternoon", zh("中午过后，就是下午。在……之后，加上中午：", "alt:afternoon"),
      en("after"), en("noon"), en("afternoon"), en("Good afternoon!"))
L.seg("show:evening edge:afternoon>evening focus:evening", zh("太阳慢慢落山，天边红红的，是傍晚："), en("evening"), en("Good evening!"))
L.seg("show:night edge:evening>night focus:night", zh("月亮和星星出来了，是夜晚："), en("night"),
      zh("还记得吗？g h 又不发音了。睡觉前，我们说："), en("Good night!"))
L.seg("show:midnight edge:night>midnight focus:midnight", zh("夜里最深最深的时候，大家都睡着了，是半夜。中间，加上夜晚：", "alt:midnight"),
      en("mid"), en("night"), en("midnight"))
L.seg("focus:morning,afternoon,evening,night", zh("见面打招呼，要看是什么时候："),
      en("Good morning!", "focus:morning"), en("Good afternoon!", "focus:afternoon"), en("Good evening!", "focus:evening"),
      zh("晚上道别、睡觉前，才说", "focus:night"), en("Good night!"))
L.seg("show:time focus:time", zh("一分一秒地过去，看不见也摸不着的，是时间："), en("time"), en("What time is it?"))
L.seg("show:clock edge:time>clock focus:clock", zh("想知道时间，就看看钟："), en("clock"), en("Look at the clock."))
L.seg("show:oclock edge:clock>oclock focus:oclock", zh("长针指着十二，短针指着三，就是三点整。整点，要说"), en("o'clock"),
      en("three o'clock"), zh("它只能用在整点哦。"))
L.seg("show:at edge:at>oclock edge:at>midnight focus:at", zh("在几点钟做一件事，前面要加上小词"), en("at"),
      en("at three o'clock", "focus:at,oclock"), en("at midnight", "focus:at,midnight"),
      en("I have a party at four o'clock.", "focus:at,oclock"))
L.seg("show:hour edge:clock>hour focus:hour", zh("钟上的短针走一大格，就是一个小时："), en("hour"),
      zh("小提示：开头的 h 不发音，所以前面要用"), en("an hour"))
L.seg("show:minute edge:clock>minute focus:minute", zh("长针走一小格，是一分钟："), en("minute"), en("Wait a minute!"))
L.seg("show:second edge:clock>second focus:second", zh("细细的秒针嗒地跳一下，是一秒："), en("second"),
      zh("这个词还有一个意思：第二。"))
L.seg("focus:hour,minute,second", zh("我们从大到小排一排："), en("hour", "focus:hour"), en("minute", "focus:minute"), en("second", "focus:second"),
      zh("一小时有六十分钟，一分钟有六十秒：", "focus:hour,minute"), en("sixty minutes in an hour"), en("sixty seconds in a minute", "focus:minute,second"))
L.seg("focus:hour", zh("很多个，在后面加上字母 s："),
      en("hours", "plural:hour"), en("minutes", "plural:minute focus:minute"), en("seconds", "plural:second focus:second"), en("days", "plural:day focus:day"))
L.seg("focus:none", zh("我们来说一说，小明的一天吧！"))
L.seg("", en("I get up at seven o'clock in the morning.", "focus:morning,oclock"),
      en("I eat lunch at noon.", "focus:noon"), en("I play in the afternoon.", "focus:afternoon"),
      en("I go to bed at nine o'clock at night.", "focus:night,oclock"))
L.review([("day", "day, days"), ("morning", "morning"), ("noon", "noon"), ("afternoon", "afternoon"), ("evening", "evening"),
          ("night", "night"), ("midnight", "midnight"), ("time", "time"), ("clock", "clock"), ("oclock", "o'clock"), ("at", "at"),
          ("hour", "hour, hours"), ("minute", "minute, minutes"), ("second", "second, seconds")],
         "太棒了！今天晚上，看着钟，用英语说一说现在几点了吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
