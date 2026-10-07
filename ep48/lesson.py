import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep48", "shopping", "购物", 48, "shopping")
V, A = dict(kind="verb"), dict(kind="adj")
L.node("store", "store", "/stɔːr/", "商店")
L.node("buy", "buy", "/baɪ/", "买", **V)
L.node("sell", "sell", "/sel/", "卖", **V)
L.node("free", "free", "/friː/", "免费的", **A)
L.node("afford", "afford", "/əˈfɔːrd/", "买得起", **V)
L.node("steal", "steal", "/stiːl/", "偷", **V)
L.node("shopping", "shopping", "/ˈʃɑːpɪŋ/", "购物", alt="shop", altLabel="来自")
L.node("market", "market", "/ˈmɑːrkɪt/", "市场")
L.node("cheap", "cheap", "/tʃiːp/", "便宜的", **A)
L.node("expensive", "expensive", "/ɪkˈspensɪv/", "贵的", **A)
L.node("trade", "trade", "/treɪd/", "交易；交换", **V)
L.node("deal", "deal", "/diːl/", "成交；交易")
L.grid(["sell store buy",
        "free shopping afford",
        "cheap market expensive",
        "trade deal steal"], dy=350)
L.edge("store", "buy"); L.edge("store", "sell"); L.edge("store", "shopping"); L.edge("shopping", "free", dashed=True); L.edge("shopping", "afford")
L.edge("shopping", "market"); L.edge("market", "cheap"); L.edge("market", "expensive"); L.edge("market", "trade"); L.edge("trade", "deal")
L.edge("afford", "steal", "买不起也不能", dashed=True)

L.seg("title", zh("小朋友们好！和妈妈一起去逛街买东西吧！"), en("shopping"))
L.seg("map show:store focus:store", zh("卖东西的地方，是商店："), en("store"), zh("还记得第四十三集的书店 bookstore 吗？"))
L.seg("show:buy edge:store>buy focus:buy", zh("花钱买东西，是"), en("buy"), en("I want to buy a toy."))
L.seg("show:sell edge:store>sell focus:sell", zh("把东西卖给别人，是"), en("sell"), zh("买和卖，正好相反："), en("buy", "focus:buy"), en("sell", "focus:sell"))
L.seg("show:shopping edge:store>shopping focus:shopping", zh("逛商店买东西，是购物："), en("shopping"),
      zh("它来自", "alt:shopping"), en("shop"), zh("要多写一个 p，再加上 i n g。"), en("Let's go shopping!"))
L.seg("show:free edge:shopping>free focus:free", zh("不要钱，是免费的："), en("free"), en("It's free!"))
L.seg("show:afford edge:shopping>afford focus:afford", zh("钱够了，买得起，英语是"), en("afford"), en("I can afford it."))
L.seg("show:market edge:shopping>market focus:market", zh("很多小摊子挤在一起，是市场："), en("market"), zh("还记得超市 supermarket 吗？"))
L.seg("show:cheap edge:market>cheap focus:cheap", zh("价钱低，是便宜的："), en("cheap"))
L.seg("show:expensive edge:market>expensive focus:expensive", zh("价钱高，是贵的："), en("expensive"),
      zh("便宜和贵："), en("cheap", "focus:cheap"), en("expensive", "focus:expensive"))
L.seg("show:trade edge:market>trade focus:trade", zh("用我的东西，换你的东西，是交换、交易："), en("trade"))
L.seg("show:deal edge:trade>deal focus:deal", zh("双方都同意了，握握手，成交！"), en("deal"), en("It's a deal!"))
L.seg("show:steal edge:afford>steal focus:steal", zh("买不起的东西，也绝对不能偷。偷，英语是"), en("steal"), en("Never steal!"))
L.seg("focus:none", zh("我们来演一演买东西吧！"))
L.seg("", en("How much is it?", "focus:store"), en("It's ten yuan.", "focus:cheap"), en("That's cheap! I'll buy it.", "focus:buy"),
      en("Deal!", "focus:deal"))
L.review([("store", "store"), ("buy", "buy"), ("sell", "sell"), ("shopping", "shopping"), ("free", "free"), ("afford", "afford"), ("market", "market"),
          ("cheap", "cheap"), ("expensive", "expensive"), ("trade", "trade"), ("deal", "deal"), ("steal", "steal")],
         "太棒了！下次去商店，用英语问一问 How much is it 吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
