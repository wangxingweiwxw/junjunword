import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep45", "animals", "动物", 45, "animal")
A = dict(kind="adj")
L.node("animal", "animal", "/ˈænɪml/", "动物", plural="animals", pluralIpa="/ˈænɪmlz/")
L.node("wild", "wild", "/waɪld/", "野生的", **A)
L.node("pet", "pet", "/pet/", "宠物")
L.node("care", "care", "/ker/", "照顾；关心", kind="verb", alt="take care of", altLabel="常说")
L.node("usual", "usual", "/ˈjuːʒuəl/", "平常的", **A)
L.node("unusual", "unusual", "/ʌnˈjuːʒuəl/", "不寻常的", **A)
L.node("dog", "dog", "/dɔːɡ/", "狗")
L.node("cat", "cat", "/kæt/", "猫")
L.node("mouse", "mouse", "/maʊs/", "老鼠", plural="mice", pluralIpa="/maɪs/")
L.node("snake", "snake", "/sneɪk/", "蛇")
L.node("bird", "bird", "/bɜːrd/", "鸟")
L.node("wing", "wing", "/wɪŋ/", "翅膀", plural="wings", pluralIpa="/wɪŋz/")
L.node("fly", "fly", "/flaɪ/", "飞", kind="verb")
L.node("tail", "tail", "/teɪl/", "尾巴")
L.grid(["wild animal pet",
        ". care dog",
        "usual unusual cat",
        "snake mouse bird",
        "tail wing fly"], dy=330)
L.edge("wild", "animal"); L.edge("animal", "pet"); L.edge("pet", "care", "要"); L.edge("pet", "dog"); L.edge("dog", "cat")
L.edge("usual", "unusual", "un+"); L.edge("unusual", "snake", dashed=True); L.edge("unusual", "mouse", dashed=True); L.edge("cat", "bird")
L.edge("bird", "wing"); L.edge("wing", "fly"); L.edge("wing", "tail", dashed=True)

L.seg("title", zh("小朋友们好！你喜欢小动物吗？今天，我们来学动物和宠物。"), en("animals"))
L.seg("map show:animal focus:animal", zh("会跑、会跳、会飞的生物，都是动物："), en("animal"), zh("很多动物：", "plural:animal"), en("animals"))
L.seg("show:wild edge:wild>animal focus:wild", zh("住在森林、草原里，没人养的，是野生的："), en("wild"), en("wild animals"))
L.seg("show:pet edge:animal>pet focus:pet", zh("养在家里的，是宠物："), en("pet"), en("Do you have a pet?"))
L.seg("show:care edge:pet>care focus:care", zh("养宠物，要好好照顾它："), en("care"), zh("常常这样说：", "alt:care"), en("take care of my pet"))
L.seg("show:dog edge:pet>dog focus:dog", zh("最常见的宠物，是狗："), en("dog"))
L.seg("show:cat edge:dog>cat focus:cat", zh("还有猫："), en("cat"), en("Cats and dogs are pets."))
L.seg("show:usual focus:usual", zh("猫和狗当宠物，是很平常的事。平常的，英语是"), en("usual"))
L.seg("show:unusual edge:usual>unusual focus:unusual", zh("前面加上 u n，意思就反过来了，不寻常的："), en("unusual"),
      en("usual", "focus:usual"), en("unusual", "focus:unusual"))
L.seg("show:snake edge:unusual>snake focus:snake", zh("有人养蛇当宠物，那可真不寻常："), en("snake"))
L.seg("show:mouse edge:unusual>mouse focus:mouse", zh("还有人养小老鼠："), en("mouse"),
      zh("很多只老鼠，不加 s，而是变成", "plural:mouse"), en("mice"))
L.seg("show:bird edge:cat>bird focus:bird", zh("叽叽喳喳的鸟，也可以当宠物："), en("bird"))
L.seg("show:wing edge:bird>wing focus:wing", zh("鸟有一对翅膀："), en("wing"), zh("两只翅膀：", "plural:wing"), en("wings"))
L.seg("show:fly edge:wing>fly focus:fly", zh("扇动翅膀，就能飞："), en("fly"), en("My pet bird can fly."))
L.seg("show:tail edge:wing>tail focus:tail", zh("鸟、猫、狗，都有尾巴："), en("tail"))
L.seg("focus:mouse", zh("今天又学了一个特别的复数，像第八集的脚 feet 一样，要单独记："), en("one mouse, two mice."))
L.seg("focus:none", zh("介绍一下你的宠物吧！"))
L.seg("", en("I have a pet dog.", "focus:pet,dog"), en("It has a long tail.", "focus:tail"), en("I take care of it every day.", "focus:care"))
L.review([("animal", "animal, animals"), ("wild", "wild"), ("pet", "pet"), ("care", "care"), ("dog", "dog"), ("cat", "cat"),
          ("usual", "usual"), ("unusual", "unusual"), ("snake", "snake"), ("mouse", "mouse, mice"), ("bird", "bird"), ("wing", "wing, wings"),
          ("fly", "fly"), ("tail", "tail")],
         "太棒了！你最想养什么宠物？用英语告诉爸爸妈妈吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
