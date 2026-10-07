import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep33", "learning", "学习", 33, "learn")
V = dict(kind="verb")
L.node("learn", "learn", "/lɜːrn/", "学习", **V)
L.node("read", "read", "/riːd/", "读", **V)
L.node("story", "story", "/ˈstɔːri/", "故事", plural="stories", pluralIpa="/ˈstɔːriz/")
L.node("write", "write", "/raɪt/", "写", **V)
L.node("spell", "spell", "/spel/", "拼写", **V)
L.node("spelling", "spelling", "/ˈspelɪŋ/", "拼写；拼法")
L.node("teach", "teach", "/tiːtʃ/", "教", **V)
L.node("explain", "explain", "/ɪkˈspleɪn/", "解释", **V)
L.node("example", "example", "/ɪɡˈzæmpl/", "例子")
L.node("clear", "clear", "/klɪr/", "清楚的", kind="adj")
L.node("understand", "understand", "/ˌʌndərˈstænd/", "明白；理解", **V)
L.node("repeat", "repeat", "/rɪˈpiːt/", "重复", **V)
L.node("speak", "speak", "/spiːk/", "说（语言）", **V)
L.node("speech", "speech", "/spiːtʃ/", "演讲")
L.grid(["read learn write",
        "story understand spell",
        "repeat teach spelling",
        "example explain clear",
        "speak speech ."], dy=330)
L.edge("learn", "read"); L.edge("read", "story"); L.edge("learn", "write"); L.edge("write", "spell"); L.edge("spell", "spelling", "+ing")
L.edge("learn", "understand"); L.edge("understand", "repeat", "不懂就"); L.edge("teach", "explain"); L.edge("explain", "example", "举")
L.edge("explain", "clear", "讲得"); L.edge("speak", "speech", "ea→ee")

L.seg("title", zh("小朋友们好！在学校里，我们每天都在学习。今天，就来学和学习有关的单词。"), en("learn"))
L.seg("map show:learn focus:learn", zh("学新的东西，英语是"), en("learn"), en("I learn English."))
L.seg("show:read edge:learn>read focus:read", zh("学习的第一步，是读："), en("read"), en("Let's read together."))
L.seg("show:story edge:read>story focus:story", zh("读什么呢？读有趣的故事："), en("story"),
      zh("很多故事，要把 y 变成 i e s：", "plural:story"), en("stories"))
L.seg("show:write edge:learn>write focus:write", zh("学了还要会写："), en("write"), zh("开头的 w 不发音哦。"), en("I write well."))
L.seg("show:spell edge:write>spell focus:spell", zh("把一个单词的字母，一个一个说出来，是拼写："), en("spell"), en("C, A, T, cat."))
L.seg("show:spelling edge:spell>spelling focus:spelling", zh("加上 i n g，就是拼写这件事，比如拼写测验："), en("spelling"), en("a spelling test"))
L.seg("show:understand edge:learn>understand focus:understand", zh("学会了，心里亮堂堂的，是明白、理解："), en("understand"),
      zh("在下面，加上站："), en("under"), en("stand"), en("understand"))
L.seg("show:repeat edge:understand>repeat focus:repeat", zh("要是还没懂，就请老师再说一遍。重复，英语是"), en("repeat"),
      en("Please repeat."))
L.seg("show:teach focus:teach", zh("还记得第六集的教吗？"), en("teach"))
L.seg("show:explain edge:teach>explain focus:explain", zh("老师把难懂的地方讲明白，是解释："), en("explain"), en("Can you explain it?"))
L.seg("show:example edge:explain>example focus:example", zh("解释的时候，举一个例子，就更容易懂啦："), en("example"), en("for example"))
L.seg("show:clear edge:explain>clear focus:clear", zh("讲得清清楚楚，是"), en("clear"), en("It's very clear."))
L.seg("show:speak focus:speak", zh("还记得第七集的说吗？说一种语言："), en("speak"))
L.seg("show:speech edge:speak>speech focus:speech", zh("站在台上，对着大家说一段话，是演讲："), en("speech"),
      zh("说是 e a，演讲变成了两个 e。"), en("speak", "focus:speak"), en("speech", "focus:speech"))
L.seg("focus:none", zh("我们在课堂上，常常会这样说："))
L.seg("", en("I don't understand.", "focus:understand"), en("Can you explain it again?", "focus:explain"),
      en("Please repeat.", "focus:repeat"), en("Now I understand!", "focus:understand"))
L.review([("learn", "learn"), ("read", "read"), ("story", "story, stories"), ("write", "write"), ("spell", "spell"),
          ("spelling", "spelling"), ("understand", "understand"), ("repeat", "repeat"), ("teach", "teach"), ("explain", "explain"),
          ("example", "example"), ("clear", "clear"), ("speak", "speak"), ("speech", "speech")],
         "太棒了！上课没听懂的时候，勇敢地用英语说一句 Please repeat 吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
