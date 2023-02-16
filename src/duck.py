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

        self.score = abs(speed)

        self.y = y

        if speed < 0:
            speed -= 5
        else:
            speed += 5

        self.speed = self.screen_width * speed / 1000

        self.init_image()
        self.init_pos()

        self.duck_image = pygame.transform.scale(
            self.duck_image, (self.duck_width, self.duck_height,))
        self.fall_image = pygame.transform.scale(
            self.fall_image, (self.duck_height, self.duck_width,))
        self.mask_image = pygame.transform.scale(
            self.mask_image, (self.duck_width, self.duck_height,))

        self.offset_x = self.duck_width / 2
        self.offset_y = self.duck_height / 2

        self.reset()

    def init_image(self):

        self.duck_image = pygame.image.load("../images/duck1.png")
        (orig_width, orig_height,) = self.duck_image.get_size()
        self.duck_height = self.screen_height / 6
        shrink_width = self.duck_height / orig_height
        self.duck_width = orig_width * shrink_width

        self.mask_image = pygame.image.load("../images/duck1mask.png")

    def init_pos(self):

        if self.speed < 0:
            self.starting_x = self.screen_width + (self.duck_width / 2)
            self.duck_image = pygame.transform.flip(
                self.duck_image, flip_x=True, flip_y=False)
            self.fall_image = pygame.transform.rotate(self.duck_image, 90)
            self.fly_ending_x = -(self.duck_width / 2)
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

        if self.speed > 0:
            out_of_screen = (self.x > self.fly_ending_x)
        else:
            out_of_screen = (self.x < self.fly_ending_x)

        if out_of_screen:
            self.state = Duck.ST_OVER
            self.play.duck_over(self.id)
            return

        self.screen.blit(self.duck_image, (self.x -
                         self.offset_x, self.y - self.offset_y,))

        self.x += self.speed

    def update_fall(self):

        if self.y > self.fall_ending_y:
            self.state = Duck.ST_OVER
            self.play.duck_over(self.id)
            return

        self.screen.blit(self.fall_image, (self.x -
                         self.offset_x, self.y - self.offset_y,))

        self.y += 10

    def shoot(self, shoot_x, shoot_y):

        if self.hitbox(shoot_x, shoot_y) and self.hitmask(shoot_x, shoot_y):            
            self.play.duck_hit(self.id)
            self.state = Duck.ST_FALL
            return

    def hitbox(self, shoot_x, shoot_y):

        if shoot_x < (self.x - self.offset_x):
            return False
        if shoot_x > (self.x + self.offset_x):
            return False
        if shoot_y < (self.y - self.offset_y):
            return False
        if shoot_y > (self.y + self.offset_y):
            return False

        return True

    def hitmask(self, shoot_x, shoot_y):

        duck_corner_x = self.x - self.offset_x
        hit_x = int(shoot_x - duck_corner_x)
        duck_corner_y = self.y - self.offset_y
        hit_y = int(shoot_y - duck_corner_y)
        try:
            color = self.mask_image.get_at((hit_x, hit_y,))
        except IndexError:
            color = (0, 0, 0, 0,)

        return color[3] > 50

    def get_score(self):

        return self.score
