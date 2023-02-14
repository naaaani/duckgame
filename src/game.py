#!/usr/bin/env python3

import pygame
from menu_state import Menu
from play_state import Play


class Game:

    def __init__(self):

        pygame.init()
        pygame.font.init()

        self.screen_width = 800
        self.screen_height = 600

        self.create_screen()

        self.menu = Menu(self)
        self.play = Play(self)
        
        self.active_state = None
        #TODO: change back to menu state
        self.set_active_state(self.play)

    def set_active_state(self, state):

        if self.active_state is not None:
            self.active_state.deactivate()
        self.active_state = state
        self.active_state.activate()

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

if __name__ == "__main__":
    game = Game()
    game.main_loop()