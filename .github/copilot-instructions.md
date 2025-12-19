# Copilot instructions (Ren'Py)

## Project Architecture
- **Core Script**: `game/script.rpy` contains the main story flow, character definitions, and variable initialization. This is the primary file for narrative content.
- **Configuration**: `game/options.rpy` handles game metadata (name, version), build settings, and global audio configurations (e.g., main menu music).
- **UI/Visuals**: `game/gui.rpy` defines theme constants (resolution, colors, fonts), while `game/screens.rpy` manages screen layouts and styles.
- **Assets**: Resources are organized in `game/images/` and `game/audio/`.

## Critical Workflows
- **Run/Build**: This project relies on the **Ren'Py Launcher** for running the game and building distributions. There are no CLI build scripts.
- **State Management**: Always use `default` to initialize variables (e.g., `default 好感度_雨晴 = 0`). This ensures variables participate in the save/load system correctly.
- **Asset Binding**: New assets must be declared in `game/script.rpy` using `image` statements before use (e.g., `image bg dormitory = "images/bg/dormitory.jpg"`).

## Project-Specific Conventions
- **Variable Naming**: This project uses **Chinese variable names** for game state (e.g., `好感度_雨晴`, `专业选择`, `社团路线`). Maintain this pattern for narrative logic.
- **Character Definitions**: Characters are defined with specific colors in `game/script.rpy`. Use the defined variable names (e.g., `雨晴`, `浩然`) in dialogue.
- **Asset Formats**:
  - **Backgrounds**: Located in `game/images/bg/`. The project currently uses **.jpg** for backgrounds (e.g., `images/bg/dormitory.jpg`).
  - **Sprites**: Located in `game/images/ch/<character>/`. The project uses **.png** for character sprites (e.g., `images/ch/yuqing/happy.png`).
  - **Audio**: Background music in `game/audio/bgm/` (supports .mp3/.ogg). Main menu music is configured as `audio/bgm/main_menu.mp3`.
- **Story Structure**: Flow is controlled via `label`, `menu`, and `jump`. Player name interpolation uses `[player_name]`.

## Integration & Dependencies
- **Ren'Py Engine**: The codebase is strictly Ren'Py. Avoid Python-only constructs unless wrapped in `python:` blocks or `$` lines for simple statements.
- **Localization**: Translation files reside in `game/tl/`. Edit `.rpym` files for translations, not the compiled `.rpymc` files.

## Generated Files (Do Not Edit)
- `game/**/*.rpyc`, `game/**/*.rpymc` (Compiled scripts)
- `game/cache/`
- `game/saves/`
