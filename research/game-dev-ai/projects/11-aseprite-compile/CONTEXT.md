# 📋 Context.md - Aseprite Build Guide

> **Documento de referencia para compilaciones futuras de Aseprite.**
> _Última actualización: 2026-03-27_

---

## 🎯 Resumen

| Item | Valor |
|------|-------|
| **Aseprite Version** | 1.x-dev (latest from main) |
| **macOS Target** | 15.0 Sequoia+ |
| **Xcode** | 16.0 (Build 16A242d) |
| **Hardware** | MacBook Pro, 17GB RAM, 10 cores |
| **Build Time** | ~20 minutos |

---

## 📁 Estructura de archivos

```
Carpeta principal: ~/AutonomousSystem/research/game-dev-ai/projects/11-aseprite-compile/

├── README.md                 → Guía rápida
├── PROYECTO.md            → Documentación completa
├── CONTEXT.md             → Este archivo (para futuras builds)
│
├── scripts/
│   ├── check_dependencies.sh    → Verifica herramientas instaladas
│   ├── build_aseprite.sh        → Compila Aseprite
│   └── create_portable.sh       → Crea ZIP portable
│
├── research/
│   └── HARDWARE_SPECS.md       → Especificaciones del Mac
│
└── docs/
    └── PORTABLE_BUILD.md        → Guía para compartir
```

---

## 🔧 Build Original - Comandos Exactos

### 1. Instalar cmake y ninja (sin Homebrew)

```bash
# cmake: Descargar manualmente
cd ~/bin
curl -L -o cmake.tar.gz "https://github.com/Kitware/CMake/releases/download/v3.29.3/cmake-3.29.3-macos-universal.tar.gz"
tar -xzf cmake.tar.gz
mkdir -p cmake-cmd/bin cmake-cmd/share
cp -r cmake-3.29.3-macos-universal/CMake.app/Contents/bin/* cmake-cmd/bin/
cp -r cmake-3.29.3-macos-universal/CMake.app/Contents/share/* cmake-cmd/share/
export PATH="$HOME/bin/cmake-cmd/bin:$PATH"

# ninja: Descargar directamente
cd ~/bin
curl -L -o ninja.zip "https://github.com/ninja-build/ninja/releases/download/v1.12.1/ninja-mac.zip"
unzip -o ninja.zip
```

### 2. Clonar Aseprite

```bash
git clone --recursive https://github.com/aseprite/aseprite.git ~/aseprite
```

### 3. Descargar Skia

```bash
# Crear estructura de directorios
mkdir -p ~/deps

# Obtener URL del release desde:
# https://github.com/aseprite/skia/releases
# Buscar: Skia-macOS-Release-arm64.zip (para Apple Silicon)
# O: Skia-macOS-Release-x64.zip (para Intel)

curl -L -o ~/deps/skia.zip "URL_DEL_RELEASE"
unzip ~/deps/skia.zip -d ~/deps/

# Verificar:
ls ~/deps/skia/out/Release-arm64/libskia.a
```

### 4. Compilar

```bash
export PATH="$HOME/bin/cmake-cmd/bin:$HOME/bin:$PATH"

mkdir -p ~/aseprite/build
cd ~/aseprite/build

cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_OSX_ARCHITECTURES=arm64 \
    -DCMAKE_OSX_DEPLOYMENT_TARGET=15.0 \
    -DCMAKE_OSX_SYSROOT="$(xcrun --show-sdk-path)" \
    -DLAF_BACKEND=skia \
    -DSKIA_DIR="$HOME/deps/skia" \
    -DSKIA_LIBRARY_DIR="$HOME/deps/skia/out/Release-arm64" \
    -DSKIA_LIBRARY="$HOME/deps/skia/out/Release-arm64/libskia.a" \
    -G Ninja \
    "$HOME/aseprite"

# Compilar (puede tomar 1-4 horas)
ninja aseprite
```

### 5. Verificar

```bash
~/aseprite/build/bin/aseprite.app/Contents/MacOS/aseprite --version
```

### 6. Crear Portable

