#!/usr/bin/env python3

import pygame
from menu import Menu
from play import Play


class Game:

    def __init__(self):

        pygame.init()

        self.screen_width = 640
        self.screen_height = 480

        self.create_screen()

        self.menu = Menu(self)
        self.play = Play(self)

        self.set_mode("menu")

    def set_mode(self, mode):        
        self.mode = mode
        print(f"---- mode: {self.mode}")

    def create_screen(self):

        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height,))
        pygame.display.flip()

    def get_screen(self):
        return self.screen
    
    def get_screen_dim(self):
        return (self.screen_width, self.screen_height,)

    def main_loop(self):

        running = True
        while running:
            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.set_mode("quit")

                if self.mode == "menu":
                    self.menu.proc_event(event)
                elif self.mode == "play":
                    self.play.proc_event(event)
                elif self.mode == "quit":
                    running = False
                else:
                    assert("invalid mode")

                print(event)

            pygame.display.update()



if __name__ == "__main__":
    game = Game()
    game.main_loop()