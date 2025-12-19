
## 《青春的抉择》
## 大学恋爱 × 成长叙事（可多周目）

## ================== 素材放置说明（把文件放到 game/images/） ==================
## 你需要准备的素材（推荐 PNG/JPG，分辨率按 1920x1080 背景、立绘 800~1200 高）：
##
## 背景（在剧情里用法：scene bg xxx）：
## - game/images/bg/dormitory.png        宿舍（上床下桌）
## - game/images/bg/corridor.png         宿舍走廊/楼道
## - game/images/bg/lecture_hall.png     大讲堂/报告厅
## - game/images/bg/classroom.png        教室（数学课）
## - game/images/bg/cafeteria.png        食堂
## - game/images/bg/library.png          图书馆
## - game/images/bg/basketball_court.png 篮球场
## - game/images/bg/campus_garden.png    校园草坪/迎新棚子附近
## - game/images/bg/cafe.png             咖啡馆/小店
## - game/images/bg/morning.png          时间氛围：清晨/白天（可选，用纯色也行）
## - game/images/bg/sunset.png           时间氛围：傍晚（可选）
## - game/images/bg/night.png            时间氛围：夜晚（可选）
##
## 立绘（在剧情里用法：show yuqing happy / show shiyun elegant / show haoran happy）：
## - game/images/ch/yuqing/happy.png     苏雨晴-开心
## - game/images/ch/yuqing/shy.png       苏雨晴-害羞
## - game/images/ch/yuqing/sad.png       苏雨晴-难过
## - game/images/ch/yuqing/thinking.png  苏雨晴-思考
## - game/images/ch/shiyun/elegant.png   江诗韵-淡定/优雅
## - game/images/ch/shiyun/shy.png       江诗韵-有点害羞
## - game/images/ch/shiyun/happy.png     江诗韵-开心
## - game/images/ch/haoran/happy.png     陈浩然-开心
## - game/images/ch/haoran/excited.png   陈浩然-兴奋
## - game/images/ch/haoran/serious.png   陈浩然-认真
##
## 可选音频（如果你愿意加氛围感）：
## - game/audio/bgm/main_menu.ogg        标题界面 BGM（在 options.rpy 里启用）
## - game/audio/bgm/campus_day.ogg       校园日常
## - game/audio/bgm/library_night.ogg    图书馆夜聊
## - game/audio/sfx/message.ogg          手机提示音
## ============================================================================

## ========== 角色定义 ==========
define mc = Character("[player_name]", color="#3498db")
define 雨晴 = Character("苏雨晴", color="#e74c3c")
define 浩然 = Character("陈浩然", color="#2ecc71")
define 诗韵 = Character("江诗韵", color="#f39c12")
define 教授 = Character("李教授", color="#9b59b6")
define 辅导员 = Character("王辅导员", color="#34495e")
define 室友1 = Character("室友小王", color="#7f8c8d")
define 室友2 = Character("室友小李", color="#95a5a6")

## ========== 变量 ==========
default player_name = "林川"
default player_gender = "男"  # 固定男主

default 专业选择 = "未选择"      # 计算机 / 经管 / 数学
default 社团路线 = "未加入"      # 文学社 / 篮球社 / 建模协会
default 住宿选择 = "上床下桌"

default 好感度_雨晴 = 0
default 好感度_诗韵 = 0

default 学习分数 = 50
default 社交分数 = 50
default 创造力 = 50
default 体力 = 80
default 金钱 = 500

default day = 1
default week = 1
default 时段 = "早晨"

default 已完成_报到 = False
default 已完成_社团招新 = False
default 已完成_图书馆事件 = False
default 已完成_篮球场事件 = False
default 已完成_沙龙事件 = False

## ========== 素材绑定（把占位替换为你的图片文件） ==========
## 背景：把对应图片放进 game/images/bg/，文件名按下方写。
image bg dormitory = "images/bg/dormitory.jpg"        # 宿舍
image bg corridor = "images/bg/corridor.jpg"         # 走廊
image bg lecture_hall = "images/bg/lecture_hall.jpg" # 报告厅
image bg classroom = "images/bg/classroom.jpg"       # 教室
image bg cafeteria = "images/bg/cafeteria.jpg"       # 食堂
image bg library = "images/bg/library.jpg"           # 图书馆
image bg basketball_court = "images/bg/basketball_court.jpg" # 篮球场
image bg campus_garden = "images/bg/campus_garden.jpg"       # 校园草坪/迎新
image bg cafe = "images/bg/cafe.jpg"                 # 咖啡馆

## 时间氛围背景（可选；没素材就用同名图片做简单渐变也行）
image bg morning = "images/bg/morning.jpg"           # 清晨/白天
image bg sunset = "images/bg/sunset.jpg"             # 傍晚
image bg night = "images/bg/night.jpg"               # 夜晚

