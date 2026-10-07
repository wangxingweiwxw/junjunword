import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep25", "transportation", "交通", 25, "transportation")
A = dict(kind="adj")
L.node("transportation", "transportation", "/ˌtrænspərˈteɪʃn/", "交通运输")
L.node("car", "car", "/kɑːr/", "小汽车")
L.node("truck", "truck", "/trʌk/", "卡车")
L.node("bus", "bus", "/bʌs/", "公共汽车")
L.node("motorbike", "motorbike", "/ˈmoʊtərbaɪk/", "摩托车")
L.node("bicycle", "bicycle", "/ˈbaɪsɪkl/", "自行车", alt="bike", altLabel="简称")
L.node("ride", "ride", "/raɪd/", "骑；乘坐", kind="verb")
L.node("train", "train", "/treɪn/", "火车")
L.node("subway", "subway", "/ˈsʌbweɪ/", "地铁")
L.node("ticket", "ticket", "/ˈtɪkɪt/", "票")
L.node("plane", "plane", "/pleɪn/", "飞机", alt="airplane", altLabel="也叫")
L.node("ship", "ship", "/ʃɪp/", "轮船")
L.node("boat", "boat", "/boʊt/", "小船")
L.node("fast", "fast", "/fæst/", "快的", **A)
L.node("slow", "slow", "/sloʊ/", "慢的", **A)
L.grid(["fast plane slow",
        "car transportation ship",
        "truck bus boat",
        "motorbike bicycle train",
        ". ride subway",
        ". . ticket"], dy=330)
for b in ["plane", "car", "ship", "bus", "truck", "boat"]:
    L.edge("transportation", b)
L.edge("plane", "fast", "很"); L.edge("ship", "slow", "比较"); L.edge("bicycle", "ride"); L.edge("motorbike", "ride")
L.edge("train", "subway", "在地下"); L.edge("subway", "ticket", "要买")

L.seg("title", zh("小朋友们好！出门去远方，要坐什么呢？今天，我们来学交通工具。"), en("transportation"), zh("交通运输。"))
L.seg("map show:transportation focus:transportation", zh("把人和东西从一个地方送到另一个地方，就是交通运输："), en("transportation"),
      zh("这个词很长，我们拆开读："), en("trans, por, ta, tion"), en("transportation"))
L.seg("show:car edge:transportation>car focus:car", zh("路上跑得最多的，是小汽车："), en("car"), en("Dad drives a car."))
L.seg("show:truck edge:transportation>truck focus:truck", zh("拉货的大卡车："), en("truck"))
L.seg("show:bus edge:transportation>bus focus:bus", zh("很多人一起坐的，是公共汽车："), en("bus"), en("I go to school by bus."))
L.seg("show:bicycle focus:bicycle", zh("两个轮子，用脚蹬的，是自行车。二，加上圈圈："), en("bi"), en("cycle"), en("bicycle"),
      zh("平时常常简单地叫它", "alt:bicycle"), en("bike"))
L.seg("show:motorbike focus:motorbike", zh("带着发动机的两轮车，是摩托车。马达，加上自行车："), en("motor"), en("bike"), en("motorbike"))
L.seg("show:ride edge:bicycle>ride edge:motorbike>ride focus:ride", zh("骑自行车、骑摩托车，都用"), en("ride"),
      en("I ride a bike to the park.", "focus:ride,bicycle"))
L.seg("show:train focus:train", zh("在铁轨上跑的长长的车，是火车："), en("train"), en("Choo choo! Here comes the train."))
L.seg("show:subway edge:train>subway focus:subway", zh("在城市的地下跑的火车，是地铁。在下面，加上路："), en("sub"), en("way"), en("subway"))
L.seg("show:ticket edge:subway>ticket focus:ticket", zh("坐地铁、坐火车，都要先买票："), en("ticket"), en("Two tickets, please."))
L.seg("show:plane edge:transportation>plane focus:plane", zh("在天上飞的，是飞机："), en("plane"),
      zh("它的全名是", "alt:plane"), en("airplane"), zh("空气，加上飞机。"))
L.seg("show:ship edge:transportation>ship focus:ship", zh("在大海上航行的大轮船："), en("ship"))
L.seg("show:boat edge:transportation>boat focus:boat", zh("在小河里漂的小船："), en("boat"),
      zh("大的是"), en("ship", "focus:ship"), zh("小的是", "focus:boat"), en("boat"))
L.seg("show:fast edge:plane>fast focus:fast", zh("飞机跑得特别快。快的，英语是"), en("fast"), en("The plane is fast."))
L.seg("show:slow edge:ship>slow focus:slow", zh("轮船走得比较慢，像小蜗牛。慢的，英语是"), en("slow"), en("The ship is slow."))
L.seg("focus:fast,slow", zh("一快一慢："), en("fast", "focus:fast"), en("slow", "focus:slow"))
L.seg("focus:none", zh("说一说，你怎么去这些地方？用 by 加上交通工具："))
L.seg("", en("by bus", "focus:bus"), en("by train", "focus:train"), en("by plane", "focus:plane"), en("by ship", "focus:ship"),
      en("I choose to ride a bike!", "focus:ride,bicycle"))
L.review([("transportation", "transportation"), ("car", "car"), ("truck", "truck"), ("bus", "bus"), ("bicycle", "bicycle, bike"),
          ("motorbike", "motorbike"), ("ride", "ride"), ("train", "train"), ("subway", "subway"), ("ticket", "ticket"),
          ("plane", "plane, airplane"), ("ship", "ship"), ("boat", "boat"), ("fast", "fast"), ("slow", "slow")],
         "太棒了！下次出门的时候，用英语说一说你坐的是什么车吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
