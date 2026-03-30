# 🔧 Proyecto 08: Automatización de Sprite Sheets

## Resumen Ejecutivo

**Objetivo:** Crear un pipeline automatizado que tome descripciones de sprites y genere sprite sheets completos listos para usar en engines, reduciendo tiempo de 4+ horas a 15-30 minutos.

**Herramientas principales:** Stable Diffusion, Python, PIL/Pillow, ImageMagick

**Tiempo estimado:** 2-3 semanas

**Dificultad:** Media-Alta (scripts + AI integration)

**Qué resuelve:** El proceso tedioso de generar, organizar y formatear sprites para game engines.

---

## 1. Concepto

### Pipeline:

```
┌─────────────────────────────────────────────────────────────────┐
│                     SPRITE SHEET PIPELINE                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  INPUT                                                           │
│  ├── Text description del sprite                                │
│  ├── Animation type (idle, walk, attack, etc.)                 │
│  ├── Number of frames                                          │
│  └── Style specifications                                       │
│                                                                  │
│                    ▼                                              │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │           STABLE DIFFUSION GENERATION                    │    │
│  │  - Generate N frames from description                    │    │
│  │  - Use ControlNet para consistency                      │    │
│  │  - Batch generation para velocidad                       │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│                    ▼                                              │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │              POST-PROCESSING                             │    │
│  │  - Remove backgrounds (rembg)                           │    │
│  │  - Resize to target resolution                          │    │
│  │  - Fix any artifacts                                    │    │
│  │  - Batch rename                                         │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│                    ▼                                              │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │              SHEET ASSEMBLY                             │    │
│  │  - Grid layout (4x4, 8x4, etc.)                       │    │
│  │  - Metadata JSON (frame data)                          │    │
│  │  - Import-ready format                                 │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│  OUTPUT                                                          │
│  ├── sprite_sheet.png (grid layout)                            │
│  ├── sprite_001.png, sprite_002.png (individual frames)       │
│  └── metadata.json (animation data)                             │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. Plan de implementación

### Fase 1: Core scripts (Días 1-7)

```
DÍA 1-2: Setup y estructuras

project/
├── main.py                 # Entry point
├── generators/
│   ├── __init__.py
│   ├── sd_generator.py     # Stable Diffusion API
│   └── batch_generator.py   # Batch processing
├── processors/
│   ├── __init__.py
│   ├── background_remover.py
│   ├── resizer.py
│   └── validator.py
├── assembler/
│   ├── __init__.py
│   ├── grid_assembler.py
│   └── metadata_generator.py
├── config/
│   └── settings.json
└── output/
```

```
DÍA 3-4: SD Generator

sd_generator.py:
```python
import requests
import json
from pathlib import Path
from typing import List, Optional

class StableDiffusionGenerator:
    def __init__(self, api_key: str, base_url: str = "https://api.stability.ai"):
        self.api_key = api_key
        self.base_url = base_url
        
    def generate_sprite(
        self,
        prompt: str,
        negative_prompt: str = None,
        width: int = 512,
        height: int = 512,
        steps: int = 30,
        seed: int = None
    ) -> bytes:
        """Generate a single sprite"""
        
        payload = {
            "text_prompts": [
                {"text": prompt, "weight": 1.0}
            ],
            "cfg_scale": 7.5,
            "width": width,
            "height": height,
            "steps": steps,
            "samples": 1
        }
        
        if negative_prompt:
            payload["text_prompts"].append(
                {"text": negative_prompt, "weight": -1.0}
            )
        
        if seed:
            payload["seed"] = seed
        
        response = requests.post(
            f"{self.base_url}/v1/generation/stable-diffusion-xl-1024-v1-0/image-to-image",
            headers={"Authorization": f"Bearer {self.api_key}"},
            json=payload
        )
        
        if response.status_code == 200:
            return response.json()["artifacts"][0]["base64"]
        else:
            raise Exception(f"Generation failed: {response.text}")
    
    def generate_batch(
        self,
        prompts: List[dict],
        output_dir: Path
    ) -> List[Path]:
        """Generate multiple sprites from prompts"""
        
        outputs = []
        for i, prompt_config in enumerate(prompts):
            try:
                image_data = self.generate_sprite(
                    prompt=prompt_config["prompt"],
                    negative_prompt=prompt_config.get("negative", ""),
                    width=prompt_config.get("width", 512),
                    height=prompt_config.get("height", 512)
                )
                
                output_path = output_dir / f"sprite_{i:03d}.png"
                with open(output_path, "wb") as f:
                    f.write(bytes.fromhex(image_data))
                
                outputs.append(output_path)
                
            except Exception as e:
                print(f"Failed to generate sprite {i}: {e}")
                outputs.append(None)
        
        return outputs
```
```

```
DÍA 5-6: Background remover + resizer

