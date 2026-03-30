#!/bin/bash
# check_dependencies.sh
# Verifica si tienes todas las dependencias para compilar Aseprite

echo "🔍 Verificando dependencias para compilar Aseprite..."
echo ""
echo "Tu sistema:"
echo "   macOS: 15.0 Sequoia ✅"
echo "   Xcode:  16.0 (⚠️ se recomienda 16.3+)"
echo ""

# Función para verificar
check() {
    local cmd=$1
    local brew_pkg=${2:-$1}
    
    if command -v $cmd &> /dev/null; then
        version=$($cmd --version 2>/dev/null | head -n1)
        echo "✅ $cmd: $version"
        return 0
    else
        echo "❌ $cmd: NO INSTALADO"
        echo "   → brew install $brew_pkg"
        return 1
    fi
}

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "HERRAMIENTAS DE DESARROLLO"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Verificar herramientas
check cmake cmake
check ninja ninja
check git git

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "XCODE"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [ -d "/Applications/Xcode.app" ]; then
    echo "✅ Xcode instalado"
    xcodebuild -version 2>/dev/null || echo "   No se pudo obtener versión"
    
    # Verificar versión
    xcode_version=$(xcodebuild -version 2>/dev/null | grep "Xcode" | awk '{print $2}')
    if [[ $(echo "$xcode_version" | cut -d'.' -f1) -lt 16 ]]; then
        echo "⚠️  AVISO: Xcode $xcode_version detectado"
        echo "   Se recomienda Xcode 16.3+ para compilar Aseprite"
        echo "   Actualiza desde: App Store → Xcode → Update"
    else
        echo "✅ Xcode $xcode_version cumple requisitos"
    fi
else
    echo "❌ Xcode: NO INSTALADO"
    echo "   → Descargar desde: developer.apple.com/xcode"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "SKIA (Librería gráfica)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [ -d "$HOME/deps/skia" ]; then
    echo "✅ Skia: Descargado en ~/deps/skia"
    
    # Verificar que existe libskia.a
    if [ -f "$HOME/deps/skia/out/Release-arm64/libskia.a" ]; then
        echo "   ✅ libskia.a encontrado"
    elif [ -f "$HOME/deps/skia/out/Release-x64/libskia.a" ]; then
        echo "   ⚠️  AVISO: Encontrado Release-x64, pero tu Mac usa ARM64"
        echo "   → Descarga la versión ARM64 para mejor rendimiento"
    else
        echo "   ⚠️  AVISO: libskia.a no encontrado"
        echo "   → Verifica que descargaste el ZIP correcto"
    fi
else
    echo "❌ Skia: NO DESCARGADO"
    echo "   → Descargar desde: github.com/aseprite/skia/releases"
    echo "   → Buscar: aseprite-skia-macos-*.zip"
    echo "   → Descomprimir en: ~/deps/skia"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "CÓDIGO FUENTE DE ASEPRITE"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [ -d "$HOME/aseprite/.git" ]; then
    echo "✅ Aseprite: Código fuente en ~/aseprite"
    
    # Mostrar última fecha de commit
    cd "$HOME/aseprite" 2>/dev/null && git log -1 --format="%ai" 2>/dev/null && echo "   Última actualización"
else
    echo "⚠️  Aseprite: Código fuente NO descargado"
    echo "   → git clone --recursive https://github.com/aseprite/aseprite.git ~/aseprite"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "ESPACIO EN DISCO"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Verificar espacio libre
free_space=$(df -h "$HOME" | tail -1 | awk '{print $4}')
echo "   Espacio libre: $free_space"
if [ "$(df "$HOME" | tail -1 | awk '{print $4}' | tr -d 'GiMi')" -lt 10 ]; then
    echo "⚠️  AVISO: Poco espacio. Se recomienda 10GB+ para compilación"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "RESUMEN"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Contar problemas
problems=0

if ! command -v cmake &> /dev/null; then ((problems++)); fi
if ! command -v ninja &> /dev/null; then ((problems++)); fi
if ! command -v git &> /dev/null; then ((problems++)); fi
if [ ! -d "$HOME/deps/skia" ]; then ((problems++)); fi

if [ $problems -eq 0 ]; then
    echo "🎉 ¡Todo listo para compilar!"
    echo ""
    echo "   Próximos pasos:"
    echo "   1. Si aún no tienes el código: git clone --recursive https://github.com/aseprite/aseprite.git ~/aseprite"
    echo "   2. Ejecutar: ./build_aseprite.sh"
    echo "   3. O compilar manualmente:"
    echo "      cd ~/aseprite && mkdir build && cd build"
    echo "      cmake [opciones...] ..."
    echo "      ninja aseprite"
else
    echo "⚠️  Hay $problems problema(s) por resolver antes de compilar"
    echo ""
    echo "   Resuelve los ❌ marcados arriba antes de continuar"
fi

echo ""
