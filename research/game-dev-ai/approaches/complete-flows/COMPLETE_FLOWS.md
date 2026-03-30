# 🚀 Flujos Completos: Text-to-Game con IA

_Guía exhaustiva sobre plataformas y pipelines que permiten generar juegos completos desde descripciones de texto usando inteligencia artificial._

---

## 📋 Índice

1. [Plataformas Text-to-Game](#plataformas-text-to-game)
2. [SEELE - Guía Completa](#seele---guía-completa)
3. [Rosebud AI](#rosebud-ai)
4. [Flujo Multi-Stage](#flujo-multi-stage)
5. [Generación por Componentes](#generación-por-componentes)
6. [De Prototipo a Producción](#de-prototipo-a-producción)
7. [Comparativa de Plataformas](#comparativa-de-plataformas)

---

## Plataformas Text-to-Game

### Panorama General 2026

| Plataforma | 2D | 3D | Código | Assets | Export | Nivel |
|------------|----|----|--------|--------|--------|-------|
| **SEELE** | ✅ | ✅ | ✅ C#, JS | ✅ | Unity, WebGL | Producción |
| **Rosebud AI** | ✅ | ⚠️ | ✅ JS | ✅ | Web only | Prototipo |
| **GameMixer** | ✅ | ✅ | ✅ | ✅ | Web, Mobile | Beta |
| **Ludo.ai** | ⚠️ | ❌ | ❌ | ✅ | - | Assets |
| **Oasis (experimental)** | ✅ | ✅ | ✅ | ✅ | Real-time | Research |

---

## SEELE - Guía Completa

### ¿Qué es SEELE?

SEELE es la plataforma más completa de text-to-game en 2026:
- ✅ Dual-engine: Unity + Three.js
- ✅ 5M+ animaciones
- ✅ Pipeline de assets completo
- ✅ World model para física
- ✅ MCP integration (Claude AI)

### Especificaciones Técnicas

| Metric | Tiempo |
|--------|--------|
| 2D sprite | 5-10 segundos |
| 3D model | 30-60 segundos |
| Sprite sheet (16 frames) | 15-30 segundos |
| 2D game completo | 2-5 minutos |
| 3D game completo | 2-10 minutos |
| BGM | 30-120 segundos |
| Voice line | 2-5 segundos |
| Texture resolution | 512px - 4K |
| 3D poly count | 1K - 300K (ajustable) |

### Flujo de Trabajo SEELE

```
┌─────────────────────────────────────────────────────────────┐
│                    SEELE WORKFLOW                           │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  1. CONVERSATIONAL GAME CREATION                            │
│     └─→ "Create a 2D platformer with a ninja character"       │
│         - Genre detection: Platformer                        │
│         - Features: Jumping, wall-sliding, dash              │
│         - Assets: Ninja sprite, platforms, enemies            │
│                                                               │
│  2. INITIAL PROTOTYPE (2-5 min)                             │
│     ├─→ Game structure generated                              │
│     ├─→ Character with basic animations                       │
│     ├─→ Core mechanics implemented                            │
│     └─→ Simple level layout                                   │
│                                                               │
│  3. ITERATIVE REFINEMENT (conversational)                    │
│     ├─→ "Add wall-jumping ability"                            │
│     ├─→ "Make the dash ability have i-frames"                 │
│     ├─→ "Change art style to cyberpunk neon"                  │
│     └─→ "Add 3 more levels with increasing difficulty"        │
│                                                               │
│  4. ASSET GENERATION                                         │
│     ├─→ "Generate sprite sheet with 8-frame run cycle"        │
│     ├─→ "Create enemy sprites: 3 types"                      │
│     └─→ "Design UI: health bar, score, pause menu"           │
│                                                               │
│  5. EXPORT OPTIONS                                           │
│     ├─→ Unity project (.unitypackage)                         │
│     └─→ WebGL build (playable in browser)                     │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Prompts Optimizados para SEELE

```text
// Bien estructurado
"Create a 2D pixel art platformer with these specs:
- Character: Robot hero, blue color scheme
- Mechanics: Double jump, ground pound, wall climb
- Enemies: 3 types (patrol, flyer, boss)
- Levels: 5 levels with increasing difficulty
- Art style: Retro 16-bit, limited palette
- UI: Health bar, score counter, pause menu
- Audio: 8-bit background music, jump sound effects
Export as Unity project."

// Con constraints claros
"Build a 3D third-person shooter for me:
- Player character with auto-aim assist
- 10 waves of enemies, increasing in count
- Weapon: Laser rifle with unlimited ammo
- Environment: Sci-fi space station, 3 rooms
- Graphics: Low-poly style, neon lighting
- Performance: Must run at 60fps on mobile
- Output: Unity C# project, Android APK"
```

### MCP Integration con Claude

```python
# seele_mcp_client.py
import requests
import json

class SeeleMCPClient:
    """Cliente MCP para integración SEELE con Claude AI"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.seele.ai/mcp"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    
    def generate_game(self, description: str, export_format: str = "unity"):
        """Generar juego completo desde descripción"""
        payload = {
            "description": description,
            "export": export_format,
            "options": {
                "include_assets": True,
                "include_code": True,
                "include_audio": True,
                "optimize_for": "mobile"  # or "desktop"
            }
        }
        
        response = requests.post(
            f"{self.base_url}/generate",
            json=payload,
            headers=self.headers
        )
        
        return response.json()
    
    def generate_asset(self, asset_type: str, prompt: str):
        """Generar asset individual"""
        payload = {
            "type": asset_type,  # sprite, model, audio, animation
            "prompt": prompt
        }
        
        response = requests.post(
            f"{self.base_url}/assets",
            json=payload,
            headers=self.headers
        )
        
        return response.json()
    
    def refine_game(self, game_id: str, instruction: str):
        """Refinar juego existente con instrucción"""
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
```

---

## Rosebud AI

### Overview

Rosebud AI es ideal para principiantes y prototipado rápido:
- ✅ Interfaz conversacional simple
- ✅ PixelVibe generator
- ✅ Visual novel templates
- ⚠️ Solo web export
- ⚠️ Limitado en sprites sheets

### Comparación con SEELE

| Feature | SEELE | Rosebud |
|---------|-------|---------|
| **Unity export** | ✅ | ❌ |
| **Web export** | ✅ | ✅ |
| **2D games** | ✅ | ✅ |
| **3D games** | ✅ | ⚠️ Limited |
| **Sprite sheets** | ✅ Advanced | ⚠️ Basic |
| **Code generation** | ✅ C# + JS | ✅ JS only |
| **Audio generation** | ✅ Full | ⚠️ Basic |
| **Animation library** | 5M+ | Limited |
| **Learning curve** | Medium | Low |

---

## Flujo Multi-Stage

### Pipeline Completa de Generación

```
┌─────────────────────────────────────────────────────────────────┐
│              TEXT-TO-GAME COMPLETE PIPELINE                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  STAGE 1: CONCEPTUALIZATION (LLM)                                │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │ Input: "Create a metroidvania with time manipulation"     │    │
│  │                                                          │    │
│  │ Tasks:                                                    │    │
│  │ - Expand concept into full game design                    │    │
│  │ - Define core mechanics (time slow, time stop, rewind)   │    │
│  │ - List required assets (character, enemies, tiles)        │    │
│  │ - Design progression system                               │    │
│  │ - Create item/ability unlocks                             │    │
│  └─────────────────────────────────────────────────────────┘    │
│                            ↓                                     │
│  STAGE 2: ASSET GENERATION (AI Art)                              │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │ - Character sprite sheet (idle, walk, run, jump, attack) │    │
│  │ - Enemy sprites (3 types + boss)                        │    │
│  │ - Environment tiles (ground, platforms, hazards)         │    │
│  │ - Backgrounds (parallax layers)                         │    │
│  │ - UI elements (health, inventory, abilities)              │    │
│  │ - Particles and effects                                  │    │
│  │                                                          │    │
│  │ Tools: Stable Diffusion, Midjourney, Leonardo, Scenario  │    │
│  └─────────────────────────────────────────────────────────┘    │
│                            ↓                                     │
│  STAGE 3: CODE GENERATION (LLM + Copilot)                        │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │ - Game manager / state machine                           │    │
│  │ - Player controller (movement, abilities)                │    │
│  │ - Enemy AI (patrol, chase, attack patterns)              │    │
│  │ - Level system (room-based or open world)                │    │
│  │ - Time manipulation mechanics                            │    │
│  │ - Save/load system                                       │    │
│  │ - UI system (HUD, menus, inventory)                     │    │
│  │                                                          │    │
│  │ Tools: Claude Code, GitHub Copilot, Unity MCP            │    │
│  └─────────────────────────────────────────────────────────┘    │
│                            ↓                                     │
│  STAGE 4: AUDIO GENERATION                                       │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │ - Background music (3-4 tracks for different areas)      │    │
│  │ - Sound effects (jump, land, attack, enemy death)        │    │
│  │ - Voice lines (grunts, ability activation)               │    │
│  │                                                          │    │
│  │ Tools: Bark, Coqui Studio, ElevenLabs, Jukebox          │    │
│  └─────────────────────────────────────────────────────────┘    │
│                            ↓                                     │
│  STAGE 5: ASSEMBLY & INTEGRATION                                 │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │ - Import assets into engine                              │    │
│  │ - Wire up animations to code                             │    │
│  │ - Connect UI to game state                              │    │
│  │ - Test all mechanics                                    │    │
│  │ - Build and verify                                       │    │
│  │                                                          │    │
│  │ Tools: Unity, Godot, GameMaker, or text-to-game platform│    │
│  └─────────────────────────────────────────────────────────┘    │
│                            ↓                                     │
│  STAGE 6: POLISH & ITERATION                                    │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │ - Balance gameplay feel                                 │    │
│  │ - Add screen shake, hitstop, particles                   │    │
│  │ - Optimize performance                                   │    │
│  │ - Playtest and fix issues                               │    │
│  │ - Final export                                          │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

### Automatización con Agentes

```yaml
# game_dev_agents.yaml
# Ejemplo de pipeline multi-agente para game dev

agents:
  - name: game_designer
    role: Game Design Lead
    model: claude-sonnet-4
    goal: Create detailed game specification from user idea
    
  - name: asset_lead
    role: Art Director
    model: gemini-pro
    goal: Generate all visual assets using AI tools
    depends_on: [game_designer]
    
  - name: programmer
    role: Lead Developer
    model: claude-sonnet-4
    goal: Implement game mechanics and systems
    depends_on: [game_designer]
    
  - name: audio_engineer
    role: Audio Director
    model: gpt-4o
    goal: Generate and integrate audio
    depends_on: [game_designer]
    
  - name: integrator
    role: Build Engineer
    model: claude-sonnet-4
    goal: Assemble all components into playable game
    depends_on: [asset_lead, programmer, audio_engineer]
    
  - name: tester
    role: QA Lead
    model: claude-sonnet-4
    goal: Test and report issues
    depends_on: [integrator]
```

---

## Generación por Componentes

### Generación Modular de Juegos

```
┌─────────────────────────────────────────────────────────────────┐
│              COMPONENT-BASED GAME GENERATION                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  GAME COMPONENTS                                                 │
│  ================                                                 │
│                                                                   │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │ CHARACTERS  │  │   ENEMIES   │  │ ENVIRONMENT │              │
│  │             │  │             │  │             │              │
│  │ • Player    │  │ • Basic     │  │ • Tilemaps  │              │
│  │ • NPCs      │  │ • Advanced  │  │ • Buildings │              │
│  │ • Bosses    │  │ • Mini-boss │  │ • Nature    │              │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
│                                                                   │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │  UI/UX      │  │   AUDIO     │  │ GAMEPLAY    │              │
│  │             │  │             │  │ MECHANICS   │              │
│  │ • Menus     │  │ • BGM       │  │ • Movement  │              │
│  │ • HUD       │  │ • SFX       │  │ • Combat    │              │
│  │ • Inventory │  │ • Voice     │  │ • Puzzles   │              │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
│                                                                   │
│  Each component can be generated independently and combined      │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

### Templates por Género

| Genre | Components | Typical Generation Time |
|-------|-----------|------------------------|
| **Platformer** | Player, enemies (3), tileset, BGM, SFX | 10-20 min |
| **RPG** | Character, items, dialogue system, combat | 20-40 min |
| **Shooter** | Player, weapons (5), enemies (5), levels (3) | 15-30 min |
| **Puzzle** | Mechanic, level designs (10), UI | 10-20 min |
| **Adventure** | Player, NPCs (3), world, puzzles, story | 30-60 min |
| **Roguelike** | Player, enemies (8), items (20), procedural gen | 20-35 min |

---

## De Prototipo a Producción

### Checklist de Polishing

```markdown
## Prototipo → Producción Checklist

### Gameplay
- [ ] Balancing de dificultad
- [ ] Game feel (screen shake, hitstop, particles)
- [ ] Tutorial para mecánicas nuevas
- [ ] Progresión clara
- [ ] Sin exploits obvios
- [ ] Save system robusto

### Audio
- [ ] BGM para cada estado
- [ ] SFX para todas las acciones
- [ ] No audio quieto (silencio incómodo)
- [ ] Volumen balanceado
- [ ] Audio que no moleste en sesiones largas

### Visual
- [ ] Estilo consistente
- [ ] Sin assets placeholder
- [ ] Animaciones fluidas
- [ ] UI clara y legible
- [ ] Responsive en diferentes pantallas

### Performance
- [ ] 60fps en target platform
- [ ] Sin memory leaks
- [ ] Load times aceptables
- [ ] Sin freeze frames
- [ ] Compatible con target hardware

### Polish
- [ ] Menú de pausa
- [ ] Opciones de volumen
- [ ] Controles customizables
- [ ] Créditos
- [ ] Icono de app
- [ ] Splash screen
```

---

## Comparativa de Plataformas

### Text-to-Game: Comparativa Detallada

| Feature | SEELE | Rosebud | Ludo.ai | Oasis |
|---------|-------|---------|---------|-------|
| **Complete games** | ✅ | ✅ | ❌ | ✅ |
| **2D support** | ✅ | ✅ | ⚠️ | ✅ |
| **3D support** | ✅ | ⚠️ | ❌ | ✅ |
| **Unity export** | ✅ | ❌ | ❌ | ❌ |
| **Web export** | ✅ | ✅ | ✅ | ✅ |
| **Mobile export** | ⚠️ | ❌ | ❌ | ❌ |
| **Sprite generation** | ✅ | ✅ | ✅ | ✅ |
| **3D model gen** | ✅ | ⚠️ | ✅ | ✅ |
| **Code generation** | ✅ | ✅ | ❌ | ✅ |
| **Audio generation** | ✅ | ⚠️ | ❌ | ✅ |
| **Animation library** | 5M+ | Limited | ❌ | ❌ |
| **Free tier** | ✅ | ✅ | ✅ | ❌ |
| **API access** | ✅ | ⚠️ | ✅ | ❌ |
| **MCP integration** | ✅ | ❌ | ❌ | ❌ |

### Recomendaciones por Caso de Uso

| Use Case | Recommended Platform | Why |
|----------|---------------------|-----|
| **Indie dev prototyping** | SEELE | Full pipeline, Unity export |
| **Game jam entry** | Rosebud | Fast, web-based |
| **AAA pre-production** | SEELE + custom | Best quality, export control |
| **Learning game dev** | Rosebud / SEELE | Low barrier to entry |
| **Students** | SEELE | Educational discounts |
| **UGC platform** | Custom + Metaplay | Scale with player base |
| **Research/AI** | Oasis | Cutting edge, experimental |

---

## Métricas de Rendimiento

### SEELE vs Traditional Development

| Metric | Traditional | SEELE AI | Improvement |
|--------|-------------|----------|-------------|
| **Prototype time** | 40-80 hours | 2-10 minutes | **95% faster** |
| **First playable** | 2-3 weeks | Same day | **Day 1** |
| **Asset (per character)** | 8-16 hours | 30-60 seconds | **98% faster** |
| **Sprite sheet** | 2-4 hours | 15-30 seconds | **97% faster** |
| **Code first-run** | 78% success | 94% success | **+20%** |
| **Iteration cycles** | 5-8 rounds | 1-2 rounds | **75% less** |
| **Learning curve** | 3-6 months | Immediate | **∞** |

---

## Recursos

- [SEELE Documentation](https://www.seeles.ai/docs)
- [Rosebud AI Tutorials](https://docs.rosebud.ai)
- [Ludo.ai Research](https://ludo.ai)
- [Game AI Research Papers](https://arxiv.org/list/cs.AI/recent)

---

_Volver a [README principal](../README.md)_