background_remover.py:
```python
from rembg import remove
from PIL import Image
from pathlib import Path
from typing import Union

class BackgroundRemover:
    def __init__(self):
        self.session = None  # Lazy init
    
    def remove(self, input_path: Union[str, Path]) -> Image.Image:
        """Remove background from image"""
        input_img = Image.open(input_path)
        
        # Remove background
        output = remove(input_img)
        
        return output
    
    def batch_remove(self, input_dir: Path, output_dir: Path):
        """Remove backgrounds from all images in directory"""
        output_dir.mkdir(parents=True, exist_ok=True)
        
        for img_path in input_dir.glob("*.png"):
            try:
                output_img = self.remove(img_path)
                output_path = output_dir / img_path.name
                output_img.save(output_path, "PNG")
            except Exception as e:
                print(f"Failed on {img_path}: {e}")
```

resizer.py:
```python
from PIL import Image
from pathlib import Path
from typing import Union, Tuple

class SpriteResizer:
    def __init__(self, target_size: Tuple[int, int]):
        self.target_size = target_size
    
    def resize(self, input_path: Union[str, Path]) -> Image.Image:
        """Resize image to target size, maintaining aspect ratio"""
        img = Image.open(input_path)
        
        # Calculate scaling to fit in target
        scale = min(
            self.target_size[0] / img.width,
            self.target_size[1] / img.height
        )
        
        new_size = (
            int(img.width * scale),
            int(img.height * scale)
        )
        
        resized = img.resize(new_size, Image.Resampling.LANCZOS)
        
        # Create new image with exact target size, centered
        result = Image.new("RGBA", self.target_size, (0, 0, 0, 0))
        paste_pos = (
            (self.target_size[0] - new_size[0]) // 2,
            (self.target_size[1] - new_size[1]) // 2
        )
        result.paste(resized, paste_pos, resized)
        
        return result
    
    def batch_resize(self, input_dir: Path, output_dir: Path):
        """Batch resize all images"""
        output_dir.mkdir(parents=True, exist_ok=True)
        
        for img_path in input_dir.glob("*.png"):
            try:
                resized = self.resize(img_path)
                output_path = output_dir / img_path.name
                resized.save(output_path, "PNG")
            except Exception as e:
                print(f"Failed on {img_path}: {e}")
```

```
DÍA 7: Grid assembler

grid_assembler.py:
```python
from PIL import Image
from pathlib import Path
from typing import Union, Tuple, List

