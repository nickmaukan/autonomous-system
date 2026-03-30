# 🎨 Proyecto 01: Pipeline de Sprites con LoRA Training

## Resumen Ejecutivo

**Objetivo:** Crear un pipeline completo y reusable para generar sprites de personajes con consistencia de estilo usando Stable Diffusion + LoRA (Low-Rank Adaptation).

**Herramientas principales:** Stable Diffusion (local), Fooocus, Dreambooth/LoRA training scripts, ComfyUI

**Tiempo estimado:** 2-3 semanas para setup completo

**Dificultad:** Media-Alta (requiere configuración técnica)

**Qué resuelve:** La principal debilidad de SD para sprites - la inconsistency de estilo entre generaciones.

---

## 1. Problema que resuelve

### El problema actual de generar sprites con AI:

```
❌ GENERACIÓN SIN LoRA:
   Sprite 1: "warrior with red armor"
   Sprite 2: "warrior with red armor"  
   Sprite 3: "warrior with red armor"
   
   Resultado: 3 guerreros que NO se parecen en nada
   - Diferentes proporciones
   - Diferente estilo de cara
   - Diferentes colores de armadura
   - Inconsistentes para animation frames

✅ CON LoRA ENTRENADO:
   Sprite 1-100: Mismo personaje, poses diferentes
   
   Resultado: Consistencia perfecta
   - Mismas proporciones
   - Mismo estilo facial
   - Paleta de colores idéntica
   - Perfecto para sprite sheets
```

### Por qué es importante:

1. **Sprite sheets requieren consistency** - 16 frames de walk cycle deben ser idénticos excepto por pose
2. **Character consistency** - Player, enemies, NPCs deben pertenecer al mismo universo visual
3. **Animation smoothness** - Inconsistencia causa "jumpy" animation

---

## 2. Stack tecnológico

### Software necesario:

```
CORE:
├── Stable Diffusion WebUI (AUTOMATIC1111) o ComfyUI
├── Fooocus (alternativa más simple)
├── Kohya_ss (para LoRA training)
└── Python scripts para automatización

OPCIONAL:
├── ControlNet (para poses controladas)
├── LoRA (modelos pre-entrenados)
└── inpaint masking (para fixing)
```

### Hardware:

```
MÍNIMO: RTX 3060 12GB
- LoRA training: 20-40 minutos
- Inference: 5-15 segundos por imagen

ÓPTIMO: RTX 4090 24GB
- LoRA training: 10-20 minutos
- Inference: 2-5 segundos por imagen

⚠️ CPU only: NO RECOMENDADO (10x más lento)
```

### Configuración de SD:

```json
{
  "model": "stable-diffusion-xl-base-1.0",
  "vae": "sdxl-vae-fp16-fix",
  "resolution": 1024,
  "batch_size": 4,
  "guidance_scale": 5.0,
  "steps": 25
}
```

---

## 3. Plan de implementación

### Fase 1: Setup del ambiente (Días 1-3)

```
DÍA 1: Instalación
├── Instalar Stable Diffusion WebUI
│   ├── Git clone
│   ├── Instalar Python 3.10+
│   ├── Crear venv
│   └── Test run
├── Instalar Fooocus (alternativa simple)
│   └── Descargar de GitHub
├── Instalar Kohya_ss
│   ├── Git clone
│   ├── Setup venv
│   └── Test run
└── Descargar SDXL base model (6.5GB)

DÍA 2: Configuración
├── Configurar paths correctamente
├── Instalar modelos VAE
├── Probar generación básica
├── Verificar VRAM usage
└── Documentar workflows

DÍA 3: Primeras pruebas
├── Generar sprites sin LoRA
├── Identificar problemas de consistency
├── Probar prompts con style tokens
├── Empezar a documentar qué funciona
└── Setup folder structure
```

### Fase 2: Recolección de datos (Días 4-6)

```
DÍA 4-5: Crear dataset de entrenamiento

REQUIREMENTS PARA LORA DE PERSONAJE:
- 15-30 imágenes mínimo
- Mismo personaje en diferentes poses
- Mismo fondo (transparente o consistente)
- Misma iluminación
- Imágenes de alta resolución (512x512 mínimo)

OPCIÓN A: Generar con Midjourney/Leonardo
├── Generar 30 variaciones del mismo personaje
├── Seleccionar las más consistentes
├── Recortar a cuadrado
└── Limpiar backgrounds

OPCIÓN B: Usar sprites existentes como base
├── Sprites de juegos retro (CC0)
├── Modificar con SD para crear variaciones
└── Usar como dataset

OPCIÓN C: Dibujar/photographear
├── Dibujar sketch básico
├── Generar variaciones con SD
├── Seleccionar mejores
└── Recopilar 20-30 imágenes finales

DÍA 6: Preprocessing del dataset

HERRAMIENTAS:
├── rembg (background removal)
├── Pillow (resize y crop)
├── upscale (SD upscale si necesario)
└── manual cleanup (Photoshop/GIMP)

PASOS:
1. Remove background → PNG transparente
2. Resize a 512x512 o 1024x1024
3. Center character
4. Verificar que todas las imágenes sean del mismo estilo
5. Descartar inconsistentes
6. Organizar en folders
```

