# 🎮 Proyecto 10: Micro-Game Collection para Validación

## Resumen Ejecutivo

**Objetivo:** Crear una colección de 10 micro-juegos pequeños (1-3 mechanics cada uno) para validar qué tipo de juegos funcionan mejor con AI-assistance y para tener un portfolio diverso de mechanics probadas.

**Herramientas principales:** Godot 4, Stable Diffusion, Claude Code, SEELE

**Tiempo estimado:** 6-8 semanas (1 juego/semana)

**Dificultad:** Baja-Media

**Resultado:** Portfolio de mechanics probadas + aprendizajes sobre qué funciona con AI.

---

## 1. Concepto

### Por qué micro-juegos:

```
VENTAJAS:
├── Rápidos de hacer (1 semana cada uno)
├── Fácil testear mecánicas específicas
├── Portfolio diverso
├── Aprendes qué funciona
├── AI assistance más efectiva
└── Feedback rápido

CADA MICRO-JUEGO:
- 1-3 mecánicas core
- 1-5 minutos de gameplay
- Tutorial implícito
- Feedback inmediato
- Art style consistente
```

### Lista de micro-juegos:

```
📋 LISTA DE 10 MICRO-JUEGOS:

1. DASH的平台 - Movement mechanic
   → Dash para evitar obstáculos
   → Timing-based

2. REFLECT - Physics mechanic  
   → Rebotar proyectiles
   → Puzzles de ángulos

3. CHAIN REACTION - Combo mechanic
   → Encadenar acciones
   → Caída en cascada

4. STEALTH TAP - Timing mechanic
   → Tap para esconderse
   → Ritmo y precisión

5. GRAVITY SHIFT - Puzzle mechanic
   → Cambiar gravedad
   → Navegar laberintos

6. AIM TRAINER - Skill mechanic
   → Mínimo para disparar
   → Altamente repeatable

7. RHYTHM DODGE - Rhythm mechanic
   → Dodging al ritmo
   → Sincronización

8. GROW - Accumulation mechanic
   → Crecer/consumir
   → Estrategia simple

9. ESCAPE - Chase mechanic
   → Huir de perseguidor
   → Tomar decisiones rápido

10. SURVIVE - Endurance mechanic
    → Durar lo más posible
    → Dificultad progresiva
```

---

## 2. Plan de implementación

### Juego 1: DASH platformer (Semana 1)

```
CONCEPTO:
"Un platformer donde solo puedes moverte con dash.
Tienes dash infinito pero cada dash te lleva en una dirección
fija que cambias con el mouse. Evita los pinchos."

MECÁNICAS:
├── Dash movement (dirección = mouse)
├── Invincibility frames durante dash
├── Pinchos como obstáculos
├── Goal: llegar al otro lado
└── Timer para speedrun

ART:
├── Estilo: Minimalista neon
├── Colores: Negro + cyan + magenta
├── Sprites: Geometría simple (triángulos, líneas)
└── Generados con SD

CÓDIGO:
├── Player controller (custom physics)
├── Dash mechanic
├── Obstacle spawner
├── Collision system
└── Win condition

ESCOPE:
├── 1 level simple
├── Tutorial implícito (murphy para aprender)
└── 1 estado de win/lose
```

```
DÍA 1: Diseño + setup
- Documentar mechanics
- Setup Godot project
- Configurar pixel art

DÍA 2-3: Player + dash
- Movement system
- Dash system
- i-frames
- Mouse direction

DÍA 4: Obstáculos + level
- Spikes/sawblades
- Level design
- Collision

DÍA 5: Art (AI)
- Generate sprites con SD
- Minimal neon aesthetic
- Post-processing

DÍA 6-7: Polish + testing
- Screen shake
- Particles
- Sound effects
- Test + fix
- Export
```

### Juego 2: REFLECT (Semana 2)

```
CONCEPTO:
"Eres un cuadrado. Dispara proyectiles que rebotan
en las paredes. Destruye todos los targets
 antes de quedarte sin balas."

MECÁNICAS:
├── Shoot projectiles
├── Physics-based bouncing
├── Wall reflection
├── Limited ammo
├── Destroy targets

ART:
├── Estilo: Isométrico low-poly
├── Colores: Pastel + sombras
└── Geometría simple

CÓDIGO:
├── Shoot system
├── Physics (bounce)
├── Target detection
└── Win/lose conditions

ESCOPE:
├── 5 niveles
├── Progresión de dificultad
└── Puntuación por efficiency
```

### Juego 3: CHAIN REACTION (Semana 3)

```
CONCEPTO:
"Toca para crear círculos que crecen.
Cada círculo toca otros círculos y los hace crecer también.
Goal: Crear la reacción más grande."

MECÁNICAS:
├── Touch to create
├── Growth animation
├── Collision triggers more growth
├── Chain reactions
└── Score based on chain

ART:
├── Estilo: Blob/slime
├── Colores: Vibrantes, random
├── Efectos de fusión
└── Generativo
```

### Juego 4: STEALTH TAP (Semana 4)

