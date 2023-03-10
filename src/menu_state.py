import pygame
from pygame_button import Button
from abstract_state import AbstractState

class Menu(AbstractState):

    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    ORANGE = (255, 180, 0)

    def __init__(self, game):

        self.game = game
        self.screen = self.game.get_screen() 
        self.create_button()
        self.create_title()

    def activate(self):

        self.create_hiscore()
            
    def get_name(self):
        return "menu"

    def create_button(self):

        (width, height,) = self.game.get_screen_dim()
        button_width = width / 4
        button_height = height / 4

        style = {
            "hover_color": Menu.BLUE,
            "clicked_color": Menu.GREEN,
            "clicked_font_color": Menu.BLACK,
            "hover_font_color": Menu.ORANGE
        }
        self.button = Button(
            (0, 0, button_width, button_height), Menu.RED, self.press, text="Start", **style
        )
        self.button.rect.center = (width / 2, height / 4 * 3)

    def create_title(self):

        font = pygame.font.SysFont('Arial', 50)
        self.title_surface = font.render('Duck game', False, (20, 20, 40,))
        (screen_width, screen_height,) = self.game.get_screen_dim()
        (title_width, title_height,) = self.title_surface.get_size()
        self.title_x = (screen_width / 2) - (title_width / 2)
        self.title_y = (screen_height / 4) - (title_height / 2)

    def create_hiscore(self):

        font = pygame.font.SysFont('Arial', 50)
        self.hiscore_surface = font.render('Hiscore: ' + self.hiscore, False, (20, 20, 40,))
        (screen_width, screen_height,) = self.game.get_screen_dim()
        (hiscore_width, hiscore_height,) = self.hiscore_surface.get_size()
        self.hiscore_x = (screen_width / 2) - (hiscore_width / 2)
        self.hiscore_y = (screen_height / 2) - (hiscore_height / 2)

    def set_hiscore(self, hiscore):
        self.hiscore = str(hiscore)
    
    def proc_event(self, event):       
        self.button.check_event(event)
       
    def press(self):
        self.game.menu_start_pressed()

    def update(self):
        self.button.update(self.screen)
        self.screen.blit(self.title_surface, (self.title_x, self.title_y,))
        self.screen.blit(self.hiscore_surface, (self.hiscore_x, self.hiscore_y,))
        
