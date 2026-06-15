# 🚀 Space Defenders

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green)
![License](https://img.shields.io/badge/License-MIT-red)

A simple arcade-style **space shooter game** built with **Python** and **Pygame**. Control your spaceship, automatically fire bullets, destroy incoming monsters, and survive as long as possible while trying to beat your high score.

---

## 🎮 Features

- 🚀 Player-controlled spaceship
- 👾 Randomly spawning enemies
- 🔫 Automatic shooting system
- ❤️ Three lives system
- 📈 Score counter
- 🏆 High score saving using `highscore.txt`
- 🔄 Restart game without closing the application
- 💥 Collision detection
- ⚡ Smooth gameplay at 60 FPS

---

## 📸 Gameplay

### Player
- Move left and right to avoid enemies.
- Bullets are fired automatically.

### Enemies
- Monsters spawn from the top of the screen.
- Destroy them before they reach the bottom.

### Lives
- Start with **3 lives**.
- Lose one life each time an enemy reaches the bottom.
- Game ends when all lives are lost.

---

## 🎮 Controls

| Key | Action |
|------|--------|
| ← Left Arrow | Move Left |
| → Right Arrow | Move Right |
| R | Restart After Game Over |
| X | Close Window |

---

## 🛠 Technologies Used

- Python 3
- Pygame
- Random Module
- File Handling

---

## 📂 Project Structure

```text
Space_Defenders/
│
├── space_defender_game.py
├── highscore.txt
│
├── assets/
│   ├── ufo.png
│   ├── ufo (1).png
│   ├── monster.png
│   └── bullet.png
│
└── README.md
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/Space-Defenders.git
```

### Move into the project directory

```bash
cd Space-Defenders
```

### Install Pygame

```bash
pip install pygame
```

### Run the game

```bash
python space_defender_game.py
```

---

## 🏆 Scoring System

- Destroying an enemy gives **+1 point**.
- High scores are automatically stored in:

```text
highscore.txt
```

Your best score is saved even after closing the game.

---

## ⚙️ Game Mechanics

### Enemy Spawn System
- Enemies spawn periodically.
- Minimum spacing between enemies prevents overlap.

### Shooting System
- Bullets are fired automatically.
- Fire rate is controlled using a delay timer.

### Collision Detection
- Bullets destroy enemies on contact.
- Enemies reaching the bottom remove one life.

### Game Over
When all three lives are lost:

- The game displays **GAME OVER**
- Press **R** to restart
- High score is saved automatically

---

## 🔮 Future Improvements

- Add player-controlled shooting
- Multiple enemy types
- Increasing difficulty levels
- Sound effects and background music
- Power-ups and shields
- Boss enemies
- Explosion animations
- Pause menu
- Start screen
- Different spaceship skins

---

## 🎯 Purpose

This project was created to practice:

- Python Programming
- Pygame Development
- Collision Detection
- Game Loops
- File Handling
- Object Management
- Basic Game Design

---

## 👨‍💻 Author

**Harshith Dupam**

- Chemical Engineering Student
- Python Developer
- Aspiring Software Engineer
- Game Developer

---

## ⭐ Support

If you enjoyed this project, consider giving the repository a **star ⭐**.

---

## 📜 License

This project is open-source and available under the **MIT License**.
