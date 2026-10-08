import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep87", "sweets", "甜食", 87, "icecream")
L.node("sweet", "sweet", "/swiːt/", "甜的；糖果", kind="adj")
for id, w, ipa, z in [("sugar", "sugar", "/ˈʃʊɡər/", "糖"), ("honey", "honey", "/ˈhʌni/", "蜂蜜"), ("biscuit", "biscuit", "/ˈbɪskɪt/", "饼干"), ("candy", "candy", "/ˈkændi/", "糖果"),
                      ("icecream", "ice cream", "/ˌaɪs ˈkriːm/", "冰淇淋"), ("cake", "cake", "/keɪk/", "蛋糕"), ("chocolate", "chocolate", "/ˈtʃɔːklət/", "巧克力"), ("cream", "cream", "/kriːm/", "奶油")]:
    L.node(id, w, ipa, z)
L.node("little", "little", "/ˈlɪtl/", "一点；少量", alt="a little", altLabel="常说")
L.grid(["sugar honey biscuit",
        "candy sweet icecream",
        "cake chocolate cream",
        ". little ."], dy=350)
for b in ["sugar", "honey", "biscuit", "candy", "icecream", "cake", "chocolate", "cream"]:
    L.edge("sweet", b)
L.edge("chocolate", "little", dashed=True)

L.seg("title", zh("小朋友们好！谁不爱吃甜甜的东西呢？今天，我们来学甜食！"), en("sweets"))
L.seg("map show:sweet focus:sweet", zh("还记得第十七集的甜吗？"), en("sweet"), zh("在英国，糖果也叫 sweets。"))
L.seg("show:sugar edge:sweet>sugar focus:sugar", zh("甜甜的糖："), en("sugar"), zh("开头的 s 读成 sh，很特别哦。"))
L.seg("show:honey edge:sweet>honey focus:honey", zh("小蜜蜂酿的蜂蜜："), en("honey"))
L.seg("show:biscuit edge:sweet>biscuit focus:biscuit", zh("脆脆的饼干："), en("biscuit"), zh("中间的 u 不发音。在美国常叫 cookie。"))
L.seg("show:candy edge:sweet>candy focus:candy", zh("五颜六色的糖果："), en("candy"))
L.seg("show:icecream edge:sweet>icecream focus:icecream", zh("夏天最爱的冰淇淋。冰，加上奶油："), en("ice"), en("cream"), en("ice cream"))
L.seg("show:cake edge:sweet>cake focus:cake", zh("还记得第四集生日的蛋糕吗？"), en("cake"))
L.seg("show:chocolate edge:sweet>chocolate focus:chocolate", zh("浓浓的巧克力："), en("chocolate"), zh("中间的 o 读得很轻，常常听不到。"))
L.seg("show:cream edge:sweet>cream focus:cream", zh("蛋糕上白白的奶油："), en("cream"))
L.seg("show:little edge:chocolate>little focus:little", zh("甜食好吃，但只能吃一点点哦。一点，英语是"), en("a little"),
      en("Just a little chocolate, please.", "focus:little,chocolate"), zh("吃太多糖，牙齿会疼的。"))
L.seg("focus:none", zh("你最喜欢哪一种甜食？"))
L.seg("", en("I like ice cream.", "focus:icecream"), en("I like chocolate cake.", "focus:chocolate,cake"), en("But just a little!", "focus:little"))
L.review([("sweet", "sweet"), ("sugar", "sugar"), ("honey", "honey"), ("biscuit", "biscuit"), ("candy", "candy"), ("icecream", "ice cream"), ("cake", "cake"),
          ("chocolate", "chocolate"), ("cream", "cream"), ("little", "a little")],
         "太棒了！甜食虽好，可不要贪吃，吃完记得刷牙哦。点一点图上的单词，还能再听一遍发音。")
L.save()
