# 🎮 AI Game Development Knowledge Base

_Base de conocimiento exhaustiva sobre desarrollo de videojuegos con IA, agentes y herramientas modernas._

> ⚡ Última actualización: 2026-03-27 | Mantenida por Aurus ⚡ para Mauri Esp

---

## 📁 Estructura del Proyecto

```
game-dev-ai/
├── README.md                    ← Este archivo (índice principal)
│
├── 📂 approaches/               ← Aproximaciones por tipo de desarrollo
│   ├── sprites/                 ← Generación de sprites con IA
│   ├── code-generation/         ← Generación de código
│   ├── complete-flows/          ← Flujos completos (text-to-game)
│   ├── 2d-games/                ← Desarrollo de juegos 2D
│   └── 3d-games/                ← Desarrollo de juegos 3D
│
├── 📂 ides/                     ← Integraciones por motor/engine
│   ├── unity/                   ← Unity + AI
│   ├── godot/                   ← Godot + AI
│   ├── unreal/                  ← Unreal Engine + AI
│   ├── game-maker/              ← GameMaker Studio + AI
│   └── construct/               ← Construct + AI
│
├── 📂 agents/                   ← Agentes IA para game dev
│   ├── openclaw/                ← OpenClaw como agente de game dev
│   ├── crewai/                  ← CrewAI para pipelines de juego
│   ├── autogen/                 ← AutoGen multi-agent
│   ├── langchain-mcp/            ← LangChain + MCP
│   └── custom/                  ← Agentes personalizados
│
├── 📂 tools/                    ← Herramientas categorizadas
│   ├── sprite-generation/       ← Herramientas para sprites
│   ├── code-generation/         ← Herramientas para código
│   ├── level-generation/       ← Generación de niveles
│   ├── audio-generation/        ← Audio y música
│   ├── narrative-llm/            ← Narrativa y diálogos
│   ├── animation/               ← Animación
│   ├── physics-ai/              ← Física y simulación
│   ├── asset-pipeline/          ← Pipelines de assets
│   └── workflow-automation/     ← Automatización
│
└── 📂 resources/                ← Recursos adicionales
    ├── tutorials/               ← Tutoriales
    ├── courses/                 ← Cursos
    ├── communities/             ← Comunidades
    ├── prompts/                ← Prompts optimizados
    ├── datasets/               ← Datasets
    └── research-papers/        ← Papers de investigación
```

---

## 🚀 quick-start

### Para empezar desde cero:

1. **Define tu objetivo**: ¿2D o 3D? ¿Qué engine prefieres?
2. **Elige tu stack de IA**: Ver `tools/code-generation/` para opciones
3. **Configura tu pipeline**: Ver `approaches/complete-flows/` para flujos completos
4. **Automatiza con agentes**: Ver `agents/` para multi-agent workflows

### Recomendaciones por perfil:

| Perfil | Herramienta Principal | Secondary | Automatización |
|--------|---------------------|-----------|-----------------|
| **Indie 2D** | Godot + Ziva | Stable Diffusion | CrewAI |
| **Indie 3D** | Unity + Unity MCP | SEELE | AutoGen |
| **AAA/Pro** | Unreal + Copilot | Promethean AI | Agentes custom |
| **Prototipado rápido** | SEELE | Rosebud AI | OpenClaw |

---

## 📊 Estado del Ecosistema (2026)

### Tecnologías Maduras ✅
- Código: GitHub Copilot, Claude Code, ChatGPT
- Sprites 2D: Stable Diffusion, Leonardo AI, Midjourney
- Assets 3D: Scenario, Tripo, Meshy
- Engines: Unity MCP, Godot LLM Framework, Unreal AI

### Tecnologías Emergentes 🔄
- Text-to-game completo: SEELE, Rosebud AI
- Agentes multi-tarea: CrewAI, AutoGen
- World models: Promethean AI, Oasis
- NPCs interactivos: Charisma.ai, Convai, Inworld

### Preview/Experimental 🧪
- Generación en tiempo real: Oasis
- UGC con IA: Bitmagic (Supercell)
- AI playtesting: Tools internos de studios

---

## 🔄 Flujo de Trabajo Típico con IA

```
1. IDEACIÓN
   └─→ LLM para brainstorming + Ludo.ai para investigación

2. DISEÑO
   ├─→ Game design doc → ChatGPT/Claude
   ├─→ World building → Promethean AI
   └─→ Character concepts → Midjourney/Stable Diffusion

3. PROTOTIPADO
   ├─→ Código base → GitHub Copilot / Claude Code
   ├─→ Game maker → SEELE / Rosebud AI
   └─→ Nivel inicial → Charmed Tilemap Generator

4. PRODUCCIÓN DE ASSETS
   ├─→ Sprites → Stable Diffusion + ControlNet
   ├─→ 3D Models → Tripo/Meshy → Scenario
   ├─→ Audio → Bark, Coqui Studio, ElevenLabs
   └─→ Animations → Plask, Radicals

5. PROGRAMACIÓN
   ├─→ Scripts → Copilot/Claude Code
   ├─→ NPCs → Convai/Charisma.ai
   └─→ Physics → Havok AI

6. TESTING & POLISH
   ├─→ Playtesting → AI agents
   ├─→ Balance → ML systems
   └─→ Bug finding → Claude/ChatGPT

7. LIVE OPS (post-lanzamiento)
   └─→ Metaplay + AI analytics
```

---

## 📝 Contribuir a esta Knowledge Base

Esta KB es viva. Agrega:

- Nuevas herramientas que descubras
- Prompts optimizados que funcionen
- Workflows que hayas probado
- Tutorials que valgan la pena
- Issues o limitaciones encontradas

---

_“AI no reemplaza a los desarrolladores de juegos—los hace 10x más productivos.”_
