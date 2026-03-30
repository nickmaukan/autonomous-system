# 🔧 Proyecto 11: Compilar Aseprite desde Source

> Compilar Aseprite desde el código fuente en GitHub para obtenerlo gratis.

---

## 📋 Índice

1. [¿De qué trata este proyecto?](#de-qué-trata-este-proyecto)
2. [Tu sistema](#tu-sistema)
3. [Guía rápida](#guía-rápida)
4. [Estado actual](#estado-actual)
5. [Archivos del proyecto](#archivos-del-proyecto)

---

## ¿De qué trata este proyecto?

```
OBJETIVO: Obtener Aseprite gratis compilándolo desde source

BENEFICIOS:
├── $0 costo (vs $20 oficial)
├── Código más reciente
├── Aprendizaje de compilación
└── Personalización del código

CONSECUENCIAS:
├── ⏱️ Toma tiempo (1-4 horas)
├── ⚠️ Requiere actualizar Xcode
└── 🔧 Necesita troubleshooting
```

---

## Tu Sistema

| Componente | Estado | Detalle |
|------------|--------|---------|
| **macOS** | ✅ Compatible | 15.0 Sequoia |
| **Xcode** | ⚠️ Casi | 16.0 (necesita 16.3+) |
| **RAM** | ✅ OK | 17 GB |
| **CPU** | ✅ OK | 10 cores |

---

## Guía Rápida

### Paso 1: Verificar Dependencias

```bash
# Verificar qué tienes y qué falta
chmod +x scripts/check_dependencies.sh
./scripts/check_dependencies.sh
```

### Paso 2: Instalar lo que Falte

```bash
# Instalar herramientas
brew install cmake ninja git

# Descargar Skia (ir manualmente)
# github.com/aseprite/skia/releases
# Descomprimir en ~/deps/skia
```

### Paso 3: Clonar Código Fuente

```bash
git clone --recursive https://github.com/aseprite/aseprite.git ~/aseprite
```

### Paso 4: Compilar

```bash
chmod +x scripts/build_aseprite.sh
./scripts/build_aseprite.sh
```

### Paso 5: Usar

```bash
# Ejecutar
~/aseprite/build/bin/aseprite

# O crear alias
echo 'alias aseprite="$HOME/aseprite/build/bin/aseprite"' >> ~/.zshrc
source ~/.zshrc
aseprite
```

---

## Estado Actual

```
✅ 1. Verificar dependencias        → Completado
✅ 2. Instalar cmake + ninja        → Completado
✅ 3. Descargar Skia                → Completado  
✅ 4. Clonar repositorio            → Completado
✅ 5. Compilar Aseprite             → Completado (1.0-dev)
✅ 6. Ejecutar Aseprite            → Funcionando!

📦 CREAR VERSION PORTABLE:
   ./scripts/create_portable.sh
```

---

## Archivos del Proyecto

```
11-aseprite-compile/
├── README.md                    ← Este archivo (resumen)
├── PROYECTO.md                 ← Plan detallado completo
├── CONTEXT.md                  ← 📋 Commands exactos para rebuild futuro
│
├── 📂 research/
│   └── HARDWARE_SPECS.md       ← Especificaciones de tu Mac
│
├── 📂 scripts/
│   ├── check_dependencies.sh   ← Verifica qué tienes instalado
│   ├── build_aseprite.sh       ← Script para compilar
│   └── create_portable.sh      ← Crea ZIP portable
│
└── 📂 docs/
    └── PORTABLE_BUILD.md        ← Guía para compartir
```

## 📦 Descarga Portable

```
ZIP: ~/Aseprite-Portable-1.0.zip (~35MB)

Para compartir:
- AirDrop, USB, o nube
- El otro Mac: descomprimir → /Applications/
```

---

## ⚠️ Aviso Importante

La versión oficial de Aseprite cuesta $20 y es la recomendada si:
- No quieres complicaciones
- No tienes tiempo para compilar
- Necesitas soporte técnico

Este proyecto es para quienes:
- Quieren aprender cómo compilar
- Tienen tiempo disponible
- Prefieren gastar esfuerzo en lugar de dinero

---

## Recursos

| Recurso | Link |
|---------|------|
| **Aseprite GitHub** | github.com/aseprite/aseprite |
| **Skia Releases** | github.com/aseprite/skia/releases |
| **Aseprite Docs** | aseprite.org/docs |
| **Aseprite Discord** | discord.gg/Yb2CeX8 |

---

_Volver a [README principal](../README.md)_
