import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep58", "feelings", "感受", 58, "happiness")
V, A = dict(kind="verb"), dict(kind="adj")
L.node("feelings", "feelings", "/ˈfiːlɪŋz/", "感受", icon="feeling")
L.node("enjoy", "enjoy", "/ɪnˈdʒɔɪ/", "享受", **V)
L.node("comfortable", "comfortable", "/ˈkʌmftəbl/", "舒服的", **A)
L.node("pleasant", "pleasant", "/ˈpleznt/", "令人愉快的", **A)
L.node("happiness", "happiness", "/ˈhæpinəs/", "幸福；快乐", alt="happy", altLabel="来自")
L.node("unhappiness", "unhappiness", "/ʌnˈhæpinəs/", "不快乐")
L.node("miss", "miss", "/mɪs/", "想念", **V)
L.node("separate", "separate", "/ˈsepəreɪt/", "分开", **V)
L.node("shame", "shame", "/ʃeɪm/", "羞愧；遗憾")
L.node("regret", "regret", "/rɪˈɡret/", "后悔", **V)
L.node("pity", "pity", "/ˈpɪti/", "同情；可惜")
L.node("hate", "hate", "/heɪt/", "讨厌；恨", **V)
L.grid(["enjoy pleasant comfortable",
        "happiness feelings miss",
        "unhappiness . separate",
        "shame regret pity",
        ". hate ."], dy=330)
L.edge("enjoy", "pleasant"); L.edge("comfortable", "pleasant"); L.edge("feelings", "pleasant"); L.edge("feelings", "happiness"); L.edge("happiness", "unhappiness", "un+")
L.edge("feelings", "miss"); L.edge("miss", "separate", "因为"); L.edge("feelings", "regret", dashed=True); L.edge("regret", "shame", dashed=True)
L.edge("regret", "pity", dashed=True); L.edge("regret", "hate", dashed=True)

L.seg("title", zh("小朋友们好！还记得第三十九集的情绪吗？今天，我们学更多表达感受的单词。"), en("feelings"))
L.seg("map show:feelings focus:feelings", zh("心里的各种感受："), en("feelings"))
L.seg("show:enjoy focus:enjoy", zh("开开心心地享受一件事："), en("enjoy"), en("I enjoy the sunshine at the beach."))
L.seg("show:comfortable focus:comfortable", zh("躺在软软的沙发上，真舒服："), en("comfortable"), zh("这个词很长，中间的 or 读得很轻："), en("com, fort, able"))
L.seg("show:pleasant edge:enjoy>pleasant edge:comfortable>pleasant edge:feelings>pleasant focus:pleasant", zh("让人心情愉快的，是"), en("pleasant"),
      en("a pleasant day"))
L.seg("show:happiness edge:feelings>happiness focus:happiness", zh("开心是 happy，把 y 变成 i，加上 n e s s，就是幸福、快乐：", "alt:happiness"),
      en("happy"), en("happiness"))
L.seg("show:unhappiness edge:happiness>unhappiness focus:unhappiness", zh("前面加上 u n，就是不快乐："), en("unhappiness"),
      zh("还记得第四十五集的 unusual 吗？un 让意思反过来。"))
L.seg("show:miss edge:feelings>miss focus:miss", zh("好久没见到奶奶了，好想她："), en("miss"), en("I miss my grandma."))
L.seg("show:separate edge:miss>separate focus:separate", zh("因为我们分开了，所以想念。分开，英语是"), en("separate"))
L.seg("show:regret edge:feelings>regret focus:regret", zh("做错了事，心里很后悔："), en("regret"))
L.seg("show:shame edge:regret>shame focus:shame", zh("羞愧，英语是"), en("shame"), zh("它也表示遗憾，比如："), en("What a shame!"))
L.seg("show:pity edge:regret>pity focus:pity", zh("看到小狗淋雨，心里很同情："), en("pity"), zh("也可以表示可惜："), en("What a pity!"))
L.seg("show:hate edge:regret>hate focus:hate", zh("非常非常讨厌，是"), en("hate"), en("I hate rainy days."))
L.seg("focus:shame,pity", zh("两句表示可惜的话："), en("What a shame!", "focus:shame"), en("What a pity!", "focus:pity"))
L.seg("focus:none", zh("说一说你现在的感受吧！"))
L.seg("", en("I enjoy my vacation.", "focus:enjoy"), en("The bed is comfortable.", "focus:comfortable"), en("I miss my friends.", "focus:miss"))
L.review([("feelings", "feelings"), ("enjoy", "enjoy"), ("comfortable", "comfortable"), ("pleasant", "pleasant"), ("happiness", "happiness"),
          ("unhappiness", "unhappiness"), ("miss", "miss"), ("separate", "separate"), ("regret", "regret"), ("shame", "shame"), ("pity", "pity"), ("hate", "hate")],
         "太棒了！每天睡觉前，用英语说一说今天的感受吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
