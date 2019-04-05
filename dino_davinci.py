import arcade
import random
import math
from random import randint

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BID = [0]
PLAYER_LP = [0]
COMPUTER_LP = [0]
options = ["rock", "paper", "scissors"]


class Window(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.background = None
        self.Chomp = DinoModel(filename="images/Terry.png", center_x=width//4, center_y=height//2)
        self.Tank = DinoModel(filename="images/Gigas.png", center_x=width//1.3, center_y=height//2)
        self.player_name = "TYRANNOSAURUS REX"
        self.com_name = "GIGAS"

    def set_up(self):
        self.background = arcade.load_texture("images/bg1.png")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.Chomp.draw()
        self.Tank.draw()

        arcade.draw_text(str(self.com_name), self.width - 100, self.height - 30, arcade.color.BLACK, 20)
        arcade.draw_text(str(self.player_name), self.width - 20, self.height - 30, arcade.color.BLACK, 20)


class DinoModel(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw(self):
        super().draw()

class judgement():
    def __init__(self):
        self.player = player
        self.com = com

    def rps_judge(self):
        if player == "rock":
            options.remove(player)
            com = random.choice(options)
            if com == "paper":
                return False
            elif com == "scissors":
                return True
        elif player == "paper":
            options.remove(player)
            com = random.choice(options)
            if com == "rock":
                return True
            elif com == "scissors":
                return False
        elif player == "scissors":
            options.remove(player)
            com = random.choice(options)
            if com == "rock":
                return False
            elif com == "paper":
                return True

    def rps_system(self):
        if self.rps_judge() == False:
            PLAYER_LP[0] = PLAYER_LP[0] - BID[0]
        elif self.rps_judge() == True:
            COMPUTER_LP[0] = COMPUTER_LP[0] - BID[0]


if __name__ == '__main__':
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.set_up()
    arcade.run()