### Fase 3: LoRA Training (Días 7-10)

```
DÍA 7: Configuración de Kohya_ss

PARÁMETROS ÓPTIMOS PARA SPRITES:

{
  "network_module": "networks.lora",
  "network_dim": 32,           # Para pixel art (bajo)
  "network_alpha": 16,          # Half of dim
  "lr": "1e-4",
  "lr_scheduler": "cosine_with_restarts",
  "lr_warmup_steps": 100,
  "max_train_steps": 1000-2000, # 1000 para test, 2000 para final
  "batch_size": 2,             # Ajustar según VRAM
  "gradient_accumulation_steps": 4,
  "optimizer": "AdamW8bit",
  "optimizer_args": ["weight_decay=0.01"],
  "train_batch_size": 2,
  "noise_offset": 0.1,
  "resolution": "512,512",
  "caption_extension": ".txt",
  "enable_bucket": true,
  "min_bucket_reso": 256,
  "max_bucket_reso": 1024
}

SCRIPT DE ENTRENAMIENTO:
├── Crear config file
├── Preparar captions
│   └── Template: "pixel_art_character style"
├── Run training
└── Monitorear loss

DÍA 8-9: Iteración de LoRA

TESTING:
├── Generar 10 sprites con LoRA
├── Evaluar consistencia
├── Ajustar parámetros si necesario
├── Re-entrenar si resultados pobres
└── Guardar múltiples versions (steps 500, 1000, 1500, 2000)

MÉTRICAS DE EVALUACIÓN:
- ✅ Consistencia facial entre sprites
- ✅ Proporciones corporales consistentes
- ✅ Rango de poses disponibles
- ✅ Estilo visual consistente
- ✅ Paleta de colores consistente
```

### Fase 4: Workflow de generación (Días 11-14)

```
DÍA 10-12: Crear workflow en ComfyUI o SD WebUI

WORKFLOW Components:

1. INPUT
   ├── Reference image (pose/style)
   ├── Pose description
   ├── Action/frame number
   └── Color adjustments

2. GENERATION
   ├── LoRA model selector
   ├── Prompt template
   ├── Negative prompt
   ├── ControlNet (OpenPose)
   └── Sampler settings

3. POST-PROCESSING
   ├── Background removal
   ├── Resize to target resolution
   ├── Batch rename
   └── Organize into sprite sheet grid

DÍA 13-14: Automatización

PYTHON SCRIPTS:
├── generate_sprite_batch.py
│   ├── Lee lista de poses
│   ├── Genera batch de sprites
│   ├── Aplica post-processing
│   └── Organiza output
│
├── create_sprite_sheet.py
│   ├── Lee frames individuales
│   ├── Crea grid layout
│   ├── Genera PNG final
│   └── Genera metadata JSON
│
└── validate_consistency.py
    ├── Compara sprites generados
    ├── Detecta inconsistencias
    └── Reporta problems
```

---

## 4. Prompts optimizados

### Para entrenamiento LoRA:

```text
Captions del dataset:

"pixel_art_knight style"
"pixel_art_knight_armor style"
"pixel_art_knight_helmet style"
"pixel_art_knight_sword style"
```

### Para generación post-LoRA:

```text
POSITIVE PROMPT:
"pixel_art_knight style, walking pose, facing front, 
transparent background, 16x16, sprite sheet frame, 
game character, consistent with reference"

NEGATIVE PROMPT:
"photorealistic, 3d render, high detail, smooth shading,
blurry, low quality, bad anatomy, extra fingers,
different character, inconsistent style"

CONTROLNET:
"use_openpose_for_consistency"
```

### Templates por tipo de juego:

```text
8-BIT RETRO:
"pixel_art_character style, 16x16, NES era, 4 color palette,
dithering, transparent background"

16-BIT SNES:
"pixel_art_character style, 32x32, SNES era,
smooth gradients, transparent background"

MODERN INDIE:
"pixel_art_character style, 64x64, smooth pixel art,
rich colors, transparent background, modern indie game"
```

---

## 5. Entregables esperados

### Al finalizar el proyecto:

