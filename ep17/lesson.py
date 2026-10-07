import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep17", "senses", "感觉", 17, "sense")
V, A = dict(kind="verb"), dict(kind="adj")
L.node("sense", "sense", "/sens/", "感觉", plural="senses", pluralIpa="/ˈsensɪz/")
L.node("see", "see", "/siː/", "看见", **V)
L.node("sight", "sight", "/saɪt/", "视觉")
L.node("hear", "hear", "/hɪr/", "听见", **V)
L.node("listen", "listen", "/ˈlɪsn/", "听", **V)
L.node("hearing", "hearing", "/ˈhɪrɪŋ/", "听觉")
L.node("smell", "smell", "/smel/", "闻；嗅觉", **V)
L.node("taste", "taste", "/teɪst/", "尝；味觉", **V)
L.node("sweet", "sweet", "/swiːt/", "甜的", **A)
L.node("salty", "salty", "/ˈsɔːlti/", "咸的", **A)
L.node("sour", "sour", "/ˈsaʊər/", "酸的", **A)
L.node("bitter", "bitter", "/ˈbɪtər/", "苦的", **A)
L.node("touch", "touch", "/tʌtʃ/", "摸；触觉", **V)
L.node("feel", "feel", "/fiːl/", "感觉；觉得", **V)
L.grid(["see sight sense",
        "hear hearing listen",
        ". smell .",
        "salty taste sweet",
        "sour . bitter",
        "feel touch ."], dy=330)
L.edge("see", "sight"); L.edge("sense", "sight"); L.edge("hear", "hearing"); L.edge("listen", "hearing", dashed=True)
for a, b in [("sight", "hearing"), ("hearing", "smell"), ("smell", "taste"), ("taste", "touch")]:
    L.edge(a, b, dashed=True)
for f in ["salty", "sweet", "sour", "bitter"]:
    L.edge("taste", f)
L.edge("feel", "touch")

L.seg("title", zh("小朋友们好！我们的身体，有五种神奇的感觉。今天，我们来一个一个认识它们。"), en("senses"), zh("感觉。"))
L.seg("map show:sense focus:sense", zh("看、听、闻、尝、摸，这些感觉，英语叫"), en("sense"),
      zh("我们一共有五种感觉：", "plural:sense"), en("five senses"))
L.seg("show:see focus:see", zh("第一种，靠眼睛。眼睛能看见："), en("see"), en("Eyes can see."))
L.seg("show:sight edge:see>sight edge:sense>sight focus:sight", zh("能看见东西的本领，叫视觉："), en("sight"))
L.seg("show:hear focus:hear", zh("第二种，靠耳朵。耳朵能听见："), en("hear"), en("Ears can hear."))
L.seg("show:listen focus:listen", zh("竖起耳朵，认认真真地去听，用"), en("listen"),
      zh("就像第七集的看和看见：主动去听，是"), en("listen", "focus:listen"), zh("听到了，是", "focus:hear"), en("hear"),
      en("Listen! Can you hear it?", "focus:listen,hear"))
L.seg("show:hearing edge:hear>hearing edge:listen>hearing edge:sight>hearing focus:hearing", zh("能听见声音的本领，叫听觉："), en("hearing"))
L.seg("show:smell edge:hearing>smell focus:smell", zh("第三种，靠鼻子。闻一闻，英语是"), en("smell"),
      zh("这个词，也是嗅觉的意思。"), en("It smells good!"))
L.seg("show:taste edge:smell>taste focus:taste", zh("第四种，靠舌头。尝一尝，英语是"), en("taste"),
      zh("它也是味觉的意思。舌头能尝出好多种味道："))
L.seg("show:sweet edge:taste>sweet focus:sweet", zh("糖果是甜的："), en("sweet"))
L.seg("show:salty edge:taste>salty focus:salty", zh("盐是咸的。盐，加上字母 y，就是咸的："), en("salt"), en("salty"))
L.seg("show:sour edge:taste>sour focus:sour", zh("柠檬是酸的："), en("sour"))
L.seg("show:bitter edge:taste>bitter focus:bitter", zh("药是苦的："), en("bitter"), en("The medicine is bitter."))
L.seg("show:touch edge:taste>touch focus:touch", zh("第五种，靠手。摸一摸，英语是"), en("touch"),
      zh("它也是触觉的意思。"), en("Hands can touch."))
L.seg("show:feel edge:feel>touch focus:feel", zh("摸到了东西，心里就有了感觉："), en("feel"), en("It feels soft."))
L.seg("focus:sight,hearing,smell,taste,touch", zh("五种感觉，我们一起来数一数："),
      en("sight", "focus:sight"), en("hearing", "focus:hearing"), en("smell", "focus:smell"), en("taste", "focus:taste"), en("touch", "focus:touch"))
L.seg("focus:none", zh("猜一猜，这些东西是什么味道？"))
L.seg("", zh("柠檬："), en("sour", "focus:sour"), zh("糖果："), en("sweet", "focus:sweet"),
      zh("盐："), en("salty", "focus:salty"), zh("药："), en("bitter", "focus:bitter"))
L.review([("sense", "sense, senses"), ("see", "see"), ("sight", "sight"), ("hear", "hear"), ("listen", "listen"),
          ("hearing", "hearing"), ("smell", "smell"), ("taste", "taste"), ("sweet", "sweet"), ("salty", "salty"),
          ("sour", "sour"), ("bitter", "bitter"), ("touch", "touch"), ("feel", "feel")],
         "太棒了！吃饭的时候，试着用英语说一说，每道菜是什么味道吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
