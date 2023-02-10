import pygame
from game_state import GameState
from duck import Duck

class Play(GameState):

    def __init__(self, game):
        self.game = game
        self.ducks = []
        for index in range(5):
            duck = self.create_duck(index)
            self.ducks.append(duck)

    def get_name(self):
        return "play"
    
    def proc_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            self.game.play_end()
    
    def update(self):
        
        for duck in self.ducks:
            duck.update()

    def activate(self):
        
        for duck in self.ducks:
            duck.reset()

    def duck_over(self, id):
        duck = self.create_duck(id)
        self.ducks[id] = duck
        
    def create_duck(self, id):

        (_, screen_height,) = self.game.get_screen_dim()
        y = (screen_height / 5) * (id + 0.5)
        speed = id + 1
        duck = Duck(id, self.game, self, y, speed)

        print(f"Duck {id}")

        return duck

