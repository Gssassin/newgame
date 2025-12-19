# 项目导出

**文件数量**: 4  
**总大小**: 106.2 KB  
**Token 数量**: 23.3K  
**生成时间**: 2025/12/18 20:20:39

## 文件结构

```
📁 .
  📄 gui.rpy
  📄 options.rpy
  📄 screens.rpy
  📄 script.rpy
```

## 源文件

### gui.rpy

*大小: 16.3 KB | Token: 3.5K*

```text
################################################################################
## 初始化
################################################################################

## “init offset”语句可使此文件中的初始化语句在任何其他文件中的“init”语句之前运
## 行。
init offset = -2

## 调用 gui.init 会将样式重置为合理的默认值，并设置游戏的宽度和高度（基准分辨
## 率）。
init python:
    gui.init(1920, 1080)

## 启用对屏幕或变换中无效或不稳定属性的检查
define config.check_conflicting_properties = True


################################################################################
## GUI 配置变量
################################################################################


## 颜色 ##########################################################################
##
## 界面中文本的颜色。

## 整个界面中使用的强调色，用于标记和突出显示文本。
define gui.accent_color = '#00cc70f4'

## 当文本按钮既未被选中也未被悬停时使用的颜色。
define gui.idle_color = '#888888'

## 小的颜色用于小的文本，需要更亮/更暗才能达到同样的效果。
define gui.idle_small_color = '#aaaaaa'

## 当按钮和滑条被悬停时使用的颜色。
define gui.hover_color = '#66c1e0'

## 当文本按钮被选中但非焦点时使用的颜色。当一个按钮为当前屏幕或设置选项值时，会
## 处于选中状态。
define gui.selected_color = '#ffffff'

## 当文本按钮无法被选择时使用的颜色。
define gui.insensitive_color = '#8888887f'

## 滑条未填充的部分使用的颜色。这些颜色不直接使用，但在重新生成条形图像文件时使
## 用。
define gui.muted_color = '#003d51'
define gui.hover_muted_color = '#005b7a'

## 对话和菜单选择文本使用的颜色。
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'


## 字体和字体大小 #####################################################################

## 游戏内文本使用的字体。
define gui.text_font = "fonts/dialogue.ttf"

## 角色名称使用的字体。
define gui.name_text_font = "fonts/dialogue.ttf"

## 游戏外文本使用的字体。
define gui.interface_text_font = "fonts/interface.ttf"

## 普通对话文本的大小。
define gui.text_size = 33

## 角色名称的大小。
define gui.name_text_size = 45

## 游戏用户界面中文本的大小。
define gui.interface_text_size = 40

## 游戏用户界面中标签的大小。
define gui.label_text_size = 42

## 通知屏幕上文本的大小。
define gui.notify_text_size = 30

## 游戏标题的大小。
define gui.title_text_size = 90


## 标题和游戏菜单 #####################################################################

## 标题菜单和游戏菜单使用的图像。
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"

## 可选：自定义标题/菜单背景。
## 将检测放在较晚的 init 阶段，确保资源系统已就绪。
init 10 python:
    def _first_loadable(paths):
        for p in paths:
            if renpy.loadable(p):
                return p
        return None

    # 标题字体（直接指定，若缺失则回退界面字体）。
    title_font = _first_loadable([
        "fonts/title.ttf",
        "fonts/title.otf",
        "fonts/title.ttc",
        gui.interface_text_font,
    ])
    gui.title_font = title_font or gui.interface_text_font

    # 标题界面背景（覆盖 gui/main_menu.png）
    title_bg = _first_loadable([
        "images/bg/title.png",
        "images/bg/title.jpg",
        "images/bg/title.jpeg",
        "images/bg/title.webp",
    ])
    if title_bg:
        gui.main_menu_background = title_bg

    # 游戏菜单背景（按 ESC，覆盖 gui/game_menu.png）
    game_menu_bg = _first_loadable([
        "images/bg/game_menu.png",
        "images/bg/game_menu.jpg",
        "images/bg/game_menu.jpeg",
        "images/bg/game_menu.webp",
    ])
    if game_menu_bg:
        gui.game_menu_background = game_menu_bg


## 对话 ##########################################################################
##
## 这些变量控制对话如何在屏幕上逐行显示。

## 包含对话的文本框的高度。
define gui.textbox_height = 278

## 文本框在屏幕上的垂直位置。0.0 是顶部，0.5 是居中，1.0 是底部。
define gui.textbox_yalign = 1.0


## 叙述角色名字相对于文本框的位置。可以是从左侧或顶部起的整数像素，或设为 0.5 来
## 居中。
define gui.name_xpos = 360
define gui.name_ypos = 0

## 角色名字的水平对齐方式。0.0 为左侧对齐，0.5 为居中显示，而 1.0 为右侧对齐。
define gui.name_xalign = 0.0

## 包含角色名字的方框的宽度、高度和边框尺寸，或设为 None 来自动确定其大小。
define gui.namebox_width = None
define gui.namebox_height = None

## 包含角色名字的方框的边界尺寸，以左、上、右、下顺序排列。
define gui.namebox_borders = Borders(5, 5, 5, 5)

## 若为 True，则名字框的背景将平铺；若为 False，则名字框的背景将缩放。
define gui.namebox_tile = False


## 对话相对于文本框的位置。可以是相对于文本框从左侧或顶部起的整数像素，或设为
## 0.5 来居中。
define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75

## 对话文本的最大宽度，以像素为单位。
define gui.dialogue_width = 1116

## 对话文本的水平对齐方式。0.0 为左侧对齐，0.5 为居中显示，而 1.0 为右侧对齐。
define gui.dialogue_text_xalign = 0.0


## 按钮 ##########################################################################
##
## 这些变量以及 gui/button 中的图像文件控制着按钮显示方式。

## 按钮的宽度和高度像素数。如果为 None，则 Ren'Py 将计算大小。
define gui.button_width = None
define gui.button_height = None

## 按钮两侧的边框，按左、上、右、下的顺序排列。
define gui.button_borders = Borders(6, 6, 6, 6)

## 若为 True，则背景图像将平铺。若为 False，则背景图像将线性缩放。
define gui.button_tile = False

## 按钮使用的字体。
define gui.button_text_font = gui.interface_text_font

## 按钮所使用的文本大小。
define gui.button_text_size = gui.interface_text_size

## 按钮文本在各种状态下的颜色。
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## 按钮文本的水平对齐方式。（0.0 为左侧对齐，0.5 为居中对齐，而 1.0 为右侧对
## 齐）。
define gui.button_text_xalign = 0.0


## 这些变量覆盖了不同类型按钮的设置。关于可用的按钮种类以及每种按钮的用途，请参
## 阅 gui 文档。
##
## 这些定制由默认界面使用：

define gui.radio_button_borders = Borders(27, 6, 6, 6)

define gui.check_button_borders = Borders(27, 6, 6, 6)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)

define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## 您还可以通过添加正确命名的变量来添加自己的定制。例如，您可以将以下几行取消注
## 释来设置导航按钮的宽度。

# define gui.navigation_button_width = 250


## 选项按钮 ########################################################################
##
## 游戏内菜单使用的选项按钮。

define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#888888'
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = '#8888887f'


## 存档按钮 ########################################################################
##
## 存档按钮是一种特殊的按钮。它包含一个缩略图和描述该存档内容的文本。存档使用
## gui/button 中的图像文件，就像其他类型的按钮一样。

## 存档位按钮。
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## 存档所用缩略图的宽度和高度。
define config.thumbnail_width = 384
define config.thumbnail_height = 216

## 存档网格中的列数和行数。
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## 定位和间距 #######################################################################
##
## 这些变量控制各种用户界面元素的位置和间距。

## 导航按钮左侧相对于屏幕左侧的位置。
define gui.navigation_xpos = 60

## 快进指示器的垂直位置。
define gui.skip_ypos = 15

## 通知界面的垂直位置。
define gui.notify_ypos = 68

## 菜单选项之间的间距。
define gui.choice_spacing = 33

## 标题菜单和游戏菜单的导航部分中的按钮。
define gui.navigation_spacing = 6

## 控制设置项目之间的间隔量。
define gui.pref_spacing = 15

## 控制设置按钮之间的间距。
define gui.pref_button_spacing = 0

## 存档页面按钮之间的间距。
define gui.page_spacing = 0

## 存档按钮之间的间距。
define gui.slot_spacing = 15

## 标题菜单文本的位置。
define gui.main_menu_text_xalign = 1.0


## 框架 ##########################################################################
##
## 这些变量控制在不存在覆盖层或窗口时可以包含用户界面组件的框架的外观。

## 通用框架。
define gui.frame_borders = Borders(6, 6, 6, 6)

## 用作确认界面部分的框架。
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

## 用作快进界面部分的框架。
define gui.skip_frame_borders = Borders(24, 8, 75, 8)

## 用作通知界面部分的框架。
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

## 框架背景是否应平铺？
define gui.frame_tile = False


## 条，滚动条和滑块 ####################################################################
##
## 这些语句控制条，滚动条和滑块的外观和大小。
##
## 默认的 GUI 仅使用滑块和垂直滚动条。所有其他栏仅在创建者编写的屏幕中使用。

## 水平条，滚动条和滑块的高度。垂直条，滚动条和滑块的宽度。
define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38

## 若为 True，则条的底图平铺。若为 False，则条的底图线性缩放。
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## 水平边框。
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)

## 垂直边框。
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

## What to do with unscrollable scrollbars in the game menu. "hide" hides them,
## while None shows them.
define gui.unscrollable = "hide"


## 历史 ##########################################################################
##
## 历史记录屏幕显示玩家已经阅读过的对话。

## Ren'Py 将保留的对话历史块数。
define config.history_length = 250

## 历史屏幕条目的高度，或设置为 None 以使高度变量自适应。
define gui.history_height = 210

## 在历史记录屏幕条目之间添加额外的空间。
define gui.history_spacing = 0

## 所指定叙述角色的标签的坐标、宽度和对齐方式。
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

## 对话文本的坐标、宽度和对齐方式。
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0


## NVL 模式 ######################################################################
##
## NVL 模式屏幕显示 NVL 模式的角色所产生的对话。

## NVL 模式背景窗口的背景边框。
define gui.nvl_borders = Borders(0, 15, 0, 30)

## Ren'Py 所显示的 NVL 模式条目的最大数量。当要显示的条目多于此数量时，最旧的条
## 目将被删除。
define gui.nvl_list_length = 6

## NVL 模式条目的高度。将此设置为 None 可使条目动态调整高度。
define gui.nvl_height = 173

## 当 gui.nvl_height 为 None 时，NVL 模式条目之间的间距，以及 NVL 模式条目和 NVL
## 模式菜单之间的间距。
define gui.nvl_spacing = 15

## 所指定叙述角色的标签的坐标、宽度和对齐方式。
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

## 对话文本的坐标、宽度和对齐方式。
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

## nvl_thought 文本（由 nvl_narrator 字符表示的文本）的位置，宽度和对齐方式。
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

## NVL menu_buttons 的位置。
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0


## 本地化 #########################################################################

## 该变量控制允许在何时换行。默认值适用于大多数语言。可用的值请参见 https://
## www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"


################################################################################
## 移动设备
################################################################################

init python:

    ## 该变量增加快捷菜单按钮的尺寸来使它们在平板和手机上更容易被按到。
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(60, 21, 60, 0)

    ## 该变量更改各个 GUI 元素的尺寸和间距来确保它们在手机上更容易被辨识。
    @gui.variant
    def small():

        ## 字体大小。
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51

        ## 调整对话框的位置。
        gui.textbox_height = 360
        gui.name_xpos = 120
        gui.dialogue_xpos = 135
        gui.dialogue_width = 1650

        ## 更改各元素的尺寸和间距。
        gui.slider_size = 54

        gui.choice_button_width = 1860
        gui.choice_button_text_size = 45

        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15

        gui.history_height = 285
        gui.history_text_width = 1035

        gui.quick_button_text_size = 30

        ## 文件按钮布局。
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## NVL 模式。
        gui.nvl_height = 255

        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488

        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8

        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30

        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30
```

