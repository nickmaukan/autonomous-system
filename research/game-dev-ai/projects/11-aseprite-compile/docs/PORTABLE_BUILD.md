# 📦 Aseprite Portable - Guía para compartir entre Macs

_Guía para crear una versión portable de Aseprite que funcione en múltiples Macs._

---

## Resumen del problema

```
ACTUALMENTE:
├── Aseprite compilado en: ~/aseprite/
├── Skia en: ~/deps/skia/
├── Paths hardcoded durante compilación
└── ⚠️ Solo funciona en el Mac original
```

---

## Método recomendado: Incluir Skia en el App Bundle

Este método empaqueta Skia dentro del .app para que sea self-contained.

### Paso 1: Crear estructura portable

```bash
# Crear carpeta para el build portable
mkdir -p ~/Aseprite-Portable
cd ~/Aseprite-Portable

# Copiar el app bundle
cp -R ~/aseprite/build/bin/aseprite.app .

# Copiar Skia dentro del app
mkdir -p aseprite.app/Contents/Resources/skia
cp -R ~/deps/skia/* aseprite.app/Contents/Resources/skia/

# Copiar LICENSE y archivos necesarios
cp ~/aseprite/build/bin/aseprite.app/Contents/Resources/data.key aseprite.app/Contents/Resources/ 2>/dev/null
cp ~/aseprite/build/bin/aseprite.app/Contents/Resources/*.txt aseprite.app/Contents/Resources/ 2>/dev/null
```

### Paso 2: Reorganizar estructura de Skia

```bash
cd ~/Aseprite-Portable/aseprite.app/Contents/Resources/skia

# Crear estructura estándar que espera Aseprite
mkdir -p out/Release-arm64

# Mover archivos a la ubicación correcta
# (Asumiendo que los archivos ya están en ~/deps/skia/out/Release-arm64/)
```

### Paso 3: Verificar tamaños

```bash
cd ~/Aseprite-Portable
du -sh aseprite.app/
# Debería mostrar ~400-500MB

# Verificar contenido
ls -la aseprite.app/Contents/
```

### Paso 4: Comprimir para compartir

```bash
# Crear ZIP portable
cd ~/Aseprite-Portable
zip -r Aseprite-Portable-1.0.zip aseprite.app

# Ver tamaño final
ls -lh Aseprite-Portable-1.0.zip
```

### Paso 5: Compartir

```
OPCIONES DE COMPARTIR:

1. AirDrop (si ambos Macs están cerca):
   - Clic derecho en Aseprite-Portable-1.0.zip
   - Compartir → AirDrop

2. USB/Disco externo:
   - Copiar el ZIP o el .app directo

3. Google Drive / Dropbox:
   - Subir el ZIP
   - Descargar en el otro Mac

4. GitHub Release (si quieres publicly):
   - Crear release en repo
   - Upload como asset
```

---

## Instalación en otro Mac

### Opción A: ZIP directo

```bash
# 1. Descargar ZIP

# 2. Descomprimir
unzip Aseprite-Portable-1.0.zip

# 3. Mover a Applications
mv aseprite.app /Applications/

# 4. Dar permisos
chmod +x /Applications/aseprite.app/Contents/MacOS/aseprite

# 5. Ejecutar
open /Applications/aseprite.app
# O buscar "Aseprite" en Launchpad
```

### Opción B: Copiar directo

```bash
# En el Mac con el ZIP descomprimido:
cp -R aseprite.app /Applications/

# O si compartes el .app directo:
cp -R aseprite.app /Applications/
chmod +x /Applications/aseprite.app/Contents/MacOS/aseprite
```

---

## Requisitos para el otro Mac

```
PARA QUE FUNCIONE:

Hardware:
├── Mac con Apple Silicon (M1/M2/M3/M4)
└── macOS 12.0+ (Sequoia 15.0 recomendado)

Software:
├── Nada adicional requerido
└── El ZIP incluye todo
```

---

## Troubleshooting en otro Mac

### Error: "App is damaged"

```bash
# Quitar extended attributes
xattr -cr /Applications/aseprite.app
open /Applications/aseprite.app
```

### Error: "Can't be opened because..."

```bash
# En System Settings → Privacy & Security
# Buscar mensaje de security
# Click "Open Anyway"
```

### App no inicia

```bash
# Ver logs
open ~/Library/Logs/DiagnosticReports/
# Buscar aseprite related logs

# O desde terminal:
/Applications/aseprite.app/Contents/MacOS/aseprite 2>&1
```

