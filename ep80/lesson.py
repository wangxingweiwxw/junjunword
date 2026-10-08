import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep80", "adjectives", "形容词", 80, "fantastic")
A = dict(kind="adj")
L.node("situation", "situation", "/ˌsɪtʃuˈeɪʃn/", "情况")
L.node("condition", "condition", "/kənˈdɪʃn/", "条件；状况")
L.node("real", "real", "/riːl/", "真的", **A)
L.node("fake", "fake", "/feɪk/", "假的", **A)
L.node("exciting", "exciting", "/ɪkˈsaɪtɪŋ/", "令人兴奋的", **A)
L.node("boring", "boring", "/ˈbɔːrɪŋ/", "无聊的", **A)
L.node("amazing", "amazing", "/əˈmeɪzɪŋ/", "令人惊奇的", **A)
L.node("fantastic", "fantastic", "/fænˈtæstɪk/", "极好的", **A)
L.node("excellent", "excellent", "/ˈeksələnt/", "优秀的", **A)
L.node("useful", "useful", "/ˈjuːsfl/", "有用的", **A, alt="use", altLabel="来自")
L.node("useless", "useless", "/ˈjuːsləs/", "没用的", **A)
L.node("harmful", "harmful", "/ˈhɑːrmfl/", "有害的", **A, alt="harm", altLabel="来自")
L.node("harmless", "harmless", "/ˈhɑːrmləs/", "无害的", **A)
L.grid(["real situation condition",
        "fake exciting amazing",
        "boring . fantastic",
        "useful . excellent",
        "useless harmful harmless"], dy=330)
L.edge("situation", "real"); L.edge("real", "fake", "反义"); L.edge("situation", "exciting"); L.edge("exciting", "boring", "反义", dashed=True)
L.edge("condition", "amazing"); L.edge("amazing", "fantastic", dashed=True); L.edge("fantastic", "excellent", dashed=True)
L.edge("useful", "useless", "ful→less"); L.edge("harmful", "harmless", "ful→less")

L.seg("title", zh("小朋友们好！今天，我们来学一组很有用的形容词，还有两个神奇的小尾巴！"), en("adjectives"))
L.seg("map show:situation focus:situation", zh("事情现在的样子，是情况："), en("situation"))
L.seg("show:condition focus:condition", zh("东西的状况、条件，英语是"), en("condition"))
L.seg("show:real edge:situation>real focus:real", zh("真的，是"), en("real"))
L.seg("show:fake edge:real>fake focus:fake", zh("假的，是"), en("fake"), en("Is it real or fake?", "focus:real,fake"))
L.seg("show:exciting edge:situation>exciting focus:exciting", zh("坐过山车，好刺激！令人兴奋的："), en("exciting"))
L.seg("show:boring edge:exciting>boring focus:boring", zh("一直等啊等，好无聊："), en("boring"),
      zh("还记得第三十九集的 excited 吗？e d 说人的感受，i n g 说事情的样子。"))
L.seg("show:amazing edge:condition>amazing focus:amazing", zh("让人吃惊得张大嘴巴，是令人惊奇的："), en("amazing"))
L.seg("show:fantastic edge:amazing>fantastic focus:fantastic", zh("太棒了，极好的："), en("fantastic"))
L.seg("show:excellent edge:fantastic>excellent focus:excellent", zh("特别优秀的："), en("excellent"), en("Excellent work!"))
L.seg("focus:none", zh("下面是两个神奇的小尾巴。f u l 表示有、充满；l e s s 表示没有。"))
L.seg("show:useful focus:useful", zh("用，加上 f u l，是有用的："), en("use"), en("useful"))
L.seg("show:useless edge:useful>useless focus:useless", zh("换成 l e s s，就是没用的："), en("useless"))
L.seg("show:harmful focus:harmful", zh("伤害，加上 f u l，是有害的："), en("harm"), en("harmful"), en("Smoking is harmful."))
L.seg("show:harmless edge:harmful>harmless focus:harmless", zh("换成 l e s s，就是无害的："), en("harmless"))
L.seg("focus:useful,useless,harmful,harmless", zh("一起读："), en("useful, useless", "focus:useful,useless"), en("harmful, harmless", "focus:harmful,harmless"),
      zh("小提示：要说没用的、无害的，用 less，不说 unuseful、unharmful 哦。"))
L.review([("situation", "situation"), ("condition", "condition"), ("real", "real"), ("fake", "fake"), ("exciting", "exciting"), ("boring", "boring"),
          ("amazing", "amazing"), ("fantastic", "fantastic"), ("excellent", "excellent"), ("useful", "useful"), ("useless", "useless"),
          ("harmful", "harmful"), ("harmless", "harmless")],
         "太棒了！你今天过得怎么样？用一个形容词说一说吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
