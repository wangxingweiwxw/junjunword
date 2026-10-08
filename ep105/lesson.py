import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep105", "technology", "科技", 105, "technology")
V = dict(kind="verb")
L.node("technology", "technology", "/tekˈnɑːlədʒi/", "科技；技术")
L.node("advance", "advance", "/ədˈvæns/", "进步；前进", **V)
L.node("retrogress", "retrogress", "/ˌretrəˈɡres/", "倒退", **V)
L.node("unnatural", "unnatural", "/ʌnˈnætʃrəl/", "不自然的", kind="adj")
L.node("failure", "failure", "/ˈfeɪljər/", "失败", alt="fail", altLabel="来自")
L.node("pioneer", "pioneer", "/ˌpaɪəˈnɪr/", "先驱；开拓者")
L.node("invent", "invent", "/ɪnˈvent/", "发明", **V)
L.node("invention", "invention", "/ɪnˈvenʃn/", "发明（名词）")
L.node("radio", "radio", "/ˈreɪdioʊ/", "收音机")
L.node("communicate", "communicate", "/kəˈmjuːnɪkeɪt/", "交流", **V)
L.node("communication", "communication", "/kəˌmjuːnɪˈkeɪʃn/", "通讯；交流")
L.grid(["advance unnatural retrogress",
        "pioneer technology .",
        "failure invent invention",
        ". radio communicate",
        ". . communication"], dy=330)
for id, x, y in [("advance", 170, 150), ("retrogress", 170, 470), ("pioneer", 170, 790), ("technology", 520, 470), ("unnatural", 520, 150), ("failure", 870, 150),
                 ("invent", 870, 470), ("invention", 870, 790), ("radio", 1220, 470), ("communicate", 1570, 470), ("communication", 1570, 790)]:
    L.byid[id]["at"] = [x, y]
L.edge("technology", "advance"); L.edge("technology", "retrogress", dashed=True); L.edge("technology", "unnatural", dashed=True); L.edge("technology", "pioneer")
L.edge("technology", "invent"); L.edge("invent", "invention", "+ion"); L.edge("invent", "failure", dashed=True); L.edge("invent", "radio"); L.edge("radio", "communicate")
L.edge("communicate", "communication", "e→ion")

L.seg("title", zh("小朋友们好！从收音机到手机，科技让生活越来越方便。今天，我们来学和科技有关的单词。"), en("technology"))
L.seg("map show:technology focus:technology", zh("科学技术，是科技："), en("technology"), zh("中间的 c h，读 k。"))
L.seg("show:advance edge:technology>advance focus:advance", zh("科技在不断进步、前进："), en("advance"))
L.seg("show:retrogress edge:technology>retrogress focus:retrogress", zh("进步的反面，是倒退。这是一个比较正式的词："), en("retrogress"))
L.seg("show:unnatural edge:technology>unnatural focus:unnatural", zh("还记得第九十一集的 natural 吗？加上 u n，就是不自然的："), en("unnatural"))
L.seg("show:pioneer edge:technology>pioneer focus:pioneer", zh("第一个走出新路的人，是先驱、开拓者："), en("pioneer"))
L.seg("show:invent edge:technology>invent focus:invent", zh("创造出以前没有的东西，是发明："), en("invent"))
L.seg("show:invention edge:invent>invention focus:invention", zh("发明出来的东西，加上 i o n："), en("invention"))
L.seg("show:failure edge:invent>failure focus:failure", zh("发明的路上，常常会失败。失败是 fail，加上 u r e："), en("fail"), en("failure"),
      en("Failure is the mother of success."))
L.seg("show:radio edge:invent>radio focus:radio", zh("很久以前，人们发明了收音机："), en("radio"))
L.seg("show:communicate edge:radio>communicate focus:communicate", zh("有了收音机，远方的人也能交流："), en("communicate"))
L.seg("show:communication edge:communicate>communication focus:communication", zh("交流这件事，把 e 换成 i o n，就是通讯："), en("communication"))
L.seg("focus:invention,communication", zh("两个 i o n 结尾的："), en("invent, invention", "focus:invent,invention"), en("communicate, communication", "focus:communicate,communication"))
L.review([("technology", "technology"), ("advance", "advance"), ("retrogress", "retrogress"), ("unnatural", "unnatural"), ("pioneer", "pioneer"), ("invent", "invent"),
          ("invention", "invention"), ("failure", "failure"), ("radio", "radio"), ("communicate", "communicate"), ("communication", "communication")],
         "太棒了！不怕失败，长大了你也可以做一个发明家哦。点一点图上的单词，还能再听一遍发音。")
L.save()
