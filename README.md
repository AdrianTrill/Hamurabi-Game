### Updated README without YAML issues:

---

# **Hamurabi - Ancient Kingdom Simulation Game**

### Overview

**Hamurabi** is a Python-based strategic simulation game where you manage resources as the ruler of an ancient kingdom. You must make decisions about feeding your people, planting crops, and managing land while handling random events like harvest rates and rat infestations. The goal is to keep your population thriving over multiple years.

### Key Features

- **Resource Management**: Make strategic decisions about how much grain to allocate, what land to buy or sell, and how much to plant each year.
- **Random Events**: Unpredictable events, including harvest changes, rat infestations, and fluctuating land prices, keep gameplay dynamic.
- **Multiple Endings**: Depending on your decisions, you will either lead your people to prosperity or see them starve.
- **Replay Value**: Random elements make each playthrough different, enhancing replayability.

---

## **Project Structure**

```bash
📁 src
   ├── game.py             # Core game logic, including resource management and random events.
   ├── exceptions.py       # Custom exceptions for game errors.
   ├── start.py            # Main entry point to start the game.
   ├── UI.py               # User interface (CLI) for interacting with the game.
   └── tests.py            # Unit tests for game mechanics and UI.
```

---

## **How to Play**

1. **Start the Game**: Run the `start.py` file.
2. **Make Decisions**: Decide how many acres to buy/sell, how much grain to feed your people, and how much land to plant.
3. **Survive**: Maintain your population and resources while managing random events each year.

---

## **Installation**

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-repo/hamurabi-game.git
   ```

2. Install the necessary dependencies (if any):  
   ```bash
   pip install -r requirements.txt
   ```

3. Run the game:  
   ```bash
   python src/start.py
   ```

---

## **Contributing**

Contributions are welcome! If you find any bugs or have suggestions, feel free to submit an issue or pull request.

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