---

## Script automático para crear portable

```bash
#!/bin/bash
# create_portable.sh

set -e

PORTABLE_DIR="$HOME/Aseprite-Portable"
ZIP_NAME="Aseprite-Portable-1.0.zip"

echo "🎨 Creating Aseprite Portable Build"
echo "=================================="
echo ""

# 1. Clean previous
rm -rf "$PORTABLE_DIR"
rm -f ~/"$ZIP_NAME"

# 2. Create structure
echo "📁 Creating directory structure..."
mkdir -p "$PORTABLE_DIR"

# 3. Copy app
echo "📦 Copying Aseprite.app..."
cp -R "$HOME/aseprite/build/bin/aseprite.app" "$PORTABLE_DIR/"

# 4. Copy Skia into app
echo "📚 Copying Skia libraries..."
mkdir -p "$PORTABLE_DIR/aseprite.app/Contents/Resources/skia"

# Copy essential Skia files
cp -R "$HOME/deps/skia/include" "$PORTABLE_DIR/aseprite.app/Contents/Resources/skia/"
cp -R "$HOME/deps/skia/modules" "$PORTABLE_DIR/aseprite.app/Contents/Resources/skia/"
cp -R "$HOME/deps/skia/src" "$PORTABLE_DIR/aseprite.app/Contents/Resources/skia/"
cp -R "$HOME/deps/skia/third_party" "$PORTABLE_DIR/aseprite.app/Contents/Resources/skia/"

# Copy compiled libraries
mkdir -p "$PORTABLE_DIR/aseprite.app/Contents/Resources/skia/out/Release-arm64"
cp "$HOME/deps/skia/out/Release-arm64/libskia.a" "$PORTABLE_DIR/aseprite.app/Contents/Resources/skia/out/Release-arm64/"
cp "$HOME/deps/skia/out/Release-arm64/"*.a "$PORTABLE_DIR/aseprite.app/Contents/Resources/skia/out/Release-arm64/"

# 5. Copy licenses
echo "📄 Copying licenses..."
cp "$HOME/deps/skia/LICENSE" "$PORTABLE_DIR/aseprite.app/Contents/Resources/" 2>/dev/null || true

# 6. Set permissions
echo "🔧 Setting permissions..."
chmod +x "$PORTABLE_DIR/aseprite.app/Contents/MacOS/aseprite"

# 7. Create ZIP
echo "📦 Creating ZIP archive..."
cd "$PORTABLE_DIR"
zip -r ~/"$ZIP_NAME" aseprite.app

# 8. Summary
echo ""
echo "✅ Portable build created!"
echo ""
echo "📍 Location: ~/$ZIP_NAME"
echo "📊 Size: $(ls -lh ~/$ZIP_NAME | awk '{print $5}')"
echo ""
echo "To share:"
echo "1. Upload to cloud or copy to USB"
echo "2. Recipient: unzip and move aseprite.app to /Applications/"
echo "3. Run: chmod +x /Applications/aseprite.app/Contents/MacOS/aseprite"
```

---

## Notas importantes

### Limitaciones

```
⚠️ ESTE MÉTODO PUEDE NO FUNCIONAR SI:

1. El otro Mac tiene macOS muy diferente
2. Faltan librerías del sistema
3. Paths absolutos en el código

SI FALLA:
- Opción: Compilar en cada Mac individually
- O: Comprar licencia oficial $20
```

### Por qué funciona este método

```
El App Bundle de macOS puede incluir:
├── El executable
├── Librerías dinámicas (.dylib)
├── Recursos (skia, fonts, etc.)
└── Info.plist con configuración

Al incluir Skia dentro del bundle,
no necesita paths externos.
```

---

## Versión oficial vs Compilada

| Aspecto | Versión Oficial ($20) | Compilada (esta) |
|---------|----------------------|------------------|
| Costo | $20 | $0 |
| Soporte | Sí | No |
| Updates | Automáticos | Manual |
| Funciona siempre | ✅ | ⚠️ Puede fallar |
| portable | Sí | Depende |

---

## Recomendación final

```
PARA USO PERSONAL EN 2 MACS:
✅ Usa el método portable (ZIP)

PARA DISTRIBUIR A OTROS:
❌ No recomendado - errores potenciales
✅ Mejor: Comprar licencia oficial $20
✅ O: Compilar en cada Mac individually
```

---

_Volver a [README principal](../README.md)_
