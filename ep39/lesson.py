import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep39", "feelings", "情绪", 39, "feeling")
A = dict(kind="adj")
L.node("feeling", "feeling", "/ˈfiːlɪŋ/", "感觉；情绪", alt="feel", altLabel="来自")
L.node("happy", "happy", "/ˈhæpi/", "开心的", **A)
L.node("smile", "smile", "/smaɪl/", "微笑", kind="verb")
L.node("like", "like", "/laɪk/", "喜欢", kind="verb")
L.node("excited", "excited", "/ɪkˈsaɪtɪd/", "兴奋的", **A)
L.node("surprised", "surprised", "/sərˈpraɪzd/", "惊讶的", **A)
L.node("sudden", "sudden", "/ˈsʌdn/", "突然的", **A, alt="suddenly", altLabel="+ly")
L.node("mad", "mad", "/mæd/", "生气的", **A)
L.node("sad", "sad", "/sæd/", "伤心的", **A)
L.node("cry", "cry", "/kraɪ/", "哭", kind="verb")
L.node("tears", "tears", "/tɪrz/", "眼泪")
L.node("afraid", "afraid", "/əˈfreɪd/", "害怕的", **A)
L.node("scared", "scared", "/skerd/", "吓坏的", **A)
L.node("fear", "fear", "/fɪr/", "恐惧")
L.grid(["like smile happy",
        "excited feeling surprised",
        "mad sad sudden",
        "tears cry .",
        "fear scared afraid"], dy=330)
L.edge("feeling", "happy"); L.edge("happy", "smile"); L.edge("smile", "like", dashed=True); L.edge("feeling", "excited")
L.edge("feeling", "surprised"); L.edge("surprised", "sudden", "因为"); L.edge("feeling", "mad"); L.edge("feeling", "sad")
L.edge("sad", "cry"); L.edge("cry", "tears"); L.edge("sad", "afraid", dashed=True); L.edge("afraid", "scared", "更怕"); L.edge("scared", "fear")

L.seg("title", zh("小朋友们好！你今天心情怎么样？今天，我们来学表达情绪的单词。"), en("feelings"))
L.seg("map show:feeling focus:feeling", zh("心里的感受，是感觉、情绪："), en("feeling"),
      zh("它来自第十七集学过的", "alt:feeling"), en("feel"), en("How are you feeling?"))
L.seg("show:happy edge:feeling>happy focus:happy", zh("心里乐开了花，是开心的："), en("happy"), en("I'm happy!"))
L.seg("show:smile edge:happy>smile focus:smile", zh("开心的时候，我们会微笑："), en("smile"), en("Smile!"))
L.seg("show:like edge:smile>like focus:like", zh("看到喜欢的东西，眼睛都亮了。喜欢，英语是"), en("like"), en("I like you!"))
L.seg("show:excited edge:feeling>excited focus:excited", zh("要去游乐园啦，激动得跳起来，是兴奋的："), en("excited"))
L.seg("show:surprised edge:feeling>surprised focus:surprised", zh("没想到的事情发生了，眼睛瞪得圆圆的，是惊讶的："), en("surprised"))
L.seg("show:sudden edge:surprised>sudden focus:sudden", zh("让人吃惊的事，常常是突然发生的："), en("sudden"),
      zh("加上 l y，就是突然地：", "alt:sudden"), en("suddenly"), en("Suddenly, it rained!"))
L.seg("show:mad edge:feeling>mad focus:mad", zh("气鼓鼓的，是生气的："), en("mad"), en("Don't be mad."))
L.seg("show:sad edge:feeling>sad focus:sad", zh("心里难过，是伤心的："), en("sad"))
L.seg("show:cry edge:sad>cry focus:cry", zh("太伤心了，就会哭："), en("cry"))
L.seg("show:tears edge:cry>tears focus:tears", zh("哭的时候，流下的是眼泪："), en("tears"))
L.seg("show:afraid focus:afraid", zh("怕黑、怕打雷，是害怕的："), en("afraid"), en("I'm afraid of the dark."))
L.seg("show:scared edge:afraid>scared focus:scared", zh("被吓了一大跳，是吓坏的："), en("scared"))
L.seg("show:fear edge:scared>fear focus:fear", zh("心里的害怕，叫恐惧："), en("fear"))
L.seg("focus:excited,surprised,scared", zh("你发现了吗？好多表示感觉的词，都是 e d 结尾的："),
      en("excited", "focus:excited"), en("surprised", "focus:surprised"), en("scared", "focus:scared"))
L.seg("focus:happy,sad", zh("一开心，一伤心："), en("happy", "focus:happy"), en("sad", "focus:sad"))
L.seg("focus:none", zh("我们来做一做表情吧！"))
L.seg("", en("Show me happy!", "focus:happy"), en("Show me sad!", "focus:sad"), en("Show me surprised!", "focus:surprised"),
      en("Show me mad!", "focus:mad"))
L.review([("feeling", "feeling"), ("happy", "happy"), ("smile", "smile"), ("like", "like"), ("excited", "excited"),
          ("surprised", "surprised"), ("sudden", "sudden, suddenly"), ("mad", "mad"), ("sad", "sad"), ("cry", "cry"),
          ("tears", "tears"), ("afraid", "afraid"), ("scared", "scared"), ("fear", "fear")],
         "太棒了！每天放学，用英语说一说你今天的心情吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