## 立绘：把对应图片放进 game/images/ch/...，文件名按下方写。
image yuqing happy = "images/ch/yuqing/happy.png"        # 雨晴-开心
image yuqing shy = "images/ch/yuqing/shy.png"            # 雨晴-害羞
image yuqing sad = "images/ch/yuqing/sad.png"            # 雨晴-难过
image yuqing thinking = "images/ch/yuqing/thinking.png"  # 雨晴-思考

image haoran happy = "images/ch/haoran/happy.png"        # 浩然-开心
image haoran excited = "images/ch/haoran/excited.png"    # 浩然-兴奋
image haoran serious = "images/ch/haoran/serious.png"    # 浩然-认真

image shiyun elegant = "images/ch/shiyun/elegant.png"    # 诗韵-优雅
image shiyun shy = "images/ch/shiyun/shy.png"            # 诗韵-害羞
image shiyun happy = "images/ch/shiyun/happy.png"        # 诗韵-开心


## ========== 音乐工具（自动选择可用格式） ==========
init python:
    def pick_bgm(stem):
        """Return a loadable BGM path under audio/bgm/ for the given filename stem.

        Example: pick_bgm("campus_day") -> "audio/bgm/campus_day.flac" (or .ogg/.mp3)
        """

        candidates = [
            "audio/bgm/%s.ogg" % stem,
            "audio/bgm/%s.mp3" % stem,
            "audio/bgm/%s.flac" % stem,
            "audio/bgm/%s.wav" % stem,
        ]

        for path in candidates:
            if renpy.loadable(path):
                return path

        # Not found.
        return None

    def play_bgm(stem, fadeout=0.0, fadein=0.0, loop=True):
        """Play BGM from audio/bgm/ by filename stem (no extension).

        Ren'Py statements don't support `expression` here, so we do it in Python.
        """

        path = pick_bgm(stem)
        if not path:
            return

        # 如果当前正在播放同一首，就不要反复重播。
        try:
            current = renpy.music.get_playing(channel="music")
        except Exception:
            current = None
        if current == path:
            return

        # Prefer a single call if supported, otherwise fall back.
        try:
            renpy.music.play(path, channel="music", loop=loop, fadein=fadein, fadeout=fadeout)
            return
        except TypeError:
            pass

        if fadeout:
            try:
                renpy.music.stop(channel="music", fadeout=fadeout)
            except TypeError:
                renpy.music.stop(channel="music")

        try:
            renpy.music.play(path, channel="music", loop=loop, fadein=fadein)
        except TypeError:
            renpy.music.play(path, channel="music", loop=loop)


## ========== 工具标签 ==========
label show_status:
    ""
    "（你把一天的杂音收进抽屉，准备继续往前。）"
    return

## ========== 游戏开始 ==========
label start:

    scene bg night with fade

    $ play_bgm("decision", fadein=1.0)

    "高考结束后的第七天，夜里闷得发烫。"
    "你躺在床上，手机屏幕反复亮起：同学群、招生直播、志愿填报教程。"

    "你做了个梦。"
    "梦里有人把选择题一页页翻给你看，却不让你写答案。"
    "你猛地坐起，心跳像还贴在耳膜上。"

    scene bg morning with dissolve

    $ play_bgm("daily_life", fadeout=1.0, fadein=1.0)

    "第二天一早，你坐在电脑前。"
    "标题栏写着：‘普通高校招生志愿填报系统’。"

    $ player_name = renpy.input("请输入男主名字：", default=player_name)
    $ player_name = player_name.strip() or "林川"

    mc "……填志愿啊。"
    mc "原来人生真的会被一个下拉框改变。"

    "你打开一张纸，上面写着家里人给的建议：‘稳’。"
    "旁边还有班主任发来的语音转文字：‘别冲，先上车。’"

    "你盯着‘稳’这个字，忽然想起考场最后一题。"
    "你当时写下的，不是答案，是一种赌——赌自己能把不确定握在手里。"

    menu:
        "你在键盘前停了很久。最终，你更像谁？"

        "像父母（把风险压到最低）":
            $ 社交分数 += 1
            "你告诉自己：先把路走通，再谈风景。"

        "像老师（把选择当成策略）":
            $ 学习分数 += 2
            "你开始列清单：分数、梯度、保底、冲刺。"

        "像自己（把选择当成宣言）":
            $ 创造力 += 2
            "你承认：你也想要一次不被安排的决定。"

    menu:
        "你最终把第一志愿写成了："

        "中国矿业大学 · 数学类":
            $ 专业选择 = "数学"
            $ 学习分数 += 12
            $ 创造力 += 4
            $ 社交分数 -= 1

        "中国矿业大学 · 计算机类":
            $ 专业选择 = "计算机"
            $ 学习分数 += 10
            $ 创造力 += 2

        "中国矿业大学 · 经管类":
            $ 专业选择 = "经管"
            $ 社交分数 += 6
            $ 学习分数 += 4

    "提交按钮按下去的一瞬间，你反而有点空。"
    "像把一个版本的自己，交给了未来的随机数。"

    "——几周后。"
    "录取结果出来了。"

    scene bg night with dissolve

    "你盯着屏幕上的那行字，心跳越来越快。"
    "‘中国矿业大学 录取。’"

    "你没有大喊，也没有流泪，只是长长呼出一口气。"

    scene bg morning with dissolve

    "开学报到日。"
    mc "走吧，[player_name]。"

    jump day1_gate

