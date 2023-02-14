import pygame


class Duck:

    ST_FLY = 1
    ST_FALL = 2
    ST_OVER = 3

    def __init__(self, id, game, play, y, speed):

        self.state = Duck.ST_FLY
        self.id = id
        self.game = game
        self.screen = self.game.get_screen()
        self.play = play
        (self.screen_width, self.screen_height,) = self.game.get_screen_dim()

        self.y = y
        self.speed = self.screen_width * speed / 1000
        
        self.init_image()
        self.init_pos()

        self.duck_image = pygame.transform.scale(self.duck_image, (self.duck_width, self.duck_height,))
        self.fall_image = pygame.transform.scale(self.fall_image, (self.duck_height, self.duck_width,))

        self.offset_x = self.duck_width / 2
        self.offset_y = self.duck_height / 2

        self.reset()


    def init_image(self):

        self.duck_image = pygame.image.load("../images/duck1.png")
        (orig_width, orig_height,) = self.duck_image.get_size()
        self.duck_height = self.screen_height / 6
        shrink_width = self.duck_height / orig_height
        self.duck_width = orig_width * shrink_width

    def init_pos(self):

        if self.speed < 0:
            self.starting_x = self.screen_width + (self.duck_width / 2)
            self.duck_image = pygame.transform.flip(
            self.duck_image, flip_x=True, flip_y=False)
            self.fall_image = pygame.transform.rotate(self.duck_image, 90)
        else:
            self.starting_x = -self.duck_width / 2
            self.fall_image = pygame.transform.rotate(self.duck_image, -90)

        self.fly_ending_x = self.screen_width + (self.duck_width / 2)
        self.fall_ending_y = self.screen_height + (self.duck_width / 2)

    def reset(self):
        self.x = self.starting_x

    def update(self):

        if self.state == Duck.ST_FLY:
            self.update_fly()
        elif self.state == Duck.ST_FALL:
            self.update_fall()

    def update_fly(self):

        if self.x > self.fly_ending_x:
            self.state = Duck.ST_OVER        
            self.play.duck_over(self.id)
            return
                
        self.screen.blit(self.duck_image, (self.x - self.offset_x, self.y - self.offset_y,))
        
        self.x += self.speed

    def update_fall(self):
        
        if self.y > self.fall_ending_y:
            self.state = Duck.ST_OVER
            self.play.duck_over(self.id)
            return
        
        self.screen.blit(self.fall_image, (self.x - self.offset_x, self.y - self.offset_y,))

        self.y += 10

    def shoot(self, shoot_x, shoot_y):

        if shoot_x < (self.x - self.offset_x):
            return
        if shoot_x > (self.x + self.offset_x):
            return
        if shoot_y < (self.y - self.offset_y):
            return
        if shoot_y > (self.y + self.offset_y):
            return
        
        #TODO: better hitbox
        self.play.duck_hit(self.id)
        self.state = Duck.ST_FALL
        #self.play.duck_over(self.id)
