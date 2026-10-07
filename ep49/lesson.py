import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep49", "accessories", "配饰", 49, "handbag")
L.node("clothes", "clothes", "/kloʊðz/", "衣服")
L.node("shop", "shop", "/ʃɑːp/", "商店", icon="store")
L.node("available", "available", "/əˈveɪləbl/", "有空的；可获得的", kind="adj")
L.node("bring", "bring", "/brɪŋ/", "带来", kind="verb")
L.node("suit", "suit", "/suːt/", "西装")
L.node("tie", "tie", "/taɪ/", "领带")
L.node("earring", "earring", "/ˈɪrɪŋ/", "耳环", plural="earrings", pluralIpa="/ˈɪrɪŋz/")
L.node("scarf", "scarf", "/skɑːrf/", "围巾")
L.node("glove", "glove", "/ɡlʌv/", "手套", plural="gloves", pluralIpa="/ɡlʌvz/")
L.node("ring", "ring", "/rɪŋ/", "戒指")
L.node("bag", "bag", "/bæɡ/", "包")
L.node("handbag", "handbag", "/ˈhændbæɡ/", "手提包")
L.node("purse", "purse", "/pɜːrs/", "钱包（女式）")
L.node("wallet", "wallet", "/ˈwɑːlɪt/", "钱包（男式）")
L.grid(["available shop bring",
        "earring clothes suit",
        "scarf ring tie",
        "glove bag handbag",
        "purse wallet ."], dy=330)
L.edge("shop", "clothes"); L.edge("available", "shop", dashed=True); L.edge("bring", "suit"); L.edge("clothes", "earring", "耳朵上")
L.edge("clothes", "scarf", "脖子上"); L.edge("clothes", "ring", "手指上"); L.edge("suit", "tie"); L.edge("scarf", "glove", dashed=True)
L.edge("bag", "handbag", "hand+"); L.edge("purse", "wallet", "都是钱包"); L.edge("clothes", "bag")

L.seg("title", zh("小朋友们好！还记得第十集的衣服吗？今天，我们来学衣服的好搭档，配饰！"), en("accessories"))
L.seg("map show:clothes focus:clothes", zh("衣服："), en("clothes"))
L.seg("show:shop edge:shop>clothes focus:shop", zh("我们去服装店逛一逛。商店，也可以说"), en("shop"), en("a clothes shop"))
L.seg("show:available edge:available>shop focus:available", zh("周六你有空吗？有空的，英语是"), en("available"), en("Are you available on Saturday?"))
L.seg("show:earring edge:clothes>earring focus:earring", zh("耳朵上戴的，是耳环。耳朵，加上环："), en("ear"), en("ring"), en("earring"),
      zh("两只耳朵，一对耳环：", "plural:earring"), en("earrings"))
L.seg("show:scarf edge:clothes>scarf focus:scarf", zh("冬天脖子上围的，是围巾："), en("scarf"))
L.seg("show:glove edge:scarf>glove focus:glove", zh("手上戴的，是手套："), en("glove"), zh("一双手套：", "plural:glove"), en("a pair of gloves"))
L.seg("show:ring edge:clothes>ring focus:ring", zh("手指上戴的，是戒指："), en("ring"))
L.seg("show:bring focus:bring", zh("爸爸要去参加聚会，快把西装带来！带来，英语是"), en("bring"))
L.seg("show:suit edge:bring>suit focus:suit", zh("西装："), en("suit"))
L.seg("show:tie edge:suit>tie focus:tie", zh("穿西装，要系一条领带："), en("tie"), en("Can you tie a tie?"))
L.seg("show:bag edge:clothes>bag focus:bag", zh("出门要背一个包："), en("bag"))
L.seg("show:handbag edge:bag>handbag focus:handbag", zh("提在手里的，是手提包。手，加上包："), en("hand"), en("bag"), en("handbag"))
L.seg("show:purse focus:purse", zh("装钱的，是钱包。妈妈用的小钱包，常叫"), en("purse"))
L.seg("show:wallet edge:purse>wallet focus:wallet", zh("爸爸放在口袋里的，常叫"), en("wallet"))
L.seg("focus:earring,handbag", zh("今天的拼词："), en("ear, ring, earring", "focus:earring"), en("hand, bag, handbag", "focus:handbag"))
L.seg("focus:none", zh("你今天戴了什么？"))
L.seg("", en("I wear a scarf.", "focus:scarf"), en("I wear gloves.", "focus:glove"), en("And I bring my bag!", "focus:bring,bag"))
L.review([("clothes", "clothes"), ("shop", "shop"), ("available", "available"), ("earring", "earring, earrings"), ("scarf", "scarf"),
          ("glove", "glove, gloves"), ("ring", "ring"), ("bring", "bring"), ("suit", "suit"), ("tie", "tie"), ("bag", "bag"), ("handbag", "handbag"),
          ("purse", "purse"), ("wallet", "wallet")],
         "太棒了！出门前，用英语说一说你要带什么吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