## ========== Day 1：报到与相遇 ==========
label day1_gate:

    $ day = 1
    $ 时段 = "早晨"

    scene bg campus_garden with fade

    $ play_bgm("campus_day", fadeout=1.0, fadein=1.0)

    "迎新棚子一排排搭在草坪边，志愿者的嗓子已经喊到沙哑。"
    "你排队领资料袋，手心全是汗。"
    "棚子后面挂着横幅：‘欢迎来到中国矿业大学’。你读了两遍，才相信这不是梦。"

    menu:
        "你最担心的是什么？"

        "选错专业，走弯路":
            $ 学习分数 += 5
            $ 创造力 -= 2
            "你在心里默背‘可迁移技能’四个字，像在给自己打气。"

        "交不到朋友，被落下":
            $ 社交分数 += 5
            "你逼自己抬头看人群，试图记住每一张脸。"

        "经济压力，撑不住":
            $ 金钱 -= 0
            $ 学习分数 += 3
            "你把奖学金和兼职信息点开又关上。"
            "你发现自己甚至会下意识去算：一学期餐费、电话费、车费——每一项都像一道隐形题。"

    "你刚拿到宿舍钥匙，一个女生匆匆从你身边跑过——"

    show yuqing sad at center with dissolve

    雨晴 "对不起！我迟到了——"

    "她的资料袋擦过你的手臂，几张表格落在地上。"

    menu:
        "你怎么做？"

        "帮她捡起表格":
            jump day1_help_yuqing

        "提醒她慢点，别摔":
            jump day1_warn_yuqing

        "先顾自己，继续排队":
            jump day1_ignore_yuqing

label day1_help_yuqing:

    mc "我来吧。"
    "你蹲下把表格一张张捡起，发现其中一张是‘新生奖助申请意向表’。"

    show yuqing shy

    雨晴 "谢谢你……我叫苏雨晴。中文系。"
    mc "[player_name]。刚来报到。"

    "她犹豫了一下，声音放轻。"
    show yuqing thinking
    雨晴 "你也觉得……大学的第一步特别像一场分流吗？"

    $ 好感度_雨晴 += 10
    $ 社交分数 += 5

    jump day1_choose_major

label day1_warn_yuqing:

    mc "慢点，小心摔。"
    show yuqing shy
    雨晴 "嗯……谢谢。"

    $ 好感度_雨晴 += 6

    jump day1_choose_major

label day1_ignore_yuqing:

    "你下意识往前走了一步。"
    "可脚下的一张表格还在风里翻页。"

    $ 好感度_雨晴 -= 2
    $ 学习分数 += 2

    jump day1_choose_major

label day1_choose_major:

    scene bg corridor with fade

    if 专业选择 != "未选择":
        "资料袋里夹着‘专业方向确认’。"
        "你的第一志愿已经写过答案： [专业选择]。"
        "你只需要在报到表上再签一次名。"
        $ 已完成_报到 = True
        jump day1_dorm

    "资料袋里夹着‘专业方向确认’。你必须今天做出选择。"

    menu:
        "你选择的方向是？"

        "计算机（理工，硬核但踏实）":
            $ 专业选择 = "计算机"
            $ 学习分数 += 10
            $ 创造力 += 2

        "经管（资源与规则，现实感强）":
            $ 专业选择 = "经管"
            $ 社交分数 += 6
            $ 学习分数 += 4

        "数学（抽象与严谨，越学越清醒）":
            $ 专业选择 = "数学"
            $ 学习分数 += 12
            $ 创造力 += 4
            $ 社交分数 -= 1

    "你签下名字那一刻，像把未来某一段路封死，又把另一段路打开。"
    $ 已完成_报到 = True

    jump day1_dorm

label day1_dorm:

    scene bg dormitory with fade

    "宿舍楼里弥漫着新床垫和洗衣粉味。"
    "上床下桌的木板与金属架在灯下泛着冷光。"

    室友1 "新来的？我小王，隔壁市的。"
    室友2 "小李。上床下桌，默认都是上铺。你想坐靠窗那张桌子吗？"

    menu:
        "你怎么选宿舍位置？"

        "靠窗桌位":
            $ 住宿选择 = "上床下桌-靠窗桌位"
            $ 学习分数 += 2
            "你把台灯放在桌角，窗外的风把窗帘轻轻顶起。"

        "靠门桌位":
            $ 住宿选择 = "上床下桌-靠门桌位"
            $ 社交分数 += 2
            "你离门更近，室友进进出出，你总能第一时间知道消息。"

        "中间桌位":
            $ 住宿选择 = "上床下桌-中间桌位"
            $ 体力 += 2
            "你把箱子推到床下，决定先把日子过顺。"

    "晚上还没开始，你已经觉得自己像跑了半马。"

    jump day1_lunch

