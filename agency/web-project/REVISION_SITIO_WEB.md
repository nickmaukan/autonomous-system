# REVISIÓN: Entramados Estudio — Sitio Web Nuevo vs Original

**Fecha:** 2026-03-21  
**Revisor:** Agent Reviewer  
**Sitio original:** https://entramadosstudio.com (inaccesible al momento de revisar)  
**Sitio nuevo:** `/Users/nickmaukan/AutonomousSystem/agency/web-project/index.html`

---

## 1. LISTA DE SECCIONES ENCONTRADAS

### Sitio Original (según brief)
| # | Sección | Descripción |
|---|--------|-------------|
| 1 | Header con logo | Navegación superior |
| 2 | Hero | Tagline "Arquitectura \| Mobiliario \| Interiorismo" |
| 3 | SIGUENOS EN | Instagram feed |
| 4 | NUESTROS FAVORITOS | Selección de productos destacados |
| 5 | CATEGORÍAS DESTACADAS | ESCRITORIOS, ALMACENAMIENTO, etc. |
| 6 | Productos | COCINAS, SOFABEDS |
| 7 | Quote/Tagline | "Quality into the fashion conscious home" |
| 8 | JOIN THE CLUB | Email signup |
| 9 | FOLLOW US | Instagram |
| 10 | GET THE CATALOGUE | Descarga de catálogo |
| 11 | "Honesty and sustainability" | Sección valores |
| 12 | CHOSEN WITH CARE | Sección curaduría |
| 13 | HISTORIAS / #REYTHEME | Blog o historias |

### Sitio Nuevo (construido)
| # | Sección | Estado | Notas |
|---|--------|--------|-------|
| 1 | Header con logo | ✅ Presente | Logo "E" + "Entramados" |
| 2 | Hero | ✅ Presente | Copy diferente: "Diseñamos espacios que cuentan tu historia" |
| 3 | SERVICIOS | ✅ Presente | Arquitectura, Interiorismo, Mobiliario Custom |
| 4 | PROYECTOS | ✅ Presente | Galería con 5 proyectos (usa hero.jpg como imagen 5) |
| 5 | NOSOTROS | ✅ Presente | Historia + valores |
| 6 | TESTIMONIOS | ✅ Presente | 3 testimonios con estrellas |
| 7 | CONTACTO | ✅ Presente | Formulario + info + redes |
| 8 | Footer | ✅ Presente | Navegación + servicios + contacto |
| 9 | WhatsApp flotante | ✅ Presente | Botón fijo esquina inferior derecha |
| 10 | Back to Top | ✅ Presente | Botón flotante esquina inferior izquierda |

---

## 2. DIFERENCIAS ENTRE ORIGINAL Y NUEVO

### Lo que tiene el nuevo sitio que NO estaba en la estructura del original
- **Testimonios de clientes** — Sección completa con 3 reviews y estrellas ⭐
- **Formulario de contacto completo** — Con campos de nombre, email, teléfono, servicio y mensaje
- **Stats en el hero** — "150+ Proyectos", "12 Años", "98% Satisfechos"
- **Sección About/Nosotros** — Historia del estudio con valores explícitos

### Lo que tenía el original que NO aparece en el nuevo
| Elemento original | Impacto |
|-------------------|---------|
| "SIGUENOS EN" (Instagram feed) | ⚠️ Solo hay link directo, no feed visual |
| "NUESTROS FAVORITOS" | ❌ No hay sección de favoritos |
| "CATEGORÍAS DESTACADAS" (ESCRITORIOS, ALMACENAMIENTO, etc.) | ❌ No hay categorías tipo e-commerce |
| Sección productos (COCINAS, SOFABEDS) con precios | ❌ No hay productos individuales con precio |
| "Quality into the fashion conscious home" | ❌ No hay quote/tagline de marca |
| "JOIN THE CLUB" (email signup) | ❌ No hay newsletter signup |
| "GET THE CATALOGUE" | ❌ No hay botón de descarga de catálogo |
| "CHOSEN WITH CARE" | ❌ No hay sección de curaduría |
| "HISTORIAS / #REYTHEME" | ❌ No hay blog ni historias |

### Estilo Visual — Comparación

| Aspecto | Original (estimado) | Nuevo Sitio | Match |
|----------|--------------------|----|--------|
| **Paleta de colores** | Neutral/oscuro (estilo UK brand) | Primary #6366F1, Secondary #1E1B4B, Accent #F97316, Cream #FAF8F5 | ⚠️ Diferente — el nuevo usa colores vibrantes (índigo/naranja) vs estilo minimal del original |
| **Tipografía headings** | Playfair Display (✅ mismo) | Playfair Display | ✅ |
| **Tipografía body** | Inter (✅ mismo) | Inter | ✅ |
| **Cards de productos** | Minimal, solo imagen + nombre | Overlay con gradiente oscuro + texto | ⚠️ Estilo diferente |
| **Hero** | Imagen con overlay oscuro + texto claro | Imagen con gradiente secondary/90 a secondary/60 | ✅ Similar |

