import pygame
import random
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
        self.create_countdown()
        self.create_score()

    def get_name(self):
        return "play"
    
    def proc_event(self, event):

        if event.type == pygame.MOUSEBUTTONUP:
            self.shoot(event.pos[0], event.pos[1])
        
        if event.type == pygame.MOUSEMOTION:
            (self.ch_x, self.ch_y,) = event.pos

        if event.type == pygame.WINDOWLEAVE:
            self.hide_crosshair()
        
        if event.type == pygame.USEREVENT:
            self.timer = self.timer - 1
            if self.timer == -1:
                self.game.play_end()
                return
            self.render_countdown_surface()

    def update(self):
        
        for duck in self.ducks:
            duck.update()

        self.update_crosshair()
        self.update_countdown()
        self.update_score()

    def activate(self):
        
        for duck in self.ducks:
            duck.reset()
        
        self.hide_crosshair()

        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.timer = 30
        self.render_countdown_surface()
        self.score = 0
        self.render_score_surface()

    def deactivate(self):

        pygame.time.set_timer(pygame.USEREVENT, 0)

    def hide_crosshair(self):

        self.ch_x = -self.crosshair_w
        self.ch_y = -self.crosshair_h

    def duck_hit(self, id):
        
        duck = self.ducks[id]
        self.score += duck.get_score()
        self.render_score_surface()

    def duck_over(self, id):

        duck = self.create_duck(id)
        self.ducks[id] = duck
        
    def create_duck(self, id):

        y = (self.screen_height / 5) * (id + 0.5)

        speed = random.randrange(1, 7)
        if random.randrange(1, 3) == 1:
            speed = -speed
        
        duck = Duck(id, self.game, self, y, speed)

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
    
    def create_countdown(self):

        self.timer = 30
        self.render_countdown_surface()
        (screen_width, screen_height,) = self.game.get_screen_dim()
        (countdown_width, countdown_height,) = self.countdown_surface.get_size()
        self.countdown_x = screen_width - (countdown_width * 1.5)
        self.countdown_y = 0

    def update_countdown(self):
        
        self.screen.blit(self.countdown_surface, (self.countdown_x, self.countdown_y,))

    def render_countdown_surface(self):

        font = pygame.font.SysFont('Arial', 30)
        self.countdown_surface = font.render(str(self.timer), False, (20, 20, 40,))
    
    def create_score(self):
        
        self.score = 0
        self.render_score_surface()
        (screen_width, screen_height,) = self.game.get_screen_dim()
        (score_width, score_height,) = self.score_surface.get_size()
        self.score_x = score_width / 2
        self.score_y = 0

    def render_score_surface(self):

        font = pygame.font.SysFont('Arial', 30)
        self.score_surface = font.render(str(self.score), False, (20, 20, 40,))

    def update_score(self):
        
        self.screen.blit(self.score_surface, (self.score_x, self.score_y,))
