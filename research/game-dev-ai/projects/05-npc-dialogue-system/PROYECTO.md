# 💬 Proyecto 05: Sistema de Diálogos con NPC con IA

## Resumen Ejecutivo

**Objetivo:** Crear un sistema de diálogos procedurales para NPCs usando LLMs, permitiendo conversaciones dinámicas e ilimitadas con personajes no jugadores.

**Herramientas principales:** ChatGPT API / Claude API, Godot/Unity, Convai/Charisma.ai (alternativas)

**Tiempo estimado:** 3-4 semanas

**Dificultad:** Alta (requiere diseño de sistema + API integration)

**Qué resuelve:** NPCs con diálogos limitados/repetitivos → NPCs que conversan naturalmente sobre cualquier tema.

---

## 1. Concepto del sistema

### El problema:

```
NPCs TRADICIONALES:
- Tienen X líneas pre-escritas
- Repiten las mismas 5 respuestas
- No recuerdan conversaciones previas
- No adaptan respuestas al contexto
- "Flavor text" sin significado real

NPCs CON IA:
- Conversaciones ilimitadas
- Contextually appropriate
- Recuerdan información compartida
- Personalidad consistente
- In-World knowledge
```

### Solución arquitectónica:

```
┌─────────────────────────────────────────────────────────────────┐
│                 NPC DIALOGUE SYSTEM ARCHITECTURE                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  PLAYER                                     NPC                   │
│    │                                          │                   │
│    ▼                                          ▼                   │
│  ┌─────────┐                          ┌─────────────┐         │
│  │ Player  │                          │ NPC Profile  │         │
│  │ Input   │                          │ - Persona    │         │
│  └────┬────┘                          │ - Backstory  │         │
│       │                                │ - Knowledge  │         │
│       │                                │ - Goals      │         │
│       │                                └──────┬──────┘         │
│       │                                       │                   │
│       │                                       ▼                   │
│       │                               ┌─────────────┐            │
│       │                               │   LLM API   │            │
│       │                               │  (GPT-4 /   │            │
│       │                               │   Claude)   │            │
│       │                               └──────┬──────┘            │
│       │                                      │                   │
│       ▼                                      ▼                   │
│  ┌─────────┐                          ┌─────────────┐          │
│  │ Display │                          │  Response   │          │
│  │ Text    │                          │  Generator  │          │
│  └─────────┘                          └─────────────┘          │
│                                                                  │
│  ┌──────────────────────────────────────────────────────┐       │
│  │              CONTEXT MANAGER                          │       │
│  │  - Conversation History (últimas N messages)         │       │
│  │  - World State (qué sabe el NPC del mundo)          │       │
│  │  - Player State (qué sabe el NPC del player)        │       │
│  │  - Session Memory (esta conversación específica)     │       │
│  └──────────────────────────────────────────────────────┘       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. Plan de implementación

### Fase 1: Diseño del sistema (Días 1-3)

```
DÍA 1: Arquitectura básica

COMPONENTES:

┌─────────────────────────────────────────────────────────────────┐
│                     SYSTEM DESIGN                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. NPCProfile (Data)                                           │
│     ├── name: String                                            │
│     ├── persona: String (system prompt)                         │
│     ├── backstory: String                                        │
│     ├── knowledge: List<String> (qué sabe)                      │
│     ├── goals: List<String> (qué quiere lograr)                │
│     ├── speaking_style: String (formal, casual, etc.)            │
│     ├── speech_patterns: List<String> (expresiones características)│
│     └── max_memory: int (cuántas msgs recordar)                 │
│                                                                  │
│  2. ConversationManager                                          │
│     ├── active_conversations: Dict<NPCId, List<Message>>       │
│     ├── world_state: WorldState                                  │
│     └── player_state: PlayerState                               │
│                                                                  │
│  3. DialogueInterface (UI)                                       │
│     ├── NPC portrait/sprite                                     │
│     ├── Text display (typewriter effect)                        │
│     ├── Choice buttons (si hay opciones)                         │
│     └── Skip/continue button                                    │
│                                                                  │
│  4. LLMIntegration                                              │
│     ├── provider: LLMProvider (OpenAI/Claude/Local)            │
│     ├── rate_limiting: RateLimiter                              │
│     └── caching: ResponseCache                                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