### options.rpy

*大小: 7.3 KB | Token: 1.3K*

```text
## 此文件包含有可自定义您游戏的设置。
##
## 以“##”开头的语句是注释，您不应该对其取消注释。以“#”开头的语句是注释掉的代码，
## 在适用的时候您可能需要对其取消注释。


## 基础 ##########################################################################

## 用户可读的游戏名称。此命令用来设置默认窗口标题，并且会在界面和错误报告中出
## 现。
##
## 带有 _() 的字符串表示其可被翻译。

define config.name = _("青春的抉择")


## 决定上面给出的标题是否显示在标题界面屏幕。设置为 False 来隐藏标题。

define gui.show_name = True


## 游戏版本号。

define config.version = "1.0"


## 放置在游戏内“关于”屏幕上的文本。将文本放在三个引号之间，并在段落之间留出空
## 行。

define gui.about = _p("""
《青春的抉择》是一部以大学新生入学为起点的生活向视觉小说。

你将从高考后的志愿填报开始，走进中国矿业大学的校园：宿舍、食堂、图书馆、课堂与操场。
在日常与选择里，你会遇见苏雨晴与江诗韵，并在成长、学业与关系之间，写下属于自己的答案。


BGM:

dance! dance! dance! - 虻川治

Dream (short ver.) - Rabpit

Nine Point Eight - Mili

Old Memory - Bruno Wen-li

Sea, You & Me - VISUAL ARTS、Key Sounds Label

Summer Pockets - VISUAL ARTS、Key Sounds Label

静かな冬の夜 - AQUAPLUS

夏野与暗恋 - 闫东炜


照片来自个人拍摄/神秘舍友/神秘群友/神秘豆包


感谢游玩""")


## 在构建的发布版中，可执行文件和目录所使用的短名称。此处仅限使用 ASCII 字符，并
## 且不能包含空格、冒号或分号。

define build.name = "newgame"


## 音效和音乐 #######################################################################

## 这三个变量控制哪些内置的混音器会默认显示给用户。将其中一个设置为 False 将隐藏
## 对应的混音器。

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## 为了让用户在音效或语音轨道上播放测试音频，请取消对下面一行的注释并设置播放的
## 样本声音。

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## 将以下语句取消注释就可以设置标题界面播放的背景音乐文件。此文件将在整个游戏中
## 持续播放，直至音乐停止或其他文件开始播放。

## 标题界面 BGM（把音频放到：game/audio/bgm/main_menu.ogg）
## 建议格式：.ogg（Ren'Py 原生支持最好）
define config.main_menu_music = "audio/bgm/main_menu.mp3"


## 转场 ##########################################################################
##
## 这些变量用来控制某些事件发生时的转场。每一个变量都应设置成一个转场，或者是
## None 来表示无转场。

## 进入或退出游戏菜单。

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## 各个游戏菜单之间的转场。

define config.intra_transition = dissolve


## 载入游戏后使用的转场。

define config.after_load_transition = None


## 在游戏结束之后进入主菜单时使用的转场。

define config.end_game_transition = None


## 用于控制在游戏开始标签不存在时转场的变量。作为替代，在显示初始化场景后使用
## with 语句。


## 窗口管理 ########################################################################
##
## 此命令控制对话框窗口何时显示。若为 show，对话框将总是显示。若为 hide，对话框
## 仅在对话出现时显示。若为 auto，对话框会在 scene 语句前隐藏，并在有新对话时重
## 新显示。
##
## 在游戏开始后，可以用 window show、window hide 和 window auto 语句来改变其状
## 态。

define config.window = "auto"


## 用于显示和隐藏对话框窗口的转场

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## 默认设置 ########################################################################

## 控制默认的文字显示速度。默认的 0 为瞬间，而其他数字则是每秒显示出的字符数。

default preferences.text_cps = 0


## 默认的自动前进延迟。数字越大，等待时间越长，有效范围为 0 - 30。

default preferences.afm_time = 15


## 存档目录 ########################################################################
##
## 控制 Ren'Py 放置游戏存档的特定操作系统目录。存档文件将放置在：
##
## Windows：%APPDATA\RenPy\<config.save_directory>
##
## Macintosh：$HOME/Library/RenPy/<config.save_directory>
##
## Linux：$HOME/.renpy/<config.save_directory>
##
## 该语句通常不应变更，若要变更，应为有效字符串而不是表达式。

define config.save_directory = "newgame-1765722885"


## 图标 ##########################################################################
##
## 在任务栏或 Dock 上显示的图标。

define config.window_icon = "gui/window_icon.png"


## 构建配置 ########################################################################
##
## 此部分控制 Ren'Py 如何将您的项目转变为发行版文件。

init python:

    ## 以下函数接受文件模式。文件模式不区分大小写，并与基础目录的相对路径相匹
    ## 配，包括或不包括 /。如果多个模式匹配，则使用第一个模式。
    ##
    ## 在一个模式中：
    ##
    ## / 是目录分隔符。
    ##
    ## * 匹配所有字符，目录分隔符除外。
    ##
    ## ** 匹配所有字符，包括目录分隔符。
    ##
    ## 例如，“*.txt”匹配基础目录中的 txt 文件，“game/**.ogg”匹配游戏目录或任何子
    ## 目录中的 ogg 文件，“**.psd”匹配项目中任何位置的 psd 文件。

    ## 将文件列为 None 来使其从构建的发行版中排除。

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## 若要封装文件，需将其列为“archive”。

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## 匹配为文档模式的文件会在 Mac 应用程序构建中被复制，因此它们同时出现在 APP
    ## 和 ZIP 文件中。

    build.documentation('*.html')
    build.documentation('*.txt')


## 执行应用内购需要一个 Google Play 许可密钥。许可密钥可以在 Google Play 开发者
## 控制台的“Monetize” > “Monetization Setup” > “Licensing”页面找到。

# define build.google_play_key = "..."


## 与 itch.io 项目相关的用户名和项目名，以 / 分隔。

# define build.itch_project = "renpytom/test-project"


init python:
    # 移除鼠标滚轮上滑的回滚功能，改为查看历史记录（在 screens.rpy 的 say 屏幕中绑定）
    if "mousedown_4" in config.keymap["rollback"]:
        config.keymap["rollback"].remove("mousedown_4")
```

