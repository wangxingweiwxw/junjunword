import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep13", "schoolbag", "书包", 13, "schoolbag")
L.node("schoolbag", "schoolbag", "/ˈskuːlbæɡ/", "书包", alt="bookbag")
L.node("book", "book", "/bʊk/", "书", plural="books", pluralIpa="/bʊks/")
L.node("dictionary", "dictionary", "/ˈdɪkʃəneri/", "词典")
L.node("notebook", "notebook", "/ˈnoʊtbʊk/", "笔记本")
L.node("paper", "paper", "/ˈpeɪpər/", "纸")
L.node("pen", "pen", "/pen/", "钢笔；笔", plural="pens", pluralIpa="/penz/")
L.node("pencil", "pencil", "/ˈpensl/", "铅笔")
L.node("eraser", "eraser", "/ɪˈreɪsər/", "橡皮")
L.node("ruler", "ruler", "/ˈruːlər/", "尺子")
L.node("crayon", "crayon", "/ˈkreɪɑːn/", "蜡笔")
L.grid(["ruler schoolbag crayon",
        "dictionary book notebook",
        "paper pencil pen",
        ". eraser ."], dy=350)
L.edge("schoolbag", "ruler"); L.edge("schoolbag", "crayon"); L.edge("schoolbag", "book")
L.edge("book", "dictionary", "很厚的"); L.edge("book", "notebook", "note +"); L.edge("book", "paper", "用纸做")
L.edge("pen", "notebook", "写"); L.edge("pencil", "notebook"); L.edge("eraser", "pencil", "擦掉")

L.seg("title", zh("小朋友们好！明天要上学啦，我们先来收拾一下书包。"), en("schoolbag"), zh("书包。"))
L.seg("map show:schoolbag focus:schoolbag", zh("背着去上学的包，叫书包。学校，加上包："), en("school"), en("bag"), en("schoolbag"),
      zh("它还有一个名字，书加上包：", "alt:schoolbag"), en("bookbag"))
L.seg("show:book edge:schoolbag>book focus:book", zh("书包里，最重要的就是书："), en("book"), zh("很多本书：", "plural:book"), en("books"))
L.seg("show:dictionary edge:book>dictionary focus:dictionary", zh("遇到不认识的字，就查一查又厚又大的词典："), en("dictionary"),
      en("Look it up in the dictionary."))
L.seg("show:notebook edge:book>notebook focus:notebook", zh("用来记笔记的本子，是笔记，加上书："), en("note"), en("book"), en("notebook"))
L.seg("show:paper edge:book>paper focus:paper", zh("书和本子，都是用纸做的："), en("paper"),
      zh("纸通常不加 s。一张纸，要这样说："), en("a piece of paper"))
L.seg("show:pen edge:pen>notebook focus:pen", zh("在本子上写字，要用笔："), en("pen"), zh("很多支笔：", "plural:pen"), en("pens"))
L.seg("show:pencil edge:pencil>notebook focus:pencil", zh("画画、写作业，常常用铅笔："), en("pencil"),
      zh("比一比，铅笔就是在钢笔后面，多了几个字母。"), en("pen", "focus:pen"), en("pencil", "focus:pencil"))
L.seg("show:eraser edge:eraser>pencil focus:eraser", zh("铅笔字写错了，用橡皮擦一擦："), en("eraser"),
      zh("擦掉这个动作，加上字母 r，就变成了擦东西的工具："), en("erase"), en("eraser"))
L.seg("show:ruler edge:schoolbag>ruler focus:ruler", zh("要画一条直直的线，就用尺子："), en("ruler"), en("a long ruler"))
L.seg("show:crayon edge:schoolbag>crayon focus:crayon", zh("画画用的五颜六色的笔，是蜡笔："), en("crayon"), en("I draw with crayons."))
L.seg("focus:none", zh("我们一起把书包装好吧！"))
L.seg("", en("a book", "focus:book"), en("a notebook", "focus:notebook"), en("a dictionary", "focus:dictionary"),
      en("a pen", "focus:pen"), en("a pencil", "focus:pencil"), en("an eraser", "focus:eraser"), en("a ruler", "focus:ruler"),
      en("and crayons!", "focus:crayon"), en("My schoolbag is ready!", "focus:schoolbag"))
L.review([("schoolbag", "schoolbag, bookbag"), ("book", "book, books"), ("dictionary", "dictionary"), ("notebook", "notebook"),
          ("paper", "paper"), ("pen", "pen, pens"), ("pencil", "pencil"), ("eraser", "eraser"), ("ruler", "ruler"), ("crayon", "crayon")],
         "太棒了！今天晚上收拾书包的时候，一边装一边用英语说出来吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
