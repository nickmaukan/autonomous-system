# Instagram Widget — Guía de Configuración

## Opciones disponibles

El sitio tiene **dos formas** de mostrar contenido de Instagram:

---

## Opción 1: Catálogo Visual (YA INSTALADO)

Las 8 imágenes placeholder ya están en el sitio en la sección `#instagram`. Para actualizarlas:

1. Abre `index.html` y busca la sección `<!-- INSTAGRAM CATÁLOGO VISUAL -->`
2. Reemplaza los `src` de las `<img>` con las URLs de las fotos reales de Instagram
3. O descarga las imágenes y guárdalas en `/images/instagram/`

**Ventajas:** Rápido, sin dependencias externas, carga inmediata.
**Desventaja:** Hay que actualizar manualmente.

---

## Opción 2: Widget Automático con Elfsight (RECOMENDADO)

El código del widget está preparado pero **comentado**. Para activarlo:

### Paso 1: Crear cuenta en Elfsight
1. Ir a **https://elfsight.com/**
2. Click en **"Instagram Widget"** → **"Create widget"**
3. Conectar con la cuenta de Instagram `@entramados_estudio78`
4. Personalizar: diseño (grid), número de fotos (8-12), tamaño
5. Hacer clic en **"Get Code"**

### Paso 2: Obtener el código
El código tendrá esta estructura:
```html
<script src="https://static.elfsight.com/analytics/loader.js" defer></script>
<div class="elfsight-app-XXXXXXXXXXXX"></div>
```

### Paso 3: Activar en index.html
1. Abrir `index.html`
2. Buscar `<!-- Elfsight Instagram Widget (gratuito) -->`
3. **Descomentar** el bloque:
   ```html
   <script src="https://static.elfsight.com/analytics/loader.js" defer></script>
   <div class="elfsight-app-TU-ID-AQUI"></div>
   ```
4. Reemplazar `TU-ID-AQUI` con el ID real del widget (ej: `a1b2c3d4-e5f6-7890`)
5. **Eliminar o comentar** las 8 imágenes placeholder si prefieres solo el widget

### Plan gratuito de Elfsight incluye:
- ✅ Grid de hasta 9 fotos
- ✅ Enlace a perfil de Instagram
- ✅ Sin marca de agua obligatoria
- ✅ Actualizaciones automáticas

---

## Opción 3: Walls.io (alternativa)

1. Ir a **https://walls.io/**
2. Crear un widget social wall gratuito
3. Obtener el `data-wall-id`
4. Descomentar en `index.html`:
```html
<script src="https://walls.io/js/wallsio-widget-1.2.js"></script>
<div class="wallsio-widget" data-wall-id="TU-ID"></div>
```

---

## Notas técnicas

- La sección Instagram está insertada **después de "Sobre Nosotros"** y **antes de "Contacto"**
- Mantiene el estilo del sitio: fondo blanco, tipografía serif para títulos
- El botón "Ver más en Instagram" es un enlace directo al perfil
- El widget Elfsight se carga de forma asíncrona — no afecta la velocidad del sitio
- Para máximo rendimiento, usar Option 1 (catálogo manual con imágenes optimizadas)

---

## Checklist antes de lanzar

- [ ] Reemplazar imágenes placeholder con fotos reales
- [ ] Verificar que las imágenes pesen < 100KB cada una (optimizar con Squoosh)
- [ ] Si se usa widget: probar en móvil y escritorio
- [ ] Verificar que el botón linkea correctamente a `@entramados_estudio78`
- [ ] Eliminar el código no usado (placeholder images o widget commented)
