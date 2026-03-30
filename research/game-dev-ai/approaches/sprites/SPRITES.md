# 🎨 Generación de Sprites con IA

_Guía completa sobre herramientas, pipelines y técnicas para crear sprites de juegos usando inteligencia artificial._

---

## 📋 Índice

1. [Herramientas Principales](#herramientas-principales)
2. [Stable Diffusion Pipeline](#stable-diffusion-pipeline)
3. [Generación de Sprite Sheets](#generación-de-sprite-sheets)
4. [Pixel Art](#pixel-art)
5. [Character Consistency](#character-consistency)
6. [Workflows Recomendados](#workflows-recomendados)
7. [Prompts](#prompts)
8. [Código y Automatización](#código-y-automatización)

---

## Herramientas Principales

### Gratuitas/Open Source

| Herramienta | Mejor Para | Costo | Link |
|------------|------------|-------|------|
| **Stable Diffusion** | Sprite sheets, персонажей | Gratis (local) | [HuggingFace](https://huggingface.co/spaces/stabilityai/stable-diffusion) |
| **ComfyUI** | Workflows complejos | Gratis | [ComfyUI](https://github.com/comfyanonymous/ComfyUI) |
| **ControlNet** | Poses controladas | Gratis | [ControlNet](https://github.com/lllyasviel/ControlNet-v1-1-nightly) |
| **Fooocus** | Uso simple | Gratis | [Fooocus](https://github.com/foxy/foxy) |

### Proprietarias

| Herramienta | Mejor Para | Costo | Link |
|------------|------------|-------|------|
| **Leonardo AI** | Sprites consistency | $10-30/mes | [Leonardo.ai](https://app.leonardo.ai/) |
| **Midjourney** | Concept art alta calidad | $10-30/mes | [Midjourney](https://www.midjourney.com/) |
| **Scenario** | Game-ready assets | $10+/mes | [Scenario.com](https://www.scenario.com/) |
| **Rosebud AI** | Pixel art | Freemium | [Rosebud AI](https://play.rosebud.ai/home) |

---

## Stable Diffusion Pipeline

### Configuración Recomendada

```json
{
  "model": "stable-diffusion-xl-base-1.0",
  "guidance_scale": 7.5,
  "steps": 30,
  "negative_prompt": "low quality, worst quality, bad anatomy, bad hands, extra fingers"
}
```

### Modelos Recomendados para Sprites

| Estilo | Modelo | Link |
|--------|--------|------|
| **Anime/2D** | Animagine XL 3.1 | [Civitai](https://civitai.com/models/101407/animagine-xl-3-1) |
| **Pixel Art** | SDXL Pixel Art | [Civitai](https://civitai.com/models/2583/sdxl-pixel-art) |
| **Fantasy** | Dreamshaper XL | [Civitai](https://civitai.com/models/112197/dreamshaper-xl) |
| **Sci-Fi** | Juggernaut XL | [Civitai](https://civitai.com/models/79107/juggernaut-xl) |

---

## Generación de Sprite Sheets

### Pipeline con Gemini + Sharp (del artículo Firevibe)

```typescript
// Arquitectura del sistema
// 1. Subir imagen al Google Cloud Storage
// 2. Llamar 16 veces a Gemini 2.5 Flash en paralelo
// 3. Recibir frames generados
// 4. Stitch con Sharp para crear sprite sheet

const prompts = [
  "Using the character from the image, generate a full-body sprite...",
  // 15 prompts más, uno por frame
];

const responses = await Promise.all(
  prompts.map(prompt => generativeModel.generateContent({
    contents: [{
      role: 'user',
      parts: [
        { text: prompt },
        { fileData: { mimeType: file.type, fileUri: gcsUri } }
      ]
    }]
  }))
);
```

### Especificaciones de Sprite Sheets

| Tipo de Juego | Tamaño Base | Frames por Animación | Layout Sheet |
|--------------|-------------|---------------------|--------------|
| **Retro 8-bit** | 16x16, 32x32 | 3-8 | Linear |
| **Retro 16-bit** | 32x32, 64x64 | 6-12 | 4x4 grid |
| **Indie Moderno** | 64x64, 128x128 | 8-12 | 4x4 o 8x4 |
| **HD/Isométrico** | 256x256+ | 8-16 | Variable |

### Estructura de Nomenclatura

```
character_name/
├── idle/
│   ├── character_idle_001.png
│   ├── character_idle_002.png
│   └── ...
├── walk/
│   ├── character_walk_001.png
│   └── ...
├── attack/
│   └── ...
└── sprite_sheet/
    ├── character_idle_sheet.png (4x4 grid)
    ├── character_walk_sheet.png
    └── ...
```

---

## Pixel Art

### Herramientas Especializadas

| Herramienta | Características | Costo |
|------------|-----------------|-------|
| **PixelPerfect** | Generation with constraints | Freemium |
| **NightCafe** | Pixel art style | $10+/mes |
| **Rosebud AI** | Text-to-pixel-game | Freemium |
| **Stable Diffusion + Pixelart Colab** | SD + Pixel art LoRA | Gratis |

### Técnicas con ControlNet para Pixel Art

```
Prompt: "pixel art warrior character, 16-bit style, 4 directions"
Negative: "photorealistic, high resolution, smooth"

ControlNet Preprocessors:
- canny (for edge detection)
- openpose (for poses)
- tile_resample (for pixel consistency)
```

### LoRA para Estilo Consistente

```python
# Entrenar LoRA con 15-30 imágenes del mismo personaje
# Para mantener consistencia en todas las animaciones

training_config = {
    "lr": 1e-4,
    "batch_size": 4,
    "resolution": 512,
    "num_epochs": 10,
    "network_dim": 32,  # Para pixel art
    "optimizer": "AdamW"
}
```

---

## Character Consistency

### Técnica 1: Reference Image

```json
{
  "prompt": "same character as reference, different pose",
  "image": "reference_character.png"
}
```

### Técnica 2: LoRA Training

```bash
# Entrenar LoRA específico para tu personaje
python train_dreambooth.py \
  --instance_data_dir="./my_character" \
  --output_dir="./lora_output" \
  --concept="my_game_character" \
  --resolution=512 \
  --batch_size=2 \
  --learning_rate=1e-4 \
  --num_train_images=20
```

### Técnica 3: Character Sheet Template

```
Crear un character sheet con:
- Front view (idle)
- Back view
- Side views (L/R)
- 3/4 views
- Expression sheet
- Pose variations

Usar como input consistente para SD
```

---

## Workflows Recomendados

### Workflow 1: Indie Platformer 2D

```
1. Diseñar personaje base con Midjourney
   → "8-bit platformer character, red hero, simple design"

2. Crear variations para animations
   → Same style, different poses

3. Generar sprite sheets
   → 4x4 grid, 16 frames

4. Post-processing
   → Remove background (remove.bg)
   → Add to tilemap

Tiempo estimado: 30-60 min por personaje
```

### Workflow 2: RPG Characters

```
1. Character concept (Midjourney/Leonardo)
   → Full body, front view, 4 variations

2. Extract components
   → Body, face expressions, armor pieces

3. Build variations
   → Different equipment
   → Different expressions

4. Create sprite sheet per animation
   → Idle, walk, attack, magic, hurt, death

5. Generate UI elements
   → Portraits, icons, inventory items
```

### Workflow 3: Top-Down Shooter

```
1. Character base
   → 4-directional sprites

2. Enemy types
   → Variations with consistent style

3. Projectiles
   → Bullets, lasers, explosions

4. Environment tiles
   → Ground, walls, objects

5. Effects
   → Particles, muzzle flash, impact
```

---

## Prompts

### Prompts para Sprites de Personajes

```text
// Personaje base
"pixel art warrior character, 16x16 sprites, 4 color palette, 
front facing, idle pose, NES era style, transparent background"

// Animación walk cycle
"same character walking, 8 frames, pixel art, transparent background, 
consistent with previous sprite"

// Personaje con arma
"pixel art knight holding sword, same style as reference, 
front view, battle stance, 32x32, transparent background"

// Enemigo
"pixel art slime enemy, green translucent, bouncy idle animation,
16-bit style, 4 color palette"

// Personaje isométrico
"isometric RPG character, warrior class, 64x64, 8 directions,
dark fantasy art style, transparent background"
```

### Prompts para Estructuras/Entornos

```text
// Tile de tierra
"pixel art grass tile, 16x16, top-down view, 8-bit, 
seamless texture, transparent background"

// Tile de agua
"pixel art water tile, animated, 4 frames loop, 
top-down view, 16x16, transparent background"

// Edificio
"pixel art house, 64x64, front view, medieval fantasy,
transparent background, RPG style"

// Objeto interactivo
"pixel art treasure chest, closed, wooden, golden lock,
16x16, isometric 2.5D, transparent background"
```

### Prompts para UI

```text
// Icono de menú
"pixel art heart icon, 16x16, health symbol, red,
seamless on dark background, UI game element"

// Botón
"pixel art button, wooden style, 32x32, 
hover state included, RPG game UI"

// Barra de vida
"pixel art health bar, red to green gradient, 
wooden frame, 64x8, game UI element"
```

---

## Código y Automatización

### Script: Generar Sprite Sheet con Python

```python
# sprite_sheet_generator.py
from PIL import Image
import os
import requests
from io import BytesIO

def create_sprite_sheet(frames_dir, output_path, cols=4):
    """Crear sprite sheet desde frames individuales"""
    frames = sorted([f for f in os.listdir(frames_dir) if f.endswith('.png')])
    
    if not frames:
        raise ValueError("No frames found")
    
    # Leer primer frame para dimensiones
    sample = Image.open(os.path.join(frames_dir, frames[0]))
    frame_width, frame_height = sample.size
    
    # Calcular grid
    rows = (len(frames) + cols - 1) // cols
    
    # Crear sheet
    sheet = Image.new('RGBA', (frame_width * cols, frame_height * rows))
    
    for i, frame_name in enumerate(frames):
        row = i // cols
        col = i % cols
        
        frame = Image.open(os.path.join(frames_dir, frame_name))
        sheet.paste(frame, (col * frame_width, row * frame_height))
    
    sheet.save(output_path)
    print(f"Sprite sheet created: {output_path}")

def extract_frames_from_sheet(sheet_path, cols=4, rows=4):
    """Extraer frames individuales desde sprite sheet"""
    sheet = Image.open(sheet_path)
    frame_width = sheet.width // cols
    frame_height = sheet.height // rows
    
    frames = []
    for row in range(rows):
        for col in range(cols):
            x = col * frame_width
            y = row * frame_height
            frame = sheet.crop((x, y, x + frame_width, y + frame_height))
            frames.append(frame)
    
    return frames
```

### Script: API Leonardo AI para Sprites

```python
# leonardo_sprites.py
import requests
import os

LEONARDO_API_KEY = os.getenv("LEONARDO_API_KEY")

def generate_sprite(prompt, negative_prompt=None):
    """Generar sprite usando Leonardo AI"""
    url = "https://cloud.leonardo.ai/api/rest/v1/generations"
    
    headers = {
        "Authorization": f"Bearer {LEONARDO_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "prompt": prompt,
        "negative_prompt": negative_prompt or "low quality, deformed",
        "model_id": "6bef9f1b-33b5-4584-8b78-4c8e9c4c7e0a",  # Animagine XL
        "width": 512,
        "height": 512,
        "num_images": 1,
        "guidance_scale": 7.5,
        "prompt_magic": True
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

# Ejemplo uso
sprite = generate_sprite(
    prompt="pixel art ninja character, 16-bit era, transparent background, 4 color palette",
    negative_prompt="photorealistic, modern, high detail"
)
```

### Automatización con ComfyUI

```json
// sprite_generation_workflow.json
{
  "nodes": [
    {
      "id": "1",
      "type": "CheckpointLoaderSimple",
      "name": "Load Model",
      "widgets_values": ["animagine_xl.safetensors"]
    },
    {
      "id": "2", 
      "type": "CLIPTextEncode",
      "name": "Positive Prompt",
      "widgets_values": ["pixel art warrior, 16x16, transparent background"]
    },
    {
      "id": "3",
      "type": "CLIPTextEncode", 
      "name": "Negative Prompt",
      "widgets_values": ["low quality, bad anatomy, extra fingers"]
    },
    {
      "id": "4",
      "type": "ControlNetApply",
      "name": "Apply Pose",
      "widgets_values": ["pose_reference.png"]
    },
    {
      "id": "5",
      "type": "KSampler",
      "name": "Sampler",
      "widgets_values": [42, "fixed", 20, 7.5, "euler_a"]
    },
    {
      "id": "6",
      "type": "SaveImage",
      "name": "Save Sprite",
      "widgets_values": ["output/sprite_001.png"]
    }
  ]
}
```

---

## Frameworks de Generación Automatizada

### Pipeline Completo para Juegos 2D

```
┌─────────────┐
│ Concept Art │ → Midjourney / Leonardo
└──────┬──────┘
       ↓
┌─────────────┐
│ Character   │ → Character.com / Ready Player Me
│ Generator   │
└──────┬──────┘
       ↓
┌─────────────┐
│ Sprite      │ → Stable Diffusion + LoRA
│ Pipeline    │ → ControlNet for poses
└──────┬──────┘
       ↓
┌─────────────┐
│ Animation   │ → Sprite Sheet Generator
│ Composer    │ → 4x4 Grid Layout
└──────┬──────┘
       ↓
┌─────────────┐
│ Game Engine │ → Unity / Godot / GameMaker
│ Import      │
└─────────────┘
```

### Herramientas Especializadas en Pipeline

| Herramienta | Función | Integración |
|-------------|---------|-------------|
| **Charmed Tilemap Generator** | Generar tilemaps 2D completos | Unity, Godot |
| **Promethean AI** | World building con IA | Unreal, Unity, Blender |
| **Scenario** | Game-ready assets con API | Unity, Unreal |
| **Meshy** | Text-to-3D con个好 | Cualquier engine |

---

## Mejores Prácticas

### ✅ Hacer

1. **Usa siempre negative prompts** para excluir estilos no deseados
2. **Mantén consistente la paleta de colores** del juego
3. **Entrena LoRA** si tienes un estilo único
4. **Genera variaciones** y selecciona las mejores
5. **Usa ControlNet** para poses específicas
6. **Trabaja a resolución mayor** y reduce después

### ❌ No Hacer

1. **No generes sprites sueltos** — trabaja en sheets
2. **No mezcles estilos** de diferentes generadores
3. **No uses prompts vagos** — sé específico
4. **No saltees el post-processing** — limpia los fondos
5. **No ignores los spritesheets** para animaciones

---

## Recursos Adicionales

- [ComfyUI Workflows para Sprites](https://github.com/comfyanonymous/ComfyUI)
- [Stable Diffusion Sprites Guide](https://rentry.org/sd-sprites)
- [Pixel Art LoRA Collection](https://civitai.com/collections/pixel-art)
- [Sprite Sheet Templates](https://.game dev marketplace)

---

_Volver a [README principal](../README.md)_
