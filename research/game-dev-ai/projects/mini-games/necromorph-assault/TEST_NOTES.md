# TEST_NOTES.md — Necromorph Assault

## Build Summary
- **File:** `index.html` (~18KB, single-file)
- **Sprites used:** `engineer_frame1-8.png` (player walk), `necromorph_twitch.png` / `necromorph_attack_fixed.png` (enemies)
- **Resolution:** 800×600 canvas
- **Target:** 60 FPS

## What's Implemented

### Core Gameplay
- [x] WASD movement (8-directional, normalized)
- [x] Mouse aim — player rotates to face cursor
- [x] Click-to-shoot plasma projectiles with trail effect
- [x] Muzzle flash on shoot (80ms duration, yellow/white glow)
- [x] Player clamped to canvas bounds

### Enemies
- [x] Spawn from all 4 edges at random positions
- [x] Move toward player at variable speed (1.4–1.9 px/frame)
- [x] Attack when within 40px (10 damage, 800ms cooldown)
- [x] 3 HP each, hit-flash on damage
- [x] HP bar shown when damaged
- [x] 6-frame twitch animation / 8-frame attack animation

### Scoring & Combos
- [x] +15 per kill × combo multiplier
- [x] Combo window: 2 seconds
- [x] Combo displayed as `Nx COMBO!` (max display 5x)
- [x] Score shown top-right HUD

### Waves
- [x] Wave 1: 8 enemies, increases by 3 per wave
- [x] Spawn delay decreases per wave (1200ms → min 400ms)
- [x] "WAVE N" announcement with fade
- [x] Brief pause between waves (2 seconds)
- [x] Enemies remaining counter

### Game States
- [x] **Menu** — title screen, click to start
- [x] **Playing** — full gameplay loop
- [x] **Game Over** — score + wave display, click to restart

### Visual Polish
- [x] Dark grid background (sci-fi aesthetic)
- [x] Projectile trails (5-point fade)
- [x] Player invincibility frames (500ms) after hit
- [x] HP bar color changes: green → yellow → red
- [x] FPS counter (top-right)

## Manual Test Checklist
- [ ] Game loads without console errors
- [ ] Player spawns at center
- [ ] WASD moves player smoothly
- [ ] Player sprite rotates toward mouse cursor
- [ ] Clicking fires projectile from gun tip
- [ ] Muzzle flash visible on each shot
- [ ] Necromorphs spawn from edges each wave
- [ ] Enemies path toward player
- [ ] Taking damage depletes health bar
- [ ] Player flashes when invincible
- [ ] Killing enemy increases score (+15 × combo)
- [ ] Combo multiplier resets after 2s without kill
- [ ] Wave number increments after clearing all enemies
- [ ] Wave announcement appears briefly
- [ ] Game Over screen appears at 0 HP
- [ ] Click to restart works

## Known Notes
- Player uses 8 individual frame files (engineer_frame1-8) for walk animation
- Enemy uses sprite sheets: necromorph_twitch.png (6-frame) and necromorph_attack_fixed.png (8-frame, 4 cols)
- If sprite images fail to load, game still runs (uses canvas primitives)
- Target: ~60 FPS at 60 enemies on-screen