label day1_lunch:

    $ 时段 = "中午"

    scene bg cafeteria with fade

    "食堂里热得像开了高压锅。"
    "你端着餐盘找座位。"

    "雨晴坐在靠窗的位置，手指还夹着一张表格。"
    "另一边，一个男生冲你挥手，像跟你认识很久一样。"

    show haoran happy at right with dissolve
    show yuqing happy at left with dissolve

    浩然 "嘿，新同学！我陈浩然，体育学院的。来这边！"
    雨晴 "[player_name]……这边也有位置。"

    "不远处，社团招新的声音一阵高过一阵。"

    menu:
        "你去哪边坐？"

        "坐雨晴旁边":
            hide haoran
            jump day1_lunch_yuqing

        "坐浩然那边":
            hide yuqing
            jump day1_lunch_haoran

        "自己吃，观察环境":
            hide yuqing
            hide haoran
            jump day1_lunch_alone

label day1_lunch_yuqing:

    show yuqing thinking at center with dissolve

    mc "你刚才在填什么？"
    雨晴 "奖助申请意向表。"
    "她抿了抿唇。"
    雨晴 "我不是想要谁可怜，只是……我必须把生活算清楚。"

    menu:
        "你怎么回应？"

        "认真支持":
            mc "这不是丢人的事。你很勇敢。"
            $ 好感度_雨晴 += 10
            $ 社交分数 += 5

        "转移话题":
            mc "食堂的辣子鸡看起来不错。"
            $ 好感度_雨晴 += 2

        "分享自己的压力":
            mc "我也有压力。只是方式不一样。"
            $ 好感度_雨晴 += 6
            $ 学习分数 += 3

    "窗外的光落在她的睫毛上，你忽然意识到：大学不是只和自己较劲。"

    "你们端着餐盘站起来时，她忽然低声补了一句。"
    show yuqing shy
    雨晴 "其实……我也不是一直都这么‘算’。"
    雨晴 "只是有些东西没人替你兜底，你就会变得特别认真。"

    menu:
        "你怎么接她的话？"

        "说你理解":
            $ 好感度_雨晴 += 3
            mc "我懂。认真不是冷漠，是你在保护自己。"

        "说点轻松的":
            $ 好感度_雨晴 += 2
            mc "那我们先从‘把饭吃完’开始保护自己。"
            "她愣了愣，终于笑了一下。"

        "邀请她一起走走":
            $ 好感度_雨晴 += 4
            mc "吃完要不要在校园里转转？我怕我等会儿就迷路。"
            雨晴 "……好啊。"

    jump day1_afternoon

label day1_lunch_haoran:

    show haoran excited at center with dissolve

    浩然 "你专业选了啥？"
    mc "[专业选择]。"
    浩然 "行！以后有事找我，球场上我罩你。"

    menu:
        "你要不要和他约训练？"

        "约一场（拓展圈子）":
            $ 社交分数 += 10
            $ 体力 -= 5
            $ 好感度_诗韵 += 0
            "你们约好明天下午去球场。"

        "婉拒（先稳学习）":
            $ 学习分数 += 5
            "你笑着说以后再约。"

    jump day1_afternoon

label day1_lunch_alone:

    "你找了个角落。"
    "餐盘里热气往上冒，你却没什么胃口。"

    "隔壁桌压低声音：‘社团招新挺卷的。’"
    "另一人接话：‘别急，先把军训熬过去。’"
    "第三个人笑了一声：‘新生第一周的目标：别迷路、别迟到、别把卡丢了。’"

    "你本能想装作没听见，却还是忍不住跟着笑了一下。"

    $ 学习分数 += 4
    $ 社交分数 += 2

    jump day1_afternoon

label day1_afternoon:

    $ 时段 = "下午"

    scene bg campus_garden with fade

    "下午的阳光很硬，照得你有点恍惚。"
    "你可以选择把时间花在哪儿。"

    menu:
        "去图书馆":
            jump day1_library

        "去篮球场":
            jump day1_court

        "回宿舍休整":
            jump day1_back_dorm

