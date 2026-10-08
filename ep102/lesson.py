import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep102", "space", "太空", 102, "space")
L.node("space", "space", "/speɪs/", "太空")
L.node("planet", "planet", "/ˈplænɪt/", "行星")
L.node("world", "world", "/wɜːrld/", "世界")
L.node("earth", "Earth", "/ɜːrθ/", "地球")
L.node("equator", "equator", "/ɪˈkweɪtər/", "赤道")
L.node("star", "star", "/stɑːr/", "星星")
L.node("sky", "sky", "/skaɪ/", "天空")
L.node("astronaut", "astronaut", "/ˈæstrənɔːt/", "宇航员")
L.node("beyond", "beyond", "/bɪˈjɑːnd/", "在……之外", kind="prep")
L.node("rocket", "rocket", "/ˈrɑːkɪt/", "火箭")
L.node("require", "require", "/rɪˈkwaɪər/", "需要", kind="verb")
L.node("moon", "moon", "/muːn/", "月亮")
L.node("moonlight", "moonlight", "/ˈmuːnlaɪt/", "月光")
L.grid(["world planet equator",
        "earth space astronaut",
        "moon require beyond",
        "moonlight rocket sky",
        ". . star"], dy=330)
for id, x, y in [("moonlight", 170, 150), ("world", 520, 150), ("planet", 870, 150), ("equator", 1220, 150),
                 ("moon", 170, 470), ("earth", 520, 470), ("space", 870, 470), ("astronaut", 1220, 470), ("beyond", 1570, 470),
                 ("rocket", 520, 790), ("require", 870, 790), ("star", 1220, 790), ("sky", 1570, 790)]:
    L.byid[id]["at"] = [x, y]
L.edge("space", "planet"); L.edge("planet", "equator", dashed=True); L.edge("space", "world", dashed=True); L.edge("space", "earth"); L.edge("earth", "moon")
L.edge("moon", "moonlight"); L.edge("space", "astronaut"); L.edge("astronaut", "beyond"); L.edge("beyond", "sky", dashed=True); L.edge("sky", "star")
L.edge("space", "require", dashed=True); L.edge("require", "rocket")

L.seg("title", zh("小朋友们好！坐上火箭，我们一起去太空探险吧！"), en("space"))
L.seg("map show:space focus:space", zh("地球外面广阔的地方，是太空："), en("space"))
L.seg("show:planet edge:space>planet focus:planet", zh("绕着太阳转的大星球，是行星："), en("planet"))
L.seg("show:equator edge:planet>equator focus:equator", zh("地球中间那条看不见的线，是赤道："), en("equator"), zh("赤道附近特别热。"))
L.seg("show:world edge:space>world focus:world", zh("我们生活的整个世界："), en("world"))
L.seg("show:earth edge:space>earth focus:earth", zh("我们住的星球，是地球："), en("Earth"), zh("还记得上一集的地震 earthquake 吗？earth 就在里面。"))
L.seg("show:moon edge:earth>moon focus:moon", zh("离地球最近的，是月亮："), en("moon"))
L.seg("show:moonlight edge:moon>moonlight focus:moonlight", zh("月亮，加上光，就是月光："), en("moon"), en("light"), en("moonlight"))
L.seg("show:astronaut edge:space>astronaut focus:astronaut", zh("飞上太空的人，是宇航员："), en("astronaut"))
L.seg("show:beyond edge:astronaut>beyond focus:beyond", zh("宇航员飞得很高，到了天空之外："), en("beyond"), en("beyond the sky"))
L.seg("show:sky edge:beyond>sky focus:sky", zh("天空，英语是"), en("sky"))
L.seg("show:star edge:sky>star focus:star", zh("天空里一闪一闪的星星："), en("star"))
L.seg("show:require edge:space>require focus:require", zh("去太空，需要很多东西："), en("require"))
L.seg("show:rocket edge:require>rocket focus:rocket", zh("最需要的，是一枚火箭："), en("rocket"), en("Going to space requires a rocket."))
L.seg("focus:none", zh("我们一起倒数，发射火箭吧！"))
L.seg("", en("Ten, nine, eight…", "focus:rocket"), en("three, two, one…"), en("Blast off!", "focus:space"))
L.review([("space", "space"), ("planet", "planet"), ("equator", "equator"), ("world", "world"), ("earth", "Earth"), ("moon", "moon"), ("moonlight", "moonlight"),
          ("astronaut", "astronaut"), ("beyond", "beyond"), ("sky", "sky"), ("star", "star"), ("require", "require"), ("rocket", "rocket")],
         "太棒了！今天晚上，抬头看看天上的月亮和星星吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
