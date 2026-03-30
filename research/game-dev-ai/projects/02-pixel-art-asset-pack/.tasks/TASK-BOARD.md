# 📋 Task Board - Medieval Pixel Art Collection

> **Project Manager:** Aurus ⚡  
> **Sprint:** 1 (Kickoff)

---

## 🚀 Sprint Backlog

### TODO - Pendientes de iniciar

| ID | Tarea | Prioridad | Estimación | Dependencias |
|----|--------|-----------|------------|--------------|
| T-001 | Setup Leonardo AI + cuentas | 🔴 Alta | 1h | - |
| T-002 | Definir Style Guide completo | 🔴 Alta | 4h | T-001 |
| T-003 | Crear folder structure | 🟡 Media | 1h | - |
| T-004 | Generar Knight sprite sheet | 🔴 Alta | 4h | T-002 |
| T-005 | Generar Archer sprite sheet | 🔴 Alta | 4h | T-002 |
| T-006 | Generar Enemies (Slime, Skeleton, Goblin) | 🔴 Alta | 6h | T-002 |
| T-007 | Generar Tiles (Ground, Stone, Castle) | 🟡 Media | 6h | T-002 |
| T-008 | Generar Props (Weapons, Items, Furniture) | 🟡 Media | 6h | T-002 |
| T-009 | Generar UI Elements | 🟡 Media | 4h | T-002 |
| T-010 | Generar Effects (Particles, Projectiles) | 🟢 Baja | 3h | T-002 |
| T-011 | Assembly y organización final | 🔴 Alta | 4h | T-004,T-005,T-006,T-007,T-008,T-009 |
| T-012 | Crear metadata.json | 🟡 Media | 2h | T-011 |
| T-013 | Crear README + Documentation | 🟡 Media | 2h | T-011 |
| T-014 | QA Final - Verificación completa | 🔴 Alta | 4h | T-012,T-013 |
| T-015 | Preparar para publicación | 🟡 Media | 3h | T-014 |
| T-016 | Publicar en itch.io | 🟢 Baja | 1h | T-015 |

### IN PROGRESS - En desarrollo

| ID | Tarea | Status | Asignado | Review |
|----|--------|--------|----------|--------|
| - | Ninguna actualmente | - | - | - |

### IN REVIEW - En revisión

| ID | Tarea | Reviewer | Status | Feedback |
|----|--------|----------|--------|----------|
| - | Ninguna actualmente | - | - | - |

### QA TESTING - En testing

| ID | Tarea | Tester | Resultado | Bugs |
|----|--------|--------|-----------|------|
| - | Ninguna actualmente | - | - | - |

### DONE - Completadas

| ID | Tarea | Completada | QA |
|----|--------|------------|-----|
| - | Ninguna | - | - |

---

## 📊 Sprint Stats

```
SPINT 1 - Kickoff
═══════════════════════════════════════════
Total Tasks:     16
Completed:       0
In Progress:     0
In Review:      0
QA Testing:      0
Blocked:         0

Progress:        ░░░░░░░░░░░░░░░░░░░░░ 0%

Sprint Goal:     Setup + Primeros assets
ETA:            Pendiente
```

---

## 🔄 Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                     TASK WORKFLOW                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  TODO ──────► IN PROGRESS ──────► IN REVIEW ──────► QA         │
│    │              │                  │                │           │
│    │              │                  │                │           │
│    │              ▼                  ▼                ▼           │
│    │         [Dev Task]         [Review]        [QA Test]     │
│    │              │                  │                │           │
│    │              │                  │                │           │
│    │              └────── FAILED ────┴────────────────┘         │
│    │                                                            │
│    │                    PASSED                                   │
│    └────────────────────────────────────────────────► DONE       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘

FAILED → Vuelve a TODO con comments de por qué falló
```

---

## 🎯 Definition of Done

```
✓ Completada según specs
✓ Revisada por PM/Diseñador
✓ Pasó QA sin blockers
✓ Documentación actualizada
✓ Assets en folder correcto
✓ Metadata preenchida
✓ README actualizado
```

---

## 📁 Ubicación de archivos

```
.gitkeep
.tasks/
├── TASK-BOARD.md     ← Este archivo
├── T-001.md         ← Task individual
├── T-002.md
└── ...

assets/
├── characters/       ← Sprites de personajes
├── tiles/           ← Tiles de environments
├── props/           ← Props y objetos
├── ui/              ← UI elements
└── effects/         ← Effects y particles
```

---

_Last updated: 2026-03-27_