```
DÍA 2: Definir NPC profiles

NPCs DE EJEMPLO PARA TESTING:

NPC 1: EL MERCHANT
---
name: "Gideon el Mercader"
persona: "You are Gideon, a gruff but fair merchant who has traveled
the realm selling rare goods. You're suspicious of strangers but 
appreciate those who show respect. You speak in short, practical 
sentences and always try to make a good deal."
backstory: "You've been trading for 30 years, seen many adventurers
come and go. You lost your partner to bandits and trust is hard for you."
knowledge: [
  "You know the prices of all common goods",
  "You heard rumors about a dragon in the northern mountains",
  "You don't trust adventurers who brag",
  "You have a rare artifact but won't sell it to just anyone"
]
goals: [
  "Make fair trades",
  "Protect your valuable merchandise",
  "Maybe find a trustworthy adventurer to hire"
]
speaking_style: "Short, direct sentences. Practical. Uses 'hmm' and 
'look here' frequently."
---

NPC 2: EL SCHOLAR
---
name: "Elara la Sabia"
persona: "You are Elara, a scholar who has spent decades studying
ancient texts. You're excited to share knowledge but sometimes get
lost in academic details. You're kind but absent-minded about 
mundane things."
backstory: "You came to this town to study the ruins nearby. You've
made breakthrough discoveries but there are still mysteries you can't solve."
knowledge: [
  "You know the history of the ancient civilization",
  "You can translate old inscriptions",
  "You know about magical artifacts",
  "You're working on a theory about the ruins"
]
goals: [
  "Complete your research",
  "Find someone to help investigate the ruins",
  "Share knowledge with those worthy"
]
speaking_style: "Verbose, uses academic terms, gets excited about
subjects, apologizes when rambling."
---

NPC 3: EL GUARD
---
name: "Soldado Roderick"
persona: "You are Roderick, a guard at the town gate. You're bored
with routine duty but take your job seriously. You appreciate
politeness and proper paperwork."
backstory: "You served in the king's army for 10 years before
getting this post. You miss action but appreciate the stability.
You have a family in town."
knowledge: [
  "You know everyone who passes through the gate",
  "You know the patrol schedules",
  "You heard rumors about trouble in the capital",
  "You know shortcuts in the city"
]
goals: [
  "Maintain order",
  "Do your shift without trouble",
  "Maybe hear some interesting news"
]
speaking_style: "Formal, military bearing, uses titles, occasionally
lets slip soldier slang."
```

```
DÍA 3: Diseño de UI

DIALOGUE BOX DESIGN:

┌─────────────────────────────────────────────────────────────┐
│  ┌─────────┐                                                 │
│  │   NPC   │  NPC NAME                                       │
│  │ PORTRAIT│  ─────────────────────────────────────────────  │
│  └─────────┘                                                 │
│               "Dialogue text appears here with a             │
│               typewriter effect, character by                │
│               character. The player can wait                  │
│               for full text or click to skip."               │
│                                                             │
│                                       [Continue ▼]          │
└─────────────────────────────────────────────────────────────┘

CHOICE SYSTEM (optional):

┌─────────────────────────────────────────────────────────────┐
│  ┌─────────┐                                                 │
│  │   NPC   │  NPC NAME                                       │
│  │ PORTRAIT│  ─────────────────────────────────────────────  │
│  └─────────┘                                                 │
│               "So, adventurer, what brings you              │
│               to my shop today?"                             │
│                                                             │
│  ┌──────────────────────────────────────┐                    │
│  │  I need supplies for a quest.       │                    │
│  └──────────────────────────────────────┘                    │
│  ┌──────────────────────────────────────┐                    │
│  │  Just browsing.                     │                    │
│  └──────────────────────────────────────┘                    │
│  ┌──────────────────────────────────────┐                    │
│  │  Do you know anything about [topic]?│                   │
│  └──────────────────────────────────────┘                    │
└─────────────────────────────────────────────────────────────┘
```

---

### Fase 2: Implementación básica (Días 4-8)

