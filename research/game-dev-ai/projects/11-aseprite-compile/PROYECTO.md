# 🔧 Proyecto 11: Compilar Aseprite desde Source

## Resumen Ejecutivo

**Objetivo:** Compilar Aseprite desde el código fuente en GitHub para obtener una versión gratuita y de código abierto de esta herramienta de pixel art.

**Estado actual:** Investigando viabilidad

**Tu sistema:**
- macOS 15.0 Sequoia ✅
- Xcode 16.0 (⚠️ necesita 16.3+)
- RAM 17GB ✅
- 10 cores CPU ✅

---

## 1. ¿Qué es Aseprite?

```
┌─────────────────────────────────────────────────────────────────┐
│                         ASEPRITE                                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  DESCRIPCIÓN:                                                    │
│  Editor de sprites animados y pixel art profesional              │
│  Alternativa a Photoshop especializada en pixel art              │
│                                                                  │
│  CARACTERÍSTICAS:                                               │
│  ├── Animación con timeline                                     │
│  ├── Capas y frames                                            │
│  ├── Export a sprite sheets                                     │
│  ├── Paletas de colores (256 colores)                           │
│  ├── Onion skinning                                             │
│  ├── Pixel perfect mode                                         │
│  ├── Scripts Lua                                                │
│  └── CLI para automatización                                    │
│                                                                  │
│  PRECIO OFICIAL:                                                │
│  ├── $20 USD (licencia perpetua)                                │
│  ├── Source code disponible en GitHub                            │
│  └── Para compilar necesitas cumplir requisitos técnicos          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. Requisitos para Compilar

### Requisitos Oficiales (macOS)

| Requisito | Versión Mínima | Tu Sistema | Estado |
|-----------|----------------|------------|--------|
| **macOS** | 15.2 Sequoia | 15.0 | ⚠️ Casi |
| **Xcode** | 16.3 | 16.0 | ❌ No cumple |
| **CMake** | Latest | ? | ⏳ Verificar |
| **Ninja** | Latest | ? | ⏳ Verificar |
| **Skia** | Pre-built | Requerido | ⏳ Descargar |

### Dependencias adicionales

```
DEPENDENCIAS NECESARIAS:

1. CMake
   └→ brew install cmake

2. Ninja
   └→ brew install ninja

3. Skia Library (PRE-COMPILED)
   └→ Descargar desde GitHub releases
   └→ github.com/aseprite/skia/releases

4. Xcode Command Line Tools
   └→ Incluidas con Xcode 16.0 ✅
```

---

## 3. Plan de Implementación

### Fase 1: Preparación (Día 1)

```
TAREAS DE PREPARACIÓN:

□ 1.1 Verificar/Instalar CMake
   └→ cmake --version
   └→ Si no está: brew install cmake

□ 1.2 Verificar/Instalar Ninja
   └→ ninja --version
   └→ Si no está: brew install ninja

□ 1.3 Descargar Skia pre-built
   └→ Ir a: github.com/aseprite/skia/releases
   └→ Descargar: aseprite-skia-macos-latest.zip
   └→ Descomprimir en: ~/deps/skia

□ 1.4 Actualizar Xcode (RECOMENDADO)
   └→ App Store → Xcode → Update
   └→ O descargar 16.3+ desde developer.apple.com
   └→ ⚠️ ~12GB, puede tomar tiempo

□ 1.5 Crear directorio de build
   └→ mkdir -p ~/aseprite/build
```

### Fase 2: Obtener Código Fuente (Día 1)

```
TAREAS:

□ 2.1 Clonar repositorio
   cd ~
   git clone --recursive https://github.com/aseprite/aseprite.git

□ 2.2 (Opcional) Descargar source ZIP
   └→ Ir a github.com/aseprite/aseprite/releases
   └→ Descargar Aseprite-v1.x-Source.zip
   └→ Descomprimir

□ 2.3 Verificar submodules
   └→ cd aseprite
   └→ git submodule update --init --recursive
```

### Fase 3: Compilación (Día 2-3)

```
TAREAS:

