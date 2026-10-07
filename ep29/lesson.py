import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep29", "clubs", "社团", 29, "club")
L.node("club", "club", "/klʌb/", "俱乐部；社团")
L.node("join", "join", "/dʒɔɪn/", "参加；加入", kind="verb")
L.node("chess", "chess", "/tʃes/", "国际象棋")
L.node("painting", "painting", "/ˈpeɪntɪŋ/", "绘画；画", alt="paint", altLabel="来自")
L.node("imagine", "imagine", "/ɪˈmædʒɪn/", "想象", kind="verb")
L.node("camera", "camera", "/ˈkæmərə/", "照相机")
L.node("photo", "photo", "/ˈfoʊtoʊ/", "照片")
L.node("background", "background", "/ˈbækɡraʊnd/", "背景")
L.node("tent", "tent", "/tent/", "帐篷")
L.node("camping", "camping", "/ˈkæmpɪŋ/", "露营")
L.node("magazine", "magazine", "/ˌmæɡəˈziːn/", "杂志")
L.node("article", "article", "/ˈɑːrtɪkl/", "文章")
L.node("poem", "poem", "/ˈpoʊəm/", "诗")
L.node("inspiration", "inspiration", "/ˌɪnspəˈreɪʃn/", "灵感")
L.grid(["join club chess",
        "camping painting imagine",
        "tent photo background",
        ". camera .",
        "magazine article inspiration",
        ". poem ."], dy=330)
L.edge("join", "club"); L.edge("club", "chess"); L.edge("club", "painting"); L.edge("club", "camping")
L.edge("imagine", "painting"); L.edge("tent", "camping"); L.edge("camera", "photo", "拍"); L.edge("background", "photo")
L.edge("magazine", "article", "里面有"); L.edge("inspiration", "article"); L.edge("inspiration", "poem")

L.seg("title", zh("小朋友们好！放学以后，学校里有好多有趣的社团。今天，我们去参观一下！"), en("clubs"))
L.seg("map show:club focus:club", zh("喜欢同一件事的人，聚在一起，就是俱乐部、社团："), en("club"))
L.seg("show:join edge:join>club focus:join", zh("想参加一个社团，英语说"), en("join"), en("Can I join the club?"))
L.seg("show:chess edge:club>chess focus:chess", zh("第一个，棋社。国际象棋，英语是"), en("chess"), en("I joined chess club this morning."))
L.seg("show:painting edge:club>painting focus:painting", zh("第二个，画画社。画画，加上 i n g，就是绘画：", "alt:painting"), en("paint"), en("painting"))
L.seg("show:imagine edge:imagine>painting focus:imagine", zh("画画之前，先闭上眼睛，想象一下要画什么："), en("imagine"), en("Imagine a pink cloud!"))
L.seg("show:photo focus:photo", zh("第三个，摄影社。拍出来的照片，英语是"), en("photo"))
L.seg("show:camera edge:camera>photo focus:camera", zh("拍照，要用照相机："), en("camera"), en("The camera is for photo club."))
L.seg("show:background edge:background>photo focus:background", zh("照片里，站在人后面的风景，叫背景。后面，加上地面："),
      en("back"), en("ground"), en("background"))
L.seg("show:camping edge:club>camping focus:camping", zh("第四个，露营社。周末去野外住一晚，是露营："), en("camping"))
L.seg("show:tent edge:tent>camping focus:tent", zh("露营的时候，要搭一顶帐篷："), en("tent"))
L.seg("show:magazine focus:magazine", zh("第五个，文学社。我们来编一本自己的杂志："), en("magazine"))
L.seg("show:article edge:magazine>article focus:article", zh("杂志里，有一篇一篇的文章："), en("article"))
L.seg("show:poem focus:poem", zh("还有短短的、读起来像唱歌一样的诗："), en("poem"))
L.seg("show:inspiration edge:inspiration>article edge:inspiration>poem focus:inspiration",
      zh("写文章、写诗的时候，脑子里突然冒出一个好主意，叮！那就是灵感："), en("inspiration"))
L.seg("focus:chess,painting,photo,camping,magazine", zh("你想参加哪个社团呢？"),
      en("chess club", "focus:chess"), en("painting club", "focus:painting"), en("photo club", "focus:photo"),
      en("camping club", "focus:camping"), en("or a magazine club?", "focus:magazine"))
L.seg("focus:join,club", zh("说出你的选择吧："), en("I want to join the painting club!", "focus:join,painting"))
L.review([("club", "club"), ("join", "join"), ("chess", "chess"), ("painting", "painting"), ("imagine", "imagine"), ("photo", "photo"),
          ("camera", "camera"), ("background", "background"), ("camping", "camping"), ("tent", "tent"), ("magazine", "magazine"),
          ("article", "article"), ("poem", "poem"), ("inspiration", "inspiration")],
         "太棒了！用英语告诉你的好朋友，你最想参加哪个社团吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
