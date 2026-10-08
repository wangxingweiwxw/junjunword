import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep94", "money", "钱", 94, "money")
V = dict(kind="verb")
L.node("money", "money", "/ˈmʌni/", "钱")
L.node("coin", "coin", "/kɔɪn/", "硬币")
L.node("cent", "cent", "/sent/", "分")
L.node("note", "note", "/noʊt/", "纸币")
L.node("pound", "pound", "/paʊnd/", "英镑")
L.node("dollar", "dollar", "/ˈdɑːlər/", "美元")
L.node("change", "change", "/tʃeɪndʒ/", "零钱；找零")
L.node("bill", "bill", "/bɪl/", "账单")
L.node("check", "check", "/tʃek/", "支票", alt="cheque", altLabel="英式")
L.node("price", "price", "/praɪs/", "价格")
L.node("cost", "cost", "/kɔːst/", "花费", **V)
L.node("pay", "pay", "/peɪ/", "付钱", **V, alt="paid", altLabel="过去式")
L.node("spend", "spend", "/spend/", "花（钱）", **V, alt="spent", altLabel="过去式")
L.grid(["price cost pay",
        "coin money note",
        "cent change spend",
        "bill check .",
        "pound dollar ."], dy=330)
for id, x, y in [("price", 170, 150), ("cost", 520, 150), ("pay", 870, 150), ("spend", 1220, 150), ("cent", 170, 470), ("coin", 520, 470), ("money", 870, 470),
                 ("note", 1220, 470), ("pound", 1570, 300), ("dollar", 1570, 640), ("change", 520, 790), ("bill", 870, 790), ("check", 1220, 790)]:
    L.byid[id]["at"] = [x, y]
L.edge("money", "coin"); L.edge("coin", "cent"); L.edge("money", "note"); L.edge("note", "pound"); L.edge("note", "dollar"); L.edge("money", "change"); L.edge("money", "bill")
L.edge("money", "check"); L.edge("price", "cost", dashed=True); L.edge("pay", "spend", dashed=True)

L.seg("title", zh("小朋友们好！还记得第四十八集的购物吗？今天，我们来学和钱有关的单词。"), en("money"))
L.seg("map show:money focus:money", zh("钱，英语是"), en("money"), zh("钱不能数，不加 s 哦。"))
L.seg("show:coin edge:money>coin focus:coin", zh("圆圆的硬币："), en("coin"))
L.seg("show:cent edge:coin>cent focus:cent", zh("一美元有一百美分。美分，是"), en("cent"), zh("还记得第八十一集的 century 吗？一百年。"))
L.seg("show:note edge:money>note focus:note", zh("纸做的钱，是纸币："), en("note"))
L.seg("show:pound edge:note>pound focus:pound", zh("英国用的钱，是英镑："), en("pound"))
L.seg("show:dollar edge:note>dollar focus:dollar", zh("美国用的钱，是美元："), en("dollar"))
L.seg("show:change edge:money>change focus:change", zh("买东西后找回的零钱："), en("change"), en("Here is your change."))
L.seg("show:bill edge:money>bill focus:bill", zh("在餐厅吃完饭，服务员拿来账单："), en("bill"), en("Can I have the bill, please?"))
L.seg("show:check edge:money>check focus:check", zh("写上金额就能付钱的，是支票："), en("check"), zh("英国写成", "alt:check"), en("cheque"))
L.seg("show:price focus:price", zh("东西卖多少钱，是价格："), en("price"))
L.seg("show:cost edge:price>cost focus:cost", zh("东西要花多少钱，用"), en("cost"), en("This toy costs twenty yuan."))
L.seg("show:pay edge:money>pay focus:pay", zh("付钱，是"), en("pay"), zh("已经付了，要说", "alt:pay"), en("paid"))
L.seg("show:spend edge:pay>spend focus:spend", zh("把钱花出去，是"), en("spend"), zh("已经花了，要说", "alt:spend"), en("spent"))
L.seg("focus:none", zh("来演一演买东西吧！"))
L.seg("", en("How much does it cost?", "focus:cost"), en("I will pay with coins.", "focus:pay,coin"), en("Here is your change!", "focus:change"))
L.review([("money", "money"), ("coin", "coin"), ("cent", "cent"), ("note", "note"), ("pound", "pound"), ("dollar", "dollar"), ("change", "change"), ("bill", "bill"),
          ("check", "check, cheque"), ("price", "price"), ("cost", "cost"), ("pay", "pay, paid"), ("spend", "spend, spent")],
         "太棒了！花钱要有计划，记得把零花钱存起来哦。点一点图上的单词，还能再听一遍发音。")
L.save()