```
DÍA 4-5: Core DialogueManager

GODOT IMPLEMENTATION (GDScript):

class_name DialogueManager
extends Node

signal dialogue_started(npc_id: String)
signal dialogue_ended
signal response_received(text: String)
signal choices_received(choices: Array)

const MAX_MEMORY: int = 20
const API_PROVIDER: String = "openai"  # or "claude"

var _active_npcs: Dictionary = {}
var _conversation_histories: Dictionary = {}
var _player_knowledge: Dictionary = {}

func start_dialogue(npc_id: String, npc_profile: NPCProfile) -> void:
    """Iniciar conversación con un NPC"""
    
    dialogue_started.emit(npc_id)
    
    _active_npcs[npc_id] = npc_profile
    _conversation_histories[npc_id] = []
    
    # Mensaje inicial del NPC (opcional)
    var initial_greeting = _generate_greeting(npc_profile)
    _add_to_history(npc_id, "assistant", initial_greeting)
    response_received.emit(initial_greeting)

func send_message(npc_id: String, player_input: String) -> void:
    """Enviar mensaje del jugador y obtener respuesta"""
    
    _add_to_history(npc_id, "user", player_input)
    _update_player_knowledge(npc_id, player_input)
    
    var response = await _generate_response(npc_id)
    
    _add_to_history(npc_id, "assistant", response)
    response_received.emit(response)

func _generate_greeting(profile: NPCProfile) -> String:
    """Generar saludo inicial basado en perfil"""
    var system_prompt = _build_system_prompt(profile)
    
    var messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "Start a natural conversation. 
         Greet the player in character. Don't be overly long."}
    ]
    
    return await _call_llm(messages)

func _generate_response(npc_id: String) -> String:
    """Generar respuesta al input del jugador"""
    
    var profile = _active_npcs[npc_id]
    var history = _get_recent_history(npc_id)
    var system_prompt = _build_system_prompt(profile)
    
    var messages = [{"role": "system", "content": system_prompt}]
    messages.append_array(history)
    
    return await _call_llm(messages)

func _build_system_prompt(profile: NPCProfile) -> String:
    """Construir system prompt completo"""
    
    var prompt = """
You are {name}.

PERSONALITY: {persona}

BACKSTORY: {backstory}

SPEAKING STYLE: {speaking_style}

IMPORTANT RULES:
1. Stay in character at all times
2. Keep responses moderate length (2-4 sentences typically)
3. If asked about topics you don't know, say so
4. Be helpful but maintain your character
5. Reference your backstory when appropriate
6. Show interest in what the player says
7. Remember information the player shares with you

YOUR KNOWLEDGE:
{knowledge}

YOUR GOALS:
{goals}
""".format({
    "name": profile.name,
    "persona": profile.persona,
    "backstory": profile.backstory,
    "speaking_style": profile.speaking_style,
    "knowledge": "\n".join(profile.knowledge),
    "goals": "\n".join(profile.goals)
})
    
    return prompt
```

```
DÍA 6-7: LLM Integration

PYTHON/GOODSCRIPT API CLIENT:

func _call_llm(messages: Array) -> String:
    """Llamar a LLM API"""
    
    var api_key = OS.get_env("OPENAI_API_KEY")
    var endpoint = "https://api.openai.com/v1/chat/completions"
    
    var body = {
        "model": "gpt-4o",
        "messages": messages,
        "max_tokens": 200,
        "temperature": 0.8
    }
    
    var headers = [
        "Authorization: Bearer " + api_key,
        "Content-Type: application/json"
    ]
    
    var http_request = HTTPRequest.new()
    add_child(http_request)
    
    var result = await http_request.request(
        endpoint, headers, HTTPClient.METHOD_POST, 
        JSON.stringify(body)
    )
    
    http_request.queue_free()
    
    if result[0] == OK:
        var response = JSON.parse_string(result[3].get_string_from_utf8())
        return response["choices"][0]["message"]["content"]
    else:
        return "Hmm, something went wrong. Try again later."

func _get_recent_history(npc_id: String) -> Array:
    """Obtener últimas N mensagens de historial"""
    
    var history = _conversation_histories.get(npc_id, [])
    var recent = history.slice(max(0, history.size() - MAX_MEMORY))
    
    return recent
```

```
DÍA 8: Rate limiting y Caching

class_name RateLimiter
extends Node

var _requests_this_minute: int = 0
var _minute_reset_timer: float = 60.0

const MAX_REQUESTS_PER_MINUTE: int = 20

func _process(delta: float) -> void:
    if _requests_this_minute >= MAX_REQUESTS_PER_MINUTE:
        # Wait or queue request
        pass

func can_make_request() -> bool:
    return _requests_this_minute < MAX_REQUESTS_PER_MINUTE

func record_request() -> void:
    _requests_this_minute += 1


class_name ResponseCache
extends Node

var _cache: Dictionary = {}

func get_cached_response(prompt_hash: String) -> String:
    return _cache.get(prompt_hash)

func cache_response(prompt_hash: String, response: String) -> void:
    _cache[prompt_hash] = response

func _hash_messages(messages: Array) -> String:
    var text = JSON.stringify(messages)
    return text.md5_text()
```

