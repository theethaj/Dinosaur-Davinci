import arcade
import sys
import arcade.key
import random
import math
from random import randint

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

PLAYER_DINOS = ["ANKYLOSAURUS", "STYRACOSAURUS", "TYRANNOSAURUS REX", "AMPELOSAURUS"]
PLAYER_LP = [1600, 1800, 2000, 2200]
COM_DINOS = ["STEGOSAURUS", "NEDOCERATOPS", "AMPELOSAURUS", "BLACK T-REX",
         "ARMATUS", "MAXIMUS", "GIGAS", "CRYOLOPHOSAURUS", "BRONTIKENS"]
COM_LP = [1600, 1800, 2200, 2500, 3400, 3600, 3800, 4000, 4200]

options = ["rock", "paper", "scissors"]


class Window(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.background = None
        self.player_pic = DinoModel(filename="images/Terry.png", center_x=width//4, center_y=height//2)
        self.com_pic = DinoModel(filename="images/Gigas.png", center_x=width//1.3, center_y=height//2)
        self.player_name = PLAYER_DINOS[2]
        self.player_lp = PLAYER_LP[2]
        self.com_name = COM_DINOS[6]
        self.com_lp = COM_LP[6]
        self.win = ''
        self.clan = ''

    def set_up(self):
        self.background = arcade.load_texture("images/bg1.png")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.player_pic.draw()
        self.com_pic.draw()

        arcade.draw_text(str(self.player_name), self.width - 770, self.height - 30, arcade.color.WHITE, 20)
        arcade.draw_text(str(self.player_lp), self.width - 770, self.height - 55, arcade.color.WHITE, 20)

        arcade.draw_text(str(self.com_name), self.width - 100, self.height - 30, arcade.color.BLACK, 20)
        arcade.draw_text(str(self.com_lp), self.width - 100, self.height - 55, arcade.color.BLACK, 20)

        arcade.draw_text("PRESS (R)ock, (P)aper and (S)cissors.", 100, 550, arcade.color.YELLOW, 10)

        if self.win == False:
            arcade.draw_text("YOU LOSE !!", 300, 550, arcade.color.YELLOW, 40)
        elif self.win == True:
            arcade.draw_text("YOU WIN !!", 300, 550, arcade.color.YELLOW, 40)

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