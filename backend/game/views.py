# game/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .logic.tic_tac_toe import player_move, ai_move, check_winner, is_full

@csrf_exempt
def make_move(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            board = data.get("board")
            move = data.get("move")        # [x, y]
            difficulty = data.get("difficulty", "hard")
            player_first = data.get("player_first", True)

            # Player move (if player clicked a cell)
            if move:
                x, y = move
                if board[x][y] == ' ':
                    board[x][y] = 'X'

            # Check winner after player move
            winner = check_winner(board)
            if winner or is_full(board):
                return JsonResponse({
                    "board": board,
                    "winner": winner if winner else "Draw"
                })

            # AI move (if game not over)
            board = ai_move(board, difficulty)

            # Check winner after AI move
            winner = check_winner(board)
            if not winner and is_full(board):
                winner = "Draw"

            return JsonResponse({
                "board": board,
                "winner": winner
            })

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)
