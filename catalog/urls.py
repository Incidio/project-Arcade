from django.urls import path
#from . import views
from .views import game_page, create_game, make_move

urlpatterns = [
    path("", game_page, name="game_page"),
    path("create/", create_game, name="create_game"),
    path("move/<int:game_id>/", make_move, name="make_move"),
    path('memory/', views.memory, name='memory'),
]
