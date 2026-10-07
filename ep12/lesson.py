import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep12", "party", "生日派对", 12, "celebrate")
V = dict(kind="verb")
L.node("invite", "invite", "/ɪnˈvaɪt/", "邀请", **V)
L.node("invitation", "invitation", "/ˌɪnvɪˈteɪʃn/", "请帖；邀请")
L.node("guest", "guest", "/ɡest/", "客人", plural="guests", pluralIpa="/ɡests/")
L.node("please", "please", "/pliːz/", "请", kind="adv")
L.node("celebrate", "celebrate", "/ˈselɪbreɪt/", "庆祝", **V)
L.node("among", "among", "/əˈmʌŋ/", "在…之中", kind="prep")
L.node("without", "without", "/wɪˈðaʊt/", "没有", kind="prep")
L.node("age", "age", "/eɪdʒ/", "年龄")
L.node("forget", "forget", "/fərˈɡet/", "忘记", **V)
L.node("remember", "remember", "/rɪˈmembər/", "记得；记住", **V)
L.node("remind", "remind", "/rɪˈmaɪnd/", "提醒", **V)
L.node("excuse", "excuse", "/ɪkˈskjuːz/", "原谅；打扰", alt="Excuse me.", altLabel="常说", **V)
L.grid(["please invite invitation",
        "without guest celebrate",
        "forget among age",
        "remember remind excuse"], dy=350)
L.edge("please", "invite", "礼貌地", dashed=True); L.edge("invite", "invitation", "+ation"); L.edge("invite", "guest")
L.edge("without", "guest", dashed=True); L.edge("guest", "among"); L.edge("celebrate", "among")
L.edge("celebrate", "age", "又长一岁"); L.edge("forget", "remember", "反义"); L.edge("remember", "remind")

L.seg("title", zh("小朋友们好！还记得第四集的生日聚会吗？今天，我们来办一场更热闹的生日派对！"), en("a birthday party"))
L.seg("map show:invite focus:invite", zh("想让好朋友来参加派对，就要邀请他们："), en("invite"), en("I invite my friends."))
L.seg("show:invitation edge:invite>invitation focus:invitation", zh("写在卡片上的邀请，叫请帖。邀请这个词的后面，加上 a t i o n："),
      en("invitation"), en("a birthday invitation"))
L.seg("show:guest edge:invite>guest focus:guest", zh("被请来的朋友，就是客人："), en("guest"),
      zh("来了很多客人：", "plural:guest"), en("guests"))
L.seg("show:please edge:please>invite focus:please", zh("邀请别人的时候要有礼貌，记得说请："), en("please"), en("Please come to my party!"))
L.seg("show:celebrate focus:celebrate", zh("大家聚在一起，开开心心地庆祝："), en("celebrate"), en("Let's celebrate!"))
L.seg("show:among edge:guest>among edge:celebrate>among focus:among", zh("我站在客人们的中间，和大家一起庆祝。在……之中，英语是"),
      en("among"), en("I sing among my friends."))
L.seg("show:without edge:without>guest focus:without", zh("要是一个客人都没有，派对就冷清了。没有，英语是"), en("without"),
      zh("它是由两个小词拼起来的："), en("with"), en("out"), en("without"), en("a party without guests"))
L.seg("show:age edge:celebrate>age focus:age", zh("过一次生日，我们就又长大了一岁。年龄，英语是"), en("age"),
      zh("问别人几岁了，常常这样说："), en("How old are you?"))
L.seg("show:forget focus:forget", zh("哎呀，出门的时候，忘了带礼物！忘记，英语是"), en("forget"), en("Don't forget!"))
L.seg("show:remember edge:forget>remember focus:remember", zh("忘记的反面，是记得、记住："), en("remember"), en("I remember your birthday."))
L.seg("show:remind edge:remember>remind focus:remind", zh("帮别人记住一件事，就是提醒："), en("remind"),
      zh("它和记得一样，也是 r e 开头的哦。"), en("Please remind me."))
L.seg("show:excuse focus:excuse", zh("想请别人让一让，或者要打扰别人的时候，我们会礼貌地说：", "alt:excuse"), en("Excuse me."),
      zh("打扰、原谅，英语是"), en("excuse"))
L.seg("focus:please,excuse", zh("请和打扰了，都是有礼貌的好孩子常常说的话："), en("Please.", "focus:please"), en("Excuse me.", "focus:excuse"))
L.seg("focus:forget,remember,remind", zh("再来比一比这三个和记忆有关的词："),
      en("forget", "focus:forget"), en("remember", "focus:remember"), en("remind", "focus:remind"))
L.review([("invite", "invite"), ("invitation", "invitation"), ("guest", "guest, guests"), ("please", "please"),
          ("celebrate", "celebrate"), ("among", "among"), ("without", "without"), ("age", "age"), ("forget", "forget"),
          ("remember", "remember"), ("remind", "remind"), ("excuse", "excuse, Excuse me.")],
         "太棒了！下次过生日，用英语给好朋友写一张请帖吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
