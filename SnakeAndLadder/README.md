# 🐍🎲 Snake and Ladder - Low Level Design (LLD) in Python

This project implements the **Snake and Ladder** game using **Low-Level Design (LLD) principles** in Python. The program follows various **design patterns** to create a scalable and maintainable solution.

## 🚀 Features
- **Board Initialization**: A single game board is created (Singleton Pattern)
- **Players**: Multiple players can play the game
- **Snakes and Ladders**: Randomly placed obstacles to increase difficulty
- **Dice Roll**: A dice determines movement (Strategy Pattern)
- **Game Logic**: Players move based on dice rolls, handling snakes and ladders
- **Turn Notification**: Players are notified of their moves (Observer Pattern)

---

## 📐 Design Patterns Used

| Design Pattern    | Purpose |
|-------------------|---------|
| **Singleton**     | Ensures only one instance of the `Board` class exists |
| **Factory**       | Creates snakes and ladders dynamically using `ObstacleFactory` |
| **Observer**      | Notifies players about their turns |
| **Strategy**      | Allows different dice rolling strategies (Normal/Loaded Dice) |
| **Command**       | Encapsulates player moves in the `MoveCommand` class |

---

## 🔧 How to Run
1. **Clone the repository**
   ```sh
   git clone https://github.com/LLD-Python/SnakeAndLadder.git
   cd SnakeAndLadder
   ```

2. **Run the game**
   ```sh
   python Main.py
   ```

---

## 📌 Future Enhancements
- Add a **GUI version** of the game using `Tkinter` or `Pygame`
- Implement **Multiplayer Online Mode**
- Add **Custom Dice Strategies**

---

## 🤝 Contributing
Pull requests are welcome! Feel free to contribute by fixing issues or adding new features.

```sh
git checkout -b feature-branch
# Make your changes
git commit -m "Added new feature"
git push origin feature-branch
```

---

## 📧 Contact
For any queries, reach out via **[imabhijitdeb@gmail.com](mailto:imabhijitdeb@gmail.com)** or open an issue in the repo.

