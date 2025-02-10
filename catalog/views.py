from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Game

@csrf_exempt
def create_game(request):
    """Creates a new game instance"""
    if request.method == "POST":
        data = json.loads(request.body)
        game = Game.objects.create(
            board=[""] * 9,
            player_x=data.get("player_x"),
            player_o=data.get("player_o")
        )
        return JsonResponse({"game_id": game.id, "message": "Game created!"})

@csrf_exempt
def make_move(request, game_id):
    """Handles a player's move"""
    if request.method == "POST":
        data = json.loads(request.body)
        index = data.get("index")

        try:
            game = Game.objects.get(id=game_id)
        except Game.DoesNotExist:
            return JsonResponse({"message": "Game not found"}, status=404)

        if not game.is_active:
            return JsonResponse({"message": "Game is over"}, status=400)

        if game.board[index] != "":  # Prevent overwriting moves
            return JsonResponse({"message": "Invalid move, cell occupied"}, status=400)

        # Apply the move
        game.board[index] = game.current_turn
        game.current_turn = "O" if game.current_turn == "X" else "X"
        
        winner = game.check_winner()
        game.save()

        return JsonResponse({
            "message": "Move made!",
            "board": game.board,
            "current_turn": game.current_turn,
            "winner": winner
        })

    return JsonResponse({"message": "Invalid request"}, status=400)

def game_page(request):
    return render(request, "index.html")
# Create your views here.
