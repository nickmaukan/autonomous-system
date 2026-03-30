# Knight Runner - Test Notes

## Build Status: ✅ COMPLETE

## File Location
`~/AutonomousSystem/research/game-dev-ai/projects/mini-games/knight-runner/index.html`

## How to Play
1. Open `index.html` in any modern browser
2. Press **SPACE** to start
3. **SPACE** = Jump over rocks, spikes, slimes
4. **X** = Attack bats and slimes
5. **R** = Restart after game over

## Features Implemented

### Core Gameplay
- [x] Knight auto-runs with 8-frame walk animation
- [x] SPACE jump with proper gravity/arc physics
- [x] X attack with sword swing arc + hitbox
- [x] One-hit death on obstacle collision
- [x] Game Over screen with final score
- [x] Restart with R key

### Obstacles
- [x] **Rocks** — Ground obstacles, must jump over
- [x] **Spikes** — Ground obstacles, must jump over
- [x] **Bats** — Flying at head height, can attack OR jump over
- [x] **Slimes** — Ground bouncing enemies, jump over OR attack

### Visual Features
- [x] Parallax scrolling background (3 layers: mountains, mid hills, near hills)
- [x] Starfield with twinkling animation
- [x] Moon
- [x] Scrolling ground tiles with grass tufts
- [x] Particle effects on jump, attack kills, and death
- [x] Fallback pixel-art styled sprites if sprite sheets fail to load

### Scoring
- [x] Distance-based score (accumulates over time, faster = more points)
- [x] Bat kill: +50 points
- [x] Slime kill: +30 points

### Difficulty Progression
- [x] Speed starts at 4, increases by 0.3 every 5 seconds
- [x] Max speed caps at 12
- [x] Spawn interval decreases over time (more obstacles)
- [x] Double-spawn chance at high speeds

## Sprite Sheet Handling
- Knight walk: `characters/knight_walk_v2.png` (8 frames × 64×64)
- Bat fly: `enemies/bat_fly.png` (6 frames × 24×24)
- Slime: `characters/slime_fixed.png` (fallback: drawn programmatically)
- If sprites fail to load, fallback procedural pixel-art is drawn

## Browser Compatibility
- Tested on Chrome/Firefox/Safari (modern versions)
- Canvas 2D, no WebGL required
- 60 FPS target via requestAnimationFrame

## Known Limitations
- Bat sprite sheet loaded but drawn procedurally in this version (wing animation)
- No audio (kept simple for single-file delivery)
- No save/leaderboard (single session)
- Slime sprite sheet exists but drawn procedurally (matching task description of "slime_fixed.png" as fallback)

## Controls Summary
| Key | Action |
|-----|--------|
| SPACE | Jump / Start game |
| X | Attack (sword swing) |
| R | Restart (any time) |

## Playability Notes
- Early game is easy, gives player time to learn controls
- By score 200+, speed becomes challenging
- Bats at head height require quick reactions — attack or jump
- Rocks/spikes are easy to clear with basic jump timing
- Slimes have a bounce animation but don't move horizontally — just jump over them
