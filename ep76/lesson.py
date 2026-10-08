import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep76", "letters", "书信", 76, "letter")
A = dict(kind="adj")
L.node("friendship", "friendship", "/ˈfrendʃɪp/", "友谊", alt="friend", altLabel="来自")
L.node("conversation", "conversation", "/ˌkɑːnvərˈseɪʃn/", "对话")
L.node("personal", "personal", "/ˈpɜːrsənl/", "私人的", **A)
L.node("secret", "secret", "/ˈsiːkrət/", "秘密")
L.node("unlucky", "unlucky", "/ʌnˈlʌki/", "不幸的", **A)
L.node("send", "send", "/send/", "寄；发送", kind="verb")
L.node("mail", "mail", "/meɪl/", "邮件")
L.node("postcard", "postcard", "/ˈpoʊstkɑːrd/", "明信片")
L.node("letter", "letter", "/ˈletər/", "信")
L.node("stamp", "stamp", "/stæmp/", "邮票")
L.node("package", "package", "/ˈpækɪdʒ/", "包裹")
L.node("box", "box", "/bɑːks/", "盒子")
L.node("mention", "mention", "/ˈmenʃn/", "提到", kind="verb")
L.node("express", "express", "/ɪkˈspres/", "快递；快的")
L.grid(["secret conversation personal",
        "unlucky friendship send",
        "mail letter postcard",
        "stamp mention package",
        ". express box"], dy=330)
L.edge("friendship", "conversation"); L.edge("conversation", "secret"); L.edge("conversation", "personal"); L.edge("unlucky", "friendship", dashed=True)
L.edge("friendship", "send"); L.edge("send", "letter", dashed=True); L.edge("letter", "mail"); L.edge("letter", "postcard"); L.edge("letter", "stamp", "贴上")
L.edge("letter", "mention"); L.edge("send", "package"); L.edge("package", "box"); L.edge("package", "express")

L.seg("title", zh("小朋友们好！给远方的好朋友写一封信吧！今天，我们来学和书信有关的单词。"), en("letters"))
L.seg("map show:friendship focus:friendship", zh("还记得第二十二集的朋友 friend 吗？加上 s h i p，就是友谊："), en("friend"), en("friendship"))
L.seg("show:conversation edge:friendship>conversation focus:conversation", zh("好朋友之间，有说不完的对话："), en("conversation"))
L.seg("show:secret edge:conversation>secret focus:secret", zh("还会分享小秘密："), en("secret"), en("It's a secret!"))
L.seg("show:personal edge:conversation>personal focus:personal", zh("只属于自己的，是私人的："), en("personal"), en("a personal letter"))
L.seg("show:unlucky edge:unlucky>friendship focus:unlucky", zh("好朋友搬走了，真不幸。还记得第六十七集的 lucky 吗？加上 u n："), en("unlucky"))
L.seg("show:send edge:friendship>send focus:send", zh("没关系，我们可以寄东西给他："), en("send"))
L.seg("show:letter edge:send>letter focus:letter", zh("写一封信："), en("letter"), en("I received a letter from my grandmother."))
L.seg("show:mail edge:letter>mail focus:mail", zh("寄出去的信件，叫邮件："), en("mail"), zh("电子邮件，就是 e-mail。"))
L.seg("show:postcard edge:letter>postcard focus:postcard", zh("背面有风景画的，是明信片。邮寄，加上卡片："), en("post"), en("card"), en("postcard"))
L.seg("show:stamp edge:letter>stamp focus:stamp", zh("信封上，要贴一张邮票："), en("stamp"))
L.seg("show:mention edge:letter>mention focus:mention", zh("在信里提到了你的名字。提到，英语是"), en("mention"))
L.seg("show:package edge:send>package focus:package", zh("大一点的东西，就寄包裹："), en("package"))
L.seg("show:box edge:package>box focus:box", zh("包裹里面，是一个盒子："), en("box"))
L.seg("show:express edge:package>express focus:express", zh("要快一点到，就寄快递："), en("express"))
L.seg("focus:friendship,unlucky", zh("今天的两个小尾巴："), en("friend, friendship", "focus:friendship"), en("lucky, unlucky", "focus:unlucky"))
L.review([("friendship", "friendship"), ("conversation", "conversation"), ("secret", "secret"), ("personal", "personal"), ("unlucky", "unlucky"), ("send", "send"),
          ("letter", "letter"), ("mail", "mail"), ("postcard", "postcard"), ("stamp", "stamp"), ("mention", "mention"), ("package", "package"), ("box", "box"), ("express", "express")],
         "太棒了！给你的好朋友写一张明信片吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
