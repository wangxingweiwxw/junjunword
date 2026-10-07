import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep57", "travel", "旅行", 57, "travel")
L.node("vacation", "vacation", "/veɪˈkeɪʃn/", "假期")
L.node("travel", "travel", "/ˈtrævl/", "旅行", kind="verb")
L.node("agent", "agent", "/ˈeɪdʒənt/", "代理人", alt="travel agent", altLabel="常说")
L.node("passport", "passport", "/ˈpæspɔːrt/", "护照")
L.node("hotel", "hotel", "/hoʊˈtel/", "酒店")
L.node("tour", "tour", "/tʊr/", "游览")
L.node("guide", "guide", "/ɡaɪd/", "导游")
L.node("palace", "palace", "/ˈpæləs/", "宫殿")
L.node("museum", "museum", "/mjuˈziːəm/", "博物馆")
L.node("tower", "tower", "/ˈtaʊər/", "塔")
L.node("island", "island", "/ˈaɪlənd/", "岛")
L.node("beach", "beach", "/biːtʃ/", "海滩")
L.node("map", "map", "/mæp/", "地图")
L.grid(["passport vacation hotel",
        "agent travel tour",
        "map island guide",
        "beach palace museum",
        ". . tower"], dy=330)
L.edge("vacation", "travel"); L.edge("travel", "agent"); L.edge("travel", "passport", dashed=True); L.edge("vacation", "hotel", dashed=True)
L.edge("travel", "tour"); L.edge("tour", "guide"); L.edge("guide", "museum"); L.edge("guide", "palace"); L.edge("museum", "tower")
L.edge("travel", "island"); L.edge("island", "beach"); L.edge("island", "map", dashed=True)

L.seg("title", zh("小朋友们好！暑假到了，我们一起去旅行吧！"), en("travel"))
L.seg("map show:vacation focus:vacation", zh("长长的假期，英语是"), en("vacation"), zh("还记得上一集的 holiday 吗？意思差不多。"))
L.seg("show:travel edge:vacation>travel focus:travel", zh("去远方玩，是旅行："), en("travel"), en("I love to travel."))
L.seg("show:agent edge:travel>agent focus:agent", zh("帮我们安排旅行的人，是旅行社的代理人："), en("agent"), zh("合起来叫", "alt:agent"), en("travel agent"))
L.seg("show:passport edge:travel>passport focus:passport", zh("出国旅行，要带护照。通过，加上港口："), en("pass"), en("port"), en("passport"))
L.seg("show:hotel edge:vacation>hotel focus:hotel", zh("晚上，住在酒店里："), en("hotel"))
L.seg("show:tour edge:travel>tour focus:tour", zh("跟着旅行团，四处游览："), en("tour"))
L.seg("show:guide edge:tour>guide focus:guide", zh("举着小旗子带路的，是导游："), en("guide"), en("Follow the guide!"))
L.seg("show:palace edge:guide>palace focus:palace", zh("导游带我们参观宫殿："), en("palace"))
L.seg("show:museum edge:guide>museum focus:museum", zh("参观博物馆，看古老的宝贝："), en("museum"))
L.seg("show:tower edge:museum>tower focus:tower", zh("爬上高高的塔，看看风景："), en("tower"))
L.seg("show:island edge:travel>island focus:island", zh("坐船去一座小岛："), en("island"), zh("小提示：中间的 s 不发音哦。"))
L.seg("show:beach edge:island>beach focus:beach", zh("岛上有金色的沙滩："), en("beach"), en("I enjoy the sunshine at the beach."))
L.seg("show:map edge:island>map focus:map", zh("迷路了，看看地图："), en("map"))
L.seg("focus:none", zh("说一说你的旅行计划吧！"))
L.seg("", en("I will travel to an island.", "focus:travel,island"), en("I will stay at a hotel.", "focus:hotel"),
      en("I will visit a museum and a palace!", "focus:museum,palace"))
L.review([("vacation", "vacation"), ("travel", "travel"), ("agent", "agent"), ("passport", "passport"), ("hotel", "hotel"), ("tour", "tour"),
          ("guide", "guide"), ("palace", "palace"), ("museum", "museum"), ("tower", "tower"), ("island", "island"), ("beach", "beach"), ("map", "map")],
         "太棒了！你最想去哪里旅行？用英语告诉爸爸妈妈吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
