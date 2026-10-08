import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep77", "character", "品格", 77, "honest")
A = dict(kind="adj")
L.node("people", "people", "/ˈpiːpl/", "人们", icon="group")
L.node("serious", "serious", "/ˈsɪriəs/", "严肃的；认真的", **A)
L.node("seriously", "seriously", "/ˈsɪriəsli/", "认真地", kind="adv")
L.node("seem", "seem", "/siːm/", "似乎；看起来", kind="verb")
L.node("wonderful", "wonderful", "/ˈwʌndərfl/", "极好的", **A)
L.node("polite", "polite", "/pəˈlaɪt/", "有礼貌的", **A)
L.node("rude", "rude", "/ruːd/", "粗鲁的", **A)
L.node("honest", "honest", "/ˈɑːnɪst/", "诚实的", **A)
L.node("truthful", "truthful", "/ˈtruːθfl/", "说真话的", **A, alt="truth", altLabel="来自")
L.node("faithful", "faithful", "/ˈfeɪθfl/", "忠诚的", **A, alt="faith", altLabel="来自")
L.node("job", "job", "/dʒɑːb/", "工作")
L.node("poor", "poor", "/pʊr/", "贫穷的", **A)
L.node("successful", "successful", "/səkˈsesfl/", "成功的", **A, alt="success", altLabel="来自")
L.grid(["wonderful people seem",
        "seriously serious .",
        "polite rude honest",
        "truthful faithful job",
        ". poor successful"], dy=330)
L.edge("people", "wonderful", dashed=True); L.edge("people", "seem", dashed=True); L.edge("people", "serious"); L.edge("serious", "seriously", "+ly")
L.edge("polite", "rude", "反义"); L.edge("rude", "honest", dashed=True); L.edge("honest", "faithful", dashed=True); L.edge("faithful", "truthful", dashed=True)
L.edge("job", "poor", dashed=True); L.edge("job", "successful")

L.seg("title", zh("小朋友们好！一个人好不好，要看他的品格。今天，我们来学描述人的形容词。"), en("character"))
L.seg("map show:people focus:people", zh("还记得第一集的人们吗？"), en("people"))
L.seg("show:wonderful edge:people>wonderful focus:wonderful", zh("让人拍手叫好的，是极好的："), en("wonderful"), en("You are wonderful!"))
L.seg("show:seem edge:people>seem focus:seem", zh("看上去、似乎，英语是"), en("seem"), en("He seems happy."))
L.seg("show:serious edge:people>serious focus:serious", zh("板着脸、不开玩笑，是严肃的、认真的："), en("serious"))
L.seg("show:seriously edge:serious>seriously focus:seriously", zh("加上 l y，就是认真地："), en("seriously"), en("Take it seriously."))
L.seg("show:polite focus:polite", zh("见人就打招呼，说请和谢谢，是有礼貌的："), en("polite"))
L.seg("show:rude edge:polite>rude focus:rude", zh("用手指着别人，大声嚷嚷，是粗鲁的："), en("rude"), zh("我们要做有礼貌的孩子，不要粗鲁哦。"))
L.seg("show:honest focus:honest", zh("不说谎的，是诚实的："), en("honest"), zh("开头的 h 不发音，所以要说"), en("an honest boy"))
L.seg("show:faithful edge:honest>faithful focus:faithful", zh("永远站在朋友身边的，是忠诚的。信任，加上 f u l："), en("faith"), en("faithful"))
L.seg("show:truthful edge:faithful>truthful focus:truthful", zh("总说真话的。真相，加上 f u l："), en("truth"), en("truthful"))
L.seg("show:job focus:job", zh("工作："), en("job"))
L.seg("show:poor edge:job>poor focus:poor", zh("没有钱，是贫穷的："), en("poor"))
L.seg("show:successful edge:job>successful focus:successful", zh("努力工作，就会成功："), en("success"), en("successful"))
L.seg("focus:wonderful,faithful,truthful,successful", zh("你发现了吗？好多形容词都是 f u l 结尾的，意思是充满了："),
      en("wonderful", "focus:wonderful"), en("faithful", "focus:faithful"), en("truthful", "focus:truthful"), en("successful", "focus:successful"))
L.review([("people", "people"), ("wonderful", "wonderful"), ("seem", "seem"), ("serious", "serious"), ("seriously", "seriously"), ("polite", "polite"),
          ("rude", "rude"), ("honest", "honest"), ("faithful", "faithful"), ("truthful", "truthful"), ("job", "job"), ("poor", "poor"), ("successful", "successful")],
         "太棒了！做一个诚实、有礼貌的好孩子吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