label day1_library:

    scene bg library with fade

    $ play_bgm("library_night", fadeout=1.0, fadein=1.0)

    "书页翻动的声音像海。"
    "你在书架间走，听见有人轻轻哼歌。"
    "那旋律很短，却像一条线，把你从嘈杂里牵出来。"

    show shiyun elegant at center with dissolve

    诗韵 "你也喜欢在这里躲开热闹？"
    mc "算是。"
    诗韵 "江诗韵。艺术学院。"

    "她说‘艺术学院’时，语气很轻，像怕被误解成某种标签。"
    "你注意到她手指上有点颜料的淡痕——像是刚洗过，却没洗干净。"

    menu:
        "你对她的第一印象？"

        "她很耀眼":
            $ 好感度_诗韵 += 8
            $ 创造力 += 5

        "她看起来有点孤独":
            $ 好感度_诗韵 += 6
            $ 社交分数 += 3

        "保持距离":
            $ 学习分数 += 5

    "你们聊到‘大学里最难的是坚持’。"
    "你们聊到‘大学里最难的是坚持’。"
    "你说起高考后的空落，她却说：‘空落也算一种开始。’"

    menu:
        "你顺着话题问："

        "‘你为什么想做这个展？’":
            $ 好感度_诗韵 += 2
            诗韵 "因为我不想装作‘大家都没事’。"
            诗韵 "我想让人承认：焦虑也可以被摆在桌面上。"

        "‘你平时就这么安静吗？’":
            $ 社交分数 += 2
            诗韵 "我不是安静。"
            诗韵 "我是在挑选值得说的话。"

        "‘你会不会也会怕？’":
            $ 好感度_诗韵 += 3
            show shiyun shy
            诗韵 "会啊。"
            诗韵 "怕别人看见我很用力，怕别人说我矫情。"
            诗韵 "但更怕……我什么都不做。"

    "她递给你一张展览海报。"
    诗韵 "有空来看看。别只活在绩点里。"

    "你把海报夹进书里，纸边蹭到指腹。那一瞬间你忽然很确定：这张纸会在未来某天变重。"

    $ 已完成_图书馆事件 = True

    jump day1_evening

label day1_court:

    scene bg basketball_court with fade

    show haoran excited at center with dissolve

    浩然 "来得正好！"
    "你被拉进一场临时对抗。"

    menu:
        "你怎么打？"

        "拼（燃起来）":
            $ 体力 -= 15
            $ 社交分数 += 8
            $ 好感度_雨晴 += 0
            $ 已完成_篮球场事件 = True
            "汗水糊住眼睛，你却笑了。"

        "稳（不逞强）":
            $ 体力 -= 8
            $ 学习分数 += 2
            $ 社交分数 += 5
            $ 已完成_篮球场事件 = True

        "看（先熟悉）":
            $ 社交分数 += 4
            $ 已完成_篮球场事件 = True

    jump day1_evening

label day1_back_dorm:

    scene bg dormitory with fade

    "你躺了十分钟，身体像终于落地。"
    $ 体力 += 10

    "室友小王把行李箱一拍：‘我先声明，晚上打游戏不开麦。’"
    "室友小李在床底找半天，掏出一个插线板：‘桌位就这么点，咱们得分配一下。’"

    menu:
        "宿舍里第一件小事，你更愿意怎么处理？"

        "主动提出规则（省得以后别扭）":
            $ 社交分数 += 3
            mc "那我们先说好：熄灯后外放别太大，卫生轮流，插线板谁都能用。"
            室友1 "行，兄弟靠谱。"
            室友2 "可以，写个小纸条贴门后？"

        "先观察一下（不急着当‘班长’）":
            $ 学习分数 += 2
            "你没急着开口，只把自己的桌面收得很干净。"
            "你想：日子还长，很多事不必第一天就定死。"

        "开个玩笑缓和气氛":
            $ 创造力 += 2
            mc "规则先不急，我的底线只有一个：别把我泡面当公共财产。"
            室友1 "哈哈哈，懂，泡面就是尊严。"

    "手机亮起：班级群里一串新消息。"
    "有人在问：‘军训怎么分连？’，有人在晒‘校园卡到手’。"
    "你跟着刷了几条，忽然觉得这就是大学：琐碎、热闹、真实。"

    jump day1_evening

label day1_evening:

    $ 时段 = "晚上"

    scene bg sunset with fade

    $ play_bgm("campus_evening", fadeout=1.0, fadein=1.0)

    "傍晚的风把白天的喧嚣吹散。"
    "你忽然想起梦里那句：‘先学会选择。’"

    menu:
        "你今晚怎么安排？"

        "去听学术沙龙":
            jump day1_salon

        "去咖啡馆写计划":
            jump day1_cafe

        "回宿舍早睡":
            jump day1_sleep

label day1_salon:

    scene bg classroom with fade

    "教室里坐着不多的人，投影写着：‘信息差与选择成本’。"

    "主持人是研究生学长，语速很快，像怕被人打断。"
    "他先讲‘怎么选课’、‘怎么跟老师沟通’，再讲‘怎么从失败里爬出来’。"

    menu:
        "你在沙龙里的表现？"

        "提出问题":
            mc "如果规则被人利用，普通人还能怎么选？"
            $ 学习分数 += 10
            "学长愣了半秒，随即笑着把话题拉回：‘所以更要把基本功打扎实。’"
            "他没回避你的尖锐，但也没让气氛变沉。"

        "认真记录":
            "你把每个关键词都记下来。"
            $ 学习分数 += 8

    "散场时，学长把几张讲义留在讲台边：‘如果你愿意把问题写下来，我们会在下一次认真回答。’"
    "你拿了一张，纸有点薄，却很干净。"
    $ 已完成_沙龙事件 = True

    jump day1_end

