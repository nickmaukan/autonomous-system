#!/bin/bash
# build_aseprite.sh
# Script para compilar Aseprite desde source en macOS

set -e  # Salir si hay error

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

ASEPRITE_DIR="${HOME}/aseprite"
SKIA_DIR="${HOME}/deps/skia"
BUILD_DIR="${ASEPRITE_DIR}/build"

echo ""
echo -e "${BLUE}╔═══════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║${NC}         ${GREEN}🎨 Aseprite Build Script${NC}                              ${BLUE}║${NC}"
echo -e "${BLUE}╚═══════════════════════════════════════════════════════════╝${NC}"
echo ""

# Función para mostrar progreso
step() {
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}▶ $1${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
}

# Función para mostrar error
error() {
    echo ""
    echo -e "${RED}❌ ERROR: $1${NC}"
    echo ""
    exit 1
}

# Función para verificar
check() {
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}   ✅ $1${NC}"
    else
        echo -e "${RED}   ❌ $1${NC}"
    fi
}

# 1. Verificar Homebrew
step "Verificando Homebrew..."
if ! command -v brew &> /dev/null; then
    error "Homebrew no instalado. Instalar desde: brew.sh"
fi
echo "   ✅ Homebrew instalado"
brew --version | head -n1

# 2. Verificar herramientas
step "Verificando herramientas..."

for tool in cmake ninja git; do
    if command -v $tool &> /dev/null; then
        echo "   ✅ $tool: $($tool --version 2>/dev/null | head -n1)"
    else
        echo "   ❌ $tool no instalado"
        echo "   → brew install $tool"
        error "Instala $tool antes de continuar"
    fi
done

# 3. Verificar Xcode
step "Verificando Xcode..."
if [ -d "/Applications/Xcode.app" ]; then
    echo "   ✅ Xcode instalado"
    xcodebuild -version 2>/dev/null | grep "Xcode"
    
    # Verificar Command Line Tools
    if [ -d "/Library/Developer/CommandLineTools" ]; then
        echo "   ✅ Command Line Tools instaladas"
    else
        echo -e "   ${YELLOW}⚠️  Command Line Tools no encontradas, instalando...${NC}"
        xcode-select --install
    fi
else
    error "Xcode no instalado. Descarga desde developer.apple.com/xcode"
fi

# 4. Verificar Skia
step "Verificando Skia..."

if [ ! -d "$SKIA_DIR" ]; then
    error "Skia no encontrado en $SKIA_DIR
    
   Pasos:
    1. Ve a: https://github.com/aseprite/skia/releases
    2. Descarga: aseprite-skia-macos-*.zip
    3. Descomprime en ~/deps/skia
    "
fi

echo "   ✅ Skia encontrado: $SKIA_DIR"

# Verificar arquitectura
if [ -f "$SKIA_DIR/out/Release-arm64/libskia.a" ]; then
    echo "   ✅ libskia.a (ARM64) encontrado"
    SKIA_LIBRARY="$SKIA_DIR/out/Release-arm64/libskia.a"
    SKIA_LIBRARY_DIR="$SKIA_DIR/out/Release-arm64"
elif [ -f "$SKIA_DIR/out/Release-x64/libskia.a" ]; then
    echo -e "   ${YELLOW}⚠️  Usando versión x64 (menos óptimo para tu Mac)${NC}"
    SKIA_LIBRARY="$SKIA_DIR/out/Release-x64/libskia.a"
    SKIA_LIBRARY_DIR="$SKIA_DIR/out/Release-x64"
else
    error "No se encontró libskia.a en $SKIA_DIR"
fi

# 5. Verificar código fuente
step "Verificando código fuente de Aseprite..."

