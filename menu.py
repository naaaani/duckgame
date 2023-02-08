from pygame_button import Button


class Menu:

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

    def start(self):
        pass

    def proc_event(self, event):

        self.button.check_event(event)
        self.button.update(self.screen)


    def press(self):
        print("Press")