□ 3.1 Configurar CMake
   cd ~/aseprite
   mkdir build && cd build
   
   cmake \
     -DCMAKE_BUILD_TYPE=RelWithDebInfo \
     -DCMAKE_OSX_ARCHITECTURES=arm64 \
     -DCMAKE_OSX_DEPLOYMENT_TARGET=15.0 \
     -DLAF_BACKEND=skia \
     -DSKIA_DIR=$HOME/deps/skia \
     -DSKIA_LIBRARY_DIR=$HOME/deps/skia/out/Release-arm64 \
     -DSKIA_LIBRARY=$HOME/deps/skia/out/Release-arm64/libskia.a \
     -G Ninja \
     ..

□ 3.2 Compilar
   ninja aseprite

   ⚠️ Esto puede tomar 1-4 HORAS dependiendo del hardware

□ 3.3 (Si hay errores)
   └→ Revisar sección de troubleshooting
   └→ google.com → buscar error específico
```

### Fase 4: Verificación y Uso (Día 3)

```
TAREAS:

□ 4.1 Verificar executable
   ls -la ~/aseprite/build/bin/

□ 4.2 Crear alias o acceso directo
   # Agregar a ~/.zshrc:
   alias aseprite='~/aseprite/build/bin/aseprite'

□ 4.3 Probar ejecución
   ~/aseprite/build/bin/aseprite

□ 4.4 (Opcional) Crear App bundle
   └→ Para tener icono en Launchpad
```

---

## 4. Scripts de Automatización

### Script 1: Verificar Dependencias

```bash
#!/bin/bash
# check_dependencies.sh
# Verifica si tienes todas las dependencias instaladas

echo "🔍 Verificando dependencias para compilar Aseprite..."
echo ""

# Función para verificar
check() {
    if command -v $1 &> /dev/null; then
        version=$($1 --version 2>/dev/null | head -n1)
        echo "✅ $1: $version"
    else
        echo "❌ $1: NO INSTALADO"
        echo "   Instalar con: brew install $2"
    fi
}

# Verificar herramientas
check cmake cmake
check ninja ninja
check git git

# Verificar Xcode
if [ -d "/Applications/Xcode.app" ]; then
    xcodebuild -version
else
    echo "❌ Xcode: NO INSTALADO"
fi

# Verificar Skia
if [ -d "$HOME/deps/skia" ]; then
    echo "✅ Skia: Descargado en ~/deps/skia"
else
    echo "❌ Skia: NO DESCARGADO"
    echo "   Descargar desde: github.com/aseprite/skia/releases"
fi

echo ""
echo "📋 Resumen:"
echo "   - Si hay ❌, resuelve antes de continuar"
echo "   - Si hay ⚠️, puedes continuar pero puede fallar"
```

### Script 2: Compilar Aseprite

```bash
#!/bin/bash
# build_aseprite.sh
# Script para compilar Aseprite

set -e  # Salir si hay error

ASEPRITE_DIR="$HOME/aseprite"
SKIA_DIR="$HOME/deps/skia"
BUILD_DIR="$ASEPRITE_DIR/build"

echo "🎨 Aseprite Build Script"
echo "========================"
echo ""

# 1. Verificar que existe el source
if [ ! -d "$ASEPRITE_DIR" ]; then
    echo "❌ Error: No se encontró el código fuente en $ASEPRITE_DIR"
    echo "   Clonar con: git clone --recursive https://github.com/aseprite/aseprite.git"
    exit 1
fi

# 2. Verificar Skia
if [ ! -d "$SKIA_DIR" ]; then
    echo "❌ Error: Skia no encontrado en $SKIA_DIR"
    echo "   1. Descargar: github.com/aseprite/skia/releases"
    echo "   2. Descomprimir en ~/deps/skia"
    exit 1
fi

# 3. Crear build dir
echo "📁 Creando directorio de build..."
mkdir -p "$BUILD_DIR"
cd "$BUILD_DIR"

# 4. Configurar CMake
echo "⚙️  Configurando con CMake..."
cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_OSX_ARCHITECTURES=arm64 \
    -DCMAKE_OSX_DEPLOYMENT_TARGET=15.0 \
    -DLAF_BACKEND=skia \
    -DSKIA_DIR="$SKIA_DIR" \
    -DSKIA_LIBRARY_DIR="$SKIA_DIR/out/Release-arm64" \
    -DSKIA_LIBRARY="$SKIA_DIR/out/Release-arm64/libskia.a" \
    -G Ninja \
    "$ASEPRITE_DIR"

# 5. Compilar
echo "🔨 Compilando (esto puede tomar 1-4 horas)..."
echo "   Presiona Ctrl+C para cancelar"
echo ""

ninja aseprite

