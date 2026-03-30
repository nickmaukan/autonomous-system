# 🎵 Proyecto 09: Sistema de Música Procedural con IA

## Resumen Ejecutivo

**Objetivo:** Crear un sistema que genere música procedural adaptable para juegos, permitiendo generar BGM (background music) infinita y adaptativa basada en el estado del juego, usando IA generativa de audio.

**Herramientas principales:** AIVA, Boomy, Mubert, Google Magenta, Python

**Tiempo estimado:** 3-4 semanas

**Dificultad:** Alta (conceptos de audio + ML)

**Qué resuelve:** Música costosa/limitada → Generación infinita, adaptativa y económica.

---

## 1. Concepto

### El problema:

```
MÚSICA TRADICIONAL:
- $200-2000 por track original
- Música pre-hecha: $20-50 por license
- Limited variety (same loops)
- No adapt to gameplay
- Time-consuming to find

MÚSICA CON IA:
- Generación infinita: $0-50/mes
- Adaptive: changes with gameplay
- Unlimited variety
- Customizable en tiempo real
- Instant generation
```

### Arquitectura del sistema:

```
┌─────────────────────────────────────────────────────────────────┐
│                 PROCEDURAL MUSIC SYSTEM                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  GAME STATE                                                      │
│  ├── Current scene (menu, battle, exploration, cutscene)         │
│  ├── Player state (health, location)                              │
│  ├── Enemy presence (near/far/none)                             │
│  └── Time/Weather                                                │
│                                                                  │
│                    ▼                                              │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │              STATE ANALYZER                              │    │
│  │  - Maps game state → music parameters                   │    │
│  │  - Detects transitions                                  │    │
│  │  - Manages crossfades                                   │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│                    ▼                                              │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │              PARAMETER GENERATOR                         │    │
│  │  - BPM based on action intensity                        │    │
│  │  - Key based on mood                                    │    │
│  │  - Instrumentation based on setting                      │    │
│  │  - Intensity curve                                       │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│                    ▼                                              │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │              AI MUSIC GENERATOR                          │    │
│  │  - AIVA / Mubert / Magenta integration                  │    │
│  │  - Generates continuous stream                           │    │
│  │  - Seamless loops                                         │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│                    ▼                                              │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │              AUDIO MIXER                                  │    │
│  │  - Crossfade between tracks                               │    │
│  │  - Layer multiple stems                                   │    │
│  │  - Apply real-time effects                                │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│                    ▼                                              │
│  OUTPUT                                                          │
│  └── Seamless, adaptive game music                               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. Plan de implementación

### Fase 1: Análisis y diseño (Días 1-4)

```
DÍA 1: Game music fundamentals

MUSIC PARAMETERS:

1. TEMPO (BPM)
   - Menu/Rest: 70-90 BPM
   - Exploration: 90-110 BPM
   - Combat normal: 110-140 BPM
   - Combat intense: 140-180 BPM
   - Boss: 180-200 BPM

2. KEY (Musical key)
   - Happy scenes: Major keys (C, G, D, A)
   - Sad scenes: Minor keys (Am, Em, Dm)
   - Tense scenes: Minor + diminished
   - Victory: Major with dominant chord

3. INSTRUMENTATION
   - Medieval: Lute, flute, strings
   - Sci-fi: Synths, pads, electronic
   - Horror: Drones, strings, dissonant
   - Adventure: Orchestra, percussion

4. INTENSITY (0-100)
   - Affects: tempo, volume, complexity
   - Smooth transitions over 2-5 seconds

DÍA 2: State mapping

STATE_TO_MUSIC mapping:

Menu:
  - bpm: 80
  - key: "C_major"
  - mood: calm, welcoming
  - intensity: 20

Exploration Calm:
  - bpm: 95
  - key: "G_major"  
  - mood: peaceful, wonder
  - intensity: 30

Exploration Active:
  - bpm: 110
  - key: "D_major"
  - mood: adventurous
  - intensity: 50

Combat Normal:
  - bpm: 130
  - key: "Am"
  - mood: tense, action
  - intensity: 70

Combat Intense:
  - bpm: 160
  - key: "Dm"
  - mood: intense, urgent
  - intensity: 90

