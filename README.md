# 🎮 Tic-Tac-Toe-Python-GUI

A modern and interactive **Tic Tac Toe game built with Python and Tkinter**.  
The project features an attractive graphical interface, AI opponent with multiple difficulty levels, Light/Dark themes, score tracking, win-rate statistics, and persistent game history.

---

## ✨ Features

- 🎮 Interactive Tic Tac Toe gameplay
- 🖥️ Graphical User Interface using Tkinter
- ❌ Player X vs 🤖 Computer O
- 🏆 Automatic winner detection
- 😐 Automatic draw detection
- 🟢 Winning combination highlighting
- 🤖 AI opponent
- 🎯 Three AI difficulty levels:
  - Easy
  - Medium
  - Hard
- 🎨 Light Theme
- 🌙 Dark Theme
- 📊 Live score tracking
- 🏆 Win-rate calculation
- 🎮 Total games counter
- 📜 Persistent game history
- 💾 Game history stored in JSON
- 🔄 Restart Game functionality
- 🗑️ Reset Scores functionality
- 🎨 Modern and colorful interface
- 💻 Beginner-friendly Python project

---

## 🛠️ Technologies Used

- **Python 3**
- **Tkinter**
- **JSON**
- **Object-Oriented Programming**
- **GUI Programming**

---

## 📂 Project Structure

```text
Tic-Tac-Toe-Python-GUI/
│
├── main.py
├── gui.py
├── game.py
├── ai.py
├── scores.py
├── history.py
├── config.py
├── game_history.json
├── scores.json
├── test_game.py
├── requirements.txt
└── README.md

📄 File Description
File	Description
main.py	Starts the Tic Tac Toe application
gui.py	Handles the complete Tkinter graphical interface
game.py	Contains the core Tic Tac Toe game logic
ai.py	Implements the computer opponent and difficulty levels
scores.py	Manages scores, total games, and win rate
history.py	Manages game history
config.py	Stores window, font, and theme configuration
game_history.json	Stores previous game records
scores.json	Stores persistent game scores
test_game.py	Contains game logic tests
requirements.txt	Project dependency information
🎯 How to Play
Run the application using:
python main.py
Player X starts the game.
Click any empty cell to place X.
The computer plays as O.
Select the desired AI difficulty:
Easy
Medium
Hard
Choose between:
☀️ Light Theme
🌙 Dark Theme
The first player to get three symbols in a row wins.
If all cells are filled without a winner, the game ends in a draw.
Click 🔄 Restart Game to start a new game.
Use 🗑️ Reset Scores to clear the score statistics.
🤖 AI Difficulty Levels

The game provides three different AI difficulty levels:

🟢 Easy

The computer provides a basic challenge and is suitable for beginners.

🟡 Medium

Provides a more challenging gameplay experience.

🔴 Hard

Provides the most challenging AI gameplay experience.

🎨 Theme System

The game includes two visual themes:

☀️ Light Theme

A bright and colorful interface designed for comfortable daytime use.

🌙 Dark Theme

A darker interface designed for a modern appearance and comfortable viewing.

The theme can be changed directly from the Theme selector while playing.

📊 Score Statistics

The game keeps track of:

❌ Player X wins
⭕ Computer O wins
😐 Draws
🎮 Total games
🏆 Player win rate

Example:

❌ X: 5
⭕ O: 3
😐 Draws: 2
🎮 Games: 10
🏆 Win Rate: 50.0%
📜 Game History

Completed games are stored in:

game_history.json

Each game record contains information such as:

{
    "date": "2026-08-23 17:50:19",
    "result": "X",
    "difficulty": "Easy",
    "theme": "LIGHT"
}

This allows the project to maintain a history of completed games.

📸 Project Preview

🧠 Learning Outcomes

Through this project, I practiced and improved my understanding of:

Python programming
Object-Oriented Programming
Tkinter GUI development
Event handling
Classes and objects
Lists and nested lists
Conditional statements
Loops
Game logic implementation
Winner and draw detection
AI-based gameplay
GUI state management
File handling
JSON data storage
Persistent data management
Theme management
Score and statistics tracking

🔮 Future Improvements

Possible future improvements include:

👥 Two-player local multiplayer mode
🌐 Online multiplayer
🏆 Leaderboard system
🔊 Sound effects
🎵 Background music
🎨 More customizable themes
🧠 More advanced AI
📈 Detailed statistics dashboard
📜 GUI-based game history viewer

👩‍💻 Developer

Harpreet Kaur

Made with ❤️ using Python and Tkinter.