import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep35", "jobs", "职业", 35, "job")
L.node("job", "job", "/dʒɑːb/", "工作；职业")
L.node("become", "become", "/bɪˈkʌm/", "成为", kind="verb", alt="became", altLabel="过去式")
for id, ipa, z in [("artist", "/ˈɑːrtɪst/", "艺术家；画家"), ("scientist", "/ˈsaɪəntɪst/", "科学家"), ("cook", "/kʊk/", "厨师"),
                   ("engineer", "/ˌendʒɪˈnɪr/", "工程师"), ("dentist", "/ˈdentɪst/", "牙医"), ("nurse", "/nɜːrs/", "护士"),
                   ("doctor", "/ˈdɑːktər/", "医生"), ("pilot", "/ˈpaɪlət/", "飞行员"), ("driver", "/ˈdraɪvər/", "司机")]:
    L.node(id, id, ipa, z)
L.grid(["artist scientist dentist",
        "become job engineer",
        "cook doctor nurse",
        "driver . pilot"], dy=350)
for b in ["artist", "scientist", "dentist", "engineer", "cook", "doctor", "nurse", "driver", "pilot"]:
    L.edge("job", b)
L.edge("become", "job", dashed=True)

L.seg("title", zh("小朋友们好！长大以后，你想做什么呢？今天，我们来学职业。"), en("jobs"))
L.seg("map show:job focus:job", zh("大人每天去上班做的事，是工作、职业："), en("job"), en("What's your job?"))
L.seg("show:become edge:become>job focus:become", zh("长大以后成为……，英语说"), en("become"),
      zh("已经成为了，要变成", "alt:become"), en("became"), en("I want to become a doctor."))
L.seg("focus:none", zh("很多职业的名字，都有小小的规律。"))
L.seg("show:artist edge:job>artist focus:artist", zh("画画的艺术家。艺术，加上 i s t："), en("art"), en("artist"))
L.seg("show:scientist edge:job>scientist focus:scientist", zh("做实验的科学家。科学，加上 i s t："), en("science"), en("scientist"))
L.seg("show:dentist edge:job>dentist focus:dentist", zh("给牙齿看病的牙医，也带着 i s t："), en("dentist"))
L.seg("focus:artist,scientist,dentist", zh("你发现了吗？i s t 常常表示做某件事的人。"),
      en("artist", "focus:artist"), en("scientist", "focus:scientist"), en("dentist", "focus:dentist"))
L.seg("show:engineer edge:job>engineer focus:engineer", zh("造桥、造机器的工程师："), en("engineer"))
L.seg("show:driver edge:job>driver focus:driver", zh("开车的司机。开车，加上 e r："), en("drive"), en("driver"))
L.seg("show:pilot edge:job>pilot focus:pilot", zh("开飞机的飞行员："), en("pilot"))
L.seg("show:cook edge:job>cook focus:cook", zh("做饭的厨师："), en("cook"),
      zh("小心哦，做饭的人是 cook，不是 cooker。cooker 是做饭的锅。"))
L.seg("show:doctor edge:job>doctor focus:doctor", zh("给我们看病的医生："), en("doctor"))
L.seg("show:nurse edge:job>nurse focus:nurse", zh("在医院照顾病人的护士："), en("nurse"))
L.seg("focus:none", zh("说一说你的梦想吧！"))
L.seg("", en("I want to become a pilot.", "focus:become,pilot"), en("My mom is a nurse.", "focus:nurse"),
      en("My father became a scientist.", "focus:become,scientist"))
L.review([("job", "job"), ("become", "become, became"), ("artist", "artist"), ("scientist", "scientist"), ("dentist", "dentist"),
          ("engineer", "engineer"), ("driver", "driver"), ("pilot", "pilot"), ("cook", "cook"), ("doctor", "doctor"), ("nurse", "nurse")],
         "太棒了！你长大想做什么？用英语告诉爸爸妈妈吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
