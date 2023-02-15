import pygame

class Flare:

    def __init__(self, id, game, play, x, y):
        
        self.game = game
        self.screen = self.game.get_screen()
        self.play = play
        self.x = x
        self.y = y
        self.id = id

        (self.screen_width, self.screen_height,) = self.game.get_screen_dim()

        self.init_image()
        self.timer = 25

    def init_image(self):

        self.image = pygame.image.load("../images/dot.png")
        (orig_width, orig_height,) = self.image.get_size()
        self.image_height = self.screen_height / 20
        shrink_width = self.image_height / orig_height
        self.image_width = orig_width * shrink_width
        
        self.image = pygame.transform.scale(self.image, (self.image_width, self.image_height,))

        offset_x = 0.5 * self.image_width
        offset_y = 0.5 * self.image_height        
        self.pos = (self.x - offset_x, self.y - offset_y,)

    def update(self):

        if self.timer == 0:
            self.play.flare_over(self.id)
            return
        
        self.screen.blit(self.image, self.pos)
        self.timer -= 1