### screens.rpy

*大小: 43.8 KB | Token: 11.3K*

```text
################################################################################
## 初始化
################################################################################

init offset = -1


################################################################################
## 样式
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## 游戏内屏幕
################################################################################


## 对话屏幕 ########################################################################
##
## 对话屏幕用于向用户显示对话。它需要两个参数，who 和 what，分别是叙述角色的名字
## 和所叙述的文本。（如果没有名字，参数 who 可以是 None。）
##
## 此屏幕必须创建一个 id 为 what 的文本可视控件，因为 Ren'Py 使用它来管理文本显
## 示。它还可以创建 id 为 who 和 id 为 window 的可视控件来应用样式属性。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    key "mousedown_4" action ShowMenu("history")

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## 如果有对话框头像，会将其显示在文本之上。请不要在手机界面下显示这个，因为
    ## 没有空间。
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## 通过 Character 对象使名称框可用于样式化。
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## 输入屏幕 ########################################################################
##
## 此屏幕用于显示 renpy.input。prompt 参数用于传递文本提示。
##
## 此屏幕必须创建一个 id 为 input 的输入可视控件来接受各种输入参数。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## 选择屏幕 ########################################################################
##
## 此屏幕用于显示由 menu 语句生成的游戏内选项。参数 items 是一个对象列表，每个对
## 象都有字幕和动作字段。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## 快捷菜单屏幕 ######################################################################
##
## 快捷菜单显示于游戏内，以便于访问游戏外的菜单。

screen quick_menu():

    ## 确保该菜单出现在其他屏幕之上，
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"
            style "quick_menu"

            textbutton _("回退") action Rollback()
            textbutton _("历史") action ShowMenu('history')
            textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("保存") action ShowMenu('save')
            textbutton _("快存") action QuickSave()
            textbutton _("快读") action QuickLoad()
            textbutton _("设置") action ShowMenu('preferences')


## 此代码确保只要用户没有主动隐藏界面，就会在游戏中显示 quick_menu 屏幕。
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 1.0

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## 标题和游戏菜单屏幕
################################################################################

## 导航屏幕 ########################################################################
##
## 该屏幕包含在标题菜单和游戏菜单中，并提供导航到其他菜单，以及启动游戏。

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("开始游戏") action Start()

        else:

            textbutton _("历史") action ShowMenu("history")

            textbutton _("保存") action ShowMenu("save")

        textbutton _("读取游戏") action ShowMenu("load")

        textbutton _("设置") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("结束回放") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("标题菜单") action MainMenu()

        textbutton _("关于") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## “帮助”对移动设备来说并非必需或相关。
            textbutton _("帮助") action ShowMenu("help")

        if renpy.variant("pc"):

            ## 退出按钮在 iOS 上是被禁止使用的，在安卓和网页上也不是必要的。
            textbutton _("退出") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## 标题菜单屏幕 ######################################################################
##
## 用于在 Ren'Py 启动时显示标题菜单。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#main-menu

screen main_menu():

    ## 此语句可确保替换掉任何其他菜单屏幕。
    tag menu

    # 运行时覆盖标题背景：若存在 images/bg/title.(png/jpg/jpeg/webp) 则优先使用。
    if renpy.loadable("images/bg/title.png"):
        add "images/bg/title.png"
    elif renpy.loadable("images/bg/title.jpg"):
        add "images/bg/title.jpg"
    elif renpy.loadable("images/bg/title.jpeg"):
        add "images/bg/title.jpeg"
    elif renpy.loadable("images/bg/title.webp"):
        add "images/bg/title.webp"
    else:
        add gui.main_menu_background

    ## 此空框可使标题菜单变暗。
    frame:
        style "main_menu_frame"

    ## use 语句将其他的屏幕包含进此屏幕。标题屏幕的实际内容在导航屏幕中。
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 0.5
    xoffset 0
    xmaximum 1200
    yalign 0.0
    yoffset 60

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")
    font gui.title_font

style main_menu_version:
    properties gui.text_properties("version")


## 游戏菜单屏幕 ######################################################################
##
## 此屏幕列出了游戏菜单的基本共同结构。可使用屏幕标题调用，并显示背景、标题和导
## 航菜单。
##
## scroll 参数可以是 None，也可以是 viewport 或 vpgrid。此屏幕旨在与一个或多个子
## 屏幕同时使用，这些子屏幕将被嵌入（放置）在其中。

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        # 与标题界面一致：优先使用 images/bg/title.*
        if renpy.loadable("images/bg/title.png"):
            add "images/bg/title.png"
        elif renpy.loadable("images/bg/title.jpg"):
            add "images/bg/title.jpg"
        elif renpy.loadable("images/bg/title.jpeg"):
            add "images/bg/title.jpeg"
        elif renpy.loadable("images/bg/title.webp"):
            add "images/bg/title.webp"
        else:
            add gui.main_menu_background
    else:
        # 运行时覆盖游戏菜单背景：若存在 images/bg/game_menu.* 则优先使用。
        if renpy.loadable("images/bg/game_menu.png"):
            add "images/bg/game_menu.png"
        elif renpy.loadable("images/bg/game_menu.jpg"):
            add "images/bg/game_menu.jpg"
        elif renpy.loadable("images/bg/game_menu.jpeg"):
            add "images/bg/game_menu.jpeg"
        elif renpy.loadable("images/bg/game_menu.webp"):
            add "images/bg/game_menu.webp"
        else:
            add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## 导航部分的预留空间。
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("返回"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size 75
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## 关于屏幕 ########################################################################
##
## 此屏幕提供有关游戏和 Ren'Py 的制作人员和版权信息。
##
## 此屏幕没有什么特别之处，因此它也可以作为一个例子来说明如何制作一个自定义屏
## 幕。

screen about():

    tag menu

    ## 此 use 语句将 game_menu 屏幕包含到了这个屏幕内。子级 vbox 将包含在
    ## game_menu 屏幕的 viewport 内。
    use game_menu(_("关于"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("版本 [config.version!t]\n")

            ## gui.about 通常在 options.rpy 中设置。
            if gui.about:
                text "[gui.about!t]\n"

            text _("引擎：{a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## 读取和保存屏幕 #####################################################################
##
## 这些屏幕负责让用户保存游戏并能够再次读取。由于它们几乎完全一样，因此这两个屏
## 幕都是以第三个屏幕 file_slots 来实现的。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#save https://doc.renpy.cn/zh-
## CN/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("保存"))


screen load():

    tag menu

    use file_slots(_("读取游戏"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("第 {} 页"), auto=_("自动存档"), quick=_("快速存档"))

    use game_menu(title):

        fixed:

            ## 此代码确保输入控件在任意按钮执行前可以获取 enter 事件。
            order_reverse True

            ## 页面名称，可以通过单击按钮进行编辑。
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## 存档位网格。
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%Y-%m-%d %H:%M"), empty=_("空存档位")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## 用于访问其他页面的按钮。
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) 给出 1 到 9 之间的数字。
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("上传同步"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("下载同步"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5
    xalign 0.5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## 设置屏幕 ########################################################################
##
## 设置屏幕允许用户配置游戏，使其更适合自己。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("设置"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("显示")
                        textbutton _("窗口") action Preference("display", "window")
                        textbutton _("全屏") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("快进")
                    textbutton _("未读文本") action Preference("skip", "toggle")
                    textbutton _("选项后继续") action Preference("after choices", "toggle")
                    textbutton _("忽略转场") action InvertSelected(Preference("transitions", "toggle"))

                ## 可在此处添加 radio_pref 或 check_pref 类型的额外 vbox，以添加
                ## 额外的创建者定义的偏好设置。

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("文字速度")

                    bar value Preference("text speed")

                    label _("自动前进时间")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("音乐音量")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("音效音量")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("测试") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("语音音量")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("测试") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("全部静音"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## 历史屏幕 ########################################################################
##
## 这是一个向用户显示对话历史的屏幕。虽然此屏幕没有什么特别之处，但它必须访问储
## 存在 _history_list 中的对话历史记录。
##
## https://doc.renpy.cn/zh-CN/history.html

screen history():

    tag menu

    ## 避免预缓存此屏幕，因为它可能非常大。
    predict False

    use game_menu(_("历史"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## 此代码可确保如果 history_height 为 None 时仍可正常显示条目。
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## 从 Character 对象中获取叙述角色的文字颜色，如果设置了
                        ## 的话。
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("尚无对话历史记录。")


## 此代码决定了允许在历史记录屏幕上显示哪些标签。

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## 帮助屏幕 ########################################################################
##
## 提供有关键盘和鼠标映射信息的屏幕。它使用其它屏幕（keyboard_help、mouse_help
## 和 gamepad_help）来显示实际的帮助内容。

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("帮助"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("键盘") action SetScreenVariable("device", "keyboard")
                textbutton _("鼠标") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("手柄") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("回车")
        text _("推进对话并激活界面。")

    hbox:
        label _("空格")
        text _("在没有选择的情况下推进对话。")

    hbox:
        label _("方向键")
        text _("导航界面。")

    hbox:
        label _("Esc")
        text _("访问游戏菜单。")

    hbox:
        label _("键盘")
        text _("按住时快进对话。")

    hbox:
        label _("Tab")
        text _("切换对话快进。")

    hbox:
        label _("上一页")
        text _("回退至先前的对话。")

    hbox:
        label _("下一页")
        text _("向前至后来的对话。")

    hbox:
        label "H"
        text _("隐藏用户界面。")

    hbox:
        label "S"
        text _("截图。")

    hbox:
        label "V"
        text _("切换辅助{a=https://doc.renpy.cn/zh-CN/self_voicing.html}机器朗读{/a}。")

    hbox:
        label "Shift+A"
        text _("打开无障碍菜单。")


screen mouse_help():

    hbox:
        label _("左键点击")
        text _("推进对话并激活界面。")

    hbox:
        label _("中键点击")
        text _("隐藏用户界面。")

    hbox:
        label _("右键点击")
        text _("访问游戏菜单。")

    hbox:
        label _("鼠标滚轮上")
        text _("打开历史对话记录。")

    hbox:
        label _("鼠标滚轮下")
        text _("向前至后来的对话。")


screen gamepad_help():

    hbox:
        label _("右扳机键\nA/底键")
        text _("推进对话并激活界面。")

    hbox:
        label _("左扳机键\n左肩键")
        text _("回退至先前的对话。")

    hbox:
        label _("右肩键")
        text _("向前至后来的对话。")

    hbox:
        label _("十字键，摇杆")
        text _("导航界面。")

    hbox:
        label _("开始，向导，B/右键")
        text _("访问游戏菜单。")

    hbox:
        label _("Y/顶键")
        text _("隐藏用户界面。")

    textbutton _("校准") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## 其他屏幕
################################################################################


## 确认屏幕 ########################################################################
##
## 当 Ren'Py 需要询问用户有关确定或取消的问题时，会调用确认屏幕。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## 显示此屏幕时，确保其他屏幕无法输入。
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("确定") action yes_action
                textbutton _("取消") action no_action

    ## 右键点击退出并答复 no（取消）。
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## 快进指示屏幕 ######################################################################
##
## skip_indicator 屏幕用于指示快进正在进行中。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("正在快进")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## 此变换用于一个接一个地闪烁箭头。
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## 我们必须使用包含“▸”（黑色右旋小三角）字形的字体。
    font "DejaVuSans.ttf"


## 通知屏幕 ########################################################################
##
## 通知屏幕用于向用户显示消息。（例如，当游戏快速保存或进行截屏时。）
##
## https://doc.renpy.cn/zh-CN/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL 模式屏幕 ####################################################################
##
## 此屏幕用于 NVL 模式的对话和菜单。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## 在 vpgrid 或 vbox 中显示对话框。
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## 显示菜单，如果给定的话。如果 config.narrator_menu 设置为 True，则菜单
        ## 可能显示不正确。
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## 此语句控制一次可以显示的 NVL 模式条目的最大数量。
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## 对话气泡屏幕 ######################################################################
##
## 对话气泡屏幕用于以对话气泡的形式向玩家显示对话。对话气泡屏幕的参数与 say 屏幕
## 相同，必须创建一个 id 为 what 的可视控件，并且可以创建 id 为 namebox、who 和
## window 的可视控件。
##
## https://doc.renpy.cn/zh-CN/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## 移动设备界面
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## 由于可能没有鼠标，我们将快捷菜单替换为一个使用更少、更大按钮的版本，这样更容
## 易触摸。
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style "quick_menu"
            style_prefix "quick"

            textbutton _("回退") action Rollback()
            textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("菜单") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 1305

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
```

### script.rpy

*大小: 38.9 KB | Token: 7.2K*

```text
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
```
