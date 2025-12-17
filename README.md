https://www.loom.com/share/4002bbb9966847f9a37ff7ac102c46c0


# 🎮 Kristijan - Tic Tac Toe SSE Code Screen

A full-stack Tic-Tac-Toe AI game built using **Django REST Framework** for the backend and **React** for the frontend.  
The AI uses the **Minimax algorithm** with difficulty levels, offering a fun and challenging experience for all players.

## Features
### 🎮 Game Features
- Single Player vs AI: Play against a computer opponent with configurable difficulty
- Four AI Difficulty Levels:
    - Easy: Random moves
    - Medium: Defensive strategy (blocks wins)
    - Hard: Minimax algorithm with alpha-beta pruning (unbeatable)
    - Expert: Monte Carlo Tree Search (advanced probabilistic AI)

- Statistics Tracking: Win/loss/draw rates, move counts, game durations
- Game State Persistence: Save and load game statistics
- Comprehensive Logging: Rotating log files with different severity levels

### 🏗️ Architecture & Design
- Strategy Pattern: Clean separation of AI algorithms
- Observer Pattern: Event-driven game state notifications
- Factory Pattern: Dynamic AI strategy creation
- Repository Pattern: Statistics persistence
- Immutability: Move objects are immutable
- Type Hints: Full Python type annotations

### 🔧 Technical Features
- Minimax with Alpha-Beta Pruning: Optimal move selection with performance optimizations
- Transposition Tables: Memoization for board state evaluations
- Move Ordering: Heuristic-based move ordering for better pruning
- Board State Hashing: Efficient board comparison and caching
- Configurable Board Size: Extensible for different board dimensions
- Comprehensive Error Handling: Graceful degradation and user-friendly error messages

## Tech Stack
### Frontend
- React JS 

### Backend
- Django REST Framework  
- Python  


## Folder Structure
```
tic-tac-toe-ai/
│
├── backend/                        # Django Backend
│   ├── game/                       # Game API
│   │   ├── logic/tic_tac_toe.py    # Main AI Game logic
│   │   └── ...
│   ├── manage.py
│   └── ...
│
└── frontend/                       # React Frontend
    ├── src/
    ├── public/
    └── package.json
```

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/KrisitijanDev/tic-tac-toe-ai.git
cd tic-tac-toe-ai
```

### 2. Backend Setup
```bash
cd backend
python manage.py migrate
python manage.py runserver
```
Backend runs by default on `http://127.0.0.1:8000/`

### 3. Frontend Setup
```bash
cd ../frontend
npm install
npm start
```
Frontend runs by default on `http://localhost:3000/`
