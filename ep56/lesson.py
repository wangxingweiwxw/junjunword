import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep56", "holiday", "假日", 56, "festival")
A, V = dict(kind="adj"), dict(kind="verb")
L.node("holiday", "holiday", "/ˈhɑːlədeɪ/", "假日；节日")
L.node("general", "general", "/ˈdʒenrəl/", "普通的；一般的", **A)
L.node("relaxing", "relaxing", "/rɪˈlæksɪŋ/", "令人放松的", **A)
L.node("trip", "trip", "/trɪp/", "旅行；出游")
L.node("away", "away", "/əˈweɪ/", "离开；远离", kind="adv")
L.node("picnic", "picnic", "/ˈpɪknɪk/", "野餐")
L.node("suppose", "suppose", "/səˈpoʊz/", "猜想；认为", **V)
L.node("festival", "festival", "/ˈfestɪvl/", "节日")
L.node("during", "during", "/ˈdʊrɪŋ/", "在……期间", kind="prep")
L.node("visit", "visit", "/ˈvɪzɪt/", "拜访", **V, alt="visitor", altLabel="加 or →")
L.node("come", "come", "/kʌm/", "来", **V, alt="came", altLabel="过去式")
L.node("together", "together", "/təˈɡeðər/", "一起", kind="adv")
L.grid(["general holiday relaxing",
        "picnic trip away",
        "suppose festival during",
        "come visit together"], dy=350)
L.edge("holiday", "general", dashed=True); L.edge("holiday", "relaxing"); L.edge("holiday", "trip"); L.edge("trip", "away"); L.edge("trip", "picnic")
L.edge("picnic", "suppose", dashed=True); L.edge("holiday", "festival", dashed=True); L.edge("festival", "during", dashed=True); L.edge("festival", "visit")
L.edge("visit", "come"); L.edge("visit", "together")

L.seg("title", zh("小朋友们好！放假啦！今天，我们来学和假日有关的单词。"), en("holiday"))
L.seg("map show:holiday focus:holiday", zh("不用上学、不用上班的日子，是假日："), en("holiday"), en("Happy holiday!"))
L.seg("show:general edge:holiday>general focus:general", zh("平常的、一般的日子，英语是"), en("general"), en("a general day"))
L.seg("show:relaxing edge:holiday>relaxing focus:relaxing", zh("假日让人很放松："), en("relaxing"), en("The holiday is relaxing."))
L.seg("show:trip edge:holiday>trip focus:trip", zh("放假了，出去玩一趟："), en("trip"), en("a trip to the beach"))
L.seg("show:away edge:trip>away focus:away", zh("离开家，去远方，是"), en("away"), en("We go away for the holiday."))
L.seg("show:picnic edge:trip>picnic focus:picnic", zh("带上吃的，去公园野餐："), en("picnic"))
L.seg("show:suppose edge:picnic>suppose focus:suppose", zh("明天会下雨吗？我猜想不会："), en("suppose"), en("I suppose it will be sunny."))
L.seg("show:festival edge:holiday>festival focus:festival", zh("春节、中秋节，都是节日："), en("festival"), en("the Spring Festival"))
L.seg("show:during edge:festival>during focus:during", zh("在节日期间，英语是"), en("during"), en("during the festival"))
L.seg("show:visit edge:festival>visit focus:visit", zh("节日里，我们去拜访亲戚："), en("visit"), en("I visit my family during the festival.", "focus:visit,during"),
      zh("加上 o r，就是来拜访的人，客人：", "alt:visit"), en("visitor"))
L.seg("show:come edge:visit>come focus:come", zh("客人来了！来，英语是"), en("come"), zh("已经来了，要说", "alt:come"), en("came"))
L.seg("show:together edge:visit>together focus:together", zh("一家人聚在一起，是"), en("together"), en("We have dinner together."))
L.seg("focus:none", zh("说一说你的假期吧！"))
L.seg("", en("During the holiday, I go on a trip.", "focus:during,trip"), en("We have a picnic together.", "focus:picnic,together"),
      en("It's very relaxing!", "focus:relaxing"))
L.review([("holiday", "holiday"), ("general", "general"), ("relaxing", "relaxing"), ("trip", "trip"), ("away", "away"), ("picnic", "picnic"),
          ("suppose", "suppose"), ("festival", "festival"), ("during", "during"), ("visit", "visit, visitor"), ("come", "come, came"), ("together", "together")],
         "太棒了！放假的时候，和家人一起做点开心的事吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
