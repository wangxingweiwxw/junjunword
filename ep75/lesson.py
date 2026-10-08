import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep75", "jobs", "职业（三）", 75, "company")
L.node("jobs", "jobs", "/dʒɑːbz/", "工作", icon="job")
L.node("duty", "duty", "/ˈduːti/", "责任；职责")
L.node("soldier", "soldier", "/ˈsoʊldʒər/", "士兵")
L.node("guard", "guard", "/ɡɑːrd/", "守卫")
L.node("captain", "captain", "/ˈkæptɪn/", "队长；船长")
L.node("officer", "officer", "/ˈɔːfɪsər/", "官员；警官")
L.node("police", "police", "/pəˈliːs/", "警察")
L.node("company", "company", "/ˈkʌmpəni/", "公司")
L.node("office", "office", "/ˈɔːfɪs/", "办公室")
L.node("meeting", "meeting", "/ˈmiːtɪŋ/", "会议", alt="meet", altLabel="来自")
L.node("boss", "boss", "/bɔːs/", "老板")
L.node("manager", "manager", "/ˈmænɪdʒər/", "经理", alt="manage", altLabel="来自")
L.node("business", "business", "/ˈbɪznəs/", "生意")
L.node("businessman", "businessman", "/ˈbɪznəsmæn/", "商人")
L.node("earn", "earn", "/ɜːrn/", "挣钱", kind="verb")
L.grid(["guard soldier captain",
        "duty jobs officer",
        "police company office",
        "boss manager meeting",
        "business businessman earn"], dy=330)
L.edge("jobs", "soldier"); L.edge("soldier", "guard"); L.edge("soldier", "captain"); L.edge("duty", "jobs", dashed=True); L.edge("jobs", "officer")
L.edge("jobs", "company"); L.edge("company", "office"); L.edge("office", "meeting"); L.edge("company", "manager")
L.edge("manager", "boss", dashed=True); L.edge("manager", "businessman", dashed=True); L.edge("business", "businessman", "+man"); L.edge("businessman", "earn")

L.seg("title", zh("小朋友们好！我们再来认识一些职业吧！还记得第六十四集吗？"), en("jobs"))
L.seg("map show:jobs focus:jobs", zh("工作："), en("jobs"))
L.seg("show:duty edge:duty>jobs focus:duty", zh("每份工作都有自己的责任："), en("duty"))
L.seg("show:soldier edge:jobs>soldier focus:soldier", zh("保卫国家的士兵："), en("soldier"))
L.seg("show:guard edge:soldier>guard focus:guard", zh("站岗放哨的守卫："), en("guard"), zh("中间的 u 不发音。"))
L.seg("show:captain edge:soldier>captain focus:captain", zh("带领大家的队长，也是船长："), en("captain"))
L.seg("show:officer edge:jobs>officer focus:officer", zh("当官的人，是"), en("officer"), zh("还记得 office 吗？加上 r。"))
L.seg("show:police edge:officer>police focus:police", zh("保护大家安全的警察："), en("police"))
L.seg("show:company edge:jobs>company focus:company", zh("很多人一起上班的地方，是公司："), en("company"))
L.seg("show:office edge:company>office focus:office", zh("公司里，大家在办公室工作："), en("office"))
L.seg("show:meeting edge:office>meeting focus:meeting", zh("坐在一起开会。见面，加上 i n g："), en("meet"), en("meeting"), zh("要双写 e 哦。"))
L.seg("show:manager edge:company>manager focus:manager", zh("管理大家的人，是经理。管理，加上 r："), en("manage"), en("manager"))
L.seg("show:boss edge:manager>boss focus:boss", zh("公司最大的头，是老板："), en("boss"))
L.seg("show:business focus:business", zh("做买卖，是生意："), en("business"), zh("小提示：中间的 i 读得很轻，常常像没有一样。"))
L.seg("show:businessman edge:business>businessman edge:manager>businessman focus:businessman", zh("做生意的人。生意，加上男人："), en("businessman"))
L.seg("show:earn edge:businessman>earn focus:earn", zh("工作，就能挣钱："), en("earn"), en("He earns money."))
L.review([("jobs", "jobs"), ("duty", "duty"), ("soldier", "soldier"), ("guard", "guard"), ("captain", "captain"), ("officer", "officer"), ("police", "police"),
          ("company", "company"), ("office", "office"), ("meeting", "meeting"), ("manager", "manager"), ("boss", "boss"), ("business", "business"),
          ("businessman", "businessman"), ("earn", "earn")],
         "太棒了！问一问爸爸妈妈在哪里工作吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
