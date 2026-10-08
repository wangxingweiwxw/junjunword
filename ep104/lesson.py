import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep104", "phone", "手机", 104, "phone")
V = dict(kind="verb")
L.node("phone", "phone", "/foʊn/", "电话；手机", alt="telephone", altLabel="全称")
L.node("electronic", "electronic", "/ɪˌlekˈtrɑːnɪk/", "电子的", kind="adj")
L.node("screen", "screen", "/skriːn/", "屏幕")
L.node("request", "request", "/rɪˈkwest/", "请求")
L.node("accept", "accept", "/əkˈsept/", "接受", **V)
L.node("refuse", "refuse", "/rɪˈfjuːz/", "拒绝", **V)
L.node("message", "message", "/ˈmesɪdʒ/", "信息；消息")
L.node("receive", "receive", "/rɪˈsiːv/", "收到", **V)
L.node("reply", "reply", "/rɪˈplaɪ/", "回复", **V)
L.node("delete", "delete", "/dɪˈliːt/", "删除", **V)
L.node("save", "save", "/seɪv/", "保存", **V)
L.node("video", "video", "/ˈvɪdioʊ/", "视频")
L.node("picture", "picture", "/ˈpɪktʃər/", "图片；照片")
L.grid(["accept electronic screen",
        "request phone message",
        "refuse save receive",
        "delete video reply",
        ". picture ."], dy=330)
for id, x, y in [("accept", 170, 150), ("electronic", 870, 150), ("screen", 1220, 150), ("receive", 1570, 150),
                 ("refuse", 170, 470), ("request", 520, 470), ("phone", 870, 470), ("message", 1220, 470), ("reply", 1570, 470),
                 ("delete", 170, 790), ("save", 520, 790), ("video", 870, 790), ("picture", 1220, 790)]:
    L.byid[id]["at"] = [x, y]
L.edge("electronic", "phone"); L.edge("phone", "screen"); L.edge("phone", "request"); L.edge("request", "accept"); L.edge("request", "refuse")
L.edge("phone", "message"); L.edge("message", "receive"); L.edge("receive", "reply"); L.edge("phone", "save"); L.edge("save", "delete", dashed=True); L.edge("save", "video")
L.edge("video", "picture", dashed=True)

L.seg("title", zh("小朋友们好！手机能打电话、发消息、拍照片。今天，我们来学和手机有关的单词。"), en("phone"))
L.seg("map show:phone focus:phone", zh("电话、手机，英语是"), en("phone"), zh("它的全称是", "alt:phone"), en("telephone"))
L.seg("show:electronic edge:electronic>phone focus:electronic", zh("手机是电子产品。电子的，英语是"), en("electronic"))
L.seg("show:screen edge:phone>screen focus:screen", zh("手机亮亮的屏幕："), en("screen"))
L.seg("show:request edge:phone>request focus:request", zh("好友发来一个请求："), en("request"))
L.seg("show:accept edge:request>accept focus:accept", zh("同意了，就是接受："), en("accept"))
L.seg("show:refuse edge:request>refuse focus:refuse", zh("不同意，就是拒绝："), en("refuse"), zh("陌生人的请求，要学会拒绝哦。"))
L.seg("show:message edge:phone>message focus:message", zh("手机上的消息："), en("message"))
L.seg("show:receive edge:message>receive focus:receive", zh("收到一条消息："), en("receive"), zh("小提示：e i 读长长的 ee。"))
L.seg("show:reply edge:receive>reply focus:reply", zh("收到了，要回复："), en("reply"), en("Please reply soon."))
L.seg("show:save edge:phone>save focus:save", zh("重要的东西，保存好："), en("save"))
L.seg("show:delete edge:save>delete focus:delete", zh("不要的东西，删除掉："), en("delete"))
L.seg("show:video edge:save>video focus:video", zh("用手机拍的视频，也能保存下来："), en("video"))
L.seg("show:picture edge:video>picture focus:picture", zh("还有拍的照片："), en("picture"), zh("还记得第二十九集的 photo 吗？"))
L.seg("focus:accept,refuse", zh("接受和拒绝："), en("accept", "focus:accept"), en("refuse", "focus:refuse"))
L.seg("focus:delete,save", zh("保存和删除："), en("save", "focus:save"), en("delete", "focus:delete"))
L.review([("phone", "phone, telephone"), ("electronic", "electronic"), ("screen", "screen"), ("request", "request"), ("accept", "accept"), ("refuse", "refuse"),
          ("message", "message"), ("receive", "receive"), ("reply", "reply"), ("save", "save"), ("delete", "delete"), ("video", "video"), ("picture", "picture")],
         "太棒了！玩手机要有时间限制，保护好眼睛哦。点一点图上的单词，还能再听一遍发音。")
L.save()
