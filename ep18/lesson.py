import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep18", "food", "食物", 18, "food")
A = dict(kind="adj")
L.node("hungry", "hungry", "/ˈhʌŋɡri/", "饿的", **A)
L.node("eat", "eat", "/iːt/", "吃", kind="verb")
L.node("full", "full", "/fʊl/", "饱的", **A)
L.node("food", "food", "/fuːd/", "食物")
L.node("meal", "meal", "/miːl/", "一顿饭", plural="meals", pluralIpa="/miːlz/")
L.node("rice", "rice", "/raɪs/", "米饭")
L.node("meat", "meat", "/miːt/", "肉")
L.node("chicken", "chicken", "/ˈtʃɪkɪn/", "鸡肉；鸡")
L.node("pork", "pork", "/pɔːrk/", "猪肉", alt="pig", altLabel="来自")
L.node("beef", "beef", "/biːf/", "牛肉", alt="cow", altLabel="来自")
L.node("mutton", "mutton", "/ˈmʌtn/", "羊肉", alt="sheep", altLabel="来自")
L.node("oil", "oil", "/ɔɪl/", "油")
L.node("spicy", "spicy", "/ˈspaɪsi/", "辣的", **A)
L.grid(["hungry eat full",
        "rice food meal",
        "chicken meat oil",
        "pork beef mutton",
        ". spicy ."])
L.edge("hungry", "eat", "饿了就"); L.edge("eat", "full", "吃饱"); L.edge("eat", "food"); L.edge("eat", "meal")
L.edge("food", "rice"); L.edge("food", "meat"); L.edge("meat", "chicken"); L.edge("oil", "meat", "炒", dashed=True)
L.edge("meat", "pork"); L.edge("meat", "beef"); L.edge("meat", "mutton"); L.edge("spicy", "beef", dashed=True)

L.seg("title", zh("小朋友们好！肚子咕咕叫了吗？今天，我们来学好吃的。"), en("food"), zh("食物。"))
L.seg("map show:hungry focus:hungry", zh("到了中午，肚子咕咕叫，那是饿了："), en("hungry"), en("I'm hungry!"))
L.seg("show:eat edge:hungry>eat focus:eat", zh("饿了，就要吃东西："), en("eat"), en("Let's eat!"))
L.seg("show:food edge:eat>food focus:food", zh("能吃的东西，统统叫食物："), en("food"), zh("小提示：中间是两个字母 o。"), en("I like Chinese food."))
L.seg("show:meal edge:eat>meal focus:meal", zh("早饭、午饭、晚饭，每一顿饭，叫"), en("meal"),
      zh("一天要吃三顿饭：", "plural:meal"), en("three meals a day"))
L.seg("show:rice edge:food>rice focus:rice", zh("中国小朋友天天都吃的主食，是米饭："), en("rice"), en("a bowl of rice"))
L.seg("show:meat edge:food>meat focus:meat", zh("很多小朋友最爱吃肉："), en("meat"))
L.seg("show:chicken edge:meat>chicken focus:chicken", zh("鸡肉，英语是"), en("chicken"), zh("鸡和鸡肉，是同一个词。"), en("I love chicken."))
L.seg("show:pork edge:meat>pork focus:pork", zh("猪肉可就不一样了。猪是", "alt:pork"), en("pig"), zh("猪肉，却叫"), en("pork"))
L.seg("show:beef edge:meat>beef focus:beef", zh("牛是", "alt:beef"), en("cow"), zh("牛肉，叫"), en("beef"))
L.seg("show:mutton edge:meat>mutton focus:mutton", zh("羊是", "alt:mutton"), en("sheep"), zh("羊肉，叫"), en("mutton"))
L.seg("focus:pork,beef,mutton", zh("动物和它的肉，名字不一样，要分开记哦："),
      en("pig, pork", "focus:pork"), en("cow, beef", "focus:beef"), en("sheep, mutton", "focus:mutton"))
L.seg("show:oil edge:oil>meat focus:oil", zh("做菜的时候，锅里要先倒上一点油："), en("oil"))
L.seg("show:spicy edge:spicy>beef focus:spicy", zh("放上红红的辣椒，菜就变得辣辣的："), en("spicy"), en("This beef is spicy!"))
L.seg("show:full edge:eat>full focus:full", zh("吃了这么多，肚子圆滚滚的，吃饱啦："), en("full"), en("I'm full."))
L.seg("focus:hungry,full", zh("饿了，是"), en("hungry", "focus:hungry"), zh("饱了，是", "focus:full"), en("full"))
L.seg("focus:none", zh("我们来演一演，去饭店点菜吧！"))
L.seg("", en("I'm hungry.", "focus:hungry"), en("I want rice and chicken.", "focus:rice,chicken"),
      en("Not too spicy, please.", "focus:spicy"), en("Yummy! I'm full.", "focus:full"))
L.review([("hungry", "hungry"), ("eat", "eat"), ("full", "full"), ("food", "food"), ("meal", "meal, meals"), ("rice", "rice"),
          ("meat", "meat"), ("chicken", "chicken"), ("pork", "pork"), ("beef", "beef"), ("mutton", "mutton"),
          ("oil", "oil"), ("spicy", "spicy")],
         "太棒了！吃饭的时候，用英语说一说碗里有什么吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
