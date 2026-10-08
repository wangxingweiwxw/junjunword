import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep68", "illness", "生病", 68, "hospital")
A = dict(kind="adj")
L.node("hospital", "hospital", "/ˈhɑːspɪtl/", "医院")
L.node("sick", "sick", "/sɪk/", "生病的", **A)
L.node("ill", "ill", "/ɪl/", "生病的", **A)
L.node("illness", "illness", "/ˈɪlnəs/", "疾病")
L.node("fever", "fever", "/ˈfiːvər/", "发烧")
L.node("cough", "cough", "/kɔːf/", "咳嗽")
L.node("flu", "flu", "/fluː/", "流感")
L.node("spread", "spread", "/spred/", "传播", kind="verb")
L.node("medicine", "medicine", "/ˈmedɪsn/", "药")
L.node("heart", "heart", "/hɑːrt/", "心脏")
L.node("beat", "beat", "/biːt/", "跳动", kind="verb", alt="heartbeat", altLabel="心跳")
L.grid(["sick hospital ill",
        "fever . illness",
        "cough flu spread",
        "medicine heart beat"], dy=350)
L.edge("hospital", "sick"); L.edge("hospital", "ill"); L.edge("ill", "illness", "+ness"); L.edge("sick", "fever"); L.edge("fever", "cough", dashed=True)
L.edge("cough", "flu", dashed=True); L.edge("flu", "spread", "会"); L.edge("cough", "medicine", "吃"); L.edge("heart", "beat")

L.seg("title", zh("小朋友们好！生病了可不好受。今天，我们来学和生病有关的单词，学会照顾好自己。"))
L.seg("map show:hospital focus:hospital", zh("看病的地方，是医院："), en("hospital"), zh("还记得第三十五集的医生和护士吗？他们就在这里工作。"))
L.seg("show:sick edge:hospital>sick focus:sick", zh("生病了，可以说"), en("sick"), en("I feel sick."))
L.seg("show:ill edge:hospital>ill focus:ill", zh("生病，还可以说"), en("ill"))
L.seg("show:illness edge:ill>illness focus:illness", zh("加上 n e s s，就是疾病："), en("illness"), zh("还记得 happiness 吗？一样的小尾巴。"))
L.seg("show:fever edge:sick>fever focus:fever", zh("身体烫烫的，是发烧："), en("fever"), en("I have a fever."))
L.seg("show:cough edge:fever>cough focus:cough", zh("咳咳咳，是咳嗽："), en("cough"), zh("最后的 g h，读成 f。还记得第四十集的 enough 吗？"))
L.seg("show:flu edge:cough>flu focus:flu", zh("又发烧又咳嗽，可能是得了流感："), en("flu"))
L.seg("show:spread edge:flu>spread focus:spread", zh("流感会传染给别人。传播，英语是"), en("spread"), zh("所以生病了要戴好口罩。"))
L.seg("show:medicine edge:cough>medicine focus:medicine", zh("医生开了药："), en("medicine"), en("The doctor gave me medicine for my cough."), zh("药虽然苦，但要按时吃哦。"))
L.seg("show:heart focus:heart", zh("医生用听诊器，听一听我们的心脏："), en("heart"))
L.seg("show:beat edge:heart>beat focus:beat", zh("心脏扑通扑通地跳动："), en("beat"), zh("心跳，就是", "alt:beat"), en("heartbeat"))
L.seg("focus:sick,ill", zh("两个都表示生病："), en("sick", "focus:sick"), en("ill", "focus:ill"))
L.seg("focus:none", zh("看病的时候，我们可以这样说："))
L.seg("", en("I don't feel well.", "focus:sick"), en("I have a fever and a cough.", "focus:fever,cough"), en("I need some medicine.", "focus:medicine"))
L.review([("hospital", "hospital"), ("sick", "sick"), ("ill", "ill"), ("illness", "illness"), ("fever", "fever"), ("cough", "cough"), ("flu", "flu"),
          ("spread", "spread"), ("medicine", "medicine"), ("heart", "heart"), ("beat", "beat")],
         "太棒了！多运动、多喝水、按时睡觉，就不容易生病啦。点一点图上的单词，还能再听一遍发音哦。")
L.save()
