# 🛠️ Proyecto 07: Game Jam AI Toolkit

## Resumen Ejecutivo

**Objetivo:** Crear un toolkit reusable y optimizado para participar en game jams usando AI, reduciendo tiempo de desarrollo 60%+. Incluye templates, prompts optimizados, scripts de automatización y workflows probados.

**Herramientas principales:** SEELE, Stable Diffusion, Claude Code, Godot/Unity

**Tiempo estimado:** 2-3 semanas para crear el toolkit

**Dificultad:** Media

**Resultado:** Toolkit reusable para TODO game jam futuro

---

## 1. Concepto del toolkit

### Componentes:

```
📁 game-jam-toolkit/
│
├── 📂 templates/
│   ├── godot_project_template/      # Proyecto Godot listo
│   ├── unity_project_template/      # Proyecto Unity listo
│   └── game_jam_gameplan.md        # Plan maestro
│
├── 📂 prompts/
│   ├── sprites.md                  # Prompts para sprites
│   ├── code.md                    # Prompts para código
│   ├── audio.md                   # Prompts para audio
│   └── design.md                  # Prompts para game design
│
├── 📂 scripts/
│   ├── generate_assets.py          # Batch sprite generator
│   ├── setup_project.sh           # Auto-setup
│   └── build_export.py            # Build automation
│
├── 📂 checklists/
│   ├── pre_jam_checklist.md
│   ├── during_jam_checklist.md
│   └── post_jam_checklist.md
│
└── 📂 docs/
    ├── quickstart.md
    ├── best_practices.md
    └── troubleshooting.md
```

### Filosofía:

```
EL PROBLEMA: Game jams son 48-72 horas intensas
LA SOLUCIÓN: toolkit que automatiza lo repetitivo

QUE AUTOMATIZA:
├── Setup inicial del proyecto
├── Generación de sprites básicos
├── Templates de código comunes
├── Audio placeholder
└── Estructura de niveles

QUE NO AUTOMATIZA:
├── Game design creativo
├── Game feel y polish
├── Decisiones de diseño
└── Testing y QA
```

---

## 2. Plan de implementación

### Fase 1: Templates de proyecto (Días 1-5)

```
DÍA 1-2: Godot template

GODOT TEMPLATE CONTENTS:
├── Project settings optimizados
│   ├── Display: 640x360 (16:9, pixel art friendly)
│   ├── Physics: 2D
│   ├── Stretch: viewport
│   └── Import: nearest filter
├── Folder structure pre-creada
│   ├── scenes/
│   ├── scripts/
│   ├── assets/
│   ├── fonts/
│   └── autoloads/
├── Autoloads básicos
│   ├── GameManager (singleton)
│   ├── AudioManager
│   └── SaveManager
├── Escenas base
│   ├── Main.tscn (plantilla de nivel)
│   ├── Player.tscn (con controller básico)
│   ├── UI.tscn (HUD placeholder)
│   └── Menu.tscn (menú base)
└── Scripts templates
    ├── player_controller_template.gd
    ├── enemy_template.gd
    └── ui_template.gd

SETUP SCRIPT:
#!/bin/bash
# setup_godot_template.sh

echo "Setting up Godot Game Jam Template..."

# Ask for game name
read -p "Game name: " gamename

# Copy template
cp -r godot_template "$gamename"

# Rename project
cd "$gamename"
sed -i "s/GameJamTemplate/$gamename/g" project.godot

echo "Done! Open $gamename in Godot"
```

```
DÍA 3-5: Unity template

UNITY TEMPLATE CONTENTS:
├── Project settings
│   ├── 2D mode
│   ├── Target: WebGL (para publicar)
│   └── Quality: Fastest
├── Folder structure
│   ├── Scenes/
│   ├── Scripts/
│   ├── Prefabs/
│   ├── Sprites/
│   └── Audio/
├── Scripts base
│   ├── GameManager.cs
│   ├── PlayerController.cs
│   ├── AudioManager.cs
│   └── UIManager.cs
├── Prefabs
│   ├── Player_Prefab
│   ├── Enemy_Prefab
│   └── UI_Canvas
└── Scene template
    ├── MainGame
    └── MainMenu
```

### Fase 2: Prompts library (Días 6-12)

