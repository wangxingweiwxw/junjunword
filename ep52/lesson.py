import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep52", "transport", "交通（二）", 52, "traffic")
L.node("airport", "airport", "/ˈerpɔːrt/", "机场")
L.node("flight", "flight", "/flaɪt/", "航班")
L.node("arrive", "arrive", "/əˈraɪv/", "到达", kind="verb")
L.node("narrowly", "narrowly", "/ˈnæroʊli/", "勉强地；差一点", kind="adv")
L.node("drive", "drive", "/draɪv/", "开车", kind="verb", alt="driver", altLabel="加 r →")
L.node("license", "license", "/ˈlaɪsns/", "执照；驾照")
L.node("wheel", "wheel", "/wiːl/", "轮子")
L.node("taxi", "taxi", "/ˈtæksi/", "出租车")
L.node("traffic", "traffic", "/ˈtræfɪk/", "交通；车流")
L.node("underground", "underground", "/ˈʌndərɡraʊnd/", "地铁", icon="subway")
L.node("station", "station", "/ˈsteɪʃn/", "车站", alt="train station", altLabel="常说")
L.node("railway", "railway", "/ˈreɪlweɪ/", "铁路")
L.node("tunnel", "tunnel", "/ˈtʌnl/", "隧道")
L.node("bridge", "bridge", "/brɪdʒ/", "桥")
L.grid(["airport flight arrive",
        "license drive narrowly",
        "wheel taxi traffic",
        "underground station railway",
        "bridge . tunnel"], dy=330)
L.edge("airport", "flight"); L.edge("flight", "arrive"); L.edge("arrive", "narrowly", dashed=True); L.edge("license", "drive", "要有")
L.edge("drive", "taxi"); L.edge("taxi", "wheel", dashed=True); L.edge("taxi", "traffic"); L.edge("station", "underground"); L.edge("station", "railway")
L.edge("railway", "tunnel"); L.edge("underground", "bridge", dashed=True)

L.seg("title", zh("小朋友们好！还记得第二十五集的交通工具吗？今天，我们学更多出行的单词。"), en("transportation"))
L.seg("map show:airport focus:airport", zh("坐飞机，先去机场。空中，加上港口："), en("air"), en("port"), en("airport"))
L.seg("show:flight edge:airport>flight focus:flight", zh("每一班飞机，叫航班："), en("flight"), zh("还记得飞 fly 吗？g h 不发音。"))
L.seg("show:arrive edge:flight>arrive focus:arrive", zh("飞机降落，我们到达了："), en("arrive"), en("We arrive in Beijing."))
L.seg("show:narrowly edge:arrive>narrowly focus:narrowly", zh("差一点就没赶上，勉强地，英语是"), en("narrowly"), en("We narrowly caught the flight."))
L.seg("show:drive focus:drive", zh("开汽车，是"), en("drive"), zh("加上 r，就是开车的人，司机：", "alt:drive"), en("driver"))
L.seg("show:license edge:license>drive focus:license", zh("大人开车，要先考一个驾照："), en("license"), en("a driver's license"))
L.seg("show:taxi edge:drive>taxi focus:taxi", zh("路边招手，坐出租车："), en("taxi"))
L.seg("show:wheel edge:taxi>wheel focus:wheel", zh("汽车跑起来，靠四个轮子："), en("wheel"), zh("开头的 w h，只读 w。"))
L.seg("show:traffic edge:taxi>traffic focus:traffic", zh("路上车来车往，是交通："), en("traffic"), en("There is a lot of traffic."))
L.seg("show:station focus:station", zh("坐火车，要去车站："), en("station"), zh("火车站常常说成", "alt:station"), en("train station"))
L.seg("show:underground edge:station>underground focus:underground", zh("在英国，地铁叫"), en("underground"),
      zh("在下面，加上地面。还记得美国叫什么吗？"), en("subway"))
L.seg("show:railway edge:station>railway focus:railway", zh("火车跑的路，是铁路："), en("railway"))
L.seg("show:tunnel edge:railway>tunnel focus:tunnel", zh("铁路穿过大山，要钻隧道："), en("tunnel"))
L.seg("show:bridge edge:underground>bridge focus:bridge", zh("跨过大河，要过桥："), en("bridge"))
L.seg("focus:airport,railway,underground", zh("今天的拼词："),
      en("air, port, airport", "focus:airport"), en("rail, way, railway", "focus:railway"), en("under, ground, underground", "focus:underground"))
L.review([("airport", "airport"), ("flight", "flight"), ("arrive", "arrive"), ("narrowly", "narrowly"), ("drive", "drive, driver"),
          ("license", "license"), ("taxi", "taxi"), ("wheel", "wheel"), ("traffic", "traffic"), ("station", "station"), ("underground", "underground"),
          ("railway", "railway"), ("tunnel", "tunnel"), ("bridge", "bridge")],
         "太棒了！下次出门，用英语说一说你坐的是什么交通工具吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
