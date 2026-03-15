// Pixel Quest - Classic Arcade Game
// A nostalgic arcade game with retro pixel art style

const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

// Game Constants
const GRID_SIZE = 20;
const COLS = canvas.width / GRID_SIZE;
const ROWS = canvas.height / GRID_SIZE;

// Game States
const GAME_STATE = {
    MENU: 'menu',
    PLAYING: 'playing',
    PAUSED: 'paused',
    GAME_OVER: 'gameOver',
    LEVEL_COMPLETE: 'levelComplete'
};

// Game Variables
let gameState = GAME_STATE.MENU;
let score = 0;
let level = 1;
let lives = 3;
let highScore = localStorage.getItem('pixelQuestHighScore') || 0;

// Player Object
const player = {
    x: 10,
    y: 10,
    width: GRID_SIZE,
    height: GRID_SIZE,
    speed: 1,
    direction: { x: 0, y: 0 },
    nextDirection: { x: 0, y: 0 },
    color: '#ffff00'
};

// Enemies (Ghosts)
let enemies = [];

// Pellets (Dots to collect)
let pellets = [];

// Power-ups
let powerUps = [];

// Game Objects
let walls = [];

// Input Handling
const keys = {};

document.addEventListener('keydown', (e) => {
    keys[e.key.toLowerCase()] = true;

    // Arrow keys and WASD
    if (e.key === 'ArrowUp' || e.key === 'w' || e.key === 'W') {
        player.nextDirection = { x: 0, y: -1 };
    }
    if (e.key === 'ArrowDown' || e.key === 's' || e.key === 'S') {
        player.nextDirection = { x: 0, y: 1 };
    }
    if (e.key === 'ArrowLeft' || e.key === 'a' || e.key === 'A') {
        player.nextDirection = { x: -1, y: 0 };
    }
    if (e.key === 'ArrowRight' || e.key === 'd' || e.key === 'D') {
        player.nextDirection = { x: 1, y: 0 };
    }

    // Space to start/pause
    if (e.key === ' ') {
        e.preventDefault();
        if (gameState === GAME_STATE.MENU) {
            startGame();
        } else if (gameState === GAME_STATE.PLAYING) {
            pauseGame();
        } else if (gameState === GAME_STATE.PAUSED) {
            resumeGame();
        }
    }

    // R to restart
    if (e.key === 'r' || e.key === 'R') {
        restartGame();
    }
});

document.addEventListener('keyup', (e) => {
    keys[e.key.toLowerCase()] = false;
});

// Initialize Game
function initGame() {
    player.x = 10;
    player.y = 10;
    player.direction = { x: 0, y: 0 };
    player.nextDirection = { x: 0, y: 0 };

    createWalls();
    createPellets();
    createEnemies();
    createPowerUps();
}

// Create Walls (Maze)
function createWalls() {
    walls = [];
    
    // Border walls
    for (let i = 0; i < COLS; i++) {
        walls.push({ x: i, y: 0 });
        walls.push({ x: i, y: ROWS - 1 });
    }
    for (let i = 0; i < ROWS; i++) {
        walls.push({ x: 0, y: i });
        walls.push({ x: COLS - 1, y: i });
    }

    // Internal maze walls
    const mazePattern = [
        { x: 5, y: 5, w: 10, h: 1 },
        { x: 5, y: 10, w: 10, h: 1 },
        { x: 5, y: 15, w: 10, h: 1 },
        { x: 3, y: 7, w: 1, h: 6 },
        { x: 16, y: 7, w: 1, h: 6 },
        { x: 8, y: 12, w: 4, h: 1 }
    ];

    mazePattern.forEach(wall => {
        for (let x = wall.x; x < wall.x + wall.w; x++) {
            for (let y = wall.y; y < wall.y + wall.h; y++) {
                if (x > 0 && x < COLS - 1 && y > 0 && y < ROWS - 1) {
                    walls.push({ x, y });
                }
            }
        }
    });
}

// Create Pellets
function createPellets() {
    pellets = [];
    for (let x = 1; x < COLS - 1; x++) {
        for (let y = 1; y < ROWS - 1; y++) {
            const isWall = walls.some(w => w.x === x && w.y === y);
            const isPlayer = player.x === x && player.y === y;
            if (!isWall && !isPlayer && Math.random() > 0.2) {
                pellets.push({ x, y, collected: false });
            }
        }
    }
}

// Create Power-ups
function createPowerUps() {
    powerUps = [];
    const powerUpCount = Math.min(3, Math.floor(level / 2) + 1);
    for (let i = 0; i < powerUpCount; i++) {
        let x, y, valid;
        do {
            x = Math.floor(Math.random() * (COLS - 2)) + 1;
            y = Math.floor(Math.random() * (ROWS - 2)) + 1;
            valid = !walls.some(w => w.x === x && w.y === y) &&
                    !pellets.some(p => p.x === x && p.y === y);
        } while (!valid);
        powerUps.push({ x, y, type: 'star', active: true });
    }
}

