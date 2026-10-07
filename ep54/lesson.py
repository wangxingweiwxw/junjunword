import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep54", "animal traits", "动物特点", 54, "cute")
A = dict(kind="adj")
L.node("size", "size", "/saɪz/", "大小；尺寸")
L.node("big", "big", "/bɪɡ/", "大的", **A)
L.node("small", "small", "/smɔːl/", "小的", **A)
L.node("brave", "brave", "/breɪv/", "勇敢的", **A)
L.node("cute", "cute", "/kjuːt/", "可爱的", **A)
L.node("funny", "funny", "/ˈfʌni/", "好笑的", **A)
L.node("humorous", "humorous", "/ˈhjuːmərəs/", "幽默的", **A)
L.node("smart", "smart", "/smɑːrt/", "聪明的", **A)
L.node("stupid", "stupid", "/ˈstuːpɪd/", "笨的", **A)
L.node("silly", "silly", "/ˈsɪli/", "傻乎乎的", **A)
L.node("though", "though", "/ðoʊ/", "不过；虽然", kind="adv")
L.grid(["big size small",
        "brave cute .",
        "funny humorous .",
        "smart stupid silly",
        ". though ."], dy=330)
L.edge("size", "big"); L.edge("size", "small"); L.edge("small", "cute", dashed=True); L.edge("funny", "humorous", "更文雅")
L.edge("smart", "stupid", "反义"); L.edge("stupid", "silly", "差不多")

L.seg("title", zh("小朋友们好！每种动物都有自己的特点。今天，我们来学描述动物的形容词！"))
L.seg("map show:size focus:size", zh("动物有大有小。大小、尺寸，英语是"), en("size"))
L.seg("show:big edge:size>big focus:big", zh("大象很大："), en("big"), en("Elephants are big."))
L.seg("show:small edge:size>small focus:small", zh("老鼠很小："), en("small"), en("Mice are small."), zh("还记得第四十五集学过的 mice 吗？"))
L.seg("show:cute edge:small>cute focus:cute", zh("小小的动物，常常很可爱："), en("cute"), en("The puppy is so cute!"))
L.seg("show:brave focus:brave", zh("不怕危险，是勇敢的："), en("brave"), en("The little dog is brave."))
L.seg("show:funny focus:funny", zh("让人哈哈大笑的，是好笑的："), en("funny"), en("Pigs are funny."))
L.seg("show:humorous edge:funny>humorous focus:humorous", zh("会讲笑话、说话风趣的，是幽默的："), en("humorous"))
L.seg("show:smart focus:smart", zh("脑子转得快，是聪明的："), en("smart"), en("Monkeys are smart."))
L.seg("show:stupid edge:smart>stupid focus:stupid", zh("聪明的反面，是笨的："), en("stupid"),
      zh("这个词有点不礼貌，可别用来说别人哦。"))
L.seg("show:silly edge:stupid>silly focus:silly", zh("傻乎乎的、调皮的，是"), en("silly"), en("Don't be silly!"))
L.seg("show:though focus:though", zh("最后学一个小词：不过、虽然。"), en("though"), en("My dog is small, though it is brave."),
      zh("还记得第三十四集的 although 吗？意思差不多。"))
L.seg("focus:big,small", zh("一大一小："), en("big", "focus:big"), en("small", "focus:small"))
L.seg("focus:none", zh("描述一下你喜欢的动物吧！"))
L.seg("", en("My cat is small and cute.", "focus:small,cute"), en("It is very smart.", "focus:smart"), en("And a little bit silly!", "focus:silly"))
L.review([("size", "size"), ("big", "big"), ("small", "small"), ("cute", "cute"), ("brave", "brave"), ("funny", "funny"), ("humorous", "humorous"),
          ("smart", "smart"), ("stupid", "stupid"), ("silly", "silly"), ("though", "though")],
         "太棒了！用英语描述一下你最喜欢的动物吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
