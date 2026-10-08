import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep66", "sleep", "睡眠", 66, "sleep")
V, A, AD = dict(kind="verb"), dict(kind="adj"), dict(kind="adv")
L.node("sleep", "sleep", "/sliːp/", "睡觉", **V)
L.node("asleep", "asleep", "/əˈsliːp/", "睡着的", **A)
L.node("wake", "wake", "/weɪk/", "醒来", **V, alt="wake up", altLabel="常说")
L.node("awake", "awake", "/əˈweɪk/", "醒着的", **A)
L.node("rest", "rest", "/rest/", "休息", **V)
L.node("diary", "diary", "/ˈdaɪəri/", "日记")
L.node("suggest", "suggest", "/səɡˈdʒest/", "建议", **V)
L.node("suggestion", "suggestion", "/səɡˈdʒestʃən/", "建议（名词）")
L.node("main", "main", "/meɪn/", "主要的", **A)
L.node("even", "even", "/ˈiːvn/", "甚至", **AD)
L.node("more", "more", "/mɔːr/", "更多")
L.node("less", "less", "/les/", "更少")
L.node("hardly", "hardly", "/ˈhɑːrdli/", "几乎不", **AD)
L.grid(["asleep sleep awake",
        "rest diary wake",
        "suggest suggestion main",
        "more less hardly",
        ". even ."], dy=330)
L.edge("sleep", "asleep", "a+"); L.edge("sleep", "awake", dashed=True); L.edge("wake", "awake", "a+"); L.edge("sleep", "rest", dashed=True); L.edge("sleep", "diary", dashed=True)
L.edge("suggest", "suggestion", "+ion"); L.edge("more", "less", "反义"); L.edge("less", "hardly", "更少"); L.edge("less", "even", dashed=True)

L.seg("title", zh("小朋友们好！好好睡觉，才能长高高。今天，我们来学和睡眠有关的单词。"), en("sleep"))
L.seg("map show:sleep focus:sleep", zh("睡觉，英语是"), en("sleep"), en("I sleep at nine o'clock."))
L.seg("show:asleep edge:sleep>asleep focus:asleep", zh("在前面加一个 a，就是睡着的："), en("asleep"), en("The baby is asleep."))
L.seg("show:wake focus:wake", zh("早上醒来，是"), en("wake"), zh("常常说", "alt:wake"), en("wake up"))
L.seg("show:awake edge:wake>awake edge:sleep>awake focus:awake", zh("加上 a，就是醒着的："), en("awake"),
      zh("睡着和醒着，一对好朋友："), en("asleep", "focus:asleep"), en("awake", "focus:awake"))
L.seg("show:rest edge:sleep>rest focus:rest", zh("累了，就坐下休息一会儿："), en("rest"), en("Let's take a rest."))
L.seg("show:diary edge:sleep>diary focus:diary", zh("睡觉前，写一篇日记："), en("diary"))
L.seg("show:suggest focus:suggest", zh("医生建议我们早点睡："), en("suggest"), zh("还记得第六十五集的 advise 吗？意思差不多。"))
L.seg("show:suggestion edge:suggest>suggestion focus:suggestion", zh("加上 i o n，就是建议这件事："), en("suggestion"))
L.seg("show:main focus:main", zh("最重要的、主要的，英语是"), en("main"), en("Sleep is the main thing!"))
L.seg("show:more focus:more", zh("多睡一点，是"), en("more"), en("more sleep"))
L.seg("show:less edge:more>less focus:less", zh("少玩一点手机，是"), en("less"), en("less TV"))
L.seg("show:hardly edge:less>hardly focus:hardly", zh("少到几乎没有，是"), en("hardly"), en("I hardly watch TV at night."))
L.seg("show:even edge:less>even focus:even", zh("甚至，英语是"), en("even"), en("I even suggest you keep a sleep diary."))
L.seg("focus:none", zh("一起读一读睡前好习惯："))
L.seg("", en("Rest more.", "focus:rest,more"), en("Watch less TV.", "focus:less"), en("Go to sleep early!", "focus:sleep"))
L.review([("sleep", "sleep"), ("asleep", "asleep"), ("wake", "wake, wake up"), ("awake", "awake"), ("rest", "rest"), ("diary", "diary"),
          ("suggest", "suggest"), ("suggestion", "suggestion"), ("main", "main"), ("more", "more"), ("less", "less"), ("hardly", "hardly"), ("even", "even")],
         "太棒了！今天晚上早点睡，明天早上精神好。点一点图上的单词，还能再听一遍发音哦。")
L.save()
