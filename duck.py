import pygame

class Duck:

    def __init__(self, id, game, play, y, speed):

        self.id = id
        self.game = game
        self.screen = self.game.get_screen() 
        self.play = play
        (self.screen_width, self.screen_height,) = self.game.get_screen_dim()

        self.y = y
        self.speed = self.screen_width * speed / 1000

        self.duck_image = pygame.image.load("duck1.png")
        (orig_width, orig_height,) = self.duck_image.get_size()
        duck_height = self.screen_height / 8
        shrink_width = duck_height / orig_height
        duck_width = orig_width * shrink_width
        self.starting_x = -duck_width

        self.duck_image = pygame.transform.scale(self.duck_image, (duck_width, duck_height,))

        self.reset()

    def reset(self):
        self.x = self.starting_x

    def update(self):

        if self.x > self.screen_width:
            self.play.duck_over(self.id)
            return
                
        self.screen.blit(self.duck_image, (self.x, self.y,))
        self.x += self.speed
