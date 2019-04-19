import arcade
import arcade.key
import random
import math
from random import randint

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_DINOS = ["TYRANNOSAURUS REX", "TRICERATOPS", "SAICHANIA", "ISISAURUS"]
PLAYER_LP = [1800, 1700, 1600, 2000]
ADV_DINOS = ["DEINONYCHUS", "CRYOLOPHOSAURUS", "THERIZINOSAURUS", "MEGALOSAURUS"]
ADV_LP = [3700, 4400, 4000, 4200]
EXP_DINOS = ["GIGAS", "MAXIMUS", "ARMATUS", "BRONTIKENS"]
EXP_LP = [4800, 4700, 4600, 5000]
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

    def set_up(self):
        self.background = arcade.load_texture("images/bg1.png")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.Chomp.draw()
        self.Tank.draw()

        arcade.draw_text(str(self.player_name), self.width - 770, self.height - 30, arcade.color.WHITE, 20)
        arcade.draw_text(str(PLAYER_LP[0]), self.width - 770, self.height - 55, arcade.color.WHITE, 20)
        arcade.draw_text(str(self.com_name), self.width - 100, self.height - 30, arcade.color.BLACK, 20)
        arcade.draw_text(str(EXP_LP[0]), self.width - 100, self.height - 55, arcade.color.BLACK, 20)


class DinoModel(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw(self):
        super().draw()


class judgement():
    def __init__(self):
        self.answer = answer
        self.com_ans = com_ans

    def on_key_press(self):
        if arcade.key.R:
            options.remove(options[0])
            self.com_ans = random.choice(options)
            if self.com_ans == "paper":
                return False
            elif self.com_ans == "scissors":
                return True
            options.append(options[0])
        elif arcade.key.P:
            self.answer = options[1]
            options.remove(options[1])
            self.com_ans = random.choice(options)
            if self.com_ans == "rock":
                return True
            elif self.com_ans == "scissors":
                return False
            options.append(options[1])
        elif arcade.key.S:
            self.answer = options[2]
            options.remove(options[2])
            self.com_ans = random.choice(options)
            if self.com_ans == "rock":
                return False
            elif self.com_ans == "paper":
                return True
            options.append(options[2])

    # def rps_judge(self):
    #     if self.answer == options[0]:
    #         options.remove(options[0])
    #         self.com_ans = random.choice(options)
    #         if self.com_ans == options[1]:
    #             return False
    #         elif self.com_ans == options[2]:
    #             return True
    #         options.append(options[0])
    #     elif self.answer == options[1]:
    #         options.remove(options[1])
    #         self.com_ans = random.choice(options)
    #         if self.com_ans == options[0]:
    #             return True
    #         elif self.com_ans == options[2]:
    #             return False
    #         options.append(options[1])
    #     elif self.answer == options[2]:
    #         options.remove(options[2])
    #         self.com_ans = random.choice(options)
    #         if self.com_ans == options[0]:
    #             return False
    #         elif self.com_ans == options[1]:
    #             return True
    #         options.append(options[2])

    def update(self):
        if self.on_key_press() == False:
            PLAYER_LP[0] -= 200
        elif self.on_key_press() == True:
            EXP_LP[0] -= 200


if __name__ == '__main__':
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.set_up()
    arcade.run()