class SpriteSheetAssembler:
    def __init__(
        self,
        frame_size: Tuple[int, int],
        columns: int,
        padding: int = 0
    ):
        self.frame_size = frame_size
        self.columns = columns
        self.padding = padding
    
    def assemble(
        self,
        frame_paths: List[Path],
        output_path: Path
    ) -> None:
        """Assemble frames into a sprite sheet"""
        
        num_frames = len(frame_paths)
        rows = (num_frames + self.columns - 1) // self.columns
        
        sheet_width = self.columns * (self.frame_size[0] + self.padding)
        sheet_height = rows * (self.frame_size[1] + self.padding)
        
        sheet = Image.new("RGBA", (sheet_width, sheet_height), (0, 0, 0, 0))
        
        for i, frame_path in enumerate(frame_paths):
            if frame_path is None:
                continue
            
            frame = Image.open(frame_path)
            
            col = i % self.columns
            row = i // self.columns
            
            x = col * (self.frame_size[0] + self.padding)
            y = row * (self.frame_size[1] + self.padding)
            
            # Resize to frame size
            frame = frame.resize(self.frame_size, Image.Resampling.LANCZOS)
            
            sheet.paste(frame, (x, y), frame)
        
        sheet.save(output_path, "PNG")
        print(f"Saved sprite sheet to {output_path}")
    
    def extract_frames(
        self,
        sheet_path: Path,
        output_dir: Path
    ) -> List[Path]:
        """Extract individual frames from sprite sheet"""
        
        sheet = Image.open(sheet_path)
        
        output_dir.mkdir(parents=True, exist_ok=True)
        
        num_cols = sheet.width // (self.frame_size[0] + self.padding)
        num_rows = sheet.height // (self.frame_size[1] + self.padding)
        
        frames = []
        
        for row in range(num_rows):
            for col in range(num_cols):
                x = col * (self.frame_size[0] + self.padding)
                y = row * (self.frame_size[1] + self.padding)
                
                frame = sheet.crop((
                    x, y,
                    x + self.frame_size[0],
                    y + self.frame_size[1]
                ))
                
                frame_path = output_dir / f"frame_{row}_{col:02d}.png"
                frame.save(frame_path)
                frames.append(frame_path)
        
        return frames
```

DÍA 8-10: Metadata generator

metadata_generator.py:
```python
import json
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class AnimationFrame:
    frame_index: int
    file_name: str
    duration: float  # in milliseconds
    
@dataclass  
class Animation:
    name: str
    frames: List[AnimationFrame]
    loop: bool = True

class MetadataGenerator:
    def __init__(self, sprite_name: str):
        self.sprite_name = sprite_name
        self.animations: Dict[str, Animation] = {}
    
    def add_animation(
        self,
        name: str,
        frame_count: int,
        fps: int = 10,
        loop: bool = True
    ):
        """Add an animation definition"""
        
        frames = [
            AnimationFrame(
                frame_index=i,
                file_name=f"{self.sprite_name}_{name}_{i:03d}.png",
                duration=1000 / fps
            )
            for i in range(frame_count)
        ]
        
        self.animations[name] = Animation(
            name=name,
            frames=frames,
            loop=loop
        )
    
    def generate_json(self, output_path: Path):
        """Generate metadata JSON"""
        
        metadata = {
            "sprite_name": self.sprite_name,
            "animations": {}
        }
        
        for name, anim in self.animations.items():
            metadata["animations"][name] = {
                "frames": [
                    {
                        "index": f.frame_index,
                        "file": f.file_name,
                        "duration": f.duration
                    }
                    for f in anim.frames
                ],
                "loop": anim.loop,
                "total_duration": sum(f.duration for f in anim.frames)
            }
        
        with open(output_path, "w") as f:
            json.dump(metadata, f, indent=2)
        
        return metadata
```

DÍA 11-14: Main orchestrator

main.py:
```python
#!/usr/bin/env python3
"""
Sprite Sheet Generator
Automated pipeline for generating game-ready sprite sheets
"""

import argparse
import json
from pathlib import Path
from typing import Dict, List

from generators.sd_generator import StableDiffusionGenerator
from generators.batch_generator import BatchGenerator
from processors.background_remover import BackgroundRemover
from processors.resizer import SpriteResizer
from assembler.grid_assembler import SpriteSheetAssembler
from assembler.metadata_generator import MetadataGenerator

