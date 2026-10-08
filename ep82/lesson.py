import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep82", "furniture", "家具", 82, "furniture")
L.node("apartment", "apartment", "/əˈpɑːrtmənt/", "公寓", alt="flat", altLabel="英式")
L.node("wall", "wall", "/wɔːl/", "墙")
L.node("mirror", "mirror", "/ˈmɪrər/", "镜子")
L.node("shelf", "shelf", "/ʃelf/", "架子", plural="shelves", pluralIpa="/ʃelvz/")
L.node("bookcase", "bookcase", "/ˈbʊkkeɪs/", "书柜")
L.node("reach", "reach", "/riːtʃ/", "够到", kind="verb")
L.node("furniture", "furniture", "/ˈfɜːrnɪtʃər/", "家具")
L.node("bed", "bed", "/bed/", "床")
L.node("quilt", "quilt", "/kwɪlt/", "被子")
L.node("sofa", "sofa", "/ˈsoʊfə/", "沙发")
L.node("table", "table", "/ˈteɪbl/", "桌子")
L.node("chair", "chair", "/tʃer/", "椅子")
L.node("drawer", "drawer", "/drɔːr/", "抽屉", alt="draw", altLabel="来自")
L.grid(["mirror wall shelf",
        "apartment . reach",
        "bookcase furniture sofa",
        "bed drawer table",
        "quilt . chair"], dy=330)
L.edge("apartment", "wall"); L.edge("wall", "mirror"); L.edge("wall", "shelf"); L.edge("reach", "shelf"); L.edge("apartment", "furniture")
L.edge("furniture", "bookcase"); L.edge("furniture", "sofa"); L.edge("furniture", "bed"); L.edge("bed", "quilt"); L.edge("furniture", "drawer"); L.edge("furniture", "table"); L.edge("table", "chair")

L.seg("title", zh("小朋友们好！搬新家啦！今天，我们来认识家里的家具。"), en("furniture"))
L.seg("map show:apartment focus:apartment", zh("高楼里的一套房子，是公寓："), en("apartment"), zh("在英国，常常叫", "alt:apartment"), en("flat"))
L.seg("show:wall edge:apartment>wall focus:wall", zh("房间四周，是墙："), en("wall"))
L.seg("show:mirror edge:wall>mirror focus:mirror", zh("墙上挂着一面镜子："), en("mirror"))
L.seg("show:shelf edge:wall>shelf focus:shelf", zh("墙上还钉着架子："), en("shelf"), zh("很多个架子，f 变成 v e s：", "plural:shelf"), en("shelves"), zh("还记得 leaf 和 wolf 吗？"))
L.seg("show:reach edge:reach>shelf focus:reach", zh("架子太高，踮起脚才够得到："), en("reach"))
L.seg("show:furniture edge:apartment>furniture focus:furniture", zh("屋里摆的桌椅床柜，统称家具："), en("furniture"), zh("家具不能数，不加 s 哦。"))
L.seg("show:bookcase edge:furniture>bookcase focus:bookcase", zh("放书的柜子。书，加上箱子："), en("book"), en("case"), en("bookcase"))
L.seg("show:sofa edge:furniture>sofa focus:sofa", zh("软软的沙发："), en("sofa"))
L.seg("show:bed edge:furniture>bed focus:bed", zh("睡觉的床："), en("bed"))
L.seg("show:quilt edge:bed>quilt focus:quilt", zh("床上铺着被子："), en("quilt"))
L.seg("show:drawer edge:furniture>drawer focus:drawer", zh("可以拉出来的抽屉。拉，加上 e r："), en("draw"), en("drawer"))
L.seg("show:table edge:furniture>table focus:table", zh("吃饭的桌子："), en("table"))
L.seg("show:chair edge:table>chair focus:chair", zh("坐的椅子："), en("chair"))
L.seg("focus:none", zh("布置一下我的房间吧！"))
L.seg("", en("The bed is beside the wall.", "focus:bed,wall"), en("The books are on the shelves.", "focus:shelf"), en("The chair is under the table.", "focus:chair,table"))
L.review([("apartment", "apartment, flat"), ("wall", "wall"), ("mirror", "mirror"), ("shelf", "shelf, shelves"), ("reach", "reach"), ("furniture", "furniture"),
          ("bookcase", "bookcase"), ("sofa", "sofa"), ("bed", "bed"), ("quilt", "quilt"), ("drawer", "drawer"), ("table", "table"), ("chair", "chair")],
         "太棒了！回家看一看，用英语说一说你家有哪些家具吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
