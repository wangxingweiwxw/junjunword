import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep85", "community", "社区", 85, "community")
L.node("community", "community", "/kəˈmjuːnəti/", "社区")
L.node("neighborhood", "neighborhood", "/ˈneɪbərhʊd/", "街坊；社区", alt="neighbor", altLabel="来自")
L.node("block", "block", "/blɑːk/", "街区")
L.node("park", "park", "/pɑːrk/", "公园")
L.node("gym", "gym", "/dʒɪm/", "健身房")
L.node("playground", "playground", "/ˈpleɪɡraʊnd/", "操场")
L.node("volunteer", "volunteer", "/ˌvɑːlənˈtɪr/", "志愿者")
L.node("society", "society", "/səˈsaɪəti/", "社会")
L.node("social", "social", "/ˈsoʊʃl/", "社会的", kind="adj")
L.node("garden", "garden", "/ˈɡɑːrdn/", "花园")
L.node("rock", "rock", "/rɑːk/", "石头")
L.node("insect", "insect", "/ˈɪnsekt/", "昆虫")
L.node("butterfly", "butterfly", "/ˈbʌtərflaɪ/", "蝴蝶")
L.node("ant", "ant", "/ænt/", "蚂蚁")
L.grid(["playground volunteer society",
        "gym community social",
        "park block neighborhood",
        "rock garden insect",
        ". butterfly ant"], dy=330)
L.edge("community", "playground"); L.edge("community", "volunteer"); L.edge("community", "gym"); L.edge("community", "block"); L.edge("block", "park", dashed=True); L.edge("block", "neighborhood")
L.edge("society", "social"); L.edge("community", "society", dashed=True); L.edge("garden", "rock"); L.edge("garden", "insect"); L.edge("insect", "ant"); L.edge("garden", "butterfly")
L.edge("park", "garden", dashed=True)

L.seg("title", zh("小朋友们好！我们住的地方，叫社区。今天，我们去社区里逛一逛！"), en("community"))
L.seg("map show:community focus:community", zh("大家住在一起的地方，是社区："), en("community"))
L.seg("show:block edge:community>block focus:block", zh("几条街围起来的一片，是街区："), en("block"))
L.seg("show:neighborhood edge:block>neighborhood focus:neighborhood", zh("邻居们住的这一片。邻居，加上 h o o d："), en("neighbor"), en("neighborhood"), zh("g h 不发音哦。"))
L.seg("show:playground edge:community>playground focus:playground", zh("小朋友玩耍的操场。玩，加上地面："), en("play"), en("ground"), en("playground"))
L.seg("show:gym edge:community>gym focus:gym", zh("锻炼身体的健身房："), en("gym"))
L.seg("show:volunteer edge:community>volunteer focus:volunteer", zh("帮大家捡垃圾、不要报酬的人，是志愿者："), en("volunteer"))
L.seg("show:society edge:community>society focus:society", zh("很多很多社区合在一起，就是社会："), en("society"))
L.seg("show:social edge:society>social focus:social", zh("社会的，英语是"), en("social"))
L.seg("show:park edge:block>park focus:park", zh("街区旁边有一个公园："), en("park"))
L.seg("show:garden edge:park>garden focus:garden", zh("公园里有一个花园："), en("garden"))
L.seg("show:rock edge:garden>rock focus:rock", zh("花园里有大石头："), en("rock"))
L.seg("show:butterfly edge:garden>butterfly focus:butterfly", zh("蝴蝶在花丛中飞舞。黄油，加上飞："), en("butter"), en("fly"), en("butterfly"))
L.seg("show:insect edge:garden>insect focus:insect", zh("草丛里还有很多昆虫："), en("insect"))
L.seg("show:ant edge:insect>ant focus:ant", zh("搬家的小蚂蚁："), en("ant"), zh("开头是元音，所以说"), en("an ant"))
L.seg("focus:playground,butterfly,neighborhood", zh("今天的拼词："), en("play, ground, playground", "focus:playground"), en("butter, fly, butterfly", "focus:butterfly"))
L.review([("community", "community"), ("block", "block"), ("neighborhood", "neighborhood"), ("playground", "playground"), ("gym", "gym"), ("volunteer", "volunteer"),
          ("society", "society"), ("social", "social"), ("park", "park"), ("garden", "garden"), ("rock", "rock"), ("butterfly", "butterfly"), ("insect", "insect"), ("ant", "ant")],
         "太棒了！做一个社区小志愿者，帮大家做点好事吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
