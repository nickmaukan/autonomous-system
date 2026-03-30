# 💻 Generación de Código para Videojuegos con IA

_Guía completa sobre cómo usar LLMs y herramientas de IA para escribir código de videojuegos._

---

## 📋 Índice

1. [Herramientas Principales](#herramientas-principales)
2. [Comparativa de Modelos](#comparativa-de-modelos)
3. [Prompts para Game Dev](#prompts-para-game-dev)
4. [Workflows por Engine](#workflows-por-engine)
5. [Code Snippets](#code-snippets)
6. [Debugging con IA](#debugging-con-ia)
7. [Testing Automatizado](#testing-automatizado)

---

## Herramientas Principales

### Asistentes de Código

| Herramienta | Mejor Para | Costo | Engines |
|------------|------------|-------|---------|
| **GitHub Copilot** | Autocompletado general | $10-19/mes | Todos |
| **Claude Code** | Código complejo, agentes | Variable | Todos |
| **ChatGPT** | Prototipado rápido | $20/mes (Plus) | Todos |
| **Cursor** | IDE con IA integrada | $20/mes | Todos |
| **Codeium** | Alternativa gratuita | Gratis | Todos |

### Herramientas Específicas para Game Dev

| Herramienta | Descripción | Engine |
|------------|-------------|--------|
| **Unity MCP** | Plugin + CLI para Unity con IA | Unity |
| **Ziva** | AI plugin nativo para Godot | Godot |
| **Godot LLM Framework** | Integración LLM en Godot | Godot |
| **Unreal AI Assist** | Blueprint + Python assist | Unreal |

---

## Comparativa de Modelos

### Modelos para Código de Juegos

| Modelo | Fortalezas | Debilidades | Mejor Uso |
|--------|-----------|-------------|-----------|
| **Claude 3.5/3.7 Sonnet** | Código limpio, contexto largo, razonamiento | Costoso | Código complejo, architecture |
| **GPT-4o** |通用, multimodal | Puede ser verbose | Prototipado, game design |
| **o1/o3 (OpenAI)** | Razonamiento profundo | Lento, caro | Algoritmos complejos |
| **Gemini 1.5 Pro** | Contexto 1M tokens | Optimizado Google | Proyectos grandes |
| **Code Llama** | Local, open source | Menor calidad | Privacidad, local |
| **Starcoder** | Open source, fine-tuned | Limitado | Stack específico |

### Rendimiento en Game Dev Tasks

```
Task                    | Claude | GPT-4 | Gemini | o1
------------------------|--------|-------|--------|----
Physics code            | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐   | ⭐⭐⭐⭐⭐
Game loop patterns      | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐
AI/NPC behavior         | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐   | ⭐⭐⭐⭐
UI systems              | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐
Networking/Multiplayer  | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐   | ⭐⭐⭐⭐
Shaders                 | ⭐⭐⭐   | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐
Performance optimization| ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐   | ⭐⭐⭐⭐⭐
```

---

## Prompts para Game Dev

### Prompts para Unity (C#)

```text
// Sistema de movimiento 2D
"Write a Unity C# script for a 2D platformer character controller.
Requirements:
- WASD movement
- Jump with variable height (hold to jump higher)
- Coyote time (0.1s grace period after leaving platform)
- Jump buffering (0.1s before landing)
- Ground check using raycast
- Smooth acceleration/deceleration
- Include Input.GetAxis for smooth movement"

// Sistema de inventario
"Create a Unity C# inventory system with:
- Grid-based inventory (6x5 slots)
- Drag and drop UI
- Item pickup from world
- Item tooltips on hover
- Stack limit of 64 per slot
- Save/load to JSON
- Events for inventory changes
Use Events for UI updates instead of direct references"

// AI de enemigo
"Write a Unity C# enemy AI script for a top-down shooter:
- State machine: Idle, Patrol, Chase, Attack, Flee
- Pathfinding using A*
- Line of sight detection
- Attack cooldown system
- Animation state transitions
- Knockback when hit
- Object pooling for projectiles"
```

### Prompts para Godot (GDScript)

```text
// Movimiento de personaje
"Write a Godot 4 GDScript for a 3D player character with:
- WASD movement
- Mouse look (first person camera)
- Sprint with stamina
- Crouch system
- Head bob effect
- State machine for movement states
- Jumping with double jump ability
- Wall sliding for platformer"

# Platformer character controller
extends CharacterBody2D

@export var speed: float = 300.0
@export var jump_velocity: float = -400.0
@export var gravity: float = 980.0
@export var coyote_time: float = 0.1
@export var jump_buffer: float = 0.1

# [ resto del código...]
```

### Prompts para Unreal (C++ / Blueprint)

```text
// GameplayAbility System
"Create an Unreal Engine 5 GameplayAbility for a sword slash attack:
- Must use GAS (GameplayAbilitySystem)
- Cooldown of 2 seconds
- Damage calculation based on character stats
- Visual effect (Niagara particle system)
- Sound effect
- Animation montage play
- Grant ability on character spawn
- AttributeSet for damage calculation"

// Widget de salud
"Create a UE5 UMG widget for health bar:
- Progress bar with gradient (red to green)
- Smooth animation when health changes
- Shake effect when taking damage
- Floating damage numbers
- Health text showing current/max
- Scale based on importance (boss health)"
```

### Prompts Genéricos Multi-Engine

```text
// Sistema de guardado
"Write a save game system that:
- Serializes game state to JSON
- Supports multiple save slots (10)
- Auto-save every 5 minutes
- Screenshots for save previews
- Version migration for updates
- Compresses data to reduce size
- Validates data integrity on load"

// Pool de objetos
"Implement an object pooling system:
- Pre-instantiate objects (no runtime allocations)
- Get() and Return() methods
- Automatic expansion if pool empty
- Configurable pool size per prefab
- Events for pool empty/full
- Memory usage tracking
- Reset objects to initial state on return"
```

---

## Workflows por Engine

### Unity + AI Workflow

```
┌──────────────────────────────────────────────────────────────┐
│                    UNITY + AI PIPELINE                       │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  1. PROJECT SETUP                                             │
│     └─→ Unity MCP CLI install                                 │
│         npx unity-mcp-cli install-plugin ./MyProject         │
│                                                               │
│  2. AI AGENT CONNECTION                                       │
│     └─→ Claude Code / Cursor / Windsurf                        │
│         └─→ Unity MCP bridge (100+ tools)                     │
│                                                               │
│  3. DEVELOPMENT LOOP                                          │
│     ┌─────────────────────────────────────────────────────┐   │
│     │ Ask AI: "Create player movement script"              │   │
│     │ ↓                                                   │   │
│     │ AI generates code using Unity MCP tools             │   │
│     │ ↓                                                   │   │
│     │ AI creates GameObjects, Components                  │   │
│     │ ↓                                                   │   │
│     │ AI runs tests / Play mode                           │   │
│     │ ↓                                                   │   │
│     │ Human reviews / iterates                            │   │
│     └─────────────────────────────────────────────────────┘   │
│                                                               │
│  4. SPECIFIC TASKS                                            │
│     ├─→ Code: script-update-or-create                          │
│     ├─→ Scene: gameobject-create, scene-save                   │
│     ├─→ Assets: assets-find, assets-prefab-create              │
│     └─→ Debug: console-get-logs, tests-run                     │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

### Godot + AI Workflow

```
┌──────────────────────────────────────────────────────────────┐
│                    GODOT + AI PIPELINE                       │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  1. PLUGIN INSTALLATION                                       │
│     └─→ Ziva AI (recommended)                                 │
│         - Download from ziva.sh                               │
│         - Install in Godot 4.2+                               │
│         - 20 free credits to start                            │
│                                                               │
│     OR                                                         │
│                                                               │
│     └─→ AI Assistant Hub (free)                                │
│         - Godot Asset Library                                  │
│         - Connect to Ollama/Gemini                            │
│                                                               │
│  2. NATURAL LANGUAGE DEVELOPMENT                              │
│                                                               │
│     Example prompts:                                          │
│     "Create a 3D character with WASD movement and jump"        │
│     "Build a complete inventory UI with drag-drop"            │
│     "Add enemy AI that patrols and chases player"             │
│                                                               │
│  3. CODE GENERATION FEATURES                                  │
│     ├─→ GDScript generation                                    │
│     ├─→ Scene creation from description                       │
│     ├─→ Node structure generation                             │
│     ├─→ Project context understanding                          │
│     └─→ Debug integration                                     │
│                                                               │
│  4. GDLLM FRAMEWORK (ADVANCED)                                │
│     └─→ Local LLMs in Godot                                   │
│         - GdLlama node (local models)                         │
│         - GdEmbedding for similarity                          │
│         - LLMDB for NPC dialogues                             │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

### Unreal + AI Workflow

```
┌──────────────────────────────────────────────────────────────┐
│                  UNREAL + AI PIPELINE                         │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  1. AI ASSISTANTS                                             │
│     ├─→ GitHub Copilot in VS Code                             │
│     │   - C++ and Blueprint completion                        │
│     │   - Comment generation                                  │
│     │   - Documentation lookup                                │
│     │                                                         │
│     └─→ Claude Code via terminal                              │
│         - Complex logic generation                            │
│         - Architecture planning                               │
│         - Code review and refactor                           │
│                                                               │
│  2. BLUEPRINT ASSISTANCE                                      │
│     └─→ Describe logic, AI writes Blueprint nodes             │
│         (manual implementation)                               │
│                                                               │
│  3. PYTHON SCRIPTING                                          │
│     └─→ Unreal Python API + AI                                │
│         - Asset automation                                    │
│         - Batch operations                                    │
│         - Pipeline scripts                                   │
│                                                               │
│  4. COMMON TASKS                                              │
│     ├─→ GameplayAbility: AI writes GAS setup                  │
│     ├─→ AI Behavior: BehaviorTree, EQS, Perception            │
│     ├─→ Animation: State Machine, Blend Space                  │
│     └─→ UI: UMG with Slate                                    │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

---

## Code Snippets

### Unity C# - Game Manager Singleton

```csharp
using UnityEngine;
using System;

public class GameManager : MonoBehaviour
{
    public static GameManager Instance { get; private set; }
    
    [Header("Game State")]
    public int currentLevel = 1;
    public int playerScore = 0;
    public float gameTime = 0f;
    public bool isPaused = false;
    
    [Header("Events")]
    public static event Action<int> OnLevelChanged;
    public static event Action<int> OnScoreChanged;
    public static event Action OnGamePaused;
    public static event Action OnGameResumed;
    
    void Awake()
    {
        if (Instance != null && Instance != this)
        {
            Destroy(gameObject);
            return;
        }
        Instance = this;
        DontDestroyOnLoad(gameObject);
    }
    
    void Update()
    {
        if (!isPaused)
            gameTime += Time.deltaTime;
    }
    
    public void AddScore(int points)
    {
        playerScore += points;
        OnScoreChanged?.Invoke(playerScore);
    }
    
    public void NextLevel()
    {
        currentLevel++;
        OnLevelChanged?.Invoke(currentLevel);
    }
    
    public void PauseGame()
    {
        isPaused = true;
        Time.timeScale = 0f;
        OnGamePaused?.Invoke();
    }
    
    public void ResumeGame()
    {
        isPaused = false;
        Time.timeScale = 1f;
        OnGameResumed?.Invoke();
    }
}
```

### Godot GDScript - State Machine

```gdscript
extends Node

class_name StateMachine

signal state_changed(from_state, to_state)

@export var initial_state: State

var current_state: State
var states: Dictionary = {}

func _ready():
    for child in get_children():
        if child is State:
            states[child.name.to_lower()] = child
            child.state_machine = self
    
    if initial_state:
        current_state = initial_state
        current_state.enter()

func _process(delta):
    if current_state:
        current_state.update(delta)

func _physics_process(delta):
    if current_state:
        current_state.physics_update(delta)

func transition_to(state_name: String):
    var new_state = states.get(state_name.to_lower())
    if new_state == null || new_state == current_state:
        return
    
    var old_state = current_state
    current_state.exit()
    current_state = new_state
    current_state.enter()
    state_changed.emit(old_state.name, new_state.name)
```

### Unreal C++ - Actor Component

```cpp
// FPHealthComponent.h
#pragma once

#include "CoreMinimal.h"
#include "Components/ActorComponent.h"
#include "FPHealthComponent.generated.h"

DECLARE_DYNAMIC_MULTICAST_DELEGATE_FourParams(
    FOnHealthChanged, 
    AActor*, Instigator, 
    UFPHealthComponent*, OwningComp, 
    float, NewHealth, 
    float, Delta
);

UCLASS( ClassGroup=(Custom), meta=(BlueprintSpawnableComponent) )
class GAME_API UFPHealthComponent : public UActorComponent
{
    GENERATED_BODY()

public:    
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category="Health")
    float MaxHealth = 100.f;
    
    UPROPERTY(ReplicatedUsing=OnRep_Health, BlueprintReadOnly)
    float CurrentHealth = 100.f;
    
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category="Health")
    bool bIsDead = false;
    
    UPROPERTY(BlueprintAssignable)
    FOnHealthChanged OnHealthChanged;
    
    UFPHealthComponent();
    
    UFUNCTION(BlueprintCallable, Category="Health")
    void TakeDamage(AActor* DamagedActor, float Damage, const UDamageType* DamageType, AController* EventInstigator, AActor* DamageCauser);
    
    UFUNCTION(BlueprintCallable, Category="Health")
    void Heal(float Amount);
    
protected:
    virtual void BeginPlay() override;
    
    UFUNCTION()
    void OnRep_Health(float OldHealth);
    
    void Die(AController* Killer);
    
    virtual void GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const override;
};
```

---

## Debugging con IA

### Workflow de Debug

```
1. Copy error message or buggy code
2. Ask AI: "Explain why this code is causing [error]"
3. Ask AI: "Fix this bug with explanation"
4. Apply fix
5. Ask AI: "How would you prevent this in the future?"
```

### Prompts para Debug

```text
// Error de Unity
"I'm getting this error in Unity:
'NullReferenceException: Object reference not set to an instance of an object'
at PlayerController.Update() line 42:
  movement = inputDirection * speed;
  
The full code is:
[pegcode]

What could cause this and how do I fix it?"

// Memory leak
"My Unity game runs fine for 5 minutes but then gets slower.
I suspect a memory leak. Here's my code for spawning enemies:

[code]

How can I identify and fix memory leaks in this pattern?"

// AI behavior bug
"My enemy AI in Godot keeps getting stuck in corners.
I'm using A* for pathfinding. Here's the relevant code:

[code]

How do I fix the stuck behavior?"
```

### AI Debugging Prompts Específicos

```text
// Performance issue
"This Unity code is running at 5fps. Help me optimize:

[code]

Target: 60fps
Constraints: Must maintain current behavior"

/// Code quality improvement
"Review this Godot script for code smells and best practices:

[gdscript]

Suggest refactoring while maintaining functionality"

// Security audit
"Review this multiplayer game code for security vulnerabilities:

[csharp]

Focus on: cheating prevention, validation, server authority"
```

---

## Testing Automatizado

### Unity Test Generation

```csharp
// AI-generated Unity test
using NUnit.Framework;
using UnityEngine;
using UnityEngine.TestTools;

public class PlayerControllerTests
{
    GameObject playerPrefab;
    GameObject playerInstance;
    PlayerController controller;
    
    [SetUp]
    public void Setup()
    {
        playerPrefab = Resources.Load<GameObject>("PlayerPrefab");
        playerInstance = Object.Instantiate(playerPrefab);
        controller = playerInstance.GetComponent<PlayerController>();
    }
    
    [TearDown]
    public void Teardown()
    {
        Object.Destroy(playerInstance);
    }
    
    [Test]
    public void PlayerCanMoveRight()
    {
        controller.Move(1f);
        Assert.AreEqual(controller.transform.position.x > 0, true);
    }
    
    [UnityTest]
    public IEnumerator PlayerJumpsWhenGrounded()
    {
        var initialY = controller.transform.position.y;
        controller.Jump();
        yield return new WaitForSeconds(0.1f);
        Assert.Greater(controller.transform.position.y, initialY);
    }
}
```

### Godot Unit Tests

```gdscript
# test_player.gd
extends GutTest

var Player = load("res://scripts/Player.gd")
var player

func before_each():
    player = Player.new()

func after_each():
    player.free()

func test_player_initial_state():
    assert_eq(player.health, 100)
    assert_eq(player.speed, 300)
    assert_false(player.is_dead)

func test_player_takes_damage():
    player.take_damage(25)
    assert_eq(player.health, 75)

func test_player_dies_at_zero_health():
    player.take_damage(100)
    assert_true(player.is_dead)
    assert_eq(player.health, 0)

func test_player_cannot_heal_above_max():
    player.heal(50)
    assert_eq(player.health, 100)
```

---

## Recursos Adicionales

### Documentación
- [Unity MLAPI Documentation](https://docs.unity3d.com/Packages/com.unity.netcode@latest)
- [Godot AI Plugins](https://ziva.sh)
- [Unreal Gameplay Framework](https://docs.unrealengine.com)

### Comunidad
- [r/gamedev](https://reddit.com/r/gamedev)
- [GameDev.ai Discord](https://discord.gg/gamedevai)
- [Unity AI Discord](https://discord.gg/unity)

---

_Volver a [README principal](../README.md)_
