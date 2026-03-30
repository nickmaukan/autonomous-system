# 🎮 Proyecto 03: Platformer 2D Prototype con AI

## Resumen Ejecutivo

**Objetivo:** Crear un platformer 2D jugable completo usando AI para acelerar arte y código. El juego demuestra el potencial del pipeline y sirve como base para proyectos más ambiciosos.

**Herramientas principales:** Godot 4 + Ziva, Stable Diffusion, Claude Code, SEELE (para validación)

**Tiempo estimado:** 4-6 semanas (prototipo completo)

**Dificultad:** Media-Alta

**Resultado esperado:** Un platformer de 3-5 niveles jugable, publicado en itch.io

---

## 1. Concepto del juego

### Genre: Platformer de acción

```
ELEVATOR PITCH:
"Un platformer de ritmo rápido donde controlas a un ninja cyberpunk
en una ciudad futurista. Corre por las azoteas, deslizate por paredes,
y usa tu dash para atravesar el paisaje urbano."

DIFERENCIACIÓN:
- Estilo cyberpunk/neón (nicho menos saturado)
- Movimiento fluido tipo Celeste
- Mecánicas: wall jump, wall slide, dash
- boss fights en cada nivel
```

### Core mechanics:

```
MOVEMENT:
├── Run: Velocidad base, acceleration suave
├── Jump: Variable height (hold para más alto)
├── Double jump: Un uso por aire
├── Wall slide: Reduced gravity en paredes
├── Wall jump: Rebote desde paredes
└── Dash: 8-directional, 1s cooldown, i-frames

COLLECTIBLES:
├── Data orbs: Collectibles principales
├── Power-ups: Dash upgrade, double jump upgrade
└── Keys: Open doors para shortcuts

ENEMIES:
├── Patrol drones: Simple back-and-forth
├── Turrets: Stationary, shoot bullets
├── Security bots: Chase when see player
└── Boss: Each level has a mini-boss

LEVELS:
├── Level 1: Tutorial - basic movement
├── Level 2: Wall mechanics
├── Level 3: Dash + enemies
├── Level 4: Boss fight
└── Level 5: Everything combined
```

---

## 2. Plan de implementación

### Fase 1: Prototyping sin arte (Semana 1)

```
DÍA 1-2: Setup del proyecto

GODOT 4 SETUP:
├── Crear nuevo proyecto 2D
├── Configurar pixel art settings:
│   ├── Display > Window > Size: 384x216
│   ├── Stretch > Mode: viewport
│   ├── Texture > Filter: Nearest
│   └── Import > Defaults > Sprite > Filter: Nearest
├── Setup folder structure:
│   ├── scenes/
│   ├── scripts/
│   ├── assets/
│   └── resources/
└── Documentar settings

PHYSICS SETTINGS:
├── 2D Physics > Gravity: 1200
├── 2D Physics > Unit MPP: 16 (pixels per meter)
└── Tilemap > Cell > Size: 16x16
```

```
DÍA 3-4: Player controller básico

IMPLEMENTAR:
├── CharacterBody2D setup
├── Variables exportadas:
│   ├── speed: 200
│   ├── jump_velocity: -400
│   ├── gravity: 1200
│   ├── wall_slide_speed: 60
│   ├── dash_speed: 500
│   └── dash_cooldown: 1.0
├── Movement: _physics_process
├── Jump: Input.is_action_just_pressed
├── Coyote time (0.1s grace period)
├── Jump buffer (0.1s pre-landing)
└── Debug: Print player state

TESTEAR:
├── Ground movement
├── Jumping (single)
├── Double jump
├── Wall slide
└── Dash
```

```
DÍA 5-7: Level design - Nivel 1

SKETCH EN PAPEL:
├── Start: spawn point
├── Tutorial section: aprender a correr
├── Gap: requires jump
├── Platform section: aprender a land
├── Exit: portal al next level

TILEMAP:
├── Ground tiles: collision solo top
├── Walls: collision all sides
├── Platforms: pass-through desde arriba
└── Spawn/Exit points

ITERATIONS:
├── Ajustar spacing
├── Test jump distances
├── Verify no softlocks
└── Documentar level flow
```

### Fase 2: Arte generado con AI (Semanas 2-3)

```
SEMANA 2: Character + Enemies art

DÍA 1-2: Setup LoRA para estilo cyberpunk

ENTRENAR LoRA:
├── Dataset: 25 imágenes cyberpunk characters
├── Estilo: neon-lit, dark background
├── Resolution: 512x512
└── Test: generar ninja cyborg

OUTPUT:
├── Player sprite sheet: idle, run, jump, slide, dash
├── Palette: dark blues, neon pink accents, white highlights
└── Style: "cyberpunk ninja"
```

