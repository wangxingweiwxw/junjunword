import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep27", "classroom", "教室", 27, "classroom")
L.node("classroom", "classroom", "/ˈklæsruːm/", "教室")
L.node("board", "board", "/bɔːrd/", "木板；板")
L.node("blackboard", "blackboard", "/ˈblækbɔːrd/", "黑板")
L.node("chalk", "chalk", "/tʃɔːk/", "粉笔")
L.node("teacher", "teacher", "/ˈtiːtʃər/", "老师", icon="teach", alt="teach + er", altLabel="=")
L.node("lesson", "lesson", "/ˈlesn/", "一节课", plural="lessons", pluralIpa="/ˈlesnz/")
L.node("student", "student", "/ˈstuːdnt/", "学生", plural="students", pluralIpa="/ˈstuːdnts/")
L.node("monitor", "monitor", "/ˈmɑːnɪtər/", "班长")
L.node("desk", "desk", "/desk/", "课桌")
L.node("seat", "seat", "/siːt/", "座位")
L.node("row", "row", "/roʊ/", "一排")
L.node("group", "group", "/ɡruːp/", "小组")
L.grid(["board blackboard chalk",
        "lesson classroom teacher",
        "monitor student group",
        "desk seat row"], dy=340)
L.edge("board", "blackboard", "black +"); L.edge("blackboard", "chalk", "用…写"); L.edge("classroom", "blackboard")
L.edge("classroom", "teacher"); L.edge("classroom", "lesson"); L.edge("classroom", "student")
L.edge("student", "monitor"); L.edge("student", "group"); L.edge("student", "seat"); L.edge("desk", "seat"); L.edge("seat", "row")

L.seg("title", zh("小朋友们好！上课铃响了，我们走进教室吧。"), en("classroom"), zh("教室。"))
L.seg("map show:classroom focus:classroom", zh("还记得第六集的班级吗？班级，加上房间，就是上课的教室："), en("class"), en("room"), en("classroom"))
L.seg("show:board focus:board", zh("一块平平的木板，英语叫"), en("board"))
L.seg("show:blackboard edge:board>blackboard edge:classroom>blackboard focus:blackboard", zh("把木板涂成黑色，挂在教室前面，就是黑板。黑色，加上板："),
      en("black"), en("board"), en("blackboard"))
L.seg("show:chalk edge:blackboard>chalk focus:chalk", zh("在黑板上写字，要用粉笔："), en("chalk"), zh("小提示：中间的 l 不发音。"))
L.seg("show:teacher edge:classroom>teacher focus:teacher", zh("站在黑板前给我们上课的，是老师。还记得第六集的教吗？加上 e r：", "alt:teacher"),
      en("teach"), en("teacher"), en("Good morning, teacher!"))
L.seg("show:lesson edge:classroom>lesson focus:lesson", zh("老师上的一节课，叫"), en("lesson"), en("Lesson One"))
L.seg("show:student edge:classroom>student focus:student", zh("坐在下面认真听课的，是学生："), en("student"),
      zh("很多学生：", "plural:student"), en("students"))
L.seg("show:monitor edge:student>monitor focus:monitor", zh("帮老师管理班级的学生，是班长："), en("monitor"), en("He is our monitor."))
L.seg("show:desk focus:desk", zh("每个学生都有一张课桌："), en("desk"))
L.seg("show:seat edge:student>seat edge:desk>seat focus:seat", zh("还有一个自己的座位："), en("seat"), en("Please take your seat."))
L.seg("show:row edge:seat>row focus:row", zh("座位一个挨着一个，排成一排："), en("row"), en("I sit in the first row."))
L.seg("show:group edge:student>group focus:group", zh("上课讨论的时候，几个同学围在一起，组成一个小组："), en("group"), en("Let's work in groups."))
L.seg("focus:board,blackboard,classroom", zh("今天的拼词："), en("black, board, blackboard", "focus:blackboard"), en("class, room, classroom", "focus:classroom"))
L.seg("focus:none", zh("上课啦！跟着老师的口令做一做："))
L.seg("", en("Stand up!", "focus:student"), en("Good morning, teacher!", "focus:teacher"), en("Sit down, please.", "focus:seat"),
      en("Look at the blackboard.", "focus:blackboard"), en("Work in groups.", "focus:group"))
L.review([("classroom", "classroom"), ("board", "board"), ("blackboard", "blackboard"), ("chalk", "chalk"), ("teacher", "teacher"),
          ("lesson", "lesson"), ("student", "student, students"), ("monitor", "monitor"), ("desk", "desk"), ("seat", "seat"),
          ("row", "row"), ("group", "group")],
         "太棒了！明天到了教室，用英语说一说你看到的东西吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