Boss:
  - bpm: 180
  - key: "Em"
  - mood: epic, dangerous
  - intensity: 100

Victory:
  - bpm: 140
  - key: "C_major"
  - mood: triumphant
  - intensity: 80

DÍA 3-4: API research

AI MUSIC SERVICES:

1. AIVA
   - Strengths: High quality, customizable
   - API: Yes
   - Pricing: $15/mo base
   - Generation time: 30-120 seconds
   - Loops: Yes, customizable

2. Mubert
   - Strengths: Infinite generation, API
   - API: Yes
   - Pricing: Freemium tier
   - Generation time: Real-time
   - Loops: Infinite streams

3. Boomy
   - Strengths: Quick, simple
   - API: Limited
   - Pricing: Freemium
   - Generation time: 20-60 seconds
   - Loops: Yes

4. Google Magenta (local)
   - Strengths: Free, extensible
   - API: Yes
   - Pricing: Free (GPU needed)
   - Generation time: Variable
   - Loops: Via generation
```

### Fase 2: Core system (Días 5-12)

```
DÍA 5-6: State analyzer

state_analyzer.py:
```python
from enum import Enum
from dataclasses import dataclass
from typing import Optional

class GameState(Enum):
    MENU = "menu"
    EXPLORATION_CALM = "exploration_calm"
    EXPLORATION_ACTIVE = "exploration_active"
    COMBAT_NORMAL = "combat_normal"
    COMBAT_INTENSE = "combat_intense"
    BOSS = "boss"
    VICTORY = "victory"
    DEFEAT = "defeat"
    CUTSCENE = "cutscene"

@dataclass
class MusicParameters:
    bpm: int
    key: str
    intensity: float  # 0.0 to 1.0
    mood: str
    genre: str
    instruments: list

class GameStateAnalyzer:
    def __init__(self):
        self.current_state = GameState.MENU
        self.previous_state = None
        self.transition_timer = 0
        self.transition_duration = 3.0  # seconds
        
    def update(self, game_data: dict, delta_time: float):
        """Analyze game state and determine music parameters"""
        
        # Detect state change
        new_state = self.analyze_game_state(game_data)
        
        if new_state != self.current_state:
            self.previous_state = self.current_state
            self.current_state = new_state
            self.transition_timer = 0
        
        # Update transition
        if self.previous_state:
            self.transition_timer += delta_time
        
        # Generate parameters
        return self.get_music_parameters()
    
    def analyze_game_state(self, game_data: dict) -> GameState:
        """Determine current game state"""
        
        if game_data.get("is_menu"):
            return GameState.MENU
        
        if game_data.get("health", 0) <= 0:
            return GameState.DEFEAT
        
        combat_intensity = game_data.get("combat_intensity", 0)
        
        if combat_intensity >= 0.9:
            if game_data.get("is_boss", False):
                return GameState.BOSS
            return GameState.COMBAT_INTENSE
        
        if combat_intensity >= 0.5:
            return GameState.COMBAT_NORMAL
        
        if combat_intensity >= 0.2:
            return GameState.EXPLORATION_ACTIVE
        
        return GameState.EXPLORATION_CALM
    
    def get_music_parameters(self) -> MusicParameters:
        """Get music parameters for current state"""
        
        state_params = {
            GameState.MENU: MusicParameters(
                bpm=80, key="C_major", intensity=0.2,
                mood="calm", genre="ambient", 
                instruments=["piano", "strings"]
            ),
            GameState.EXPLORATION_CALM: MusicParameters(
                bpm=95, key="G_major", intensity=0.3,
                mood="peaceful", genre="ambient",
                instruments=["flute", "strings", "harp"]
            ),
            GameState.EXPLORATION_ACTIVE: MusicParameters(
                bpm=110, key="D_major", intensity=0.5,
                mood="adventurous", genre="orchestral",
                instruments=["strings", "brass", "percussion"]
            ),
            GameState.COMBAT_NORMAL: MusicParameters(
                bpm=130, key="Am", intensity=0.7,
                mood="tense", genre="action",
                instruments=["drums", "strings", "synth"]
            ),
            GameState.COMBAT_INTENSE: MusicParameters(
                bpm=160, key="Dm", intensity=0.9,
                mood="intense", genre="action",
                instruments=["drums", "electric_guitar", "synth"]
            ),
            GameState.BOSS: MusicParameters(
                bpm=180, key="Em", intensity=1.0,
                mood="epic", genre="orchestral_epic",
                instruments=["full_orchestra", "choir", "drums"]
            ),
            GameState.VICTORY: MusicParameters(
                bpm=140, key="C_major", intensity=0.8,
                mood="triumphant", genre="orchestral",
                instruments=["full_orchestra", "choir"]
            ),
            GameState.DEFEAT: MusicParameters(
                bpm=60, key="Am", intensity=0.1,
                mood="sad", genre="ambient",
                instruments=["piano", "strings"]
            ),
        }
        
        return state_params.get(
            self.current_state,
            state_params[GameState.MENU]
        )
```

