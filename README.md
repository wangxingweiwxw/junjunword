# 背单词动画课（原创 HTML 版）

每集 = 一个 `lesson.json`（单词、布局、讲解词），播放器全部共用。画面是代码画的 SVG，配音是 edge-tts，
整集不到 1 MB，100 集约 100 MB，放 Cloudflare R2 / Pages / GitHub Pages 都在免费额度内。

```
player/            共用引擎（所有集只需一份）
  player.js        播放器：render(t) 由音频时钟驱动；横屏/竖屏自动切换；点卡片读单词
  player.css
  icons.js         原创插图库（person/boy/girl/man/woman/elder/group/nametag/sprout，
                   ep02 起：family/parents/mother/father/child/kid/daughter/son/depend/kiss/call；
                   ep03 起：number/numbers/n1…n10），也可直接用 emoji
ep01/
  index.html       10 行壳子，引用 ../player/
  lesson.json      ← 唯一需要手写的文件
  timeline.json    tts.py 生成
  audio/lesson.mp3 讲解音轨（tts.py 生成）
  audio/words.mp3  单词发音包，点卡片时播放（tts.py 生成）
  audio/cache/     TTS 缓存（不用部署）
  ep01.mp4         可选：录成视频（capture.cjs 生成）
tools/
  tts.py           lesson.json → 音频 + timeline.json
  capture.cjs      逐帧录成 1280x720 MP4
  shots.cjs        任意时间点截图检查
  ffmpeg           带 libx264 的静态 ffmpeg（不在仓库里，体积太大；自行放一个静态版 ffmpeg 到这里）
```

## 用 Python 写课（ep04 起）

ep04+ 的 `lesson.json` 由同目录的 `lesson.py` 生成（`python3 ep04/lesson.py`），用 `tools/lessonkit.py`：
只画**竖屏 3 列网格**（每行一个字符串，`.` 表示空位），横屏自动取转置（也可在 `grid()` 之后改 `L.byid[id]["at"]` 自定横屏位置，见 ep11）——竖屏里不交叉的箭头，横屏里也不交叉。
`L.grid(rows, flip=True)` 让横屏上下翻转；`dy` 调竖屏行距。保存时会检查 cue 里引用的 id 是否都存在。
`altLabel` 改徽章前缀（默认“也叫”，如 `"过去式"`、`"搭配"`）；`kind` 可选 `adj` `verb` `num` `prep` `adv`。
`icons.js` 里有可摆姿势的 `kid({la, ra, ll, rl, rot, hl})`（四肢角度，0=向下，90=向前），走、跑、坐、跳、身体部位高亮都用它。

## 做新的一集

1. 复制 `ep01/` 为 `ep02/`，删掉 `audio/`、`timeline.json`、`*.mp4`，改 `index.html` 的标题。
2. 改 `lesson.json`：
   - `nodes`：单词卡。`at` 是横屏坐标（舞台 1800×900），`atP` 是竖屏坐标（900×1120）；
     `kind: "adj"` 显示绿色 adj. 标签，`kind: "verb"` 显示蓝色 v. 标签；有 `plural` 的卡片会在 `plural:id` 提示时变成复数并高亮变化的字母；
     有 `alt`（如 mother 的 `"alt": "mom"`）的卡片会在 `alt:id` 提示时在下方弹出“也叫 mom”，点卡片会连读两个词。
     单词超过 6 个字母时字号自动缩小。`kind: "num"` 显示紫色 num. 标签；`pluralIcon` 可给复数形式换一张专用插图。
     `icon` 用 icons.js 里的名字，或直接写一个 emoji。
   - `edges`：箭头，`label` 是箭头旁的小字，`dashed` 虚线。
   - `script`：讲解词。每段 `parts` 是 `{"zh": …}` 或 `{"en": …}`（中英文分别用不同的声音读）；
     `cue` 在这一段（或这一句）开始时触发：`title` `map` `show:id` `edge:a>b` `focus:id[,id]` `focus:none` `plural:id` `alt:id` `end`。
     中文句子里尽量不要夹英文单词，英文单独写成 `en` 句，读音才标准。
