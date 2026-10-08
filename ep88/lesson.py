import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep88", "kitchen", "厨房", 88, "pot")
V = dict(kind="verb")
L.node("cook", "cook", "/kʊk/", "做饭", **V)
L.node("prepare", "prepare", "/prɪˈper/", "准备", **V)
L.node("oven", "oven", "/ˈʌvn/", "烤箱")
L.node("turnoff", "turn off", "/tɜːrn ɔːf/", "关掉", **V, alt="turn on", altLabel="反义")
L.node("pot", "pot", "/pɑːt/", "锅")
L.node("boil", "boil", "/bɔɪl/", "煮沸", **V)
L.node("lid", "lid", "/lɪd/", "盖子")
L.node("cover", "cover", "/ˈkʌvər/", "盖上", **V)
L.node("bottle", "bottle", "/ˈbɑːtl/", "瓶子")
L.node("cap", "cap", "/kæp/", "瓶盖", icon="bottlecap")
L.node("fill", "fill", "/fɪl/", "装满", **V)
L.node("bowl", "bowl", "/boʊl/", "碗")
L.node("chopsticks", "chopsticks", "/ˈtʃɑːpstɪks/", "筷子")
L.node("knife", "knife", "/naɪf/", "刀", plural="knives", pluralIpa="/naɪvz/")
L.node("fork", "fork", "/fɔːrk/", "叉子")
L.grid(["prepare oven turnoff",
        "boil cook pot",
        "lid cover bottle",
        "fill cap .",
        "bowl chopsticks knife",
        ". fork ."], dy=310)
for id, x, y in [("prepare", 180, 150), ("cook", 180, 470), ("oven", 180, 790), ("turnoff", 540, 790), ("pot", 540, 470), ("boil", 540, 150), ("lid", 900, 150),
                 ("cover", 900, 470), ("bottle", 1260, 470), ("cap", 1260, 150), ("fill", 900, 790), ("chopsticks", 1620, 470), ("bowl", 1620, 150),
                 ("knife", 1620, 790), ("fork", 1260, 790)]:
    L.byid[id]["at"] = [x, y]
L.edge("prepare", "cook"); L.edge("cook", "oven"); L.edge("oven", "turnoff"); L.edge("cook", "pot"); L.edge("pot", "boil"); L.edge("pot", "lid")
L.edge("lid", "cover"); L.edge("bottle", "cap"); L.edge("bottle", "fill")
L.edge("chopsticks", "bowl"); L.edge("chopsticks", "knife"); L.edge("chopsticks", "fork")

L.seg("title", zh("小朋友们好！今天，我们走进厨房，一起做饭吧！"), en("cook food"))
L.seg("map show:cook focus:cook", zh("还记得第三十五集的厨师吗？做饭，也是这个词："), en("cook"))
L.seg("show:prepare edge:prepare>cook focus:prepare", zh("做饭前，先把菜洗好、切好，做准备："), en("prepare"), zh("还记得第五十五集的 preparation 吗？"))
L.seg("show:oven edge:cook>oven focus:oven", zh("烤面包，要用烤箱："), en("oven"))
L.seg("show:turnoff edge:oven>turnoff focus:turnoff", zh("烤好了，记得关掉："), en("turn off"), zh("打开，是", "alt:turnoff"), en("turn on"))
L.seg("show:pot edge:cook>pot focus:pot", zh("煮汤，要用锅："), en("pot"))
L.seg("show:boil edge:pot>boil focus:boil", zh("水咕嘟咕嘟煮开了："), en("boil"))
L.seg("show:lid edge:pot>lid focus:lid", zh("锅上有一个盖子："), en("lid"))
L.seg("show:cover edge:lid>cover focus:cover", zh("把盖子盖上，是"), en("cover"), en("Cover the pot with the lid.", "focus:cover,lid,pot"))
L.seg("show:bottle focus:bottle", zh("装油和醋的瓶子："), en("bottle"))
L.seg("show:cap edge:bottle>cap focus:cap", zh("瓶子上拧着瓶盖。还记得第十集的鸭舌帽吗？同一个词！"), en("cap"))
L.seg("show:fill edge:bottle>fill focus:fill", zh("把瓶子装满水："), en("fill"), en("Fill the bottle with water."))
L.seg("show:chopsticks focus:chopsticks", zh("饭做好了！中国人用筷子吃饭："), en("chopsticks"), zh("筷子是一双，所以总有 s。"))
L.seg("show:bowl edge:chopsticks>bowl focus:bowl", zh("盛饭的碗："), en("bowl"))
L.seg("show:knife edge:chopsticks>knife focus:knife", zh("西餐用刀："), en("knife"), zh("k 不发音。很多把刀，f 变成 v e s：", "plural:knife"), en("knives"))
L.seg("show:fork edge:chopsticks>fork focus:fork", zh("还有叉子："), en("fork"))
L.review([("cook", "cook"), ("prepare", "prepare"), ("oven", "oven"), ("turnoff", "turn off"), ("pot", "pot"), ("boil", "boil"), ("lid", "lid"), ("cover", "cover"),
          ("bottle", "bottle"), ("cap", "cap"), ("fill", "fill"), ("chopsticks", "chopsticks"), ("bowl", "bowl"), ("knife", "knife, knives"), ("fork", "fork")],
         "太棒了！帮爸爸妈妈摆一摆碗筷吧。小提示：刀和火都很危险，一定要大人陪着哦。点一点图上的单词，还能再听一遍发音。")
L.save()