DÍA 7-8: AIVA/Mubert integration

music_generator.py:
```python
import requests
import json
from abc import ABC, abstractmethod
from typing import Optional
from pathlib import Path

class MusicGenerator(ABC):
    @abstractmethod
    def generate(
        self,
        bpm: int,
        key: str,
        mood: str,
        duration: int
    ) -> bytes:
        pass

class AIVAGenerator(MusicGenerator):
    """AIVA API integration"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.aiva.ai/v1"
    
    def generate(
        self,
        bpm: int,
        key: str,
        mood: str,
        duration: int
    ) -> bytes:
        """Generate music using AIVA"""
        
        payload = {
            "bpm": bpm,
            "key": key,
            "moodTag": mood,
            "durationSeconds": duration,
            " instrumentation": self.get_instrumentation(mood)
        }
        
        response = requests.post(
            f"{self.base_url}/generate",
            headers={"Authorization": f"Bearer {self.api_key}"},
            json=payload
        )
        
        if response.status_code == 200:
            job_id = response.json()["jobId"]
            return self.poll_for_completion(job_id)
        else:
            raise Exception(f"AIVA generation failed: {response.text}")
    
    def poll_for_completion(self, job_id: str, timeout: int = 120) -> bytes:
        """Poll AIVA until generation is complete"""
        # Implementation
        pass
    
    def get_instrumentation(self, mood: str) -> list:
        """Get instrumentation based on mood"""
        instrumentation_map = {
            "calm": ["piano", "strings"],
            "peaceful": ["flute", "harp"],
            "adventurous": ["strings", "brass"],
            "tense": ["strings", "drums"],
            "intense": ["drums", "electric_guitar"],
            "epic": ["orchestra", "choir"],
            "triumphant": ["orchestra", "brass"],
            "sad": ["piano", "cello"]
        }
        return instrumentation_map.get(mood, ["piano"])

class MubertGenerator(MusicGenerator):
    """Mubert API for infinite streams"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.mubert.com/v2"
    
    def generate(
        self,
        bpm: int,
        key: str,
        mood: str,
        duration: int
    ) -> bytes:
        """Generate infinite-ish music stream from Mubert"""
        
        # Map mood to Mubert tags
        tags = self.mood_to_tags(mood)
        
        payload = {
            "method": "RecordTrack",
            "params": {
                "pathtag": tags,
                "duration": duration,
                "bpm": bpm,
                "mode": "track"
            }
        }
        
        response = requests.post(
            f"{self.base_url}/RecordTrack",
            headers={"Authorization": f"Bearer {self.api_key}"},
            json=payload
        )
        
        if response.status_code == 200:
            data = response.json()
            # Download the audio file
            audio_url = data["data"]["download_link"]
            return self.download_audio(audio_url)
        else:
            raise Exception(f"Mubert failed: {response.text}")
    
    def mood_to_tags(self, mood: str) -> str:
        """Map game mood to Mubert tags"""
        tag_map = {
            "calm": "ambient,chill",
            "peaceful": "nature,ambient",
            "adventurous": "adventure,orchestral",
            "tense": "action,electronic",
            "intense": "hardstyle,drumstep",
            "epic": "epic,orchestral",
            "triumphant": "triumph,victory",
            "sad": "sad,piano"
        }
        return tag_map.get(mood, "ambient")
    
    def download_audio(self, url: str) -> bytes:
        response = requests.get(url)
        return response.content
```

