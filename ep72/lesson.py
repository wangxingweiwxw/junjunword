import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep72", "compass", "方位", 72, "north")
A = dict(kind="adj")
for id, ipa, z in [("north", "/nɔːrθ/", "北"), ("south", "/saʊθ/", "南"), ("east", "/iːst/", "东"), ("west", "/west/", "西")]:
    L.node(id, id, ipa, z)
for id, ipa, z in [("northern", "/ˈnɔːrðərn/", "北方的"), ("southern", "/ˈsʌðərn/", "南方的"), ("eastern", "/ˈiːstərn/", "东方的"), ("western", "/ˈwestərn/", "西方的")]:
    L.node(id, id, ipa, z, **A)
L.node("then", "then", "/ðen/", "然后", kind="adv", alt="and then", altLabel="常说")
L.grid(["north . northern",
        "south . southern",
        "east then eastern",
        "west . western"], dy=340)
for i, d in enumerate(["north", "south", "east", "west"]):
    L.byid[d]["at"] = [270 + i * 420, 150]; L.byid[d + "ern"]["at"] = [270 + i * 420, 470]
L.byid["then"]["at"] = [900, 740]
for a in ["north", "south", "east", "west"]:
    L.edge(a, a + "ern", "+ern")

L.seg("title", zh("小朋友们好！拿出指南针，我们来学东南西北！"), en("north, south, east, west"))
L.seg("map show:north focus:north", zh("指南针的红针指向北方："), en("north"))
L.seg("show:south focus:south", zh("北的对面，是南："), en("south"), zh("最后的 t h，舌尖放在牙齿中间。"))
L.seg("show:east focus:east", zh("太阳升起的地方，是东："), en("east"))
L.seg("show:west focus:west", zh("太阳落下的地方，是西："), en("west"))
L.seg("focus:north,south,east,west", zh("中文说东南西北，英语常常说："), en("north, south, east, west"))
L.seg("show:northern edge:north>northern focus:northern", zh("在后面加上 e r n，就变成了形容词。北方的："), en("northern"))
L.seg("show:southern edge:south>southern focus:southern", zh("南方的，要小心，读音变成了 suh："), en("southern"))
L.seg("show:eastern edge:east>eastern focus:eastern", zh("东方的："), en("eastern"))
L.seg("show:western edge:west>western focus:western", zh("西方的："), en("western"))
L.seg("show:then focus:then", zh("指路的时候，先做一件事，然后做另一件事。然后，英语是"), en("then"),
      zh("常常说", "alt:then"), en("and then"), en("Go north and then go east.", "focus:north,east,then"))
L.seg("focus:none", zh("还记得第五十三集的转弯 turn 吗？我们来指路："))
L.seg("", en("Go north.", "focus:north"), en("Then turn east at the supermarket.", "focus:east,then"), en("Go southwest for two kilometers.", "focus:south,west"))
L.review([("north", "north"), ("south", "south"), ("east", "east"), ("west", "west"), ("northern", "northern"), ("southern", "southern"),
          ("eastern", "eastern"), ("western", "western"), ("then", "then, and then")],
         "太棒了！看看你家的窗户朝哪个方向，用英语说一说吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
