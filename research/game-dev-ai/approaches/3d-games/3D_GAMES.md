# 🌐 Desarrollo de Juegos 3D con IA

_Guía especializada para crear juegos 3D utilizando herramientas de inteligencia artificial._

---

## 📋 Índice

1. [Stack Recomendado](#stack-recomendado)
2. [Generación de Assets 3D](#generación-de-assets-3d)
3. [World Building](#world-building)
4. [Engine Selection](#engine-selection)
5. [Workflow Completo](#workflow-completo)
6. [Prompts por Tipo de Juego](#prompts-por-tipo-de-juego)

---

## Stack Recomendado

### Setup Óptimo para 3D

```
┌─────────────────────────────────────────────────────────────────┐
│              STACK PARA JUEGOS 3D CON IA                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  3D ASSET GENERATION                                             │
│  ├─ Text-to-3D: Tripo, Meshy, Scenario                          │
│  ├─ Image-to-3D: Tripo, One-2-3-45                              │
│  ├─ PBR Textures: Leonardo, Midjourney                          │
│  └─ Character: Mixamo + AI polish                               │
│                                                                  │
│  WORLD BUILDING                                                  │
│  ├─ Promethean AI (Unreal/Unity)                               │
│  ├─ World Creator ( Unity)                                      │
│  ├─ Gaia Pro                                                    │
│  └─ Landscape Auto Material                                     │
│                                                                  │
│  ENGINE                                                          │
│  ├─ Unreal Engine 5 (AAA features, Nanite, Lumen)              │
│  ├─ Unity (Good balance, extensive tutorials)                  │
│  └─ Godot 4 (Open source, improving 3D)                          │
│                                                                  │
│  AI CODE                                                          │
│  ├─ Unity MCP (Unity - 100+ tools)                             │
│  ├─ Copilot + Claude Code (Universal)                           │
│  └─ Custom LLM integration (Advanced)                          │
│                                                                  │
│  ANIMATION                                                       │
│  ├─ Mixamo (Auto-rigging + animations)                          │
│  ├─ Plask (Video to animation)                                  │
│  └─ Radicals (Motion capture)                                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Generación de Assets 3D

### Text-to-3D Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│                    3D ASSET PIPELINE                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. TEXT/IMAGE INPUT                                             │
│     └─→ "low poly knight character, holding sword"              │
│     └─→ Or: Upload reference image                              │
│                                                                  │
│  2. INITIAL GENERATION (30-60 seconds)                           │
│     ├─→ Tripo: "3D model, 30s"                                  │
│     ├─→ Meshy: "text-to-3D, 30s"                               │
│     └─→ Scenario: "AI-powered, 60s"                             │
│                                                                  │
│  3. REFINEMENT                                                   │
│     ├─→ Adjust pose                                             │
│     ├─→ Change style (low poly, realistic, stylized)            │
│     ├─→ Modify colors/textures                                  │
│     └─→ Add variations                                          │
│                                                                  │
│  4. EXPORT                                                       │
│     ├─→ Formats: FBX, GLB, OBJ, USD                             │
│     └─→ LODs generated (optional)                               │
│                                                                  │
│  5. OPTIMIZATION                                                 │
│     ├─→ Reduce polygon count                                    │
│     ├─→ UV unwrap                                               │
│     ├─→ Generate PBR textures                                   │
│     └─→ Import to engine                                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Tools Comparison

| Tool | Speed | Quality | Cost | Best For |
|------|-------|---------|------|----------|
| **Tripo** | 40s | ⭐⭐⭐⭐ | Freemium | Characters, props |
| **Meshy** | 30s | ⭐⭐⭐⭐ | Freemium | General purpose |
| **Scenario** | 60s | ⭐⭐⭐⭐⭐ | Paid | Game-ready |
| **One-2-3-45** | 60s | ⭐⭐⭐ | Free | Quick prototypes |
| **Masterpiece Studio** | 90s | ⭐⭐⭐⭐ | Freemium | Characters |

### Asset Types for 3D Games

```
3D GAME ASSETS
├── Characters
│   ├── Player (generated + Mixamo rigged)
│   ├── NPCs (variations)
│   ├── Enemies (multiple types)
│   └── Boss (larger, detailed)
├── Props
│   ├── Furniture
│   ├── Weapons
│   ├── Containers (chests, barrels)
│   └── Interactive objects
├── Environment
│   ├── Trees and plants
│   ├── Rocks and terrain features
│   ├── Buildings (modular)
│   └── Skyboxes/Cubemaps
├── Vehicles
│   ├── Cars
│   ├── Aircraft
│   └── Spacecraft
└─ Effects
    ├── Particles
    ├── Projectiles
    └── Magic effects
```

---

## World Building

### AI World Generation

| Tool | Engine | Price | Features |
|------|--------|-------|----------|
| **Promethean AI** | Unreal, Unity | $99+/mo | Full world generation |
| **World Creator** | Unity | $115 | Terrain, biomes |
| **Gaia Pro** | Unity | $75 | Procedural terrain |
| **MapMagic** | Unity | $90 | Node-based world gen |

### Workflow: AAA-Quality World

```
1. TERRAIN
   └─→ Promethean AI: "mountainous forest landscape"
   └─→ Or: Gaia Pro procedural generation
   └─→ Or: Manual terrain in engine

2. BIOMES
   └─→ Divide into biomes (forest, desert, snow)
   └─→ Configure materials per biome

3. PLACE ASSETS (AI-assisted)
   └─→ "Place 50 pine trees in forest area"
   └─→ "Add rocks along river bank"
   └─→ "Scatter grass throughout meadow"

4. LIGHTING
   └─→ Set up dynamic lighting
   └─→ Configure time of day
   └─→ Add fog/atmosphere

5. NAVIGATION
   └─→ Bake navigation meshes
   └─→ Configure NPC waypoints
```

### Promethean AI Commands

```text
"create medieval castle on hill"
"add forest around castle perimeter"
"place 30 trees with random rotation"
"generate river flowing through valley"
"add 10 enemy spawn points near castle"
"scatter props: barrels, crates, weapons"
"create path from castle to forest"
"add atmospheric fog, density 0.3"
```

---

## Engine Selection

### Comparativa 3D

| Feature | Unreal 5 | Unity | Godot 4 |
|---------|----------|-------|---------|
| **Price** | Free* | Free/Paid | Free |
| **Nanite** | ✅ Yes | ❌ | ❌ |
| **Lumen** | ✅ Yes | ❌ | ❌ |
| **Physics** | Chaos | PhysX/Flex | Jolt |
| **AI Integration** | Copilot/Claude | Unity MCP | Ziva |
| **3D Quality** | Highest | High | Medium-High |
| **Learning Curve** | High | Medium | Low-Medium |
| **Mobile** | ⚠️ Heavy | ✅ Excellent | ✅ Good |
| **VR/AR** | ✅ Good | ✅ Excellent | ⚠️ Limited |

*Unreal: 5% royalty after $1M revenue

### Recomendaciones 3D

```
AAA QUALITY / LARGE PROJECTS:
└─→ Unreal Engine 5
    • Best graphics (Nanite, Lumen)
    • Best for large open worlds
    • Promethean AI integration
    • Higher learning curve

MID-INDIES / BALANCE:
└─→ Unity
    • Good 3D + excellent tooling
    • Unity MCP available
    • Better for mobile
    • More tutorials/resources

SMALLER 3D PROJECTS / OPEN SOURCE:
└─→ Godot 4
    • Free, open source
    • Improving 3D capabilities
    • Lightweight
    • Less 3D-specific AI tools
```

---

## Workflow Completo

### 3D Game AI Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│              3D GAME: AI-POWERED WORKFLOW                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  PHASE 1: PRE-PRODUCTION (1-2 days)                              │
│  ├─ Concept + GDD                                               │
│  ├─ Art direction defined                                       │
│  ├─ Asset list created                                          │
│  └─ AI tools configured                                         │
│                                                                  │
│  PHASE 2: ASSET CREATION (3-7 days)                              │
│  ├─ Character models (Tripo/Meshy)                              │
│  │   └─ Generate base meshes                                   │
│  │   └─ Rig with Mixamo                                        │
│  │   └─ Create variations                                     │
│  ├─ Environment (Promethean AI / manual)                        │
│  │   └─ Terrain generation                                     │
│  │   └─ Place trees/rocks                                     │
│  │   └─ Build modular buildings                               │
│  ├─ Props (Tripo/Meshy)                                        │
│  ├─ Weapons and items                                          │
│  └─ UI elements (2D rendered or 3D)                             │
│                                                                  │
│  PHASE 3: IMPLEMENTATION (7-14 days)                            │
│  ├─ Project setup                                              │
│  ├─ Character controller (3rd person)                          │
│  ├─ Camera system                                              │
│  ├─ Combat system (if applicable)                              │
│  ├─ AI NPCs (pathfinding, behavior)                           │
│  ├─ Level design (AI-assisted)                                 │
│  ├─ UI system                                                  │
│  └─ Save system                                                │
│                                                                  │
│  PHASE 4: POLISH (5-7 days)                                     │
│  ├─ Animation polish                                           │
│  ├─ Lighting and atmosphere                                    │
│  ├─ Particle effects                                           │
│  ├─ Sound design                                               │
│  ├─ Performance optimization (Nanite/LODs)                     │
│  └─ Bug fixing                                                  │
│                                                                  │
│  PHASE 5: RELEASE (2-3 days)                                    │
│  ├─ Platform builds                                            │
│  ├─ Certification (if console)                                 │
│  └─ Launch preparation                                         │
│                                                                  │
│  TOTAL: ~3-4 weeks (vs 3-6 months traditional)                  │
│  Improvement: ~75% faster with AI                              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Prompts por Tipo de Juego

### First Person Shooter

```text
// Character / Weapon
"3D model military rifle, assault rifle style,
game-ready, PBR textures, 2K,
low poly optimization"

// Environment
"3D model abandoned warehouse interior,
modular pieces, industrial style,
PBR textures, game-ready"

// Props
"3D model ammo crate, wooden military style,
low poly, game-ready, 16x16x16 units"
```

### RPG / Adventure

```text
// Character
"3D model fantasy knight armor, full body,
T-pose, game-ready, PBR textures,
character creation style"

// Environment
"3D model medieval tavern interior,
modular walls, floor, ceiling,
warm lighting, game-ready"

// NPC
"3D model village elder NPC,
fantasy robes, holding staff,
game-ready, low poly style"
```

### Racing Game

```text
// Vehicle
"3D model sports car, low poly style,
game-ready, 4x LODs, PBR textures,
top-down or rear view reference"

// Environment
"3D model race track section, asphalt,
with guardrails, grandstands background,
game-ready, modular"

// Props
"3D model checkered flag, pole,
low poly, game-ready, animated"
```

### Survival / Open World

```text
// Character
"3D model survivor character,
worn clothes, backpack,
low poly, game-ready, rigged"

// Building
"3D model wooden shelter base,
survival game style, modular,
low poly, PBR textures"

// Crafting
"3D model crafting station,
survival game props, campfire style,
low poly, game-ready"
```

### Horror / Thriller

```text
// Enemy
"3D model horror creature, monster,
dark atmosphere, game-ready,
PBR textures, rigged"

// Environment
"3D model abandoned hospital corridor,
modular, dark atmosphere,
PBR textures, game-ready,
blood spatters included"

// Props
"3D model medical equipment,
hospital horror prop,
low poly, game-ready"
```

---

## Optimization Tips

### LOD Generation

```markdown
## LOD Levels for 3D Games

| LOD | Polygons | Distance | Use Case |
|-----|----------|----------|----------|
| LOD0 | 100% | 0-10m | Close-up, main view |
| LOD1 | 50% | 10-50m | Mid-distance |
| LOD2 | 25% | 50-100m | Far distance |
| LOD3 | 10% | 100m+ | Very far, crowd |

Tools: 
- Unreal: Hierarchical LOD System (built-in)
- Unity: LOD Group (built-in)
- Blender: Decimate + manually
```

### Texture Optimization

```
PBR TEXTURE SETS
├── Albedo (Color)
│   └── Resolution: 1K-2K for props, 2K-4K for characters
├── Normal
│   └── Same resolution as Albedo
├── Roughness
│   └── Can be packed or separate
├── Metallic
│   └── Can be packed or separate
└── AO
    └── 512-1K typically sufficient

COMPRESSION
- DXT5 for desktop
- ASTC for mobile
- BC7 for high quality
```

---

_Volver a [README principal](../README.md)_
