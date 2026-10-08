import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep101", "news", "新闻", 101, "news")
L.node("news", "news", "/nuːz/", "新闻")
L.node("information", "information", "/ˌɪnfərˈmeɪʃn/", "信息")
L.node("interesting", "interesting", "/ˈɪntrəstɪŋ/", "有趣的", kind="adj")
L.node("happen", "happen", "/ˈhæpən/", "发生", kind="verb")
L.node("event", "event", "/ɪˈvent/", "事件；大事")
L.node("earthquake", "earthquake", "/ˈɜːrθkweɪk/", "地震", alt="quake", altLabel="简称")
L.node("reporter", "reporter", "/rɪˈpɔːrtər/", "记者")
L.node("report", "report", "/rɪˈpɔːrt/", "报道")
L.node("exposure", "exposure", "/ɪkˈspoʊʒər/", "曝光；暴露")
L.node("recorder", "recorder", "/rɪˈkɔːrdər/", "录音机", alt="record", altLabel="来自")
L.grid(["interesting information earthquake",
        "happen news reporter",
        "event exposure report",
        ". recorder ."], dy=350)
L.edge("news", "information"); L.edge("information", "interesting", dashed=True); L.edge("news", "happen"); L.edge("happen", "event", dashed=True); L.edge("news", "earthquake", dashed=True)
L.edge("news", "reporter"); L.edge("reporter", "report"); L.edge("news", "exposure"); L.edge("exposure", "recorder", dashed=True)

L.seg("title", zh("小朋友们好！每天晚上，爸爸都要看新闻。今天，我们来学和新闻有关的单词。"), en("news"))
L.seg("map show:news focus:news", zh("新闻，英语是"), en("news"), zh("它虽然有 s，却只当一件事来说哦。"), en("The news is on TV."))
L.seg("show:information edge:news>information focus:information", zh("新闻告诉我们很多信息："), en("information"), zh("信息也不能数，不加 s。"))
L.seg("show:interesting edge:information>interesting focus:interesting", zh("有趣的，英语是"), en("interesting"), en("This is interesting news."))
L.seg("show:happen edge:news>happen focus:happen", zh("发生了什么事？发生，英语是"), en("happen"), en("What happened?"))
L.seg("show:event edge:happen>event focus:event", zh("发生的大事，是事件："), en("event"))
L.seg("show:earthquake edge:news>earthquake focus:earthquake", zh("地球，加上摇动，就是地震："), en("earth"), en("quake"), en("earthquake"),
      zh("地震时，要躲到结实的桌子下面哦。"))
L.seg("show:reporter edge:news>reporter focus:reporter", zh("拿着话筒采访的人，是记者："), en("reporter"))
L.seg("show:report edge:reporter>report focus:report", zh("记者写的报道。报道，去掉 e r："), en("report"), zh("还记得 teach 加 er 是 teacher 吗？report 加 er，就是 reporter。"))
L.seg("show:exposure edge:news>exposure focus:exposure", zh("把坏事公开出来，是曝光："), en("exposure"))
L.seg("show:recorder edge:exposure>recorder focus:recorder", zh("记者用录音机录下声音。记录是 record，加上 e r："), en("record"), en("recorder"))
L.seg("focus:reporter,recorder", zh("两个 e r 结尾的："), en("report, reporter", "focus:reporter"), en("record, recorder", "focus:recorder"))
L.review([("news", "news"), ("information", "information"), ("interesting", "interesting"), ("happen", "happen"), ("event", "event"), ("earthquake", "earthquake"),
          ("reporter", "reporter"), ("report", "report"), ("exposure", "exposure"), ("recorder", "recorder")],
         "太棒了！和爸爸妈妈一起看看新闻，用英语说一说发生了什么吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
