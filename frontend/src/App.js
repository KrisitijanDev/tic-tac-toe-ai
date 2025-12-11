import React, { useState } from "react";
import "./App.css";

function App() {
  const emptyBoard = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
  ];

  const [board, setBoard] = useState(emptyBoard);
  const [gameOver, setGameOver] = useState(false);
  const [winner, setWinner] = useState(null);
  const [difficulty, setDifficulty] = useState("medium");

  const handleClick = async (r, c) => {
    if (gameOver || board[r][c] !== " ") return;

    const newBoard = board.map((row) => [...row]);
    newBoard[r][c] = "X";
    setBoard(newBoard);

    const res = await fetch("http://127.0.0.1:8000/game/move/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        board: newBoard,
        move: [r, c],
        difficulty: difficulty,
        player_first: true,
      }),
    });

    const data = await res.json();
    setBoard(data.board);
    setWinner(data.winner);
    if (data.winner) setGameOver(true);
  };

  const resetGame = () => {
    setBoard(emptyBoard);
    setGameOver(false);
    setWinner(null);
  };

  return (
    <div className="app">
      <h1>🤖 Tic Tac Toe AI</h1>

      <div className="difficulty">
        <label>Difficulty:</label>
        <select
          value={difficulty}
          onChange={(e) => setDifficulty(e.target.value)}
        >
          <option value="easy">Easy</option>
          <option value="medium">Medium</option>
          <option value="hard">Hard</option>
        </select>
      </div>

      <div className="board">
        {board.map((row, r) => (
          <div key={r} className="row">
            {row.map((cell, c) => (
              <button
                key={c}
                className="cell"
                onClick={() => handleClick(r, c)}
              >
                {cell}
              </button>
            ))}
          </div>
        ))}
      </div>

      {winner && (
  <h2>
    {winner === "Draw"
      ? "😐 It's a Draw!"
      : winner === "X"
      ? "🎉 You Win!"
      : "💻 AI Wins!"}
  </h2>
)}

      <button className="reset-btn" onClick={resetGame}>
        Restart
      </button>
    </div>
  );
}

export default App;
