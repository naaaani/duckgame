import pygame
from abstract_state import AbstractState

class GameOver(AbstractState):

    def __init__(self, game):
        
        self.game = game
        self.screen = self.game.get_screen() 

    def get_name(self):
        return "Game over"
    
    def set_score(self, score):

        self.score = score
            
        font = pygame.font.SysFont('Arial', 50)
        self.title_surface = font.render('Score: ' + str(self.score), False, (20, 20, 40,))
        (screen_width, screen_height,) = self.game.get_screen_dim()
        (title_width, title_height,) = self.title_surface.get_size()
        self.title_x = (screen_width / 2) - (title_width / 2)
        self.title_y = (screen_height / 4) - (title_height / 2)

    def activate(self):
        pygame.time.set_timer(pygame.USEREVENT, 2000)
        self.mouse_lock = True

    def deactivate(self):
        pygame.time.set_timer(pygame.USEREVENT, 0)

    def proc_event(self, event):
        
        if event.type == pygame.USEREVENT:
            self.mouse_lock = False

        if event.type == pygame.MOUSEBUTTONUP:
            if not self.mouse_lock:
                self.game.game_over_end()

    def update(self):
        
        self.screen.blit(self.title_surface, (self.title_x, self.title_y,))



