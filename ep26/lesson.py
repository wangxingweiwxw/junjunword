import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep26", "relatives", "亲戚", 26, "relative")
L.node("grandparents", "grandparents", "/ˈɡrænperənts/", "祖父母")
L.node("grandfather", "grandfather", "/ˈɡrænfɑːðər/", "爷爷；外公", alt="grandpa", altLabel="口语")
L.node("grandmother", "grandmother", "/ˈɡrænmʌðər/", "奶奶；外婆", alt="grandma", altLabel="口语")
L.node("grandson", "grandson", "/ˈɡrænsʌn/", "孙子；外孙")
L.node("granddaughter", "granddaughter", "/ˈɡrændɔːtər/", "孙女；外孙女")
L.node("uncle", "uncle", "/ˈʌŋkl/", "叔叔；舅舅")
L.node("aunt", "aunt", "/ænt/", "阿姨；姑姑")
L.node("cousin", "cousin", "/ˈkʌzn/", "堂/表兄弟姐妹", plural="cousins", pluralIpa="/ˈkʌznz/")
L.node("relative", "relative", "/ˈrelətɪv/", "亲戚", plural="relatives", pluralIpa="/ˈrelətɪvz/")
L.grid(["grandfather grandparents grandmother",
        "grandson . granddaughter",
        "uncle cousin aunt",
        ". relative ."], dy=360)
L.edge("grandfather", "grandparents"); L.edge("grandmother", "grandparents")
L.edge("grandparents", "grandson"); L.edge("grandparents", "granddaughter")
L.edge("uncle", "cousin"); L.edge("aunt", "cousin"); L.edge("cousin", "relative")

L.seg("title", zh("小朋友们好！过年的时候，家里来了好多亲戚。还记得第二集的家人吗？今天，我们认识更多家人。"), en("relatives"))
L.seg("focus:none", zh("今天有一个小秘密：在家人的名字前面加上"), en("grand"), zh("就变成了长一辈，或者小一辈的家人。"))
L.seg("map show:grandfather focus:grandfather", zh("爸爸的爸爸，或者妈妈的爸爸，就是爷爷或外公："), en("father"), en("grandfather"),
      zh("在家里，可以亲切地叫他", "alt:grandfather"), en("Grandpa"))
L.seg("show:grandmother focus:grandmother", zh("爸爸的妈妈，或者妈妈的妈妈，就是奶奶或外婆："), en("mother"), en("grandmother"),
      zh("亲切地叫她", "alt:grandmother"), en("Grandma"))
L.seg("show:grandparents edge:grandfather>grandparents edge:grandmother>grandparents focus:grandparents",
      zh("他们两个合在一起，就是祖父母："), en("parents"), en("grandparents"))
L.seg("show:grandson edge:grandparents>grandson focus:grandson", zh("对爷爷奶奶来说，你如果是男孩，就是他们的孙子："),
      en("son"), en("grandson"))
L.seg("show:granddaughter edge:grandparents>granddaughter focus:granddaughter", zh("如果是女孩，就是孙女："),
      en("daughter"), en("granddaughter"), zh("注意哦，这里有两个字母 d 连在一起。"))
L.seg("focus:grandfather,grandmother,grandson,granddaughter", zh("加上 grand，家人就变多啦："),
      en("father, grandfather", "focus:grandfather"), en("mother, grandmother", "focus:grandmother"),
      en("son, grandson", "focus:grandson"), en("daughter, granddaughter", "focus:granddaughter"))
L.seg("show:uncle focus:uncle", zh("爸爸妈妈的兄弟，叔叔、舅舅、伯伯，英语都叫"), en("uncle"),
      en("My uncle is my grandfather's son."))
L.seg("show:aunt focus:aunt", zh("爸爸妈妈的姐妹，姑姑、阿姨，英语都叫"), en("aunt"))
L.seg("show:cousin edge:uncle>cousin edge:aunt>cousin focus:cousin", zh("叔叔阿姨家的孩子，堂哥、表妹，英语都叫"), en("cousin"),
      zh("小提示：中间的 o u，读短短的 a。"), en("My cousin is in the car."))
L.seg("show:relative edge:cousin>relative focus:relative", zh("所有这些亲人，合在一起，就是亲戚："), en("relative"),
      zh("很多亲戚：", "plural:relative"), en("relatives"))
L.seg("focus:uncle,aunt,cousin", zh("中文要分叔叔、舅舅、姑姑、阿姨，英语简单多了："),
      en("uncle", "focus:uncle"), en("aunt", "focus:aunt"), en("cousin", "focus:cousin"))
L.seg("focus:none", zh("我们来介绍一下全家福吧！"))
L.seg("", en("This is my grandpa.", "focus:grandfather"), en("This is my grandma.", "focus:grandmother"),
      en("These are my uncle and aunt.", "focus:uncle,aunt"), en("And this is my cousin!", "focus:cousin"))
L.review([("grandfather", "grandfather, grandpa"), ("grandmother", "grandmother, grandma"), ("grandparents", "grandparents"),
          ("grandson", "grandson"), ("granddaughter", "granddaughter"), ("uncle", "uncle"), ("aunt", "aunt"),
          ("cousin", "cousin"), ("relative", "relative, relatives")],
         "太棒了！下次见到亲戚的时候，用英语和他们打个招呼吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