---

## 3. PROBLEMAS ENCONTRADOS

### 🔴 Problemas Funcionales

1. **Botón menú móvil no funciona correctamente**
   - El HTML usa `id="menuToggle"` pero el CSS busca `.menu-toggle`
   - El JavaScript busca `.menu-toggle` y `.nav-mobile` — clase que NO existe en el HTML
   - El HTML tiene `.mobile-nav` pero el JS referencia `.nav-mobile`
   - **Fix:** Cambiar `class="mobile-nav hidden md:hidden"` → `class="nav-mobile hidden md:flex"` o viceversa

2. **Hero imagen 5 (proyecto-5) reutiliza hero.jpg**
   - El último proyecto usa `src="images/hero.jpg"` — es la misma imagen del hero
   - Debería ser una imagen distinta de proyecto

### ⚠️ Problemas de Diseño/Marketing

3. **No hay Instagram feed visual**
   - El original tenía "SIGUENOS EN" con feed visual
   - El nuevo solo tiene un link 📷 en la sección contacto
   - **Recomendación:** Agregar una sección "Síguenos en Instagram" con grid de fotos o embed

4. **No hay Newsletter / "JOIN THE CLUB"**
   - El original tenía email signup para comunidad
   - **Recomendación:** Agregar sección email signup cerca del footer

5. **No hay "GET THE CATALOGUE"**
   - Un CTA importante del original falta en el nuevo
   - **Recomendación:** Agregar botón o sección para descargar catálogo PDF

6. **Colores diferentes al original**
   - El sitio usa índigo (#6366F1) como color primario
   - El original probablemente usaba tonos más neutros/oscuros
   - Si el objetivo es replicar el estilo del original, revisar la paleta de colores

7. **No hay "Quality into the fashion conscious home" ni "CHOSEN WITH CARE"**
   - Son elementos de branding del original
   - Podrían adaptarse al español como tagline de marca

### 🟡 Observaciones Menores

8. **Placeholder images** — `about.jpg` muestra la misma imagen que `hero.jpg` potencialmente
9. **JSON-LD tiene teléfono placeholder** — `+593981234567` (verificar si es real)
10. **No hay página de gracias después del form** — El success state es inline (acceptable)

---

## 4. RECOMENDACIONES DE MEJORA

### Prioridad ALTA

1. **Arreglar el menú móvil** — Inconsistencia entre clases CSS/JS y HTML
2. **Agregar Newsletter signup** — Sección "Únete al Club" o similar con email input
3. **Agregar Instagram feed visual** — Grid de fotos de Instagram o embed oficial

### Prioridad MEDIA

4. **Botón "Descarga el Catálogo"** — CTA visible en hero o después de proyectos
5. **Corregir proyecto-5** — No reutilizar hero.jpg como imagen de proyecto
6. **Adaptar tagline de marca** — "Quality into the fashion conscious home" → versión español si aplica
7. **Revisar paleta de colores** — Comparar con el original si el estilo debe ser idéntico

### Prioridad BAJA

8. **Agregar "NUESTROS FAVORITOS"** — Si hay productos destacados, mostrarlos
9. **Agregar "HISTORIAS / #REYTHEME"** — Blog o carrusel de casos de éxito
10. **Animaciones scroll** — Las clases `animate-on-scroll` existen en CSS pero no se usan en HTML (solo hay `animate-fade-in` inline)

---

## 5. CHECKLIST DE CUMPLIMIENTO

| Requisito | Estado |
|-----------|--------|
| Header con logo | ✅ |
| Hero con propuesta de valor | ✅ |
| Sección servicios (Arquitectura, Interiorismo, Mobiliario) | ✅ |
| Galería de productos/proyectos | ✅ |
| Instagram link | ✅ (pero sin feed visual) |
| Sección valores o about | ✅ |
| Email signup o CTA de contacto | ✅ (formulario, pero falta newsletter) |
| Footer completo | ✅ |
| Menú de navegación funciona | ❌ (roto en móvil) |
| Botones con hover effects | ✅ |
| Formulario de contacto completo | ✅ |
| Botón WhatsApp visible | ✅ |
| Catálogo sin compra (no e-commerce) | ✅ |
| CTAs van a contacto/WhatsApp | ✅ |

---

## CONCLUSIÓN

El sitio nuevo tiene una **estructura sólida y moderna** con todas las secciones principales presentes. El mayor problema es el **menú móvil roto** por inconsistencia de clases CSS/JS vs HTML. El enfoque de catálogo sin e-commerce está **correctamente implementado** — todos los CTAs van a contacto.

Las principales gaps vs el original son la **ausencia de newsletter signup, Instagram feed visual y botón de catálogo**, además de **diferencias en la paleta de colores** que deberían evaluarse si el objetivo es replicar fielmente el estilo del sitio original.

**Score general:** 7.5/10 — Buen trabajo, necesita arreglos de funcionalidad y contenido.