```
DÍA 6-7: Sprite prompts

SPRITE_PROMPTS.md:

# SPRITE GENERATION PROMPTS

## Character (Base)
"pixel art {character_type}, {style}, {color_scheme},
{view_angle}, {pose}, transparent background,
{game_style}, {resolution}"

Examples:
"pixel art hero character, red armor, front view, 
idle pose, transparent background, 16-bit style, 32x32"

"pixel art slime enemy, green translucent, front view,
idle bounce, transparent background, 16-bit style, 16x16"

## Animation Frames
"pixel art {character} {animation} frame {frame_number},
{style}, transparent background, consistent with reference"

## Tiles
"pixel art {tile_type} tile, {variation}, seamless,
{view_angle}, transparent background, {game_style}"

## Props
"pixel art {prop_name}, {style}, transparent background,
{game_asset}, {resolution}"

## UI Elements
"pixel art {ui_element}, {style}, {color}, 
{game_asset}, {resolution}"
```

```
DÍA 8-9: Code prompts

CODE_PROMPTS.md:

# CODE GENERATION PROMPTS

## Player Controller (Godot)
```
Write a Godot 4 GDScript for a 2D platformer player controller.
Requirements:
- WASD/Arrow movement
- Variable jump height (hold for higher)
- Coyote time: 0.1s
- Jump buffer: 0.1s
- Wall slide and wall jump
- {ADDITIONAL_MECHANICS}
Use export variables for tuning.
Include comments.
```

## Enemy AI (Godot)
```
Write a Godot 4 GDScript for a 2D enemy with:
- State machine: idle, patrol, chase, attack
- Player detection (Area2D)
- Basic pathfinding
- {ENEMY_SPECIFIC_BEHAVIOR}
Extends Node2D.
```

## UI System (Godot)
```
Write Godot 4 GDScript for a UI system with:
- Health bar (ImageProgressBar)
- Score counter
- Pause menu
- Game over screen
- {ADDITIONAL_UI}
Use signals for updates.
```

## Player Controller (Unity)
```
Write Unity C# for a 2D platformer with:
- Rigidbody2D physics
- Horizontal movement with acceleration
- Variable jump (Input.GetAxis for smooth)
- {ADDITIONAL}
Use [SerializeField] for inspector.
```

## Game Manager (Unity)
```
Write Unity C# GameManager singleton with:
- Score tracking
- Game state (playing, paused, gameover)
- Scene management
- {ADDITIONAL}
Use Events for communication.
```
```

```
DÍA 10-12: Audio prompts

AUDIO_PROMPTS.md:

# AUDIO GENERATION PROMPTS

## Background Music
"Generate {genre} background music for a {game_type}.
Mood: {mood}. Length: {duration}.
Style: {style_details}.

Use {tool} to generate."

Examples:
"Retro 8-bit background music for a platformer game.
Cheerful, upbeat, looping seamlessly.
Use Boomy or AIVA."

"Dark ambient music for horror game.
Tense, atmospheric, subtle percussion.
Use AIVA or Mubert."

## Sound Effects
"Generate {sfx_type} sound effect for {game}.
Style: {style}. Duration: {length}.

Examples:
"Jump sound, retro 8-bit style, short and bouncy.
Use ElevenLabs or Bark."

"Laser shoot sound, futuristic, sci-fi weapon.
Use ElevenLabs SFX."

"Coin collect, satisfying ding, retro game style.
Use Bark."

"Explosion, 8-bit, small, pixel art game.
Use Bark."
```

### Fase 3: Scripts de automatización (Días 13-17)

```
DÍA 13-14: Asset generator script

generate_assets.py:
```python
#!/usr/bin/env python3
"""
Game Jam Asset Generator
Generates sprites, audio placeholders, and code templates
"""

import os
import json
from pathlib import Path

