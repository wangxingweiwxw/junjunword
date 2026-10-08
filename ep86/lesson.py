import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep86", "nature", "大自然", 86, "nature")
L.node("nature", "nature", "/ˈneɪtʃər/", "大自然")
L.node("peaceful", "peaceful", "/ˈpiːsfl/", "宁静的", kind="adj", alt="peace", altLabel="来自")
L.node("discover", "discover", "/dɪˈskʌvər/", "发现", kind="verb", alt="cover", altLabel="dis+")
L.node("wonder", "wonder", "/ˈwʌndər/", "奇迹；想知道")
L.node("countryside", "countryside", "/ˈkʌntrisaɪd/", "乡村")
L.node("river", "river", "/ˈrɪvər/", "河")
L.node("lake", "lake", "/leɪk/", "湖")
L.node("ocean", "ocean", "/ˈoʊʃn/", "海洋")
L.node("coast", "coast", "/koʊst/", "海岸")
L.node("desert", "desert", "/ˈdezərt/", "沙漠")
L.node("mountain", "mountain", "/ˈmaʊntn/", "高山")
L.node("hill", "hill", "/hɪl/", "小山")
L.node("forest", "forest", "/ˈfɔːrɪst/", "森林")
L.grid(["discover nature wonder",
        "peaceful countryside river",
        "lake ocean coast",
        "mountain hill desert",
        ". forest ."], dy=330)
L.edge("nature", "discover"); L.edge("nature", "wonder"); L.edge("nature", "countryside"); L.edge("countryside", "peaceful"); L.edge("countryside", "river")
L.edge("lake", "ocean", "更大"); L.edge("ocean", "coast"); L.edge("mountain", "hill", "更矮"); L.edge("hill", "forest", dashed=True); L.edge("coast", "desert", dashed=True)

L.seg("title", zh("小朋友们好！走出家门，去大自然里看一看吧！"), en("nature"))
L.seg("map show:nature focus:nature", zh("山川河流、花草树木，都是大自然："), en("nature"), en("Nature is full of wonders."))
L.seg("show:discover edge:nature>discover focus:discover", zh("在大自然里，我们能发现很多东西。盖子是 cover，加上 d i s，就是揭开盖子，发现："), en("discover"))
L.seg("show:wonder edge:nature>wonder focus:wonder", zh("大自然里到处都是奇迹，让人好想知道为什么："), en("wonder"), en("I wonder why the sky is blue."))
L.seg("show:countryside edge:nature>countryside focus:countryside", zh("远离城市的乡村。国家，加上旁边："), en("country"), en("side"), en("countryside"))
L.seg("show:peaceful edge:countryside>peaceful focus:peaceful", zh("乡村里安安静静的，很宁静。和平，加上 f u l："), en("peace"), en("peaceful"),
      en("The countryside is very peaceful."))
L.seg("show:river edge:countryside>river focus:river", zh("弯弯的小河："), en("river"))
L.seg("show:lake focus:lake", zh("河水流进了湖里："), en("lake"))
L.seg("show:ocean edge:lake>ocean focus:ocean", zh("比湖大得多得多的，是海洋："), en("ocean"))
L.seg("show:coast edge:ocean>coast focus:coast", zh("海洋和陆地交界的地方，是海岸："), en("coast"))
L.seg("show:desert edge:coast>desert focus:desert", zh("很少下雨、到处是沙子的，是沙漠："), en("desert"), zh("小心，别和甜点 dessert 搞混了，甜点有两个 s。"))
L.seg("show:mountain focus:mountain", zh("高高的大山："), en("mountain"))
L.seg("show:hill edge:mountain>hill focus:hill", zh("矮一点的小山："), en("hill"))
L.seg("show:forest edge:hill>forest focus:forest", zh("长满大树的森林："), en("forest"), zh("还记得第四十六集的树林 woods 吗？森林比树林更大。"))
L.seg("focus:mountain,hill", zh("大山和小山："), en("mountain", "focus:mountain"), en("hill", "focus:hill"))
L.review([("nature", "nature"), ("discover", "discover"), ("wonder", "wonder"), ("countryside", "countryside"), ("peaceful", "peaceful"), ("river", "river"),
          ("lake", "lake"), ("ocean", "ocean"), ("coast", "coast"), ("desert", "desert"), ("mountain", "mountain"), ("hill", "hill"), ("forest", "forest")],
         "太棒了！周末去爬爬山、看看湖，好好享受大自然吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