label day1_cafe:

    scene bg cafe with fade

    "咖啡馆的灯很柔。"
    "你摊开本子写下：‘大学四年我想成为什么样的人。’"

    menu:
        "你写下的第一句话是："

        "我要更强":
            $ 学习分数 += 6
            $ 创造力 += 2

        "我要更自由":
            $ 创造力 += 8

        "我要更可靠":
            $ 社交分数 += 6

    "你写着写着，手机又亮了一次。"
    "是室友发来的：‘明早一起去领军训服不？’"

    jump day1_end

label day1_sleep:

    scene bg night with fade

    $ play_bgm("library_night", fadeout=1.0, fadein=1.0)

    "你决定先睡。"
    "可关灯前，你还是看了一眼窗外——校园的灯像一排排小坐标，安静地亮着。"
    $ 体力 += 15

    jump day1_end

label day1_end:

    scene bg night with fade
    "【第一天结束】"
    call show_status from _call_show_status

    menu:
        "进入第二天":
            jump day2_morning

        "直接查看结局":
            jump ending_selection

        "结束游戏":
            jump game_end

## ========== Day 2：选择与代价 ==========
label day2_morning:

    $ day = 2
    $ 时段 = "早晨"

    scene bg dormitory with fade

    $ play_bgm("daily_life", fadeout=1.0, fadein=1.0)

    "第二天早晨。"
    "昨晚的沙龙讲义和你写的计划，像两只手，分别把你往不同方向拉。"

    menu:
        "你今天优先做什么？"

        "去图书馆":
            jump day2_library

        "去找雨晴":
            jump day2_yuqing

        "去球场":
            jump day2_court

        "去上数学课":
            jump day2_math

label day2_math:

    scene bg lecture_hall with fade

    "你走进阶梯教室，黑板上已经写满符号。"
    "粉笔灰像细小的雪，落在讲台边。"

    教授 "同学们，数学不是算出来的，是证明出来的。"

    "你翻开笔记本，标题写着：‘数学分析（I）’。"

    if 专业选择 == "数学":
        "这不是你第一次面对它，但你依然会在‘极限’两个字前停顿。"
        $ 学习分数 += 8
        $ 创造力 += 3
        "你忽然想起高考那天，监考老师把卷子翻过来时的声音。"
        "原来很多‘开始’，只是把熟悉换一种更残酷的写法。"
    else:
        "你听得懂一半，另一半像雾。你忽然理解：每个专业都有自己的‘语言’。"
        $ 学习分数 += 4

    "下课时，走廊里贴着一张社团招新：‘数学建模协会｜新生体验赛’。"
    "有人在海报旁边写了句吐槽：‘不会建模也能来，主要是会熬夜。’"
    "你看完没忍住笑了，突然没那么紧张了。"

    menu:
        "你怎么选？"

        "报名体验赛":
            $ 学习分数 += 6
            $ 创造力 += 6
            $ 社交分数 += 2
            if 社团路线 == "未加入":
                $ 社团路线 = "建模协会"
            "你把名字写在报名表上，突然有点兴奋。"

        "先旁听，不报名":
            $ 学习分数 += 3
            "你拍下海报，打算回去再研究。"

        "无视":
            $ 体力 += 2
            "你揉了揉眉心，决定先把课业稳住。"

    "你手机震了一下。"
    "是教务系统的提醒：‘请及时完成课程测验。’"

    jump day2_evening

label day2_library:

    scene bg library with fade

    $ play_bgm("library_night", fadeout=1.0, fadein=1.0)

    show shiyun shy at center with dissolve

    诗韵 "你真的来了。"
    mc "你说过：别只活在绩点里。"

    "她带你看展览策划草案。"
    诗韵 "我想做一场‘新生的焦虑’主题。可他们说不够‘正能量’。"

    menu:
        "你建议她怎么做？"

        "坚持表达":
            $ 创造力 += 10
            $ 好感度_诗韵 += 10
            mc "真实不是负能量。真实是起点。"

        "折中表达":
            $ 创造力 += 5
            $ 学习分数 += 3
            $ 好感度_诗韵 += 6
            mc "把锋芒藏一点，先让作品落地。"

        "让她放弃":
            $ 社交分数 += 2
            $ 好感度_诗韵 -= 2
            mc "别硬碰硬。你会更难受。"

    jump day2_evening

