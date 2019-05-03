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
         "ARMATUS", "MAXIMUS", "GIGAS", "CRYOLOPHOSAURUS", "BRONTOSAURUS"]
COM_LP = [1600, 1800, 2200, 2600, 3400, 3600, 3800, 4000, 4200]

options = ["rock", "paper", "scissors"]
tf = [True, False, False, False, False]
bg = ["images/menu.png", "images/volcano.jpg"]

player_dinos = ["images/Ankylosaurus.png", "images/Styracosaurus.png", "images/Terry.png", "images/Ampelosaurus.png"]
com_dinos = ["images/Stegosaurus.png", "images/Diceratops.png", "images/Jobaria.png", "images/acrocantho.png",
             "images/Armatus.png", "images/Maximus.png", "images/Gigas.png", "images/Cry.png", "images/Brontikens.png"]

player_menu = ["images/l-ank.png", "images/l-sty.png", "images/l-tyr.png", "images/l-amp.png"]
com_menu = ["images/l-ste.png", "images/l-ned.png", "images/l-job.png", "images/l-acr.png", "images/l-arm.png",
            "images/l-max.png", "images/l-gig.png", "images/l-cry.png", "images/l-bro.png"]


class MainWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.window = Window(self, width, height)

    def on_draw(self):
        self.window.on_draw()

    def on_key_press(self, key, key_modifies):
        if key == arcade.key.ENTER and bg.index(self.window.background_filename) > 0:
            self.window = Window(self, self.width, self.height)
            return
        self.window.on_key_press(key, key_modifies)


