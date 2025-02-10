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
    """Handles a move request"""
    if request.method == "POST":
        data = json.loads(request.body)
        game = Game.objects.get(id=game_id)
        index = data.get("index")
        player = data.get("player")

        if game.make_move(index, player):
            return JsonResponse({"message": "Move made!", "board": game.board, "winner": game.winner})
        return JsonResponse({"message": "Invalid move"}, status=400)
    
def game_page(request):
    return render(request, "index.html")
# Create your views here.