```
CONCEPTO:
"Un guardia patrulla. Toca para esconderte cuando
su línea de visión se acerca. Evita ser visto.
Sobrevive X segundos."

MECÁNICAS:
├── Guard patrol (patrón fijo)
├── Vision cone
├── Tap to hide
├── Detection = fail
└── Timer survival

ART:
├── Estilo: Noir/Shadow
├── Colores: Blanco + negro + rojo (danger)
└── Simple silhouette
```

### Juego 5: GRAVITY SHIFT (Semana 5)

```
CONCEPTO:
"El mundo rota 90° cada vez que tocas.
Navega el laberinto cambiando gravedad.
Llega a la salida."

MECÁNICAS:
├── Gravity directions (4: up, down, left, right)
├── Tap to rotate world
├── Momentum/inertia
├── Maze navigation
└── Collectibles opcionales

ART:
├── Estilo: Geometric maze
├── Colores: Monocromo + accent
└── Laberinto procedural
```

### Juego 6: AIM TRAINER (Semana 6)

```
CONCEPTO:
"Targets aparecen. Haz click en ellos rápido.
Targets más pequeños = más puntos.
Dificultad aumenta con el tiempo."

MECÁNICAS:
├── Click on targets
├── Smaller = more points
├── Time pressure
├── Accuracy tracking
└── Endless mode

ART:
├── Estilo: Retro arcade
├── Colores: Verde neón (como old CRT)
├── Targets variados
└── Score/accuracy display
```

### Juego 7: RHYTHM DODGE (Semana 7)

```
CONCEPTO:
"Patrones de obstáculos vienen al ritmo.
Mueve izquierda/derecha para esquivar.
El ritmo es la pista."

MECÁNICAS:
├── Rhythm-based spawning
├── Left/right movement
├── Pattern recognition
├── Combo system
└── Endless

ART:
├── Estilo: Synthwave
├── Colores: Púrpura + cyan + rosa
├── Grid visual para ritmo
└── Neon effects
```

### Juego 8: GROW (Semana 8)

```
CONCEPTO:
"Eres un círculo. Come partículas más pequeñas para crecer.
Evita partículas más grandes.
Eres más grande = más lento."

MECÁNICAS:
├── Eat to grow
├── Size = speed tradeoff
├── Avoid larger
├── Eat smaller
└── Survival/accumulation

ART:
├── Estilo: Cellular/biológico
├── Colores: Verdes, azules, orgánicos
├── Smooth growth animation
└── Membrane effect
```

---

## 3. Estructura común

### Cada juego comparte:

```
SHARED ELEMENTS:

├── Consistent menu system
├── Score tracking (global)
├── Settings (volume, etc.)
├── Common art style (within each game)
├── Tutorial system (if needed)
└── Export profiles (HTML5, Windows)
```

### Art style por juego:

```
PER GAME AESTHETIC:

1. DASH - Neon minimalista
2. REFLECT - Isométrico pastel  
3. CHAIN REACTION - Blob/vibrante
4. STEALTH TAP - Noir/siluetas
5. GRAVITY SHIFT - Geométrico/monocromo
6. AIM TRAINER - Retro arcade/CRT
7. RHYTHM DODGE - Synthwave
8. GROW - Cellular/biológico
9. ESCAPE - Dark thriller
10. SURVIVE - Abstracto
```

---

## 4. Prompts para AI

### Sprites genéricos:

```
DASH (Neon):
"minimal neon game sprite, cyan triangle on black background,
glowing edges, geometric, transparent background, 32x32"

REFLECT (Isometric):
"isometric cube, pastel pink, soft shadows,
low poly, game asset, transparent background, 64x64"

CHAIN REACTION:
"circular blob, gradient blue to purple,
semi-transparent, organic shape, game asset, 32x32"

STEALTH TAP:
"humanoid silhouette, noir style, black on white,
simple geometric, 32x64"

AIM TRAINER:
"target circle, neon green, retro arcade style,
glowing, transparent background, 32x32"
```

### Backgrounds:

```
Neon background:
"dark background, black, subtle grid lines in dark blue,
neon glow spots, game background, seamless"

Synthwave background:
"purple gradient background, synthwave aesthetic,
retro sun, grid perspective, game background"
```

---

## 5. Code templates

### Player base (Godot):

```gdscript
# player_base.gd
extends CharacterBody2D

@export var speed: float = 200.0
@export var jump_velocity: float = -400.0

var gravity: float = 980.0

func _physics_process(delta: float) -> void:
    # Apply gravity if not on floor
    if not is_on_floor():
        velocity.y += gravity * delta
    
    # Get input
    var input := Vector2.ZERO
    input.x = Input.get_axis("ui_left", "ui_right")
    
    # Apply movement
    velocity.x = input.x * speed
    
    move_and_slide()
```

### Simple state machine:

```gdscript
# state_machine.gd
extends Node

enum State { IDLE, MOVE, JUMP, DASH, DEAD }

var current_state: State = State.IDLE

func transition_to(new_state: State) -> void:
    current_state = new_state
    match new_state:
        State.IDLE:
            _enter_idle()
        State.MOVE:
            _enter_move()
        State.JUMP:
            _enter_jump()
        State.DASH:
            _enter_dash()
        State.DEAD:
            _enter_dead()
```

