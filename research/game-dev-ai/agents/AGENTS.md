# 🤖 Agentes IA para Desarrollo de Videojuegos

_Guía completa sobre cómo usar agentes IA multi-tarea (CrewAI, AutoGen, LangChain MCP) para automatizar y масштабировать el desarrollo de videojuegos._

---

## 📋 Índice

1. [Conceptos Fundamentales](#conceptos-fundamentales)
2. [CrewAI para Game Dev](#crewai-para-game-dev)
3. [AutoGen Studios](#autogen-studios)
4. [LangChain MCP](#langchain-mcp)
5. [OpenClaw como Agente](#openclaw-como-agente)
6. [Pipeline Multi-Agente](#pipeline-multi-agente)
7. [Configuraciones](#configuraciones)

---

## Conceptos Fundamentales

### ¿Qué es un Agente IA?

```
┌──────────────────────────────────────────────────────────────┐
│                      AGENTE IA                                │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  Un agente es un sistema que puede:                           │
│  1. Percibir su entorno (tools, files, APIs)                 │
│  2. Tomar decisiones basadas en contexto                      │
│  3. Ejecutar acciones (calls, writes, commands)               │
│  4. Iterar basándose en feedback                              │
│                                                               │
│  Tipos de agentes:                                           │
│  ├─ Single Agent: Una IA con tools específicos                │
│  ├─ Multi-Agent: Múltiples agentes especializados            │
│  └─ Agentic AI: Agentes que delegan a otros agentes         │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

### Multi-Agent Architecture para Game Dev

```
                    ┌─────────────────┐
                    │   GAME DESIGNER  │ ← Define concepto, mecánicas
                    │   (Orchestrator) │
                    └────────┬────────┘
                             │
           ┌─────────────────┼─────────────────┐
           │                 │                 │
           ▼                 ▼                 ▼
    ┌────────────┐   ┌────────────┐   ┌────────────┐
    │  ART DIR   │   │   CODER    │   │  SOUND     │
    │  (Assets)  │   │  (Code)    │   │  (Audio)   │
    └─────┬──────┘   └─────┬──────┘   └─────┬──────┘
          │                 │                 │
          └────────┬────────┴────────┬────────┘
                   ▼                 ▼
            ┌─────────────────────────────┐
            │      QUALITY ASSURANCE        │
            │    (Review, Testing, Fix)     │
            └─────────────────────────────┘
```

---

## CrewAI para Game Dev

### ¿Qué es CrewAI?

CrewAI es un framework para crear agentes IA que trabajan juntos en crews (equipos). Cada agente tiene un rol, objetivo y herramientas específicas.

### Instalación

```bash
pip install crewai
pip install crewai-tools

# O desde source
git clone https://github.com/crewAIInc/crewAI.git
cd crewAI && pip install -e .
```

### Ejemplo: Game Jam Crew

```python
# game_jam_crew.py
from crewai import Agent, Crew, Task, Process
from crewai_tools import SerperDevTool, DirectoryReadTool, FileWriteTool

# Tools
search_tool = SerperDevTool()
dir_tool = DirectoryReadTool()
write_tool = FileWriteTool()

# Agents
game_designer = Agent(
    role="Game Designer",
    goal="Create an engaging game concept within 48 hours",
    backstory="""You are a veteran game designer with 15 years 
    of experience in indie development. You specialize in 
    creating fun mechanics in tight timeframes.""",
    tools=[search_tool, write_tool],
    verbose=True
)

artist = Agent(
    role="Pixel Artist",
    goal="Create all visual assets needed for the game",
    backstory="""You are a pixel artist who has worked on 
    50+ shipped games. You can create consistent sprite 
    sheets and tilemaps quickly.""",
    tools=[dir_tool, write_tool],
    verbose=True
)

programmer = Agent(
    role="Game Developer",
    goal="Implement all game mechanics cleanly and completely",
    backstory="""You are a full-stack game developer who 
    specializes in Godot and Unity. You've shipped 20+ 
    games and can code fast without sacrificing quality.""",
    tools=[dir_tool, write_tool],
    verbose=True
)

qa_tester = Agent(
    role="QA Tester",
    goal="Find and document all bugs and issues",
    backstory="""You are a meticulous QA engineer who 
    cares about polish. You've found critical bugs in 
    AAA releases before launch.""",
    tools=[dir_tool, write_tool],
    verbose=True
)

# Tasks
concept_task = Task(
    description="""Create a complete game design document for a 
    game jam entry. Theme is 'time loops'. Include:
    - Game concept and elevator pitch
    - Core mechanics (max 3)
    - Control scheme
    - Art style reference
    - Audio direction
    
    Save as DESIGN.md""",
    agent=game_designer,
    expected_output="A complete game design document"
)

assets_task = Task(
    description="""Based on the design doc, create:
    - Player sprite sheet (idle, walk, jump, interact) - 4x4 grid
    - 3 enemy sprites
    - Tilemap tileset (ground, platform, hazard, decoration)
    - UI elements (health, score)
    
    Create placeholder images if AI image gen not available.
    Save all in /assets/ folder.""",
    agent=artist,
    expected_output="All game assets in /assets/"
)

code_task = Task(
    description="""Implement the complete game based on DESIGN.md:
    - Player controller (movement, jump, interact)
    - Enemy AI (basic chase/attack)
    - Level with tilemap
    - UI system
    - Win/lose conditions
    
    Use Godot 4 with GDScript.
    Save in /game/ folder.""",
    agent=programmer,
    expected_output="Complete playable game in /game/"
)

qa_task = Task(
    description="""Test the game thoroughly:
    - Play through entire game
    - Document any bugs found
    - Test edge cases (pause during action, resize window)
    - Check performance
    
    Create BUGS.md with findings.""",
    agent=qa_tester,
    expected_output="Bug report in BUGS.md"
)

# Crew
game_crew = Crew(
    agents=[game_designer, artist, programmer, qa_tester],
    tasks=[concept_task, assets_task, code_task, qa_task],
    process=Process.sequential,  # Sequential for game jam
    verbose=True
)

# Execute
result = game_crew.kickoff()
print(result)
```

### Game Dev Crew Avanzado

```python
# advanced_game_crew.py
from crewai import Agent, Crew, Task, Process

# Agents con roles más específicos
narrative_writer = Agent(
    role="Narrative Designer",
    goal="Create compelling story and dialogues",
    backstory="Expert writer with experience in interactive fiction",
    allow_delegation=True  # Puede delegar a otros agentes
)

ui_designer = Agent(
    role="UI/UX Designer",
    goal="Design intuitive game interfaces",
    backstory="UI specialist for games, knows game feel principles"
)

combat_designer = Agent(
    role="Combat System Designer",
    goal="Create satisfying combat mechanics",
    backstory="""Battle designer who has worked on RPGs and 
    action games. Understands weapon feel, hit feedback,
    and balance.""",
    allow_delegation=True
)

world_builder = Agent(
    role="World Designer",
    goal="Create immersive game environments",
    backstory="Level designer with expertise in pacing and flow"
)

audio_designer = Agent(
    role="Audio Designer",
    goal="Create all sound and music",
    backstory="Audio engineer specializing in game audio"
)

# Task hierarchy
main_story = Task(
    description="Create a 3-chapter story outline",
    agent=narrative_writer,
    tasks=[
        Task(description="Chapter 1: Introduction", ...),
        Task(description="Chapter 2: Rising action", ...),
        Task(description="Chapter 3: Climax and resolution", ...),
    ]
)

combat_system = Task(
    description="Design combat system with 5 weapons, 10 enemies",
    agent=combat_designer,
    tasks=[
        Task(description="Weapon mechanics", ...),
        Task(description="Enemy behaviors", ...),
        Task(description="Balance numbers", ...),
    ]
)
```

---

## AutoGen Studios

### ¿Qué es AutoGen?

AutoGen es un framework de Microsoft para crear aplicaciones con múltiples agentes que pueden conversar entre sí.

### Instalación

```bash
pip install autogen-agentchat autogen-code-executor

# Para Studio (GUI)
pip install autogenstudio
autogenstudio ui --port 8080
```

### Ejemplo: Game Builder con AutoGen

```python
# autogen_game_builder.py
import autogen
from autogen import ConversableAgent, GroupChat, GroupChatManager

# Configuration
config_list = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={"model": ["gpt-4o", "claude-sonnet-4"]}
)

llm_config = {
    "config_list": config_list,
    "temperature": 0.7,
}

# Agents
spec_writer = ConversableAgent(
    name="Game_Spec_Writer",
    system_message="""You are a game specification writer.
    Create detailed game specs based on user requirements.
    Focus on: gameplay mechanics, art style, technical specs.""",
    llm_config=llm_config,
)

coder = ConversableAgent(
    name="Game_Coder",
    system_message="""You are a game programmer.
    Write clean, complete game code based on specs.
    Output runnable code only.""",
    llm_config=llm_config,
)

artist = ConversableAgent(
    name="Game_Artist",
    system_message="""You are a game artist.
    Create detailed prompts for AI image generation.
    Describe sprites, environments, UI elements.""",
    llm_config=llm_config,
)

# Human-in-the-loop for approval
user_proxy = ConversableAgent(
    name="User",
    is_human_input_mode=True,
    human_input_mode="ALWAYS",
)

# Group Chat
group_chat = GroupChat(
    agents=[user_proxy, spec_writer, coder, artist],
    messages=[],
    max_round=20
)

manager = GroupChatManager(groupchat=group_chat, llm_config=llm_config)

# Initiate conversation
user_proxy.initiate_chat(
    manager,
    message="Build me a 2D platformer with wall jumping and dash mechanics. "
            "Use HTML5 Canvas for rendering."
)
```

### AutoGen Studio UI

```bash
# Iniciar AutoGen Studio
autogenstudio ui --port 8080

# Luego abrir en navegador: http://localhost:8080
```

```
┌─────────────────────────────────────────────────────────────┐
│                 AUTOGEN STUDIO                               │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐            │
│  │  AGENTS     │  │   SKILLS    │  │  WORKFLOWS  │            │
│  │  Manager    │  │   Library   │  │   Builder   │            │
│  └─────────────┘  └─────────────┘  └─────────────┘            │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐     │
│  │                                                      │     │
│  │   CHAT INTERFACE                                     │     │
│  │                                                      │     │
│  │   > User: Build a shooter game                       │     │
│  │   > SpecWriter: Creating game spec...                │     │
│  │   > Artist: Generating asset prompts...              │     │
│  │   > Coder: Implementing game...                     │     │
│  │                                                      │     │
│  └─────────────────────────────────────────────────────┘     │
│                                                              │
│  [Stop] [Clear] [Export]                                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## LangChain MCP

### LangChain + Model Context Protocol

LangChain se integra con MCP para dar a agentes acceso a herramientas externas.

### Ejemplo de Integración

```python
# langchain_mcp_game.py
from langchain.agents import Agent, Tool
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from mcp import Client as MCPClient

# Initialize MCP client
mcp_client = MCPClient(
    command=["npx", "unity-mcp-cli", "open", "./MyGameProject"]
)

# Tools from MCP
@mcp_client.tool()
def unity_create_gameobject(name: str, parent: str = None) -> dict:
    """Create a GameObject in Unity scene"""
    pass

@mcp_client.tool()
def unity_add_component(gameobject: str, component: str) -> dict:
    """Add component to Unity GameObject"""
    pass

@mcp_client.tool()
def unity_set_script(gameobject: str, script_path: str) -> dict:
    """Attach C# script to GameObject"""
    pass

# LangChain Agent
llm = ChatOpenAI(model="gpt-4o", temperature=0)

tools = [
    Tool(name="UnityCreate", func=unity_create_gameobject),
    Tool(name="UnityAddComponent", func=unity_add_component),
    Tool(name="UnitySetScript", func=unity_set_script),
]

prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a Unity game developer assistant.
    You have access to Unity Editor tools.
    Help the user build games by creating GameObjects,
    adding components, and writing scripts."""),
    ("human", "{input}"),
    ("agent", "{agent_scratchpad}"),
])

agent = Agent.from_llm_and_tools(
    llm=llm,
    tools=tools,
    prompt=prompt,
    verbose=True
)

# Use
result = agent.run("Create a player character with WASD movement and jump")
```

---

## OpenClaw como Agente

### OpenClaw para Game Dev

OpenClaw puede actuar como agente de game development:

```yaml
# Configuración de agente OpenClaw para game dev
agents:
  game_dev_agent:
    model: minimax/MiniMax-M2.7
    system: |
      You are an expert game developer AI.
      You have access to file system tools, 
      code execution, and can help build complete games.
      
      Capabilities:
      - Create and edit code files
      - Execute build commands
      - Run tests
      - Generate assets with external tools
      
      For Unity projects:
      - Use unity-mcp-cli for Unity integration
      - Generate C# scripts
      - Create prefabs via code
      
      For Godot:
      - Generate GDScript
      - Create .tscn scenes
      - Use godot-cli for testing
      
      Always:
      - Follow best practices for the engine
      - Include error handling
      - Test code before delivery
```

### Prompts para OpenClaw Game Dev

```text
"Create a complete Unity 2D platformer game in a folder called 
/platformer/. Include:
- PlayerController.cs with smooth movement, variable jump, wall slide
- EnemyController.cs with patrol and chase behavior
- GameManager.cs singleton for score, lives, game state
- UIManager.cs for HUD (health, score, pause)
- Main menu scene with play, options, quit
- Basic sprite placeholders
- Build settings for PC/WebGL

Use Unity 2022.3 LTS. Write production-ready code."
```

---

## Pipeline Multi-Agente

### Arquitectura Completa

```
┌─────────────────────────────────────────────────────────────────┐
│                    GAME DEV MULTI-AGENT PIPELINE                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  PHASE 1: CONCEPT (1 Agent)                                       │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │ GameDesigner:                                           │    │
│  │ • Analyze market trends                                │    │
│  │ • Create game concept                                  │    │
│  │ • Write GDD                                             │    │
│  │ • Estimate scope                                       │    │
│  └──────────────────────────────────────────────────────────┘    │
│                              ↓                                    │
│  PHASE 2: ASSETS (2-3 Agents)                                    │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │ ArtDirector → CharacterArtist → EnvironmentArtist       │    │
│  │                                                            │    │
│  │ ArtDirector:                                             │    │
│  │ • Create art direction doc                              │    │
│  │ • Define style guide                                    │    │
│  │ • Assign tasks to artists                              │    │
│  │                                                            │    │
│  │ CharacterArtist:                                        │    │
│  │ • Generate character sprites                            │    │
│  │ • Create sprite sheets                                  │    │
│  │ • Design UI elements                                    │    │
│  │                                                            │    │
│  │ EnvironmentArtist:                                       │    │
│  │ • Generate tilemaps                                     │    │
│  │ • Create background assets                              │    │
│  │ • Design props and objects                              │    │
│  └──────────────────────────────────────────────────────────┘    │
│                              ↓                                    │
│  PHASE 3: CODE (2-3 Agents)                                       │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │ LeadCoder: SystemsProgrammer + UIProgrammer + NetProgrammer│    │
│  │                                                            │    │
│  │ SystemsProgrammer:                                        │    │
│  │ • Game loop and state machine                            │    │
│  │ • Player controller                                      │    │
│  │ • Enemy AI                                               │    │
│  │ • Physics and collision                                  │    │
│  │                                                            │    │
│  │ UIProgrammer:                                             │    │
│  │ • HUD system                                             │    │
│  │ • Menus and navigation                                   │    │
│  │ • Settings and options                                  │    │
│  │                                                            │    │
│  │ NetProgrammer (if multiplayer):                          │    │
│  │ • Lobby system                                           │    │
│  │ • Player sync                                            │    │
│  │ • State synchronization                                  │    │
│  └──────────────────────────────────────────────────────────┘    │
│                              ↓                                    │
│  PHASE 4: AUDIO (1 Agent)                                         │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │ AudioDesigner:                                            │    │
│  │ • Generate BGM prompts                                   │    │
│  │ • Create SFX list                                        │    │
│  │ • Describe voice requirements                            │    │
│  └──────────────────────────────────────────────────────────┘    │
│                              ↓                                    │
│  PHASE 5: QA (1-2 Agents)                                        │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │ QAEngineer + Playtester:                                 │    │
│  │                                                            │    │
│  │ QAEngineer:                                              │    │
│  │ • Code review                                            │    │
│  │ • Find bugs and issues                                   │    │
│  │ • Write test cases                                       │    │
│  │ • Verify fixes                                           │    │
│  │                                                            │    │
│  │ Playtester (human or AI):                                │    │
│  │ • Play game end-to-end                                  │    │
│  │ • Report game feel issues                                │    │
│  │ • Validate fun factor                                    │    │
│  └──────────────────────────────────────────────────────────┘    │
│                              ↓                                    │
│  PHASE 6: INTEGRATION (LeadCoder)                                │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │ • Assemble all components                               │    │
│  │ • Fix integration issues                                 │    │
│  │ • Optimize performance                                  │    │
│  │ • Final build and test                                   │    │
│  └──────────────────────────────────────────────────────────┘    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### YAML Configuration

```yaml
# game_dev_crew.yaml
# CrewAI configuration for game development

crew:
  agents:
    - id: game_designer
      role: Game Designer
      goal: Create engaging game designs
      backstory: Expert game designer with industry experience
      
    - id: character_artist
      role: Character Artist
      goal: Create all character assets
      backstory: Pixel art specialist
      
    - id: environment_artist
      role: Environment Artist  
      goal: Create all environment and tileset assets
      backstory: Environment artist for indie games
      
    - id: systems_programmer
      role: Systems Programmer
      goal: Implement core game systems
      backstory: 10+ years game dev experience
      
    - id: ui_programmer
      role: UI Programmer
      goal: Build user interface systems
      backstory: UX specialist for games
      
    - id: qa_engineer
      role: QA Engineer
      goal: Ensure game quality
      backstory: Veteran game tester
      
  tasks:
    - id: design_game
      description: Create game design document
      agent: game_designer
      
    - id: create_characters
      description: Generate character sprites and animations
      agent: character_artist
      depends_on: [design_game]
      
    - id: create_environments
      description: Generate tilemaps and environment assets
      agent: environment_artist
      depends_on: [design_game]
      
    - id: implement_core
      description: Build core gameplay systems
      agent: systems_programmer
      depends_on: [design_game]
      
    - id: implement_ui
      description: Build UI and menus
      agent: ui_programmer
      depends_on: [design_game]
      
    - id: test_game
      description: Test and report bugs
      agent: qa_engineer
      depends_on: [implement_core, implement_ui, create_characters, create_environments]
      
    - id: fix_issues
      description: Fix all reported bugs
      agent: systems_programmer
      depends_on: [test_game]
      
  process: hierarchical
  manager_agent: game_designer
```

---

## Configuraciones

### CrewAI con Ollama (Local)

```python
# crewai_ollama.py
from crewai import Agent
from langchain.llms import Ollama

# Usar modelo local
llm = Ollama(model="llama3.2")

game_designer = Agent(
    role="Game Designer",
    goal="Create fun games",
    backstory="Expert developer",
    llm=llm  # Usar Ollama en vez de OpenAI
)
```

### AutoGen con Azure OpenAI

```python
# autogen_azure.py
import autogen

config_list = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    file_location=".",
    filter_dict={
        "provider": ["azure"],
        "model": ["gpt-4o", "gpt-4-turbo"]
    }
)

# Configuration for Azure
llm_config = {
    "config_list": config_list,
    "api_type": "azure",
    "api_version": "2024-02-01",
}
```

---

## Mejores Prácticas

### ✅ Hacer

1. **Define roles claros** - Cada agente debe tener responsabilidad única
2. **Usa dependencias** - Asegura que tareas están en orden correcto
3. **Human-in-the-loop** - Para decisiones importantes
4. **Logs detallados** - Para debugging de agents
5. **Retry logic** - Agentes pueden fallar

### ❌ No Hacer

1. **No overload agents** - Dale tools específicas, no todo
2. **No skip review** - Siempre revisa output de agentes
3. **No ignores errors** - Agentes pueden dar código incorrecto
4. **No over-engineer** - Empieza simple, escala si es necesario

---

## Recursos

- [CrewAI Documentation](https://docs.crewai.com)
- [AutoGen Documentation](https://microsoft.github.io/autogen/)
- [LangChain MCP](https://python.langchain.com/docs/integrations/mcp)
- [OpenClaw Documentation](https://docs.openclaw.ai)

---

_Volver a [README principal](../../README.md)_