// Create Enemies
function createEnemies() {
    enemies = [];
    const enemyCount = Math.min(4, 2 + level);
    const colors = ['#ff0000', '#ff69b4', '#00ffff', '#ffa500'];

    for (let i = 0; i < enemyCount; i++) {
        let x, y, valid;
        do {
            x = Math.floor(Math.random() * (COLS - 4)) + 2;
            y = Math.floor(Math.random() * (ROWS - 4)) + 2;
            valid = !walls.some(w => w.x === x && w.y === y) &&
                    !(x === player.x && y === player.y);
        } while (!valid);

        enemies.push({
            x,
            y,
            width: GRID_SIZE,
            height: GRID_SIZE,
            speed: 0.5 + (level * 0.1),
            direction: { x: Math.random() > 0.5 ? 1 : -1, y: 0 },
            color: colors[i % colors.length],
            moveCounter: 0
        });
    }
}

// Start Game
function startGame() {
    gameState = GAME_STATE.PLAYING;
    initGame();
    updateStatus('GAME STARTED! Collect all dots!');
    gameLoop();
}

// Pause Game
function pauseGame() {
    gameState = GAME_STATE.PAUSED;
    updateStatus('PAUSED - Press SPACE to Resume');
}

// Resume Game
function resumeGame() {
    gameState = GAME_STATE.PLAYING;
    updateStatus('GAME RESUMED!');
    gameLoop();
}

// Restart Game
function restartGame() {
    score = 0;
    level = 1;
    lives = 3;
    gameState = GAME_STATE.MENU;
    updateStatus('Press SPACE to Start');
    updateUI();
    draw();
}

// Update Status Text
function updateStatus(text) {
    document.getElementById('statusText').textContent = text;
}

// Update UI
function updateUI() {
    document.getElementById('score').textContent = score;
    document.getElementById('level').textContent = level;
    document.getElementById('lives').textContent = lives;
    document.getElementById('highScore').textContent = highScore;
}

// Main Game Loop
function gameLoop() {
    if (gameState !== GAME_STATE.PLAYING) {
        if (gameState === GAME_STATE.MENU) {
            draw();
        }
        return;
    }

    update();
    draw();
    requestAnimationFrame(gameLoop);
}

// Update Game Logic
function update() {
    // Update player direction
    if (canMove(player.x + player.nextDirection.x, player.y + player.nextDirection.y)) {
        player.direction = player.nextDirection;
    }

    // Move player
    const newX = player.x + player.direction.x;
    const newY = player.y + player.direction.y;

    if (canMove(newX, newY)) {
        player.x = newX;
        player.y = newY;
    }

    // Collect pellets
    pellets.forEach(pellet => {
        if (pellet.x === player.x && pellet.y === player.y && !pellet.collected) {
            pellet.collected = true;
            score += 10;
        }
    });

    // Collect power-ups
    powerUps.forEach(powerUp => {
        if (powerUp.x === player.x && powerUp.y === player.y && powerUp.active) {
            powerUp.active = false;
            score += 50;
        }
    });

    // Update enemies
    enemies.forEach(enemy => {
        enemy.moveCounter++;
        if (enemy.moveCounter > 30 / enemy.speed) {
            enemy.moveCounter = 0;

            // Simple AI - try to move towards player
            const dx = player.x - enemy.x;
            const dy = player.y - enemy.y;

            if (Math.abs(dx) > Math.abs(dy)) {
                enemy.direction.x = dx > 0 ? 1 : -1;
                enemy.direction.y = 0;
            } else {
                enemy.direction.x = 0;
                enemy.direction.y = dy > 0 ? 1 : -1;
            }

            // Try to move
            let newEnemyX = enemy.x + enemy.direction.x;
            let newEnemyY = enemy.y + enemy.direction.y;

            if (!canMove(newEnemyX, newEnemyY)) {
                // Random direction if blocked
                const directions = [
                    { x: 1, y: 0 },
                    { x: -1, y: 0 },
                    { x: 0, y: 1 },
                    { x: 0, y: -1 }
                ];
                const validDirs = directions.filter(d => canMove(enemy.x + d.x, enemy.y + d.y));
                if (validDirs.length > 0) {
                    enemy.direction = validDirs[Math.floor(Math.random() * validDirs.length)];
                    newEnemyX = enemy.x + enemy.direction.x;
                    newEnemyY = enemy.y + enemy.direction.y;
                }
            }

            enemy.x = newEnemyX;
            enemy.y = newEnemyY;
        }

        // Check collision with player
        if (enemy.x === player.x && enemy.y === player.y) {
            lives--;
            if (lives <= 0) {
                gameOver();
            } else {
                player.x = 10;
                player.y = 10;
                updateStatus(`HIT! Lives: ${lives}`);
            }
        }
    });

    // Check level complete
    const allCollected = pellets.every(p => p.collected);
    if (allCollected) {
        levelComplete();
    }

    updateUI();
}

