import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep07", "action", "动作", 7, "action")
V = dict(kind="verb")
L.node("action", "action", "/ˈækʃn/", "动作；行动")
L.node("walk", "walk", "/wɔːk/", "走；步行", **V)
L.node("run", "run", "/rʌn/", "跑", **V)
L.node("stand", "stand", "/stænd/", "站", **V)
L.node("sit", "sit", "/sɪt/", "坐", **V)
L.node("wait", "wait", "/weɪt/", "等待", **V)
L.node("look", "look", "/lʊk/", "看", **V)
L.node("see", "see", "/siː/", "看见", **V)
L.node("talk", "talk", "/tɔːk/", "交谈；聊天", alt="talk with friends", altLabel="搭配", **V)
L.node("say", "say", "/seɪ/", "说（话）", alt="say hello", altLabel="搭配", **V)
L.node("speak", "speak", "/spiːk/", "说（语言）", alt="speak English", altLabel="搭配", **V)
L.node("tell", "tell", "/tel/", "告诉；讲述", alt="tell a story", altLabel="搭配", **V)
L.grid(["run walk action",
        "sit stand look",
        "wait . see",
        "talk say speak",
        ". tell ."], flip=True, dy=330)
L.edge("action", "walk"); L.edge("walk", "run", "更快"); L.edge("walk", "stand", "停下")
L.edge("stand", "sit"); L.edge("stand", "wait"); L.edge("action", "look"); L.edge("look", "see", "结果")

L.seg("title", zh("小朋友们好！今天我们来学动作。准备好了吗？一起动起来！"), en("action"), zh("动作，行动。"))
L.seg("map show:action focus:action", zh("拍电影的时候，导演一喊这个词，演员们就开始表演啦："), en("Action!"),
      zh("它的意思，就是动作、行动。"), en("action"))
L.seg("show:walk edge:action>walk focus:walk", zh("两只脚轮流向前，一步一步地走："), en("walk"), en("Let's walk to school."))
L.seg("show:run edge:walk>run focus:run", zh("走得越来越快，两只脚一起离开地面，就变成了跑："), en("run"), en("Run, run, run!"))
L.seg("show:stand edge:walk>stand focus:stand", zh("停下脚步，直直地站好："), en("stand"), en("Stand up, please."))
L.seg("show:sit edge:stand>sit focus:sit", zh("站累了，找一把椅子坐下来："), en("sit"), en("Sit down, please."))
L.seg("focus:stand,sit", zh("站起来，是"), en("stand up", "focus:stand"), zh("坐下去，是", "focus:sit"), en("sit down"))
L.seg("show:wait edge:stand>wait focus:wait", zh("站在路口，红灯亮了，要耐心地等一等："), en("wait"), en("Wait for me!"))
L.seg("show:look edge:action>look focus:look", zh("下面是眼睛的动作。把眼睛转过去，专门去看："), en("look"), en("Look at me!"))
L.seg("show:see edge:look>see focus:see", zh("东西自己跑进了你的眼睛里，就是看见："), en("see"), en("I can see a bird."))
L.seg("focus:look,see", zh("看，是你主动去看；看见，是看的结果。"), en("Look! Can you see it?"))
L.seg("focus:none", zh("最后是嘴巴的动作。这四个词都和说话有关，用法却各不相同哦。"))
L.seg("show:talk focus:talk", zh("两个人你一句、我一句，聊天交谈，用"), en("talk"),
      zh("常常这样说：", "alt:talk"), en("talk with friends"))
L.seg("show:say focus:say", zh("说出一句具体的话，用"), en("say"), zh("比如，说一声你好：", "alt:say"), en("say hello"))
L.seg("show:speak focus:speak", zh("说一种语言，用"), en("speak"), zh("比如，说英语：", "alt:speak"), en("speak English"))
L.seg("show:tell focus:tell", zh("把一件事告诉别人，或者讲一个故事，用"), en("tell"), zh("比如，讲一个故事：", "alt:tell"), en("tell a story"))
L.seg("focus:talk,say,speak,tell", zh("我们把这四个连起来说一遍："),
      en("talk with friends", "focus:talk"), en("say hello", "focus:say"), en("speak English", "focus:speak"), en("tell a story", "focus:tell"))
L.seg("focus:none", zh("来玩个小游戏吧！听到口令，就跟着做动作！"))
L.seg("", en("Stand up!", "focus:stand"), en("Walk!", "focus:walk"), en("Run!", "focus:run"),
      en("Stop! Wait!", "focus:wait"), en("Look!", "focus:look"), en("Sit down.", "focus:sit"))
L.review([("action", "action"), ("walk", "walk"), ("run", "run"), ("stand", "stand"), ("sit", "sit"), ("wait", "wait"),
          ("look", "look"), ("see", "see"), ("talk", "talk"), ("say", "say"), ("speak", "speak"), ("tell", "tell")],
         "太棒了！今天回家，用英语给爸爸妈妈发口令，让他们也动起来吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
