import arcade
from DinoModel import PlayerDino

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class DinoDavWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

        self.Chomp = DinoModel(filename="images/Player-Triceratops.gif", center_x=width//2, center_y=height//2)

    def on_draw(self):
        arcade.start_render()
        self.Chomp.draw()


def main():
    window = DinoDavWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()


class DinoModel(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw(self):
        super().draw()

if __name__ == '__main__':
    main()