import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep19", "weather", "天气", 19, "weather")
A = dict(kind="adj")
L.node("weather", "weather", "/ˈweðər/", "天气")
L.node("air", "air", "/er/", "空气")
L.node("sunny", "sunny", "/ˈsʌni/", "晴朗的", alt="sun", altLabel="来自", **A)
L.node("sunshine", "sunshine", "/ˈsʌnʃaɪn/", "阳光")
L.node("cloudy", "cloudy", "/ˈklaʊdi/", "多云的", alt="cloud", altLabel="来自", **A)
L.node("windy", "windy", "/ˈwɪndi/", "刮风的", alt="wind", altLabel="来自", **A)
L.node("rainy", "rainy", "/ˈreɪni/", "下雨的", alt="rain", altLabel="来自", **A)
L.node("shower", "shower", "/ˈʃaʊər/", "阵雨")
L.node("storm", "storm", "/stɔːrm/", "暴风雨", alt="stormy", altLabel="加 y →")
L.node("snowy", "snowy", "/ˈsnoʊi/", "下雪的", alt="snow", altLabel="来自", **A)
L.node("foggy", "foggy", "/ˈfɑːɡi/", "有雾的", alt="fog", altLabel="来自", **A)
L.node("hot", "hot", "/hɑːt/", "热的", **A)
L.node("cold", "cold", "/koʊld/", "冷的", **A)
L.grid(["sunshine air foggy",
        "sunny weather cloudy",
        "hot . windy",
        "cold rainy storm",
        "snowy shower ."], dy=350)
L.edge("weather", "air"); L.edge("weather", "sunny"); L.edge("sunny", "sunshine"); L.edge("weather", "cloudy")
L.edge("air", "foggy", dashed=True); L.edge("cloudy", "windy"); L.edge("weather", "rainy"); L.edge("rainy", "shower", "一阵")
L.edge("rainy", "storm"); L.edge("sunny", "hot"); L.edge("hot", "cold", "反义"); L.edge("cold", "snowy")

L.seg("title", zh("小朋友们好！出门前，先看看窗外。今天的天气怎么样呢？"), en("weather"), zh("天气。"))
L.seg("map show:weather focus:weather", zh("晴天、雨天、下雪天，都是天气："), en("weather"),
      zh("中间的 e a，在这里读得很短。"), en("How's the weather today?"))
L.seg("show:air edge:weather>air focus:air", zh("我们每时每刻都在呼吸的，是空气："), en("air"), en("fresh air"))
L.seg("focus:none", zh("今天要学一个小魔法：很多天气的词，就是在名词后面加上一个字母 y。"))
L.seg("show:sunny edge:weather>sunny focus:sunny alt:sunny", zh("太阳是"), en("sun"),
      zh("加上 y 的时候，要再多写一个 n。晴朗的："), en("sunny"), en("It's sunny today."))
L.seg("show:sunshine edge:sunny>sunshine focus:sunshine", zh("太阳照下来的光，暖暖的，是阳光。太阳，加上照耀："), en("sun"), en("shine"), en("sunshine"))
L.seg("show:cloudy edge:weather>cloudy focus:cloudy alt:cloudy", zh("云是"), en("cloud"), zh("满天都是云，就是多云的："), en("cloudy"))
L.seg("show:windy edge:cloudy>windy focus:windy alt:windy", zh("风是"), en("wind"), zh("树叶被吹得哗哗响，就是刮风的："), en("windy"))
L.seg("show:rainy edge:weather>rainy focus:rainy alt:rainy", zh("雨是"), en("rain"), zh("下雨的："), en("rainy"),
      en("It's rainy. Take an umbrella."))
L.seg("show:shower edge:rainy>shower focus:shower", zh("雨下一会儿就停了，这种一阵一阵的雨，叫阵雨："), en("shower"),
      zh("洗澡用的淋浴，也是这个词哦。"))
L.seg("show:storm edge:rainy>storm focus:storm", zh("雨越下越大，还打雷闪电，那是暴风雨："), en("storm"),
      zh("同样，加上 y，就是有暴风雨的：", "alt:storm"), en("stormy"))
L.seg("show:foggy edge:air>foggy focus:foggy alt:foggy", zh("雾是"), en("fog"),
      zh("加上 y 的时候，要再多写一个 g。有雾的："), en("foggy"), zh("雾天里，什么都看不清。"))
L.seg("show:hot edge:sunny>hot focus:hot", zh("夏天，太阳火辣辣的，好热："), en("hot"), en("It's so hot!"))
L.seg("show:cold edge:hot>cold focus:cold", zh("热的反面，是冷："), en("cold"), en("It's cold. Put on your coat."))
L.seg("show:snowy edge:cold>snowy focus:snowy alt:snowy", zh("冷到一定程度，就会下雪。雪是"), en("snow"), zh("下雪的："), en("snowy"))
L.seg("focus:sunny,cloudy,windy,rainy,snowy,foggy", zh("我们把名词和它的 y 形式，一对一对地读一遍："),
      en("sun, sunny", "focus:sunny"), en("cloud, cloudy", "focus:cloudy"), en("wind, windy", "focus:windy"),
      en("rain, rainy", "focus:rainy"), en("snow, snowy", "focus:snowy"), en("fog, foggy", "focus:foggy"))
L.seg("focus:none", zh("我们来当小小天气预报员吧！"))
L.seg("", en("Good morning! Here's the weather.", "focus:weather"), en("Monday is sunny.", "focus:sunny"),
      en("Tuesday is rainy.", "focus:rainy"), en("Wednesday is windy and cold.", "focus:windy,cold"))
L.review([("weather", "weather"), ("air", "air"), ("sunny", "sunny"), ("sunshine", "sunshine"), ("cloudy", "cloudy"),
          ("windy", "windy"), ("rainy", "rainy"), ("shower", "shower"), ("storm", "storm, stormy"), ("foggy", "foggy"),
          ("hot", "hot"), ("cold", "cold"), ("snowy", "snowy")],
         "太棒了！明天早上，看看窗外，用英语说一说天气吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
