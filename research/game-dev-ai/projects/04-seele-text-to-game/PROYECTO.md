# 🚀 Proyecto 04: SEELE - Master Text-to-Game Pipeline

## Resumen Ejecutivo

**Objetivo:** Dominar SEELE como herramienta de text-to-game, entender sus capacidades y limitaciones, y crear un workflow optimizado para prototipado rápido.

**Herramientas principales:** SEELE, Claude Code, Godot/Unity (para refinamiento)

**Tiempo estimado:** 2-3 semanas

**Dificultad:** Baja-Media (la herramienta es user-friendly)

**Qué resuelve:** Validación rápida de ideas de juegos antes de invertir tiempo en desarrollo completo.

---

## 1. ¿Qué es SEELE?

### Overview:

```
SEELE es una plataforma de text-to-game que permite:
- Generar juegos completos desde descripciones en texto
- Exportar a Unity o Three.js
- Generar assets (sprites, 3D models, audio)
- Iterar conversacionalmente

CAPABILITIES (2026):
├── 2D game generation: 2-5 minutos
├── 3D game generation: 2-10 minutos
├── Sprite generation: 5-10 segundos
├── 3D model generation: 30-60 segundos
├── Sprite sheets: 15-30 segundos
├── BGM generation: 30-120 segundos
└── Export: Unity projects, WebGL
```

### Por qué aprenderlo:

```
POR QUÉ IMPORTA:
├── Validar ideas en MINUTOS vs semanas
├── Prototipar para game jams
├── Test mechanic concepts rápidamente
├── Presentar a publishers/inversores
├── Aprender qué hace falta para production
└── Base para workflow más serio
```

---

## 2. Plan de implementación

### Fase 1: Setup y exploración (Días 1-3)

```
DÍA 1: Cuenta + Setup

REGISTRO:
├── Ir a seele.ai
├── Crear cuenta (free tier disponible)
├── Verificar email
├── Login
└── Explorar dashboard

FREE TIER:
├── X generaciones por día
├── Modelos básicos
├── Export básico
└── Limitaciones en resolution

INTERFACE:
├── Playground para prompts
├── Historial de generaciones
├── Project management
├── Asset library
└── Settings
```

```
DÍA 2: Primeras pruebas

EXPERIMENTO 1: 2D Platformer simple
PROMPT:
"Create a simple 2D platformer where a character jumps
between floating platforms to collect coins and reach a goal.
Include basic movement, jump, and coin collection."

OBSERVAR:
- Qué genera exactamente
- Calidad del código
- Assets incluidos
- Tiempo de generación
- Qué falta

EXPERIMENTO 2: Top-down shooter
PROMPT:
"Create a top-down shooter where a spaceship moves with WASD,
shoots with spacebar, and must survive waves of enemies
that spawn from the edges."

OBSERVAR:
- Shooting mechanics
- Enemy spawning
- Wave system
- Difficulty
- Polish

EXPERIMENTO 3: Puzzle game
PROMPT:
"Create a simple puzzle game where you push boxes onto targets.
Classic Sokoban style with 5 levels."

OBSERVAR:
- Puzzle mechanics
- Level progression
- Win/lose conditions
- UI
```

```
DÍA 3: Documentar findings

DOCUMENTO: seele-capabilities.md

PARA CADA EXPERIMENTO:
├── Qué funcionó bien
├── Qué no funcionó
├── Calidad del output
├── Tiempo real
├── Problemas encontrados
└── Posibles fixes

IDENTIFICAR PATTERNS:
├── Qué tipos de juegos genera bien
├── Qué requiere demasiado
├── Errores comunes
└── Limitaciones conocidas
```

### Fase 2: Deep dive en features (Días 4-8)

```
DÍA 4-5: Generación de assets

PROBAR:
├── Sprites
│   ├── Character sprites
│   ├── Enemy sprites
│   ├── Items
│   └── UI elements
├── 3D Models
│   ├── Characters
│   ├── Props
│   └── Environments
└── Audio
    ├── Background music
    └── Sound effects

EVALUAR:
├── Calidad vs expectativas
├── Tiempo de generación
├── Formato de exportación
├── Integración en engines externos
└── Consistency entre assets
```

```
DÍA 6-7: Iteración conversacional

EXPERIMENTO: Refinar un juego existente

PASO 1: Generar juego base
PROMPT:
"Create a 2D platformer with a robot character.
Include basic movement and one level."

PASO 2: Añadir dash
"Makes the robot have a dash ability that gives invincibility frames."

PASO 3: Añadir enemies
"Add patrol robots that chase the player when they see them."

PASO 4: Mejorar gráficos
"Change the art style to neon cyberpunk with glowing effects."

PASO 5: Añadir sound
"Add electronic music and laser sound effects."

DOCUMENTAR:
├── Cómo funciona la iteración
├── Qué cambios son fáciles/difíciles
├── Límites de modificación
└── Guía de prompts para iteración
```

