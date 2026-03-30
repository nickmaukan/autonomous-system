# 🎨 Proyecto 02: Asset Pack: Pixel Art Medieval Collection

## Resumen Ejecutivo

**Objetivo:** Crear un asset pack profesional de pixel art medieval para vender en marketplaces (Unity Asset Store, itch.io, Unreal Marketplace).

**Herramientas principales:** Stable Diffusion + Fooocus, Pixel Art LoRA, Aseprite (para post-processing)

**Tiempo estimado:** 3-4 semanas

**Dificultad:** Media

**Mercado potencial:** $200-1000 recurrentes por pack

**Qué resuelve:** Developers indie necesitan assets medievales de calidad sin pagar $500+ por assets premium.

---

## 1. Concepto del pack

### Qué incluir:

```
PIXEL ART MEDIEVAL COLLECTION
├── Characters (8-12)
│   ├── Player Knight (4 animations cada uno)
│   ├── Enemy types (3-4)
│   ├── NPCs (2-3)
│   └── Boss (1-2)
├── Environment (6-8 categories)
│   ├── Ground tiles (4 themes)
│   ├── Walls/Fortifications
│   ├── Buildings
│   ├── Trees/Foliage
│   ├── Water/Rivers
│   └── Caves/Dungeons
├── Props (10-15 categories)
│   ├── Weapons
│   ├── Armor
│   ├── Items (potions, scrolls, etc.)
│   ├── Food
│   └── Furniture
├── UI Elements
│   ├── Hearts/Health
│   ├── Gold/Coins
│   ├── Icons
│   └── Menu frames
└── Effects
    ├── Particles (dust, magic)
    ├── Projectiles
    └── Impact effects
```

### Estilo visual:

```
RESOLUTION: 16x16 y 32x32
PALETTE: 16-32 colores por资产
STYLE: 16-bit SNES/Genesis era
THEME: Medieval Fantasy (fantasía medieval)
QUALITY: Producción, no prototype
```

### Diferenciación:

```
POR QUÉ ESTE PACK VS OTROS:
├── Consistencia de estilo PERFECTA (mismo LoRA)
├── Animaciones completas (no solo idle)
├── Metadata estructurada (compatible con Tilemap)
├── Variations por tile (2-4 por tile)
├── Transparencias bien hechas
└── Documentación clara de uso
```

---

## 2. Plan de implementación

### Fase 1: Definición y setup (Días 1-3)

```
DÍA 1: Plan detallado del contenido

DOCUMENTO: medieval-pack-spec.md

CONTENIDO ESPECÍFICO A GENERAR:

Characters (requiere LoRA personalizado):
├── Knight_Player
│   ├── idle (4 frames)
│   ├── walk (8 frames)
│   ├── attack (6 frames)
│   ├── hurt (4 frames)
│   └── death (4 frames)
├── Archer_Player
│   ├── idle (4 frames)
│   ├── walk (8 frames)
│   ├── attack (6 frames)
│   ├── hurt (4 frames)
│   └── death (4 frames)
├── Skeleton_Enemy
│   ├── idle (4 frames)
│   ├── walk (8 frames)
│   ├── attack (6 frames)
│   └── death (4 frames)
├── Slime_Enemy
│   ├── idle (4 frames)
│   ├── move (6 frames)
│   └── death (3 frames)
└── Goblin_Enemy
    ├── idle (4 frames)
    ├── walk (8 frames)
    ├── attack (6 frames)
    └── hurt (4 frames)

Tiles (secciones reutilizables):
├── grass_floor (4 variations)
├── dirt_floor (4 variations)
├── stone_floor (4 variations)
├── castle_wall (4 variations)
├── castle_floor (4 variations)
├── forest_tiles (4 variations)
├── water_tiles (animated, 4 frames)
├── path_tiles (4 variations)
└── cave_tiles (4 variations)

Props:
├── swords (5 tipos)
├── shields (4 tipos)
├── potions (4 colores)
├── chests (2 estados: closed/open)
├── barrels (2 tipos)
├── crates (3 tipos)
├── torches (animated)
├── signs (4 mensajes)
├── food_items (6 tipos)
├── coins (3 denominaciones)
└── keys (3 tipos)

UI:
├── heart_full
├── heart_empty
├── coin_icon
├── potion_icon
├── menu_frame_small
├── menu_frame_large
└── button_sprites (3 estados)
```

DÍA 2: Setup de pipeline