```
DÍA 3-4: Generate sprites

PLAYER SPRITE SHEETS:
├── Idle: 4 frames (breathing)
├── Run: 8 frames (full run cycle)
├── Jump: 4 frames (takeoff, air, land anticipation)
├── Fall: 3 frames
├── Wall slide: 3 frames
├── Dash: 4 frames (strech effect)
├── Hurt: 3 frames
└── Death: 4 frames

ENEMY SPRITES:
├── Drone: 4 frames (idle hover)
├── Turret: 2 frames (idle, firing)
├── Security bot: reuse player sprites (different colors)
└── Boss: 2x size, más frames

UI SPRITES:
├── Health hearts: 3 states
├── Dash cooldown indicator
├── Data orb icon
└── Level exit portal
```

```
DÍA 5-6: Backgrounds + Tiles

CITYSCAPE BACKGROUNDS:
├── Parallax layer 1 (far): city silhouette, 2 colors
├── Parallax layer 2 (mid): buildings, neon signs
├── Parallax layer 3 (near): pipes, cables
└── Foreground: platforms, interactivos

TILEMAP TILES:
├── Ground: dark metal, neon trim
├── Platforms: grating, pass-through
├── Walls: concrete, industrial
├── Hazards: electric, spikes
├── Decorations: signs, pipes, vents
└── Variations: 2-3 por tile para variety

PROPS:
├── Data orbs: glowing cyan spheres
├── Power-ups: neon icons
├── Doors: metal with neon trim
└── Exit portal: swirling neon vortex
```

```
DÍA 7: Post-processing

SPRITE CLEANUP:
├── Remove backgrounds (rembg)
├── Fix any inconsistencies
├── Verify animation timing
├── Exportar como PNG
└── Importar a Godot

PALETTE ADJUSTMENT:
├── Unificar tonos
├── Ensure consistency
├── Add to project as resources
└── Document palette
```

### Fase 3: Sistema de juego (Semana 4)

```
DÍA 1-2: Camera + Effects

CAMERA:
├── Follows player smoothly
├── Look-ahead: player direction
├── Slight zoom en dash
├── Screen shake on hits
└── Bounds: no show outside level

PARTICLES:
├── Dust on land
├── Sparks on wall slide
├── Trail on dash
├── Death explosion
└── Hit effect

SCREEN EFFECTS:
├── Chromatic aberration (subtle)
├── Vignette (optional)
├── Speed lines on dash
└── Flash on damage
```

```
DÍA 3-4: Enemy AI

DRONE AI:
├── State: patrol
│   ├── Move between 2 points
│   ├── Pause at each end
│   └── Change direction
├── Detection: Area2D overlap
│   └── If player enters: chase
└── Attack: shoot projectile every 2s

TURRET AI:
├── State: idle (default)
│   ├── Scan for player
│   └── If player in range: aim
├── Fire: cuando aligned con player
│   └── Bullet spawns, travels toward player
└── No movement

SECURITY BOT AI:
├── State: idle
│   ├── Wait for player
│   └── If player detected: chase
├── Chase:
│   ├── Move toward player
│   ├── Jump if blocked
│   └── Attack on contact
└── Return:
    └── If player out of sight for 3s: return to start
```

```
DÍA 5-6: Boss fight

BOSS: SECURITY MAINFRAME
├── Size: 4x player
├── Health: 10 hits
├── States:
│   ├── Phase 1 (100-50% HP):
│   │   ├── Sweep: horizontal attack
│   │   ├── Spawn drones (2)
│   │   └── Laser grid (avoid by dashing)
│   ├── Phase 2 (50-25% HP):
│   │   ├── Adds bullet hell patterns
│   │   ├── Faster movement
│   │   └── More drones
│   └── Phase 3 (25-0% HP):
│       ├── Enrage: speed 2x
│       └── Desperate attacks

ATTACK PATTERNS:
├── Telegraph: Boss glows 0.5s before attack
├── Player must react
├── Safe spots en cada patrón
└── I-frames on damage taken
```

```
DÍA 7: Polish de sistemas

SAVING:
├── Auto-save on level complete
├── Save position, health, collectibles
├── Load on death: respawn at checkpoint
└── No manual save (keeps simple)

UI:
├── Health bar: top left
├── Dash cooldown: near player or HUD
├── Level progress: optional
├── Pause menu: ESC key
└── Game over screen: retry option

SOUND (placeholder):
├── Use royalty-free SFX initially
├── Jump: simple "boing"
├── Hit: "thud"
├── Collect: "ding"
└── Music: use from Asset Library o generate
```

### Fase 4: Niveles completos (Semana 5)