3. `python3 tools/tts.py ep02`（需要联网；只重新合成改动过的句子）
4. 预览：在 vocab/ 下 `python3 -m http.server 8765`，打开 http://127.0.0.1:8765/ep02/
   截图检查：`node tools/shots.cjs ep02 /tmp 10 60 120`（加 `390x844` 看手机竖屏）
5. 需要视频时：服务开着的情况下 `node tools/capture.cjs ep02`（每集约 10 分钟）

## 部署

首次使用工具：`cd tools && npm install && npx playwright install chromium`，再放入静态 ffmpeg。


只需上传 `player/` 和每集的 `index.html`、`lesson.json`、`timeline.json`、`audio/*.mp3`（不传 `audio/cache/`）。

## 已完成

| 集 | 单词 | 时长 |
|---|---|---|
| ep01 people | people person name boy girl young man woman old | 2:25 |
| ep02 family | family parents mother(mom) father(dad) child kid daughter son depend kiss call | 3:42 |
| ep03 numbers | number(s) one two three four five six seven eight nine ten | 3:20 |
| ep04 birthday | birthday party present(gift) give get for cake candle match wish blow balloon | 2:50 |
| ep05 home | home house address key door lock window gate yard flower stairs step pool | 2:46 |
| ep06 school | school class teach(teacher) work schoolwork homework complete classmate uniform grade term | 2:44 |
| ep07 action | action walk run stand sit wait look see talk say speak tell | 2:57 |
| ep08 body | body head hair neck shoulder arm hand finger leg knee foot(feet) toe shake | 2:57 |
| ep09 sports | sports run race jump fall(fell) ball football soccer basketball volleyball table tennis net | 2:52 |
| ep10 clothes | clothes wear hat cap T-shirt underwear trousers sock shoe pair | 2:32 |
| ep11 numbers 11–19 | numbers eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen | 3:12 |
| ep12 party | invite invitation guest please celebrate among without age forget remember remind excuse | 2:49 |
| ep13 schoolbag | schoolbag(bookbag) book dictionary notebook paper pen pencil eraser ruler crayon | 2:23 |
| ep14 time | day morning noon afternoon evening night midnight time clock o'clock at hour minute second | 3:28 |
| ep15 sports (2) | sports choose(choice) baseball throw hit swimming swim training strong weak quick coach encourage spirit | 2:50 |
| ep16 face | face eye ear nose mouth tooth(teeth) tongue chin throat chest brain mind | 2:38 |
| ep17 senses | sense see sight hear listen hearing smell taste sweet salty sour bitter touch feel | 2:48 |
| ep18 food | hungry eat full food meal rice meat chicken pork beef mutton oil spicy | 2:29 |
| ep19 weather | weather air sunny sunshine cloudy windy rainy shower storm(stormy) foggy hot cold snowy | 3:02 |
| ep20 seasons | season spring summer autumn(fall) winter dress skirt shorts pocket jacket jeans sweater coat also | 2:55 |
| ep21 meals | breakfast porridge pancake butter prefer lunch sandwich bread salad noodles dinner hamburger spaghetti sausage | 2:53 |
| ep22 friends | let play with friend game toy share greet wave shy nervous promise | 2:42 |
| ep23 numbers 20–100 | zero twenty … ninety, one hundred | 2:44 |
| ep24 colours | colour(color) red orange yellow green blue purple pink brown bright white gold silver dark black | 2:47 |
| ep25 transportation | transportation car truck bus bicycle(bike) motorbike ride train subway ticket plane ship boat fast slow | 3:06 |
| ep26 relatives | grandfather grandmother grandparents grandson granddaughter uncle aunt cousin relative | 2:41 |
| ep27 classroom | classroom board blackboard chalk teacher lesson student monitor desk seat row group | 2:28 |
| ep28 measures | tall short long straight inch thick thin a lot much weigh half quarter | 2:41 |
| ep29 clubs | club join chess painting imagine photo camera background camping tent magazine article poem inspiration | 2:36 |
| ep30 music | sound noise music concert piano violin guitar drum song sing voice terrible | 2:29 |
| ep31 compare | compare same different as good well bad badly quite great cool | 2:17 |
| ep32 time words | today yesterday tomorrow past future tonight daily(everyday) all day since until(till) | 2:24 |
| ep33 learning | learn read story write spell spelling understand repeat teach explain example clear speak speech | 2:41 |
| ep34 family tree | husband wife couple parents ancestor brother sister twins blood relation relationship although | 2:20 |
| ep35 jobs | job become(became) artist scientist dentist engineer driver pilot cook doctor nurse | 2:10 |
| ep36 week | week Monday … Sunday weekday weekend on before after | 2:28 |
| ep37 farm | farm field grass plant tree leaf(leaves) pig sheep horse cow hen lay egg fox | 2:20 |
| ep38 rooms | room bedroom living room kitchen bathroom ceiling toilet restroom washroom toothbrush soap towel | 2:19 |
| ep39 feelings | feeling happy smile like excited surprised sudden(suddenly) mad sad cry tears afraid scared fear | 2:30 |
| ep40 drinks | thirsty(thirst) drink water milk juice coffee beer soup cup enough satisfy | 2:00 |
| ep41 chores | chore mess(messy) tidy dirty wash clean floor sweep brush rubbish bin basket | 2:11 |
| ep42 school rules | headmaster educate pupil each rule follow attention late bell alarm attend absent fight punish | 2:15 |
| ep43 town | town village square show restaurant cinema supermarket mall bookstore street zoo crossing cross open closed | 2:20 |
| ep44 restaurant | restaurant menu service treat pardon normal dish make delicious dumpling common plenty piece bit | 2:29 |
| ep45 animals | animal wild pet care dog cat usual unusual snake mouse(mice) bird wing fly tail | 2:27 |
| ep46 countryside | farm field plants kind wheat corn cotton pick water live(alive) die(dead) wood duck rabbit spider | 2:30 |
| ep47 zoo | zoo panda bamboo lion zebra giraffe elephant owl monkey bear wolf(wolves) shark whale | 2:16 |
| ep48 shopping | store buy sell shopping free afford market cheap expensive trade deal steal | 2:08 |
| ep49 accessories | clothes shop available earring scarf glove ring bring suit tie bag handbag purse wallet | 2:21 |
| ep50 weather (2) | weather temperature degree heat smoke dry wet rainy umbrella raincoat take too snowy ice freeze(froze) | 2:25 |
| ep51 town (2) | town street corner across church factory grounds prison library borrow lend return bank | 2:22 |
| ep52 transport (2) | airport flight arrive narrowly drive(driver) license taxi wheel traffic station underground railway tunnel bridge | 2:26 |
| ep53 directions | find way towards turn left right up down along over through into | 2:08 |
| ep54 animal traits | size big small cute brave funny humorous smart stupid silly though | 2:03 |
| ep55 exams | exam(examination) test preparation know start finish question answer guess right wrong correct grade level | 2:12 |
| ep56 holiday | holiday general relaxing trip away picnic suppose festival during visit(visitor) come(came) together | 2:11 |
| ep57 travel | vacation travel agent passport hotel tour guide palace museum tower island beach map | 2:04 |
| ep58 feelings (2) | feelings enjoy comfortable pleasant happiness unhappiness miss separate regret shame pity hate | 2:19 |
| ep59 order | order first … tenth next last | 2:01 |
| ep60 months | month date in January … December | 2:22 |
| ep61 fruit & vegetables | fruit apple banana grape pear lemon strawberry watermelon vegetable potato carrot tomato onion bean cabbage except | 2:44 |
| ep62 subjects | study many subject math science chemistry lab experiment history geography art | 2:06 |
| ep63 reading | textbook topic language translate pronunciation diction fiction classic theme hero heroine courage | 2:02 |
| ep64 jobs (2) | jobs farmer fisherman postman trader clerk performer actor actress director musician guitarist violinist pianist drummer | 2:31 |
| ep65 health | health healthy advise advice exercise active fit fat keep habit | 1:50 |
| ep66 sleep | sleep asleep wake awake rest diary suggest suggestion main more less hardly even | 2:10 |
| ep67 competition | activity competition score player cheer dream win(won) lose(lost) winner prize luck lucky | 2:16 |
| ep68 illness | hospital sick ill illness fever cough flu spread medicine heart beat | 2:07 |
| ep69 measures (2) | weight kilo ton height meter length kilometer mile hole deep narrow wide at least almost | 2:17 |
| ep70 positions | position on under below inside outside front back in front of behind beside between around against | 2:14 |
