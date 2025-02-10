from django.db import models

class Game(models.Model):
    board = models.JSONField(default=list)  # 3x3 board stored as a list
    player_x = models.CharField(max_length=50)  # Player X username or ID
    player_o = models.CharField(max_length=50)  # Player O username or ID
    current_turn = models.CharField(max_length=1, default="X")  # "X" or "O"
    winner = models.CharField(max_length=1, blank=True, null=True)  # "X", "O", or "draw"
    is_active = models.BooleanField(default=True)

    def check_winner(self):
        """Check if there's a winner"""
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]             # Diagonals
        ]

        for condition in win_conditions:
            if (self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] and 
                self.board[condition[0]] in ["X", "O"]):
                self.winner = self.board[condition[0]]
                self.is_active = False
                return self.winner

        if all(cell in ["X", "O"] for cell in self.board):
            self.winner = "draw"
            self.is_active = False
            return "draw"

        return None

    def make_move(self, index, player):
        """Process a move"""
        if self.board[index] == "" and self.is_active and player == self.current_turn:
            self.board[index] = player
            self.current_turn = "O" if player == "X" else "X"
            self.check_winner()
            self.save()
            return True
        return False