---

### Fase 3: Sistema de memoria (Días 9-12)

```
DÍA 9-10: World State tracking

class_name WorldState
extends Node

var _facts: Dictionary = {}

# Facts about the world that NPCs should know
var world_facts = {
    "current_date": "Year 452 of the Third Age",
    "main_threat": "Dragon sighted in northern mountains",
    "king_status": "The king is ill",
    "town_weather": "Unusually cold lately",
    "recent_events": [
        "A merchant caravan was attacked last week",
        "Strange lights seen near the old ruins",
        "The blacksmith's forge went out unexpectedly"
    ]
}

func get_relevant_facts(npc_profile: NPCProfile) -> String:
    """Get facts relevant to an NPC's knowledge and location"""
    
    var relevant = []
    
    for fact in world_facts.keys():
        if _is_relevant_to_npc(fact, npc_profile):
            relevant.append(fact + ": " + str(world_facts[fact]))
    
    return "\n".join(relevant)

func _is_relevant_to_npc(fact: String, profile: NPCProfile) -> bool:
    """Determine if a world fact is relevant to NPC"""
    # Simplified - could be more sophisticated
    return true


DÍA 11-12: Player State tracking

class_name PlayerState
extends Node

var _player_info: Dictionary = {
    "name": "Unknown",
    "class": "Adventurer",
    "quest": null,
    "reputation": 0,
    "known_info": []  # What the player has shared
}

var _npc_impressions: Dictionary = {}  # NPC -> impression of player

func update_player_info(key: String, value: Variant) -> void:
    _player_info[key] = value

func get_player_info() -> Dictionary:
    return _player_info.duplicate(true)

func add_npc_impression(npc_id: String, impression: String) -> void:
    if not _npc_impressions.has(npc_id):
        _npc_impressions[npc_id] = []
    _npc_impressions[npc_id].append(impression)

func get_npc_impression(npc_id: String) -> String:
    var impressions = _npc_impressions.get(npc_id, [])
    if impressions.is_empty():
        return "neutral"
    return impressions[-1]  # Most recent
```

---

### Fase 4: UI y polish (Días 13-17)

```
DÍA 13-14: Typewriter effect + UI

GODOT UI:

extends Control

@onready var name_label: Label = $Panel/NPCName
@onready var dialogue_label: Label = $Panel/DialogueText
@onready var portrait: TextureRect = $Panel/Portrait
@onready var continue_button: Button = $Panel/ContinueButton
@onready var choices_container: VBoxContainer = $Panel/Choices

signal dialogue_advance
signal choice_selected(choice: String)

var _full_text: String = ""
var _displayed_text: String = ""
var _char_index: int = 0
var _typewriter_speed: float = 0.03
var _is_typing: bool = false

func display_dialogue(npc_name: String, text: String, 
                     portrait_texture: Texture = null) -> void:
    
    name_label.text = npc_name
    _full_text = text
    _displayed_text = ""
    _char_index = 0
    _is_typing = true
    
    if portrait_texture:
        portrait.texture = portrait_texture
    
    continue_button.visible = false
    choices_container.visible = false
    
    _typewrite()

func _typewrite() -> void:
    while _is_typing and _char_index < _full_text.length():
        _displayed_text += _full_text[_char_index]
        dialogue_label.text = _displayed_text
        _char_index += 1
        
        # Small delay between characters
        await get_tree().create_timer(_typewriter_speed).timeout
    
    _is_typing = false
    continue_button.visible = true

func _on_continue_pressed() -> void:
    if _is_typing:
        # Skip to full text
        _is_typing = false
        dialogue_label.text = _full_text
        continue_button.visible = true
    else:
        dialogue_advance.emit()

func show_choices(choices: Array) -> void:
    choices_container.visible = true
    continue_button.visible = false
    
    for choice in choices:
        var button = Button.new()
        button.text = choice
        button.pressed.connect(
            Callable(self, "_on_choice_selected").bind(choice)
        )
        choices_container.add_child(button)

func _on_choice_selected(choice: String) -> void:
    choice_selected.emit(choice)
```

