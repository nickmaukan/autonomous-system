# 📦 Proyecto 06: 3D Props Collection para Marketplace

## Resumen Ejecutivo

**Objetivo:** Crear una colección de props 3D de alta calidad usando herramientas AI (Tripo, Meshy) para vender en marketplaces.

**Herramientas principales:** Tripo, Meshy, Blender (para cleanup), Substance Painter (alternativo: PBR generators)

**Tiempo estimado:** 4-6 semanas

**Dificultad:** Media

**Mercado potencial:** $500-2000 recurrentes por colección

---

## 1. Concepto

### Propuesta de valor:

```
COLECCIÓN: "Scifi Props Megapack"

CONTENIDO:
├── Furniture (chairs, tables, desks, beds)
├── Electronics (consoles, monitors, terminals)
├── Containers (crates, lockers, containers)
├── Decorative (plants, posters, signs)
├── Weapons (mounted guns, melee)
├── Vehicles (hover bikes, drones, parts)
└── Building elements (walls, doors, windows)

FORMATO: FBX + textures (PBR)
CANTIDAD: 100+ props
CALIDAD: Game-ready, LODs
PRECIO SUGERIDO: $25-40
```

---

## 2. Plan de implementación

### Fase 1: Setup (Días 1-3)

```
DÍA 1: Configuración de herramientas

SOFTWARE:
├── Tripo AI (tripo3d.ai) - Generador 3D
├── Meshy AI (meshy.ai) - Generador 3D
├── Blender (blender.org) - Cleanup y export
├── Materialize (bismuth.software) - PBR texture gen
└── Asset Forge (kenney.nl) - Referencia

ACCOUNTS:
├── Tripo: Free tier (50 credits)
├── Meshy: Free tier (200 credits)
└── Blender: Gratis

FOLDER STRUCTURE:
```
scifi-props/
├── _source_raw/          # Raw outputs de AI
├── _blender_work/        # Work en progreso
├── _final/              # Listos para exportar
├── _renders/            # renders para marketing
└── _docs/              # Documentation
```
```

```
DÍA 2-3: Test de calidades

GENERAR 10 props de prueba:
├── Box/simple prop
├── Chair
├── Weapon
├── Vehicle part
├── Building element

TEST:
├── Calidad visual
├── Poly count
├── Texture resolution
├── Export compatibility
└── Tiempo de generación

DOCUMENTAR:
├── Settings óptimos por tipo
├── Prompts que funcionan
├── Errores comunes
└── Workarounds
```

### Fase 2: Generación masiva (Días 4-20)

```
SEMANA DE GENERACIÓN:

DÍA 4-6: Furniture
├── Desk with monitors (5 variations)
├── Chairs (gaming, office, command)
├── Tables (conference, workbench)
├── Storage (shelving, racks)
└── Beds/sleeping pods

DÍA 7-9: Electronics
├── Consoles/control panels
├── Monitors/displays
├── Terminals
├── Servers/data banks
└── Interface panels

DÍA 10-12: Containers/Storage
├── Crates (various sizes)
├── Lockers
├── Shipping containers
├── Coolers/preservation units
└── Weapon racks

DÍA 13-15: Decorative
├── Plants (alien flora)
├── Signs/posters
├── Lighting fixtures
├── Art/sculptures
└── Rugs/floor patterns

DÍA 16-18: Weapons/Tech
├── Mounted guns
├── Energy weapons (display)
├── Melee weapons (mounted)
├── Ammo boxes
└── Weapon parts

DÍA 19-20: Vehicles/Transport
├── Hover bike (full + parts)
├── Drone (surveillance, cargo)
├── Vehicle wheels/engines
├── Landing pads
└── Vehicle ramps
```

### Fase 3: Cleanup en Blender (Días 21-30)

```
WORKFLOW DE CLEANUP:

PARA CADA PROP:

1. Importar a Blender
2. Fix topology issues
3. UV unwrap (si no viene correcto)
4. Generate PBR textures
5. Create LODs (if needed)
6. Export as FBX
7. Package with textures

PYTHON SCRIPT: batch_export.py
```python
import bpy
import os
from pathlib import Path

def batch_export():
    input_folder = "_blender_work"
    output_folder = "_final"
    
    for fbx_file in Path(input_folder).glob("*.fbx"):
        # Import
        bpy.ops.import_scene.fbx(str(fbx_file))
        
        # Select all meshes
        bpy.ops.object.select_all(action='SELECT')
        
        # Apply transforms
        bpy.ops.object.transform_apply(
            location=True, rotation=True, scale=True
        )
        
        # Export
        output_path = Path(output_folder) / fbx_file.name
        bpy.ops.export_scene.fbx(
            str(output_path),
            use_selection=False,
            apply_scale_options='FBX_SCALE_ALL'
        )
        
        # Clear scene
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete()
```

SCRIPT PARA PBR TEXTURES:
```python
# Usar Materialize o similar para generar PBR
def generate_pbrTextures(mesh_path):
    # Generate textures
    # albedo, normal, roughness, metallic, AO
    pass
