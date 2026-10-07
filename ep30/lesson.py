import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from lessonkit import Lesson, zh, en

L = Lesson("ep30", "music", "音乐", 30, "music")
L.node("sound", "sound", "/saʊnd/", "声音")
L.node("noise", "noise", "/nɔɪz/", "噪音", alt="noisy", altLabel="加 y →")
L.node("music", "music", "/ˈmjuːzɪk/", "音乐")
L.node("concert", "concert", "/ˈkɑːnsərt/", "音乐会")
L.node("song", "song", "/sɔːŋ/", "歌曲")
L.node("sing", "sing", "/sɪŋ/", "唱歌", kind="verb", alt="singer", altLabel="加 er →")
L.node("voice", "voice", "/vɔɪs/", "嗓音")
L.node("terrible", "terrible", "/ˈterəbl/", "糟糕的", kind="adj")
L.node("piano", "piano", "/piˈænoʊ/", "钢琴")
L.node("violin", "violin", "/ˌvaɪəˈlɪn/", "小提琴")
L.node("guitar", "guitar", "/ɡɪˈtɑːr/", "吉他")
L.node("drum", "drum", "/drʌm/", "鼓")
L.grid(["noise sound music",
        "song concert piano",
        "sing . violin",
        "voice drum guitar",
        "terrible . ."], dy=330)
L.edge("sound", "noise"); L.edge("sound", "music"); L.edge("concert", "music"); L.edge("concert", "song")
L.edge("song", "sing"); L.edge("sing", "voice"); L.edge("voice", "terrible", dashed=True)
for b in ["piano", "violin", "guitar", "drum"]:
    L.edge("concert", b)

L.seg("title", zh("小朋友们好！嘘，你听，是什么声音？今天，我们来学音乐。"), en("music"), zh("音乐。"))
L.seg("map show:sound focus:sound", zh("耳朵听到的一切，都叫声音："), en("sound"), en("What's that sound?"))
L.seg("show:noise edge:sound>noise focus:noise", zh("吵吵闹闹、让人想捂住耳朵的声音，是噪音："), en("noise"),
      zh("加上 y，就是吵闹的：", "alt:noise"), en("noisy"))
L.seg("show:music edge:sound>music focus:music", zh("好听的、让人想跳舞的声音，是音乐："), en("music"), en("I love music!"))
L.seg("show:concert edge:concert>music focus:concert", zh("很多人一起听乐队表演，是音乐会："), en("concert"))
L.seg("show:piano edge:concert>piano focus:piano", zh("音乐会上，有黑白琴键的钢琴："), en("piano"))
L.seg("show:violin edge:concert>violin focus:violin", zh("夹在下巴下面拉的小提琴："), en("violin"))
L.seg("show:guitar edge:concert>guitar focus:guitar", zh("抱在怀里弹的吉他："), en("guitar"), zh("小提示：开头的 g u，只读 g。"))
L.seg("show:drum edge:concert>drum focus:drum", zh("咚咚咚，敲起来的鼓："), en("drum"))
L.seg("focus:piano,violin,guitar,drum", zh("弹钢琴、拉小提琴、弹吉他、打鼓，英语里都用同一个词 play："),
      en("play the piano", "focus:piano"), en("play the violin", "focus:violin"), en("play the guitar", "focus:guitar"), en("play the drums", "focus:drum"))
L.seg("show:song edge:concert>song focus:song", zh("音乐会上，还有好听的歌曲："), en("song"))
L.seg("show:sing edge:song>sing focus:sing", zh("唱歌，是"), en("sing"), en("sing a song"),
      zh("加上 e r，就是唱歌的人，歌手：", "alt:sing"), en("singer"))
L.seg("show:voice edge:sing>voice focus:voice", zh("唱歌的时候，从嗓子里发出来的声音，是嗓音："), en("voice"), en("She has a sweet voice."))
L.seg("show:terrible edge:voice>terrible focus:terrible", zh("要是唱跑了调，听起来就很糟糕："), en("terrible"),
      zh("不过没关系，多练习就会越唱越好！"))
L.seg("focus:sound,noise,voice", zh("三种声音，比一比："), en("sound", "focus:sound"), en("noise", "focus:noise"), en("voice", "focus:voice"))
L.seg("focus:none", zh("我们也来开一场小小音乐会吧！"))
L.seg("", en("I play the guitar.", "focus:guitar"), en("You play the drums.", "focus:drum"),
      en("Let's sing a song together!", "focus:sing,song"))
L.review([("sound", "sound"), ("noise", "noise, noisy"), ("music", "music"), ("concert", "concert"), ("piano", "piano"),
          ("violin", "violin"), ("guitar", "guitar"), ("drum", "drum"), ("song", "song"), ("sing", "sing, singer"),
          ("voice", "voice"), ("terrible", "terrible")],
         "太棒了！今天回家，唱一首你最喜欢的英文歌吧。点一点图上的单词，还能再听一遍发音哦。")
L.save()
