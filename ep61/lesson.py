import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep61", "fruit", "水果蔬菜", 61, "fruit")
L.node("fruit", "fruit", "/fruːt/", "水果")
for id, ipa, z, pl in [("apple", "/ˈæpl/", "苹果", None), ("banana", "/bəˈnænə/", "香蕉", None), ("strawberry", "/ˈstrɔːberi/", "草莓", ("strawberries", "/ˈstrɔːberiz/")),
                       ("watermelon", "/ˈwɔːtərmelən/", "西瓜", None), ("pear", "/per/", "梨", None), ("grape", "/ɡreɪp/", "葡萄", ("grapes", "/ɡreɪps/")), ("lemon", "/ˈlemən/", "柠檬", None),
                       ("vegetable", "/ˈvedʒtəbl/", "蔬菜", ("vegetables", "/ˈvedʒtəblz/")), ("potato", "/pəˈteɪtoʊ/", "土豆", ("potatoes", "/pəˈteɪtoʊz/")),
                       ("carrot", "/ˈkærət/", "胡萝卜", None), ("onion", "/ˈʌnjən/", "洋葱", None), ("tomato", "/təˈmeɪtoʊ/", "西红柿", ("tomatoes", "/təˈmeɪtoʊz/")),
                       ("bean", "/biːn/", "豆子", None), ("cabbage", "/ˈkæbɪdʒ/", "卷心菜", None)]:
    L.node(id, id, ipa, z, **(dict(plural=pl[0], pluralIpa=pl[1]) if pl else {}))
L.node("except", "except", "/ɪkˈsept/", "除了……之外", kind="prep")
L.grid(["apple fruit banana",
        "pear grape strawberry",
        "lemon . watermelon",
        "potato vegetable carrot",
        "onion tomato bean",
        ". cabbage except"], dy=320)
for b in ["apple", "banana", "grape", "pear", "strawberry"]:
    L.edge("fruit", b)
L.edge("pear", "lemon", dashed=True); L.edge("strawberry", "watermelon", dashed=True)
for b in ["potato", "carrot", "tomato", "onion", "bean"]:
    L.edge("vegetable", b)
L.edge("tomato", "cabbage", dashed=True); L.edge("cabbage", "except", dashed=True)

L.seg("title", zh("小朋友们好！多吃水果和蔬菜，身体棒棒的！今天，我们来认识它们。"), en("fruit and vegetables"))
L.seg("map show:fruit focus:fruit", zh("甜甜的水果，英语是"), en("fruit"), zh("中间的 u i，只读一个长长的 u。"))
L.seg("show:apple edge:fruit>apple focus:apple", zh("红红的苹果："), en("apple"), zh("开头是元音，所以要说"), en("an apple"))
L.seg("show:banana edge:fruit>banana focus:banana", zh("弯弯的香蕉："), en("banana"), zh("三个 a，重音在中间。"))
L.seg("show:grape edge:fruit>grape focus:grape", zh("一串一串的葡萄："), en("grape"), zh("一串有很多颗：", "plural:grape"), en("grapes"))
L.seg("show:pear edge:fruit>pear focus:pear", zh("水水的梨："), en("pear"), zh("它和熊 bear 只差一个字母哦。"))
L.seg("show:lemon edge:pear>lemon focus:lemon", zh("酸酸的柠檬。还记得第十七集的酸吗？"), en("lemon"), en("Lemons are sour."))
L.seg("show:strawberry edge:fruit>strawberry focus:strawberry", zh("红红的草莓。稻草，加上浆果："), en("straw"), en("berry"), en("strawberry"))
L.seg("show:watermelon edge:strawberry>watermelon focus:watermelon", zh("夏天最爱的大西瓜。水，加上瓜："), en("water"), en("melon"), en("watermelon"),
      en("I eat watermelon in the summer."))
L.seg("show:vegetable focus:vegetable", zh("绿油油的蔬菜，英语是"), en("vegetable"), zh("中间的 e t a 读得很快："), en("veg, ta, ble"))
L.seg("show:potato edge:vegetable>potato focus:potato", zh("圆滚滚的土豆："), en("potato"))
L.seg("show:carrot edge:vegetable>carrot focus:carrot", zh("小兔子爱吃的胡萝卜："), en("carrot"))
L.seg("show:tomato edge:vegetable>tomato focus:tomato", zh("红红的西红柿："), en("tomato"))
L.seg("show:onion edge:vegetable>onion focus:onion", zh("一切就让人流眼泪的洋葱："), en("onion"))
L.seg("show:bean edge:vegetable>bean focus:bean", zh("长长的豆荚里，有一颗颗豆子："), en("bean"))
L.seg("show:cabbage edge:tomato>cabbage focus:cabbage", zh("一层一层的卷心菜："), en("cabbage"))
L.seg("focus:potato,tomato", zh("小心！土豆和西红柿变成很多个的时候，要加 e s："),
      en("potato, potatoes", "plural:potato focus:potato"), en("tomato, tomatoes", "plural:tomato focus:tomato"))
L.seg("show:except edge:cabbage>except focus:except", zh("除了……之外，英语是"), en("except"), en("I like all vegetables except onions.", "focus:except,onion"))
L.seg("focus:strawberry", zh("草莓很多个，要把 y 变成 i e s："), en("strawberries", "plural:strawberry"), en("vegetables", "plural:vegetable focus:vegetable"))
L.review([("fruit", "fruit"), ("apple", "apple"), ("banana", "banana"), ("grape", "grape, grapes"), ("pear", "pear"), ("lemon", "lemon"),
          ("strawberry", "strawberry"), ("watermelon", "watermelon"), ("vegetable", "vegetable"), ("potato", "potato, potatoes"), ("carrot", "carrot"),
          ("tomato", "tomato, tomatoes"), ("onion", "onion"), ("bean", "bean"), ("cabbage", "cabbage"), ("except", "except")],
         "太棒了！今天吃饭的时候，用英语说一说你吃了哪些水果和蔬菜吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