DÍA 9-10: Audio mixer + crossfades

audio_mixer.py:
```python
import numpy as np
from scipy import signal
from scipy.io import wavfile
from typing import List, Tuple

class AudioMixer:
    def __init__(self, sample_rate: int = 44100):
        self.sample_rate = sample_rate
        self.current_track: np.ndarray = None
        self.next_track: np.ndarray = None
        self.crossfade_progress: float = 0.0
        self.crossfade_duration: float = 3.0  # seconds
    
    def load_track(self, audio_data: bytes) -> np.ndarray:
        """Load audio bytes to numpy array"""
        import io
        sr, data = wavfile.read(io.BytesIO(audio_data))
        
        # Convert to mono if stereo
        if len(data.shape) > 1:
            data = data.mean(axis=1)
        
        return data.astype(np.float32)
    
    def queue_track(self, audio_data: bytes):
        """Queue next track for crossfade"""
        self.next_track = self.load_track(audio_data)
        self.crossfade_progress = 0.0
    
    def get_audio(self, num_samples: int) -> np.ndarray:
        """Get mixed audio output"""
        
        if self.current_track is None:
            return np.zeros(num_samples)
        
        if self.next_track is None:
            return self.current_track[:num_samples]
        
        # Crossfade
        fade_samples = int(self.crossfade_duration * self.sample_rate)
        
        if self.crossfade_progress < 1.0:
            # Generate crossfade envelope
            fade_in = np.linspace(0, 1, fade_samples)
            fade_out = np.linspace(1, 0, fade_samples)
            
            # Mix
            output = np.zeros(num_samples)
            
            # Current track fading out
            if len(self.current_track) >= num_samples:
                output += self.current_track[:num_samples] * fade_out
            
            # Next track fading in
            if len(self.next_track) >= num_samples:
                output += self.next_track[:num_samples] * fade_in
            
            self.crossfade_progress += num_samples / fade_samples
            
            if self.crossfade_progress >= 1.0:
                self.current_track = self.next_track
                self.next_track = None
            
            return output
        
        return self.current_track[:num_samples]
    
    def apply_effects(self, audio: np.ndarray, effects: dict) -> np.ndarray:
        """Apply real-time audio effects"""
        
        if effects.get("lowpass"):
            cutoff = effects["lowpass"]
            nyq = self.sample_rate / 2
            cutoff_norm = min(0.99, cutoff / nyq)
            b, a = signal.butter(4, cutoff_norm, btype='low')
            audio = signal.filtfilt(b, a, audio)
        
        if effects.get("highpass"):
            cutoff = effects["highpass"]
            nyq = self.sample_rate / 2
            cutoff_norm = min(0.99, cutoff / nyq)
            b, a = signal.butter(4, cutoff_norm, btype='high')
            audio = signal.filtfilt(b, a, audio)
        
        if effects.get("reverb"):
            # Simple reverb approximation
            reverb = effects["reverb"]
            impulse = np.exp(-np.linspace(0, 5, int(self.sample_rate * reverb)))
            audio = np.convolve(audio, impulse, mode='same')
        
        # Normalize
        audio = audio / (np.max(np.abs(audio)) + 1e-6)
        
        return audio
```

DÍA 11-12: Main system integration