```
DÍA 1-2: Level 2 - Wall mechanics

LAYOUT:
├── Vertical section: learn wall jump
├── Long walls: practice wall slide
├── Combination: wall jump + dash
├── Enemies: turrets on walls
└── Mini-boss: wall-crawling enemy

DESIGN:
├── New tiles (walls más altos)
├── Warning signs para hazards
├── Checkpoints midway
└── Challenge: wall-to-wall jumping
```

```
DÍA 3-4: Level 3 - Enemies introduction

LAYOUT:
├── Horizontal level (más wide)
├── Mix of ground y platforms
├── Enemies: drones + bots
├── No boss, pero enemies más tough
└── Collectibles reward exploration

CHALLENGE:
├── Timing jumps con enemy bullets
├── Use dash para avoid
├── Find safe spots
└── Multiple paths
```

```
DÍA 5-6: Level 4 - Boss

BOSS FIGHT (see fase 3)
├── Large arena
├── Safe spots marked (visual hint)
├── Health bar for boss
├── Victory: portal to level 5
└── If die: respawn at arena start

ADDITIONAL:
├── Health pickup después de boss
├── Cutscene pre-boss (simple)
└── Checkpoint antes de arena
```

```
DÍA 7: Level 5 - Final challenge

LAYOUT:
├── Combination de todo
├── Walls + enemies + platforming
├── Long (2x normal level)
├── 2 mini-bosses
├── Final boss at end
└── Victory screen on completion

DESIGN:
├── Start easy, increase difficulty
├── Multiple paths (one easier)
├── Secrets for power-ups
├── Real challenge: final boss
└── Reward: completion celebration
```

### Fase 5: Audio + Polish (Semana 6)

```
DÍA 1-2: Music

OPTIONS:
├── Generate con Boomy/AIVA (AI)
├── Use royalty-free tracks
├── Find en Free Music Archive
└── Create custom con Bandlab

LEVEL MUSIC:
├── Level 1-2: Upbeat, electronic
├── Level 3: More tense
├── Level 4 Boss: Dramatic
├── Level 5: Intense final
└── Victory: Triumphant
```

```
DÍA 3-4: SFX

SFX CON AI:
├── ElevenLabs: para voice clips
├── Bark: para simple sounds
└── Manual: Audacity para edit

ESSENTIAL SFX:
├── Jump
├── Land (soft/hard)
├── Wall slide (sparks)
├── Dash (whoosh)
├── Hit (player)
├── Enemy hit
├── Collect item
├── Death
├── Victory
└── Menu select
```

```
DÍA 5-6: Final polish

GAMEPLAY:
├── Tweak all values (gravity, speed, etc.)
├── Playtest repeatedly
├── Adjust difficulty
├── Fix any bugs
└── Ensure no softlocks

VISUAL:
├── Adjust colors if needed
├── Final particle effects
├── Screen effects
└── Animations smooth
```

```
DÍA 7: Build + Export

EXPORT:
├── HTML5 (itch.io requirement)
├── Windows (optional)
├── Mac (optional)
├── Linux (optional)
└── Test exported builds
```

---

## 3. Estructura de scripts

```
📂 scripts/
│
├── 👤 player/
│   ├── player_controller.gd     # Movement principal
│   ├── player_state_machine.gd  # Estados (idle, run, jump, etc.)
│   ├── player_animation.gd      # Animation controller
│   ├── player_dash.gd           # Sistema de dash
│   └── player_health.gd        # Sistema de vida
│
├── 🌍 level/
│   ├── level_manager.gd        # Gestión de niveles
│   ├── checkpoint.gd           # Sistema de checkpoints
│   ├── camera.gd               # Camera controller
│   ├── parallax_background.gd  # Parallax layers
│   └── transition.gd           # Transiciones entre escenas
│
├── 👾 enemies/
│   ├── base_enemy.gd           # Clase base enemy
│   ├── drone.gd                # Drone enemy
│   ├── turret.gd               # Turret enemy
│   ├── security_bot.gd         # Security bot
│   ├── boss.gd                 # Boss base
│   └── boss_mainframe.gd      # Boss específico
│
├── 🎮 collectibles/
│   ├── data_orb.gd            # Collectible principal
│   ├── power_up.gd            # Power-ups
│   └── key.gd                 # Llaves
│
├── 🎵 audio/
│   ├── audio_manager.gd       # Singleton audio
│   ├── music_player.gd        # Gestión de música
│   └── sfx_player.gd          # Gestión de SFX
│
├── 🖥️ ui/
│   ├── hud.gd                 # HUD principal
│   ├── health_bar.gd         # Barra de vida
│   ├── dash_cooldown.gd      # Indicador dash
│   ├── pause_menu.gd          # Menú de pausa
│   ├── game_over.gd          # Pantalla game over
│   └── victory_screen.gd     # Pantalla victoria
│
└── 🧩 systems/
    ├── save_system.gd         # Guardado/carga
    ├── game_manager.gd        # Singleton principal
    └── particle_manager.gd   # Sistema de partículas
```

