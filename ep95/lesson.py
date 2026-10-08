import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep95", "environment", "环境", 95, "environment")
V = dict(kind="verb")
L.node("environment", "environment", "/ɪnˈvaɪrənmənt/", "环境")
L.node("protection", "protection", "/prəˈtekʃn/", "保护", alt="protect", altLabel="来自")
L.node("resolution", "resolution", "/ˌrezəˈluːʃn/", "决心")
L.node("pollution", "pollution", "/pəˈluːʃn/", "污染", alt="pollute", altLabel="来自")
L.node("coal", "coal", "/koʊl/", "煤")
L.node("destroy", "destroy", "/dɪˈstrɔɪ/", "破坏", **V)
L.node("control", "control", "/kənˈtroʊl/", "控制", **V)
L.node("litter", "litter", "/ˈlɪtər/", "乱扔垃圾", **V)
L.node("kill", "kill", "/kɪl/", "杀死", **V)
L.node("endangered", "endangered", "/ɪnˈdeɪndʒərd/", "濒危的", kind="adj", alt="danger", altLabel="来自")
L.node("remain", "remain", "/rɪˈmeɪn/", "剩下；保持", **V)
L.node("prediction", "prediction", "/prɪˈdɪkʃn/", "预测")
L.node("rise", "rise", "/raɪz/", "上升", **V)
L.node("increase", "increase", "/ɪnˈkriːs/", "增加", **V)
L.node("decrease", "decrease", "/dɪˈkriːs/", "减少", **V)
L.grid(["protection environment resolution",
        "coal pollution destroy",
        "control litter kill",
        "endangered remain prediction",
        "rise increase decrease"], dy=330)
for id, x, y in [("protection", 170, 150), ("environment", 520, 150), ("resolution", 170, 470), ("coal", 870, 150), ("pollution", 870, 470), ("destroy", 1220, 150),
                 ("control", 520, 470), ("litter", 520, 790), ("kill", 1220, 470), ("endangered", 1570, 470), ("remain", 1570, 150), ("prediction", 1570, 790),
                 ("rise", 870, 790), ("increase", 1220, 790), ("decrease", 170, 790)]:
    L.byid[id]["at"] = [x, y]
L.edge("protection", "environment"); L.edge("resolution", "environment", dashed=True); L.edge("pollution", "environment"); L.edge("coal", "pollution")
L.edge("pollution", "destroy"); L.edge("control", "pollution"); L.edge("litter", "pollution"); L.edge("pollution", "kill"); L.edge("kill", "endangered")
L.edge("remain", "endangered", dashed=True); L.edge("endangered", "prediction", dashed=True); L.edge("pollution", "rise", dashed=True); L.edge("rise", "increase", "差不多")

L.seg("title", zh("小朋友们好！地球是我们共同的家。今天，我们来学和环境有关的单词。"), en("environment"))
L.seg("map show:environment focus:environment", zh("我们周围的空气、水、山林，是环境："), en("environment"))
L.seg("show:protection edge:protection>environment focus:protection", zh("我们要保护环境。保护是 protect，加上 i o n："), en("protect"), en("protection"))
L.seg("show:resolution edge:resolution>environment focus:resolution", zh("下定决心保护地球："), en("resolution"))
L.seg("show:pollution edge:pollution>environment focus:pollution", zh("工厂排出的脏东西，造成了污染："), en("pollution"))
L.seg("show:coal edge:coal>pollution focus:coal", zh("烧煤会冒黑烟："), en("coal"))
L.seg("show:destroy edge:pollution>destroy focus:destroy", zh("污染会破坏环境："), en("destroy"))
L.seg("show:control edge:control>pollution focus:control", zh("我们要控制污染："), en("control"))
L.seg("show:litter edge:litter>pollution focus:litter", zh("不要乱扔垃圾："), en("litter"), en("Don't litter!"))
L.seg("show:kill edge:pollution>kill focus:kill", zh("污染会杀死很多动物和植物："), en("kill"))
L.seg("show:endangered edge:kill>endangered focus:endangered", zh("还记得 danger 吗？前面加 e n，后面加 e d，就是濒危的："), en("endangered"),
      en("Pandas are endangered animals."))
L.seg("show:remain edge:remain>endangered focus:remain", zh("剩下的熊猫不多了。剩下，英语是"), en("remain"))
L.seg("show:prediction edge:endangered>prediction focus:prediction", zh("科学家做出预测："), en("prediction"))
L.seg("show:rise edge:pollution>rise focus:rise", zh("地球的温度在上升："), en("rise"))
L.seg("show:increase edge:rise>increase focus:increase", zh("增加，英语是"), en("increase"))
L.seg("show:decrease focus:decrease", zh("把 i n 换成 d e，就是减少："), en("decrease"), en("We must decrease pollution."))
L.seg("focus:increase,decrease", zh("增加和减少："), en("increase", "focus:increase"), en("decrease", "focus:decrease"))
L.review([("environment", "environment"), ("protection", "protection"), ("resolution", "resolution"), ("pollution", "pollution"), ("coal", "coal"), ("destroy", "destroy"),
          ("control", "control"), ("litter", "litter"), ("kill", "kill"), ("endangered", "endangered"), ("remain", "remain"), ("prediction", "prediction"),
          ("rise", "rise"), ("increase", "increase"), ("decrease", "decrease")],
         "太棒了！不乱扔垃圾，节约用水，我们一起保护地球吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