```
DÍA 8: Export y deployment

EXPORT OPTIONS:
├── Unity project (.unitypackage)
│   └── Importar a Unity, ajustar, build
├── WebGL (playable in browser)
│   └── Subir a itch.io directamente
└── Source code
    └── Revisar código generado

PRUEBAS:
├── Jugar exported game
├── Identificar bugs
├── Probar límites
└── Evaluar performance
```

### Fase 3: Workflow optimization (Días 9-12)

```
DÍA 9-10: Crear templates de prompts

TEMPLATE 1: Platformer
```markdown
Create a 2D platformer game with these specifications:

# Character
- [Character type]: [visual description]
- [Movement abilities]: [list abilities]
- [Special ability]: [if any]

# Mechanics
- [Core mechanic]: [description]
- [Goal]: [what player must do]
- [Fail condition]: [if any]

# Visual Style
- [Art style]: [e.g., pixel art, neon, etc.]
- [Color scheme]: [if specified]
- [Theme]: [e.g., cyberpunk, fantasy, etc.]

# Levels
- [Number]: [e.g., 3-5 levels]
- [Level design]: [basic description]

# Polish
- [Include]: [UI, sound, particles, etc.]
```

TEMPLATE 2: Top-down shooter
```markdown
Create a top-down shooter with:

# Player
- [Vehicle/character]: [description]
- [Weapons]: [primary, secondary if any]
- [Movement]: [2D or 8-directional]

# Enemies
- [Types]: [list enemy types]
- [Spawn patterns]: [how they appear]
- [Behavior]: [basic AI]

# Waves
- [Wave system]: [yes/no]
- [Difficulty scaling]: [how difficulty increases]
- [Boss]: [yes/no, description if yes]

# Visual
- [Style]: [description]
- [Effects]: [particles, screen shake, etc.]

# Audio
- [Music style]: [description]
- [SFX]: [important sounds]
```

TEMPLATE 3: Puzzle
```markdown
Create a [puzzle type] puzzle game:

# Core Mechanic
- [What player manipulates]: [boxes, balls, etc.]
- [Goal]: [what constitutes a win]
- [Rules]: [list rules]

# Level Design
- [Number of levels]: [e.g., 10]
- [Difficulty progression]: [easy to hard]
- [Special mechanics]: [if any unlock]

# UI
- [Menu]: [yes/no]
- [Level select]: [yes/no]
- [Hints]: [yes/no]

# Visual
- [Art style]: [description]
- [Animations]: [what animates]
```

DÍA 11: Automation scripts

PYTHON SCRIPT: seele_api_client.py
```python
import requests
import json
from typing import Dict, List, Optional

class SeeleClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.seele.ai/v1"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    
    def generate_game(self, prompt: str, 
                     game_type: str = "2d",
                     export_format: str = "unity") -> Dict:
        """Generate a game from text prompt"""
        payload = {
            "prompt": prompt,
            "type": game_type,
            "export": export_format
        }
        response = requests.post(
            f"{self.base_url}/generate",
            json=payload,
            headers=self.headers
        )
        return response.json()
    
    def generate_asset(self, asset_type: str, 
                      prompt: str) -> Dict:
        """Generate a single asset"""
        payload = {
            "type": asset_type,
            "prompt": prompt
        }
        response = requests.post(
            f"{self.base_url}/assets",
            json=payload,
            headers=self.headers
        )
        return response.json()
    
    def refine_game(self, game_id: str,
                    instruction: str) -> Dict:
        """Refine existing game"""
        payload = {
            "game_id": game_id,
            "instruction": instruction
        }
        response = requests.post(
            f"{self.base_url}/refine",
            json=payload,
            headers=self.headers
        )
        return response.json()
    
    def export_game(self, game_id: str,
                    format: str = "unity") -> str:
        """Get download URL for exported game"""
        response = requests.get(
            f"{self.base_url}/games/{game_id}/export",
            params={"format": format},
            headers=self.headers
        )
        return response.json().get("url")
```

DÍA 12: Documentar workflow optimizado

DOCUMENTO: seele-workflow-guide.md

SECTIONS:
├── Getting Started
├── Prompt Engineering for SEELE
├── Asset Generation
├── Iteration Workflow
├── Export and Deployment
├── Troubleshooting
└── Tips and Tricks
```

### Fase 4: Proyecto práctico (Días 13-18)

