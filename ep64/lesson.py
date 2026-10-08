import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep64", "jobs", "职业（二）", 64, "musician")
L.node("jobs", "jobs", "/dʒɑːbz/", "工作", icon="job")
for id, ipa, z, a in [("farmer", "/ˈfɑːrmər/", "农民", "farm"), ("fisherman", "/ˈfɪʃərmən/", "渔民", "fish"), ("postman", "/ˈpoʊstmən/", "邮递员", "post"),
                      ("trader", "/ˈtreɪdər/", "商人", "trade"), ("clerk", "/klɜːrk/", "店员；职员", None), ("performer", "/pərˈfɔːrmər/", "表演者", "perform"),
                      ("actor", "/ˈæktər/", "男演员", "act"), ("actress", "/ˈæktrəs/", "女演员", "act"), ("director", "/dəˈrektər/", "导演", "direct"),
                      ("musician", "/mjuˈzɪʃn/", "音乐家", "music"), ("guitarist", "/ɡɪˈtɑːrɪst/", "吉他手", "guitar"), ("violinist", "/ˌvaɪəˈlɪnɪst/", "小提琴手", "violin"),
                      ("pianist", "/ˈpiːənɪst/", "钢琴家", "piano"), ("drummer", "/ˈdrʌmər/", "鼓手", "drum")]:
    L.node(id, id, ipa, z, **(dict(alt=a, altLabel="来自") if a else {}))
L.grid(["farmer jobs fisherman",
        "trader clerk postman",
        "actor performer actress",
        "director musician drummer",
        "guitarist violinist pianist"], dy=330)
for b in ["farmer", "fisherman", "postman", "trader", "clerk"]:
    L.edge("jobs", b)
L.edge("clerk", "performer", dashed=True); L.edge("performer", "actor"); L.edge("performer", "actress"); L.edge("actor", "director", dashed=True)
L.edge("performer", "musician"); L.edge("musician", "guitarist"); L.edge("musician", "violinist"); L.edge("musician", "pianist"); L.edge("musician", "drummer")

L.seg("title", zh("小朋友们好！还记得第三十五集的职业吗？今天，我们认识更多的职业！"), en("jobs"))
L.seg("map show:jobs focus:jobs", zh("工作："), en("jobs"), zh("今天的秘密：很多职业，就是在一个词后面加上小尾巴。"))
L.seg("show:farmer edge:jobs>farmer focus:farmer alt:farmer", zh("在农场种地的人："), en("farm"), en("farmer"))
L.seg("show:fisherman edge:jobs>fisherman focus:fisherman alt:fisherman", zh("出海打鱼的人。鱼，加上男人："), en("fish"), en("fisherman"))
L.seg("show:postman edge:jobs>postman focus:postman alt:postman", zh("送信的人。邮件，加上男人："), en("post"), en("postman"))
L.seg("show:trader edge:jobs>trader focus:trader alt:trader", zh("做买卖的人。还记得第四十八集的交易 trade 吗？"), en("trade"), en("trader"))
L.seg("show:clerk edge:jobs>clerk focus:clerk", zh("在商店、办公室工作的人，是店员、职员："), en("clerk"))
L.seg("show:performer edge:clerk>performer focus:performer alt:performer", zh("在台上表演的人。表演，加上 e r："), en("perform"), en("performer"))
L.seg("show:actor edge:performer>actor focus:actor alt:actor", zh("演电影的男演员。表演，加上 o r："), en("act"), en("actor"))
L.seg("show:actress edge:performer>actress focus:actress alt:actress", zh("女演员，加上 r e s s："), en("actress"))
L.seg("show:director edge:actor>director focus:director alt:director", zh("指挥大家拍电影的人，是导演："), en("direct"), en("director"))
L.seg("show:musician edge:performer>musician focus:musician alt:musician", zh("做音乐的人，是音乐家。音乐，加上 i a n："), en("music"), en("musician"))
L.seg("show:guitarist edge:musician>guitarist focus:guitarist alt:guitarist", zh("还记得第三十集的乐器吗？弹吉他的人："), en("guitar"), en("guitarist"))
L.seg("show:violinist edge:musician>violinist focus:violinist alt:violinist", zh("拉小提琴的人："), en("violin"), en("violinist"))
L.seg("show:pianist edge:musician>pianist focus:pianist alt:pianist", zh("弹钢琴的人："), en("piano"), en("pianist"))
L.seg("show:drummer edge:musician>drummer focus:drummer alt:drummer", zh("打鼓的人，要多写一个 m："), en("drum"), en("drummer"))
L.seg("focus:guitarist,violinist,pianist", zh("i s t 结尾的三位："), en("guitarist", "focus:guitarist"), en("violinist", "focus:violinist"), en("pianist", "focus:pianist"))
L.seg("focus:farmer,performer,drummer", zh("e r 结尾的三位："), en("farmer", "focus:farmer"), en("performer", "focus:performer"), en("drummer", "focus:drummer"))
L.review([("jobs", "jobs"), ("farmer", "farmer"), ("fisherman", "fisherman"), ("postman", "postman"), ("trader", "trader"), ("clerk", "clerk"),
          ("performer", "performer"), ("actor", "actor"), ("actress", "actress"), ("director", "director"), ("musician", "musician"),
          ("guitarist", "guitarist"), ("violinist", "violinist"), ("pianist", "pianist"), ("drummer", "drummer")],
         "太棒了！你长大想做什么？用英语告诉爸爸妈妈吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
