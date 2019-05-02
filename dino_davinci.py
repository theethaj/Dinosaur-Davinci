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
COM_DINOS = ["STEGOSAURUS", "NEDOCERATOPS", "JOBARIA", "ACROCANTHOSAURUS",
         "ARMATUS", "MAXIMUS", "GIGAS", "CRYOLOPHOSAURUS", "BRONTIKENS"]
COM_LP = [1600, 1800, 2200, 2600, 3400, 3600, 3800, 4000, 4200]

options = ["rock", "paper", "scissors"]

player_dinos = ["images/Ankylosaurus.png", "images/Styracosaurus.png", "images/Terry.png", "images/Ampelosaurus.png"]
com_dinos = ["images/Stegosaurus.png", "images/Diceratops.png", "images/Jobaria.png", "images/acrocantho.png",
             "images/Armatus.png", "images/Maximus.png", "images/Gigas.png", "images/Cry.png", "images/Brontikens.png"]


class Window(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.background = None

        self.player_pic = DinoModel(filename=player_dinos[2], center_x=width//4.3, center_y=height//2)
        self.com_pic = DinoModel(filename=com_dinos[2], center_x=width//1.25, center_y=height//2)

        self.rock = DinoModel(filename="images/rock.png", center_x=width//4.3, center_y=height//5)
        self.paper = DinoModel(filename="images/paper.png", center_x=width//4.3, center_y=height//5)
        self.scissors = DinoModel(filename="images/scissors.png", center_x=width//4.3, center_y=height//5)

        self.com_rock = DinoModel(filename="images/rock.png", center_x=width//1.25, center_y=height//5)
        self.com_paper = DinoModel(filename="images/paper.png", center_x=width//1.25, center_y=height//5)
        self.com_scissors = DinoModel(filename="images/scissors.png", center_x=width//1.25, center_y=height//5)

        self.craw = DinoModel(filename="images/craw2.png", center_x=width//4.3, center_y=height//2)
        self.com_craw = DinoModel(filename="images/craw2.png", center_x=width//1.25, center_y=height//2)

        self.player_name = PLAYER_DINOS[2]
        self.player_lp = PLAYER_LP[2]

        self.com_name = COM_DINOS[2]
        self.com_lp = COM_LP[2]

        self.win = ''

        self.is_rock = ''
        self.is_paper = ''
        self.is_scissors = ''

        self.com_is_rock = ''
        self.com_is_paper = ''
        self.com_is_scissors = ''

        self.is_craw = ''
        self.is_com_craw = ''

    def set_up(self):
        self.background = arcade.load_texture("images/volcano.jpg")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.player_pic.draw()
        self.com_pic.draw()

        arcade.draw_text(str(self.player_name), self.width - 770, self.height - 30, arcade.color.BLACK, 20)
        arcade.draw_text(str(self.player_lp), self.width - 770, self.height - 55, arcade.color.BLACK, 20)

        arcade.draw_text(str(self.com_name), self.width - 100, self.height - 30, arcade.color.BLACK, 20)
        arcade.draw_text(str(self.com_lp), self.width - 100, self.height - 55, arcade.color.BLACK, 20)

        if self.is_rock:
            self.rock.draw()
        if self.is_paper:
            self.paper.draw()
        if self.is_scissors:
            self.scissors.draw()

        if self.com_is_rock:
            self.com_rock.draw()
        if self.com_is_paper:
            self.com_paper.draw()
        if self.com_is_scissors:
            self.com_scissors.draw()

        if self.is_com_craw:
            self.com_craw.draw()
        if self.is_craw:
            self.craw.draw()

        arcade.draw_text("PRESS (R)ock, (P)aper and (S)cissors.", 100, 550, arcade.color.YELLOW, 10)

        if self.win == False:
            arcade.draw_text("YOU LOSE !!", 300, 550, arcade.color.RED, 40)
        elif self.win == True:
            arcade.draw_text("YOU WIN !!", 300, 550, arcade.color.GREEN, 40)

    def on_key_press(self, key, key_modifies):
        if key == arcade.key.R:
            self.is_rock = True
            self.is_paper = False
            self.is_scissors = False
            options.remove("rock")
            self.com_ans = random.choice(options)
            if self.com_ans == "paper":
                self.is_craw = True
                self.is_com_craw = False
                self.com_is_rock = False
                self.com_is_paper = True
                self.com_is_scissors = False
                self.player_lp -= 200
                if self.player_lp <= 0:
                    self.win = False
            elif self.com_ans == "scissors":
                self.is_craw = False
                self.is_com_craw = True
                self.com_is_rock = False
                self.com_is_paper = False
                self.com_is_scissors = True
                self.com_lp -= 200
                if self.com_lp <= 0:
                    self.win = True
            options.append("rock")
        elif key == arcade.key.P:
            self.is_rock = False
            self.is_paper = True
            self.is_scissors = False
            options.remove("paper")
            self.com_ans = random.choice(options)
            if self.com_ans == "rock":
                self.is_craw = False
                self.is_com_craw = True
                self.com_is_rock = True
                self.com_is_paper = False
                self.com_is_scissors = False
                self.com_lp -= 200
                if self.com_lp <= 0:
                    self.win = True
            elif self.com_ans == "scissors":
                self.is_craw = True
                self.is_com_craw = False
                self.com_is_rock = False
                self.com_is_paper = False
                self.com_is_scissors = True
                self.player_lp -= 200
                if self.player_lp <= 0:
                    self.win = False
            options.append("paper")
        elif key == arcade.key.S:
            self.is_rock = False
            self.is_paper = False
            self.is_scissors = True
            options.remove("scissors")
            self.com_ans = random.choice(options)
            if self.com_ans == "rock":
                self.is_craw = True
                self.is_com_craw = False
                self.com_is_rock = True
                self.com_is_paper = False
                self.com_is_scissors = False
                self.player_lp -= 200
                if self.player_lp <= 0:
                    self.win = False
            elif self.com_ans == "paper":
                self.is_craw = False
                self.is_com_craw = True
                self.com_is_rock = False
                self.com_is_paper = True
                self.com_is_scissors = False
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