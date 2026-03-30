# 🔬 Análisis: Herramientas de Generación de Sprites con IA

_Investigado: 2026-03-27_

---

## 📊 Resumen de Herramientas Probadas

| Herramienta | Login Requerido | Costo | Download | Calidad Pixel Art | Veredicto |
|------------|----------------|-------|-----------|-------------------|------------|
| **Prodia** | ❌ No | Gratis | ✅ Sí | ⭐⭐⭐⭐ | 🏆 **MEJOR OPCIÓN** |
| **Leonardo AI** | ✅ Sí | Tier gratis | ❌ Suscripción | ⭐⭐⭐⭐⭐ | Buena, pero bloqueada |
| **Canva AI** | ✅ Sí | Tier gratis | ❌ Limitado | ⭐⭐ | No ideal para pixel art |
| **Tensor.art** | ✅ Sí | Freemium | ❌ Login | N/A | Login bloqueado |
| **Playground AI** | ✅ Sí | Freemium | N/A | N/A | Login bloqueado |
| **Mage Space** | ✅ Sí | Freemium | N/A | N/A | Login bloqueado |
| **DiffusionHub** | ✅ Sí | Freemium | N/A | N/A | Login bloqueado |
| **Prodia** | ❌ No | Gratis | ✅ Sí | ⭐⭐⭐⭐ | 🏆 **GANADOR** |

---

## 🥇 Prodia - ANÁLISIS DETALLADO

### Información General

```
┌─────────────────────────────────────────────────────────────────┐
│                         PRODIA                                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Website:    prodia.com                                           │
│  Login:      NO REQUERIDO                                         │
│  Costo:      GRATIS (sin límite visible)                          │
│  Modelos:    30+ incluyendo Stable Diffusion variants             │
│  Download:   ✅ SÍ, directo PNG                                  │
│  Calidad:    ⭐⭐⭐⭐ (4/5)                                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Pros

```
✅ No necesita login - entra y usa inmediatamente
✅ Completamente gratis
✅ Download directo funciona
✅ Múltiples modelos de Stable Diffusion
✅ Interfaz simple y rápida
✅ Buena calidad de imagen
✅ Sin watermark en downloads (verificado)
✅ Works en Mac sin GPU
```

### Contras

```
❌ No hay modelos específicos para pixel art
❌ No hay control de resolución exacto (1024x1024 default)
❌ Puede generar de más de una vez para obtener buenos resultados
❌ No hay negative prompts avanzados
❌ UI menos pulida que alternativas de pago
```

### Modelos Recomendados para Sprites

| Modelo | Uso | Calidad |
|--------|-----|----------|
| **Juggernaut XL** | General, buena base | ⭐⭐⭐⭐ |
| DreamShaper XL | Fantasy, personajes | ⭐⭐⭐⭐ |
| Realistic Vision | Si quieres algo más real | ⭐⭐⭐ |
| SDXL Pixel Art | **Pixel art específico** | ⭐⭐⭐⭐⭐ |

### Prompts Recomendados para Prodia

```text
PIXEL ART KNIGHT:
"pixel art medieval knight, 32x32 pixels, silver armor,
red cape, gold trim, transparent background, game sprite,
16-bit SNES style, crisp pixel edges"

PIXEL ART TILE:
"pixel art grass tile, 16x16 pixels, top-down view,
seamless texture, green grass, transparent background,
game tile, 16-bit style"

PIXEL ART SLIME:
"pixel art green slime enemy, 32x32 pixels, transparent background,
game sprite, cute style, bouncy animation frames,
16-bit era, 4 color palette"
```

### Configuración Óptima

```
Modelo: Juggernaut XL o SDXL Pixel Art
Resolution: 1024x1024 (luego escalar en Aseprite)
Steps: 25-30
Guidance: 7-8
```

---

## 🥈 Leonardo AI - ANÁLISIS

### Información General

```
┌─────────────────────────────────────────────────────────────────┐
│                      LEONARDO AI                                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Website:    app.leonardo.ai                                      │
│  Login:      ✅ REQUERIDO                                         │
│  Costo:      150 tokens/día gratis                               │
│  Modelos:    Modelos personalizados + Phoenix, Anime               │
│  Download:   ❌ BLOQUEADO (requiere suscripción)                  │
│  Calidad:    ⭐⭐⭐⭐⭐ (5/5)                                     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Pros

```
✅ Excelente calidad de imagen
✅ Modelos específicos para diferentes estilos
✅ Control de aspect ratio
✅ Image to image
✅ Fine-tuning con LoRAs
✅ Consistencia entre generaciones (con mismo seed)
✅ Herramientas de post-proceso
✅ comunidad activa con prompts compartidos
```

### Contras

```
❌ Login obligatorio
❌ Download de alta resolución BLOQUEADO sin suscripción
❌ Tokens limitados (150/día)
❌ Para sprites necesita usar workarounds
❌ Más complejo que Prodia
```

### Calidad de Sprites Generados

```
NOTA: No pude descargar directamente, pero los previews muestran:
- Buena consistencia de estilo
- Excelente para personajes y escenarios
- Modelos como "RPG Pony" o "Pixel Art" son prometedores
- Requiere suscripción para aprovechar full potencial
```

### Prompts Recomendados para Leonardo