```
DÍA 15-16: Portrait system

# Cada NPC tiene portraits para diferentes emociones
enum Emotion { NEUTRAL, HAPPY, SAD, ANGRY, EXCITED, THINKING }

var _emotion_portraits: Dictionary = {
    "gideon_neutral": load("res://assets/portraits/gideon_neutral.png"),
    "gideon_happy": load("res://assets/portraits/gideon_happy.png"),
    "gideon_angry": load("res://assets/portraits/gideon_angry.png"),
}

func detect_emotion(response_text: String) -> Emotion:
    """Detectar emoción basándose en el texto de respuesta"""
    
    var emotion = Emotion.NEUTRAL
    
    var happy_words = ["happy", "pleased", "glad", "excellent", "good"]
    var sad_words = ["sad", "unfortunately", "sorry", "unfortunate"]
    var angry_words = ["angry", "furious", "outraged", "annoyed"]
    var excited_words = ["amazing", "wonderful", "incredible", "excited"]
    var thinking_words = ["hmm", "interesting", "let me think"]
    
    for word in happy_words:
        if word in response_text.to_lower():
            emotion = Emotion.HAPPY
            break
    
    for word in sad_words:
        if word in response_text.to_lower():
            emotion = Emotion.SAD
            break
    
    # ... similar para otros
    
    return emotion

func update_portrait(emotion: Emotion) -> void:
    var texture = _emotion_portraits.get(
        _current_npc + "_" + emotion.to_lower(),
        _emotion_portraits.get(_current_npc + "_neutral")
    )
    portrait.texture = texture
```

```
DÍA 17: Testing y debugging

TEST SCENARIOS:

1. Conversación simple
   - Input: "Hello"
   - Esperado: NPC greeting

2. Contexto
   - Input 1: "I'm looking for the dragon"
   - Input 2: "Where is it?"
   - Esperado: Recuerda topic anterior

3. Cambio de tema
   - Input 1: "Tell me about the dragon"
   - Input 2: "What about the merchant attack?"
   - Esperado: Transición natural

4. Información inconsistente
   - Input: "What did I tell you earlier?"
   - Esperado: Recuerde información compartida

5. Rate limiting
   - 25 requests rápidos
   - Esperado: Se maneja gracefully
```

---

### Fase 5: Integración con juego (Días 18-21)

```
DÍA 18-19: Quest system integration

QUEST BRIDGE:

class_name QuestDialogueBridge
extends Node

@export var dialogue_manager: DialogueManager
@export var quest_manager: QuestManager

func _ready() -> void:
    dialogue_manager.response_received.connect(_on_response)

func _on_response(text: String) -> void:
    # Detectar keywords de quest
    if "dragon" in text.to_lower():
        _check_dragon_quests()
    
    if "help" in text.to_lower():
        _check_quest_availability()

func _check_dragon_quests() -> void:
    if quest_manager.has_quest("dragon_slayer"):
        return
    
    # Auto-offer o guardar para después
    quest_manager.add_pending_quest_offer("dragon_slayer")

func offer_quest(quest_id: String) -> void:
    var quest = quest_manager.get_quest_data(quest_id)
    
    dialogue_manager.send_message(
        "elara",  # El npc que ofrece
        "I need help with the ruins. Will you assist me?"
    )
```

```
DÍA 20-21: Save/Load integration

SAVE SYSTEM:

func save_npc_states() -> Dictionary:
    var save_data = {
        "conversation_histories": dialogue_manager._conversation_histories,
        "player_knowledge": dialogue_manager._player_knowledge,
        "world_state": world_state.facts,
        "npc_impressions": player_state._npc_impressions
    }
    return save_data

func load_npc_states(save_data: Dictionary) -> void:
    dialogue_manager._conversation_histories = save_data.get(
        "conversation_histories", {})
    dialogue_manager._player_knowledge = save_data.get(
        "player_knowledge", {})
    world_state.facts = save_data.get("world_state", {})
    player_state._npc_impressions = save_data.get(
        "npc_impressions", {})
```

---

## 3. Prompts optimizados

### System prompt base:

```text
SYSTEM PROMPT TEMPLATE:

You are {npc_name}.

{backstory}

PERSONALITY: {personality_description}

SPEAKING STYLE: {speaking_style_examples}

You know the following about the world:
{world_knowledge}

Your current goals (you try to achieve these in conversation):
{goals}

IMPORTANT GUIDELINES:
1. Stay completely in character
2. Keep responses to 2-4 sentences typically
3. If asked about things outside your knowledge, admit it
4. Show personality through word choices and reactions
5. Remember what the player tells you and reference it later
6. Be conversational, not robotic
7. Use your speaking style naturally

Current player information:
{player_info}
```