```
DÍA 13-15: Generar 3 prototipos

PROTOTIPO 1: Game jam concept
"Create a 3-level platformer about time manipulation where
you can slow down time. Control a scientist who must escape
a lab before it explodes. Include a time-slow ability
controlled by shift key, and collect power cores to open doors."

PROTOTIPO 2: Portfolio piece
"Create a polished top-down shooter demo with:
- Player spaceship with 8-directional movement
- 3 enemy types: drones, turrets, mothership
- Wave-based gameplay with increasing difficulty
- Particle effects for explosions
- Neon retro aesthetic"

PROTOTIPO 3: Genre exploration
"Create a stealth game where you play as a shadow
navigating through a laser-filled museum to steal artifacts.
Include hiding spots, alarm triggers, and 5 levels."

DÍA 16-18: Evaluar y refinar mejor prototipo

CRITERIOS DE EVALUACIÓN:
├── ¿Es jugable de principio a fin?
├── ¿Tiene game feel?
├── ¿Qué tan lejos está de "production-ready"?
├── ¿Qué toma más tiempo en refinar?
└── ¿Vale la pena seguir desarrollando?

REFINAMIENTO:
├── Elegir mejor prototipo
├── Iterar 5-10 veces para mejorar
├── Añadir polish
├── Probar en browser
└── Documentar proceso
```

---

## 3. Prompts optimizados para SEELE

### Templates por género:

```text
PLATFORMER (Basic):
"Create a 2D platformer with:
- Character: [description]
- Core mechanic: [jumping/moving]
- Goal: [reach end/collect items]
- Enemies: [types if any]
- [N] levels
- Art style: [pixel art/modern/etc]"

PLATFORMER (Advanced):
"Create a challenging 2D platformer with:
- Character: [detailed description including abilities]
- Movement: [movement details, double jump, wall jump, etc.]
- Core mechanics: [detailed mechanics]
- Enemies: [specific enemy types with behaviors]
- Boss: [boss fight at end if applicable]
- [N] levels with increasing difficulty
- Collectibles: [what and why]
- Art style: [detailed style description]
- Audio: [music mood, important SFX]"

TOP-DOWN SHOOTER:
"Create a top-down shooter with:
- Player: [vehicle/character description]
- Weapon: [primary weapon, secondary if any]
- Movement: [WASD/arrows/8-directional]
- Enemies: [list with behaviors]
- Wave system: [yes, with difficulty scaling]
- Power-ups: [types and effects]
- [N] waves + boss wave
- Visual style: [description]
- Effects: [particles, screen shake, etc.]"

PUZZLE:
"Create a [type] puzzle game:
- Core mechanic: [detailed description]
- Goal: [win condition]
- Rules: [clear rules]
- [N] levels with progression
- Difficulty curve: [easy to hard]
- UI: [menu, level select, hints]
- Visual style: [description]
- Animations: [what should animate]"
```

### Prompts para refinamiento:

```text
AÑADIR MECÁNICAS:
"Add a dash ability that:
- Is activated with [key]
- Makes player invincible during dash
- Has [duration] and [cooldown]
- Allows player to pass through enemies"

MEJORAR GRÁFICOS:
"Change the art style to [new style]:
- Color palette: [specific colors]
- Visual effects: [glow, particles, etc.]
- Keep gameplay the same"

AÑADIR SONIDO:
"Add:
- Background music: [mood/style]
- Jump sound: [type]
- Collect sound: [type]
- Enemy death: [type]
- [Any other important sounds]"

BALANCEAR:
"Balance the game:
- Make enemies [more/less] aggressive
- Increase player damage by [X]%
- Decrease enemy health by [X]%
- Make power-ups spawn [more/less] frequently"
```

---

## 4. Casos de uso práctico

### Game Jams:

```
GAME JAM WORKFLOW:

DÍA 1 (1-2 horas setup):
├── Generate game base with SEELE
├── Play and identify best mechanic
└── Document what to keep

DÍA 1-2 ( restantes):
├── Iterate to refine core mechanic
├── Add polish
├── Create simple menu
└── Build and submit

BENEFICIOS:
├── 60% less time en prototype
├── More time for polish
├── Focus on unique aspects
└── Higher quality submissions
```

### Validación de ideas:

```
VALIDATION WORKFLOW:

1. Generate concept prototype (30 min)
   → "Create a [game concept]"

2. Play and evaluate (1 hour)
   → Document: Is it fun? What's missing?

3. Refine based on feedback (1 hour)
   → Iterate to improve core mechanic

4. Decision (15 min)
   → ¿Valió la pena?
   → ¿Continuar desarrollo completo?
   → ¿Abandonar?

BENEFICIO: Save weeks of development on bad ideas
```

### Presentaciones a publishers:

```
PRESENTATION WORKFLOW:

1. Generate demo (1 hour)
   → Show playable prototype

2. Refine visuals (30 min)
   → Make it look presentable

3. Add voiceover (30 min)
   → Explain concept while playing

4. Export and share (15 min)
   → WebGL playable link

BENEFICIO: Professional-looking prototype without months of work
```

