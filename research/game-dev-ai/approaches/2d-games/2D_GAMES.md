# 🎮 Desarrollo de Juegos 2D con IA

_Guía especializada para crear juegos 2D utilizando herramientas de inteligencia artificial._

---

## 📋 Índice

1. [Stack Recomendado](#stack-recomendado)
2. [Generación de Sprites](#generación-de-sprites)
3. [Tilemap Generation](#tilemap-generation)
4. [Engine Selection](#engine-selection)
5. [Workflow Completo](#workflow-completo)
6. [Prompts por Tipo de Juego](#prompts-por-tipo-de-juego)

---

## Stack Recomendado

### Setup Óptimo para 2D

```
┌─────────────────────────────────────────────────────────────────┐
│              STACK PARA JUEGOS 2D CON IA                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ART                                                              │
│  ├─ Sprite Generation: Stable Diffusion + Fooocus                  │
│  ├─ Pixel Art: Fooocus + Pixelart LoRA                           │
│  ├─ Character Consistency: LoRA training (15-30 images)           │
│  └─ Tilemaps: Stable Diffusion + ControlNet                      │
│                                                                  │
│  ENGINE                                                           │
│  ├─ Godot 4 (Recomendado - Gratis, open source)                 │
│  ├─ Unity 2D (Professional, free tier)                           │
│  └─ GameMaker Studio 2 (Indie-friendly)                          │
│                                                                  │
│  AI CODE                                                          │
│  ├─ Ziva (Godot - Native plugin)                                 │
│  ├─ Unity MCP (Unity - 100+ tools)                              │
│  └─ Copilot/Claude (Universal)                                   │
│                                                                  │
│  AUDIO                                                            │
│  ├─ Music: Boomy o AIVA                                          │
│  ├─ SFX: ElevenLabs o Bark                                       │
│  └─ Voice: ElevenLabs                                             │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Generación de Sprites

### Pipeline de Sprites 2D

```
┌─────────────────────────────────────────────────────────────────┐
│                    SPRITE GENERATION PIPELINE                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. CHARACTER CONCEPT                                             │
│     └─→ Midjourney/Leo: "pixel art hero, 16-bit style"           │
│         Output: 4-8 concept variations                            │
│                                                                  │
│  2. SELECT BEST + CREATE REFERENCE                                │
│     └─→ Pick favorite, create style guide                        │
│         └─→ Compile reference sheet (front, side, back, expressions)│
│                                                                  │
│  3. CONSISTENCY TRAINING (LoRA)                                   │
│     └─→ Train LoRA with 15-30 character images                    │
│         Time: 30-60 minutes on GPU                                │
│         Result: Consistent character across all sprites            │
│                                                                  │
│  4. GENERATE SPRITE SHEETS                                        │
│     └─→ Idle: 4-8 frames                                         │
│     └─→ Walk: 6-12 frames                                        │
│     └─→ Jump: 4-8 frames                                         │
│     └─→ Attack: 4-12 frames (varies)                             │
│                                                                  │
│  5. POST-PROCESS                                                  │
│     └─→ Remove background (rembg)                                 │
│     └─→ Create sprite sheet grid (4x4, 8x4, etc.)                 │
│     └─→ Import to engine                                         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Configuración Stable Diffusion

```json
{
  "model": "stable-diffusion-xl-base-1.0",
  "prompt": "pixel art hero character, 16x16 sprites, 4 color palette, NES era, {pose} pose, transparent background",
  "negative_prompt": "photorealistic, modern, smooth, blurry, low quality, bad anatomy",
  "steps": 30,
  "cfg_scale": 7.5,
  "size": 512,
  "ControlNet": {
    "model": "control_v11f1e_sd15_tile",
    "weight": 0.5
  }
}
```

### Especificaciones de Sprite Sheets

| Game Style | Resolution | Frames/Animation | Grid |
|------------|------------|------------------|------|
| **Retro 8-bit** | 8x8, 16x16 | 2-4 | Linear |
| **Retro 16-bit** | 16x16, 32x32 | 4-8 | 4x2 o 4x4 |
| **Indie Modern** | 32x32, 64x64 | 6-10 | 4x4 |
| **HD Pixel** | 128x128+ | 8-12 | 4x4 o 8x4 |

---

## Tilemap Generation

### Generación con Stable Diffusion

```text
Prompt: "pixel art tileset, grass ground tile, top-down view, 
16x16, seamless texture, transparent background, 
game asset, 8-bit style, 4 color palette"
```

### Tilemap Sections

```
Tilemap Components:
├── Ground Tiles
│   ├── Grass (4-6 variations)
│   ├── Dirt
│   ├── Stone
│   ├── Water (animated)
│   └── Path/Road
├── Platform Tiles
│   ├── Wooden planks
│   ├── Metal
│   ├── Ice
│   └── Grass tops
├── Wall Tiles
│   ├── Brick
│   ├── Stone blocks
│   ├── Wood
│   └── Industrial
├── Decorative
│   ├── Flowers, bushes
│   ├── Rocks, logs
│   ├── Signs
│   └── Props
└─ Animated
    ├── Water
    ├── Lava
    ├── Fire
    └── Moving platforms
```

### Tools para Tilemaps

| Tool | Description | Link |
|------|-------------|------|
| **Tiled** | Map editor (manual + AI-friendly) | [Link](https://www.mapeditor.org) |
| **Tilesetter** | Tilemap generation | [Link](https://tilesetter.org) |
| **Charmed** | AI tilemap generator | [Link](https://charmed.ai) |
| **Asset Forge** | Create 2D assets | [Link](https://assetforge.io) |

---

## Engine Selection

### Comparativa 2D

| Feature | Godot 4 | Unity 2D | GameMaker |
|---------|---------|----------|-----------|
| **Price** | Free | Free/Paid | $39-99/yr |
| **AI Tools** | Ziva, AI Hub | Unity MCP, Copilot | Basic |
| **2D Physics** | Built-in | Built-in | Built-in |
| **Tilemap** | Native | Native | Native |
| **Learning Curve** | Low-Medium | Medium | Low |
| **Export** | PC, Mobile, Web | All platforms | PC, Mobile, Web |
| **AI Plugins** | Ziva (native) | Unity MCP (extensive) | Limited |

### Recomendaciones

```
JUEGOS 2D SÓLO CON IA:
├─→ Godot + Ziva (Mejor integración AI)
├─→ Unity + Unity MCP (Más herramientas)
└─→ SEELE/Rosebud (Text-to-game directo)

PARA PRINCIPIANTES:
└─→ Godot 4 + Ziva (Más fácil, documentación excelente)

PARA PROFESIONALES:
└─→ Unity 2D + Unity MCP (Más control, mejor tooling)

PARA GAME JAMS:
└─→ SEELE o Rosebud (Más rápido para prototipar)
```

---

## Workflow Completo

### 2D Platformer Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│              2D PLATFORMER: AI-POWERED WORKFLOW                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  PHASE 1: CONCEPT (Day 1)                                        │
│  ├─ Game idea + core mechanics (human)                           │
│  ├─ Art style defined with AI exploration                        │
│  └─ Create GDD (ChatGPT helps)                                   │
│                                                                  │
│  PHASE 2: ART ASSETS (Day 1-2)                                   │
│  ├─ Character sprite sheet generation (SD + LoRA)                 │
│  │   └─ Idle, walk, jump, attack, hurt, death                  │
│  ├─ Enemy sprites (3-5 types)                                    │
│  ├─ Tilemap generation (grass, platforms, hazards)               │
│  ├─ Background layers (2-3 parallax)                             │
│  ├─ UI elements (health, coins, menu)                           │
│  └─ Particle effects (dust, sparks, etc.)                       │
│                                                                  │
│  PHASE 3: CODE (Day 2-4)                                         │
│  ├─ Project setup (engine + AI tools)                          │
│  ├─ Player controller (movement, physics, abilities)            │
│  ├─ Level design (1-3 levels)                                   │
│  ├─ Enemy AI (patrol, chase, attack patterns)                  │
│  ├─ Collectibles and scoring                                    │
│  ├─ UI system (HUD, menus, pause)                               │
│  └─ Audio integration (BGM, SFX)                                │
│                                                                  │
│  PHASE 4: POLISH (Day 4-5)                                       │
│  ├─ Screen shake and hit feedback                               │
│  ├─ Particle effects                                            │
│  ├─ Animation smoothing                                         │
│  ├─ Sound polish                                                │
│  ├─ Level progression                                           │
│  └─ Final bug fixes                                             │
│                                                                  │
│  PHASE 5: EXPORT (Day 5)                                         │
│  ├─ Build for target platform(s)                                │
│  ├─ Performance optimization                                    │
│  └─ Playtest final build                                        │
│                                                                  │
│  TOTAL: ~5 days (vs 2-4 weeks traditional)                      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Prompts por Tipo de Juego

### Platformer

```text
// Character
"pixel art ninja character, 32x32 sprites, 8 frames walk cycle,
4 frames jump animation, transparent background,
cyberpunk neon aesthetic, clean outlines, game sprite sheet"

// Enemies
"pixel art slime enemy, green translucent, idle bounce animation,
16x16 sprites, 4 frames, transparent background,
pixel art style, game enemy"

// Tilemap
"pixel art forest background, parallax layers, 
seamless tileable, 16-bit style, dark fantasy,
transparent background, game background asset"

// UI
"pixel art heart icon, health symbol, red,
16x16, 8-bit style, transparent background,
game UI element, clean pixel art"
```

### RPG / Top-Down

```text
// Character
"pixel art knight character, front view, 32x32,
idle animation 4 frames, transparent background,
RPG style, 16-bit era, metallic armor"

// NPC
"pixel art village merchant, front view, 32x32,
idle animation 4 frames, holding items,
transparent background, friendly expression"

// Tileset
"pixel art RPG tileset, grass and dirt paths,
16x16 tiles, top-down view, seamless,
transparent background, 16-bit era style"

// Items
"pixel art sword, 32x32, gold handle,
RPG item, transparent background,
16-bit style, glowing effect"
```

### Puzzle

```text
// Game Pieces
"pixel art puzzle piece, jigsaw shape, 
blue and white, 32x32, transparent background,
game element, clean vector-like pixel art"

// Blocks
"pixel art wooden block, 32x32,
top-down isometric view, textured,
transparent background, puzzle game asset"

// Hazards
"pixel art spike trap, 16x16,
top-down view, metallic, animated open/close 2 frames,
transparent background, dungeon puzzle game"
```

### Shooter / Arcade

```text
// Player Ship
"pixel art spaceship, top-down view, 32x32,
blue thrusters, 4 frames thruster animation,
transparent background, arcade space shooter"

// Bullets
"pixel art laser bullet, blue, 8x8,
glowing effect, transparent background,
arcade shooter game asset, 3 variations: small, medium, large"

// Explosion
"pixel art explosion, 4 frames, 32x32,
orange red yellow gradient, looping animation,
transparent background, arcade effect"
```

---

## Game Jam Templates

### AI-Powered Game Jam Setup

```markdown
## 48-Hour Game Jam con AI

### Pre-Jam (1 hour)
- [ ] Install Godot 4 + Ziva plugin
- [ ] Set up Stable Diffusion / Leonardo AI
- [ ] Prepare Copilot in VS Code
- [ ] Create folder structure

### Hour 0-4: Concept
- [ ] Brainstorm with ChatGPT
- [ ] Choose game concept
- [ ] Write 1-page GDD
- [ ] Define art style

### Hour 4-16: Assets + Core
- [ ] Generate character sprites (AI)
- [ ] Generate enemies (AI)
- [ ] Generate tilemap (AI)
- [ ] Implement player controller
- [ ] Implement basic mechanics

### Hour 16-36: Gameplay
- [ ] Add all levels
- [ ] Implement enemies
- [ ] Add scoring
- [ ] Polish animations
- [ ] Add audio (AI generated)

### Hour 36-48: Polish
- [ ] Screen shake
- [ ] Particles
- [ ] Menu system
- [ ] Sound effects
- [ ] Final build

### Tools to Use:
- Art: Stable Diffusion + Leonardo AI
- Code: Godot + Ziva + Copilot
- Audio: Boomy + ElevenLabs
- Time: ChatGPT for planning
```

---

_Volver a [README principal](../README.md)_
