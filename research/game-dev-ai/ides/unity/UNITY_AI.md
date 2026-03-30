# 🎮 Unity + AI: Guía Completa

_Integración de herramientas de inteligencia artificial en el flujo de trabajo de Unity Game Engine._

---

## 📋 Índice

1. [Unity MCP - Setup Completo](#unity-mcp---setup-completo)
2. [Unity MCP - Herramientas](#unity-mcp---herramientas)
3. [Workflows con IA](#workflows-con-ia)
4. [Code Generation Prompts](#code-generation-prompts)
5. [AI Plugins Adicionales](#ai-plugins-adicionales)
6. [Runtime AI Integration](#runtime-ai-integration)

---

## Unity MCP - Setup Completo

### ¿Qué es Unity MCP?

**Unity MCP** (Model Context Protocol) es un plugin que conecta Unity con agentes IA como Claude Code, Cursor, o cualquier cliente MCP. Permite que la IA controle Unity directamente.

### Características Principales

- ✅ **100+ herramientas nativas** para operar Unity Editor
- ✅ **AI Agents** - Compatible con Claude, Copilot, Cursor, Gemini
- ✅ **Skills** - Genera skills basadas en tu proyecto específico
- ✅ **Code + Tests** - Desarrolla mecánicas y pruébalas con IA
- ✅ **Runtime (in-game)** - Usa LLMs dentro del juego compilado
- ✅ **Debug support** - IA puede debuggear y corregir problemas

### Instalación

```bash
# Opción 1: CLI (recomendada)
npm install -g unity-mcp-cli

# Instalar plugin en proyecto Unity
unity-mcp-cli install-plugin ./MyUnityProject

# Login al servidor cloud
unity-mcp-cli login ./MyUnityProject

# Abrir proyecto (auto-conecta y genera skills)
unity-mcp-cli open ./MyUnityProject

# Esperar a que Unity esté listo
unity-mcp-cli wait-for-ready ./MyUnityProject
```

### Instalación Manual (GUI)

```
1. Descargar: https://github.com/IvanMurzak/Unity-MCP/releases/latest/download/AI-Game-Dev-Installer.unitypackage
2. Importar en Unity: Assets → Import Package → Custom Package
3. O hacer doble-click en el archivo .unitypackage
4. Abrir Window → AI Game Developer
5. Click "Auto-generate Skills" (recomendado)
6. O configurar MCP manualmente
```

### Configuración del Cliente AI

```json
// Configuración para Claude Code (~/.claude/mcp.json)
{
  "mcpServers": {
    "ai-game-developer": {
      "command": "/path/to/unity-mcp-server",
      "args": [
        "--port=8080",
        "--plugin-timeout=10000",
        "--client-transport=stdio"
      ]
    }
  }
}
```

### Requisitos

```
⚠️ IMPORTANTE: La ruta del proyecto NO puede contener espacios

✅ Correcto:  C:/MyProjects/MyProject
❌ Incorrecto:  C:/My Projects/MyProject
❌ Incorrecto:  C:/My Projects/My Project
❌ Incorrecto:  C:/MyProjects/My Project
```

---

## Unity MCP - Herramientas

### Herramientas de Proyecto y Assets

| Herramienta | Descripción |
|------------|-------------|
| `assets-copy` | Copiar asset de una ruta a otra |
| `assets-create-folder` | Crear nueva carpeta |
| `assets-delete` | Eliminar assets |
| `assets-find` | Buscar en Asset Database |
| `assets-find-built-in` | Buscar built-in assets |
| `assets-get-data` | Obtener datos de un asset |
| `assets-material-create` | Crear material con parámetros default |
| `assets-modify` | Modificar archivo de asset |
| `assets-move` | Mover/renombrar assets |
| `assets-prefab-create` | Crear prefab desde GameObject |
| `assets-prefab-instantiate` | Instanciar prefab en escena |
| `assets-prefab-open` | Abrir prefab en edit mode |
| `assets-prefab-save` | Guardar prefab |
| `assets-refresh` | Refrescar AssetDatabase |
| `assets-shader-list-all` | Listar todos los shaders |
| `package-add` | Instalar paquete del UPM |
| `package-list` | Listar paquetes instalados |
| `package-remove` | Desinstalar paquete |
| `package-search` | Buscar paquetes |

### Herramientas de Escena y Hierarchy

| Herramienta | Descripción |
|------------|-------------|
| `gameobject-component-add` | Añadir Component a GameObject |
| `gameobject-component-destroy` | Destruir component(s) |
| `gameobject-component-get` | Obtener info de un Component |
| `gameobject-component-list-all` | Listar nombres de todas las classes C# |
| `gameobject-component-modify` | Modificar un Component |
| `gameobject-create` | Crear nuevo GameObject |
| `gameobject-destroy` | Destruir GameObject recursivamente |
| `gameobject-duplicate` | Duplicar GameObjects |
| `gameobject-find` | Encontrar GameObject por información |
| `gameobject-modify` | Modificar GameObject y sus fields |
| `gameobject-set-parent` | Establecer padre a GameObjects |
| `scene-create` | Crear nueva escena |
| `scene-get-data` | Obtener lista de root GameObjects |
| `scene-list-opened` | Listar escenas abiertas |
| `scene-open` | Abrir escena desde archivo |
| `scene-save` | Guardar escena abierta |
| `scene-set-active` | Establecer escena activa |
| `scene-unload` | Descargar escena |

### Herramientas de Scripting y Editor

| Herramienta | Descripción |
|------------|-------------|
| `console-get-logs` | Obtener logs del Editor con filtros |
| `editor-application-get-state` | Estado del Editor (playmode, paused) |
| `editor-application-set-state` | Controlar estado del Editor |
| `editor-selection-get` | Obtener selección actual |
| `editor-selection-set` | Establecer selección |
| `reflection-method-call` | Llamar cualquier método C# con parámetros |
| `reflection-method-find` | Encontrar método usando Reflection |
| `script-delete` | Eliminar script(s) |
| `script-execute` | Compilar y ejecutar C# con Roslyn |
| `script-read` | Leer contenido de script |
| `script-update-or-create` | Actualizar o crear script con código |
| `tests-run` | Ejecutar Unity tests (EditMode/PlayMode) |

### Capturas de Pantalla

| Herramienta | Descripción |
|------------|-------------|
| `screenshot-camera` | Capturar screenshot desde cámara |
| `screenshot-game-view` | Capturar desde Game View |
| `screenshot-scene-view` | Capturar desde Scene View |

---

## Workflows con IA

### Workflow 1: Crear Mecánica de Juego Completa

```
User: "Create a 2D platformer with wall jumping and dash mechanics"

AI Response:
1. script-update-or-create: PlayerController.cs
   → Genera código completo con:
     - Movement (WASD, Smooth acceleration)
     - Jump (Variable height, coyote time, jump buffer)
     - Wall slide (Reduced gravity, wall stick)
     - Wall jump (Push away from wall, boost upward)
     - Dash (8-direction, i-frames, cooldown)

2. gameobject-create: "Player"
   → Crea GameObject vacío con PlayerController

3. assets-material-create: "PlayerMaterial"
   → Crea material para el sprite

4. scene-save: "Assets/Scenes/Gameplay.unity"
   → Guarda cambios
```

### Workflow 2: Generar Enemigo con IA

```
User: "Create an enemy that patrols between two points and attacks when player is in range"

AI Response:
1. script-update-or-create: PatrolEnemy.cs
   → Enemy con:
     - Waypoint system (2+ points)
     - State machine (Patrol, Chase, Attack, Return)
     - Line of sight detection
     - Attack with cooldown
     - Animation state transitions

2. gameobject-create: "PatrolEnemy"
3. gameobject-component-add: PatrolEnemy
4. gameobject-modify: Set waypoints
5. scene-save
```

### Workflow 3: Setup de Nivel con Tilemap

```
User: "Create a 2D level with platforms, walls, and spawn points"

AI Response:
1. gameobject-create: "Level1" (parent)
2. package-add: com.unity.2d.tilemap (si no existe)
3. Para cada tile:
   - gameobject-create: Tile
   - gameobject-modify: position, scale
4. gameobject-create: "SpawnPoint"
5. gameobject-create: "GoalPoint"
6. scene-save
```

### Workflow 4: Debugging con IA

```
User: "The player is falling through the floor after reloading the scene"

AI Response:
1. console-get-logs
   → "NullReferenceException at PlayerController.Awake()"
   
2. script-read: PlayerController.cs
   → Identifica problema: Rigidbody2D no está cacheado

3. script-update-or-create: PlayerController.cs
   → Fija con:
     - Cachear Rigidbody2D en Awake()
     - Verificar null antes de usar
     
4. tests-run: PlayerControllerTests
   → Valida fix
```

---

## Code Generation Prompts

### Prompts para Unity C#

```text
// Sistema de vida
"Write a Unity C# health system with:
- Max health, current health properties
- TakeDamage() method with invincibility frames
- Heal() method with max cap
- OnDeath event when health reaches 0
- Health bar UI sync (Image.fillAmount)
- Damage numbers floating text
- Use [SerializeField] for inspector exposure
- Apply damage types enum for different damage"

// Sistema de inventario
"Create a Unity C# inventory system with:
- Grid-based UI (6 rows x 5 columns)
- Drag and drop item slots
- Item pickup from world (trigger collider)
- Tooltip on hover showing item info
- Stack splitting (shift+click)
- Quick equip slots (1-5 keys)
- Save/load inventory to JSON
- Audio feedback on pickup/use
- Events: OnItemAdded, OnItemRemoved, OnItemUsed"

// Sistema de diálogo
"Write a Unity dialogue system with:
- ScriptableObject for Dialogue data (text, speaker, choices)
- Typewriter effect for text reveal
- Choice buttons for branching dialogue
- Portrait/sprite for speaker
- Condition system (requires item/flag to show option)
- Save/load dialogue progress
- Integration with Inventory system
- Animation triggers (shake, bounce)"

// Physics-based vehicle
"Create a Unity C# vehicle controller with:
- Rigidbody-based movement (not transform)
- Acceleration, braking, reverse
- Steering with drift feel
- Wheel colliders (4x)
- Speed-dependent steering
- Nitrous/boost system
- Surface friction variations
- Anti-roll stabilization
- Tire marks/skid trails"
```

### Prompts para AI en Runtime (NPCs)

```text
// NPC con ChatGPT integration
"Write a Unity C# script for an NPC that uses OpenAI's ChatGPT for dialogue:
- Streaming response display (typewriter)
- Context memory (last N messages)
- Character personality prompt injection
- Voice-to-text using Unity's Speech SDK
- Text-to-speech for NPC voice
- Emotion/animation triggers based on response
- Integration with NPC's Animator controller
- Rate limiting to control API costs
- Local fallback when offline"

// Dynamic narration system
"Create a Unity C# system for AI-generated narration:
- LLM generates narrative text based on game events
- TTS voice readout
- 3D positional audio attached to events
- Mood-appropriate music transitions
- Skip/dismiss functionality
- Privacy: Uses local LLM or approved API"
```

---

## AI Plugins Adicionales

### Unity AI Animation Plugin

```bash
# Instalar extensión AI Animation
npx unity-mcp-cli install-extension AI-Animation ./MyProject
```

Proporciona herramientas adicionales para:
- Generación de clips de animación
- Setup de Animator Controller
- Blend tree creation
- Animation event placement

### Unity AI ParticleSystem Plugin

```bash
# Instalar extensión AI ParticleSystem
npx unity-mcp-cli install-extension AI-ParticleSystem ./MyProject
```

Herramientas para:
- Diseño visual de partículas
- Módulos pre-configurados
- Effect presets

### Unity AI ProBuilder Plugin

```bash
# Instalar extensión AI ProBuilder
npx unity-mcp-cli install-extension AI-ProBuilder ./MyProject
```

Para:
- Generación de geometry
- UV unwrapping
- ProBuilder mesh operations

---

## Runtime AI Integration

### Usar LLM Dentro del Juego Compilado

Unity MCP también funciona en runtime, permitiendo IA dentro del juego:

```csharp
// ChessBotAI.cs - Ejemplo de uso runtime
using UnityMCP.Runtime;

public class ChessBotAI : MonoBehaviour
{
    private UnityMCPPluginRuntime _mcpPlugin;
    
    async void Start()
    {
        _mcpPlugin = UnityMCPPluginRuntime.Initialize(builder =>
        {
            builder.WithConfig(config =>
            {
                config.Host = "http://localhost:8080";
                config.Token = "your-token";
            });
            builder.WithToolsFromAssembly(Assembly.GetExecutingAssembly());
        }).Build();
        
        await _mcpPlugin.Connect();
    }
    
    // El LLM puede llamar este método para hacer jugadas
    [McpPluginTool("chess-do-turn")]
    public async Task<bool> DoTurn(int figureId, Vector2Int position)
    {
        return await MainThread.Instance.RunAsync(
            () => ChessGameController.Instance.DoTurn(figureId, position)
        );
    }
    
    [McpPluginTool("chess-get-board")]
    public async Task<BoardData> GetBoard()
    {
        return await MainThread.Instance.RunAsync(
            () => ChessGameController.Instance.GetBoardData()
        );
    }
}
```

### Ejemplo: NPC Inteligente con LLM

```csharp
// IntelligentNPC.cs
public class IntelligentNPC : MonoBehaviour
{
    [SerializeField] private string _characterPersonality = "You're a friendly merchant.";
    [SerializeField] private string _apiEndpoint = "https://api.openai.com/v1/chat/completions";
    
    private List<ChatMessage> _conversationHistory = new();
    private string _apiKey;
    
    async void Start()
    {
        _apiKey = Environment.GetEnvironmentVariable("OPENAI_API_KEY");
        
        // System prompt
        _conversationHistory.Add(new ChatMessage
        {
            Role = "system",
            Content = $"You are an NPC in a game. {_characterPersonality}"
        });
    }
    
    public async Task<string> SendMessage(string playerMessage)
    {
        _conversationHistory.Add(new ChatMessage
        {
            Role = "user",
            Content = playerMessage
        });
        
        var response = await OpenAIClient.Chat(_apiEndpoint, _apiKey, _conversationHistory);
        
        _conversationHistory.Add(new ChatMessage
        {
            Role = "assistant",
            Content = response
        });
        
        // Keep only last 10 messages for context window
        if (_conversationHistory.Count > 10)
            _conversationHistory.RemoveRange(0, 2);
        
        return response;
    }
    
    // Animation triggers based on response
    private void TriggerAnimationFromResponse(string response)
    {
        var animator = GetComponent<Animator>();
        
        if (response.Contains("!"))
            animator.SetTrigger("Excited");
        else if (response.Contains("?"))
            animator.SetTrigger("Thinking");
        else
            animator.SetTrigger("Talking");
    }
}
```

---

## Prompts para Workflows Completos

### "Create a Complete 2D Platformer"

```
"Build a complete 2D platformer in Unity with:
- Player character (sprite, animations: idle, run, jump, fall, attack)
- 5 different enemy types (basic walker, flyer, shooter, bouncy, boss)
- 3 levels with increasing difficulty
- Collectible items (coins, power-ups)
- Health system with UI
- Score system with high score
- Pause menu
- Game over screen
- Sound effects for all actions
- Background music

Use Unity 2D tilemap system for levels.
Include comments in code explaining each system."
```

### "Setup Multiplayer with Netcode for GameObjects"

```
"Create a Unity project setup for multiplayer using Netcode for GameObjects:
- NetworkManager component setup
- Player prefab with network sync
- Simple player movement (sync position)
- Host migration support
- Connection approval callback
- Player spawn system
- Basic chat system (UI + network)
- Lag compensation settings
- Network diagnostics UI

Include connection UI with IP input, host/join buttons."
```

---

## Mejores Prácticas

### ✅ Hacer

1. **Usa la AI para boilerplate** - Genera código repetitivo
2. **Mantén la AI en el editor** - Runtime tiene más consideraciones
3. **Revisa código generado** - IA no es infalible
4. **Usa tests** - Valida el código generado
5. **Divide tareas complejas** - Pide partes, no todo de golpe

### ❌ No Hacer

1. **No generes arquitectura completa** - Hazlo incrementalmente
2. **No confíes en datos de juego sensibles** - No envíes a APIs externas
3. **No ignores errores de compilación** - AI puede generar código con bugs
4. **No saltees el version control** - Haz commits frecuentes
5. **No uses código sin entenderlo** - Revisa lo que generas

---

## Recursos

- [Unity MCP GitHub](https://github.com/IvanMurzak/Unity-MCP)
- [Unity MCP Wiki](https://github.com/IvanMurzak/Unity-MCP/wiki)
- [Discord Community](https://discord.gg/cfbdMZX99G)
- [CLI Documentation](https://github.com/IvanMurzak/Unity-MCP/blob/main/cli/README.md)

---

_Volver a [README principal](../../README.md)_
