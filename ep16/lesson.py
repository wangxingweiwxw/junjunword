import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep16", "face", "脸", 16, "face")
L.node("face", "face", "/feɪs/", "脸")
L.node("eye", "eye", "/aɪ/", "眼睛", plural="eyes", pluralIpa="/aɪz/")
L.node("ear", "ear", "/ɪr/", "耳朵", plural="ears", pluralIpa="/ɪrz/")
L.node("nose", "nose", "/noʊz/", "鼻子")
L.node("mouth", "mouth", "/maʊθ/", "嘴巴")
L.node("tooth", "tooth", "/tuːθ/", "牙齿", plural="teeth", pluralIpa="/tiːθ/")
L.node("tongue", "tongue", "/tʌŋ/", "舌头")
L.node("chin", "chin", "/tʃɪn/", "下巴")
L.node("throat", "throat", "/θroʊt/", "喉咙")
L.node("chest", "chest", "/tʃest/", "胸口")
L.node("brain", "brain", "/breɪn/", "大脑")
L.node("mind", "mind", "/maɪnd/", "心思；头脑")
L.grid(["ear eye mind",
        "nose face brain",
        "chin mouth tongue",
        "tooth throat chest"])
L.edge("face", "eye"); L.edge("face", "ear"); L.edge("face", "nose"); L.edge("face", "mouth"); L.edge("face", "chin")
L.edge("face", "brain", "头里面"); L.edge("brain", "mind", "想出")
L.edge("mouth", "tongue"); L.edge("mouth", "tooth"); L.edge("mouth", "throat", "往下"); L.edge("throat", "chest")

L.seg("title", zh("小朋友们好！第八集，我们认识了身体。今天，我们凑近一点，仔细看看自己的脸。"), en("face"), zh("脸。"))
L.seg("map show:face focus:face", zh("每天照镜子，看到的就是自己的脸："), en("face"), en("Wash your face."))
L.seg("show:eye edge:face>eye focus:eye", zh("脸上亮晶晶的，是眼睛："), en("eye"), zh("两只眼睛：", "plural:eye"), en("eyes"))
L.seg("show:ear edge:face>ear focus:ear", zh("脸的两边，是耳朵："), en("ear"), zh("两只耳朵：", "plural:ear"), en("ears"))
L.seg("show:nose edge:face>nose focus:nose", zh("脸的正中间，是鼻子："), en("nose"), en("Touch your nose."))
L.seg("show:mouth edge:face>mouth focus:mouth", zh("鼻子下面，是嘴巴："), en("mouth"), en("Open your mouth."))
L.seg("show:tooth edge:mouth>tooth focus:tooth", zh("嘴巴里，有一颗一颗白白的牙齿："), en("tooth"),
      zh("很多颗牙齿可不加 s，而是像第八集的脚一样，把两个 o 变成两个 e："), en("teeth", "plural:tooth"),
      en("foot, feet."), en("tooth, teeth."))
L.seg("show:tongue edge:mouth>tongue focus:tongue", zh("嘴巴里会动、能尝出味道的，是舌头："), en("tongue"),
      zh("小提示：它最后的 u 和 e，都不发音。"))
L.seg("show:chin edge:face>chin focus:chin", zh("脸的最下面，是下巴："), en("chin"))
L.seg("show:throat edge:mouth>throat focus:throat", zh("吃下去的东西，要经过喉咙："), en("throat"),
      zh("开头的 t h，舌尖要轻轻放在牙齿中间。"), en("I have a sore throat."))
L.seg("show:chest edge:throat>chest focus:chest", zh("喉咙再往下，是胸口。心脏就在这里，扑通扑通地跳："), en("chest"))
L.seg("show:brain edge:face>brain focus:brain", zh("我们的头里面，藏着一个会思考的大脑："), en("brain"), en("Use your brain!"))
L.seg("show:mind edge:brain>mind focus:mind", zh("大脑想出来的念头和心思，叫"), en("mind"),
      zh("大脑是身体里看得见的部分，心思是看不见的想法。"), en("brain", "focus:brain"), en("mind", "focus:mind"))
L.seg("focus:eye,ear,tooth", zh("我们有两只眼睛、两只耳朵，还有很多颗牙齿："),
      en("eyes", "focus:eye"), en("ears", "focus:ear"), en("teeth", "focus:tooth"))
L.seg("focus:none", zh("来玩个小游戏！听到哪里，就指一指哪里！"))
L.seg("", en("Point to your nose!", "focus:nose"), en("Point to your eyes!", "focus:eye"), en("Point to your ears!", "focus:ear"),
      en("Open your mouth!", "focus:mouth"), en("Show me your teeth!", "focus:tooth"), en("Touch your chin!", "focus:chin"))
L.review([("face", "face"), ("eye", "eye, eyes"), ("ear", "ear, ears"), ("nose", "nose"), ("mouth", "mouth"),
          ("tooth", "tooth, teeth"), ("tongue", "tongue"), ("chin", "chin"), ("throat", "throat"), ("chest", "chest"),
          ("brain", "brain"), ("mind", "mind")],
         "太棒了！刷牙洗脸的时候，对着镜子用英语说一说吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