class Window:
    def __init__(self, main_window, width, height):
        self.main_window = main_window

        self.background = None
        self.background_filename = ''
        self.set_up()

        m = random.randrange(0, 4)
        x = random.randrange(0, 9)

        self.player_menu = DinoModel(filename=player_menu[m], center_x=width//2.7, center_y=height//1.075)
        self.com_menu = DinoModel(filename=com_menu[x], center_x=width//1.79, center_y=height//1.075)

        self.player_pic = DinoModel(filename=player_dinos[m], center_x=width//4.3, center_y=height//2)
        self.com_pic = DinoModel(filename=com_dinos[x], center_x=width//1.25, center_y=height//2)

        self.rock = DinoModel(filename="images/rock.png", center_x=width//4.3, center_y=height//5)
        self.paper = DinoModel(filename="images/paper.png", center_x=width//4.3, center_y=height//5)
        self.scissors = DinoModel(filename="images/scissors.png", center_x=width//4.3, center_y=height//5)

        self.com_rock = DinoModel(filename="images/rock.png", center_x=width//1.25, center_y=height//5)
        self.com_paper = DinoModel(filename="images/paper.png", center_x=width//1.25, center_y=height//5)
        self.com_scissors = DinoModel(filename="images/scissors.png", center_x=width//1.25, center_y=height//5)

        self.craw = DinoModel(filename="images/craw2.png", center_x=width//4.3, center_y=height//2)
        self.com_craw = DinoModel(filename="images/craw2.png", center_x=width//1.25, center_y=height//2)

        self.player_weak = DinoModel(filename="images/weak.png", center_x=width//2.7, center_y=height//1.175)
        self.com_weak = DinoModel(filename="images/weak.png", center_x=width//1.79, center_y=height//1.175)

        self.missed = DinoModel(filename="images/missed.png", center_x=width//4, center_y=height//1.075)

        self.restart_pic = DinoModel(filename="images/restart.png", center_x=width//1.07, center_y=height//1.05)

        self.game = DinoModel(filename="images/game.png", center_x=width//4, center_y=height//1.075)
        self.winner = DinoModel(filename="images/win.png", center_x=width//4, center_y=height//1.075)

        self.player_name = PLAYER_DINOS[m]
        self.player_lp = PLAYER_LP[m]

        self.com_name = COM_DINOS[x]
        self.com_lp = COM_LP[x]

        self.weak_for = ''
        self.weak_against = ''

        self.is_missed = ''

        if m == 0 and (x == 3 or x == 6):
            self.weak_for = True
        elif m == 1 and (x == 0 or x == 4):
            self.weak_for = True
        elif m == 2 and (x == 2 or x == 8):
            self.weak_for = True
        elif m == 3 and (x == 1 or x == 5):
            self.weak_for = True

        if m == 0 and (x == 1 or x == 5 or x == 7):
            self.weak_against = True
        elif m == 1 and (x == 2 or x == 7 or x == 8):
            self.weak_against = True
        elif m == 2 and (x == 0 or x == 4 or x == 7):
            self.weak_against = True
        elif m == 3 and (x == 3 or x == 6 or x == 7):
            self.weak_against = True

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
        self.background_filename = bg[0]
        self.background = arcade.load_texture(self.background_filename)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        if bg.index(self.background_filename) > 0:
            self.player_menu.draw()
            self.com_menu.draw()

            self.player_pic.draw()
            self.com_pic.draw()

            self.restart_pic.draw()

            # arcade.draw_text(str(self.player_name), self.width - 770, self.height - 30, arcade.color.BLACK, 20)
            arcade.draw_text(str(self.player_lp), self.width - 460, self.height - 50, arcade.color.BLACK, 20)

            # arcade.draw_text(str(self.com_name), self.width - 100, self.height - 30, arcade.color.BLACK, 20)
            arcade.draw_text(str(self.com_lp), self.width - 310, self.height - 50, arcade.color.BLACK, 20)

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

            if self.weak_for:
                self.com_weak.draw()
            if self.weak_against:
                self.player_weak.draw()

            # arcade.draw_text("PRESS (R)ock, (P)aper and (S)cissors.", 300, 500, arcade.color.YELLOW, 10)

            if self.win == False:
                self.game.draw()
            elif self.win == True:
                self.winner.draw()

            if self.is_missed == True:
                self.missed.draw()

    def on_key_press(self, key, key_modifies):
        if bg.index(self.background_filename) == 0:
            if key == arcade.key.ENTER:
                self.background_filename = bg[1]
                self.background = arcade.load_texture(self.background_filename)
        elif bg.index(self.background_filename) > 0:
            if key == arcade.key.ENTER:
                self.background_filename = bg[0]
                self.background = arcade.load_texture(self.background_filename)
            elif self.win == True or self.win == False:
                return
            elif key == arcade.key.R:
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
                    self.is_missed = random.choice(tf)
                    if self.is_missed == True:
                        pass
                    else:
                        if self.weak_against == True:
                            self.player_lp -= 400
                        else:
                            self.player_lp -= 200
                        if self.player_lp <= 0:
                            self.player_lp = 0
                            self.win = False
                elif self.com_ans == "scissors":
                    self.is_craw = False
                    self.is_com_craw = True
                    self.com_is_rock = False
                    self.com_is_paper = False
                    self.com_is_scissors = True
                    if self.is_missed == True:
                        pass
                    else:
                        if self.weak_for == True:
                            self.com_lp -= 400
                        else:
                            self.com_lp -= 200
                        if self.com_lp <= 0:
                            self.com_lp = 0
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
                    if self.is_missed == True:
                        pass
                    else:
                        if self.weak_for == True:
                            self.com_lp -= 400
                        else:
                            self.com_lp -= 200
                        if self.com_lp <= 0:
                            self.com_lp = 0
                            self.win = True
                elif self.com_ans == "scissors":
                    self.is_craw = True
                    self.is_com_craw = False
                    self.com_is_rock = False
                    self.com_is_paper = False
                    self.com_is_scissors = True
                    self.is_missed = random.choice(tf)
                    if self.is_missed == True:
                        pass
                    else:
                        if self.weak_against == True:
                            self.player_lp -= 400
                        else:
                            self.player_lp -= 200
                        if self.player_lp <= 0:
                            self.player_lp = 0
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
                    self.is_missed = random.choice(tf)
                    if self.is_missed == True:
                        pass
                    else:
                        if self.weak_against == True:
                            self.player_lp -= 400
                        else:
                            self.player_lp -= 200
                        if self.player_lp <= 0:
                            self.player_lp = 0
                            self.win = False
                elif self.com_ans == "paper":
                    self.is_craw = False
                    self.is_com_craw = True
                    self.com_is_rock = False
                    self.com_is_paper = True
                    self.com_is_scissors = False
                    self.is_missed = random.choice(tf)
                    if self.is_missed == True:
                        pass
                    else:
                        if self.weak_for == True:
                            self.com_lp -= 400
                        else:
                            self.com_lp -= 200
                        if self.com_lp <= 0:
                            self.com_lp = 0
                            self.win = True
                options.append("scissors")

    @property
    def width(self):
        return self.main_window.width

    @property
    def height(self):
        return self.main_window.height


class DinoModel(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw(self):
        super().draw()


if __name__ == '__main__':
    window = MainWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    # window.set_up()
    arcade.run()