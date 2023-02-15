#!/usr/bin/env python3

import pygame
from menu_state import Menu
from play_state import Play
from game_over_state import GameOver


class Game:

    def __init__(self):

        pygame.init()
        pygame.font.init()

        self.screen_width = 800
        self.screen_height = 600

        self.create_screen()

        self.menu = Menu(self)
        self.play = Play(self)
        self.game_over = GameOver(self)

        self.hiscore_fnam = "hiscore.txt"
        self.last_score = 0
        self.load_hiscore()

        self.active_state = None
        self.set_active_state(self.menu)

    def set_active_state(self, state):

        if self.active_state is not None:
            self.active_state.deactivate()
        self.active_state = state
        self.active_state.activate()

    def create_screen(self):

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height,))
        pygame.display.flip()

    def get_screen(self):
        return self.screen
    
    def get_screen_dim(self):
        return (self.screen_width, self.screen_height,)

    def menu_start_pressed(self):
        self.set_active_state(self.play)

    def play_end(self):
        
        self.set_active_state(self.game_over)
        self.last_score = self.play.get_score()
        self.game_over.set_score(self.last_score)

        if self.last_score > self.hiscore:
            self.set_hiscore(self.last_score)
            self.save_hiscore()
    
    def game_over_end(self):
        self.set_active_state(self.menu)

    def main_loop(self):

        clock = pygame.time.Clock()
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                self.active_state.proc_event(event)
                #print(event)
        
            pygame.display.get_surface().fill((200,200,255,))
            self.active_state.update()
            pygame.display.update()     
            clock.tick(60)
    
    def set_hiscore(self, hiscore):

        self.hiscore = hiscore
        self.menu.set_hiscore(hiscore)
  
    def load_hiscore(self):
        
        try:
            with open(self.hiscore_fnam, 'r') as f:
                hi = int(f.read())
                self.set_hiscore(hi)
        except FileNotFoundError:
            self.set_hiscore(0)
        except ValueError:
            self.set_hiscore(0)

    def save_hiscore(self):

        with open(self.hiscore_fnam, 'w') as f:
            f.write(str(self.hiscore))

if __name__ == "__main__":
    game = Game()
    game.main_loop()