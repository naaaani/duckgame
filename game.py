#!/usr/bin/env python3

import pygame
from menu_state import Menu
from play_state import Play


class Game:

    def __init__(self):

        pygame.init()

        self.screen_width = 800
        self.screen_height = 600

        self.create_screen()

        self.menu = Menu(self)
        self.play = Play(self)

        self.set_active_state(self.menu)

    def set_active_state(self, state):        
        self.active_state = state
        print(f"---- active: {self.active_state.get_name()}")

    def create_screen(self):

        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height,))
        pygame.display.flip()

    def get_screen(self):
        return self.screen
    
    def get_screen_dim(self):
        return (self.screen_width, self.screen_height,)

    def menu_start_pressed(self):
        self.set_active_state(self.play)

    def play_end(self):
        self.set_active_state(self.menu)

    def main_loop(self):

        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                self.active_state.proc_event(event)
                print(event)
        
            pygame.display.get_surface().fill((0,0,0,))
            self.active_state.update()
            pygame.display.update()     

if __name__ == "__main__":
    game = Game()
    game.main_loop()