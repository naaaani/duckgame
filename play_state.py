import pygame
from game_state import GameState

class Play(GameState):

    def __init__(self, game):
        self.game = game

    def get_name(self):
        return "play"
    
    def proc_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            self.game.play_end()
    
    def update(self):
        pass