class SpriteSheetGenerator:
    def __init__(self, config_path: Path):
        self.config = self.load_config(config_path)
        
        # Initialize components
        self.sd = StableDiffusionGenerator(
            api_key=self.config["api_keys"]["stability"]
        )
        self.bg_remover = BackgroundRemover()
        self.resizer = SpriteResizer(
            tuple(self.config["sprite"]["size"])
        )
        self.assembler = SpriteSheetAssembler(
            frame_size=tuple(self.config["sprite"]["size"]),
            columns=self.config["sprite"]["columns"]
        )
    
    def load_config(self, path: Path) -> Dict:
        with open(path) as f:
            return json.load(f)
    
    def run(self, description: str, animations: List[Dict]):
        """Main generation pipeline"""
        
        output_base = Path(self.config["output"]["base"])
        
        # Create temp directory
        temp_dir = output_base / "temp"
        temp_dir.mkdir(parents=True, exist_ok=True)
        
        # Step 1: Generate frames
        print("Generating frames...")
        all_frames = []
        
        for anim in animations:
            anim_name = anim["name"]
            frame_count = anim["frames"]
            
            prompts = self.build_prompts(description, anim_name, frame_count)
            frames = self.sd.generate_batch(prompts, temp_dir)
            
            all_frames.extend(frames)
        
        # Step 2: Remove backgrounds
        print("Removing backgrounds...")
        clean_dir = output_base / "clean"
        clean_dir.mkdir(parents=True, exist_ok=True)
        
        for frame_path in all_frames:
            if frame_path:
                self.bg_remover.remove(frame_path, clean_dir / frame_path.name)
        
        # Step 3: Resize
        print("Resizing...")
        resized_dir = output_base / "resized"
        resized_dir.mkdir(parents=True, exist_ok=True)
        
        self.resizer.batch_resize(clean_dir, resized_dir)
        
        # Step 4: Assemble sprite sheet
        print("Assembling sprite sheet...")
        resized_frames = sorted(resized_dir.glob("*.png"))
        
        sheet_path = output_base / f"{self.config['sprite']['name']}_sheet.png"
        self.assembler.assemble(resized_frames, sheet_path)
        
        # Step 5: Generate metadata
        print("Generating metadata...")
        metadata_gen = MetadataGenerator(self.config["sprite"]["name"])
        
        for anim in animations:
            metadata_gen.add_animation(
                name=anim["name"],
                frame_count=anim["frames"],
                fps=anim.get("fps", 10)
            )
        
        metadata_path = output_base / "metadata.json"
        metadata_gen.generate_json(metadata_path)
        
        print(f"Done! Output: {output_base}")
        
        # Cleanup temp
        # shutil.rmtree(temp_dir)

def main():
    parser = argparse.ArgumentParser(description="Generate sprite sheets")
    parser.add_argument("config", type=Path, help="Config file path")
    parser.add_argument("description", help="Sprite description")
    parser.add_argument("--output", type=Path, help="Output directory")
    
    args = parser.parse_args()
    
    generator = SpriteSheetGenerator(args.config)
    
    # Default animations
    animations = [
        {"name": "idle", "frames": 4, "fps": 6},
        {"name": "walk", "frames": 8, "fps": 10},
        {"name": "attack", "frames": 6, "fps": 12}
    ]
    
    generator.run(args.description, animations)

if __name__ == "__main__":
    main()
```

DÍA 15-17: Config file + CLI

config.json:
```json
{
  "api_keys": {
    "stability": "your-key-here"
  },
  "sprite": {
    "name": "character",
    "size": [32, 32],
    "columns": 4
  },
  "generation": {
    "steps": 30,
    "cfg_scale": 7.5
  },
  "output": {
    "base": "./output"
  }
}
```

cli_usage.py:
```python
# Usage examples

# Generate full sprite sheet
python main.py config.json "pixel art knight character, silver armor, front view"

# Custom animations
python main.py config.json "pixel art wizard" --animations idle:4:6 walk:8:10 attack:6:12

# List available commands
python main.py --help
```
```

DÍA 18-21: Testing y polish

TESTING:
1. Generate sprite sheet
2. Verify transparency
3. Check alignment in grid
4. Test import into Godot/Unity
5. Verify animation timing

