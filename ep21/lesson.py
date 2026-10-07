import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep21", "meals", "一日三餐", 21, "lunch")
L.node("breakfast", "breakfast", "/ˈbrekfəst/", "早餐")
L.node("porridge", "porridge", "/ˈpɔːrɪdʒ/", "粥")
L.node("pancake", "pancake", "/ˈpænkeɪk/", "薄煎饼")
L.node("butter", "butter", "/ˈbʌtər/", "黄油")
L.node("prefer", "prefer", "/prɪˈfɜːr/", "更喜欢", kind="verb")
L.node("lunch", "lunch", "/lʌntʃ/", "午餐")
L.node("sandwich", "sandwich", "/ˈsænwɪtʃ/", "三明治")
L.node("bread", "bread", "/bred/", "面包")
L.node("salad", "salad", "/ˈsæləd/", "沙拉")
L.node("noodles", "noodles", "/ˈnuːdlz/", "面条")
L.node("dinner", "dinner", "/ˈdɪnər/", "晚餐")
L.node("hamburger", "hamburger", "/ˈhæmbɜːrɡər/", "汉堡包")
L.node("sausage", "sausage", "/ˈsɔːsɪdʒ/", "香肠")
L.node("spaghetti", "spaghetti", "/spəˈɡeti/", "意大利面")
L.grid(["porridge breakfast pancake",
        "prefer . butter",
        "salad lunch sandwich",
        "noodles . bread",
        "hamburger dinner spaghetti",
        ". sausage ."], dy=330)
L.edge("breakfast", "porridge"); L.edge("breakfast", "pancake"); L.edge("butter", "pancake", "抹上"); L.edge("prefer", "porridge", dashed=True)
L.edge("lunch", "salad"); L.edge("lunch", "sandwich"); L.edge("lunch", "noodles"); L.edge("sandwich", "bread", "用…做")
L.edge("dinner", "hamburger"); L.edge("dinner", "spaghetti"); L.edge("dinner", "sausage")

L.seg("title", zh("小朋友们好！还记得第十八集吗？一天要吃三顿饭。今天，我们来看看每顿饭都吃些什么。"), en("three meals a day"))
L.seg("map show:breakfast focus:breakfast", zh("早上起床吃的第一顿饭，是早餐："), en("breakfast"),
      zh("它是两个词拼起来的：打破，加上禁食。睡了一整夜，饿了很久，现在终于可以吃东西啦！"), en("break"), en("fast"), en("breakfast"))
L.seg("show:porridge edge:breakfast>porridge focus:porridge", zh("早餐可以喝一碗热乎乎的粥："), en("porridge"))
L.seg("show:pancake edge:breakfast>pancake focus:pancake", zh("也可以吃一叠软软的薄煎饼。平底锅，加上蛋糕："), en("pan"), en("cake"), en("pancake"))
L.seg("show:butter edge:butter>pancake focus:butter", zh("煎饼上抹一块黄油，香喷喷的："), en("butter"))
L.seg("show:prefer edge:prefer>porridge focus:prefer", zh("粥和煎饼，你更喜欢哪一个？更喜欢，英语是"), en("prefer"),
      en("I prefer porridge for breakfast.", "focus:prefer,porridge"))
L.seg("show:lunch focus:lunch", zh("中午吃的饭，是午餐："), en("lunch"), en("Lunch time!"))
L.seg("show:sandwich edge:lunch>sandwich focus:sandwich", zh("午餐带一个三明治："), en("sandwich"),
      zh("中间的字母 d，读的时候几乎听不到。"))
L.seg("show:bread edge:sandwich>bread focus:bread", zh("三明治是用面包做的："), en("bread"),
      zh("面包通常不加 s。一片面包，要说"), en("a slice of bread"))
L.seg("show:salad edge:lunch>salad focus:salad", zh("再配一碗新鲜的蔬菜沙拉："), en("salad"), en("I eat salad at noon."))
L.seg("show:noodles edge:lunch>noodles focus:noodles", zh("中国小朋友午餐还爱吃面条。面条长长的、很多根，所以总是带着 s："), en("noodles"))
L.seg("show:dinner focus:dinner", zh("傍晚，一家人坐在一起，吃晚餐："), en("dinner"), en("Dinner is ready!"))
L.seg("show:hamburger edge:dinner>hamburger focus:hamburger", zh("晚餐吃一个大大的汉堡包："), en("hamburger"))
L.seg("show:spaghetti edge:dinner>spaghetti focus:spaghetti", zh("或者一盘意大利面："), en("spaghetti"),
      zh("它是从意大利来的词，g 后面跟着一个不发音的 h。"))
L.seg("show:sausage edge:dinner>sausage focus:sausage", zh("再来一根烤香肠："), en("sausage"))
L.seg("focus:breakfast,lunch,dinner", zh("一天三顿饭，按顺序读一遍："),
      en("breakfast in the morning", "focus:breakfast"), en("lunch at noon", "focus:lunch"), en("dinner in the evening", "focus:dinner"))
L.seg("focus:none", zh("你最喜欢吃什么呢？像这样说一说吧："))
L.seg("", en("For breakfast, I have porridge.", "focus:breakfast,porridge"), en("For lunch, I have noodles.", "focus:lunch,noodles"),
      en("For dinner, I prefer spaghetti!", "focus:dinner,spaghetti,prefer"))
L.review([("breakfast", "breakfast"), ("porridge", "porridge"), ("pancake", "pancake"), ("butter", "butter"), ("prefer", "prefer"),
          ("lunch", "lunch"), ("sandwich", "sandwich"), ("bread", "bread"), ("salad", "salad"), ("noodles", "noodles"),
          ("dinner", "dinner"), ("hamburger", "hamburger"), ("spaghetti", "spaghetti"), ("sausage", "sausage")],
         "太棒了！明天吃早餐的时候，用英语说一说你在吃什么吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
