# Slime Slayer - TEST_NOTES

## What Works
- ✅ Knight player with walk animation (8 frames from sprite sheet)
- ✅ Attack animation with visual attack box (yellow flash)
- ✅ Slimes bounce from side to side with squish animation
- ✅ Goblins walk toward player and attack when close
- ✅ Ground platform at bottom of screen
- ✅ Score: +10 per slime, +25 per goblin, shown as floating popups
- ✅ Health: 3 hearts, invincibility frames after hit, screen shake
- ✅ Game states: Start screen, Playing, Game Over with restart
- ✅ Increasing difficulty: spawn rate and enemy count increase over time
- ✅ AABB collision detection (player attack vs enemies, enemies vs player)
- ✅ Gravity physics and jumping
- ✅ Web Audio API sound effects (attack, hit, jump, kills, game over)
- ✅ Particle system for death/hit effects
- ✅ Pixel art background (night scene with moon, hills)
- ✅ Stomping slimes (jump on them to kill)
- ✅ Knockback when hit by enemies
- ✅ Enemy types differentiate (slimes = 1HP, goblins = 2HP)

## Sprites Used
- `characters/knight_walk_v2.png` (8 frames, 64x64)
- `characters/slime_fixed.png` (4 frames, 32x32)
- `enemies/goblin_idle_fixed.png` (4 frames, 32x32)
- `enemies/goblin_attack.png` (6 frames, 32x32)
- `enemies/goblin_walk.png` (6 frames, 32x32) — used for goblin walking

## Missing (Fallback to Placeholder)
- No placeholder fallbacks needed — all sprites load correctly

## Potential Polish
- Goblin sprites may not align perfectly in width (walk vs attack sheets differ) — visual is slightly off but functional
- Goblin doesn't have a separate death animation — enemy fades/squishes out
- Player sprite attack frames reuse walk frames (no dedicated attack sprite in the source files)
- No boss wave every N waves (could be added)
- No pause menu
- High score not persisted (no localStorage)
- Mobile controls not implemented (keyboard only)
