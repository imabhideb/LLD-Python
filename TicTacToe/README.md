# Tic-Tac-Toe Game

A Python implementation of the classic Tic-Tac-Toe game using **Low-Level System Design (LLD) principles** and multiple **Design Patterns**.

## 🚀 Features
- **Singleton Pattern**: Ensures a single instance of the Game Controller.
- **Factory Pattern**: Creates Player instances dynamically.
- **Observer Pattern**: Notifies players of board state changes.
- **Strategy Pattern**: Encapsulates move validation and win condition checking.
- **Modular Design**: Clean separation of concerns for easy extension.

---

## 🛠 Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/tic-tac-toe.git
cd tic-tac-toe
```

### 2️⃣ Run the Game
```bash
python Main.py
```

---

## 🎮 How to Play
1. The game starts with an **empty 3x3 board**.
2. **Player X goes first**, followed by Player O.
3. Players take turns entering **row and column (0-2)** to place their symbol.
4. The game continues until **a player wins or the game is a draw**.

---

## 🏗 Design Patterns Used
| Pattern       | Purpose |
|--------------|------------------------------|
| **Singleton** | Ensures only one `GameController` instance exists. |
| **Factory**   | Creates Player instances dynamically. |
| **Observer**  | Notifies players when board state changes. |
| **Strategy**  | Defines move validation & win conditions. |

---

## 🎯 Future Enhancements
✅ **Add AI Player (Minimax Algorithm)** 🤖  
✅ **Allow users to play against AI or another human** 🎭

---