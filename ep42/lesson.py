import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep42", "school rules", "校规", 42, "rule")
V, A = dict(kind="verb"), dict(kind="adj")
L.node("headmaster", "headmaster", "/ˌhedˈmæstər/", "校长")
L.node("pupil", "pupil", "/ˈpjuːpl/", "小学生")
L.node("each", "each", "/iːtʃ/", "每个", kind="adj")
L.node("educate", "educate", "/ˈedʒukeɪt/", "教育", **V)
L.node("rule", "rule", "/ruːl/", "规则", plural="rules", pluralIpa="/ruːlz/")
L.node("follow", "follow", "/ˈfɑːloʊ/", "遵守；跟随", **V)
L.node("attention", "attention", "/əˈtenʃn/", "注意")
L.node("late", "late", "/leɪt/", "迟到的", **A)
L.node("bell", "bell", "/bel/", "铃")
L.node("alarm", "alarm", "/əˈlɑːrm/", "闹钟", alt="alarm clock", altLabel="全称")
L.node("attend", "attend", "/əˈtend/", "出席", **V)
L.node("absent", "absent", "/ˈæbsənt/", "缺席的", **A)
L.node("fight", "fight", "/faɪt/", "打架", **V)
L.node("punish", "punish", "/ˈpʌnɪʃ/", "惩罚", **V)
L.grid(["headmaster educate pupil",
        "follow rule each",
        "attention late bell",
        "attend alarm absent",
        "fight punish ."], dy=330)
L.edge("headmaster", "educate"); L.edge("educate", "pupil"); L.edge("pupil", "each", dashed=True); L.edge("educate", "rule")
L.edge("rule", "follow", "要"); L.edge("rule", "attention"); L.edge("rule", "late", "不要"); L.edge("late", "bell", "听到")
L.edge("late", "alarm", "定好"); L.edge("attend", "absent", "反义"); L.edge("fight", "punish", "会被")

L.seg("title", zh("小朋友们好！学校里，有很多要遵守的规则。今天，我们来学校规！"), en("school rules"))
L.seg("map show:headmaster focus:headmaster", zh("学校里最大的老师，是校长。头，加上主人："), en("head"), en("master"), en("headmaster"))
L.seg("show:educate edge:headmaster>educate focus:educate", zh("校长和老师们，一起教育我们："), en("educate"))
L.seg("show:pupil edge:educate>pupil focus:pupil", zh("在小学上学的孩子，是小学生："), en("pupil"))
L.seg("show:each edge:pupil>each focus:each", zh("每一个学生，都很重要。每个，英语是"), en("each"), en("each pupil"))
L.seg("show:rule edge:educate>rule focus:rule", zh("学校的规矩，是规则："), en("rule"), zh("很多条规则：", "plural:rule"), en("rules"))
L.seg("show:follow edge:rule>follow focus:follow", zh("规则要好好遵守："), en("follow"), en("Please follow the rules."))
L.seg("show:attention edge:rule>attention focus:attention", zh("上课要集中注意力："), en("attention"), en("Attention, please!"))
L.seg("show:late edge:rule>late focus:late", zh("早上不能迟到："), en("late"), en("Don't be late for school."))
L.seg("show:bell edge:late>bell focus:bell", zh("叮铃铃，上课铃响了！"), en("bell"))
L.seg("show:alarm edge:late>alarm focus:alarm", zh("为了不迟到，晚上要定好闹钟："), en("alarm"), zh("全称是", "alt:alarm"), en("alarm clock"))
L.seg("show:attend focus:attend", zh("每天都来上课，是出席："), en("attend"), en("I attend every class."))
L.seg("show:absent edge:attend>absent focus:absent", zh("没有来上课，是缺席的："), en("absent"), en("Who is absent today?"))
L.seg("show:fight focus:fight", zh("同学之间，不能打架："), en("fight"), en("Don't fight!"))
L.seg("show:punish edge:fight>punish focus:punish", zh("违反了规则，就会受到惩罚："), en("punish"))
L.seg("focus:none", zh("我们一起来读一读校规："))
L.seg("", en("Follow the rules.", "focus:follow,rule"), en("Don't be late.", "focus:late"), en("Pay attention in class.", "focus:attention"),
      en("Don't fight.", "focus:fight"))
L.review([("headmaster", "headmaster"), ("educate", "educate"), ("pupil", "pupil"), ("each", "each"), ("rule", "rule, rules"),
          ("follow", "follow"), ("attention", "attention"), ("late", "late"), ("bell", "bell"), ("alarm", "alarm"), ("attend", "attend"),
          ("absent", "absent"), ("fight", "fight"), ("punish", "punish")],
         "太棒了！做一个遵守校规的好学生吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