// Check if can move to position
function canMove(x, y) {
    if (x < 0 || x >= COLS || y < 0 || y >= ROWS) return false;
    return !walls.some(w => w.x === x && w.y === y);
}

// Level Complete
function levelComplete() {
    level++;
    score += 100;
    gameState = GAME_STATE.LEVEL_COMPLETE;
    updateStatus(`LEVEL ${level - 1} COMPLETE! Press SPACE for Next Level`);
    updateUI();

    setTimeout(() => {
        if (gameState === GAME_STATE.LEVEL_COMPLETE) {
            gameState = GAME_STATE.PLAYING;
            initGame();
            updateStatus('Level ' + level + ' - GO!');
        }
    }, 3000);
}

// Game Over
function gameOver() {
    gameState = GAME_STATE.GAME_OVER;
    if (score > highScore) {
        highScore = score;
        localStorage.setItem('pixelQuestHighScore', highScore);
    }
    updateStatus(`GAME OVER! Final Score: ${score} | Press R to Restart`);
    updateUI();
}

// Draw Game
function draw() {
    // Clear canvas
    ctx.fillStyle = '#000000';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    if (gameState === GAME_STATE.MENU) {
        drawMenu();
        return;
    }

    // Draw walls
    ctx.fillStyle = '#0099ff';
    walls.forEach(wall => {
        ctx.fillRect(wall.x * GRID_SIZE, wall.y * GRID_SIZE, GRID_SIZE, GRID_SIZE);
        ctx.strokeStyle = '#00ff00';
        ctx.lineWidth = 1;
        ctx.strokeRect(wall.x * GRID_SIZE, wall.y * GRID_SIZE, GRID_SIZE, GRID_SIZE);
    });

    // Draw pellets
    ctx.fillStyle = '#ffff99';
    pellets.forEach(pellet => {
        if (!pellet.collected) {
            ctx.fillRect(
                pellet.x * GRID_SIZE + 8,
                pellet.y * GRID_SIZE + 8,
                4,
                4
            );
        }
    });

    // Draw power-ups
    ctx.fillStyle = '#ff00ff';
    powerUps.forEach(powerUp => {
        if (powerUp.active) {
            ctx.fillRect(
                powerUp.x * GRID_SIZE + 5,
                powerUp.y * GRID_SIZE + 5,
                10,
                10
            );
        }
    });

    // Draw player
    ctx.fillStyle = player.color;
    ctx.fillRect(player.x * GRID_SIZE, player.y * GRID_SIZE, GRID_SIZE, GRID_SIZE);
    ctx.strokeStyle = '#ffff00';
    ctx.lineWidth = 2;
    ctx.strokeRect(player.x * GRID_SIZE, player.y * GRID_SIZE, GRID_SIZE, GRID_SIZE);

    // Draw enemies
    enemies.forEach(enemy => {
        ctx.fillStyle = enemy.color;
        ctx.fillRect(enemy.x * GRID_SIZE, enemy.y * GRID_SIZE, GRID_SIZE, GRID_SIZE);
        ctx.strokeStyle = '#ffffff';
        ctx.lineWidth = 1;
        ctx.strokeRect(enemy.x * GRID_SIZE, enemy.y * GRID_SIZE, GRID_SIZE, GRID_SIZE);
    });
}

// Draw Menu
function drawMenu() {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.7)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = '#ffff00';
    ctx.font = 'bold 24px Courier New';
    ctx.textAlign = 'center';
    ctx.fillText('PIXEL QUEST', canvas.width / 2, 80);

    ctx.fillStyle = '#00ff00';
    ctx.font = '16px Courier New';
    ctx.fillText('A Classic Arcade Game', canvas.width / 2, 120);

    ctx.fillStyle = '#ff00ff';
    ctx.font = 'bold 20px Courier New';
    ctx.fillText('Press SPACE to Start', canvas.width / 2, 200);

    ctx.fillStyle = '#00ffff';
    ctx.font = '14px Courier New';
    ctx.fillText('Arrow Keys or WASD to Move', canvas.width / 2, 260);
    ctx.fillText('Collect all dots to advance', canvas.width / 2, 290);
    ctx.fillText('Avoid the ghosts!', canvas.width / 2, 320);

    ctx.fillStyle = '#ffff00';
    ctx.fillText(`High Score: ${highScore}`, canvas.width / 2, 360);
}

// Initialize and start
updateUI();
draw();
