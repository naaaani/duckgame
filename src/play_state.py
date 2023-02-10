import pygame
from game_state import GameState
from duck import Duck

class Play(GameState):

    def __init__(self, game):

        self.game = game
        (self.screen_width, self.screen_height,) = self.game.get_screen_dim()
        self.screen = self.game.get_screen() 

        self.ducks = []
        for index in range(5):
            duck = self.create_duck(index)
            self.ducks.append(duck)

        self.create_crosshair()

    def get_name(self):
        return "play"
    
    def proc_event(self, event):

        if event.type == pygame.MOUSEBUTTONUP:
            #self.game.play_end()
            self.shoot(event.pos[0], event.pos[1])
        
        if event.type == pygame.MOUSEMOTION:
            (self.ch_x, self.ch_y,) = event.pos

        if event.type == pygame.WINDOWLEAVE:
            self.hide_crosshair()

    
    def update(self):
        
        for duck in self.ducks:
            duck.update()

        self.update_crosshair()

    def activate(self):
        
        for duck in self.ducks:
            duck.reset()
        
        self.hide_crosshair()

    def hide_crosshair(self):

        self.ch_x = -self.crosshair_w
        self.ch_y = -self.crosshair_h

    def duck_over(self, id):

        duck = self.create_duck(id)
        self.ducks[id] = duck
        
    def create_duck(self, id):

        y = (self.screen_height / 5) * (id + 0.5)
        speed = id + 1
        duck = Duck(id, self.game, self, y, speed)

        print(f"Duck {id}")

        return duck
    
    def create_crosshair(self):
        
        self.crosshair_image = pygame.image.load("../images/crosshair.png")
        (orig_width, orig_height,) = self.crosshair_image.get_size()
        self.crosshair_h = self.screen_height / 5
        shrink_factor = self.crosshair_h / orig_height
        self.crosshair_w = orig_width * shrink_factor
        self.crosshair_image = pygame.transform.scale(self.crosshair_image, (self.crosshair_w, self.crosshair_h,))
        
        self.ch_offset_x = self.crosshair_w / 2
        self.ch_offset_y = self.crosshair_h / 2

    def update_crosshair(self):
        
        self.screen.blit(self.crosshair_image, (self.ch_x - self.ch_offset_x, self.ch_y - self.ch_offset_y,))

    def shoot(self, x, y):

        for duck in self.ducks:
            duck.shoot(x, y)