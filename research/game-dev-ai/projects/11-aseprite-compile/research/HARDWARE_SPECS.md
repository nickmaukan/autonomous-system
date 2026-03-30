# MacBook Pro - Especificaciones del Sistema

_Investigado: 2026-03-27_

---

## Sistema Operativo

| Campo | Valor |
|-------|-------|
| **macOS** | 15.0 (Sequoia) |
| **Build** | 24A335 |

## Xcode

| Campo | Valor |
|-------|-------|
| **Xcode Version** | 16.0 |
| **Build** | 16A242d |
| **Ubicación** | /Applications/Xcode.app |
| **Command Line Tools** | Instaladas |

## Hardware

| Campo | Valor |
|-------|-------|
| **RAM** | 17 GB (17179869184 bytes) |
| **CPU Cores** | 10 |
| **Chip** | Apple Silicon (probablemente M-series) |

---

## Verificación de Requisitos para Aseprite

### Requisitos Oficiales (macOS)

```
REQUISITO: macOS 15.2 Sequoia + Xcode 16.3 + macOS 15.4 SDK
TU SISTEMA: macOS 15.0 + Xcode 16.0

VEREDICTO: ⚠️ CASI COMPATIBLE
- macOS: 15.0 vs 15.2 → Compatible (casi)
- Xcode: 16.0 vs 16.3 → INCOMPATIBLE (necesita 16.3+)
```

### Problema Identificado

```
❌ Xcode 16.0 vs Xcode 16.3

El proyecto requiere Xcode 16.3 como mínimo.
Tu sistema tiene Xcode 16.0.

OPCIONES:
1. Actualizar Xcode a 16.3+ (App Store)
2. Instalar Xcode 16.3 beta si está disponible
3. Intentar compilar de todas formas (puede fallar)
```

---

## Comandos Útiles para Verificar

```bash
# Ver versión exacta de Xcode
xcodebuild -version

# Ver SDK disponible
ls /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/

# Ver Command Line Tools
clang --version
cmake --version
ninja --version

# Verificar tools de desarrollo
which cmake
which ninja
which clang
```

---

## Notas

- Xcode está instalado en /Applications/Xcode.app
- Command Line Tools están disponibles
- El sistema tiene suficiente RAM (17GB) para compilar
- 10 cores será bueno para compilación paralela
