import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep62", "subjects", "学科", 62, "subject")
L.node("study", "study", "/ˈstʌdi/", "学习", kind="verb")
L.node("many", "many", "/ˈmeni/", "许多", kind="adj")
L.node("subject", "subject", "/ˈsʌbdʒɪkt/", "科目", plural="subjects", pluralIpa="/ˈsʌbdʒɪkts/")
L.node("math", "math", "/mæθ/", "数学")
L.node("science", "science", "/ˈsaɪəns/", "科学")
L.node("chemistry", "chemistry", "/ˈkemɪstri/", "化学")
L.node("lab", "lab", "/læb/", "实验室")
L.node("experiment", "experiment", "/ɪkˈsperɪmənt/", "实验")
L.node("history", "history", "/ˈhɪstri/", "历史")
L.node("geography", "geography", "/dʒiˈɑːɡrəfi/", "地理")
L.node("art", "art", "/ɑːrt/", "美术；艺术")
L.grid(["study many chemistry",
        "math subject science",
        "history geography lab",
        "art . experiment"], dy=350)
L.edge("study", "subject"); L.edge("many", "subject"); L.edge("subject", "math"); L.edge("subject", "science"); L.edge("subject", "chemistry")
L.edge("subject", "history"); L.edge("subject", "geography"); L.edge("science", "lab"); L.edge("lab", "experiment"); L.edge("history", "art", dashed=True)

L.seg("title", zh("小朋友们好！在学校里，我们要学很多门课。今天，我们来认识各个学科！"), en("subjects"))
L.seg("map show:study focus:study", zh("认真学习，英语是"), en("study"), en("I study hard."))
L.seg("show:many focus:many", zh("要学的课有很多。许多，英语是"), en("many"), zh("还记得第二十八集的 much 吗？能数清的用 many。"))
L.seg("show:subject edge:study>subject edge:many>subject focus:subject", zh("每一门课，叫科目："), en("subject"),
      zh("很多门：", "plural:subject"), en("many subjects"))
L.seg("show:math edge:subject>math focus:math", zh("算加减乘除的数学："), en("math"))
L.seg("show:science edge:subject>science focus:science", zh("探索大自然的科学："), en("science"), zh("还记得第三十五集的科学家 scientist 吗？"))
L.seg("show:chemistry edge:subject>chemistry focus:chemistry", zh("瓶瓶罐罐冒泡泡的化学："), en("chemistry"), zh("开头的 c h，读 k。"), en("I have chemistry on Mondays."))
L.seg("show:lab edge:science>lab focus:lab", zh("做科学实验的房间，是实验室："), en("lab"))
L.seg("show:experiment edge:lab>experiment focus:experiment", zh("在实验室里做实验："), en("experiment"), en("We have a science experiment tomorrow."))
L.seg("show:history edge:subject>history focus:history", zh("讲很久很久以前的故事，是历史。你看，它的后半部分就是故事 story："), en("history"))
L.seg("show:geography edge:subject>geography focus:geography", zh("看着地球仪，学山川河流，是地理："), en("geography"))
L.seg("show:art edge:history>art focus:art", zh("拿起画笔画画，是美术："), en("art"), zh("还记得画家 artist 吗？art 加上 i s t。"))
L.seg("focus:none", zh("你最喜欢哪一科？"))
L.seg("", en("My favorite subject is art.", "focus:art"), en("I like math too.", "focus:math"), en("And science is fun!", "focus:science"))
L.review([("study", "study"), ("many", "many"), ("subject", "subject, subjects"), ("math", "math"), ("science", "science"), ("chemistry", "chemistry"),
          ("lab", "lab"), ("experiment", "experiment"), ("history", "history"), ("geography", "geography"), ("art", "art")],
         "太棒了！用英语说一说你今天上了哪些课吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
