# Copilot instructions (Ren'Py)

## Project map (where to change what)
- `game/script.rpy`: main story flow (labels/menus/variables), asset bindings (`image ... = "images/..."`), character definitions.
- `game/options.rpy`: game metadata (`config.name`, `config.version`), main menu BGM (`config.main_menu_music`), build classification rules.
- `game/gui.rpy`: GUI/theme constants (resolution `gui.init(1920, 1080)`, fonts, sizes, colors).
- `game/screens.rpy`: screen language (say/choice/quick_menu, styles/layout).
- `project.json`: Ren'Py build settings (e.g. `packages: ["win"]`, `force_recompile: true`).

## Ren'Py scripting conventions used here
- Variables are declared with `default` (including Chinese identifiers like `好感度_雨晴`, `专业选择`). Use `default` for new state so saves don’t break.
- Story control is label-driven: `label start:` → `menu:` → `$` mutations → `jump some_label`.
- Player name is interpolated via `Character("[player_name]")` and `[player_name]` in dialogue.
- Assets are referenced relative to `game/` (e.g. `image bg dormitory = "images/bg/dormitory.png"`, audio `"audio/bgm/main_menu.ogg"`).

## Assets & naming (keep paths consistent)
- Backgrounds: `game/images/bg/*.png` used as `scene bg <name>`.
- Sprites: `game/images/ch/<character>/<expression>.png` used as `show <character> <expression>`.
- Audio: `game/audio/bgm/*.ogg`, `game/audio/sfx/*.ogg` (main menu BGM configured in `game/options.rpy`).
- If you introduce new `bg`/sprite names, add matching `image ...` declarations near the existing ones in `game/script.rpy`.

## Generated/ignored files (do not edit)
- Do not modify compiled scripts (`game/**/*.rpyc`, `game/**/*.rpymc`), `game/cache/`, or `game/saves/` (see `.gitignore` and `.vscode/settings.json`).
- Source of truth is the `.rpy` / `.rpym` files.

## Localization
- Built-in UI translations live under `game/tl/` (e.g. `game/tl/None/common.rpym`). Prefer editing `.rpym` (not `.rpymc`).

## Workflow expectations
- This repo doesn’t define CLI build/test scripts. Use the Ren'Py Launcher to run and build distributions.
- For web/progressive download behavior, see `progressive_download.txt`.
