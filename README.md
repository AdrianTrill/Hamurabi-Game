---

# **Hamurabi - Ancient Kingdom Simulation Game**

### Overview

**Hamurabi** is a Python-based strategic simulation game that challenges players to manage resources effectively as they rule over an ancient kingdom. As the ruler, you must balance grain reserves, land acquisition, and population growth while facing random events like harvest fluctuations and rat infestations. Your objective is to keep your people alive and prosperous over several years, making crucial decisions about feeding your population, planting crops, and buying or selling land.

### Key Features

- **Resource Management**: Allocate grain to feed your people and plant crops while managing land acquisitions and sales.
- **Random Events**: Randomized harvest rates, rat infestations, and fluctuating land prices keep the gameplay unpredictable.
- **Multiple Endings**: The game offers different outcomes based on your decisions, from population prosperity to starvation endings.
- **Replayability**: Random elements ensure no two games are alike, enhancing replay value.
  
---

## **Project Structure**

📁 **src**  
&nbsp;&nbsp;&nbsp;&nbsp; ├── **game.py** - Core game logic, including resource management and random events.  
&nbsp;&nbsp;&nbsp;&nbsp; ├── **exceptions.py** - Custom exceptions for game errors.  
&nbsp;&nbsp;&nbsp;&nbsp; ├── **start.py** - Main entry point to start the game.  
&nbsp;&nbsp;&nbsp;&nbsp; ├── **UI.py** - User interface (CLI) for the game, handles user interactions.  
&nbsp;&nbsp;&nbsp;&nbsp; └── **tests.py** - Unit tests for game mechanics and UI.

---

## **How to Play**

1. **Start the Game**: Run the `start.py` file.
2. **Make Decisions**: Each year, decide how much land to buy/sell, how much grain to use for feeding your population, and how much land to plant with crops.
3. **Survive**: Keep your population well-fed and prosperous while managing resources and reacting to random events.

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

Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to submit an issue or a pull request.

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
