import pygame

class Duck:

    def __init__(self, game, play, y, speed):
        
        self.game = game
        self.screen = self.game.get_screen() 
        self.play = play
        self.y = y
        self.speed = speed

        self.duck_image = pygame.image.load("duck1.png")
        (orig_width, orig_height,) = self.duck_image.get_size()
        (screen_width, screen_height,) = self.game.get_screen_dim()
        duck_height = screen_height / 8
        shrink_width = duck_height / orig_height
        duck_width = orig_width * shrink_width

        self.duck_image = pygame.transform.scale(self.duck_image, (duck_width, duck_height,))

        self.reset()
        
    def reset(self):
        self.x = 0

    def update(self):
        self.screen.blit(self.duck_image, (self.x, self.y,))
        self.x += self.speed

