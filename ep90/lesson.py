import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep90", "disease", "疾病", 90, "treatment")
A, V = dict(kind="adj"), dict(kind="verb")
L.node("hospital", "hospital", "/ˈhɑːspɪtl/", "医院")
L.node("cut", "cut", "/kʌt/", "割伤；切", **V)
L.node("burn", "burn", "/bɜːrn/", "烧伤；烫伤", **V)
L.node("awful", "awful", "/ˈɔːfl/", "糟糕的；可怕的", **A)
L.node("blind", "blind", "/blaɪnd/", "失明的", **A)
L.node("deaf", "deaf", "/def/", "失聪的", **A)
L.node("disabled", "disabled", "/dɪsˈeɪbld/", "残疾的", **A, alt="able", altLabel="dis+")
L.node("disease", "disease", "/dɪˈziːz/", "疾病")
L.node("cancer", "cancer", "/ˈkænsər/", "癌症")
L.node("prevent", "prevent", "/prɪˈvent/", "预防；阻止", **V)
L.node("drug", "drug", "/drʌɡ/", "药物")
L.node("weak", "weak", "/wiːk/", "虚弱的", **A)
L.node("operation", "operation", "/ˌɑːpəˈreɪʃn/", "手术")
L.node("treatment", "treatment", "/ˈtriːtmənt/", "治疗", alt="treat", altLabel="来自")
L.grid(["cut hospital burn",
        "awful blind deaf",
        ". disabled .",
        "prevent disease cancer",
        "drug weak operation",
        ". treatment ."], dy=310)
for id, x, y in [("cut", 170, 150), ("burn", 170, 470), ("awful", 170, 790), ("hospital", 520, 470), ("blind", 520, 150), ("deaf", 870, 150), ("disabled", 870, 470),
                 ("disease", 1220, 470), ("prevent", 1220, 150), ("cancer", 1570, 470), ("drug", 1570, 150), ("weak", 1570, 790), ("operation", 870, 790), ("treatment", 1220, 790)]:
    L.byid[id]["at"] = [x, y]
L.edge("hospital", "cut"); L.edge("hospital", "burn"); L.edge("burn", "awful"); L.edge("hospital", "blind"); L.edge("blind", "deaf"); L.edge("deaf", "disabled")
L.edge("hospital", "disabled"); L.edge("disabled", "disease", dashed=True); L.edge("prevent", "disease"); L.edge("disease", "cancer"); L.edge("drug", "cancer")
L.edge("cancer", "weak"); L.edge("operation", "treatment"); L.edge("treatment", "disease")

L.seg("title", zh("小朋友们好！还记得第六十八集和第八十九集的生病吗？今天，我们学一些更严重的疾病和治疗。"), en("disease"))
L.seg("map show:hospital focus:hospital", zh("医院："), en("hospital"))
L.seg("show:cut edge:hospital>cut focus:cut", zh("不小心被刀割伤了："), en("cut"), en("I cut my finger."))
L.seg("show:burn edge:hospital>burn focus:burn", zh("被热水烫伤、被火烧伤："), en("burn"))
L.seg("show:awful edge:burn>awful focus:awful", zh("烫伤真是太糟糕了："), en("awful"), zh("还记得 terrible 吗？意思差不多。"))
L.seg("show:blind edge:hospital>blind focus:blind", zh("眼睛看不见，是失明的："), en("blind"))
L.seg("show:deaf edge:blind>deaf focus:deaf", zh("耳朵听不见，是失聪的："), en("deaf"), zh("e a 读短短的 e。"))
L.seg("show:disabled edge:deaf>disabled edge:hospital>disabled focus:disabled", zh("能够是 able，加上 d i s 和 e d，就是残疾的："), en("disabled"),
      zh("我们要尊重和帮助残疾人。"))
L.seg("show:disease edge:disabled>disease focus:disease", zh("身体得的病，是疾病："), en("disease"))
L.seg("show:prevent edge:prevent>disease focus:prevent", zh("多运动、讲卫生，可以预防疾病："), en("prevent"))
L.seg("show:cancer edge:disease>cancer focus:cancer", zh("一种很严重的病，叫癌症："), en("cancer"))
L.seg("show:drug edge:drug>cancer focus:drug", zh("医生用药物来治病："), en("drug"), zh("药物一定要听医生的话吃。"))
L.seg("show:weak edge:cancer>weak focus:weak", zh("生了重病，身体很虚弱。还记得第十五集的 weak 吗？"), en("weak"))
L.seg("show:operation focus:operation", zh("有时候，医生要给病人做手术："), en("operation"))
L.seg("show:treatment edge:operation>treatment edge:treatment>disease focus:treatment", zh("治病的方法，是治疗。还记得 treat 吗？加上 m e n t："), en("treat"), en("treatment"))
L.seg("focus:none", zh("祝大家都健健康康！"))
L.seg("", en("Prevention is better than cure.", "focus:prevent"))
L.review([("hospital", "hospital"), ("cut", "cut"), ("burn", "burn"), ("awful", "awful"), ("blind", "blind"), ("deaf", "deaf"), ("disabled", "disabled"),
          ("disease", "disease"), ("prevent", "prevent"), ("cancer", "cancer"), ("drug", "drug"), ("weak", "weak"), ("operation", "operation"), ("treatment", "treatment")],
         "太棒了！多运动、讲卫生，就能远离疾病哦。点一点图上的单词，还能再听一遍发音。")
L.save()
