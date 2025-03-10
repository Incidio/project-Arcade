from django.shortcuts import render, get_object_or_404
from .models import Game

def home(request):
    games = Game.objects.all()
    return render(request, "games/home.html", {"games": games})

def play_game(request, identifier):
    game = get_object_or_404(Game, identifier=identifier)
    return render(request, "games/play.html", {"game": game})





# Create your views here.
