import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep46", "countryside", "乡村", 46, "field")
V = dict(kind="verb")
L.node("farm", "farm", "/fɑːrm/", "农场")
L.node("field", "field", "/fiːld/", "田地")
L.node("plants", "plants", "/plænts/", "植物（复数）")
L.node("kind", "kind", "/kaɪnd/", "种类", alt="a kind of", altLabel="常说")
L.node("corn", "corn", "/kɔːrn/", "玉米")
L.node("wheat", "wheat", "/wiːt/", "小麦")
L.node("cotton", "cotton", "/ˈkɑːtn/", "棉花")
L.node("pick", "pick", "/pɪk/", "摘", **V)
L.node("water", "water", "/ˈwɔːtər/", "浇水", **V)
L.node("live", "live", "/lɪv/", "活着", **V, alt="alive", altLabel="形容词")
L.node("die", "die", "/daɪ/", "死", **V, alt="dead", altLabel="形容词")
L.node("wood", "wood", "/wʊd/", "树林；木头", alt="woods", altLabel="树林")
L.node("duck", "duck", "/dʌk/", "鸭子")
L.node("rabbit", "rabbit", "/ˈræbɪt/", "兔子")
L.node("spider", "spider", "/ˈspaɪdər/", "蜘蛛")
L.grid(["kind plants field",
        "corn wheat farm",
        "pick cotton wood",
        "spider duck rabbit",
        "live water die"], dy=330)
L.edge("farm", "field"); L.edge("field", "plants"); L.edge("plants", "kind", dashed=True); L.edge("plants", "wheat"); L.edge("wheat", "corn", dashed=True)
L.edge("wheat", "cotton"); L.edge("cotton", "pick", "去"); L.edge("farm", "wood"); L.edge("wood", "duck"); L.edge("water", "live", "浇了")
L.edge("water", "die", "不浇"); L.edge("wood", "rabbit"); L.edge("duck", "spider")

L.seg("title", zh("小朋友们好！还记得第三十七集的农场吗？今天，我们再去乡下走一走！"), en("countryside"))
L.seg("map show:farm focus:farm", zh("农场："), en("farm"))
L.seg("show:field edge:farm>field focus:field", zh("农场旁边一大片田地："), en("field"))
L.seg("show:plants edge:field>plants focus:plants", zh("田里种着各种各样的植物："), en("plants"))
L.seg("show:kind edge:plants>kind focus:kind", zh("一种、一类，英语是"), en("kind"), zh("常常这样说：", "alt:kind"), en("a kind of plant"),
      zh("小提示：它还有一个意思，是善良的。"))
L.seg("show:wheat edge:plants>wheat focus:wheat", zh("金黄的小麦："), en("wheat"), zh("面包和面条，都是小麦做的哦。"))
L.seg("show:corn edge:wheat>corn focus:corn", zh("一粒一粒黄黄的玉米："), en("corn"))
L.seg("show:cotton edge:wheat>cotton focus:cotton", zh("白白软软的棉花："), en("cotton"), en("Corn, wheat and cotton are three kinds of plants."))
L.seg("show:pick edge:cotton>pick focus:pick", zh("棉花熟了，要去摘："), en("pick"), en("Let's pick cotton."))
L.seg("show:water focus:water", zh("植物要喝水，我们要给它浇水。水这个词，也可以当动词用："), en("water"), en("Water the corn in the morning."))
L.seg("show:live edge:water>live focus:live", zh("浇了水，植物就能活下来："), en("live"), zh("活着的，是", "alt:live"), en("alive"))
L.seg("show:die edge:water>die focus:die", zh("忘了浇水，植物就会死掉："), en("die"), zh("死了的，是", "alt:die"), en("dead"))
L.seg("show:wood edge:farm>wood focus:wood", zh("农场后面，有一片树林："), en("wood"), zh("树林常常说成", "alt:wood"), en("the woods"),
      zh("这个词也是木头的意思。"))
L.seg("show:duck edge:wood>duck focus:duck", zh("树林边的小河里，鸭子在游泳："), en("duck"))
L.seg("show:rabbit edge:wood>rabbit focus:rabbit", zh("草丛里，蹦出来一只小兔子："), en("rabbit"))
L.seg("show:spider edge:duck>spider focus:spider", zh("树枝上，蜘蛛在织网："), en("spider"))
L.seg("focus:live,die", zh("活着和死去，正好相反："), en("live, alive", "focus:live"), en("die, dead", "focus:die"))
L.seg("focus:none", zh("你在乡下看到了什么？"))
L.seg("", en("I see a duck.", "focus:duck"), en("I see a rabbit.", "focus:rabbit"), en("And a spider in the woods!", "focus:spider,wood"))
L.review([("farm", "farm"), ("field", "field"), ("plants", "plants"), ("kind", "kind"), ("wheat", "wheat"), ("corn", "corn"), ("cotton", "cotton"),
          ("pick", "pick"), ("water", "water"), ("live", "live, alive"), ("die", "die, dead"), ("wood", "wood"), ("duck", "duck"), ("rabbit", "rabbit"),
          ("spider", "spider")],
         "太棒了！下次去乡下，用英语说一说你看到的植物和动物吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