### Score manager:

```gdscript
# score_manager.gd
extends Node

var score: int = 0
var high_score: int = 0

func add_points(points: int) -> void:
    score += points
    if score > high_score:
        high_score = score

func reset() -> void:
    score = 0

func _ready() -> void:
    # Load high score from save
    high_score = PlayerPrefs.get("high_score", 0)
```

### Menu system:

```gdscript
# menu.gd
extends Control

signal start_game
signal show_settings
signal quit_game

func _on_play_pressed() -> void:
    start_game.emit()
    get_tree().change_scene_to_file("res://scenes/game.tscn")

func _on_settings_pressed() -> void:
    show_settings.emit()

func _on_quit_pressed() -> void:
    quit_game.emit()
    get_tree().quit()
```

---

## 6. Templates por juego

### GameManager template:

```gdscript
# game_manager.gd
extends Node

signal game_over
signal level_complete

@export var current_level: int = 1
@export var score: int = 0

func _ready() -> void:
    start_game()

func start_game() -> void:
    score = 0
    current_level = 1
    load_level(current_level)

func load_level(level_num: int) -> void:
    # Load level scene
    var level_path = "res://levels/level_%d.tscn" % level_num
    if ResourceLoader.exists(level_path):
        var level = load(level_path).instantiate()
        add_child(level)
    else:
        # No more levels - victory!
        victory()

func game_over() -> void:
    game_over.emit()
    # Show game over UI
    pass

func victory() -> void:
    level_complete.emit()
    # Show victory UI
    pass

func next_level() -> void:
    current_level += 1
    load_level(current_level)
```

---

## 7. Testing y feedback

### Playtest checklist:

```
PARA CADA JUEGO:

CONTROLES:
- [ ] Are controls intuitive?
- [ ] Is there input lag?
- [ ] Do controls feel responsive?
- [ ] Can you win/lose easily?

DIFICULTAD:
- [ ] Is it too easy?
- [ ] Is it too hard?
- [ ] Is difficulty appropriate?
- [ ] Is it fair?

ARTE:
- [ ] Is art style consistent?
- [ ] Is everything readable?
- [ ] Are colors clear?
- [ ] Is feedback visible?

SONIDO:
- [ ] Are there sound effects?
- [ ] Is audio balanced?
- [ ] Does audio match action?

UX:
- [ ] Is it clear what to do?
- [ ] Can you pause/quit?
- [ ] Is score visible?
- [ ] Is there win/lose state?
```

---

## 8. Publicación

### itch.io:

```
PARA CADA JUEGO:
├── Game title
├── Description (mechanics)
├── Screenshots (3-5)
├── GIF gameplay (10s)
├── Genre tags
├── Controls explanation
└── Price: Free o $1-2

COLECCIÓN:
├── "Micro-Game Experiments"
├── Todos los 10 juegos
├── Bundle page
└── Download links
```

### Portfolio:

```
WEBSITE:
├── List of micro-games
├── What was learned from each
├── Technical highlights
├── Link to play each
└── Contact info
```

---

## 9. Aprendizajes documentados

### Para cada juego:

```
JUEGO_N:
├── Tiempo total: X horas
├── AI assistance: X%
├── Qué funcionó bien con AI
├── Qué no funcionó con AI
├── Dificultad técnica
├── Dificultad de design
├── ¿Es divertido?
└── Feedback de testers
```

### Aggregate insights:

```
AL FINAL:
├── ¿En qué tipo de juegos AI es más útil?
├── ¿Qué limitaciones encontramos?
├── ¿Qué workflows mejoraron?
├── ¿Qué tomó más tiempo?
├── ¿Qué generó más problemas?
└── Recomendaciones para proyectos futuros
```

---

## 10. Timeline

```
SEMANA 1: DASH platformer
SEMANA 2: REFLECT
SEMANA 3: CHAIN REACTION
SEMANA 4: STEALTH TAP
SEMANA 5: GRAVITY SHIFT
SEMANA 6: AIM TRAINER
SEMANA 7: RHYTHM DODGE
SEMANA 8: GROW

PARCIAL 1 (semanas 1-4): Entregable
PARCIAL 2 (semanas 5-8): Entregable

TOTAL: 8 semanas
```

---

## 11. Costos

```
SOFTWARE:
- Godot: $0
- Stable Diffusion: $0 (local)
- Claude API: ~$5 (generación sprites)
- itch.io hosting: $0

HARDWARE:
- Tu PC actual: $0
- GPU para SD: Ya tienes

TOTAL: ~$5-10
```

---

## 12. Resultado final esperado

```
ENTREGABLES:
├── 10 micro-juegos jugables
├── Código fuente documentado
├── Assets generados con AI
├── Learnings documentados
├── Portfolio para展出
└── Pipeline de AI-optimized game dev
```

---

_Volver a [README principal](../README.md)_
