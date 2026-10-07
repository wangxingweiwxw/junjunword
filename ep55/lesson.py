import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep55", "exams", "考试", 55, "exam")
V = dict(kind="verb")
L.node("exam", "exam", "/ɪɡˈzæm/", "考试", alt="examination", altLabel="全称")
L.node("test", "test", "/test/", "测验")
L.node("preparation", "preparation", "/ˌprepəˈreɪʃn/", "准备", alt="prepare", altLabel="来自")
L.node("start", "start", "/stɑːrt/", "开始", **V)
L.node("finish", "finish", "/ˈfɪnɪʃ/", "完成", **V)
L.node("know", "know", "/noʊ/", "知道", **V)
L.node("question", "question", "/ˈkwestʃən/", "问题")
L.node("answer", "answer", "/ˈænsər/", "答案；回答")
L.node("guess", "guess", "/ɡes/", "猜", **V)
L.node("right", "right", "/raɪt/", "对的", kind="adj", icon="rightok")
L.node("wrong", "wrong", "/rɔːŋ/", "错的", kind="adj")
L.node("correct", "correct", "/kəˈrekt/", "改正；正确的", **V)
L.node("level", "level", "/ˈlevl/", "水平；级别")
L.node("grade", "grade", "/ɡreɪd/", "成绩；分数", icon="gradeA")
L.grid(["preparation exam test",
        "start know finish",
        "question guess answer",
        "right wrong correct",
        "grade level ."], dy=330)
L.edge("preparation", "exam"); L.edge("exam", "test"); L.edge("exam", "know", dashed=True)
L.edge("question", "answer"); L.edge("question", "guess", dashed=True); L.edge("guess", "right"); L.edge("guess", "wrong"); L.edge("wrong", "correct", "要")
L.edge("grade", "level", dashed=True)

L.seg("title", zh("小朋友们好！考试要来啦，别紧张！今天，我们来学和考试有关的单词。"), en("exam"))
L.seg("map show:exam focus:exam", zh("考试，英语是"), en("exam"), zh("它的全称是", "alt:exam"), en("examination"))
L.seg("show:test edge:exam>test focus:test", zh("小一点的考试，是测验："), en("test"), en("a spelling test"))
L.seg("show:preparation edge:preparation>exam focus:preparation", zh("考试前，要做好准备："), en("preparation"),
      zh("它来自", "alt:preparation"), en("prepare"))
L.seg("show:know edge:exam>know focus:know", zh("复习好了，答案心里都知道："), en("know"), zh("开头的 k 不发音哦。"), en("I know the answer!"))
L.seg("show:start focus:start", zh("考试开始了："), en("start"))
L.seg("show:finish edge:start>finish focus:finish", zh("写完了，就是完成："), en("finish"), en("I finished the test."))
L.seg("show:question focus:question", zh("试卷上的每一道题，是问题："), en("question"))
L.seg("show:answer edge:question>answer focus:answer", zh("写出答案："), en("answer"))
L.seg("show:guess edge:question>guess focus:guess", zh("实在不会，只好猜一猜："), en("guess"), zh("中间的 u 不发音。"))
L.seg("show:right edge:guess>right focus:right", zh("答对了，是"), en("right"), zh("还记得第五十三集的右边吗？同一个词，两个意思！"))
L.seg("show:wrong edge:guess>wrong focus:wrong", zh("答错了，是"), en("wrong"), zh("开头的 w 不发音。"))
L.seg("show:correct edge:wrong>correct focus:correct", zh("错了不要紧，把它改正过来："), en("correct"), zh("它也是正确的意思。"))
L.seg("show:grade focus:grade", zh("考完试，老师给出成绩："), en("grade"), zh("还记得第六集的年级吗？也是这个词。"), en("I got a good grade!"))
L.seg("show:level edge:grade>level focus:level", zh("成绩越来越好，水平就越来越高："), en("level"))
L.seg("focus:right,wrong", zh("对和错："), en("right", "focus:right"), en("wrong", "focus:wrong"))
L.review([("exam", "exam"), ("test", "test"), ("preparation", "preparation"), ("know", "know"), ("start", "start"), ("finish", "finish"),
          ("question", "question"), ("answer", "answer"), ("guess", "guess"), ("right", "right"), ("wrong", "wrong"), ("correct", "correct"),
          ("grade", "grade"), ("level", "level")],
         "太棒了！考试前好好准备，考试时认真作答，你一定能行！点一点图上的单词，还能再听一遍发音哦。")
L.save()
