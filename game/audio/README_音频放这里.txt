把音频素材放在本目录下（game/audio/）。

已启用（标题界面 BGM）：
- game/audio/bgm/main_menu.mp3
  对应配置：game/options.rpy -> config.main_menu_music = "audio/bgm/main_menu.mp3"

可选（你想加氛围的话再用）：
- game/audio/bgm/campus_day.ogg      校园日常
- game/audio/bgm/daily_life.ogg      宿舍/轻松日常（用于 Day 2 早晨等）
- game/audio/bgm/campus_evening.ogg  校园傍晚/散步（与 campus_day 同级，用于 sunset 段落）
- game/audio/bgm/library_night.ogg   图书馆夜聊
- game/audio/sfx/message.ogg         手机提示音
紧张/抉择 game/audio/bgm/decision.ogg（填志愿、重大选择菜单前后）
温柔/恋爱 game/audio/bgm/romance.ogg（好感度事件、独处场景）
建议：
- 优先用 .ogg（兼容性最好）
- 码率不必太高，保证循环不突兀即可