---

## 4. Prompts para AI

### Character sprites:

```
BASE PROMPT:
"pixel art ninja cyberpunk character, 32x32 sprites,
facing front, standing pose, transparent background,
dark blue outfit with neon pink trim, white highlights,
cyberpunk neon city aesthetic, game sprite sheet"

ANIMATION PROMPTS:
"pixel art ninja walking, 8 frame walk cycle, 32x32"
"pixel art ninja jumping, 4 frame jump, 32x32"
"pixel art ninja dashing, 4 frame dash, 32x32"
```

### Tiles:

```
GROUND TILE:
"pixel art metal floor tile, dark gray, neon cyan trim on edge,
seamless texture, 16x16, top-down view"

PLATFORM TILE:
"pixel art grating platform tile, semi-transparent,
metal frame, 16x16, pass-through"

WALL TILE:
"pixel art concrete wall, industrial, dark gray,
rust streaks, neon sign partially visible, 16x16"
```

### Backgrounds:

```
FAR LAYER:
"pixel art cityscape silhouette, dark blue and purple,
distant buildings, no detail, 2 colors only, atmospheric"

MID LAYER:
"pixel art cyberpunk buildings, medium detail,
neon signs, windows lit, parallax ready, 16 colors max"

NEAR LAYER:
"pixel art foreground pipes and cables, detailed,
foreground elements, subtle parallax, 16x16 tiles"
```

---

## 5. Métricas de calidad

### Game feel:

| Aspecto | Target | Cómo medir |
|---------|--------|------------|
| Responsiveness | <1 frame input lag | Test manual |
| Jump feel | Satisfying arc | Playtest |
| Wall mechanics | Smooth transition | Test wall jumps |
| Dash | Powerful, usable | Playtest |
| Enemy difficulty | Challenging but fair | Playtest |

### Visual quality:

| Aspecto | Target | Cómo medir |
|---------|--------|------------|
| Consistency | Same style throughout | Visual inspection |
| Animation | Smooth, no jank | Play at 60fps |
| Particles | Subtle, not overwhelming | Visual inspection |
| Colors | Cohesive palette | Compare screenshots |

### Technical:

| Aspecto | Target | Cómo medir |
|---------|--------|------------|
| FPS | 60 stable | Profile |
| Load time | <3 seconds | Test on target |
| No crashes | 0 en playtest | Multiple runs |
| No softlocks | 0 | Full playthrough |

---

## 6. Timeline detallado

```
SEMANA 1: Prototype
├── Días 1-2: Setup + Player controller
├── Días 3-4: Wall mechanics
├── Días 5-7: Level 1 + basic enemies

SEMANA 2: Art (Characters)
├── Días 1-2: LoRA setup
├── Días 3-4: Player sprites
├── Días 5-7: Enemy sprites

SEMANA 3: Art (Environment)
├── Días 1-2: Backgrounds
├── Días 3-5: Tiles + props
├── Días 6-7: UI elements

SEMANA 4: Systems
├── Días 1-2: Camera + effects
├── Días 3-4: Enemy AI
├── Días 5-6: Boss
└── Días 7: Polish

SEMANA 5: Levels
├── Días 1-2: Level 2
├── Días 3-4: Level 3
├── Días 5-6: Level 4 (boss)
└── Días 7: Level 5

SEMANA 6: Audio + Polish
├── Días 1-2: Music
├── Días 3-4: SFX
├── Días 5-6: Final polish
└── Días 7: Export

TOTAL: 6 semanas
```

---

## 7. Publicación

### itch.io:

```
GAME PAGE:
├── Title: "Neon Ninja" o similar
├── Description: Synopsis, features, controls
├── Cover image: 630x500 pixels
├── Screenshots: 5-10 de gameplay
├── Trailer: Optional, 30-60 segundos
├── Genre: Platformer, Action, Indie
├── Tags: cyberpunk, ninja, action, 2d, pixel art
└── Price: Free o Pay what you want ($1 minimum)

FILES:
├── HTML5 build (principal)
├── Windows build (optional)
└── Source code (optional)

ANALYTICS:
├── Track plays, downloads
├── Collect feedback
├── Update based on feedback
```

---

## 8. Aprendizajes esperados

### Al terminar sabrás:

```
SKILLS DESARROLLADOS:
├── Pipeline completo de AI para game dev
├── Integración SD en workflow real
├── Godot 4 skills avanzados
├── Game feel y polish
├── Level design
└── Publicación en marketplaces

PARA PRÓXIMOS PROYECTOS:
├── Reutilizar sprites/enemigos
├── Workflow optimizado
├── Conocer qué funciona y qué no
└── Base para juegos más ambiciosos
```

---

_Volver a [README principal](../README.md)_
