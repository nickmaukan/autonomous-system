# Dungeon Survivor - Test Notes

## Location
`~/AutonomousSystem/research/game-dev-ai/projects/mini-games/dungeon-survivor/index.html`

## How to Play
1. Open `index.html` in a web browser
2. Click **START GAME**
3. Use **WASD** to move the knight
4. Press **SPACE** to swing sword (360° arc attack)

## Features Implemented

### Player
- 8-directional WASD movement
- 360° sword swing on SPACE (0.5s cooldown)
- 5 HP, 1 second invincibility after taking damage
- Visual flash when damaged
- Animated sprite from knight_walk_v2.png (8 frames)

### Enemies (6 types)
| Type | Speed | HP | Points | Behavior |
|------|-------|-----|--------|----------|
| Goblin | 1.2 | 30 | 25 | Walks toward player |
| Skeleton | 1.8 | 20 | 30 | Faster walker |
| Bat | 2.0 | 15 | 20 | Curves while moving |
| Spider | 1.5 | 25 | 35 | Medium speed |
| Ghost | 1.0 | 10 | 40 | Phases through (no collision damage) |
| Zombie | 0.6 | 60 | 50 | Slow but tanky |

### Wave System
- Wave advances every 30 seconds
- More enemies spawn per wave
- Enemy spawn rate increases each wave
- Enemy type variety increases in later waves
- Burst spawn at wave start

### Scoring & Combo
- Base points × combo multiplier
- Combo increases by 1 per kill (max x10)
- Combo resets after 1.5 seconds without a kill
- Combo popup displays on screen

### Health System
- Player has 5 HP
- Health packs spawn every ~10 seconds (max 2 on screen)
- Health packs heal 1 HP and despawn after 10 seconds
- Green cross with floating animation

### Game Over
- Displays final score, time survived, wave reached
- High score saved to localStorage
- Shows "NEW HIGH SCORE!" if beaten

### Visual Effects
- Particle explosions on enemy death
- Hit flash on enemy damage
- Knockback on enemies when hit
- Vignette effect on screen edges
- Animated sprites for player and all enemies
- Health bars on damaged enemies
- Ghost transparency effect

## Technical Details
- Resolution: 900x600
- Target: 60 FPS via requestAnimationFrame
- Collision: AABB (Axis-Aligned Bounding Box)
- Sprite loading: Async with Promise cache
- Fallback colored shapes when sprites fail to load
- Floor tiles from stone_cobble.png

## Sprites Expected
All sprites loaded relative to: `../02-pixel-art-asset-pack/assets/`
- `characters/knight_walk_v2.png` (8 frames, 64x64)
- `enemies/goblin_idle_fixed.png` (4 frames)
- `enemies/skeleton_idle.png` (4 frames)
- `enemies/bat_fly.png` (6 frames)
- `enemies/spider_idle.png` (4 frames)
- `enemies/ghost_float.png` (6 frames)
- `enemies/zombie_idle.png` (4 frames)
- `environment/floors/floor_stone_cobble.png`

## Manual Testing Checklist
- [ ] Game starts on button click
- [ ] WASD moves player smoothly
- [ ] SPACE attacks with visual arc
- [ ] Attack has visible cooldown
- [ ] Enemies spawn from screen edges
- [ ] Each enemy type behaves differently
- [ ] Ghost doesn't deal collision damage
- [ ] Bat curves in flight path
- [ ] Health packs heal player
- [ ] Combo multiplier works
- [ ] Wave number increases
- [ ] Game over shows on death
- [ ] High score persists across reloads
- [ ] Restart works properly
