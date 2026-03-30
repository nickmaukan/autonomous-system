#!/bin/bash
# create_portable.sh
# Crea una versión portable de Aseprite para compartir

set -e

PORTABLE_DIR="$HOME/Aseprite-Portable"
ZIP_NAME="Aseprite-Portable-1.0.zip"

echo "🎨 Creating Aseprite Portable Build"
echo "=================================="
echo ""

# Colores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# 1. Clean previous
echo "🧹 Cleaning previous builds..."
rm -rf "$PORTABLE_DIR"
rm -f ~/"$ZIP_NAME"

# 2. Verify source exists
if [ ! -d "$HOME/aseprite/build/bin/aseprite.app" ]; then
    echo -e "${RED}❌ Error: Aseprite not found at ~/aseprite/build/bin/aseprite.app${NC}"
    echo "   Compile Aseprite first using build_aseprite.sh"
    exit 1
fi

if [ ! -d "$HOME/deps/skia" ]; then
    echo -e "${RED}❌ Error: Skia not found at ~/deps/skia${NC}"
    echo "   Download and setup Skia first"
    exit 1
fi

# 3. Create structure
echo "📁 Creating directory structure..."
mkdir -p "$PORTABLE_DIR"

# 4. Copy app
echo "📦 Copying Aseprite.app..."
cp -R "$HOME/aseprite/build/bin/aseprite.app" "$PORTABLE_DIR/"

# 5. Copy Skia into app
echo "📚 Copying Skia libraries into app bundle..."
mkdir -p "$PORTABLE_DIR/aseprite.app/Contents/Resources/skia"

# Copy essential directories
for dir in include modules src third_party; do
    if [ -d "$HOME/deps/skia/$dir" ]; then
        cp -R "$HOME/deps/skia/$dir" "$PORTABLE_DIR/aseprite.app/Contents/Resources/skia/"
        echo "   ✓ Copied $dir"
    fi
done

# Copy compiled libraries
mkdir -p "$PORTABLE_DIR/aseprite.app/Contents/Resources/skia/out/Release-arm64"
if [ -d "$HOME/deps/skia/out/Release-arm64" ]; then
    cp "$HOME/deps/skia/out/Release-arm64"/*.a "$PORTABLE_DIR/aseprite.app/Contents/Resources/skia/out/Release-arm64/" 2>/dev/null || true
    echo "   ✓ Copied compiled libraries"
fi

# 6. Copy licenses
echo "📄 Copying licenses..."
cp "$HOME/deps/skia/LICENSE" "$PORTABLE_DIR/aseprite.app/Contents/Resources/" 2>/dev/null || true

# 7. Set permissions
echo "🔧 Setting permissions..."
chmod +x "$PORTABLE_DIR/aseprite.app/Contents/MacOS/aseprite"

# 8. Create ZIP
echo "📦 Creating ZIP archive..."
cd "$PORTABLE_DIR"
zip -r ~/"$ZIP_NAME" aseprite.app -x "*.DS_Store" -x "__MACOSX/*"

# 9. Summary
echo ""
echo -e "${GREEN}✅ Portable build created!${NC}"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📍 Location: ~/$ZIP_NAME"
SIZE=$(ls -lh ~/$ZIP_NAME 2>/dev/null | awk '{print $5}')
echo "📊 Size: $SIZE"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "To share with another Mac:"
echo ""
echo "1. UPLOAD TO CLOUD:"
echo "   - Google Drive, Dropbox, iCloud, etc."
echo "   - Download on target Mac"
echo "   - unzip Aseprite-Portable-1.0.zip"
echo "   - mv aseprite.app /Applications/"
echo "   - chmod +x /Applications/aseprite.app/Contents/MacOS/aseprite"
echo ""
echo "2. VIA USB:"
echo "   - Copy the ZIP to USB"
echo "   - Transfer to target Mac"
echo "   - Same unzip and move steps"
echo ""
echo "3. VIA AIRDROP:"
echo "   - Right-click the ZIP"
echo "   - Share → AirDrop"
echo "   - Receive on target Mac"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "⚠️  NOTE: For this to work, target Mac needs:"
echo "   - Apple Silicon (M1/M2/M3/M4)"
echo "   - macOS 12.0 or newer"
echo ""
echo "If it doesn't work on another Mac:"
echo "   - Download the ZIP on that Mac"
echo "   - Run: xattr -cr /Applications/aseprite.app"
echo "   - Then try opening again"
echo ""
