import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep97", "Europe", "欧洲", 97, "europe")
for id, w, ipa, z in [("europe", "Europe", "/ˈjʊrəp/", "欧洲"), ("european", "European", "/ˌjʊrəˈpiːən/", "欧洲人；欧洲的"),
                      ("britain", "Britain", "/ˈbrɪtn/", "英国"), ("british", "British", "/ˈbrɪtɪʃ/", "英国人；英国的"),
                      ("england", "England", "/ˈɪŋɡlənd/", "英格兰"), ("english", "English", "/ˈɪŋɡlɪʃ/", "英语；英格兰的"), ("englishman", "Englishman", "/ˈɪŋɡlɪʃmən/", "英格兰人"),
                      ("france", "France", "/fræns/", "法国"), ("french", "French", "/frentʃ/", "法语；法国人"),
                      ("germany", "Germany", "/ˈdʒɜːrməni/", "德国"), ("german", "German", "/ˈdʒɜːrmən/", "德国人；德语"),
                      ("russia", "Russia", "/ˈrʌʃə/", "俄罗斯"), ("russian", "Russian", "/ˈrʌʃn/", "俄罗斯人；俄语"),
                      ("italy", "Italy", "/ˈɪtəli/", "意大利"), ("italian", "Italian", "/ɪˈtæliən/", "意大利人；意语")]:
    L.node(id, w, ipa, z)
L.grid(["british europe european",
        "britain france french",
        "england germany german",
        "english russia russian",
        "englishman italy italian"], dy=330)
for id, x, y in [("european", 170, 150), ("europe", 520, 150), ("british", 870, 150), ("britain", 1220, 150), ("england", 1570, 150),
                 ("france", 170, 470), ("germany", 520, 470), ("russia", 870, 470), ("italy", 1220, 470), ("english", 1570, 470),
                 ("french", 170, 790), ("german", 520, 790), ("russian", 870, 790), ("italian", 1220, 790), ("englishman", 1570, 790)]:
    L.byid[id]["at"] = [x, y]
L.edge("europe", "european", "+an"); L.edge("britain", "british"); L.edge("england", "britain", "属于"); L.edge("england", "english")
L.edge("english", "englishman", "+man"); L.edge("france", "french"); L.edge("germany", "german", "−y"); L.edge("russia", "russian", "+n"); L.edge("italy", "italian", "y→ian")
L.edge("europe", "germany", dashed=True); L.edge("europe", "france", dashed=True)

L.seg("title", zh("小朋友们好！第二站，我们去欧洲看一看！"), en("Europe"))
L.seg("map show:europe focus:europe", zh("欧洲，英语是"), en("Europe"))
L.seg("show:european edge:europe>european focus:european", zh("欧洲人，加上 a n："), en("European"))
L.seg("show:britain focus:britain", zh("英国，英语是"), en("Britain"))
L.seg("show:british edge:britain>british focus:british", zh("英国人、英国的："), en("British"))
L.seg("show:england edge:england>britain focus:england", zh("英国的一部分，叫英格兰："), en("England"))
L.seg("show:english edge:england>english focus:english", zh("英格兰说的话，就是我们学的英语："), en("English"))
L.seg("show:englishman edge:english>englishman focus:englishman", zh("英格兰人，加上 m a n："), en("Englishman"))
L.seg("show:france edge:europe>france focus:france", zh("法国："), en("France"))
L.seg("show:french edge:france>french focus:french", zh("法语和法国人，长得很不一样："), en("French"), en("French fries"))
L.seg("show:germany edge:europe>germany focus:germany", zh("德国："), en("Germany"))
L.seg("show:german edge:germany>german focus:german", zh("德国人，去掉最后的 y："), en("German"))
L.seg("show:russia focus:russia", zh("俄罗斯："), en("Russia"))
L.seg("show:russian edge:russia>russian focus:russian", zh("俄罗斯人，加上 n："), en("Russian"))
L.seg("show:italy focus:italy", zh("意大利，那里有好吃的披萨："), en("Italy"))
L.seg("show:italian edge:italy>italian focus:italian", zh("意大利人，把 y 换成 i a n："), en("Italian"), zh("还记得第二十一集的意大利面 spaghetti 吗？"))
L.seg("focus:none", zh("国家和那里的人："))
L.seg("", en("France, French", "focus:france,french"), en("Germany, German", "focus:germany,german"), en("Russia, Russian", "focus:russia,russian"), en("Italy, Italian", "focus:italy,italian"))
L.review([("europe", "Europe"), ("european", "European"), ("britain", "Britain"), ("british", "British"), ("england", "England"), ("english", "English"),
          ("englishman", "Englishman"), ("france", "France"), ("french", "French"), ("germany", "Germany"), ("german", "German"), ("russia", "Russia"),
          ("russian", "Russian"), ("italy", "Italy"), ("italian", "Italian")],
         "太棒了！在地图上找一找欧洲的这些国家吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
