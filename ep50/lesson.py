import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep50", "weather", "天气（二）", 50, "umbrella")
A = dict(kind="adj")
L.node("weather", "weather", "/ˈweðər/", "天气")
L.node("temperature", "temperature", "/ˈtemprətʃər/", "温度")
L.node("degree", "degree", "/dɪˈɡriː/", "度")
L.node("heat", "heat", "/hiːt/", "炎热；热量")
L.node("smoke", "smoke", "/smoʊk/", "烟")
L.node("dry", "dry", "/draɪ/", "干的", **A)
L.node("wet", "wet", "/wet/", "湿的", **A)
L.node("rainy", "rainy", "/ˈreɪni/", "下雨的", **A)
L.node("umbrella", "umbrella", "/ʌmˈbrelə/", "雨伞")
L.node("raincoat", "raincoat", "/ˈreɪnkoʊt/", "雨衣")
L.node("take", "take", "/teɪk/", "带上；拿", kind="verb")
L.node("too", "too", "/tuː/", "也；太", kind="adv")
L.node("snowy", "snowy", "/ˈsnoʊi/", "下雪的", **A)
L.node("ice", "ice", "/aɪs/", "冰")
L.node("freeze", "freeze", "/friːz/", "结冰", kind="verb", alt="froze", altLabel="过去式")
L.grid(["degree temperature weather",
        "heat dry rainy",
        "smoke wet umbrella",
        "take raincoat too",
        "snowy ice freeze"], dy=330)
L.edge("weather", "temperature"); L.edge("temperature", "degree"); L.edge("temperature", "heat", "很高"); L.edge("heat", "smoke", dashed=True)
L.edge("heat", "dry"); L.edge("dry", "wet", "反义"); L.edge("weather", "rainy"); L.edge("rainy", "umbrella")
L.edge("take", "raincoat"); L.edge("too", "umbrella", dashed=True); L.edge("snowy", "ice"); L.edge("ice", "freeze")

L.seg("title", zh("小朋友们好！还记得第十九集的天气吗？今天，我们学更多和天气有关的词。"), en("weather"))
L.seg("map show:weather focus:weather", zh("天气："), en("weather"))
L.seg("show:temperature edge:weather>temperature focus:temperature", zh("天气有多冷多热，要看温度："), en("temperature"),
      zh("这个词很长，拆开读："), en("tem, pe, ra, ture"))
L.seg("show:degree edge:temperature>degree focus:degree", zh("温度用度来表示："), en("degree"), en("It's 25 degrees today."))
L.seg("show:heat edge:temperature>heat focus:heat", zh("温度很高的时候，热浪滚滚，是炎热："), en("heat"), zh("还记得第十九集的热 hot 吗？"))
L.seg("show:smoke edge:heat>smoke focus:smoke", zh("太热太干，要小心着火冒烟。烟，英语是"), en("smoke"))
L.seg("show:dry edge:heat>dry focus:dry", zh("很久不下雨，地面是干的："), en("dry"))
L.seg("show:wet edge:dry>wet focus:wet", zh("被雨淋了，是湿的："), en("wet"), zh("干和湿："), en("dry", "focus:dry"), en("wet", "focus:wet"))
L.seg("show:rainy edge:weather>rainy focus:rainy", zh("下雨天："), en("rainy"))
L.seg("show:umbrella edge:rainy>umbrella focus:umbrella", zh("下雨要打伞："), en("umbrella"))
L.seg("show:raincoat focus:raincoat", zh("或者穿雨衣。雨，加上外套："), en("rain"), en("coat"), en("raincoat"))
L.seg("show:take edge:take>raincoat focus:take", zh("出门前，记得带上："), en("take"), en("Take your raincoat."))
L.seg("show:too edge:too>umbrella focus:too", zh("也带上雨伞。也，英语是"), en("too"), en("Take your umbrella too."),
      zh("还记得第二十集也学过一个 also 吗？"))
L.seg("show:snowy focus:snowy", zh("下雪天："), en("snowy"))
L.seg("show:ice edge:snowy>ice focus:ice", zh("冷得水变成了冰："), en("ice"))
L.seg("show:freeze edge:ice>freeze focus:freeze", zh("水变成冰，是结冰："), en("freeze"),
      zh("已经结冰了，要说", "alt:freeze"), en("froze"), en("The water froze this morning."))
L.seg("focus:none", zh("当一回天气预报员吧！"))
L.seg("", en("Today is rainy and wet.", "focus:rainy,wet"), en("Take your umbrella!", "focus:take,umbrella"),
      en("Tomorrow is snowy. The water will freeze.", "focus:snowy,freeze"))
L.review([("weather", "weather"), ("temperature", "temperature"), ("degree", "degree"), ("heat", "heat"), ("smoke", "smoke"), ("dry", "dry"),
          ("wet", "wet"), ("rainy", "rainy"), ("umbrella", "umbrella"), ("raincoat", "raincoat"), ("take", "take"), ("too", "too"),
          ("snowy", "snowy"), ("ice", "ice"), ("freeze", "freeze, froze")],
         "太棒了！每天出门前，看看天气，用英语说一说要带什么吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