if [ ! -d "$ASEPRITE_DIR" ]; then
    echo "   ⚠️  Aseprite no encontrado en $ASEPRITE_DIR"
    echo "   ¿Quieres clonar el repositorio? (y/n)"
    read -r response
    if [[ "$response" =~ ^[Yy]$ ]]; then
        echo "   Clonando repositorio..."
        git clone --recursive https://github.com/aseprite/aseprite.git "$ASEPRITE_DIR"
    else
        error "Código fuente requerido"
    fi
fi

echo "   ✅ Aseprite encontrado: $ASEPRITE_DIR"

# Verificar submodules
if [ -d "$ASEPRITE_DIR/.git" ]; then
    cd "$ASEPRITE_DIR"
    echo "   Verificando submodules..."
    git submodule status --quiet 2>/dev/null | head -n3
fi

# 6. Crear directorio de build
step "Preparando directorio de build..."

if [ -d "$BUILD_DIR" ]; then
    echo "   ⚠️  Build directory ya existe"
    echo "   ¿Limpiar y recreate? (y/n)"
    read -r response
    if [[ "$response" =~ ^[Yy]$ ]]; then
        echo "   Limpiando..."
        rm -rf "$BUILD_DIR"
        mkdir -p "$BUILD_DIR"
        echo "   ✅ Directory recreado"
    fi
else
    mkdir -p "$BUILD_DIR"
    echo "   ✅ Directory creado"
fi

cd "$BUILD_DIR"

# 7. Configurar CMake
step "Configurando CMake..."

# Detectar macOS version
MACOS_VERSION=$(sw_vers -productVersion)

echo "   macOS: $MACOS_VERSION"
echo "   Arquitectura: arm64 (Apple Silicon)"
echo "   Build type: RelWithDebInfo"
echo ""
echo "   Ejecutando cmake..."
echo ""

cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_OSX_ARCHITECTURES=arm64 \
    -DCMAKE_OSX_DEPLOYMENT_TARGET=15.0 \
    -DCMAKE_OSX_SYSROOT="$(xcrun --show-sdk-path)" \
    -DLAF_BACKEND=skia \
    -DSKIA_DIR="$SKIA_DIR" \
    -DSKIA_LIBRARY_DIR="$SKIA_LIBRARY_DIR" \
    -DSKIA_LIBRARY="$SKIA_LIBRARY" \
    -G Ninja \
    "$ASEPRITE_DIR" 2>&1

check "CMake configuration"

# 8. Compilar
step "Compilando Aseprite..."

echo ""
echo -e "${YELLOW}⚠️  IMPORTANTE: La compilación puede tomar 1-4 horas${NC}"
echo -e "${YELLOW}   dependiendo de tu hardware y otras apps abiertas.${NC}"
echo ""
echo "   Presiona Ctrl+C para cancelar"
echo ""

# Contador de tiempo
start_time=$(date +%s)

# Compilar con ninja (usa todos los cores por defecto)
ninja aseprite 2>&1

compile_status=$?
end_time=$(date +%s)
elapsed=$(( (end_time - start_time) / 60 ))

echo ""
if [ $compile_status -eq 0 ]; then
    step "✅ ¡Compilación exitosa!"
    
    echo ""
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo "   📊 Tiempo total: $elapsed minutos"
    echo ""
    echo "   📁 Executable: $BUILD_DIR/bin/aseprite"
    echo ""
    echo "   Para ejecutar:"
    echo "   $ $BUILD_DIR/bin/aseprite"
    echo ""
    echo "   Para crear alias permanente:"
    echo "   $ echo 'alias aseprite=\"$BUILD_DIR/bin/aseprite\"' >> ~/.zshrc"
    echo "   $ source ~/.zshrc"
    echo "   $ aseprite"
    echo ""
    
    # Hacer el executable accesible
    chmod +x "$BUILD_DIR/bin/aseprite" 2>/dev/null || true
    
else
    step "❌ La compilación falló"
    echo ""
    echo "   Revisa los errores arriba."
    echo "   Busca soluciones en: github.com/aseprite/aseprite/issues"
    echo ""
fi