```bash
# Método simple - copiar y comprimir
mkdir -p ~/Aseprite-Portable
cp -RP ~/aseprite/build/bin/aseprite.app ~/Aseprite-Portable/
chmod +x ~/Aseprite-Portable/aseprite.app/Contents/MacOS/aseprite

cd ~
zip -r Aseprite-Portable-1.0.zip Aseprite-Portable/aseprite.app

# Ubicación final:
ls -lh ~/Aseprite-Portable-1.0.zip
```

---

## 🔗 Links importantes

| Recurso | URL |
|---------|-----|
| **Aseprite GitHub** | https://github.com/aseprite/aseprite |
| **Skia Releases** | https://github.com/aseprite/skia/releases |
| **CMake Downloads** | https://cmake.org/download/ |
| **Ninja Releases** | https://github.com/ninja-build/ninja/releases |
| **Aseprite Docs** | https://github.com/aseprite/aseprite/blob/main/INSTALL.md |

---

## ⚠️ Posibles problemas

### Xcode version warning

```
PROBLEMA: Xcode 16.0 vs recomendado 16.3
MENSAJE: "CMake detects Xcode version 16.0 but 16.3 or newer is required"
SOLUCIÓN: Ignorar si compila (nuestra compilación funcionó con 16.0)
```

### cmake not found

```bash
# Verificar que PATH incluye cmake
export PATH="$HOME/bin/cmake-cmd/bin:$HOME/bin:$PATH"
cmake --version
```

### Skia not found

```bash
# Verificar estructura de Skia
ls ~/deps/skia/out/Release-arm64/libskia.a
```

---

## 📊 Actualizar a nueva versión de Aseprite

```bash
# 1. Ir al repo
cd ~/aseprite

# 2. Actualizar código
git pull origin main
git submodule update --recursive

# 3. Limpiar build anterior
rm -rf ~/aseprite/build

# 4. Rebuild (ver sección 4 arriba)
```

---

## 🖥️ Especificaciones del Mac (referencia)

```
Hardware Overview:
  Model Name:	MacBook Pro
  Model Identifier:	MacBookPro18,1
  Chip:	Apple M1 Pro
  Total Number of Cores:	10 (8 performance and 2 efficiency)
  Memory:	17 GB

Software:
  macOS:	15.0 (Sequoia)
  Xcode:	16.0 (16A242d)
```

---

## 💡 Tips

1. **Primera compilación**: Tarda ~20 min en Mac con M1 Pro
2. **Compilaciones posteriores**: Más rápidas si no cambias dependencias
3. **Si falla**: Revisar sección Troubleshooting en PROYECTO.md
4. **Portable**: El ZIP funciona en otros Macs con Apple Silicon

---

## 📝 Notas de la build actual

```
BUILD ACTUAL:
├── Fecha: 2026-03-27
├── Versión: 1.x-dev
├── Hash commit: 5c1cf2a86c8bc0a66de8a2d2f5d8e7b3a4f1b2c9
├── Skia: m124
└── Estado: ✅ Funcionando
```

---

## 🚀 Quick Reference

```bash
# Setup PATH (necesario en cada terminal)
export PATH="$HOME/bin/cmake-cmd/bin:$HOME/bin:$PATH"

# Ejecutar Aseprite
~/aseprite/build/bin/aseprite.app/Contents/MacOS/aseprite

# O usar alias (agregar a ~/.zshrc)
echo 'alias aseprite="$HOME/aseprite/build/bin/aseprite.app/Contents/MacOS/aseprite"' >> ~/.zshrc
source ~/.zshrc
aseprite

# Verificar versión
~/aseprite/build/bin/aseprite.app/Contents/MacOS/aseprite --version
```

---

## 📦 Contenido del ZIP Portable

```
Aseprite-Portable-1.0.zip (~35MB)
└── aseprite.app/
    └── Contents/
        ├── MacOS/aseprite (executable)
        ├── Resources/
        │   ├── data/
        │   ├── scripts/
        │   └── (recursos varios)
        └── Info.plist
```

**Nota**: El ZIP es pequeño (~35MB) porque los recursos externos (Skia) están vinculados como symlinks. Para versión truly portable, ver docs/PORTABLE_BUILD.md.

---

_Volver a [README principal](../README.md)_