```
📁 sprite-pipeline-lora/
│
├── 📂 trained_models/
│   ├── knight_v1.safetensors    # LoRA entrenado
│   ├── knight_v2.safetensors
│   └── metadata.json
│
├── 📂 workflows/
│   ├── basic_sprite_gen.json    # ComfyUI workflow
│   ├── sprite_sheet_gen.json
│   └── batch_generation.json
│
├── 📂 scripts/
│   ├── generate_sprites.py
│   ├── create_sprite_sheet.py
│   └── validate_consistency.py
│
├── 📂 documentation/
│   ├── setup_guide.md
│   ├── training_guide.md
│   └── workflow_guide.md
│
└── 📂 sample_outputs/
    ├── character_idle_sheet.png
    ├── character_walk_sheet.png
    └── test_generations/
```

### Métricas de éxito:

| Métrica | Target | Cómo medir |
|---------|--------|------------|
| Consistencia visual | 90%+ | 20 sprites random, evaluación manual |
| Tiempo por sprite | <30 seg | promedio de 50 generaciones |
| Tiempo por sprite sheet | <10 min | generación completa de 16 frames |
| Frames usables | >85% | sprites que no requieren fix manual |

---

## 6. Aplicaciones prácticas

### Usos del pipeline:

1. **Crear assets para juegos propios**
   - Personajes completos con todas las animaciones
   - Enemigos y NPCs consistentes
   - Items y props

2. **Crear asset packs para vender**
   - Character packs (10-20 personajes)
   - Animation packs (múltiples sheets por personaje)
   - Theme packs (medieval, sci-fi, fantasy)

3. **Servicio para otros desarrolladores**
   - "Generamos sprites con tu estilo"
   - 1-2 días de turnaround
   - $200-500 por personaje completo

---

## 7. Troubleshooting

### Problemas comunes:

```markdown
## PROBLEMA: LoRA no captura el estilo

CAUSAS POSIBLES:
- Dataset muy pequeño (<15 imágenes)
- Imágenes muy diferentes entre sí
- Training steps muy pocos o muchos
- Learning rate muy alto/bajo

SOLUCIONES:
- Aumentar dataset a 30+ imágenes
- Asegurar que todas las imágenes son del mismo estilo
- Probar diferentes learning rates (1e-4, 5e-5, 1e-5)
- Ajustar network_dim (16 para estilo fuerte, 64 para sutil)

## PROBLEMA: Overfitting (memoriza las imágenes)

SÍNTOMAS:
- Genera las imágenes del dataset exactamente
- No puede crear poses nuevas

SOLUCIONES:
- Reducir network_dim
- Aumentar dataset
- Reducir training steps
- Usar stronger noise_offset

## PROBLEMA: Inconsistencia aún con LoRA

SÍNTOMAS:
- El LoRA entrenado no mantiene consistencia

SOLUCIONES:
- Usar imagen de referencia + ControlNet
- Incluir poses muy diferentes en dataset
- Entrenar por más tiempo
- Probar con SDXL en vez de SD 1.5
```

---

## 8. Coste y alternativas

### Coste:

```
HARDWARE:
- Si tienes GPU NVIDIA: $0 adicional
- Si no: Rent a GPU (Paperspace, RunPod)
  └── ~$0.50-1.00 por hora
  └── Training: 2-4 horas = $1-4

SOFTWARE:
- Todo es gratis (open source)
- Modelos base: gratis
- LoRA storage: ~50MB cada uno

TOTAL: $0-10
```

### Alternativas si no tienes GPU:

```
OPCIÓN 1: Google Colab
- Gratis con limitaciones
- T4 GPU disponible
- Notebook pre-hechos para LoRA

OPCIÓN 2: Render (cloud GPU)
- RTX 4000 ~$0.50/hr
- 4 horas de training = $2

OPCIÓN 3: Fal.ai / Replicate
- API para SD + LoRA
- Pay per generation
- Sin setup local
```

---

## 9. Siguientes pasos

### Después de completar este proyecto:

1. **Aplicar a asset packs** → Crear 10 personajes para vender
2. **Entrenar más LoRAs** → Diferentes estilos (sci-fi, fantasy, modern)
3. **Crear pipeline automatizado** → De texto a sprite sheet completo
4. **Integrar con game engine** → Exportar directamente a Godot/Unity

---

## 10. Recursos

### Documentación:

- [Kohya_ss GitHub](https://github.com/bmaltais/kohya_ss)
- [SD LoRA Training Guide](https://rentry.org/sd-lora-training)
- [ComfyUI LoRA Workflows](https://github.com/comfyanonymous/ComfyUI)
- [Pixel Art LoRA Collection](https://civitai.com/collections/pixel-art)

### Tutoriales en video:

- "LoRA Training for Characters" - YouTube search
- "Stable Diffusion Sprite Sheet Workflow" - YouTube search
- "ComfyUI for Game Dev" - YouTube search

---

_Volver a [README principal](../README.md)_