POLISH:
1. Add error handling
2. Add progress bars
3. Add verbose mode
4. Add dry-run mode
5. Create documentation
```

---

## 3. Prompts para generación

### Base prompts:

```text
# Idle animation frames
"pixel art {character}, {description}, standing idle, 
breathing animation frame {n}, transparent background,
{game_style}, {size}, game sprite"

# Walk cycle frames  
"pixel art {character}, {description}, walking frame {n},
{game_style}, transparent background, {size}, game sprite"

# Attack frames
"pixel art {character}, {description}, attacking frame {n},
{game_style}, transparent background, {size}, game sprite"
```

### Negative prompts:

```text
"low quality, blurry, deformed, extra fingers,
bad anatomy, different character, inconsistent style,
photorealistic, smooth shading, photograph"
```

---

## 4. Usage examples

```bash
# Basic usage
python main.py config.json "pixel art ninja warrior, red outfit, cyberpunk style"

# With custom animations
python main.py config.json "pixel art mage, blue robes, magical" \
    --animations "idle:4:6,walk:8:10,cast:6:12"

# Debug mode
python main.py config.json "pixel art knight" --verbose --dry-run

# Output directory
python main.py config.json "pixel art thief" --output ./my_sprites
```

---

## 5. Output formats

### Generated files:

```
output/
├── knight_sheet.png        # Sprite sheet (4x4 grid)
├── knight_idle_000.png     # Individual frames
├── knight_idle_001.png
├── knight_walk_000.png
├── knight_walk_001.png
├── knight_attack_000.png
├── knight_attack_001.png
└── metadata.json           # Animation data
```

### metadata.json:

```json
{
  "sprite_name": "knight",
  "animations": {
    "idle": {
      "frames": [
        {"index": 0, "file": "knight_idle_000.png", "duration": 166.67},
        {"index": 1, "file": "knight_idle_001.png", "duration": 166.67}
      ],
      "loop": true,
      "total_duration": 666.68
    },
    "walk": {
      "frames": [...],
      "loop": true,
      "total_duration": 800.0
    }
  }
}
```

---

## 6. Engine integration

### Godot import:

```gdscript
# Load sprite sheet
var sprite_sheet = preload("res://sprites/knight_sheet.png")

# Parse metadata
func load_sprite_data():
    var json_file = FileAccess.open("res://sprites/metadata.json", FileAccess.READ)
    var json = JSON.parse_string(json_file.get_as_text())
    return json

# Create animation frames from sheet
func create_animation_frames(sheet: Texture2D, anim_data: Dictionary):
    var frames = []
    
    for frame_data in anim_data["frames"]:
        var frame = AtlasTexture.new()
        frame.atlas = sheet
        frame.region = Rect2(
            frame_data["index"] * frame_width,
            0,
            frame_width,
            frame_height
        )
        frames.append(frame)
    
    return frames
```

### Unity import:

```csharp
// Use Unity's SpriteUtility for sheet splitting
// Or use Odin Inspector for visual setup

public class SpriteSheetImporter : MonoBehaviour {
    public Texture2D spriteSheet;
    public int frameWidth = 32;
    public int frameHeight = 32;
    
    void GenerateSprites() {
        int cols = spriteSheet.width / frameWidth;
        int rows = spriteSheet.height / frameHeight;
        
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                Rect rect = new Rect(
                    c * frameWidth,
                    r * frameHeight,
                    frameWidth,
                    frameHeight
                );
                
                Sprite.Create(
                    spriteSheet,
                    rect,
                    new Vector2(0.5f, 0.5f),
                    16
                );
            }
        }
    }
}
```

---

## 7. Métricas

```
SPEED:
- Manual sprite sheet: 4-8 hours
- This pipeline: 15-30 minutes
- Speedup: 10-20x

QUALITY:
- Consistency: High (ControlNet)
- Background removal: 95%+ accuracy
- Frame alignment: Pixel-perfect

COST:
- SD API: ~$0.01-0.05 per frame
- 50 frames: $0.50-2.50
- vs manual artist: $200-500
```

---

_Volver a [README principal](../README.md)_
