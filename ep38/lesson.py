import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep38", "rooms", "房间", 38, "room")
L.node("room", "room", "/ruːm/", "房间")
L.node("bedroom", "bedroom", "/ˈbedruːm/", "卧室")
L.node("livingroom", "living room", "/ˈlɪvɪŋ ruːm/", "客厅")
L.node("kitchen", "kitchen", "/ˈkɪtʃɪn/", "厨房")
L.node("bathroom", "bathroom", "/ˈbæθruːm/", "浴室")
L.node("washroom", "washroom", "/ˈwɑːʃruːm/", "洗手间")
L.node("restroom", "restroom", "/ˈrestruːm/", "公共厕所")
L.node("toilet", "toilet", "/ˈtɔɪlət/", "马桶；厕所")
L.node("ceiling", "ceiling", "/ˈsiːlɪŋ/", "天花板")
L.node("toothbrush", "toothbrush", "/ˈtuːθbrʌʃ/", "牙刷")
L.node("soap", "soap", "/soʊp/", "肥皂")
L.node("towel", "towel", "/ˈtaʊəl/", "毛巾")
L.grid(["bedroom ceiling kitchen",
        "livingroom room bathroom",
        "washroom restroom toilet",
        "toothbrush soap towel"], dy=350)
L.edge("room", "bedroom"); L.edge("room", "kitchen"); L.edge("room", "livingroom"); L.edge("room", "bathroom"); L.edge("room", "ceiling", "抬头看")
L.edge("room", "restroom"); L.edge("washroom", "restroom", "都可以"); L.edge("restroom", "toilet"); L.edge("bathroom", "toilet")
L.edge("toilet", "towel", dashed=True); L.edge("soap", "towel", dashed=True); L.edge("toothbrush", "soap", dashed=True)

L.seg("title", zh("小朋友们好！欢迎来我家做客！今天，我们来认识家里的房间。"), en("rooms"))
L.seg("map show:room focus:room", zh("房子里分成一间一间的，叫房间："), en("room"))
L.seg("show:bedroom edge:room>bedroom focus:bedroom", zh("睡觉的房间是卧室。床，加上房间："), en("bed"), en("room"), en("bedroom"))
L.seg("show:livingroom edge:room>livingroom focus:livingroom", zh("一家人坐在一起看电视、聊天的地方，是客厅："), en("living room"))
L.seg("show:kitchen edge:room>kitchen focus:kitchen", zh("妈妈做饭的地方，是厨房："), en("kitchen"), zh("还记得第三十五集的厨师吗？"), en("cook"))
L.seg("show:bathroom edge:room>bathroom focus:bathroom", zh("洗澡的地方，是浴室。洗澡，加上房间："), en("bath"), en("room"), en("bathroom"))
L.seg("show:ceiling edge:room>ceiling focus:ceiling", zh("抬头看，房间最上面，是天花板："), en("ceiling"), zh("c e i，读成长长的 see。"))
L.seg("show:toilet edge:bathroom>toilet focus:toilet", zh("上厕所用的马桶："), en("toilet"))
L.seg("show:restroom edge:room>restroom edge:restroom>toilet focus:restroom", zh("在商场、学校里，找厕所要说"), en("restroom"),
      en("Where is the restroom?"))
L.seg("show:washroom edge:washroom>restroom focus:washroom", zh("有的地方也叫它洗手间。洗，加上房间："), en("wash"), en("room"), en("washroom"))
L.seg("focus:bedroom,bathroom,washroom,restroom", zh("你发现了吗？好多房间的名字，都是加上 room 拼出来的："),
      en("bedroom", "focus:bedroom"), en("bathroom", "focus:bathroom"), en("washroom", "focus:washroom"), en("restroom", "focus:restroom"))
L.seg("show:toothbrush focus:toothbrush", zh("早上起床，先刷牙。牙齿，加上刷子："), en("tooth"), en("brush"), en("toothbrush"))
L.seg("show:soap edge:toothbrush>soap focus:soap", zh("再用肥皂洗洗手："), en("soap"))
L.seg("show:towel edge:soap>towel focus:towel", zh("最后，用毛巾擦干："), en("towel"))
L.seg("focus:none", zh("带客人参观一下我家吧！"))
L.seg("", en("This is the living room.", "focus:livingroom"), en("This is my bedroom.", "focus:bedroom"),
      en("The kitchen is over there.", "focus:kitchen"), en("And here is the bathroom.", "focus:bathroom"))
L.review([("room", "room"), ("bedroom", "bedroom"), ("livingroom", "living room"), ("kitchen", "kitchen"), ("bathroom", "bathroom"),
          ("ceiling", "ceiling"), ("toilet", "toilet"), ("restroom", "restroom"), ("washroom", "washroom"), ("toothbrush", "toothbrush"),
          ("soap", "soap"), ("towel", "towel")],
         "太棒了！在家里走一圈，用英语说一说每个房间的名字吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
