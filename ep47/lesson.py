import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep47", "zoo", "动物园", 47, "zoo")
L.node("zoo", "zoo", "/zuː/", "动物园")
for id, ipa, z, pl in [("panda", "/ˈpændə/", "熊猫", None), ("bamboo", "/bæmˈbuː/", "竹子", None), ("lion", "/ˈlaɪən/", "狮子", None),
                       ("zebra", "/ˈziːbrə/", "斑马", None), ("giraffe", "/dʒəˈræf/", "长颈鹿", None), ("elephant", "/ˈelɪfənt/", "大象", None),
                       ("owl", "/aʊl/", "猫头鹰", None), ("monkey", "/ˈmʌŋki/", "猴子", ("monkeys", "/ˈmʌŋkiz/")), ("bear", "/ber/", "熊", None),
                       ("wolf", "/wʊlf/", "狼", ("wolves", "/wʊlvz/")), ("shark", "/ʃɑːrk/", "鲨鱼", None), ("whale", "/weɪl/", "鲸", None)]:
    kw = dict(plural=pl[0], pluralIpa=pl[1]) if pl else {}
    L.node(id, id, ipa, z, **kw)
L.grid(["bamboo panda lion",
        "owl zoo zebra",
        "monkey . giraffe",
        "bear wolf elephant",
        "shark . whale"], dy=330)
for b in ["panda", "lion", "zebra", "owl", "monkey", "giraffe", "bear", "wolf", "elephant"]:
    L.edge("zoo", b)
L.edge("panda", "bamboo", "爱吃"); L.edge("bear", "shark", dashed=True); L.edge("elephant", "whale", dashed=True)

L.seg("title", zh("小朋友们好！还记得第四十三集的动物园吗？今天，我们进去好好逛一逛！"), en("zoo"))
L.seg("map show:zoo focus:zoo", zh("动物园："), en("zoo"), zh("两个 o，读成长长的 u。"))
L.seg("show:panda edge:zoo>panda focus:panda", zh("第一站，去看中国的国宝，大熊猫："), en("panda"))
L.seg("show:bamboo edge:panda>bamboo focus:bamboo", zh("熊猫最爱吃竹子："), en("bamboo"), en("Pandas eat bamboo all day."))
L.seg("show:lion edge:zoo>lion focus:lion", zh("森林之王，狮子："), en("lion"))
L.seg("show:zebra edge:zoo>zebra focus:zebra", zh("身上有黑白条纹的斑马："), en("zebra"))
L.seg("show:giraffe edge:zoo>giraffe focus:giraffe", zh("脖子长长的长颈鹿："), en("giraffe"), zh("还记得第二十八集的长 long 吗？"),
      en("The giraffe has a long neck."))
L.seg("show:elephant edge:zoo>elephant focus:elephant", zh("鼻子长长的大象："), en("elephant"))
L.seg("show:owl edge:zoo>owl focus:owl", zh("晚上才睁大眼睛的猫头鹰："), en("owl"))
L.seg("show:monkey edge:zoo>monkey focus:monkey", zh("爬树最快的猴子："), en("monkey"), zh("很多只猴子：", "plural:monkey"), en("monkeys"),
      en("Monkeys and owls live in the trees.", "focus:monkey,owl"))
L.seg("show:bear edge:zoo>bear focus:bear", zh("胖乎乎的熊："), en("bear"))
L.seg("show:wolf edge:zoo>wolf focus:wolf", zh("嗷呜，狼："), en("wolf"),
      zh("很多只狼，也是 f 变成 v e s。还记得 leaf 和 leaves 吗？", "plural:wolf"), en("wolves"))
L.seg("show:shark edge:bear>shark focus:shark", zh("海洋馆里，有凶猛的鲨鱼："), en("shark"))
L.seg("show:whale edge:elephant>whale focus:whale", zh("还有世界上最大的动物，鲸："), en("whale"), zh("开头的 w h，只读 w。"))
L.seg("focus:elephant,whale", zh("陆地上最大的是大象，大海里最大的是鲸："), en("elephant", "focus:elephant"), en("whale", "focus:whale"))
L.seg("focus:none", zh("猜一猜，我是谁？"))
L.seg("", en("I am black and white. I eat bamboo.", "focus:none"), en("Panda!", "focus:panda"),
      en("I have a very long neck.", "focus:none"), en("Giraffe!", "focus:giraffe"))
L.review([("zoo", "zoo"), ("panda", "panda"), ("bamboo", "bamboo"), ("lion", "lion"), ("zebra", "zebra"), ("giraffe", "giraffe"),
          ("elephant", "elephant"), ("owl", "owl"), ("monkey", "monkey, monkeys"), ("bear", "bear"), ("wolf", "wolf, wolves"),
          ("shark", "shark"), ("whale", "whale")],
         "太棒了！你最喜欢动物园里的哪种动物？用英语告诉爸爸妈妈吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
