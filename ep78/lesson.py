import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep78", "skills", "技能", 78, "skill")
A, V = dict(kind="adj"), dict(kind="verb")
L.node("skill", "skill", "/skɪl/", "技能")
L.node("try", "try", "/traɪ/", "尝试", **V)
L.node("again", "again", "/əˈɡen/", "再一次", kind="adv")
L.node("mistake", "mistake", "/mɪˈsteɪk/", "错误")
L.node("practice", "practice", "/ˈpræktɪs/", "练习", **V)
L.node("often", "often", "/ˈɔːfn/", "经常", kind="adv")
L.node("able", "able", "/ˈeɪbl/", "能够", **A, alt="be able to", altLabel="常说")
L.node("easy", "easy", "/ˈiːzi/", "容易的", **A)
L.node("difficulty", "difficulty", "/ˈdɪfɪkəlti/", "困难")
L.node("difficult", "difficult", "/ˈdɪfɪkəlt/", "困难的", **A)
L.node("proud", "proud", "/praʊd/", "自豪的", **A)
L.node("pride", "pride", "/praɪd/", "骄傲；自豪")
L.grid(["mistake again able",
        "try skill easy",
        "practice difficulty difficult",
        "often pride proud"], dy=350)
L.edge("skill", "try"); L.edge("try", "again", dashed=True); L.edge("try", "mistake", dashed=True); L.edge("skill", "able"); L.edge("skill", "easy", dashed=True)
L.edge("try", "practice"); L.edge("practice", "often", dashed=True); L.edge("skill", "difficulty"); L.edge("difficulty", "difficult", "−y"); L.edge("difficult", "proud", "克服后")
L.edge("proud", "pride")

L.seg("title", zh("小朋友们好！学一项新本领，要怎么做呢？今天，我们来学和技能有关的单词。"), en("skills"))
L.seg("map show:skill focus:skill", zh("会做的本领，是技能："), en("skill"))
L.seg("show:try edge:skill>try focus:try", zh("学新本领，第一步是尝试："), en("try"), en("Let's try!"))
L.seg("show:mistake edge:try>mistake focus:mistake", zh("刚开始，难免会出错："), en("mistake"), zh("出错不要紧，"))
L.seg("show:again edge:try>again focus:again", zh("再试一次！再一次，英语是"), en("again"), en("Try again!"))
L.seg("show:practice edge:try>practice focus:practice", zh("要学会，就要多练习："), en("practice"))
L.seg("show:often edge:practice>often focus:often", zh("经常练习，英语是"), en("often"), zh("小提示：中间的 t 通常不发音。"), en("I practice piano often."))
L.seg("show:able edge:skill>able focus:able", zh("练着练着，就能够做到了："), en("able"), zh("常常说", "alt:able"), en("be able to"))
L.seg("show:easy edge:skill>easy focus:easy", zh("有的事很容易："), en("easy"))
L.seg("show:difficulty edge:skill>difficulty focus:difficulty", zh("有的事有困难："), en("difficulty"))
L.seg("show:difficult edge:difficulty>difficult focus:difficult", zh("去掉最后的 y，就是困难的："), en("difficult"), zh("容易和困难，正好相反："), en("easy", "focus:easy"), en("difficult", "focus:difficult"))
L.seg("show:proud edge:difficult>proud focus:proud", zh("克服了困难，心里很自豪："), en("proud"), en("I'm proud of you!"))
L.seg("show:pride edge:proud>pride focus:pride", zh("自豪这种感觉，叫"), en("pride"))
L.seg("focus:none", zh("跟我一起给自己加油吧！"))
L.seg("", en("Don't be afraid of mistakes.", "focus:mistake"), en("Try again!", "focus:try,again"), en("Practice makes perfect!", "focus:practice"))
L.review([("skill", "skill"), ("try", "try"), ("mistake", "mistake"), ("again", "again"), ("practice", "practice"), ("often", "often"), ("able", "able"),
          ("easy", "easy"), ("difficulty", "difficulty"), ("difficult", "difficult"), ("proud", "proud"), ("pride", "pride")],
         "太棒了！遇到困难不要怕，多练习，你一定能行！点一点图上的单词，还能再听一遍发音哦。")
L.save()
