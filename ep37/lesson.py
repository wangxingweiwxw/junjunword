import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep37", "farm", "农场", 37, "farm")
L.node("farm", "farm", "/fɑːrm/", "农场")
L.node("field", "field", "/fiːld/", "田野；田地")
L.node("grass", "grass", "/ɡræs/", "草")
L.node("plant", "plant", "/plænt/", "植物")
L.node("tree", "tree", "/triː/", "树")
L.node("leaf", "leaf", "/liːf/", "叶子", plural="leaves", pluralIpa="/liːvz/")
L.node("pig", "pig", "/pɪɡ/", "猪")
L.node("sheep", "sheep", "/ʃiːp/", "绵羊")
L.node("horse", "horse", "/hɔːrs/", "马")
L.node("cow", "cow", "/kaʊ/", "奶牛")
L.node("hen", "hen", "/hen/", "母鸡")
L.node("lay", "lay", "/leɪ/", "下（蛋）", kind="verb")
L.node("egg", "egg", "/eɡ/", "蛋")
L.node("fox", "fox", "/fɑːks/", "狐狸")
L.grid(["grass field plant",
        "sheep farm tree",
        "horse pig leaf",
        "cow hen fox",
        "egg lay ."], dy=330)
L.edge("farm", "field"); L.edge("field", "grass"); L.edge("field", "plant"); L.edge("plant", "tree"); L.edge("tree", "leaf")
L.edge("farm", "pig"); L.edge("farm", "sheep"); L.edge("sheep", "horse"); L.edge("horse", "cow"); L.edge("pig", "hen")
L.edge("hen", "lay"); L.edge("lay", "egg"); L.edge("fox", "hen", "想吃", dashed=True)

L.seg("title", zh("小朋友们好！跟着我，去乡下的农场玩一天吧！"), en("farm"), zh("农场。"))
L.seg("map show:farm focus:farm", zh("养着很多动物、种着庄稼的地方，是农场："), en("farm"), en("Welcome to the farm!"))
L.seg("show:field edge:farm>field focus:field", zh("农场旁边，是一大片田野："), en("field"))
L.seg("show:grass edge:field>grass focus:grass", zh("田野上长满了绿绿的草："), en("grass"))
L.seg("show:plant edge:field>plant focus:plant", zh("地里种着各种植物："), en("plant"))
L.seg("show:tree edge:plant>tree focus:tree", zh("最高大的植物，是树："), en("tree"))
L.seg("show:leaf edge:tree>leaf focus:leaf", zh("树上长着一片一片的叶子："), en("leaf"),
      zh("很多叶子，要把 f 变成 v e s。还记得第三十四集的妻子 wives 吗？一样的规律！", "plural:leaf"), en("leaves"),
      en("In autumn, the leaves are orange."))
L.seg("show:pig edge:farm>pig focus:pig", zh("农场里，胖胖的猪在哼哼叫："), en("pig"))
L.seg("show:sheep edge:farm>sheep focus:sheep", zh("毛茸茸的绵羊："), en("sheep"),
      zh("很多只羊，还是叫 sheep，不加 s 哦。"), en("one sheep, two sheep"))
L.seg("show:horse edge:sheep>horse focus:horse", zh("跑得飞快的马："), en("horse"))
L.seg("show:cow edge:horse>cow focus:cow", zh("能产牛奶的奶牛："), en("cow"), en("Cows, horses and sheep eat grass.", "focus:cow,horse,sheep,grass"))
L.seg("show:hen edge:pig>hen focus:hen", zh("咯咯哒，母鸡在叫："), en("hen"))
L.seg("show:lay edge:hen>lay focus:lay", zh("母鸡要下蛋啦！下蛋的下，英语是"), en("lay"))
L.seg("show:egg edge:lay>egg focus:egg", zh("下出来一个圆圆的蛋："), en("egg"), en("The hen lays an egg."))
L.seg("show:fox edge:fox>hen focus:fox", zh("哎呀，草丛里有一只狐狸，它想偷吃小鸡！"), en("fox"), en("Watch out, hen!"))
L.seg("focus:none", zh("农场里的动物，都会叫！我们来学一学："))
L.seg("", en("The pig says oink oink.", "focus:pig"), en("The sheep says baa.", "focus:sheep"),
      en("The cow says moo.", "focus:cow"), en("The hen says cluck cluck.", "focus:hen"))
L.review([("farm", "farm"), ("field", "field"), ("grass", "grass"), ("plant", "plant"), ("tree", "tree"), ("leaf", "leaf, leaves"),
          ("pig", "pig"), ("sheep", "sheep"), ("horse", "horse"), ("cow", "cow"), ("hen", "hen"), ("lay", "lay"), ("egg", "egg"), ("fox", "fox")],
         "太棒了！你最喜欢农场里的哪种动物？用英语告诉爸爸妈妈吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
