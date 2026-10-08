import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep100", "government", "政府", 100, "government")
V = dict(kind="verb")
L.node("government", "government", "/ˈɡʌvərnmənt/", "政府", alt="govern", altLabel="来自")
L.node("agency", "agency", "/ˈeɪdʒənsi/", "机构；中介")
L.node("leader", "leader", "/ˈliːdər/", "领导者", alt="lead", altLabel="来自")
L.node("chairman", "chairman", "/ˈtʃermən/", "主席")
L.node("minister", "minister", "/ˈmɪnɪstər/", "部长")
L.node("consider", "consider", "/kənˈsɪdər/", "仔细考虑", **V)
L.node("decide", "decide", "/dɪˈsaɪd/", "决定", **V)
L.node("decision", "decision", "/dɪˈsɪʒn/", "决定（名词）")
L.node("development", "development", "/dɪˈveləpmənt/", "发展", alt="develop", altLabel="来自")
L.node("progress", "progress", "/ˈprɑːɡres/", "进步")
L.node("role", "role", "/roʊl/", "角色；作用")
L.grid(["agency leader chairman",
        "consider government minister",
        "decide . role",
        "decision development progress"], dy=350)
L.edge("government", "agency"); L.edge("government", "leader"); L.edge("government", "chairman"); L.edge("government", "minister"); L.edge("government", "consider")
L.edge("consider", "decide"); L.edge("decide", "decision"); L.edge("government", "development"); L.edge("development", "progress", dashed=True); L.edge("government", "role")

L.seg("title", zh("小朋友们好！一个国家，是谁在管理呢？今天，我们来学和政府有关的单词。"), en("government"))
L.seg("map show:government focus:government", zh("管理国家的，是政府。管理是 govern，加上 m e n t："), en("govern"), en("government"))
L.seg("show:agency edge:government>agency focus:agency", zh("政府下面有很多机构："), en("agency"), zh("它也有中介的意思，比如旅行社："), en("travel agency"))
L.seg("show:leader edge:government>leader focus:leader", zh("带领大家的人，是领导者。带领是 lead，加上 e r："), en("lead"), en("leader"))
L.seg("show:chairman edge:government>chairman focus:chairman", zh("开会时坐在主位的人，是主席。椅子，加上男人："), en("chair"), en("man"), en("chairman"))
L.seg("show:minister edge:government>minister focus:minister", zh("管理一个部门的官员，是部长："), en("minister"))
L.seg("show:consider edge:government>consider focus:consider", zh("做事之前，要仔细考虑："), en("consider"))
L.seg("show:decide edge:consider>decide focus:decide", zh("考虑好了，就做出决定："), en("decide"))
L.seg("show:decision edge:decide>decision focus:decision", zh("决定这件事，把 d e 换成 s i o n："), en("decision"), en("a good decision"))
L.seg("show:development edge:government>development focus:development", zh("国家一天天发展。发展是 develop，加上 m e n t："), en("develop"), en("development"))
L.seg("show:progress edge:development>progress focus:progress", zh("一步一步向前，是进步："), en("progress"), en("Our country makes great progress."))
L.seg("show:role edge:government>role focus:role", zh("每个人都有自己的角色和作用："), en("role"), en("Everyone plays a role."))
L.seg("focus:government,development", zh("今天有两个 m e n t 结尾的词："), en("govern, government", "focus:government"), en("develop, development", "focus:development"))
L.review([("government", "government"), ("agency", "agency"), ("leader", "leader"), ("chairman", "chairman"), ("minister", "minister"), ("consider", "consider"),
          ("decide", "decide"), ("decision", "decision"), ("development", "development"), ("progress", "progress"), ("role", "role")],
         "太棒了！在班级里，你也可以当一个好的小领导者哦。点一点图上的单词，还能再听一遍发音。")
L.save()
