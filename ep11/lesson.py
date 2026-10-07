import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep11", "numbers", "数字 11–19", 11, "numbers")
W = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
IPA = ["/ɪˈlevn/", "/twelv/", "/ˌθɜːrˈtiːn/", "/ˌfɔːrˈtiːn/", "/ˌfɪfˈtiːn/", "/ˌsɪksˈtiːn/", "/ˌsevnˈtiːn/", "/ˌeɪˈtiːn/", "/ˌnaɪnˈtiːn/"]
ZH = ["十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九"]
L.node("numbers", "numbers", "/ˈnʌmbərz/", "数字")
for i, w in enumerate(W):
    k = i + 11
    extra = dict(alt=f"{k - 10} + 10", altLabel="=") if k >= 13 else {}
    L.node(w, w, IPA[i], ZH[i], icon=f"n{k}", kind="num", **extra)
L.grid([". numbers .",
        "eleven twelve thirteen",
        "sixteen fifteen fourteen",
        "seventeen eighteen nineteen"], dy=370)
# landscape: two wide rows (the transposed grid leaves no room for the "= n + 10" badges)
for id, x, y in [("numbers", 180, 190), ("eleven", 540, 190), ("twelve", 900, 190), ("thirteen", 1260, 190), ("fourteen", 1620, 190),
                 ("fifteen", 1620, 650), ("sixteen", 1260, 650), ("seventeen", 900, 650), ("eighteen", 540, 650), ("nineteen", 180, 650)]:
    L.byid[id]["at"] = [x, y]
for a, b in zip(W, W[1:]):
    L.edge(a, b)

L.seg("title", zh("小朋友们好！第三集，我们学会了从一数到十。今天，我们接着往下数！"), en("numbers"), zh("数字。"))
L.seg("map show:numbers focus:numbers", zh("十根手指都用完了，还想往下数，怎么办？别着急，我们一起来认识十一到十九。"))
L.seg("show:eleven focus:eleven", zh("十一，是"), en("eleven"), zh("它是一个全新的单词，要单独记住。"), en("eleven"))
L.seg("show:twelve edge:eleven>twelve focus:twelve", zh("十二，是"), en("twelve"),
      zh("它也很特别，要单独记。一年正好有十二个月："), en("twelve months"))
L.seg("show:thirteen edge:twelve>thirteen focus:thirteen", zh("从十三开始，就有规律啦！十三，是"), en("thirteen"),
      zh("后面的 t e e n，意思就是十。十三，就是三加十：", "alt:thirteen"), en("three plus ten"),
      zh("不过三本来是"), en("three"), zh("在这里变成了 t h i r，要小心哦。"))
L.seg("show:fourteen edge:thirteen>fourteen focus:fourteen alt:fourteen", zh("十四，就是四，加上 t e e n："), en("four"), en("fourteen"))
L.seg("show:fifteen edge:fourteen>fifteen focus:fifteen alt:fifteen", zh("十五要注意，五本来是"), en("five"),
      zh("在这里变成了 f i f："), en("fifteen"))
L.seg("show:sixteen edge:fifteen>sixteen focus:sixteen alt:sixteen", zh("十六："), en("six"), en("sixteen"))
L.seg("show:seventeen edge:sixteen>seventeen focus:seventeen alt:seventeen", zh("十七："), en("seven"), en("seventeen"))
L.seg("show:eighteen edge:seventeen>eighteen focus:eighteen alt:eighteen", zh("十八：八本来是"), en("eight"),
      zh("它已经以字母 t 结尾了，所以只要再加上 e e n，中间只有一个 t："), en("eighteen"))
L.seg("show:nineteen edge:eighteen>nineteen focus:nineteen alt:nineteen", zh("十九："), en("nine"), en("nineteen"))
L.seg("focus:none", zh("我们来总结一下规律。"))
L.seg("focus:eleven,twelve", zh("十一和十二最特别，要单独记住："), en("eleven", "focus:eleven"), en("twelve", "focus:twelve"))
L.seg("focus:fourteen,sixteen,seventeen,nineteen", zh("十四、十六、十七、十九最听话，直接在后面加上 t e e n："),
      en("fourteen", "focus:fourteen"), en("sixteen", "focus:sixteen"), en("seventeen", "focus:seventeen"), en("nineteen", "focus:nineteen"))
L.seg("focus:thirteen,fifteen,eighteen", zh("十三、十五、十八，前面要稍微变一变："),
      en("thirteen", "focus:thirteen"), en("fifteen", "focus:fifteen"), en("eighteen", "focus:eighteen"))
L.seg("focus:none", zh("小提示：这些数字读的时候，重音落在后面的 teen 上。我们一起从十一数到十九吧！"))
L.seg("", *[en(w, "focus:" + w) for w in W])
L.seg("focus:none", zh("考考你：十加五，等于几？想一想……"))
L.seg("focus:fifteen", zh("答案是"), en("fifteen"), en("Ten plus five is fifteen."))
L.seg("focus:none", zh("再来一题：九加九，等于几？想一想……"))
L.seg("focus:eighteen", zh("答对了吗？是"), en("eighteen"), en("Nine plus nine is eighteen."))
L.review([("numbers", "numbers")] + [(w, w) for w in W],
         "太棒了！今天回家，试着用英语数一数，家里的楼梯有多少级吧。点一点图上的数字，还能再听一遍发音哦。")
L.save()
