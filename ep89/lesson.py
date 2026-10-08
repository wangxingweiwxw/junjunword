import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep89", "pain", "疼痛", 89, "headache")
A = dict(kind="adj")
L.node("hospital", "hospital", "/ˈhɑːspɪtl/", "医院")
L.node("problem", "problem", "/ˈprɑːbləm/", "问题")
L.node("pale", "pale", "/peɪl/", "苍白的", **A)
L.node("liedown", "lie down", "/laɪ daʊn/", "躺下", kind="verb")
L.node("bone", "bone", "/boʊn/", "骨头")
L.node("broken", "broken", "/ˈbroʊkən/", "断了的；坏了的", **A, alt="break", altLabel="来自")
L.node("pain", "pain", "/peɪn/", "疼痛")
L.node("hurt", "hurt", "/hɜːrt/", "弄疼；受伤", kind="verb")
L.node("ache", "ache", "/eɪk/", "疼")
L.node("headache", "headache", "/ˈhedeɪk/", "头疼")
L.node("toothache", "toothache", "/ˈtuːθeɪk/", "牙疼")
L.node("stomachache", "stomachache", "/ˈstʌməkeɪk/", "肚子疼")
L.node("backache", "backache", "/ˈbækeɪk/", "背疼")
L.grid(["problem hospital pale",
        "liedown . bone",
        "pain hurt broken",
        "ache headache toothache",
        ". stomachache backache"], dy=330)
for id, x, y in [("hospital", 180, 470), ("problem", 180, 150), ("pale", 180, 790), ("liedown", 540, 150), ("bone", 540, 790), ("broken", 900, 790),
                 ("pain", 900, 150), ("hurt", 900, 470), ("ache", 1260, 470), ("headache", 1260, 150), ("toothache", 1620, 150), ("stomachache", 1620, 470),
                 ("backache", 1620, 790)]:
    L.byid[id]["at"] = [x, y]
L.edge("hospital", "problem"); L.edge("hospital", "pale"); L.edge("hospital", "liedown"); L.edge("hospital", "bone"); L.edge("bone", "broken")
L.edge("pain", "hurt"); L.edge("pain", "ache"); L.edge("ache", "headache"); L.edge("ache", "toothache"); L.edge("ache", "stomachache"); L.edge("ache", "backache")

L.seg("title", zh("小朋友们好！还记得第六十八集的生病吗？今天，我们来学身体哪里疼怎么说。"), en("pain"))
L.seg("map show:hospital focus:hospital", zh("医院："), en("hospital"))
L.seg("show:problem edge:hospital>problem focus:problem", zh("医生问：你有什么问题？"), en("problem"), en("What's the problem?"))
L.seg("show:pale edge:hospital>pale focus:pale", zh("脸色白白的，是苍白的："), en("pale"), en("You look pale."))
L.seg("show:liedown edge:hospital>liedown focus:liedown", zh("医生说：先躺下吧。"), en("lie down"))
L.seg("show:bone edge:hospital>bone focus:bone", zh("身体里硬硬的，是骨头："), en("bone"))
L.seg("show:broken edge:bone>broken focus:broken", zh("摔了一跤，骨头断了。还记得第七十九集的 break 吗？"), en("break"), en("broken"), en("a broken arm"))
L.seg("show:pain focus:pain", zh("身上不舒服，有疼痛："), en("pain"))
L.seg("show:hurt edge:pain>hurt focus:hurt", zh("弄疼了、受伤了，是"), en("hurt"), en("My finger hurts."))
L.seg("show:ache edge:pain>ache focus:ache", zh("一直隐隐地疼，是"), en("ache"), zh("a c h e，c h 读成 k。今天的秘密：身体部位，加上 ache，就是哪里疼！"))
L.seg("show:headache edge:ache>headache focus:headache", zh("头疼：头，加上 ache："), en("head"), en("headache"))
L.seg("show:toothache edge:ache>toothache focus:toothache", zh("牙疼。还记得第十六集的牙齿吗？"), en("tooth"), en("toothache"))
L.seg("show:stomachache edge:ache>stomachache focus:stomachache", zh("肚子疼。肚子，是 stomach："), en("stomach"), en("stomachache"))
L.seg("show:backache edge:ache>backache focus:backache", zh("背疼。背，是 back："), en("back"), en("backache"))
L.seg("focus:headache,toothache,stomachache,backache", zh("说哪里疼，要说 I have a："),
      en("I have a headache.", "focus:headache"), en("I have a toothache.", "focus:toothache"), en("I have a stomachache.", "focus:stomachache"))
L.review([("hospital", "hospital"), ("problem", "problem"), ("pale", "pale"), ("liedown", "lie down"), ("bone", "bone"), ("broken", "broken"), ("pain", "pain"),
          ("hurt", "hurt"), ("ache", "ache"), ("headache", "headache"), ("toothache", "toothache"), ("stomachache", "stomachache"), ("backache", "backache")],
         "太棒了！哪里不舒服，要马上告诉爸爸妈妈哦。点一点图上的单词，还能再听一遍发音。")
L.save()
