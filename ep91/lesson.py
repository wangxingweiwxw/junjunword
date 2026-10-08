import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep91", "materials", "材料", 91, "material")
L.node("material", "material", "/məˈtɪriəl/", "材料")
L.node("natural", "natural", "/ˈnætʃrəl/", "天然的", kind="adj", alt="nature", altLabel="来自")
L.node("quality", "quality", "/ˈkwɑːləti/", "质量")
for id, ipa, z in [("plastic", "/ˈplæstɪk/", "塑料"), ("glass", "/ɡlæs/", "玻璃"), ("silk", "/sɪlk/", "丝绸"), ("sand", "/sænd/", "沙子"), ("stone", "/stoʊn/", "石头"),
                   ("steel", "/stiːl/", "钢"), ("iron", "/ˈaɪərn/", "铁")]:
    L.node(id, id, ipa, z)
L.node("wooden", "wooden", "/ˈwʊdn/", "木制的", kind="adj", alt="wood", altLabel="来自")
L.grid(["natural material quality",
        "plastic glass silk",
        "wooden sand stone",
        "iron steel ."], dy=350)
L.edge("natural", "material"); L.edge("quality", "material"); L.edge("material", "plastic"); L.edge("material", "glass"); L.edge("material", "silk")
L.edge("material", "sand", dashed=True); L.edge("glass", "sand", "用…做"); L.edge("sand", "stone", dashed=True); L.edge("silk", "stone", dashed=True)
L.edge("plastic", "wooden", dashed=True); L.edge("iron", "steel", "炼成")

L.seg("title", zh("小朋友们好！东西都是用什么做的呢？今天，我们来学材料！"), en("materials"))
L.seg("map show:material focus:material", zh("做东西用的原料，是材料："), en("material"))
L.seg("show:natural edge:natural>material focus:natural", zh("大自然里本来就有的，是天然的。还记得第八十六集的 nature 吗？"), en("natural"))
L.seg("show:quality edge:quality>material focus:quality", zh("材料好不好，看质量："), en("quality"), en("good quality"))
L.seg("show:plastic edge:material>plastic focus:plastic", zh("轻轻的塑料瓶："), en("plastic"), en("This company makes plastic."))
L.seg("show:glass edge:material>glass focus:glass", zh("透明的玻璃："), en("glass"), zh("它也是玻璃杯的意思。"))
L.seg("show:silk edge:material>silk focus:silk", zh("中国有名的丝绸，滑滑的："), en("silk"))
L.seg("show:wooden edge:plastic>wooden focus:wooden", zh("木头是 wood，加上 e n，就是木制的："), en("wood"), en("wooden"), en("a wooden chair"))
L.seg("show:sand edge:glass>sand edge:material>sand focus:sand", zh("海边的沙子。玻璃就是用沙子做的哦："), en("sand"))
L.seg("show:stone edge:sand>stone focus:stone", zh("硬硬的石头："), en("stone"), zh("还记得第八十五集的 rock 吗？"))
L.seg("show:iron focus:iron", zh("铁："), en("iron"), zh("r 几乎不发音，读 ai ern。"))
L.seg("show:steel edge:iron>steel focus:steel", zh("铁炼成的更结实的钢："), en("steel"))
L.seg("focus:none", zh("猜一猜，它们是用什么做的？"))
L.seg("", en("A window is made of glass.", "focus:glass"), en("A bottle is made of plastic.", "focus:plastic"), en("A bridge is made of steel.", "focus:steel"))
L.review([("material", "material"), ("natural", "natural"), ("quality", "quality"), ("plastic", "plastic"), ("glass", "glass"), ("silk", "silk"), ("wooden", "wooden"),
          ("sand", "sand"), ("stone", "stone"), ("iron", "iron"), ("steel", "steel")],
         "太棒了！看看你身边的东西，用英语说一说它们是用什么做的吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
