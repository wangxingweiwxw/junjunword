import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep96", "Asia", "亚洲", 96, "asia")
L.node("continent", "continent", "/ˈkɑːntɪnənt/", "大洲；大陆")
L.node("asia", "Asia", "/ˈeɪʒə/", "亚洲")
L.node("asian", "Asian", "/ˈeɪʒn/", "亚洲人；亚洲的")
L.node("population", "population", "/ˌpɑːpjuˈleɪʃn/", "人口")
for id, w, ipa, z in [("china", "China", "/ˈtʃaɪnə/", "中国"), ("chinese", "Chinese", "/ˌtʃaɪˈniːz/", "中国人；中文"), ("india", "India", "/ˈɪndiə/", "印度"),
                      ("indian", "Indian", "/ˈɪndiən/", "印度人"), ("japan", "Japan", "/dʒəˈpæn/", "日本"), ("japanese", "Japanese", "/ˌdʒæpəˈniːz/", "日本人；日语"),
                      ("southkorea", "South Korea", "/saʊθ kəˈriːə/", "韩国"), ("korean", "Korean", "/kəˈriːən/", "韩国人；韩语")]:
    L.node(id, w, ipa, z)
L.node("infer", "infer", "/ɪnˈfɜːr/", "推断", kind="verb")
L.grid(["continent asia asian",
        "china . chinese",
        "japan . japanese",
        "southkorea . korean",
        "india population indian",
        ". infer ."], dy=310)
for id, x, y in [("continent", 170, 150), ("asia", 520, 150), ("asian", 870, 150), ("population", 1220, 150), ("infer", 1570, 150),
                 ("china", 170, 470), ("chinese", 170, 790), ("japan", 520, 470), ("japanese", 520, 790), ("southkorea", 870, 470), ("korean", 870, 790),
                 ("india", 1220, 470), ("indian", 1220, 790)]:
    L.byid[id]["at"] = [x, y]
L.edge("continent", "asia"); L.edge("asia", "asian", "+n"); L.edge("asian", "population", dashed=True); L.edge("population", "infer", dashed=True)
L.edge("china", "chinese", "+ese"); L.edge("japan", "japanese", "+ese"); L.edge("southkorea", "korean", "+n"); L.edge("india", "indian", "+n")
for c in ["china", "japan", "southkorea", "india"]:
    L.edge("asia", c, dashed=True)

L.seg("title", zh("小朋友们好！我们一起去认识世界吧！第一站，就是我们所在的亚洲。"), en("Asia"))
L.seg("map show:continent focus:continent", zh("地球上的大块陆地，叫大洲："), en("continent"), zh("地球上一共有七大洲。"))
L.seg("show:asia edge:continent>asia focus:asia", zh("最大的一个大洲，是亚洲："), en("Asia"), zh("国家和大洲的名字，开头都要大写。"))
L.seg("show:asian edge:asia>asian focus:asian", zh("亚洲人，在后面加上 n："), en("Asian"))
L.seg("show:china edge:asia>china focus:china", zh("我们的祖国，中国："), en("China"))
L.seg("show:chinese edge:china>chinese focus:chinese", zh("中国人和中文，加上 e s e："), en("Chinese"), en("I am Chinese. I speak Chinese."))
L.seg("show:japan edge:asia>japan focus:japan", zh("日本："), en("Japan"))
L.seg("show:japanese edge:japan>japanese focus:japanese", zh("日本人和日语，也加 e s e："), en("Japanese"))
L.seg("show:southkorea edge:asia>southkorea focus:southkorea", zh("韩国："), en("South Korea"))
L.seg("show:korean edge:southkorea>korean focus:korean", zh("韩国人和韩语，加上 n："), en("Korean"), en("I love Korean food."))
L.seg("show:india edge:asia>india focus:india", zh("印度："), en("India"))
L.seg("show:indian edge:india>indian focus:indian", zh("印度人，加上 n："), en("Indian"))
L.seg("show:population edge:asian>population focus:population", zh("亚洲的人口特别多。人口，英语是"), en("population"),
      zh("中国和印度，都是人口很多的国家。"))
L.seg("show:infer edge:population>infer focus:infer", zh("根据线索得出结论，是推断："), en("infer"))
L.seg("focus:chinese,japanese", zh("两个 e s e 结尾的："), en("China, Chinese", "focus:china,chinese"), en("Japan, Japanese", "focus:japan,japanese"))
L.seg("focus:asian,korean,indian", zh("三个加 n 的："), en("Asia, Asian", "focus:asia,asian"), en("Korea, Korean", "focus:southkorea,korean"), en("India, Indian", "focus:india,indian"))
L.review([("continent", "continent"), ("asia", "Asia"), ("asian", "Asian"), ("china", "China"), ("chinese", "Chinese"), ("japan", "Japan"), ("japanese", "Japanese"),
          ("southkorea", "South Korea"), ("korean", "Korean"), ("india", "India"), ("indian", "Indian"), ("population", "population"), ("infer", "infer")],
         "太棒了！在地图上找一找亚洲的这些国家吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
