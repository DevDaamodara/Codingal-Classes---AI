# 🎮 PIXEL QUEST - Classic Arcade Game

A nostalgic arcade game inspired by classic 80s arcade games like Pac-Man. Collect all the dots, avoid the ghosts, and advance through increasingly challenging levels!

## 🎯 Game Features

- **Classic Arcade Gameplay**: Collect all dots to advance to the next level
- **Retro Pixel Art Style**: Authentic 80s arcade aesthetic with neon colors
- **Progressive Difficulty**: More enemies and faster speeds as you advance
- **Power-ups**: Collect special power-ups for bonus points
- **High Score System**: Your best score is saved locally
- **Smooth Controls**: Responsive keyboard controls
- **Responsive Design**: Works on desktop and mobile devices

## 🕹️ How to Play

### Objective
- Collect all yellow dots (pellets) on the screen
- Avoid the colored ghosts (enemies)
- Grab purple power-ups for bonus points
- Complete all levels to win!

### Controls
- **Arrow Keys** or **WASD** - Move your character
- **SPACE** - Start/Pause game
- **R** - Restart game

### Game Mechanics
- **Pellets (Yellow Dots)**: Worth 10 points each
- **Power-ups (Purple Squares)**: Worth 50 points each
- **Level Completion**: Collect all pellets to advance
- **Lives**: You start with 3 lives
- **Enemies**: Ghosts that chase you around the maze

## 📁 Project Structure

```
arcade_game/
├── index.html          # Main HTML file
├── arcade_style.css    # Retro arcade styling
├── arcade_game.js      # Game logic and mechanics
├── app.py              # Python server
└── README.md           # This file
```

## 🚀 How to Run

### Option 1: Using Python Server (Recommended)

1. Open Command Prompt or Terminal
2. Navigate to the arcade_game directory:
   ```bash
   cd "c:\Users\munag\OneDrive\Codingal Classes - AI\arcade_game"
   ```
3. Run the Python server:
   ```bash
   python app.py
   ```
4. Open your browser and go to: `http://localhost:8001`

### Option 2: Direct File Opening

1. Navigate to the arcade_game folder
2. Right-click on `index.html`
3. Select "Open with" and choose your browser

### Option 3: Using Python's Built-in Server

```bash
cd "c:\Users\munag\OneDrive\Codingal Classes - AI\arcade_game"
python -m http.server 8001
```

## 🎨 Game Design

### Visual Style
- **Retro Arcade Cabinet**: Authentic 80s arcade machine design
- **Neon Colors**: Pink, green, and cyan neon aesthetic
- **Pixel Art**: Crisp, pixelated graphics
- **Glowing Effects**: Neon glow animations
- **Scanlines**: CRT monitor scanline effect

### Color Scheme
- **Primary**: Hot Pink (#ff006e)
- **Secondary**: Neon Green (#00ff00)
- **Accent**: Cyan (#00ffff)
- **Background**: Dark Blue (#0f3460)

## 🎮 Game Mechanics

### Player
- Yellow square that you control
- Moves on a grid-based maze
- Collects pellets and power-ups
- Loses a life when touching an enemy

### Enemies (Ghosts)
- Red, Pink, Cyan, and Orange colored ghosts
- Chase the player using simple AI
- Increase in number and speed with each level
- Patrol the maze when not chasing

### Maze
- Grid-based level design
- Walls block movement
- Multiple paths to navigate
- Changes slightly each game

## 📊 Scoring System

| Item | Points |
|------|--------|
| Pellet | 10 |
| Power-up | 50 |
| Level Complete | 100 |
| High Score | Saved locally |

## 🎯 Difficulty Progression

- **Level 1**: 2 enemies, normal speed
- **Level 2**: 3 enemies, faster speed
- **Level 3**: 4 enemies, even faster
- **Level 4+**: Maximum enemies, maximum speed

## 💾 Data Storage

- High scores are saved in browser's localStorage
- Persists between game sessions
- Can be cleared by clearing browser data

## 🔧 Technical Details

### Technologies Used
- **HTML5**: Canvas for game rendering
- **CSS3**: Retro styling and animations
- **JavaScript**: Game logic and mechanics
- **Python**: Simple HTTP server

### Browser Compatibility
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

### Performance
- 60 FPS gameplay
- Optimized canvas rendering
- Efficient collision detection
- Smooth animations

## 🎓 Learning Concepts

This game demonstrates:
- **Game Loop**: Update and render cycle
- **Collision Detection**: Grid-based collision system
- **AI Pathfinding**: Simple enemy AI
- **State Management**: Game states (menu, playing, paused, etc.)
- **Canvas API**: Drawing and animation
- **Event Handling**: Keyboard input
- **Local Storage**: High score persistence
- **Responsive Design**: Mobile-friendly layout

## 🐛 Known Limitations

- Enemies use simple AI (not optimal pathfinding)
- No sound effects (can be added)
- No multiplayer mode
- No difficulty settings

## 🚀 Future Enhancements

- Sound effects and background music
- Different game modes
- Difficulty settings
- Leaderboard system
- Mobile touch controls
- Power-up effects (invincibility, speed boost)
- Different maze layouts
- Boss levels

## 📝 Tips for Playing

1. **Plan Your Route**: Think ahead about where to go
2. **Use Corners**: Corners can be safe spots to avoid enemies
3. **Collect Power-ups**: They give bonus points
4. **Don't Rush**: Take your time to collect all pellets
5. **Watch Enemy Patterns**: Learn how enemies move
6. **Use Walls**: Hide behind walls to avoid enemies

## 🎮 Game States

- **MENU**: Initial state, waiting for player to start
- **PLAYING**: Active gameplay
- **PAUSED**: Game paused by player
- **LEVEL_COMPLETE**: All pellets collected
- **GAME_OVER**: No lives remaining

## 📱 Mobile Support

The game is fully responsive and works on mobile devices:
- Touch-friendly interface
- Responsive layout
- Optimized for smaller screens
- Works in portrait and landscape

## 🎉 Enjoy the Game!

Have fun playing Pixel Quest! Try to beat your high score and complete all levels. This is a classic arcade experience with a modern twist!

---

**Created with ❤️ for retro gaming enthusiasts**

*Inspired by classic arcade games of the 1980s*