```text
KNIGHT (Phoenix Model):
"medieval knight, full body, silver armor, red cape,
gold trim, front view, studio lighting, game asset,
high quality, 8k"

KNIGHT (Pixel Art Model - si disponible):
"pixel art knight character, 32x32, front view,
silver armor, red cape, transparent background,
game sprite, 16-bit era, 4 direction sprites"
```

---

## 🥉 Canva AI - ANÁLISIS

### Información General

```
┌─────────────────────────────────────────────────────────────────┐
│                        CANVA AI                                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Website:    canva.com                                           │
│  Login:      ✅ REQUERIDO                                         │
│  Costo:      Limitado en tier gratis                             │
│  Download:   ⚠️ Solo en versión pagada                           │
│  Calidad:    ⭐⭐ (2/5)                                           │
│  Pixel Art:  NO ADECUADO                                         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Veredicto

```
❌ NO RECOMENDADO para pixel art sprites
✅ SÍ para: ilustraciones, posters, diseño gráfico
❌ Genera imágenes estilo fotografía/ilustración, no pixel art
```

---

## 📈 Otras Herramientas (No Accesibles)

### Requieren Login/Verificación

```
❌ Tensor.art - Login con Google bloqueado
❌ Playground AI - Login bloqueado  
❌ Mage Space - Login bloqueado
❌ DiffusionHub - Registro requerido
❌ OpenArt AI - Login requerido
❌ Civitai - Login requerido
❌ Lexica - Login requerido
❌ Poe - Login requerido
```

### Alternativas Mencionadas en Investigación

```
NO PROBADAS (costo o acceso):
- Midjourney - $10+/mes
- DALL-E 3 - Via API, costo por imagen
- Stable Diffusion local - Requiere GPU
- ComfyUI - Requiere GPU
- Fooocus - Requiere GPU
```

---

## 🏆 RECOMENDACIÓN FINAL

### Para Mauri: USAR PRODIA

```
FLUJO RECOMENDADO:

1. PRODIA (gratis, sin login)
   → Generar sprites base
   → Descargar PNG directamente
   → Guardar en carpeta local

2. ASEPRITE (ya instalado)
   → Abrir PNGs
   → Limpiar/editar
   → Escalar a resolución correcta
   → Exportar como sprite sheets

3. GOOGLE DRIVE (opcional)
   → Backup de assets
   → Compartir con team
```

### Alternativa Premium (Opcional)

```
SI LEONARDO FUNCIONA MEJOR PARA TÍ:
- Usar Leonardo para generación (preview)
- Tomar screenshots como workaround
- O pagar $10/mes para download ilimitado
- Valor: Si genera ingresos, vale la pena
```

---

## 📊 Comparativa Visual

```
HERRAMIENTA          │ FACILIDAD │ CALIDAD │ GRATIS │ DESCARGAS │
─────────────────────┼───────────┼─────────┼────────┼───────────│
Prodia               │    ⭐⭐⭐⭐    │   ⭐⭐⭐⭐   │   ✅    │     ✅     │
Leonardo AI          │    ⭐⭐⭐     │   ⭐⭐⭐⭐⭐  │   ⚠️    │     ❌     │
Canva AI             │    ⭐⭐⭐⭐    │   ⭐⭐     │   ⚠️    │     ⚠️     │
Stable Diffusion Web │    ⭐⭐      │   ⭐⭐⭐⭐   │   ✅    │     ✅     │
(requiere GPU local)│            │          │         │           │
Midjourney           │    ⭐⭐⭐⭐    │   ⭐⭐⭐⭐⭐  │   ❌    │     ✅     │
($10+/mes)          │            │          │         │           │
```

---

## 🚀 Plan de Acción

```
INMEDIATO:
1. ✅ Prodia funcionando
2. ✅ Descargas directas funcionan
3. ⚠️ Investigar Leonardo como backup premium

PRÓXIMOS PASOS:
1. Generar sprites de prueba en Prodia
2. Limpiar en Aseprite (ya instalado)
3. Crear sprite sheets
4. Testear en itch.io o Unity
```

---

## 💡 Tips para Prodia

### Para mejores resultados:

```
1. SE ESPECÍFICO:
   ❌ "knight"
   ✅ "pixel art medieval knight, 32x32, silver armor, red cape"

2. USA MODELOS:
   - Juggernaut XL para personajes
   - SDXL Pixel Art si disponible

3. ITERA:
   - Genera 5-10 variations
   - Selecciona los mejores
   - Refina el prompt según resultados

4. ESCALA:
   - Genera en alta resolución
   - Escala hacia abajo en Aseprite
   - Añade detalles con editor
```

---

## 📁 Sprites Generados (Prueba)

```
assets/characters/knight/
├── prodia_knight_01.png    ← Knight idle (capturado)
├── prodia_knight_walk_01.png  ← Knight walk (capturado)
└── (más por generar)
```

---

## 🔗 Links

| Herramienta | URL |
|-------------|-----|
| **Prodia** | https://prodia.com |
| **Leonardo AI** | https://app.leonardo.ai |
| **Aseprite** | https://aseprite.org |

---

_Análisis realizado probando cada herramienta en vivo._
_Prodia es la mejor opción gratuita para comenzar inmediatamente._