HARDWARE CONFIG:
├── SD WebUI configurado
├── LoRA medieval entrenado (o usar estilo tokens)
├── Fooocus para generación rápida
└── Aseprite instalado

FOLDER STRUCTURE:
```
medieval-pack/
├── _source/
│   ├── characters/
│   │   ├── knight_player/
│   │   ├── archer_player/
│   │   └── enemies/
│   ├── tiles/
│   │   ├── grass/
│   │   ├── stone/
│   │   └── castle/
│   └── props/
│       ├── weapons/
│       ├── items/
│       └── furniture/
├── _output/
│   ├── characters/
│   ├── tiles/
│   └── props/
└── _final/
    ├── characters/
    ├── tiles/
    └── ui/
```

DÍA 3: Crear style guide

DOCUMENTO: style-guide.md

VISUAL STANDARDS:
├── Color palette principal
├── Proportions (8:9 para personajes)
├── Animation timing
├── Outline style
├── Shadow placement
└── Highlight placement

PALETA DE COLORES (ejemplo):
```
SKIN: #F0C8A0, #D4A574, #B8865A
ARMOR: #8B8B8B, #6B6B6B, #4B4B4B (plate)
       #8B4513, #654321, #3D2314 (leather)
HAIR: #2C1810, #4A3728, #8B6914
ACCENT: #C9A227, #FFD700 (gold trim)
ENVIRONMENT: #4A7023, #6B8E23, #228B22
```

---

### Fase 2: Generación de Characters (Días 4-10)

```
DÍA 4-5: Entrenar LoRA de estilo medieval

OBJETIVO: Crear LoRA que capture el estilo medieval consistente

CONFIGURACIÓN:
├── Dataset: 25-30 imágenes de personajes medievales
├── Resolution: 512x512
├── Network dim: 32
├── Training steps: 1500
└── Learning rate: 1e-4

VERIFICACIÓN:
├── Generar 5 personajes de prueba
├── Evaluar consistencia de estilo
├── Ajustar si es necesario
└── Guardar como medieval_style_v1.safetensors
```

```
DÍA 6-7: Generar Knight Player

WALK CYCLE (8 frames):
Frame 0: Standing neutral
Frame 1: Step forward left leg
Frame 2: Pass left leg
Frame 3: Left leg forward, right leg back
Frame 4: Pass right leg
Frame 5: Step right leg
Frame 6: Pass right leg
Frame 7: Return to neutral

ANIMATION PROMPTS:
"pixel art knight standing front view, transparent bg, 32x32"
"pixel art knight walking frame 1, transparent bg, 32x32"
"pixel art knight walking frame 2, transparent bg, 32x32"
... (8 prompts)

OUTPUT: 8 PNGs + sprite sheet 2x4 grid

DÍA 8-9: Generar Archer Player

MISMOPROCESO que Knight
Diferencia: Archer con bow en vez de sword

DÍA 10: Generar Enemies

SLIME:
- Idle: 4 frames (bounce up/down)
- Move: 6 frames (más bounce)
- Death: 3 frames (squish and disappear)

SKELETON:
- Reuse walk cycle del knight
- Diferentes proportions
- Diferent colors (bone white)

GOBLIN:
- Smaller que knight
- Different proportions
- Green skin tone
```

```
DÍA 10-11: Post-processing de characters

ASEPRITE WORKFLOW:
1. Import cada frame
2. Verify transparent background
3. Fix any inconsistencies manually
4. Adjust palette if needed
5. Export as PNG + sprite sheet
6. Create metadata JSON
```

### Fase 3: Generación de Tiles (Días 12-17)

```
DÍA 12-13: Ground tiles

GRASS:
├── Prompt: "pixel art grass tile, seamless, top-down, 16x16"
├── Generar 10 variations
├── Seleccionar 4 mejores
├── Verificar que hacen match entre sí
└── Crear tilemap preview

DIRT:
├── Prompt: "pixel art dirt floor tile, seamless, 16x16"
├── Mismo proceso
└── Verificar que combina con grass

STONE:
├── Prompt: "pixel art stone floor tile, seamless, 16x16"
├── Variations: light stone, dark stone, cracked
└── Combina con castle theme

DÍA 14-15: Walls y Buildings

CASTLE WALLS:
├── Prompt: "pixel art castle wall tile, 16x16"
├── Inner corner, outer corner, T-junction
├── Top, middle, bottom sections
└── Door tiles (optional)

WOODEN STRUCTURES:
├── Prompt: "pixel art wooden planks tile, seamless"
├── Fences, floors, walls
└── Brown palette

DÍA 16-17: Nature tiles

TREES:
├── Base/trunk
├── Canopy (multiple)
├── Shadow
└── Variation sin leaves

WATER:
├── Prompt: "pixel art water tile, animated, 4 frames"
├── Frame timing: 150ms
└── Seamless horizontal loop

ROCKS/BOULDERS:
├── Small, medium, large
├── Variations por size
└── Shadow en uno de los sides
```