class GameJamAssetGenerator:
    def __init__(self, project_name: str):
        self.project_name = project_name
        self.assets_dir = Path(project_name) / "assets"
        self.prompts_dir = Path("prompts")
    
    def generate_sprite(self, prompt: str, output_name: str):
        """Generate sprite using Leonardo AI or SD API"""
        # Implementation
        pass
    
    def generate_sprite_batch(self, sprite_list: list):
        """Generate multiple sprites from a list"""
        for sprite in sprite_list:
            self.generate_sprite(sprite["prompt"], sprite["output"])
    
    def generate_code_template(self, template_name: str, context: dict):
        """Generate code from template"""
        template = self.load_template(template_name)
        return self.fill_template(template, context)
    
    def setup_project_structure(self):
        """Create standard game jam folder structure"""
        folders = [
            "assets/sprites",
            "assets/audio",
            "scenes",
            "scripts",
            "fonts",
        ]
        for folder in folders:
            (self.assets_dir.parent / folder).mkdir(parents=True, exist_ok=True)
    
    def run(self, config_file: str):
        """Main entry point"""
        with open(config_file) as f:
            config = json.load(f)
        
        self.setup_project_structure()
        
        # Generate sprites
        if "sprites" in config:
            self.generate_sprite_batch(config["sprites"])
        
        # Generate code
        for code_template in config.get("code", []):
            output = self.generate_code_template(
                code_template["template"],
                code_template["context"]
            )
            self.write_file(code_template["output"], output)

if __name__ == "__main__":
    import sys
    generator = GameJamAssetGenerator(sys.argv[1])
    generator.run(sys.argv[2])
```
```

```
DÍA 15-16: Setup automation

setup_game_jam.sh:
```bash
#!/bin/bash
# Quick setup for game jam projects

set -e

echo "🎮 Game Jam Project Setup"
echo "========================"

# Get game info
read -p "Game name: " GAMENAME
read -p "Engine [godot/unity]: " ENGINE
read -p "Genre [platformer/shooter/puzzle/other]: " GENRE

# Clone template
if [ "$ENGINE" = "godot" ]; then
    cp -r templates/godot_template "$GAMENAME"
    cd "$GAMENAME"
    # Update project name
    sed -i "s/TemplateGame/$GAMENAME/g" project.godot
elif [ "$ENGINE" = "unity" ]; then
    echo "Please open Unity Hub and create new 2D project"
    echo "Then copy templates/unity_base/* into your project"
fi

# Generate assets from plan
if [ -f "plans/${GENRE}_plan.json" ]; then
    python3 scripts/generate_assets.py "$GAMENAME" "plans/${GENRE}_plan.json"
fi

echo "✅ Setup complete!"
echo "Run 'godotshell' to open Godot"
```
```

```
DÍA 17: Build script

build_export.py:
```python
#!/usr/bin/env python3
"""Build and export game for itch.io"""

import os
import subprocess
import sys
from pathlib import Path

def build_godot(project_path: str, export_preset: str):
    """Build Godot project and export"""
    result = subprocess.run([
        "godot",
        "--headless",
        "--export-release",
        export_preset,
        f"{project_path}/export/{game_name}.html"
    ])
    return result.returncode == 0

def build_itch_package(game_name: str):
    """Create itch.io package"""
    # Create ZIP with game files
    os.system(f"zip -r {game_name}.zip export/")
    # Upload via itch.io API or manual
    print(f"Package ready: {game_name}.zip")

if __name__ == "__main__":
    build_godot(sys.argv[1], "web")
    build_itch_package(sys.argv[2])
```
```

### Fase 4: Documentation (Días 18-21)

```
DÍA 18-19: Quickstart guide

QUICKSTART.md:
# Game Jam AI Toolkit - Quick Start

## 1. Before the Jam (30 min setup)

```bash
# Clone toolkit
git clone https://github.com/your/toolkit.git
cd toolkit

# Run setup
./setup_game_jam.sh
# Follow prompts

# Configure API keys
cp config/api_keys.example config/api_keys
# Edit with your keys
```

## 2. During the Jam

### Hour 0-1: Setup
1. Run `./setup.sh`
2. Generate base sprites with AI
3. Setup player controller from template

### Hour 1-4: Core Game
1. Implement core mechanic
2. Generate/main art assets
3. Build basic levels

### Hour 4-24: Polish
1. Add enemies/obstacles
2. Polish animations
3. Add sound effects
4. Build levels

### Hour 24-48: Final Push
1. Final level design
2. Menu and UI polish
3. Sound and music
4. Test and export

## 3. Commands Reference

```bash
# Generate sprites
python3 scripts/generate_assets.py game_name plans/sprites.json

# Generate code template
python3 scripts/generate_code.py templates/player_controller.gdtpl

# Export game
python3 scripts/build_export.py
```

```
DÍA 20-21: Best practices + troubleshooting

BEST_PRACTICES.md:
# Game Jam Best Practices with AI

## DO:
- Use AI for repetitive tasks
- Generate placeholders early
- Iterate fast with prototypes
- Keep AI outputs simple
- Review ALL AI code before committing
- Test frequently

