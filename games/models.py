from django.db import models
import json

class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='game_images/', null=True, blank=True)
    identifier = models.CharField(max_length=100)  # Add this field
    script_file = models.CharField(max_length=200, help_text="Path to game file in /static/code/")

    def __str__(self):
        return self.title
