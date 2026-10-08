import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep63", "reading", "阅读", 63, "textbook")
L.node("textbook", "textbook", "/ˈtekstbʊk/", "课本")
L.node("topic", "topic", "/ˈtɑːpɪk/", "话题")
L.node("language", "language", "/ˈlæŋɡwɪdʒ/", "语言")
L.node("translate", "translate", "/trænsˈleɪt/", "翻译", kind="verb")
L.node("pronunciation", "pronunciation", "/prəˌnʌnsiˈeɪʃn/", "发音")
L.node("diction", "diction", "/ˈdɪkʃn/", "用词")
L.node("classic", "classic", "/ˈklæsɪk/", "经典作品")
L.node("fiction", "fiction", "/ˈfɪkʃn/", "小说")
L.node("theme", "theme", "/θiːm/", "主题")
L.node("hero", "hero", "/ˈhɪroʊ/", "英雄；男主角")
L.node("heroine", "heroine", "/ˈheroʊɪn/", "女英雄；女主角")
L.node("courage", "courage", "/ˈkɜːrɪdʒ/", "勇气")
L.grid(["topic textbook language",
        "diction pronunciation translate",
        "classic fiction theme",
        "hero courage heroine"], dy=350)
L.edge("textbook", "topic"); L.edge("textbook", "language"); L.edge("language", "translate"); L.edge("language", "pronunciation"); L.edge("pronunciation", "diction", dashed=True)
L.edge("fiction", "classic"); L.edge("fiction", "theme"); L.edge("fiction", "hero", dashed=True); L.edge("fiction", "heroine", dashed=True)
L.edge("hero", "courage"); L.edge("heroine", "courage")

L.seg("title", zh("小朋友们好！翻开书，我们一起去阅读的世界吧！"), en("reading"))
L.seg("map show:textbook focus:textbook", zh("上课用的书，是课本。文字，加上书："), en("text"), en("book"), en("textbook"))
L.seg("show:topic edge:textbook>topic focus:topic", zh("每一课讲的内容，是话题："), en("topic"), en("Today's topic is animals."))
L.seg("show:language edge:textbook>language focus:language", zh("中文、英语，都是语言："), en("language"))
L.seg("show:translate edge:language>translate focus:translate", zh("把中文变成英文，是翻译："), en("translate"))
L.seg("show:pronunciation edge:language>pronunciation focus:pronunciation", zh("学语言，发音要准："), en("pronunciation"),
      zh("这个词很长，拆开读："), en("pro, nun, ci, a, tion"))
L.seg("show:diction edge:pronunciation>diction focus:diction", zh("说话写文章时选用的词，叫用词："), en("diction"))
L.seg("show:fiction focus:fiction", zh("作家编出来的故事书，是小说："), en("fiction"))
L.seg("show:classic edge:fiction>classic focus:classic", zh("很多年来大家都爱读的好书，是经典："), en("classic"), en("I have read the four classics."))
L.seg("show:theme edge:fiction>theme focus:theme", zh("一本书最想告诉我们的道理，是主题："), en("theme"))
L.seg("show:hero edge:fiction>hero focus:hero", zh("故事里勇敢的男主角，是英雄："), en("hero"))
L.seg("show:heroine edge:fiction>heroine focus:heroine", zh("勇敢的女主角，是女英雄。英雄，加上 i n e："), en("heroine"))
L.seg("show:courage edge:hero>courage edge:heroine>courage focus:courage", zh("他们都有很大的勇气："), en("courage"),
      zh("还记得第五十四集的勇敢 brave 吗？"), en("The hero has a lot of courage."))
L.seg("focus:fiction,diction", zh("小心这两个长得很像的词："), en("fiction", "focus:fiction"), en("diction", "focus:diction"))
L.review([("textbook", "textbook"), ("topic", "topic"), ("language", "language"), ("translate", "translate"), ("pronunciation", "pronunciation"),
          ("diction", "diction"), ("fiction", "fiction"), ("classic", "classic"), ("theme", "theme"), ("hero", "hero"), ("heroine", "heroine"), ("courage", "courage")],
         "太棒了！每天读一点书，你也会成为故事里的英雄。点一点图上的单词，还能再听一遍发音哦。")
L.save()
