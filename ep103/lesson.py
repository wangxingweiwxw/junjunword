import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep103", "Internet", "互联网", 103, "internet")
V = dict(kind="verb")
L.node("internet", "Internet", "/ˈɪntərnet/", "互联网")
L.node("introduction", "introduction", "/ˌɪntrəˈdʌkʃn/", "介绍")
L.node("search", "search", "/sɜːrtʃ/", "搜索", **V)
L.node("anything", "anything", "/ˈeniθɪŋ/", "任何东西")
L.node("nothing", "nothing", "/ˈnʌθɪŋ/", "什么也没有")
L.node("agree", "agree", "/əˈɡriː/", "同意", **V)
L.node("agreement", "agreement", "/əˈɡriːmənt/", "一致；协议")
L.node("disagree", "disagree", "/ˌdɪsəˈɡriː/", "不同意", **V)
L.node("disagreement", "disagreement", "/ˌdɪsəˈɡriːmənt/", "分歧")
L.node("advertisement", "advertisement", "/ˌædvərˈtaɪzmənt/", "广告", alt="ad", altLabel="简称")
L.node("advantage", "advantage", "/ədˈvæntɪdʒ/", "优点")
L.node("disadvantage", "disadvantage", "/ˌdɪsədˈvæntɪdʒ/", "缺点")
L.node("error", "error", "/ˈerər/", "错误")
L.grid(["agreement nothing anything",
        "agree introduction search",
        "disagree internet error",
        "disagreement advantage advertisement",
        ". disadvantage ."], dy=330)
for id, x, y in [("agreement", 170, 150), ("agree", 520, 150), ("introduction", 870, 150), ("search", 1220, 150), ("anything", 1570, 150),
                 ("disagreement", 170, 470), ("disagree", 520, 470), ("internet", 870, 470), ("nothing", 1570, 470), ("error", 1220, 470),
                 ("advertisement", 520, 790), ("advantage", 870, 790), ("disadvantage", 1220, 790)]:
    L.byid[id]["at"] = [x, y]
L.edge("internet", "introduction"); L.edge("internet", "agree"); L.edge("internet", "disagree"); L.edge("agree", "agreement", "+ment"); L.edge("disagree", "disagreement", "+ment")
L.edge("internet", "search"); L.edge("search", "anything"); L.edge("search", "nothing", dashed=True); L.edge("internet", "advertisement"); L.edge("internet", "advantage")
L.edge("advantage", "disadvantage", "dis+"); L.edge("internet", "error")

L.seg("title", zh("小朋友们好！上网可以查资料、看新闻。今天，我们来学和互联网有关的单词。"), en("Internet"))
L.seg("map show:internet focus:internet", zh("连接全世界电脑的网络，是互联网："), en("Internet"), zh("它的开头要大写哦。"))
L.seg("show:introduction edge:internet>introduction focus:introduction", zh("网站上的介绍："), en("introduction"), zh("自我介绍，就是 self-introduction。"))
L.seg("show:search edge:internet>search focus:search", zh("在网上搜索："), en("search"), en("Search on the Internet."))
L.seg("show:anything edge:search>anything focus:anything", zh("在网上，几乎能搜到任何东西。任何，加上东西："), en("any"), en("thing"), en("anything"))
L.seg("show:nothing edge:search>nothing focus:nothing", zh("有时候，什么也找不到。没有，加上东西："), en("no"), en("thing"), en("nothing"))
L.seg("show:agree edge:internet>agree focus:agree", zh("网上大家会讨论。同意，英语是"), en("agree"), en("I agree with you."))
L.seg("show:agreement edge:agree>agreement focus:agreement", zh("加上 m e n t，就是意见一致、协议："), en("agreement"))
L.seg("show:disagree edge:internet>disagree focus:disagree", zh("不同意，前面加 d i s："), en("disagree"))
L.seg("show:disagreement edge:disagree>disagreement focus:disagreement", zh("意见不一样，就是分歧："), en("disagreement"))
L.seg("show:advertisement edge:internet>advertisement focus:advertisement", zh("网页上弹出来的广告："), en("advertisement"), zh("简称是", "alt:advertisement"), en("ad"))
L.seg("show:advantage edge:internet>advantage focus:advantage", zh("互联网有很多优点："), en("advantage"))
L.seg("show:disadvantage edge:advantage>disadvantage focus:disadvantage", zh("也有缺点，前面加 d i s："), en("disadvantage"), zh("比如，上网太久会伤眼睛。"))
L.seg("show:error edge:internet>error focus:error", zh("网页打不开，出错了："), en("error"))
L.seg("focus:disagree,disadvantage", zh("今天的 d i s 家族："), en("agree, disagree", "focus:agree,disagree"), en("advantage, disadvantage", "focus:advantage,disadvantage"))
L.review([("internet", "Internet"), ("introduction", "introduction"), ("search", "search"), ("anything", "anything"), ("nothing", "nothing"), ("agree", "agree"),
          ("agreement", "agreement"), ("disagree", "disagree"), ("disagreement", "disagreement"), ("advertisement", "advertisement, ad"), ("advantage", "advantage"),
          ("disadvantage", "disadvantage"), ("error", "error")],
         "太棒了！上网要有节制，每次不要太久哦。点一点图上的单词，还能再听一遍发音。")
L.save()