## DON'T:
- Don't rely 100% on AI
- Don't over-engineer
- Don't skip playtesting
- Don't forget to save
- Don't skip the menu
- Don't miss the jam deadline

## Workflow:
1. Design on paper first
2. AI generate placeholders
3. Implement core mechanic
4. Add art/audio
5. Polish and playtest
6. Export

TROUBLESHOOTING.md:
# Common Issues

## AI sprite inconsistent
Solution: Use LoRA or reference image

## Code doesn't compile
Solution: Review and fix syntax errors

## Assets don't load
Solution: Check file paths and import settings

## Performance issues
Solution: Reduce sprite resolution, optimize code
```

---

## 3. Game Jam plans pre-hechos

```
plans/
├── platformer_plan.json
├── shooter_plan.json
├── puzzle_plan.json
└── rpg_plan.json
```

platformer_plan.json:
```json
{
  "game_type": "platformer",
  "estimated_time": "48 hours",
  
  "sprites": [
    {"prompt": "pixel art player character, 32x32, idle animation", "output": "player_idle.png"},
    {"prompt": "pixel art player walk cycle, 8 frames", "output": "player_walk.png"},
    {"prompt": "pixel art player jump", "output": "player_jump.png"},
    {"prompt": "pixel art slime enemy, 16x16", "output": "enemy_slime.png"},
    {"prompt": "pixel art ground tile, 16x16", "output": "tile_ground.png"},
    {"prompt": "pixel art platform tile, 16x16", "output": "tile_platform.png"},
    {"prompt": "pixel art coin, 16x16", "output": "item_coin.png"}
  ],
  
  "code": [
    {"template": "player_controller.gdtpl", "output": "Player.cs"},
    {"template": "enemy_basic.gdtpl", "output": "Enemy.cs"},
    {"template": "platform.gdtpl", "output": "Platform.cs"}
  ],
  
  "audio": [
    {"type": "bgm", "mood": "upbeat", "output": "music.wav"},
    {"type": "sfx", "name": "jump", "output": "jump.wav"},
    {"type": "sfx", "name": "coin", "output": "coin.wav"}
  ]
}
```

---

## 4. Prompts críticos para game jams

### Master prompt para sprites:

```text
SPRITE TEMPLATE:
"pixel art [SUBJECT], [STYLE], [VIEW], [POSE],
transparent background, [SIZE], [GAME_ENGINE] game asset,
[BESPOKE_DETAILS]"

EXAMPLE:
"pixel art knight character, 16-bit era style, front view,
idle breathing animation 4 frames, transparent background,
32x32 pixels, Godot game asset, silver armor with red cape"
```

### Master prompt para código:

```text
CODE TEMPLATE:
Write [ENGINE] [LANGUAGE] code for [FEATURE].

Requirements:
- [SPECIFIC_REQUIREMENTS]
- [MORE_REQUIREMENTS]

Use [SPECIFIC_CONVENTIONS].
Include error handling.
```

---

## 5. Checklist de game jam

### Pre-game jam:

```
□ Toolkit downloaded and tested
□ API keys configured
□ Godot/Unity installed
□ Assets generated as placeholders
□ Project template ready
□ Reference materials collected
□ Sleep well night before
□ Coffee/snacks ready
```

### Durante el jam:

```
HOUR 0:
□ Read theme
□ Brainstorm (30 min)
□ Choose idea
□ Scope it realistically
□ Setup project

HOURS 1-8:
□ Implement core mechanic
□ Basic player controller
□ One level playable
□ Basic sprites

HOURS 8-24:
□ Add enemies
□ More levels
□ Polish art
□ Add sound

HOURS 24-40:
□ Complete game
□ Polish everything
□ Fix bugs
□ Add menu

HOURS 40-48:
□ Final testing
□ Export
□ Create screenshots
□ Upload to itch.io
□ SUBMIT!
```

---

## 6. Métricas de éxito

### Por game jam:

```
TIME SAVINGS:
- Setup: -30 min
- Art generation: -4 hours
- Code boilerplate: -3 hours
- Audio placeholders: -2 hours
TOTAL SAVED: ~9-10 hours

QUALITY:
- Consistent art style
- Working code (usually)
- More time for polish
- Less stress

REUSABILITY:
- Toolkit improves each jam
- Templates get better
- Faster each time
```

---

_Volver a [README principal](../README.md)_