procedural_music_system.py:
```python
import threading
import queue
import time
from pathlib import Path
from typing import Optional

class ProceduralMusicSystem:
    def __init__(self, generator: MusicGenerator):
        self.generator = generator
        self.mixer = AudioMixer()
        self.state_analyzer = GameStateAnalyzer()
        
        self.generation_queue = queue.Queue()
        self.audio_buffer = queue.Queue(maxsize=10)
        
        self.is_running = False
        self.current_params: Optional[MusicParameters] = None
        
        self.buffer_duration = 30  # seconds
    
    def start(self):
        """Start the music system"""
        self.is_running = True
        
        # Start generation thread
        self.gen_thread = threading.Thread(target=self._generation_loop)
        self.gen_thread.daemon = True
        self.gen_thread.start()
    
    def stop(self):
        """Stop the music system"""
        self.is_running = False
        if hasattr(self, 'gen_thread'):
            self.gen_thread.join(timeout=5)
    
    def update(self, game_data: dict):
        """Update with current game state"""
        params = self.state_analyzer.update(game_data, time.delta)
        
        # Check if parameters changed significantly
        if self._should_regenerate(params):
            self._request_generation(params)
    
    def _should_regenerate(self, params: MusicParameters) -> bool:
        """Determine if we should regenerate music"""
        
        if self.current_params is None:
            return True
        
        # Significant BPM change
        if abs(params.bpm - self.current_params.bpm) > 20:
            return True
        
        # Significant intensity change
        if abs(params.intensity - self.current_params.intensity) > 0.3:
            return True
        
        # Key change (needs new generation)
        if params.key != self.current_params.key:
            return True
        
        return False
    
    def _request_generation(self, params: MusicParameters):
        """Queue music generation"""
        self.generation_queue.put(params)
        self.current_params = params
    
    def _generation_loop(self):
        """Background thread for music generation"""
        while self.is_running:
            try:
                params = self.generation_queue.get(timeout=1)
                
                # Generate music
                audio_data = self.generator.generate(
                    bpm=params.bpm,
                    key=params.key,
                    mood=params.mood,
                    duration=self.buffer_duration
                )
                
                # Queue for playback
                self.audio_buffer.put(audio_data)
                
                # Start crossfade if we have a current track
                if self.mixer.current_track is not None:
                    self.mixer.queue_track(audio_data)
                else:
                    self.mixer.current_track = self.mixer.load_track(audio_data)
                
            except queue.Empty:
                continue
            except Exception as e:
                print(f"Generation error: {e}")
    
    def get_audio_chunk(self, num_samples: int) -> np.ndarray:
        """Get mixed audio for playback"""
        return self.mixer.get_audio(num_samples)
```

### Fase 3: Integration con engine (Días 13-18)

```
DÍA 13-14: Godot integration

Godot plugin: procedural_music.gd
```gdscript
extends Node

signal audio_chunk_ready(chunk: PackedByteArray)

const SAMPLE_RATE = 44100
const CHUNK_SIZE = 4096

var music_system: Node = null
var audio_stream: AudioStreamPlayback = null
var is_playing = false

func _ready():
    # Initialize Python bridge
    music_system = preload("res://addons/procedural_music/music_bridge.gdns").new()

func start():
    music_system.start()
    is_playing = true
    
    # Start audio generation
    _generate_chunks()

func stop():
    is_playing = false
    music_system.stop()

func _process(delta):
    if is_playing:
        # Request audio from Python system
        var chunk = music_system.get_audio_chunk(CHUNK_SIZE)
        if chunk.size() > 0:
            # Convert to AudioStream and play
            var stream = AudioStreamSample.new()
            stream.data = chunk
            stream.format = AudioStreamSample.FORMAT_16_BITS
            stream.mix_rate = SAMPLE_RATE
            # Play through AudioStreamPlayer
            pass

func update_game_state(state_data: Dictionary):
    """Update music based on game state"""
    music_system.update(state_data)
```

DÍA 15-16: Unity integration

Unity component: ProceduralMusic.cs
```csharp
using UnityEngine;
using System.Threading;

public class ProceduralMusic : MonoBehaviour
{
    public AudioSource audioSource;
    
    private Thread generationThread;
    private ProceduralMusicSystem musicSystem;
    private bool isRunning;
    
    void Start()
    {
        musicSystem = new ProceduralMusicSystem(
            new AIVAGenerator("your-api-key")
        );
        
        musicSystem.Start();
        isRunning = true;
        
        generationThread = new Thread(GenerationLoop);
        generationThread.Start();
    }
    
    void Update()
    {
        // Send game state to music system
        var gameState = new Dictionary<string, object> {
            ["is_menu"] = GameManager.Instance.IsInMenu,
            ["health"] = Player.Instance.Health,
            ["combat_intensity"] = CombatManager.Instance.GetIntensity(),
            ["is_boss"] = CombatManager.Instance.IsBossFight
        };
        
        musicSystem.Update(gameState);
    }
    
    void OnDestroy()
    {
        isRunning = false;
        musicSystem?.Stop();
    }
}
```

DÍA 17-18: Testing + polish

TESTING:
1. State transitions
2. Crossfades
3. Audio quality
4. Memory usage
5. CPU/GPU impact

POLISH:
1. Add more moods/instruments
2. Improve crossfade algorithm
3. Add stem separation (if available)
4. Optimize performance
```