# 6. Verificar
if [ -f "$BUILD_DIR/bin/aseprite" ]; then
    echo ""
    echo "✅ Compilación exitosa!"
    echo "   Executable: $BUILD_DIR/bin/aseprite"
else
    echo ""
    echo "❌ Error: La compilación falló"
    exit 1
fi
```

### Script 3: Setup Completo

```bash
#!/bin/bash
# setup_aseprite.sh
# Script para setup inicial completo

set -e

echo "🎨 Aseprite Setup Completo"
echo "========================="
echo ""

# 1. Verificar Homebrew
if ! command -v brew &> /dev/null; then
    echo "❌ Homebrew no instalado"
    echo "   Instalar desde: brew.sh"
    exit 1
fi
echo "✅ Homebrew instalado"

# 2. Instalar dependencias
echo ""
echo "📦 Instalando dependencias..."
brew install cmake ninja git

# 3. Crear directorios
echo ""
echo "📁 Creando estructura de directorios..."
mkdir -p ~/aseprite
mkdir -p ~/deps

# 4. Verificar Skia
if [ ! -d "$HOME/deps/skia" ]; then
    echo ""
    echo "⚠️  IMPORTANTE: Skia no encontrado"
    echo ""
    echo "   1. Ve a: https://github.com/aseprite/skia/releases"
    echo "   2. Descarga: aseprite-skia-macos-latest.zip"
    echo "   3. Descomprime en ~/deps/skia"
    echo "   4. Presiona Enter cuando esté listo"
    read -r
fi

# 5. Clonar repositorio
echo ""
if [ ! -d "$HOME/aseprite/.git" ]; then
    echo "📥 Clonando código fuente..."
    git clone --recursive https://github.com/aseprite/aseprite.git ~/aseprite
else
    echo "✅ Código fuente ya existe"
fi

echo ""
echo "✅ Setup inicial completo!"
echo ""
echo "   Próximos pasos:"
echo "   1. Descargar Skia si no lo hiciste"
echo "   2. Ejecutar: ./build_aseprite.sh"
```

---

## 5. Troubleshooting

### Error: Xcode version too old

```
PROBLEMA: CMake detects Xcode version 16.0 but 16.3 or newer is required

SOLUCIÓN:
1. Actualizar Xcode desde App Store
   └→ App Store → Updates → Xcode

2. O descargar beta desde:
   └→ developer.apple.com/download

3. Verificar:
   └→ xcodebuild -version
```

### Error: Skia not found

```
PROBLEMA: Could not find Skia library

SOLUCIÓN:
1. Descargar desde:
   └→ github.com/aseprite/skia/releases

2. Descomprimir:
   └→ unzip aseprite-skia-macos-*.zip -d ~/deps/

3. Verificar estructura:
   └→ ls ~/deps/skia/
   └→ Debería tener: out/Release-arm64/libskia.a
```

### Error: CMake cannot find Ninja

```
PROBLEMA: Ninja not found

SOLUCIÓN:
1. Instalar con Homebrew:
   └→ brew install ninja

2. Verificar:
   └→ ninja --version
```

### Error: Out of memory

```
PROBLEMA: Compilation killed due to memory

SOLUCIÓN:
1. Reducir jobs paralelos:
   └→ ninja -j4 aseprite

2. No ejecutar otras apps pesadas durante compilación
```

### Error: clang: error

```
PROBLEMA: Various clang errors during compilation

SOLUCIÓN:
1. Limpiar build:
   └→ cd ~/aseprite/build
   └→ ninja -t clean
   └→ rm -rf *

2. Reiniciar compilación:
   └→ ./build_aseprite.sh
```

---

## 6. Guía Paso a Paso

### Paso 1: Prepárate (~30 min)

```bash
# 1. Abre Terminal

# 2. Instalar Homebrew (si no lo tienes)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 3. Instalar herramientas
brew install cmake ninja git

# 4. Verificar instalaciones
cmake --version
ninja --version
```

### Paso 2: Descargar Skia (~10 min)

```bash
# 1. Ve a:
#    https://github.com/aseprite/skia/releases

# 2. Busca "aseprite-skia-macos" latest release

# 3. Descarga el .zip (~500MB)

# 4. Descomprime en Finder o:
unzip ~/Downloads/aseprite-skia-macos-*.zip -d ~/deps/

