import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep43", "town", "城镇", 43, "town")
L.node("town", "town", "/taʊn/", "城镇")
L.node("village", "village", "/ˈvɪlɪdʒ/", "村庄")
L.node("square", "square", "/skwer/", "广场")
L.node("show", "show", "/ʃoʊ/", "演出；表演")
L.node("cinema", "cinema", "/ˈsɪnəmə/", "电影院")
L.node("restaurant", "restaurant", "/ˈrestərɑːnt/", "餐厅")
L.node("mall", "mall", "/mɔːl/", "购物中心")
L.node("supermarket", "supermarket", "/ˈsuːpərmɑːrkɪt/", "超市")
L.node("bookstore", "bookstore", "/ˈbʊkstɔːr/", "书店")
L.node("zoo", "zoo", "/zuː/", "动物园")
L.node("street", "street", "/striːt/", "街道")
L.node("crossing", "crossing", "/ˈkrɔːsɪŋ/", "人行横道")
L.node("cross", "cross", "/krɔːs/", "穿过", kind="verb")
L.node("open", "open", "/ˈoʊpən/", "开着的", kind="adj")
L.node("closed", "closed", "/kloʊzd/", "关着的", kind="adj", alt="close", altLabel="来自")
L.grid(["village town square",
        "cinema restaurant show",
        "mall supermarket bookstore",
        "zoo street open",
        "crossing cross closed"], dy=330)
L.edge("town", "village", "更小"); L.edge("town", "square"); L.edge("square", "show", "看"); L.edge("town", "restaurant")
L.edge("restaurant", "cinema"); L.edge("town", "supermarket", dashed=True); L.edge("supermarket", "mall"); L.edge("supermarket", "bookstore")
L.edge("street", "zoo", dashed=True); L.edge("street", "crossing"); L.edge("crossing", "cross"); L.edge("open", "closed", "反义")

L.seg("title", zh("小朋友们好！周末，我们一起逛一逛城镇吧！"), en("town"))
L.seg("map show:town focus:town", zh("有很多房子、商店和街道的地方，是城镇："), en("town"))
L.seg("show:village edge:town>village focus:village", zh("比城镇更小、在乡下的，是村庄："), en("village"))
L.seg("show:square edge:town>square focus:square", zh("城镇中间，有一个大大的广场："), en("square"), zh("这个词也是正方形的意思。"))
L.seg("show:show edge:square>show focus:show", zh("广场上正在表演节目："), en("show"), en("Let's watch the show!"))
L.seg("show:restaurant edge:town>restaurant focus:restaurant", zh("饿了，就去餐厅吃饭："), en("restaurant"))
L.seg("show:cinema edge:restaurant>cinema focus:cinema", zh("吃完饭，去电影院看电影："), en("cinema"))
L.seg("show:supermarket edge:town>supermarket focus:supermarket", zh("买吃的、用的，去超市。超级，加上市场："), en("super"), en("market"), en("supermarket"))
L.seg("show:mall edge:supermarket>mall focus:mall", zh("有很多很多商店的大楼，是购物中心："), en("mall"))
L.seg("show:bookstore edge:supermarket>bookstore focus:bookstore", zh("卖书的商店，是书店。书，加上商店："), en("book"), en("store"), en("bookstore"))
L.seg("show:street focus:street", zh("路两边都是房子的，是街道："), en("street"))
L.seg("show:zoo edge:street>zoo focus:zoo", zh("沿着街道走，就到了动物园："), en("zoo"))
L.seg("show:crossing edge:street>crossing focus:crossing", zh("过马路，要走人行横道："), en("crossing"))
L.seg("show:cross edge:crossing>cross focus:cross", zh("穿过马路，英语是"), en("cross"), en("Cross the street carefully."))
L.seg("show:open focus:open", zh("商店门口挂着牌子。开着门，是"), en("open"))
L.seg("show:closed edge:open>closed focus:closed", zh("关门了，是"), en("closed"),
      zh("它来自关上：", "alt:closed"), en("close"), en("The store is closed."))
L.seg("focus:none", zh("说一说，你周末想去哪里？"))
L.seg("", en("Let's go to the cinema.", "focus:cinema"), en("Let's go to the zoo.", "focus:zoo"), en("Let's go to the bookstore!", "focus:bookstore"))
L.review([("town", "town"), ("village", "village"), ("square", "square"), ("show", "show"), ("restaurant", "restaurant"), ("cinema", "cinema"),
          ("supermarket", "supermarket"), ("mall", "mall"), ("bookstore", "bookstore"), ("street", "street"), ("zoo", "zoo"),
          ("crossing", "crossing"), ("cross", "cross"), ("open", "open"), ("closed", "closed")],
         "太棒了！下次逛街的时候，用英语说一说你看到的地方吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
