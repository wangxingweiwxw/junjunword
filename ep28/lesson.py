import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep28", "measures", "大小和多少", 28, "weigh")
A = dict(kind="adj")
L.node("tall", "tall", "/tɔːl/", "高的", **A)
L.node("short", "short", "/ʃɔːrt/", "矮的；短的", **A)
L.node("long", "long", "/lɔːŋ/", "长的", **A)
L.node("straight", "straight", "/streɪt/", "直的", **A)
L.node("inch", "inch", "/ɪntʃ/", "英寸")
L.node("thick", "thick", "/θɪk/", "厚的", **A)
L.node("thin", "thin", "/θɪn/", "薄的；瘦的", **A)
L.node("lot", "a lot", "/ə lɑːt/", "许多")
L.node("much", "much", "/mʌtʃ/", "许多（不可数）")
L.node("weigh", "weigh", "/weɪ/", "称重", kind="verb", alt="weight", altLabel="名词")
L.node("half", "half", "/hæf/", "一半")
L.node("quarter", "quarter", "/ˈkwɔːrtər/", "四分之一")
L.grid(["tall short long",
        "straight inch .",
        "thick thin .",
        "lot much weigh",
        "half quarter ."], dy=330)
L.edge("tall", "short", "反义"); L.edge("short", "long", "反义"); L.edge("straight", "inch", "量一量", dashed=True)
L.edge("thick", "thin", "反义"); L.edge("lot", "much", "也表示多"); L.edge("half", "quarter", "再分")

L.seg("title", zh("小朋友们好！东西有高有矮，有厚有薄，有多有少。今天，我们来比一比！"))
L.seg("map show:tall focus:tall", zh("爸爸个子高高的："), en("tall"), en("Dad is tall."))
L.seg("show:short edge:tall>short focus:short", zh("我个子矮矮的："), en("short"), en("I am short."))
L.seg("show:long edge:short>long focus:long", zh("这个词还有一个意思：短。短的反面，是长："), en("long"),
      zh("长颈鹿的脖子长长的："), en("The giraffe has a long neck."))
L.seg("focus:tall,short,long", zh("记住哦：人的个子，用高和矮；东西的长度，用长和短。"),
      en("tall, short", "focus:tall,short"), en("long, short", "focus:long,short"))
L.seg("show:straight focus:straight", zh("尺子的边，是笔直笔直的："), en("straight"), zh("中间的 g h，又不发音了。"))
L.seg("show:inch edge:straight>inch focus:inch", zh("用尺子量一量。尺子上的一小段，是一英寸，差不多是你大拇指那么宽："), en("inch"))
L.seg("show:thick focus:thick", zh("词典厚厚的："), en("thick"), zh("开头的 t h，舌尖放在牙齿中间。"), en("a thick book"))
L.seg("show:thin edge:thick>thin focus:thin", zh("作业本薄薄的："), en("thin"), en("a thin book"),
      zh("说一个人很瘦，也可以用这个词。"))
L.seg("show:lot focus:lot", zh("爆米花装了满满一桶，好多好多："), en("a lot"), en("a lot of popcorn"))
L.seg("show:much edge:lot>much focus:much", zh("牛奶、水这样数不清的东西，问有多少，要用"), en("much"),
      en("How much milk do you want?"))
L.seg("show:weigh focus:weigh", zh("东西有多重，放在秤上称一称："), en("weigh"),
      zh("它的名词是重量：", "alt:weigh"), en("weight"), zh("这两个词里，g h 都不发音。"))
L.seg("show:half focus:half", zh("一个披萨，从中间切一刀，每份是一半："), en("half"), zh("小提示：l 不发音。"), en("half a pizza"))
L.seg("show:quarter edge:half>quarter focus:quarter", zh("再切一刀，切成四块，每一块是四分之一："), en("quarter"),
      zh("一刻钟，也是一小时的四分之一："), en("a quarter of an hour"))
L.seg("focus:none", zh("今天藏着好几个不发音的字母，我们一起找一找："),
      en("straight", "focus:straight"), en("weigh", "focus:weigh"), en("half", "focus:half"))
L.seg("focus:none", zh("比一比，选一选！"))
L.seg("", en("A giraffe is tall.", "focus:tall"), en("A dictionary is thick.", "focus:thick"),
      en("I want half a pizza, please.", "focus:half"))
L.review([("tall", "tall"), ("short", "short"), ("long", "long"), ("straight", "straight"), ("inch", "inch"), ("thick", "thick"),
          ("thin", "thin"), ("lot", "a lot"), ("much", "much"), ("weigh", "weigh, weight"), ("half", "half"), ("quarter", "quarter")],
         "太棒了！回家找两样东西，用英语比一比它们吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
