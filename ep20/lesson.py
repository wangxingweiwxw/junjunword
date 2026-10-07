import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep20", "seasons", "季节", 20, "season")
L.node("season", "season", "/ˈsiːzn/", "季节", plural="seasons", pluralIpa="/ˈsiːznz/")
L.node("spring", "spring", "/sprɪŋ/", "春天")
L.node("summer", "summer", "/ˈsʌmər/", "夏天")
L.node("autumn", "autumn", "/ˈɔːtəm/", "秋天", alt="fall", altLabel="美式")
L.node("winter", "winter", "/ˈwɪntər/", "冬天")
L.node("dress", "dress", "/dres/", "连衣裙")
L.node("skirt", "skirt", "/skɜːrt/", "短裙")
L.node("shorts", "shorts", "/ʃɔːrts/", "短裤")
L.node("pocket", "pocket", "/ˈpɑːkɪt/", "口袋")
L.node("jacket", "jacket", "/ˈdʒækɪt/", "夹克")
L.node("jeans", "jeans", "/dʒiːnz/", "牛仔裤")
L.node("sweater", "sweater", "/ˈswetər/", "毛衣")
L.node("coat", "coat", "/koʊt/", "外套；大衣")
L.node("also", "also", "/ˈɔːlsoʊ/", "也", kind="adv")
L.grid(["dress spring skirt",
        "shorts summer pocket",
        ". season also",
        "jacket autumn jeans",
        "sweater winter coat"], dy=330)
L.edge("season", "spring"); L.edge("spring", "dress"); L.edge("spring", "skirt"); L.edge("season", "summer")
L.edge("summer", "shorts"); L.edge("shorts", "pocket", dashed=True); L.edge("season", "autumn"); L.edge("autumn", "jacket")
L.edge("autumn", "jeans"); L.edge("season", "winter"); L.edge("winter", "sweater"); L.edge("winter", "coat")
L.edge("also", "season", dashed=True)

L.seg("title", zh("小朋友们好！一年有四个季节，每个季节，我们都穿不一样的衣服。"), en("seasons"), zh("季节。"))
L.seg("map show:season focus:season", zh("春、夏、秋、冬，都叫季节："), en("season"),
      zh("一年有四个季节：", "plural:season"), en("four seasons"))
L.seg("show:spring edge:season>spring focus:spring", zh("小草发芽，花儿开放，春天来了："), en("spring"), en("in spring"))
L.seg("show:dress edge:spring>dress focus:dress", zh("春天暖洋洋的，女孩子可以穿上漂亮的连衣裙："), en("dress"))
L.seg("show:skirt edge:spring>skirt focus:skirt", zh("或者穿一条短短的裙子："), en("skirt"),
      zh("连衣裙上下连在一起；短裙只穿在下半身。"), en("dress", "focus:dress"), en("skirt", "focus:skirt"))
L.seg("show:summer edge:season>summer focus:summer", zh("太阳火辣辣，知了叫不停，夏天到了："), en("summer"), en("in summer"))
L.seg("show:shorts edge:summer>shorts focus:shorts", zh("夏天好热，穿上凉快的短裤："), en("shorts"),
      zh("短裤有两条裤腿，所以和第十集的长裤一样，总是带着 s。"))
L.seg("show:pocket edge:shorts>pocket focus:pocket", zh("短裤上还有口袋，可以装小东西："), en("pocket"), en("What's in your pocket?"))
L.seg("show:autumn edge:season>autumn focus:autumn", zh("树叶变黄，一片片落下来，秋天到了："), en("autumn"),
      zh("美国人还管秋天叫", "alt:autumn"), en("fall"), zh("还记得第九集吗？这个词也是落下的意思，树叶落下来，就是秋天。"))
L.seg("show:jacket edge:autumn>jacket focus:jacket", zh("秋天凉凉的，穿上一件夹克："), en("jacket"))
L.seg("show:jeans edge:autumn>jeans focus:jeans", zh("再配一条蓝色的牛仔裤："), en("jeans"), zh("它也总是带着 s。"))
L.seg("show:winter edge:season>winter focus:winter", zh("下雪啦，可以堆雪人了，冬天到了："), en("winter"), en("in winter"))
L.seg("show:sweater edge:winter>sweater focus:sweater", zh("冬天好冷，要穿上暖和的毛衣："), en("sweater"),
      zh("中间的 e a，在这里读短短的 e。"), en("In winter, I wear a sweater."))
L.seg("show:coat edge:winter>coat focus:coat", zh("出门的时候，外面还要再穿一件厚厚的大衣："), en("coat"))
L.seg("show:also edge:also>season focus:also", zh("我穿了毛衣，也穿了大衣。也，英语是"), en("also"),
      en("I also wear a coat.", "focus:also,coat"))
L.seg("focus:spring,summer,autumn,winter", zh("我们按顺序，把四个季节读一遍："),
      en("spring", "focus:spring"), en("summer", "focus:summer"), en("autumn", "focus:autumn"), en("winter", "focus:winter"))
L.seg("focus:none", zh("考考你：这些衣服，在哪个季节穿？"))
L.seg("", en("Shorts?", "focus:shorts"), en("Summer!", "focus:summer"), en("A sweater?", "focus:sweater"), en("Winter!", "focus:winter"),
      en("A jacket?", "focus:jacket"), en("Autumn!", "focus:autumn"))
L.review([("season", "season, seasons"), ("spring", "spring"), ("dress", "dress"), ("skirt", "skirt"), ("summer", "summer"),
          ("shorts", "shorts"), ("pocket", "pocket"), ("autumn", "autumn, fall"), ("jacket", "jacket"), ("jeans", "jeans"),
          ("winter", "winter"), ("sweater", "sweater"), ("coat", "coat"), ("also", "also")],
         "太棒了！你最喜欢哪个季节？用英语告诉爸爸妈妈吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