label day2_yuqing:

    scene bg cafeteria with fade

    show yuqing thinking at center with dissolve

    "你在食堂二楼找到雨晴。她盯着手机，眉头紧。"

    雨晴 "我妈说……不想我申请助学。"
    雨晴 "她觉得丢脸。"

    menu:
        "你怎么陪她？"

        "尊重她的决定":
            $ 好感度_雨晴 += 8
            mc "这是你的人生。你想怎么做都可以。"

        "鼓励她争取":
            $ 好感度_雨晴 += 10
            $ 学习分数 += 3
            mc "申请不是乞讨，是制度给你的权利。"

        "转移注意":
            $ 好感度_雨晴 += 4
            mc "先吃饭。饿着做决定更糟。"

    "她忽然把手机翻过来给你看："
    "——一条来自家里的长语音转文字：‘别申请助学金，咱家丢不起这个脸。’"
    "她指尖发抖，又强迫自己把屏幕按灭。"

    "你们沉默了一会儿。食堂的嘈杂像隔了一层玻璃。"

    menu:
        "你更想给她什么？"

        "给她一个方案":
            $ 好感度_雨晴 += 2
            $ 学习分数 += 2
            mc "要不这样：你先把材料准备好，递不递交你最后决定。"
            mc "但至少别让‘怕丢脸’替你做决定。"

        "给她一个拥抱":
            $ 好感度_雨晴 += 3
            "你没说太多，只把纸巾推到她手边。"
            "她吸了吸鼻子，声音很轻。"
            雨晴 "谢谢……我其实就想有人站在我这边一会儿。"

        "给她一点轻松":
            $ 好感度_雨晴 += 1
            mc "这家糖醋里脊真的很能‘拯救情绪’。"
            "她嘴角动了动，像在努力把自己拉回现实。"

    jump day2_evening

label day2_court:

    scene bg basketball_court with fade

    show haoran excited at center with dissolve

    浩然 "说好的训练！"
    "你跑动、传球、投篮，呼吸像被重置。"

    menu:
        "训练后你选择："

        "继续加练":
            $ 体力 -= 20
            $ 社交分数 += 6
            $ 学习分数 += 2

        "结束去吃饭":
            $ 体力 -= 10
            $ 社交分数 += 5

    "浩然压低声音："
    show haoran serious
    浩然 "我跟你说个现实点的：有些社团挺卷的，别把自己逼太狠。"
    浩然 "先把身体练出来，心态也会跟着稳。"

    jump day2_evening

label day2_evening:

    scene bg sunset with fade

    $ play_bgm("campus_evening", fadeout=1.0, fadein=1.0)

    "傍晚。"
    "你心里装着几种情绪：对未来的兴奋、对现实的焦虑、对自我的怀疑。"
    "它们之间说不清逻辑，却真实得像呼吸。"

    menu:
        "你今晚想怎么收尾？"

        "去操场散步":
            jump day2_walk

        "回宿舍学习":
            jump day2_study

label day2_walk:

    scene bg campus_garden with fade

    "操场灯很亮，跑道上有人一圈圈坚持。"
    "你走得很慢，听见远处的口号、笑声、鞋底摩擦地面的声音。"

    "看台下有人在卖水，喇叭里播着校歌的伴奏，听起来有点‘土’，却莫名踏实。"

    menu:
        "你更想把谁的影子留在今晚？"

        "给雨晴发一句‘你还好吗’":
            jump day2_walk_yuqing

        "去图书馆门口等诗韵":
            jump day2_walk_shiyun

        "谁也不找，只跟自己说话":
            jump day2_walk_alone

label day2_walk_yuqing:

    scene bg campus_garden with fade

    "你站在跑道边，掏出手机，把输入框里的那句‘你还好吗’删了三次。"
    "最后你只发了四个字：‘回宿舍了吗？’"

    "她回得很快。"
    show yuqing thinking at center with dissolve
    雨晴 "在。"
    雨晴 "刚才在食堂……我有点失态。"

    menu:
        "你怎么回？"

        "说你一直在":
            $ 好感度_雨晴 += 2
            mc "没事。你不需要一直坚强。"
            mc "我在。"

        "说点具体的明天":
            $ 好感度_雨晴 += 1
            $ 学习分数 += 1
            mc "明天领军训服，我和室友一起去。"
            mc "你要是不想一个人去，我可以顺路等你。"
            show yuqing shy
            雨晴 "……好。谢谢。"

        "用玩笑把气氛拉回来":
            $ 好感度_雨晴 += 1
            mc "我刚才差点在操场迷路。"
            mc "你看，人生已经够难了，先别和自己过不去。"
            "她那边沉默两秒，发来一个很小的‘嗯’。"

    "你把手机放回兜里，风从操场中央穿过去。"
    "你忽然明白：陪伴不是替人解决问题，是让人有力气去解决。"
    $ 体力 += 4

    jump ending_selection

