import arcade
import sys
import arcade.key
import random
import math
from random import randint

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_DINOS = ["TYRANNOSAURUS REX", "TRICERATOPS", "SAICHANIA", "ISISAURUS"]
PLAYER_LP = [2000, 1800, 1600, 2200]
ADV_DINOS = ["DEINONYCHUS", "CRYOLOPHOSAURUS", "THERIZINOSAURUS", "MEGALOSAURUS"]
ADV_LP = [4000, 5200, 4200, 4400]
EXP_DINOS = ["GIGAS", "MAXIMUS", "ARMATUS", "BRONTIKENS"]
EXP_LP = [5000, 4800, 4600, 5400]
options = ["rock", "paper", "scissors"]


class Window(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.background = None
        self.Chomp = DinoModel(filename="images/Terry.png", center_x=width//4, center_y=height//2)
        self.Tank = DinoModel(filename="images/Gigas.png", center_x=width//1.3, center_y=height//2)
        self.player_name = PLAYER_DINOS[0]
        self.player_lp = PLAYER_LP[0]
        self.com_name = EXP_DINOS[0]
        self.com_lp = EXP_LP[0]
        self.win = ''
        self.rock_choice = ''
        self.paper_choice = ''
        self.scissors_choice = ''

    def set_up(self):
        self.background = arcade.load_texture("images/bg1.png")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.Chomp.draw()
        self.Tank.draw()

        arcade.draw_text(str(self.player_name), self.width - 770, self.height - 30, arcade.color.WHITE, 20)
        arcade.draw_text(str(self.player_lp), self.width - 770, self.height - 55, arcade.color.WHITE, 20)
        arcade.draw_text(str(self.com_name), self.width - 100, self.height - 30, arcade.color.BLACK, 20)
        arcade.draw_text(str(self.com_lp), self.width - 100, self.height - 55, arcade.color.BLACK, 20)
        arcade.draw_text("PRESS (R)ock, (P)aper and (S)cissors.", 100, 550, arcade.color.YELLOW, 10)

        if self.win == False:
            arcade.draw_text("YOU LOSE !!", 100, 50, arcade.color.RED, 100)
        elif self.win == True:
            arcade.draw_text("YOU WIN !!", 100, 50, arcade.color.RED, 100)

    def on_key_press(self, key, key_modifies):
        if key == arcade.key.R:
            options.remove("rock")
            self.com_ans = random.choice(options)
            if self.com_ans == "paper":
                self.player_lp -= 200
                if self.player_lp <= 0:
                    self.win = False
            elif self.com_ans == "scissors":
                self.com_lp -= 200
                if self.com_lp <= 0:
                    self.win = True
            options.append("rock")
        elif key == arcade.key.P:
            options.remove("paper")
            self.com_ans = random.choice(options)
            if self.com_ans == "rock":
                self.com_lp -= 200
                if self.com_lp <= 0:
                    self.win = True
            elif self.com_ans == "scissors":
                self.player_lp -= 200
                if self.player_lp <= 0:
                    self.win = False
            options.append("paper")
        elif key == arcade.key.S:
            options.remove("scissors")
            self.com_ans = random.choice(options)
            if self.com_ans == "rock":
                self.player_lp -= 200
                if self.player_lp <= 0:
                    self.win = False
            elif self.com_ans == "paper":
                self.com_lp -= 200
                if self.com_lp <= 0:
                    self.win = True
            options.append("scissors")


class DinoModel(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw(self):
        super().draw()


if __name__ == '__main__':
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.set_up()
    arcade.run()