---

## 5. Limitaciones y workarounds

### SEELE limitations:

```
LIMITATION: Limited control over specific mechanics
WORKAROUND: Generate base, then refine iteratively

LIMITATION: Code quality varies
WORKAROUND: Review code before investing time

LIMITATION: Assets not always production-ready
WORKAROUND: Use as placeholders, replace later

LIMITATION: Export formats have quirks
WORKAROUND: Test early, adjust expectations

LIMITATION: Free tier has generation limits
WORKAROUND: Batch generations, save best results
```

### Common issues:

```markdown
## ISSUE: Game generated but controls don't work

CAUSE: Input handling missing or incorrect
FIX: "Add WASD movement with [speed]" and iterate

## ISSUE: Enemies don't spawn

CAUSE: Spawner not configured
FIX: "Add enemy spawners at [location]" or "Make enemies spawn every [time]"

## ISSUE: Collision not working

CAUSE: Collision layers not set
FIX: "Fix collision so player cannot walk through walls"

## ISSUE: Game is too easy/hard

CAUSE: Balance not dialed in
FIX: "Reduce enemy health to [X]", "Increase player speed to [X]"

## ISSUE: Visual style inconsistent

CAUSE: Multiple generation runs have different styles
FIX: "Redo all sprites in [specific style]", generate in single session
```

---

## 6. Comparativa con alternativas

### SEELE vs Rosebud:

| Feature | SEELE | Rosebud |
|---------|-------|---------|
| Unity export | ✅ | ❌ |
| Web export | ✅ | ✅ |
| Code quality | ⭐⭐⭐ | ⭐⭐ |
| Asset generation | ⭐⭐⭐⭐ | ⭐⭐ |
| Sprite sheets | ✅ | ⚠️ Limited |
| Animation library | 5M+ | Limited |
| Learning curve | Medium | Low |

### Cuando usar SEELE vs desarrollo manual:

```
USA SEELE CUANDO:
- Prototyping ideas rápidamente
- Game jams
- Validar concepts antes de invertir
- Presentaciones/preparaciones
- Aprendiendo game design

USA DESARROLLO MANUAL CUANDO:
- Proyecto commercial serio
- Mecánicas muy específicas
- Performance crítico
- Estilo visual único
- Budget/time para hacer bien
```

---

## 7. Métricas de evaluación

### Lo que debes evaluar en cada prototipo:

```
QUALITY CHECKLIST:
├── ☐ Game loads without errors
├── ☐ Controls responsive
├── ☐ Clear goal/objectives
├── ☐ Game can be won/lost
├── ☐ Visual style consistent
├── ☐ Audio present (at least basic)
├── ☐ No obvious bugs
├── ☐ Fun to play (subjective)
└── ☐ Worth continuing development

TIME EFFICIENCY:
├── Generation: [time]
├── Iteration: [time per refinement]
├── Polish: [time]
└── Total to playable: [time]

VALUE ASSESSMENT:
├── How close to "real game"?
├── What's missing for production?
├── How long would manual development take?
└── Is SEELE faster for this concept?
```

---

## 8. Entregables del proyecto

### Al finalizar:

```
📁 seele-mastery/
│
├── 📂 experiments/
│   ├── platformer_test/
│   ├── shooter_test/
│   ├── puzzle_test/
│   └── [others]
│
├── 📂 prompts/
│   ├── platformer_templates.md
│   ├── shooter_templates.md
│   ├── puzzle_templates.md
│   └── refinement_prompts.md
│
├── 📂 scripts/
│   └── seele_api_client.py
│
├── 📂 documentation/
│   ├── capabilities.md
│   ├── workflow_guide.md
│   └── troubleshooting.md
│
├── 📂 prototypes/
│   ├── time_slow_platformer/
│   ├── neon_shooter/
│   └── stealth_game/
│
└── 📂 findings/
    ├── what_works.md
    ├── what_doesnt_work.md
    └── recommendations.md
```

---

## 9. Siguientes pasos después de SEELE

```
SKILLS ADQUIRIDOS:
├── Prompt engineering para games
├── Rapid prototyping
├── Iteration workflows
└── Understanding AI limitations

PRÓXIMOS PROYECTOS:
1. Crear asset pack específico basado en SEELE outputs
2. Usar prototipos para validar ideas de juegos completos
3. Combinar SEELE + manual development
4. Exportar y refinar en Unity/Godot
5. Crear video教程 de workflow
```

---

## 10. Recursos

- [SEELE Official Site](https://seele.ai)
- [SEELE Documentation](https://docs.seele.ai)
- [SEELE Discord](https://discord.gg/seele)
- [Game Jam Templates](../resources/templates/game-jam-templates.md)

---

_Volver a [README principal](../README.md)_
