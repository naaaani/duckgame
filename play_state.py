import pygame
from game_state import GameState
from duck import Duck

class Play(GameState):

    def __init__(self, game):
        self.game = game
        self.duck1 = Duck(self.game, self, 20, 5)
        self.duck2 = Duck(self.game, self, 100, 3)

    def get_name(self):
        return "play"
    
    def proc_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            self.game.play_end()
    
    def update(self):
        self.duck1.update()
        self.duck2.update()

    def activate(self):
        self.duck1.reset()
        self.duck2.reset()