### Para detección de emociones:

```text
EMOTION DETECTION PROMPT:

Analyze this NPC dialogue and determine the emotion:
"{dialogue_text}"

Options: neutral, happy, sad, angry, excited, thinking, confused, suspicious

Respond with only the emotion name.
```

---

## 4. Optimizaciones de costos

### Estrategia de caching:

```python
# Cache respuestas frecuentes
_conversation_patterns = {
    "greeting": "Cached greeting response",
    "farewell": "Cached farewell response",
    # ...
}

def _check_cache(messages: Array) -> Optional[String]:
    hash_key = _hash_messages(messages)
    
    # Check exact match
    if hash_key in _cache:
        return _cache[hash_key]
    
    # Check similar (para preguntas frecuentes ligeramente diferentes)
    for key, value in _cache.items():
        if _similarity(key, hash_key) > 0.9:
            return value
    
    return None
```

### Model selection:

```python
# Usar modelo más barato para inputs simples
def _select_model(conversation_length: int, 
                complexity: str) -> String:
    
    if complexity == "simple":
        return "gpt-4o-mini"  # Más barato
    
    if conversation_length > 10:
        return "gpt-4o"  # Mejor contexto
    
    return "gpt-4o"  # Default
```

---

## 5. Métricas de éxito

### Quality metrics:

```
DIÁLOGOS NATURALES:
- [ ] NPC no repite respuestas similares
- [ ] Referencia información previa
- [ ] Personalidad consistente
- [ ] Respuestas apropiadas al contexto

PERFORMANCE:
- [ ] <2 segundos por respuesta
- [ ] Sin rate limit triggers
- [ ] Cache hit rate >30%

INTEGRACIÓN:
- [ ] Funciona con save/load
- [ ] Detecta emociones correctamente
- [ ] Choices funcionan
- [ ] No crashea el juego
```

---

## 6. Alternativas sin API

### Local LLMs:

```
OLLAMA + LOCAL SETUP:

1. Instalar Ollama
   - Download desde ollama.com
   - ollama pull llama3.2

2. Setup en Godot:
   - Usar HTTPRequest para llamar Ollama API
   - http://localhost:11434/api/generate

3. Pros:
   - Sin costo de API
   - Privacy completa
   - Sin rate limits

4. Cons:
   - Requiere GPU potente
   - Más lento que API cloud
   - Calidad depende del modelo
```

### Convai/Charisma.ai:

```
EXTERNAL SERVICES:

CONVAI:
- Especializado en NPCs conversacionales
- Memoria integrada
- $ crédito por month
- API easy de integrar

CHARISMA.AI:
- Storytellingfocused
- Memory y emotion tracking
- Good para narrative games
- Pricing similar

PROS:
- No tienes que construirlo
- Optimizado para game dev
- Soporte técnico

CONS:
- Costo recurrente
- Dependencia de servicio externo
- Customización limitada
```

---

## 7. Entregables

```
📁 npc-dialogue-system/
│
├── 📂 core/
│   ├── dialogue_manager.gd
│   ├── npc_profile.gd
│   ├── world_state.gd
│   ├── player_state.gd
│   ├── llm_integration.gd
│   └── cache.gd
│
├── 📂 ui/
│   ├── dialogue_box.tscn
│   ├── dialogue_box.gd
│   ├── choice_button.tscn
│   └── portrait_display.gd
│
├── 📂 npcs/
│   ├── merchant_gideon.tres
│   ├── scholar_elara.tres
│   ├── guard_roderick.tres
│   └── npc_profile.gd (base class)
│
├── 📂 scripts/
│   ├── quest_bridge.gd
│   ├── save_system_integration.gd
│   └── emotion_detector.gd
│
├── 📂 prompts/
│   ├── base_system_prompt.txt
│   ├── emotion_detection_prompt.txt
│   └── examples/
│
└── 📂 documentation/
    ├── setup_guide.md
    ├── npc_creation_guide.md
    └── api_reference.md
```

---

## 8. Aplicaciones prácticas

```
USOS:

1. RPG con diálogos ricos
   - NPCs únicos en cada playthrough
   - Menos writing necesario
   - Más inmersión

2. Narrative games
   - Diálogos procedurales
   - Choices que importan
   - Replayability

3. NPCs tutoriales
   - Explicaciones contextual
   - Adapta al jugador

4. Social simulation
   - NPCs que conversan entre sí
   - World's más alive
```

---

_Volver a [README principal](../README.md)_