# 5. Verifica:
ls ~/deps/skia/
# Deberías ver: out/ CMakeLists.txt etc.
```

### Paso 3: Clonar Aseprite (~5 min)

```bash
git clone --recursive https://github.com/aseprite/aseprite.git ~/aseprite

# Esto puede tomar 5-10 minutos (es código grande)
```

### Paso 4: Compilar (~1-4 horas)

```bash
# Opción A: Usar script automático
chmod +x ~/AutonomousSystem/research/game-dev-ai/projects/11-aseprite-compile/scripts/build_aseprite.sh
~/AutonomousSystem/research/game-dev-ai/projects/11-aseprite-compile/scripts/build_aseprite.sh

# Opción B: Manual
cd ~/aseprite
mkdir build && cd build

cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_OSX_ARCHITECTURES=arm64 \
    -DCMAKE_OSX_DEPLOYMENT_TARGET=15.0 \
    -DLAF_BACKEND=skia \
    -DSKIA_DIR=$HOME/deps/skia \
    -DSKIA_LIBRARY_DIR=$HOME/deps/skia/out/Release-arm64 \
    -DSKIA_LIBRARY=$HOME/deps/skia/out/Release-arm64/libskia.a \
    -G Ninja \
    ..

ninja aseprite
```

### Paso 5: Usar Aseprite

```bash
# Ejecutar
~/aseprite/build/bin/aseprite

# Crear alias permanente (agregar a ~/.zshrc):
echo 'alias aseprite="$HOME/aseprite/build/bin/aseprite"' >> ~/.zshrc
source ~/.zshrc

# Ahora puedes escribir:
aseprite
```

---

## 7. Tiempo Estimado

| Fase | Tarea | Tiempo |
|------|--------|--------|
| 1 | Prep (Homebrew, cmake, ninja) | 20-30 min |
| 2 | Descargar Skia (~500MB) | 10-15 min |
| 3 | Clonar Aseprite | 5-10 min |
| 4 | Primera compilación | 1-4 horas |
| **Total** | | **1.5 - 5 horas** |

---

## 8. Alternativa: Si Falla la Compilación

Si la compilación falla o toma demasiado tiempo:

### Opción A: Usar Release Pre-compiled (LEGAL)

```
DISPONIBLE EN:
├── Steam ($20)
├── itch.io app ($20)
└── aseprite.org ($20)

NOTA: La versión compilada oficialmente cuesta $20.
No es gratuita, pero es la opción oficial y supported.
```

### Opción B: Alternativas Gratuitas

```
ALTERNATIVAS A ASEPRITE:

1. LUNA Sprite Editor
   └→ spritefusion.itch.io
   └→ Gratis, similar a Aseprite
   └→ Para macOS

2. CREScent Pixel Art
   └→ pixelart.software
   └→ Online, no install

3. GIMP
   └→ gimp.org
   └→ Gratis, más complejo

4. Lospec Palette Editor
   └→ lospec.com/palette-editor
   └→ Online, para paletas

5. LibreSprite (Fork gratis de Aseprite)
   └→ github.com/LibreSprite/LibreSprite
   └→ Requiere compilación similar
```

### Opción C: Esperar actualización de Xcode

```
SI NO QUIERES ACTUALIZAR XCODE:

1. Espera a que Xcode 16.3+ esté en App Store (automático)
2. Cuando se actualice, vuelve a intentar

MACHA VENTAJAS:
- No gastas $20
- Aprendes sobre compilación
- Tienes la última versión del código
```

---

## 9. Checklist de Verificación

Antes de empezar la compilación, marca cada uno:

```
PREPARACIÓN:
☐ Homebrew instalado
☐ cmake instalado (cmake --version)
☐ ninja instalado (ninja --version)
☐ git instalado (git --version)
☐ ~2GB de espacio libre en disco
☐ Skia descargado y descomprimido en ~/deps/skia
☐ Código fuente en ~/aseprite

OPCIONAL:
☐ Xcode actualizado a 16.3+ (recomendado)
☐ Tiempo reservado: 2-4 horas sin interrupciones
```

---

## 10. Recursos

- **Aseprite GitHub:** github.com/aseprite/aseprite
- **Aseprite Docs:** aseprite.org/docs
- **Aseprite Discord:** discord.gg/Yb2CeX8
- **Skia Releases:** github.com/aseprite/skia/releases
- **Homebrew:** brew.sh

---

_Volver a [README principal](../README.md)_