```

LOD GENERATION:
```python
def create_lods():
    # LOD0: Original
    # LOD1: 50% polygons
    # LOD2: 25% polygons
    # LOD3: 10% polygons
    pass
```
```

### Fase 4: Rendering + Marketing (Días 31-35)

```
RENDER SETTINGS (Blender Cycles):
├── Resolution: 1920x1080
├── Samples: 256
├── HDRI: Studio light
├── Ground: Infinite white
└── Camera: 45 degrees

CATALOGO:
├── 1 hero image (all items visible)
├── 5 category images
├── 10 detail shots
├── Video walkthrough (optional)
└── GIF animations (si hay animated)

METADATA:
├── Title: "Sci-Fi Props Megapack"
├── Description: Lista completa
├── Tags: sci-fi, props, 3d, game-ready, etc.
├── Specs: Poly count, textures, formats
└── License: Commercial
```

---

## 3. Prompts optimizados para 3D AI

### Tripo prompts:

```text
DESK WITH MONITORS:
"Futuristic command desk with holographic displays,
dark metal frame, glowing blue accents,
sci-fi aesthetic, game-ready prop"

LOCKER:
"Industrial sci-fi storage locker, heavy metal,
keypad lock visible, scratched surface,
rusted edges, emergency lighting strip"

HOVER BIKE:
"Futuristic hover bike, sleek design,
cyan glowing engine pods, pilot seat visible,
sci-fi vehicle, low-poly style"

ALIEN PLANT:
"Alien plant organism, bioluminescent,
cyan glowing veins, organic shape,
extraterrestrial flora, unique"

CONSOLE PANEL:
"Futuristic control console, multiple screens,
indicator lights, brushed metal,
sci-fi interface, complex detail"
```

### Meshy prompts:

```text
WEAPON RACK:
"Sci-fi weapon display rack, mountings for 5 weapons,
illuminated, glass case, industrial metal"

DRONE:
"Reconnaissance drone, compact design,
surveillance cameras, hover capability,
futuristic, unmanned vehicle"

CRATE:
"Cargo crate, reinforced metal,
caution markings, industrial,
stamped numbers, heavy-duty"
```

---

## 4. Especificaciones técnicas

### Standards:

```
POLY COUNT:
├── High LOD: 2,000-5,000 tris
├── Medium LOD: 1,000-2,000 tris
├── Low LOD: 500-1,000 tris
└── Shadow proxy: 100-200 tris

TEXTURES:
├── Albedo: 1024x1024 PNG
├── Normal: 1024x1024 PNG
├── Roughness: 1024x1024 PNG
├── Metallic: 1024x1024 PNG
└── AO: 512x512 PNG

FORMATS:
├── FBX (primary for engines)
├── OBJ (fallback)
├── GLB/GLTF (Web/alternativo)
└── Blender file (.blend) optional

NAMING:
{Category}_{Item}_{Variant}.fbx
Ejemplos:
Furniture_Desk_Command.fbx
Electronics_Console_Nav.fbx
Vehicles_HoverBike_01.fbx
```

---

## 5. Publicación

### Unity Asset Store:

```
PREPARATION:
├── Organize as Unity package structure
├── Create demo scene
├── Document prefabs
├── Record video
└── Prepare screenshots

LISTING:
├── Title: "Sci-Fi Props Megapack"
├── Category: 3D > Props > Sci-Fi
├── Price: $25-35
├── Description: [detallado con specs]
└── Tags: sci-fi, props, game-ready, scifi furniture
```

### Sketchfab:

```
UPLOAD:
├── Each prop as individual model
├── 3D pose/preview
├── PBR textures
├── Animated si aplica
└── License: Commercial

STORE:
├── Individual sales
├── Pack discount
└── Subscription option
```

---

## 6. Timeline

| Semana | Contenido |
|--------|-----------|
| Semana 1 | Setup + Test |
| Semana 2-3 | Generación furniture, electronics |
| Semana 3-4 | Containers, decorative, weapons |
| Semana 4-5 | Vehicles + cleanup |
| Semana 5-6 | Rendering + marketing + publish |

**TOTAL: 5-6 semanas**

---

## 7. Estimación de costos

```
TOOLS:
├── Tripo: $0 (free tier 50 credits) - ~15 props
├── Meshy: $0 (free tier 200 credits) - ~50 props
├── Blender: $0
├── Materialize: $0 (alternative: free tier)
└── Total: $0

OPCIONAL:
├── Paid credits para más props: $20-50
├── Premium textures: $10-20
└── Total opcional: $30-70

GANANCIAS POTENCIALES:
├── 100 props @ $25-40 = $2,500-4,000
├── After asset store cut (60-70%) = $750-1,600
└── Recurring: $100-300/mes
```

---

_Volver a [README principal](../README.md)_