label day2_walk_shiyun:

    scene bg library with fade

    "你绕到图书馆门口。台阶边坐着几个人，抱着刚借的书，像抱着某种新的开始。"

    show shiyun elegant at center with dissolve
    诗韵 "你怎么跑这儿来了？"
    mc "突然想把白天没说完的话说完。"

    "她把海报从包里抽出来，边角被压得有点皱。"

    menu:
        "你想聊什么？"

        "聊展览":
            $ 好感度_诗韵 += 2
            $ 创造力 += 2
            mc "你写的主题很准。"
            mc "如果他们怕‘不正能量’，就把‘焦虑’写成‘自我调适’。"
            show shiyun shy
            诗韵 "你这算不算……用你的方式替我撑一下？"
            mc "算。"
            "她笑得很轻，像怕把情绪吓跑。"

        "聊你自己":
            $ 好感度_诗韵 += 3
            mc "我其实也怕。"
            mc "怕选错课，怕跟不上，怕最后变成一个‘也就那样’的人。"
            诗韵 "那就允许自己也就那样一阵子。"
            诗韵 "人不是靠一天变厉害的。"

        "聊一点好笑的":
            $ 社交分数 += 2
            mc "我室友刚才说：泡面是尊严。"
            show shiyun happy
            诗韵 "那你的尊严是什么？"
            mc "我的尊严是——数学符号别写反。"
            "她笑出声，像终于松了一口气。"

    "你们并肩走了几步。"
    "夜色把图书馆的窗子照得很亮，像一格一格温柔的坐标。"
    $ 体力 += 3

    jump ending_selection

label day2_walk_alone:

    scene bg campus_garden with fade

    "你没有找任何人。"
    "你只是绕着操场外圈走，数着路灯的间距，像在给自己搭一个最简单的秩序。"

    "你忽然明白：所谓大学，并不是瞬间变强。"
    "是你开始学会和不确定共处，并且还能往前走。"
    $ 学习分数 += 2
    $ 体力 += 2

    jump ending_selection

label day2_study:

    scene bg dormitory with fade

    "你把书摊开，给自己定了一个小得不能再小的目标：把今天的公式推完。"
    "室友们还在聊天，你却第一次没那么在意别人怎么看你。"
    $ 学习分数 += 5

    jump ending_selection

## ========== 结局选择 ==========
label ending_selection:

    scene bg night with fade

    $ play_bgm("decision", fadeout=1.0, fadein=1.0)

    "时间快进。"
    "你在大学里做了很多选择。"

    if 好感度_雨晴 >= 22:
        jump ending_yuqing
    elif 好感度_诗韵 >= 22:
        jump ending_shiyun
    elif 学习分数 >= 70:
        jump ending_study
    else:
        jump ending_normal

label ending_yuqing:

    scene bg cafe with fade

    play music "audio/bgm/romance.mp3" fadeout 1.0 fadein 1.0
    show yuqing shy at center with dissolve

    "咖啡馆里，雨晴把一张申请结果单推到你面前。"
    雨晴 "我拿到了。"
    mc "恭喜。"

    "她眼睛有点红，却笑得很稳。"
    雨晴 "谢谢你。不是因为你替我做了决定，而是因为你让我相信——我可以。"

    "你忽然意识到，你们都在用不同方式对抗同一件事：被命运轻易定义。"

    "【结局：与你并肩的雨晴】"
    jump game_end

label ending_shiyun:

    scene bg library with fade

    play music "audio/bgm/romance.mp3" fadeout 1.0 fadein 1.0
    show shiyun happy at center with dissolve

    "展览开幕那天，人群在作品前停住。"
    "有人沉默，有人落泪，有人终于承认：‘焦虑不是羞耻。’"

    诗韵 "你看，真实也能被看见。"
    mc "你做到了。"

    "她把那张最初的草案翻到背面，你看到一行小字：‘把不可说的，换一种方式说出来。’"

    "【结局：被看见的诗韵】"
    jump game_end

label ending_study:

    scene bg classroom with fade

    教授 "[player_name]，你这学期做得不错。"
    "你拿到一次难得的项目机会。"

    "【结局：学业有成】"
    jump game_end

label ending_normal:

    scene bg campus_garden with fade

    "你没有成为谁的传奇，也没有跌进谁的深渊。"
    "你只是把日子过稳，把自己慢慢长出来。"

    "【结局：平凡但向上】"
    jump game_end

## ========== 游戏结束 ==========
label game_end:

    scene bg night with fade

    $ play_bgm("gameend", fadeout=1.0, fadein=1.0)

    "感谢游玩《青春的抉择》！"

    ""
    "【最终统计】"
    "姓名：[player_name]（男）"
    "专业：[专业选择]"
    "社团：[社团路线]"
    "（一些看不见的东西，在你每次犹豫与坚定里悄悄改变了。）"
    "你记得最清楚的不是某个瞬间，而是你没有停下。"

    menu:
        "重新开始":
            jump start
        "退出游戏":
            return