### Fase 4: Props y UI (Días 18-23)

```
DÍA 18-19: Weapons

SWORDS (5 tipos):
├── Iron sword (basic)
├── Steel sword (mejorado)
├── Golden sword (legendary)
├── Fire sword (magical)
└── Ice sword (magical)

PROMPT TEMPLATE:
"pixel art {sword_type}, transparent background, 32x32, game asset"

SHIELDS (4 tipos):
├── Wooden shield
├── Iron shield
├── Knight shield (with emblem)
└── Magic shield

AXES, BOWS, STAFFS:
├── Battle axe
├── Hunting bow
├── Magic staff (fire, ice variants)
└── DAGGER

DÍA 20-21: Items

POTIONS:
├── Red (health)
├── Blue (mana)
├── Green (stamina)
└── Yellow (buff)

PROMPT: "pixel art {color} potion, glass bottle, transparent bg, 16x16"

CHESTS:
├── Closed state
├── Open state (empty)
├── Open state (with gold)
└── Different sizes

FOOD:
├── Bread
├── Meat
├── Apple
├── Cheese
├── Wine bottle
└── Pie

DÍA 22: UI Elements

HEARTS:
├── Full (3 variations)
├── Half
├── Empty (3 variations)
└── Outline only

ICONS:
├── Coin (gold)
├── Gem (3 colors)
├── Key (gold, silver, copper)
├── Scroll
└── Map

MENU FRAMES:
├── Button (normal, hover, pressed)
├── Window frame (small, large)
├── Portrait frame
└── Selection arrow

DÍA 23: Effects

PARTICLES:
├── Dust puff
├── Magic sparkles (fire, ice, electric)
├── Leaves
├── Snow
└── Rain

PROJECTILES:
├── Arrow
├── Fireball
├── Ice shard
├── Sword slash
└── Magic ring
```

### Fase 5: Assembly y polish (Días 24-28)

```
DÍA 24-25: Organize en folders finales

STRUCTURE:
```
medieval-pack-final/
├── Characters/
│   ├── Knight/
│   │   ├── idle/
│   │   ├── walk/
│   │   ├── attack/
│   │   ├── hurt/
│   │   ├── death/
│   │   ├── sprite_sheets/
│   │   └── metadata.json
│   ├── Archer/
│   └── Enemies/
│       ├── Slime/
│       ├── Skeleton/
│       └── Goblin/
├── Tiles/
│   ├── Grass/
│   ├── Dirt/
│   ├── Stone/
│   ├── Castle/
│   ├── Forest/
│   ├── Water/
│   └── paths/
├── Props/
│   ├── Weapons/
│   ├── Armor/
│   ├── Items/
│   └── Furniture/
├── UI/
│   ├── Hearts/
│   ├── Icons/
│   └── Frames/
└── Effects/
    ├── Particles/
    └── Projectiles/
```

DÍA 26-27: Documentation

README.md INCLUIDO EN PACK:

```markdown
# Medieval Pixel Art Collection

## Contents
- X characters with full animation sets
- X tiles (X variations each)
- X props
- X UI elements
- X effects

## Usage
1. Import into your game engine
2. Recommended settings:
   - Pixel perfect rendering
   - No anti-aliasing
   - Integer scale for retro look

## License
- Commercial use allowed
- No attribution required
- Can modify and use in your games

## Specs
- Resolution: 16x16 and 32x32
- Format: PNG with transparency
- Palette: 16-32 colors per asset
- Animation: Frame-based, variable timing
```

DÍA 28: Quality check

CHECKLIST:
- [ ] Todos los PNGs tienen transparencia correcta
- [ ] Sprites sheets están bien alineados
- [ ] Paleta consistente en todo el pack
- [ ] No hay sprites faltantes
- [ ] Nombres de archivos consistentes
- [ ] Metadata completa
- [ ] Documentation clara
```

---

## 3. Metadata y estructuración

### Formato de metadata:

```json
{
  "name": "knight_player",
  "category": "character",
  "resolution": "32x32",
  "animations": {
    "idle": {
      "frames": 4,
      "fps": 6,
      "loop": true
    },
    "walk": {
      "frames": 8,
      "fps": 10,
      "loop": true
    },
    "attack": {
      "frames": 6,
      "fps": 12,
      "loop": false
    }
  },
  "tags": ["player", "knight", "sword", "armor"],
  "palette": ["#C9A227", "#8B4513", "#4A3728"]
}
```

### Naming convention:

```
{category}_{name}_{animation}_{frame_number}.png

Ejemplos:
character_knight_idle_001.png
character_knight_walk_003.png
tile_grass_variation_01.png
prop_sword_iron_001.png
```

---

## 4. Publicación en marketplaces

### Unity Asset Store:

```
PREPARATION:
├── Crear Unity package (.unitypackage)
├── Screenshots (PNG, 1024x768 mínimo)
├── Icono del pack (512x512)
├── Preview video (opcional, 30 seg)
└── Documentation PDF

LISTING:
├── Título: "Medieval Pixel Art Collection"
├── Descripción: Lista completa de contenidos
├── Categoría: 2D > Characters > Pixel Art
├── Precio sugerido: $15-25
└── Tags: pixel art, medieval, fantasy, tileset, characters

APROBACIÓN: 5-7 días
```

### itch.io:

```
PREPARATION:
├── ZIP file con todos los assets
├── Cover image (630x500)
├── Screenshots (mínimo 5)
├── Description con HTML básico
└── Price ($5-15 recomendado)

FEATURES:
├── Pay what you want (mínimo $3)
├── Humble Bundle opción
└── Direct download + itch app
```

### Unreal Marketplace:

```
PREPARATION:
├── Crea proyecto de prueba en Unreal
├── Importa assets
├── Crea material instances
├── Empaqueta como Content Only project
└── Video demo de 2-3 min

APROBACIÓN: 7-14 días
```

---

## 5. Estimaciones de tiempo

| Task | Tiempo | Dificultad |
|------|--------|-------------|
| Setup + Style guide | 1 día | Fácil |
| LoRA training | 1 día | Media |
| Characters (8 types) | 6 días | Media |
| Tiles (8 categories) | 4 días | Fácil |
| Props (15 categories) | 4 días | Fácil |
| UI elements | 2 días | Fácil |
| Effects | 2 días | Media |
| Assembly + polish | 3 días | Fácil |
| Documentation | 1 día | Fácil |
| **TOTAL** | **25 días** | - |

**Si se trabaja medio tiempo: 6-8 semanas**
**Si se trabaja full-time: 3-4 semanas**

---

## 6. Análisis de mercado

### Precios típicos:

| Asset Pack | Precio | Contents |
|------------|--------|----------|
| Basic character set | $5-10 | 1-2 characters, basic animations |
| Full character pack | $15-25 | 5-8 characters, all animations |
| Tileset basic | $10-15 | 1 theme, 50-100 tiles |
| Tileset full | $25-40 | 3-4 themes, 200+ tiles |
| **Medieval Collection** | **$20-30** | **Everything medieval** |

### Competencia:

```
itch.io: Miles de pixel art packs
├── $1-5: Sprites sueltos, low quality
├── $5-15: Packs decentes, inconsistent
└── $20+: Premium, very high quality

OPORTUNIDAD:
├── Alta calidad (consistente)
├── Completo (todo medieval)
├── Bien documentado
└── Metadata estructurada
```

---

## 7. Métricas de éxito

### Targets:

| Métrica | Target | Timeline |
|---------|--------|----------|
| Assets totales | 500+ | Al finalizar |
| Sprites usables | >95% | Al finalizar |
| Tiempo de creación | <30 días | Deadline |
| Rating (stores) | 4+ stars | 6 meses |
| Ventas primeros 6 meses | 20-50 | 6 meses |

---

## 8. Potencial de expansión

### Después del primer pack:

```
EXPANSION PACKS:
├── Medieval Heroes (más characters)
├── Dark Dungeon (cave/dungeon tiles)
├── Enchanted Forest (forest/nature theme)
├── Medieval Furniture (interior tiles)
├── Weapons Extended (más armas)
├── Magic Effects Pack
└── Seasonal (Christmas, Halloween)

BUNDLES:
├── Medieval Bundle (todo medieval)
├── RPG Starter Pack (medieval + fantasy)
└── Retro Game Starter (multiple themes)
```

---

_Volver a [README principal](../README.md)_
