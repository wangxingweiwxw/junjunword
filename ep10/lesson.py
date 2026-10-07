import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep10", "clothes", "衣服", 10, "clothes")
L.node("clothes", "clothes", "/kloʊðz/", "衣服")
L.node("wear", "wear", "/wer/", "穿；戴", kind="verb")
L.node("hat", "hat", "/hæt/", "帽子")
L.node("cap", "cap", "/kæp/", "鸭舌帽")
L.node("tshirt", "T-shirt", "/ˈtiː ʃɜːrt/", "T恤衫")
L.node("underwear", "underwear", "/ˈʌndərwer/", "内衣；内裤")
L.node("trousers", "trousers", "/ˈtraʊzərz/", "裤子")
L.node("sock", "sock", "/sɑːk/", "袜子", plural="socks", pluralIpa="/sɑːks/")
L.node("shoe", "shoe", "/ʃuː/", "鞋子", plural="shoes", pluralIpa="/ʃuːz/")
L.node("pair", "pair", "/per/", "一双；一对")
L.grid(["hat tshirt underwear",
        "cap clothes trousers",
        "wear shoe sock",
        ". pair ."], dy=330)
L.edge("wear", "clothes"); L.edge("clothes", "hat"); L.edge("hat", "cap", "只有帽舌"); L.edge("clothes", "tshirt")
L.edge("clothes", "underwear"); L.edge("clothes", "trousers"); L.edge("clothes", "sock"); L.edge("clothes", "shoe")
L.edge("pair", "shoe", dashed=True); L.edge("pair", "sock", dashed=True)

L.seg("title", zh("小朋友们好！早上起床，我们要穿上漂亮的衣服。"), en("clothes"), zh("衣服。"))
L.seg("map show:clothes focus:clothes", zh("身上穿的各种衣服，合在一起，叫"), en("clothes"),
      zh("它中间的 t h，舌尖要轻轻碰一下牙齿。"), en("These are my clothes."))
L.seg("show:wear edge:wear>clothes focus:wear", zh("把衣服穿在身上，把帽子戴在头上，都用同一个词："), en("wear"), en("I wear a coat."))
L.seg("show:hat edge:clothes>hat focus:hat", zh("我们从头开始。头上戴的、一圈都有帽檐的帽子："), en("hat"), en("a sun hat"))
L.seg("show:cap edge:hat>cap focus:cap", zh("只在前面有一个帽舌的，是鸭舌帽："), en("cap"), en("a red cap"))
L.seg("focus:hat,cap", zh("一圈都有帽檐，是"), en("hat", "focus:hat"), zh("只有前面的帽舌，是", "focus:cap"), en("cap"))
L.seg("show:tshirt edge:clothes>tshirt focus:tshirt", zh("身上穿的短袖衫，摊开来像一个大写字母 T，所以叫"), en("T-shirt"), en("a white T-shirt"))
L.seg("show:underwear edge:clothes>underwear focus:underwear", zh("贴着身体穿在最里面的，是内衣。下面，加上穿："),
      en("under"), en("wear"), en("underwear"))
L.seg("show:trousers edge:clothes>trousers focus:trousers", zh("两条腿穿的长长的，是裤子："), en("trousers"),
      zh("裤子有两条裤腿，所以这个词总是带着字母 s。"))
L.seg("show:sock edge:clothes>sock focus:sock", zh("脚上，先穿袜子："), en("sock"))
L.seg("show:shoe edge:clothes>shoe focus:shoe", zh("再穿上鞋子："), en("shoe"), en("Put on your shoes!"))
L.seg("show:pair edge:pair>sock edge:pair>shoe focus:pair", zh("袜子和鞋子，都是两只一起穿。两只配成一对，叫"), en("pair"),
      en("a pair of socks", "focus:pair,sock"), en("a pair of shoes", "focus:pair,shoe"),
      zh("裤子也一样，要说一条裤子：", "focus:pair,trousers"), en("a pair of trousers"))
L.seg("focus:sock", zh("很多只袜子、很多只鞋，在后面加上字母 s："),
      en("sock", "focus:sock"), en("socks", "plural:sock"), en("shoe", "focus:shoe"), en("shoes", "plural:shoe"))
L.seg("focus:none", zh("我们一起来穿衣服吧！从里到外，从头到脚！"))
L.seg("", en("underwear", "focus:underwear"), en("T-shirt", "focus:tshirt"), en("trousers", "focus:trousers"),
      en("socks", "focus:sock"), en("shoes", "focus:shoe"), en("and a cap!", "focus:cap"))
L.review([("clothes", "clothes"), ("wear", "wear"), ("hat", "hat"), ("cap", "cap"), ("tshirt", "T-shirt"),
          ("underwear", "underwear"), ("trousers", "trousers"), ("sock", "sock, socks"), ("shoe", "shoe, shoes"),
          ("pair", "pair")],
         "太棒了！明天早上穿衣服的时候，一边穿，一边用英语说出来吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
