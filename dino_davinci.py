import arcade
import random
import math
# from DinoModel import PlayerDino

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BID = 0
PLAYER_LP = 0
COMPUTER_LP = 0

class Window(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

        self.Chomp = DinoModel(filename="images/Player-Triceratops.gif", center_x=width//4, center_y=height//2)
        self.Tank = DinoModel(filename="images/Player-Saichania.jpg", center_x=width//1.3, center_y=height//2)
    def on_draw(self):
        arcade.start_render()
        self.Chomp.draw()
        self.Tank.draw()


def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()


class DinoModel(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw(self):
        super().draw()


if __name__ == '__main__':
    main()