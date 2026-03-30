# 👻 Godot + AI: Guía Completa

_Integración de herramientas de inteligencia artificial con Godot Game Engine 4.x_

---

## 📋 Índice

1. [Herramientas Disponibles](#herramientas-disponibles)
2. [Ziva - Setup y Uso](#ziva---setup-y-uso)
3. [AI Assistant Hub](#ai-assistant-hub)
4. [Prompts para Godot](#prompts-para-godot)
5. [GDScript Templates](#gdscript-templates)
6. [Godot LLM Framework](#godot-llm-framework)
7. [Promethean AI con Godot](#promethean-ai-con-godot)

---

## Herramientas Disponibles

### Comparativa

| Herramienta | Tipo | Costo | Godot-Specific | Escena Gen | Debug |
|-------------|------|-------|----------------|------------|-------|
| **Ziva** | Plugin + SaaS | Freemium | ✅ Native | ✅ | ✅ |
| **AI Assistant Hub** | Plugin | Gratis | ⚠️ Partial | ❌ | ❌ |
| **Godot Copilot** | Plugin | Gratis* | ⚠️ Partial | ❌ | ❌ |
| **JetBrains Rider** | IDE | $169/yr | ⚠️ C# only | ❌ | ✅ |
| **Workik** | Web | Freemium | ⚠️ Generic | ❌ | ❌ |
| **Claude/ChatGPT** | LLM | Variable | ❌ Manual | ❌ | ⚠️ |

### Recomendaciones por Caso

| Caso | Herramienta | Why |
|------|-------------|-----|
| **General GDScript** | Ziva | Mejor integración, scene gen |
| **Budget constrained** | AI Assistant Hub + Ollama | Gratis, local |
| **C# en Godot** | JetBrains Rider | IDE profesional |
| **Quick snippets** | Workik / ChatGPT | Web, sin install |
| **Local + Privacy** | Ollama + AI Assistant Hub | Todo local |

---

## Ziva - Setup y Uso

### ¿Qué es Ziva?

Ziva es el plugin de IA más completo para Godot:
- ✅ Plugin nativo que se integra en el editor
- ✅ Generación de GDScript desde lenguaje natural
- ✅ Creación de scenes completas
- ✅ Entendimiento profundo del proyecto
- ✅ Debugger integration
- ✅ UI Agent especializado para Control nodes

### Instalación

```bash
# Opción 1: Descargar desde web
# 1. Ir a https://ziva.sh/download
# 2. Descargar el plugin
# 3. Importar en Godot (Plugins → Add)

# Opción 2: Script de instalación
curl -sSL https://ziva.sh/install.sh | bash
```

### Primeros Pasos

```
1. Abrir Godot 4.2+
2. Ir a Project → Project Settings → Plugins
3. Activar "Ziva" plugin
4. Aparecerá panel en el editor (típicamente abajo)
5. Crear cuenta o usar 20 créditos gratis

Primer uso:
- Escribir en el chat: "Create a player character with WASD movement"
- Ziva genera el script y lo adjunta al nodo
- O pregunta si quieres crear un nuevo nodo
```

### Prompts de Ejemplo para Ziva

```text
// Character Controller
"Create a 3D player character with first-person controls, mouse look,
jump with double jump, and sprint with stamina"

// UI System
"Build a complete pause menu with resume, options, and quit buttons.
Include a settings panel for volume sliders and a controls rebinding system"

// Enemy AI
"Create an enemy that uses A* pathfinding, has patrol waypoints,
detects the player with an Area node, and attacks when in range.
Include health system and death animation"

// Inventory
"Make an inventory system with a grid of slots, drag and drop items,
a tooltip showing item description, and equip slots for weapon/armor"
```

---

## AI Assistant Hub

### Instalación

```
1. Abrir Godot Asset Library (AssetLib)
2. Buscar "AI Assistant Hub"
3. Descargar e importar
4. Configurar con Ollama o Google Gemini

Configuración con Ollama:
- Instalar Ollama: curl -fsSL https://ollama.com/install.sh | sh
- Descargar modelo: ollama pull llama3.2
- En Godot: AI Assistant Hub → Settings → Ollama URL: http://localhost:11434
- Seleccionar modelo: llama3.2
```

### Características

| Feature | AI Assistant Hub |
|---------|-------------------|
| GDScript generation | ✅ |
| Multiple backends | ✅ (Ollama, Gemini) |
| Local AI option | ✅ |
| Scene generation | ❌ |
| Project context | ⚠️ Basic |
| Price | Gratis |

---

## Prompts para Godot

### Movement y Physics

```gdscript
# Prompt: "Create a 2D platformer character with variable jump height,
# coyote time, jump buffering, and wall sliding"

extends CharacterBody2D

@export var speed: float = 300.0
@export var jump_velocity: float = -450.0
@export var gravity: float = 980.0
@export var wall_slide_speed: float = 100.0
@export var coyote_time: float = 0.1
@export var jump_buffer: float = 0.1

var _coyote_timer: float = 0.0
var _jump_buffer_timer: float = 0.0
var _wall_direction: int = 0

func _ready() -> void:
    # Inicialización
    pass

func _physics_process(delta: float) -> void:
    # Aplicar gravedad
    if not is_on_floor():
        velocity.y += gravity * delta
    else:
        _coyote_timer = coyote_time
    
    # Detectar wall
    _wall_direction = get_wall_direction()
    
    # Movimiento horizontal
    var input_direction := Input.get_axis("ui_left", "ui_right")
    velocity.x = input_direction * speed
    
    # Jump buffering
    if Input.is_action_just_pressed("ui_accept"):
        _jump_buffer_timer = jump_buffer
    
    # Coyote time + jump
    if _coyote_timer > 0 and _jump_buffer_timer > 0:
        velocity.y = jump_velocity
        _coyote_timer = 0.0
        _jump_buffer_timer = 0.0
    
    # Wall slide
    if is_on_wall() and _wall_direction != 0:
        velocity.y = min(velocity.y, wall_slide_speed)
    
    # Update timers
    _coyote_timer -= delta
    _jump_buffer_timer -= delta
    
    move_and_slide()

func get_wall_direction() -> int:
    for raycast in $WallRaycasts.get_children():
        if raycast.is_colliding():
            return int(raycast.target_position.x > 0) * 2 - 1
    return 0
```

### Sistema de Estados

```gdscript
# Prompt: "Create a state machine for a platformer with states:
# idle, run, jump, fall, wall_slide, attack"

extends Node
class_name StateMachine

signal state_changed(from: String, to: String)

@export var initial_state: State

var current_state: State
var states: Dictionary = {}

func _ready() -> void:
    for child in get_children():
        if child is State:
            states[child.name.to_lower()] = child
            child.state_machine = self
    
    if initial_state:
        current_state = initial_state
        current_state.enter()

func _physics_process(delta: float) -> void:
    if current_state:
        current_state.physics_update(delta)

func transition_to(state_name: String) -> void:
    var new_state = states.get(state_name.to_lower())
    if new_state == null or new_state == current_state:
        return
    
    var old_state = current_state
    current_state.exit()
    current_state = new_state
    current_state.enter()
    state_changed.emit(old_state.name.to_lower(), new_state.name.to_lower())
```

### Sistema de Inventario

```gdscript
# Prompt: "Create an inventory system with grid layout,
# item stacking up to 64, drag and drop, and save/load to JSON"

extends Control

signal item_added(item: Item)
signal item_removed(item: Item)

const SLOT_COUNT: int = 24
const SLOT_SIZE: int = 64
const COLUMNS: int = 6

@onready var grid_container: GridContainer = $GridContainer
@onready var item_scene: PackedScene = preload("res://scenes/item_slot.tscn")

var inventory: Array = []
var slots: Array = []

func _ready() -> void:
    _create_slots()
    inventory.resize(SLOT_COUNT)

func _create_slots() -> void:
    for i in SLOT_COUNT:
        var slot = item_scene.instantiate()
        slot.slot_index = i
        slot.item = null
        grid_container.add_child(slot)
        slots.append(slot)

func add_item(item: Item) -> bool:
    # Try to stack first
    for i in inventory.size():
        if inventory[i] != null and inventory[i].name == item.name:
            if inventory[i].quantity < 64:
                inventory[i].quantity += item.quantity
                slots[i].update_display()
                item_added.emit(item)
                return true
    
    # Find empty slot
    for i in inventory.size():
        if inventory[i] == null:
            inventory[i] = item
            slots[i].item = item
            slots[i].update_display()
            item_added.emit(item)
            return true
    
    return false  # Inventory full

func remove_item(slot_index: int, quantity: int = 1) -> Item:
    if inventory[slot_index] == null:
        return null
    
    var item = inventory[slot_index]
    item.quantity -= quantity
    
    if item.quantity <= 0:
        inventory[slot_index] = null
        slots[slot_index].item = null
        slots[slot_index].update_display()
        item_removed.emit(item)
        return null
    
    slots[slot_index].update_display()
    return item

func save() -> Dictionary:
    var save_data = []
    for item in inventory:
        if item != null:
            save_data.append({
                "name": item.name,
                "quantity": item.quantity,
                "metadata": item.metadata
            })
    return {"inventory": save_data}

func load(save_data: Dictionary) -> void:
    inventory.clear()
    inventory.resize(SLOT_COUNT)
    for slot in slots:
        slot.item = null
        slot.update_display()
    
    for i in save_data.get("inventory", []):
        var item = Item.new()
        item.name = i.name
        item.quantity = i.quantity
        item.metadata = i.metadata
        inventory[i] = item
        slots[i].item = item
        slots[i].update_display()
```

### Diálogo con NPC

```gdscript
# Prompt: "Create an NPC dialogue system with typewriter effect,
# branching choices stored in a JSON file, and portrait display"

extends Area2D

signal dialogue_ended

@export var dialogue_file: String = "res://dialogues/npc_001.json"
@export var portrait: Texture2D

var dialogue_data: Dictionary = {}
var current_node: String = "start"

@onready var dialog_label: Label = $DialogPanel/DialogLabel
@onready var portrait_sprite: Sprite2D = $DialogPanel/Portrait
@onready var choices_container: VBoxContainer = $DialogPanel/Choices

var _is_dialogue_active: bool = false
var _typewriter_speed: float = 0.03

func _ready() -> void:
    _load_dialogue()
    body_entered.connect(_on_player_enter)
    dialog_label.visible_ratio = 0.0

func _load_dialogue() -> void:
    var file = FileAccess.open(dialogue_file, FileAccess.READ)
    if file:
        dialogue_data = JSON.parse_string(file.get_as_text())

func start_dialogue() -> void:
    _is_dialogue_active = true
    current_node = "start"
    _show_node(current_node)

func _show_node(node_id: String) -> void:
    var node = dialogue_data.get("nodes", {}).get(node_id, {})
    if node.is_empty():
        end_dialogue()
        return
    
    # Set portrait
    if portrait:
        portrait_sprite.texture = portrait
    
    # Show text with typewriter
    var full_text = node.get("text", "")
    dialog_label.text = full_text
    dialog_label.visible_ratio = 0.0
    
    # Create tween for typewriter
    var tween = create_tween()
    tween.tween_property(dialog_label, "visible_ratio", 1.0, 
                         full_text.length() * _typewriter_speed)
    
    # Show choices after text
    choices_container.clear()
    var choices = node.get("choices", [])
    for i in choices.size():
        var choice_button = Button.new()
        choice_button.text = choices[i].text
        choice_button.pressed.connect(_on_choice_selected.bind(choices[i].next))
        choices_container.add_child(choice_button)

func _on_choice_selected(next_node: String) -> void:
    current_node = next_node
    _show_node(current_node)

func end_dialogue() -> void:
    _is_dialogue_active = false
    dialogue_ended.emit()
    queue_redraw()
```

---

## GDScript Templates

### Game Manager Singleton

```gdscript
# autoload/game_manager.gd
extends Node

signal score_changed(new_score: int)
signal health_changed(new_health: int)
signal game_paused(is_paused: bool)
signal game_over

var score: int = 0:
    set(v):
        score = v
        score_changed.emit(score)

var health: int = 100:
    set(v):
        health = clamp(v, 0, max_health)
        health_changed.emit(health)
        if health <= 0:
            _on_death()

var max_health: int = 100
var is_paused: bool = false:
    set(v):
        is_paused = v
        get_tree().paused = is_paused
        game_paused.emit(is_paused)

var current_level: String = ""

func _input(event: InputEvent) -> void:
    if event.is_action_pressed("pause"):
        is_paused = !is_paused

func _on_death() -> void:
    game_over.emit()

func load_level(level_path: String) -> void:
    current_level = level_path
    get_tree().change_scene_to_file(level_path)
```

### Object Pool

```gdscript
# system/object_pool.gd
extends Node

@export var pooled_scene: PackedScene
@export var initial_pool_size: int = 10
@export var max_pool_size: int = 50

var _pool: Array = []
var _active_objects: Array = []

func _ready() -> void:
    _expand_pool(initial_pool_size)

func _expand_pool(count: int) -> void:
    for i in count:
        if _pool.size() + _active_objects.size() >= max_pool_size:
            break
        var obj = pooled_scene.instantiate()
        obj.tree_exited.connect(_on_object_returned.bind(obj))
        _pool.append(obj)
        add_child(obj)
        obj.set_process(false)
        obj.visible = false

func get() -> Node:
    var obj: Node
    
    if _pool.size() > 0:
        obj = _pool.pop_back()
    elif _active_objects.size() < max_pool_size:
        obj = pooled_scene.instantiate()
        obj.tree_exited.connect(_on_object_returned.bind(obj))
        add_child(obj)
    else:
        return null
    
    _active_objects.append(obj)
    obj.set_process(true)
    obj.visible = true
    obj.emit_signal("pooled_object_ready")  # Custom signal to reset object
    return obj

func return_to_pool(obj: Node) -> void:
    if not obj in _active_objects:
        return
    
    _active_objects.erase(obj)
    _pool.append(obj)
    obj.set_process(false)
    obj.visible = false

func _on_object_returned(obj: Node) -> void:
    _active_objects.erase(obj)
    _pool.erase(obj)
    # Re-add to pool if needed
    if _pool.size() < initial_pool_size:
        _pool.append(obj)
        add_child(obj)
```

---

## Godot LLM Framework

### GdLlama - LLM Local en Godot

```gdscript
# Implementación conceptual de integración LLM local
# Requiere servidor Ollama o similar corriendo localmente

extends Node

var _base_url: String = "http://localhost:11434/api/generate"
var _model: String = "llama3.2"

var _system_prompt: String = """You are a helpful game AI assistant.
You help players with questions about the game world.
Keep responses short and in character."""

func ask(prompt: String, context: Dictionary = {}) -> String:
    var full_prompt = _system_prompt + "\n\nContext: " + str(context) + "\n\nUser: " + prompt
    
    var body = JSON.new()
    body.data = {
        "model": _model,
        "prompt": full_prompt,
        "stream": false,
        "options": {
            "temperature": 0.7,
            "num_predict": 256
        }
    }
    
    var headers = ["Content-Type: application/json"]
    var result = await HTTPRequest.new().request(
        _base_url, headers, HTTPClient.METHOD_POST, body.get_parsed_string()
    )
    
    if result[0] == OK:
        var response = JSON.parse_string(result[3].get_string_from_utf8())
        return response.get("response", "...")
    return "..."

# Usar con NPC
func _on_npc_interact(npc_id: String, player_input: String) -> void:
    var npc_context = _get_npc_context(npc_id)
    var response = await ask(player_input, npc_context)
    _show_dialogue(response)
```

---

## Promethean AI con Godot

### Integración

Promethean AI funciona junto a Godot para world building:

```
1. Instalar Promethean AI (plugin externo)
2. Usar dentro de Blender, Maya, o 3ds Max
3. Exportar assets a Godot
4. Promethean genera environments automaticamente

Workflow:
1. Promethean AI → Genera world/environment
2. Exportar a FBX/glTF
3. Importar en Godot
4. Añadir lógica de juego con Ziva/AI
```

---

## Mejores Prácticas

### ✅ Hacer

1. **Usa types estrictos** - Godot 4 es typed-first
2. **Aprovecha @export** - Expón variables al editor
3. **Usa signals** - Comunicación desacoplada
4. **Revisa código generado** - AI puede cometer errores
5. **Test local primero** - Usa Ollama si tienes privacy concerns

### ❌ No Hacer

1. **No uses GDScript para todo** - C# o C++ para performance crítica
2. **No ignores null checks** - Godot no es null-safe por defecto
3. **No generes sistemas complejos de golpe** - Hazlo incremental
4. **No Olvides los @onready** - Cachea nodos para performance

---

## Recursos

- [Ziva AI](https://ziva.sh)
- [Godot AI Assistant Hub](https://github.com/microssx/AIAssistantHub)
- [Godot Copilot](https://github.com/yythomas/godot-copilot)
- [GdLlama](https://github.com/imakeption/gdllama)
- [Official Godot AI Documentation](https://docs.godotengine.org)

---

_Volver a [README principal](../../README.md)_
