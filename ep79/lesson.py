import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep79", "manners", "礼貌", 79, "apologize")
V = dict(kind="verb")
L.node("kick", "kick", "/kɪk/", "踢", **V)
L.node("knock", "knock", "/nɑːk/", "敲；撞", **V)
L.node("break", "break", "/breɪk/", "打破", **V, alt="broke", altLabel="过去式")
L.node("proper", "proper", "/ˈprɑːpər/", "正确的；恰当的", kind="adj")
L.node("avoid", "avoid", "/əˈvɔɪd/", "避开", **V)
L.node("hide", "hide", "/haɪd/", "躲藏", **V)
L.node("leave", "leave", "/liːv/", "离开", **V)
L.node("stay", "stay", "/steɪ/", "留下", **V)
L.node("apologize", "apologize", "/əˈpɑːlədʒaɪz/", "道歉", **V)
L.node("forgive", "forgive", "/fərˈɡɪv/", "原谅", **V)
L.node("replace", "replace", "/rɪˈpleɪs/", "赔；替换", **V)
L.grid(["kick knock break",
        "avoid proper stay",
        "hide . apologize",
        "leave replace forgive"], dy=350)
L.edge("kick", "knock"); L.edge("knock", "break"); L.edge("break", "proper", dashed=True); L.edge("proper", "avoid", "不要"); L.edge("proper", "stay", "应该")
L.edge("avoid", "hide", dashed=True); L.edge("hide", "leave", dashed=True); L.edge("stay", "apologize"); L.edge("apologize", "forgive"); L.edge("apologize", "replace", dashed=True)

L.seg("title", zh("小朋友们好！做错了事，怎么办才对呢？今天，我们来讲一个小故事。"), en("manners"))
L.seg("map show:kick focus:kick", zh("小明在院子里踢球："), en("kick"))
L.seg("show:knock edge:kick>knock focus:knock", zh("砰！球撞到了邻居家的窗户："), en("knock"), zh("开头的 k 不发音哦。它也是敲门的敲。"))
L.seg("show:break edge:knock>break focus:break", zh("哗啦，窗户被打破了："), en("break"), zh("已经打破了，要说", "alt:break"), en("broke"))
L.seg("show:proper edge:break>proper focus:proper", zh("这时候，怎么做才是正确的呢？正确的、恰当的，英语是"), en("proper"))
L.seg("show:avoid edge:proper>avoid focus:avoid", zh("不要避开邻居："), en("avoid"))
L.seg("show:hide edge:avoid>hide focus:hide", zh("也不要躲起来："), en("hide"))
L.seg("show:leave edge:hide>leave focus:leave", zh("更不能偷偷离开："), en("leave"))
L.seg("show:stay edge:proper>stay focus:stay", zh("应该勇敢地留下来："), en("stay"))
L.seg("show:apologize edge:stay>apologize focus:apologize", zh("向邻居道歉："), en("apologize"), en("I'm sorry."), en("I will stay and apologize.", "focus:stay,apologize"))
L.seg("show:replace edge:apologize>replace focus:replace", zh("还要帮邻居换一块新玻璃。替换、赔，英语是"), en("replace"))
L.seg("show:forgive edge:apologize>forgive focus:forgive", zh("邻居笑着说：没关系，我原谅你啦。原谅，英语是"), en("forgive"))
L.seg("focus:avoid,hide,leave", zh("这三件事不要做："), en("avoid", "focus:avoid"), en("hide", "focus:hide"), en("leave", "focus:leave"))
L.seg("focus:stay,apologize,replace", zh("这三件事要做："), en("stay", "focus:stay"), en("apologize", "focus:apologize"), en("replace", "focus:replace"))
L.review([("kick", "kick"), ("knock", "knock"), ("break", "break, broke"), ("proper", "proper"), ("avoid", "avoid"), ("hide", "hide"), ("leave", "leave"),
          ("stay", "stay"), ("apologize", "apologize"), ("replace", "replace"), ("forgive", "forgive")],
         "太棒了！做错了事，勇敢地说一声对不起吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