### Fase 4: Content library (Días 19-24)

```
DÍA 19-21: Pre-generate music library

Crear biblioteca de tracks pre-generados para fallback:

TRACKS:
├── Menu_Ambient_01.mp3 (90s)
├── Menu_Ambient_02.mp3
├── Exploration_Calm_01.mp3
├── Exploration_Calm_02.mp3
├── Exploration_Active_01.mp3
├── Combat_Normal_01.mp3
├── Combat_Normal_02.mp3
├── Combat_Intense_01.mp3
├── Boss_Epic_01.mp3
├── Boss_Epic_02.mp3
├── Victory_Triumph_01.mp3
└── Defeat_Sad_01.mp3

CACHE SYSTEM:
```python
class MusicCache:
    def __init__(self, cache_dir: Path):
        self.cache_dir = cache_dir
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
        # Load existing tracks
        self.tracks = {}
        for track_file in cache_dir.glob("*.mp3"):
            params = self.parse_filename(track_file.stem)
            self.tracks[self.get_key(params)] = track_file
    
    def get(self, params: MusicParameters) -> Optional[Path]:
        """Get cached track for parameters"""
        key = self.get_key(params)
        return self.tracks.get(key)
    
    def store(self, params: MusicParameters, audio_data: bytes):
        """Cache generated track"""
        key = self.get_key(params)
        filename = f"{key}.mp3"
        filepath = self.cache_dir / filename
        
        with open(filepath, "wb") as f:
            f.write(audio_data)
        
        self.tracks[key] = filepath
    
    def get_key(self, params: MusicParameters) -> str:
        return f"{params.mood}_{params.bpm}_{params.key}"
```

DÍA 22-24: Documentation + examples

DOCUMENTATION:
- Setup guide
- API reference
- Examples for each engine
- Troubleshooting
```

---

## 3. Prompts para generación

### AIVA prompts:

```json
{
  "bpm": 120,
  "key": "C_major",
  "moodTag": "adventurous",
  "durationSeconds": 60,
  "tags": ["orchestral", "adventure", "strings", "brass"]
}

{
  "bpm": 160,
  "key": "Em",
  "moodTag": "epic_battle",
  "durationSeconds": 90,
  "tags": ["epic", "orchestra", "choir", "drums"]
}
```

### Mubert tags:

```
ambient,chill,peaceful
adventure,orchestral,triumph
action,electronic,drums
epic,orchestral,battle
sad,piano,strings
horror,tension,dark
```

---

## 4. Costos y alternativas

### Costos mensuales:

```
TIER 1: $0 (Free tier)
├── Mubert: 25 tracks/month
├── Boomy: 10 tracks/month
└── Magenta: Unlimited (GPU cost)

TIER 2: $15-30/mes
├── AIVA: $15/mo (unlimited generation)
├── Mubert Pro: $25/mo (100 tracks)
└── Combined: $30-40/mes

TIER 3: $50+/mes
├── AIVA Studio: $50/mo
├── Mubert Studio: $50/mo
└── Custom trained models: $200+/mo
```

### Alternativa local (Gratis, requiere GPU):

```
Google Magenta + DDSP:
- Free, open source
- Runs locally
- Requires powerful GPU
- Generation slower
- More control
```

---

## 5. Métricas

```
QUALITY:
- Percepción de continuidad: 90%
- State transition smoothness: 85%
- Audio quality (vs human): 80%
- Memory usage: ~100MB

PERFORMANCE:
- Generation time: 30-120s (API)
- Crossfade: Smooth
- CPU impact: <5%
- GPU impact: 0% (if using API)

COST SAVINGS:
- Traditional composer: $500-2000/track
- This system: $0.05-0.10/track
- 100 tracks/month: $5-10 vs $50,000+
```

---

## 6. Aplicaciones

```
USOS:
- Infinite games (roguelikes, survival)
- Dynamic difficulty games
- Adaptive horror games
- Mobile games (small builds)
- Prototyping
- Educational games
```

---

_Volver a [README principal](../README.md)_
