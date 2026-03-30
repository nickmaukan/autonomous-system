# 🎯 Unreal Engine + AI: Guía Completa

_Integración de herramientas de inteligencia artificial con Unreal Engine 5 (UE5)_

---

## 📋 Índice

1. [Opciones de IA para Unreal](#opciones-de-ia-para-unreal)
2. [GitHub Copilot con Unreal](#github-copilot-con-unreal)
3. [Blueprint + Claude Code](#blueprint--claude-code)
4. [Python Scripting con IA](#python-scripting-con-ia)
5. [AI Characters y Behavior Trees](#ai-characters-y-behavior-trees)
6. [Prompts para Unreal](#prompts-para-unreal)
7. [Plugins de IA](#plugins-de-ia)

---

## Opciones de IA para Unreal

### Comparativa

| Herramienta | Type | Costo | C++ | Blueprint | Ventajas |
|------------|------|-------|-----|-----------|----------|
| **GitHub Copilot** | IDE Extension | $10-19/mes | ✅ | ⚠️ Basic | Autocompletado, suggestions |
| **Claude Code** | CLI Agent | Variable | ✅ | ❌ | Código complejo, review |
| **ChatGPT** | API | $20/mes | ✅ | ❌ | Prototipado rápido |
| **Cursor** | IDE | $20/mes | ✅ | ❌ | IDE completo con IA |
| **Unreal AI Assist** | Experimental | ? | ⚠️ | ✅ | Nativo UE5 |

### Configuración Recomendada

```
┌─────────────────────────────────────────────┐
│         STACK RECOMENDADO PARA UNREAL        │
├─────────────────────────────────────────────┤
│                                              │
│  IDE Principal: Visual Studio + Copilot     │
│  ┌──────────────────────────────────────┐   │
│  │ • GitHub Copilot extension            │   │
│  │ • GitHub Copilot Chat                 │   │
│  │ • IntelliCode for completions         │   │
│  └──────────────────────────────────────┘   │
│                                              │
│  AI Agent: Claude Code (terminal)           │
│  ┌──────────────────────────────────────┐   │
│  │ • Complex C++ generation              │   │
│  │ • Architecture planning               │   │
│  │ • Code review y refactor              │   │
│  │ • Multi-file changes                  │   │
│  └──────────────────────────────────────┘   │
│                                              │
│  Python Scripts + IA                         │
│  ┌──────────────────────────────────────┐   │
│  │ • Asset automation                    │   │
│  │ • Batch operations                   │   │
│  │ • Pipeline scripts                   │   │
│  └──────────────────────────────────────┘   │
│                                              │
└─────────────────────────────────────────────┘
```

---

## GitHub Copilot con Unreal

### Setup

```
1. Instalar Visual Studio 2022+ con:
   ✓ Desktop development with C++
   ✓ Game development with C++
   ✓ .NET desktop development

2. Instalar GitHub Copilot extension
   ✓ GitHub Copilot in Visual Studio

3. Configurar .editorconfig para Unreal
   ✓ Unreal header tool compliance
   ✓ Standard C++ conformance

4. Configurar Copilot para C++
   Settings → Extensions → Copilot → 
   ✓ Enable C++ suggestions
   ✓ Enable inline suggestions
```

### Prompts para Copilot en Visual Studio

```cpp
// Cuando escribes:
void AMyCharacter::MoveForward(float Value)

// Copilot sugiere:
void AMyCharacter::MoveForward(float Value)
{
    if (Controller != nullptr && Value != 0.f)
    {
        const FRotator Rotation = Controller->GetControlRotation();
        const FRotator YawRotation(0, Rotation.Yaw, 0);
        const FVector Direction = FRotationMatrix(YawRotation).GetUnitAxis(EAxis::X);
        AddMovementInput(Direction, Value);
    }
}
```

### Sugerencias de Código Útiles

```cpp
// GameplayAbility con Copilot
// Escribes:
UCLASS()
// Después de class, Copilot sugiere:
UCLASS()
class UMyGameplayAbility : public UGameplayAbility
{
    GENERATED_BODY()
public:
    UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "Ability")
    float CooldownDuration = 5.0f;
    
    virtual void ActivateAbility(
        const FGameplayAbilitySpecHandle Handle,
        const FGameplayAbilityActorInfo* ActorInfo,
        const FGameplayAbilitySpec* From,
        const FGameplayEventData* TriggerEventData
    ) override;
};

// Escribes:
void UMyGameplayAbility::ActivateAbility
// Copilot sugiere el body completo
```

---

## Blueprint + Claude Code

### Workflow Híbrido

```
┌─────────────────────────────────────────────────────────────────┐
│               BLUEPRINT + AI WORKFLOW                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  CLAUDE CODE                           BLUEPRINT                 │
│  ──────────────                        ─────────                 │
│                                                                  │
│  • C++ classes (.h/.cpp)                • Visual logic           │
│  • Gameplay frameworks                  • UI widgets            │
│  • Core systems                         • Level blueprints      │
│  • Networking code                      • Animation blueprints  │
│  • Plugin development                   • Particle effects      │
│                                                                  │
│         ↓                               ↓                        │
│         └────────────── OR ───────────────┘                      │
│                          ↓                                       │
│              Blueprint Function Library                          │
│              (C++ con funciones callable desde Blueprint)        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Crear Clase C++ con Claude

```bash
# 1. Crear clase con UE Editor o Rider
# 2. Pedir a Claude Code que genere el header

# En terminal, dentro del proyecto:
claude-code

# Prompt:
"Write a complete header file for a UE5 health component:
- UPROPERTY for max health, current health (Replicated)
- UFUNCTION for TakeDamage, Heal
- Event dispatcher for OnDeath, OnHealthChanged
- Getter para current health percentage
- BlueprintCallable for all public methods"
```

### Code Snippet Generado

```cpp
// HealthComponent.h
#pragma once

#include "CoreMinimal.h"
#include "Components/ActorComponent.h"
#include "GameplayTagContainer.h"
#include "HealthComponent.generated.h"

DECLARE_DYNAMIC_MULTICAST_DELEGATE_TwoParams(
    FOnHealthChanged, 
    float, CurrentHealth, 
    float, MaxHealth
);

DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam(
    FOnDeath, 
    AController*, Instigator
);

UCLASS( ClassGroup=(Custom), meta=(BlueprintSpawnableComponent) )
class MYGAME_API UHealthComponent : public UActorComponent
{
    GENERATED_BODY()

public:    
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category="Health")
    float MaxHealth = 100.0f;
    
    UPROPERTY(ReplicatedUsing=OnRep_CurrentHealth, BlueprintReadOnly, Category="Health")
    float CurrentHealth = 100.0f;
    
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category="Health")
    bool bIsDead = false;
    
    UPROPERTY(BlueprintAssignable, Category="Health")
    FOnHealthChanged OnHealthChanged;
    
    UPROPERTY(BlueprintAssignable, Category="Health")
    FOnDeath OnDeath;
    
    UHealthComponent();
    
    UFUNCTION(BlueprintCallable, Category="Health")
    virtual void Initialize(float InitialHealth);
    
    UFUNCTION(BlueprintCallable, Category="Health")
    virtual void TakeDamage(AActor* DamageCauser, float Damage, AController* InstigatorController = nullptr);
    
    UFUNCTION(BlueprintCallable, Category="Health")
    virtual void Heal(float HealAmount);
    
    UFUNCTION(BlueprintPure, Category="Health")
    float GetHealthPercent() const { return CurrentHealth / MaxHealth; }
    
    UFUNCTION(BlueprintPure, Category="Health")
    bool IsAlive() const { return !bIsDead; }

protected:
    virtual void GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const override;
    
    UFUNCTION()
    virtual void OnRep_CurrentHealth(float OldHealth);
    
    virtual void Die(AController* Instigator);

private:
    UPROPERTY()
    TArray<FGameplayTag> DamageTags;
};
```

---

## Python Scripting con IA

### Setup Python en Unreal

```
1. Instalar Python 3.9+ (desde python.org)
2. En Unreal: Edit → Editor Preferences → Python
3. Verificar: lp:// (Unreal's Python) está disponible

Comandos útiles en Output Log:
> py exec my_script.py
> py -list
> py -help
```

### Script de Ejemplo (contexto para IA)

```python
# prompt_context.py
# Este archivo muestra a la IA el contexto de Unreal Python API

import unreal

# Obtener asset registry
asset_registry = unreal.AssetRegistryHelpers.get_asset_registry()

# Buscar assets
assets = asset_registry.get_assets_by_class("Blueprint", recursive=True)

# Filtrar por path
blueprints = [a for a in assets if "/Game/Blueprints/" in a.package_path]

# Cargar asset
bp = unreal.EditorAssetLibrary.load_asset("/Game/Blueprints/PlayerCharacter")

# Obtener class default
default = bp.get_class_default_object()

# Modificar propiedad
unreal.EditorAssetLibrary.set_editor_property(default, "MaxHealth", 200.0)

# Guardar
unreal.EditorAssetLibrary.save_loaded_asset(bp)

# Crear nuevo blueprint
factory = unreal.BlueprintFactory()
factory.set_editor_property("ParentClass", unreal.Character)
new_bp = unreal AssetToolsHelpers.get_asset_tools().create_asset(
    "NewCharacter", 
    "/Game/Blueprints", 
    unreal.Blueprint,
    factory
)
```

### Automation Script con IA

```python
# generate_enemies.py
# Generar variants de enemigos desde template
import unreal
import random

class EnemyGenerator:
    def __init__(self, template_path: str):
        self.template = unreal.EditorAssetLibrary.load_asset(template_path)
        self.asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    
    def generate_variant(self, name: str, stats: dict) -> object:
        # Duplicar template
        variant = self.asset_tools.duplicate_asset(
            name,
            "/Game/Blueprints/Enemies",
            self.template
        )
        
        # Obtener CDO
        cdo = variant.get_class_default_object()
        
        # Aplicar stats
        if "health" in stats:
            cdo.MaxHealth = stats["health"]
        if "damage" in stats:
            cdo.AttackDamage = stats["damage"]
        if "speed" in stats:
            cdo.MoveSpeed = stats["speed"]
        
        # Guardar
        unreal.EditorAssetLibrary.save_loaded_asset(variant)
        
        return variant
    
    def generate_wave(self, count: int, base_stats: dict) -> list:
        enemies = []
        for i in range(count):
            stats = {
                "health": base_stats["health"] * random.uniform(0.8, 1.5),
                "damage": base_stats["damage"] * random.uniform(0.7, 1.3),
                "speed": base_stats["speed"] * random.uniform(0.9, 1.1),
            }
            enemy = self.generate_variant(f"Enemy_Wave_{i+1}", stats)
            enemies.append(enemy)
        return enemies

# Uso:
generator = EnemyGenerator("/Game/Blueprints/Enemies/BaseEnemy")
wave = generator.generate_wave(10, {"health": 100, "damage": 20, "speed": 300})
print(f"Generated {len(wave)} enemies")
```

---

## AI Characters y Behavior Trees

### Sistema de IA en Unreal (GAS)

```cpp
// MyAIController.h
#pragma once

#include "CoreMinimal.h"
#include "AIController.h"
#include "MyAIController.generated.h"

UCLASS()
class MYGAME_API AMyAIController : public AAIController
{
    GENERATED_BODY()

public:
    AMyAIController();
    
    virtual void BeginPlay() override;
    virtual void OnPossess(APawn* InPawn) override;
    
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "AI")
    UBehaviorTreeComponent* BehaviorTreeComponent;
    
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "AI")
    UBlackboardComponent* BlackboardComponent;
    
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "AI")
    UBehaviorTree* BehaviorTree;
    
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "AI")
    float SightRadius = 1000.0f;
    
    UFUNCTION(BlueprintCallable, Category = "AI")
    void SetTarget(AActor* Target);
    
    UFUNCTION(BlueprintPure, Category = "AI")
    AActor* GetTarget() const;
    
protected:
    UPROPERTY()
    UAIPerceptionComponent* PerceptionComponent;

private:
    void SetupPerceptionSystem();
};
```

### Behavior Tree con Prompts

```
Prompt para Claude Code:

"Create a complete Behavior Tree for a UE5 enemy with these specs:
- Root: Selector
  - Sequence: Has Target?
    - MoveTo target (NavMesh)
    - Distance check (>500: Chase, <=500: Attack)
  - Sequence: No Target
    - Wait (3 seconds)
    - RandomPatrol (waypoints)
- Blackboard Keys:
  - TargetActor (Object)
  - TargetLocation (Vector)
  - LastKnownTargetLocation (Vector)
- Services:
  - UpdateTarget (perception via AIPerception)
  - LoseTarget (if target not seen for 5 seconds)
- Tasks:
  - MoveToTarget
  - AttackTarget
  - PatrolRandom
  - Wait"
```

---

## Prompts para Unreal

### C++ Gameplay Systems

```cpp
// Prompt para Claude: "Write a complete UE5 damage system"
/*
Requirements:
- Damage calculation with armor reduction
- Damage types (Physical, Fire, Ice, Lightning)
- Critical hit chance and multiplier
- Damage mitigation from buffs/debuffs
- Overkill damage handling
- Floating damage numbers (spawn widget)
- Damage number color by type
- Death when health reaches 0
- Drop loot on death
*/

#pragma once

#include "CoreMinimal.h"
#include "GameplayTagContainer.h"
#include "Components/ActorComponent.h"
#include "DamageSystemComponent.generated.h"

// Damage types as gameplay tags
// Fire.Damage, Ice.Damage, Lightning.Damage, Physical.Damage

USTRUCT(BlueprintType)
struct FDamageEvent
{
    GENERATED_BODY()
    
    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    float Damage = 0.0f;
    
    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    FGameplayTagContainer DamageTags;
    
    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    float CriticalMultiplier = 1.0f;
    
    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    bool bIsCritical = false;
    
    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    AActor* DamageCauser = nullptr;
    
    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    AController* InstigatorController = nullptr;
};

// ... resto de la implementación
```

### UMG Widgets

```cpp
// Prompt: "Create a health bar UMG widget with:
// - Progress bar with gradient fill
// - Shake animation when taking damage
// - Smooth interpolation when health changes
// - Text showing current/max health
// - Color based on health percentage (green > yellow > red)"
```

```cpp
// HealthBarWidget.h
UCLASS()
class UHealthBarWidget : public UUserWidget
{
    GENERATED_BODY()

public:
    UPROPERTY(meta = (BindWidget))
    UProgressBar* HealthProgressBar;
    
    UPROPERTY(meta = (BindWidget))
    UTextBlock* HealthText;
    
    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Config")
    float InterpSpeed = 5.0f;
    
    UFUNCTION(BlueprintCallable)
    void SetHealthPercent(float Percent);
    
    UFUNCTION(BlueprintCallable)
    void SetHealthInstant(float Current, float Max);
    
    UFUNCTION(BlueprintCallable)
    void PlayDamageShake();
    
protected:
    virtual void NativeTick(const FGeometry& MyGeometry, float InDeltaTime) override;
    
private:
    float DisplayHealthPercent = 1.0f;
    float TargetHealthPercent = 1.0f;
    float MaxHealth = 100.0f;
    float CurrentHealth = 100.0f;
};
```

---

## Plugins de IA

### Plugins Recomendados

| Plugin | Descripción | Precio |
|--------|-------------|--------|
| **A相对 AI Assistant** | AI asistente dentro del editor | Freemium |
| **Blueprint Assist** | Mejoras para Blueprinting (no IA, pero útil) | Gratis |
| **Copilot for Unreal** | Extensión VS con Copilot | $10/mes |
| **Rapid AI** | Generador de código experimental | ? |

### Integration con Servicios Externos

```cpp
// OpenAI Integration para NPCs
// Config.json
{
  "OpenAI": {
    "ApiKey": "${OPENAI_API_KEY}",
    "Model": "gpt-4",
    "MaxTokens": 256
  }
}

// OpenAIComponent.h
UCLASS( ClassGroup=(AI), meta=(BlueprintSpawnableComponent) )
class MYGAME_API UOpenAIComponent : public UActorComponent
{
    GENERATED_BODY()

public:
    UFUNCTION(BlueprintCallable)
    void SendMessage(const FString& Message, FOnAILResponse Received);
    
    UFUNCTION(BlueprintCallable)
    void SetSystemPrompt(const FString& Prompt);
    
    UFUNCTION(BlueprintCallable)
    void ClearConversation();

protected:
    UPROPERTY()
    TArray<FChatMessage> ConversationHistory;
    
    UPROPERTY()
    FString SystemPrompt;
    
    virtual void BeginPlay() override;

private:
    FString ApiKey;
    FString Model;
    
    void SendRequest(const FString& Message);
    void ParseResponse(const FString& Response);
};
```

---

## Prompts Específicos para Unreal

### "Create a Multiplayer Game"

```text
"Set up a UE5 multiplayer game with:
- Lobby system (max 4 players)
- Character selection screen
- Server travel to gameplay map
- Player state replication
- HP and position sync
- Simple chat system
- Ready check before start
- Graceful disconnect handling
- Reconnection support

Use GameInstance, GameMode, PlayerController, and PlayerState classes.
Include AIGameInstance, AIGameMode, AIPlayerController, AIPlayerState."
```

### "Create a Boss Battle System"

```text
"Build a boss battle system with:
- Boss actor with multiple phases (3 phases)
- Phase transitions at 66% and 33% HP
- Unique attacks per phase
- Attack patterns (melee combo, ranged attack, area attack)
- Teleportation between positions
- Enrage timer (5 minutes, 2x damage)
- Boss health bar UI (huge, center screen)
- Phase announcements
- Boss defeat animation and reward

Use Animation Montage for attacks, Behavior Tree for AI.
Include IAnimNotify interfaces for attack notifications."
```

---

## Mejores Prácticas

### ✅ Hacer

1. **Usa C++ para sistemas críticos** - Performance > convenience
2. **Blueprint Function Libraries** - Reutiliza código C++ en Blueprint
3. **Gameplay Ability System (GAS)** - Sistema oficial de habilidades
4. **Editor Utility Blueprints** - Automatización del editor
5. **AI Agents para código repetitivo** - Genera boilerplate con IA

### ❌ No Hacer

1. **No pongas lógica compleja en Blueprint** - Usa C++
2. **No ignores el profiling** - Unreal tiene herramientas excelentes
3. **No generes todo con IA** - Revisa y entiende el código
4. **No uses Tick para todo** - Timer managers son más eficientes

---

## Recursos

- [Unreal Engine AI Documentation](https://docs.unrealengine.com)
- [Gameplay Ability System](https://docs.unrealengine.com/abilitysystem)
- [Behavior Tree Documentation](https://docs.unrealengine.com/behaviortrees)
- [Unreal Python API](https://docs.unrealengine.com/pythonapi)
- [GitHub Copilot for Visual Studio](https://docs.github.com/copilot)

---

_Volver a [README principal](../../README.md)_
