import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep51", "town", "城镇（二）", 51, "library")
V = dict(kind="verb")
L.node("town", "town", "/taʊn/", "城镇")
L.node("street", "street", "/striːt/", "街道")
L.node("corner", "corner", "/ˈkɔːrnər/", "拐角")
L.node("across", "across", "/əˈkrɔːs/", "穿过；在对面", kind="prep")
L.node("church", "church", "/tʃɜːrtʃ/", "教堂")
L.node("factory", "factory", "/ˈfæktəri/", "工厂")
L.node("prison", "prison", "/ˈprɪzn/", "监狱")
L.node("grounds", "grounds", "/ɡraʊndz/", "场地", alt="ground", altLabel="来自")
L.node("library", "library", "/ˈlaɪbreri/", "图书馆")
L.node("borrow", "borrow", "/ˈbɑːroʊ/", "借入", **V)
L.node("lend", "lend", "/lend/", "借出", **V)
L.node("return", "return", "/rɪˈtɜːrn/", "归还", **V)
L.node("bank", "bank", "/bæŋk/", "银行")
L.grid(["corner street across",
        "church town factory",
        "prison grounds .",
        "borrow library lend",
        ". return bank"], dy=330)
L.edge("town", "street"); L.edge("street", "corner"); L.edge("street", "across"); L.edge("town", "church"); L.edge("town", "factory")
L.edge("town", "grounds"); L.edge("grounds", "prison", dashed=True); L.edge("library", "borrow"); L.edge("library", "lend"); L.edge("library", "return")
L.edge("bank", "lend", dashed=True); L.edge("grounds", "library", dashed=True)

L.seg("title", zh("小朋友们好！还记得第四十三集的城镇吗？今天，我们去认识城镇里更多的地方。"), en("town"))
L.seg("map show:town focus:town", zh("城镇："), en("town"))
L.seg("show:street edge:town>street focus:street", zh("走上街道："), en("street"))
L.seg("show:corner edge:street>corner focus:corner", zh("街道转弯的地方，是拐角："), en("corner"), en("at the corner"))
L.seg("show:across edge:street>across focus:across", zh("从街的这边到那边，是穿过；在街的那边，是在对面："), en("across"), en("across the street"))
L.seg("show:church edge:town>church focus:church", zh("屋顶尖尖、有十字架的建筑，是教堂："), en("church"))
L.seg("show:factory edge:town>factory focus:factory", zh("烟囱冒烟、机器轰隆隆的，是工厂："), en("factory"))
L.seg("show:grounds edge:town>grounds focus:grounds", zh("一大片空地，可以运动、做活动的，是场地："), en("grounds"),
      zh("它来自地面：", "alt:grounds"), en("ground"), en("school grounds"))
L.seg("show:prison edge:grounds>prison focus:prison", zh("坏人被关起来的地方，是监狱："), en("prison"),
      zh("还记得第四十八集吗？偷东西，就可能被关进这里。"), en("steal"))
L.seg("show:library edge:grounds>library focus:library", zh("有很多很多书，可以免费借书看的，是图书馆："), en("library"))
L.seg("show:borrow edge:library>borrow focus:borrow", zh("从图书馆把书借来，是借入："), en("borrow"), en("I borrow a book from the library."))
L.seg("show:lend edge:library>lend focus:lend", zh("把东西借给别人，是借出："), en("lend"), en("Can you lend me a pen?"))
L.seg("focus:borrow,lend", zh("借入和借出，方向正好相反，可别弄混了："), en("borrow", "focus:borrow"), en("lend", "focus:lend"))
L.seg("show:return edge:library>return focus:return", zh("书看完了，要按时还回去："), en("return"), en("Return the book on time."))
L.seg("show:bank edge:bank>lend focus:bank", zh("存钱、取钱的地方，是银行："), en("bank"), zh("银行也会把钱借给需要的人。"))
L.seg("focus:none", zh("给朋友指一指路吧！"))
L.seg("", en("The library is at the corner.", "focus:library,corner"), en("The bank is across the street.", "focus:bank,across"))
L.review([("town", "town"), ("street", "street"), ("corner", "corner"), ("across", "across"), ("church", "church"), ("factory", "factory"),
          ("grounds", "grounds"), ("prison", "prison"), ("library", "library"), ("borrow", "borrow"), ("lend", "lend"), ("return", "return"), ("bank", "bank")],
         "太棒了！周末去图书馆借一本书吧，记得按时还哦。点一点图上的单词，还能再听一遍发音。")
L.save()
