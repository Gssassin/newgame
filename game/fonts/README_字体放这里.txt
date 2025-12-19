把字体文件放在本目录下（game/fonts/）。

推荐用法（不同位置不同字体）：
- 对话文本（剧情对白/旁白）：game/fonts/dialogue.ttf（也支持 .otf / .ttc）
- 角色姓名（名字框）：game/fonts/name.ttf（也支持 .otf / .ttc）
- 界面文字（设置/按钮/菜单）：game/fonts/interface.ttf（也支持 .otf / .ttc）
- 主菜单标题（游戏名）：game/fonts/title.ttf（也支持 .otf / .ttc）

可选回退（不提供上面某个文件时用）：
- 全局回退字体：game/fonts/main.ttf（也支持 main.otf / main.ttc）

对应代码：game/gui.rpy 会按“区域字体 → main.* → 默认字体(SourceHanSansLite.ttf)”的顺序自动选择。

提示：
- 中文字体建议使用包含常用汉字的字体（否则会出现方块/缺字）。
- 改完字体后如果看起来没变化：请完全退出重进，或清空 game/cache/ 再启动。
