import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep08", "body", "身体", 8, "body")
L.node("body", "body", "/ˈbɑːdi/", "身体")
L.node("head", "head", "/hed/", "头")
L.node("hair", "hair", "/her/", "头发")
L.node("neck", "neck", "/nek/", "脖子")
L.node("shoulder", "shoulder", "/ˈʃoʊldər/", "肩膀")
L.node("arm", "arm", "/ɑːrm/", "胳膊")
L.node("hand", "hand", "/hænd/", "手", plural="hands", pluralIpa="/hændz/")
L.node("finger", "finger", "/ˈfɪŋɡər/", "手指")
L.node("leg", "leg", "/leɡ/", "腿", plural="legs", pluralIpa="/leɡz/")
L.node("knee", "knee", "/niː/", "膝盖")
L.node("foot", "foot", "/fʊt/", "脚", plural="feet", pluralIpa="/fiːt/")
L.node("toe", "toe", "/toʊ/", "脚趾", plural="toes", pluralIpa="/toʊz/")
L.node("shake", "shake", "/ʃeɪk/", "摇；晃动", kind="verb")
L.grid(["hair head shake",
        "shoulder neck .",
        "arm body .",
        "hand leg knee",
        "finger foot toe"])
L.edge("head", "hair"); L.edge("shake", "head", "摇头", dashed=True); L.edge("head", "neck"); L.edge("neck", "shoulder")
L.edge("shoulder", "arm"); L.edge("arm", "hand"); L.edge("hand", "finger"); L.edge("neck", "body")
L.edge("body", "leg"); L.edge("leg", "knee"); L.edge("leg", "foot"); L.edge("foot", "toe")

L.seg("title", zh("小朋友们好！今天，我们来认识自己的身体。"), en("body"), zh("身体。"))
L.seg("map show:body focus:body", zh("从头到脚，整个的你，就是身体："), en("body"), en("This is my body."))
L.seg("show:head focus:head", zh("身体最上面，圆圆的，是头："), en("head"), en("Touch your head."))
L.seg("show:hair edge:head>hair focus:hair", zh("头上长着头发："), en("hair"),
      zh("头发有成千上万根，可这个词通常不加 s 哦。"), en("I have black hair."))
L.seg("show:neck edge:head>neck focus:neck", zh("头和身体中间，连着脖子："), en("neck"))
L.seg("edge:neck>body focus:body", zh("脖子下面，就是身体啦："), en("body"))
L.seg("show:shoulder edge:neck>shoulder focus:shoulder", zh("脖子两边，又宽又平的地方是肩膀："), en("shoulder"), en("two shoulders"))
L.seg("show:arm edge:shoulder>arm focus:arm", zh("从肩膀往下，长长的是胳膊："), en("arm"), en("Raise your arms!"))
L.seg("show:hand edge:arm>hand focus:hand", zh("胳膊的最下面，是手："), en("hand"), en("Clap your hands!"))
L.seg("show:finger edge:hand>finger focus:finger", zh("还记得第三集吗？每只手上，都有五根手指："), en("finger"), en("five fingers"))
L.seg("show:leg edge:body>leg focus:leg", zh("身体下面，撑着我们走路、跑步的，是腿："), en("leg"))
L.seg("show:knee edge:leg>knee focus:knee", zh("腿中间能弯起来的地方，是膝盖："), en("knee"),
      zh("小提示：开头的字母 k，是不发音的。"), en("Bend your knees."))
L.seg("show:foot edge:leg>foot focus:foot", zh("腿的最下面，踩在地上的，是脚："), en("foot"))
L.seg("show:toe edge:foot>toe focus:toe", zh("脚上也有五根小小的，叫脚趾："), en("toe"), en("Wiggle your toes!"))
L.seg("show:shake edge:shake>head focus:shake", zh("最后学一个动作词：摇一摇、晃一晃，"), en("shake"),
      zh("摇头，是", "focus:shake,head"), en("shake your head"), zh("握手，是", "focus:shake,hand"), en("shake hands"))
L.seg("focus:none", zh("身体的很多部位，我们都有两个。变成很多个的时候，怎么说呢？"))
L.seg("focus:hand", zh("大部分在后面加上字母 s 就好："),
      en("hand", "focus:hand"), en("hands", "plural:hand"), en("leg", "focus:leg"), en("legs", "plural:leg"),
      en("toe", "focus:toe"), en("toes", "plural:toe"))
L.seg("focus:foot", zh("最特别的是脚。它不加 s，而是把中间的两个 o，变成两个 e："), en("foot"), en("feet", "plural:foot"),
      en("one foot, two feet."))
L.seg("focus:none", zh("来做个身体操吧！听到哪里，就摸一摸哪里！"))
L.seg("", en("Head!", "focus:head"), en("Shoulders!", "focus:shoulder"), en("Knees!", "focus:knee"),
      en("Toes!", "focus:toe"), en("Hands up!", "focus:hand"), en("Shake, shake, shake!", "focus:shake"))
L.review([("body", "body"), ("head", "head"), ("hair", "hair"), ("neck", "neck"), ("shoulder", "shoulder"),
          ("arm", "arm"), ("hand", "hand, hands"), ("finger", "finger"), ("leg", "leg, legs"), ("knee", "knee"),
          ("foot", "foot, feet"), ("toe", "toe, toes"), ("shake", "shake")],
         "太棒了！洗澡的时候，可以一边洗一边用英语说身体的部位哦。点一点图上的单词，还能再听一遍发音。")
L.save()
