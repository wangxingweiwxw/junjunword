import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep06", "school", "学校", 6, "school")
L.node("school", "school", "/skuːl/", "学校")
L.node("class", "class", "/klæs/", "班级；课")
L.node("teach", "teach", "/tiːtʃ/", "教", kind="verb", alt="teacher", altLabel="加 er →")
L.node("work", "work", "/wɜːrk/", "工作；学习", kind="verb")
L.node("schoolwork", "schoolwork", "/ˈskuːlwɜːrk/", "功课")
L.node("homework", "homework", "/ˈhoʊmwɜːrk/", "家庭作业")
L.node("complete", "complete", "/kəmˈpliːt/", "完成", kind="verb")
L.node("classmate", "classmate", "/ˈklæsmeɪt/", "同学", plural="classmates", pluralIpa="/ˈklæsmeɪts/")
L.node("uniform", "uniform", "/ˈjuːnɪfɔːrm/", "校服；制服")
L.node("grade", "grade", "/ɡreɪd/", "年级")
L.node("term", "term", "/tɜːrm/", "学期")
L.grid(["teach school work",
        "class schoolwork homework",
        "grade classmate complete",
        "term uniform ."], dy=330)
L.edge("school", "class"); L.edge("teach", "class")
L.edge("school", "schoolwork", "+"); L.edge("work", "schoolwork", "+"); L.edge("work", "homework")
L.edge("homework", "complete", "做完"); L.edge("class", "classmate"); L.edge("classmate", "uniform", "穿")
L.edge("class", "grade"); L.edge("grade", "term", "分成")

L.seg("title", zh("小朋友们好！今天，我们一起走进学校。"), en("school"), zh("学校。"))
L.seg("map show:school focus:school", zh("每天背着书包去上学的地方，就是学校："), en("school"), en("I go to school."))
L.seg("show:class edge:school>class focus:class", zh("学校里，同学们分成一个一个班，坐在一起上课。班级和课，英语都可以说"),
      en("class"), en("We have an English class."))
L.seg("show:teach edge:teach>class focus:teach", zh("站在讲台前给我们讲课，就是教："), en("teach"),
      zh("在后面加上 e r，就变成了教书的人，老师：", "alt:teach"), en("teacher"))
L.seg("show:work focus:work", zh("爸爸妈妈每天上班工作。工作，英语是"), en("work"), en("Mom goes to work."))
L.seg("show:schoolwork edge:school>schoolwork edge:work>schoolwork focus:schoolwork",
      zh("把学校和工作拼在一起，就是我们在学校里要做的功课："),
      en("school", "focus:school"), en("work", "focus:work"), en("schoolwork", "focus:schoolwork"))
L.seg("show:homework edge:work>homework focus:homework",
      zh("还记得上一集的家吗？家加上工作，就是要带回家做的家庭作业："), en("home"), en("work"), en("homework"),
      en("I do my homework."))
L.seg("show:complete edge:homework>complete focus:complete", zh("作业写完了，每一题都打上勾，就是完成："), en("complete"),
      en("I complete my homework."))
L.seg("show:classmate edge:class>classmate focus:classmate", zh("和你在同一个班的小伙伴，是同学。班级，加上表示伙伴的小词"),
      en("mate"), zh("就是"), en("classmate"), en("She is my classmate."))
L.seg("show:uniform edge:classmate>uniform focus:uniform", zh("同学们穿着一模一样的衣服，那是校服："), en("uniform"),
      zh("开头的 u n i，是一个的意思。大家穿成一个样子，就是校服。"), en("I wear my school uniform."))
L.seg("show:grade edge:class>grade focus:grade", zh("每过一年，我们就升上一个年级："), en("grade"), en("I'm in Grade Three."))
L.seg("show:term edge:grade>term focus:term", zh("一个学年，又分成上下两个学期："), en("term"), en("A new term begins!"))
L.seg("focus:none", zh("你发现了吗？今天有好几个单词，都是两个小词拼起来的。"))
L.seg("", en("school, work, schoolwork", "focus:schoolwork"), en("home, work, homework", "focus:homework"),
      en("class, mate, classmate", "focus:classmate"))
L.seg("focus:classmate", zh("很多个同学，后面加上字母 s："), en("classmate"), en("classmates", "plural:classmate"))
L.review([("school", "school"), ("class", "class"), ("teach", "teach, teacher"), ("work", "work"),
          ("schoolwork", "schoolwork"), ("homework", "homework"), ("complete", "complete"),
          ("classmate", "classmate, classmates"), ("uniform", "uniform"), ("grade", "grade"), ("term", "term")],
         "太棒了！明天上学的时候，用英语跟你的同学打个招呼吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
