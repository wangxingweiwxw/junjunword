import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep99", "nation", "国家政体", 99, "republic")
A = dict(kind="adj")
L.node("country", "country", "/ˈkʌntri/", "国家")
L.node("republic", "republic", "/rɪˈpʌblɪk/", "共和国")
L.node("public", "public", "/ˈpʌblɪk/", "公众的", **A)
L.node("province", "province", "/ˈprɑːvɪns/", "省")
L.node("state", "state", "/steɪt/", "州")
L.node("capital", "capital", "/ˈkæpɪtl/", "首都；大写字母")
L.node("national", "national", "/ˈnæʃnəl/", "国家的；民族的", **A, alt="nation", altLabel="来自")
L.node("matter", "matter", "/ˈmætər/", "事情；要紧")
L.node("abroad", "abroad", "/əˈbrɔːd/", "在国外", kind="adv")
L.node("president", "president", "/ˈprezɪdənt/", "总统；主席")
L.node("king", "king", "/kɪŋ/", "国王")
L.node("queen", "queen", "/kwiːn/", "女王；王后")
L.grid(["public republic king",
        "province country queen",
        "state capital president",
        "national matter abroad"], dy=350)
L.edge("public", "republic", dashed=True); L.edge("country", "republic"); L.edge("country", "province"); L.edge("country", "state", dashed=True); L.edge("country", "capital")
L.edge("country", "national"); L.edge("country", "president"); L.edge("country", "king", dashed=True); L.edge("king", "queen"); L.edge("country", "abroad", dashed=True)
L.edge("national", "matter", dashed=True)

L.seg("title", zh("小朋友们好！今天，我们来认识国家的更多知识！"), en("country"))
L.seg("map show:country focus:country", zh("国家："), en("country"))
L.seg("show:public focus:public", zh("还记得第八十三集的公共的吗？"), en("public"))
L.seg("show:republic edge:public>republic edge:country>republic focus:republic", zh("共和国，英语是"), en("republic"), zh("仔细看，republic 里面藏着 public 哦。"),
      en("the People's Republic of China"))
L.seg("show:province edge:country>province focus:province", zh("中国分成很多个省："), en("province"))
L.seg("show:state edge:country>state focus:state", zh("美国分成五十个州："), en("state"))
L.seg("show:capital edge:country>capital focus:capital", zh("一个国家的首都："), en("capital"), en("Beijing is the capital of China."),
      zh("它还有一个意思，是大写字母。"))
L.seg("show:national edge:country>national focus:national", zh("国家是 nation，加上 a l，就是国家的："), en("national"), en("the National Day"))
L.seg("show:president edge:country>president focus:president", zh("有的国家的领导人，叫总统或主席："), en("president"))
L.seg("show:king edge:country>king focus:king", zh("有的国家有国王："), en("king"))
L.seg("show:queen edge:king>queen focus:queen", zh("还有女王或王后："), en("queen"))
L.seg("show:abroad edge:country>abroad focus:abroad", zh("去别的国家，是到国外："), en("abroad"), en("I want to study abroad."))
L.seg("show:matter edge:national>matter focus:matter", zh("最后学一句常用语，问别人怎么了："), en("What's the matter?"), zh("matter 的意思是事情、要紧。"))
L.seg("focus:king,queen", zh("国王和女王："), en("king", "focus:king"), en("queen", "focus:queen"))
L.review([("country", "country"), ("public", "public"), ("republic", "republic"), ("province", "province"), ("state", "state"), ("capital", "capital"),
          ("national", "national"), ("president", "president"), ("king", "king"), ("queen", "queen"), ("abroad", "abroad"), ("matter", "matter")],
         "太棒了！继续加油，用英语去认识更大的世界吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
