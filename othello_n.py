import pygame
import numpy as np


class GameDisplay:
    def __init__(self):
        # define color
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.screen = pygame.display.set_mode((1280, 720))  # display size
        self.clock = pygame.time.Clock()  # time elapse

        # fonts
        pygame.font.init()
        self.font = pygame.font.SysFont("symap", 100)
        self.win_font = pygame.font.SysFont("symap", 200)
        self.button_text = pygame.font.SysFont("symap", 50)
        self.b_text = self.font.render("BLACK", True, (0, 0, 0), (255, 255, 255))
        self.w_text = self.font.render("WHITE", True, (255, 255, 255), (0, 0, 0))
        self.b_win = self.win_font.render("BLACK WIN", True, (0, 0, 0), (255, 255, 255))
        self.w_win = self.win_font.render("WHITE WIN", True, (255, 255, 255), (0, 0, 0))
        self.draw = self.win_font.render("DRAW", True, (255, 0, 0), (0, 0, 0))

        # create board
        for i in range(self.grid_size + 1):
            for k in range(self.grid_size + 1):
                self.rects[i][k][0] = 340.0 + i * 600 / self.grid_size
                self.rects[i][k][1] = 60.0 + k * 600 / self.grid_size


class Board:
    def __init__(self):
        # initialize board
        self.grid_size = 10
        self.grid_sq = self.grid_size**2
        self.rects = np.zeros([self.grid_size + 1, self.grid_size + 1, 2])

        # define directions
        self.directions = [
            "left",
            "right",
            "up",
            "down",
            "left_up",
            "left_down",
            "right_up",
            "right_down",
        ]

        self.is_black = True  # black: turn = True
        self.num_skip = 0  # count skiped turns
        self.put = False

        self.temp = 0b0
        self.can_reverse = 0b0

        self.str_in = "{:0>a}".replace("a", f"{self.grid_sq}")

        # masks
        self.horizontal_mask = int(
            ("0" + "1" * (self.grid_size - 2) + "0") * self.grid_size, 2
        )

        self.vertical_mask = int(
            "0" * self.grid_size
            + "1" * self.grid_size * (self.grid_size - 2)
            + "0" * self.grid_size,
            2,
        )

        self.allside_mask = int(
            "0" * self.grid_size
            + ("0" + "1" * (self.grid_size - 2) + "0") * (self.grid_size - 2)
            + "0" * self.grid_size,
            2,
        )

        # masks correspond to directions
        self.masks = {
            "left": self.horizontal_mask,
            "right": self.horizontal_mask,
            "up": self.vertical_mask,
            "down": self.vertical_mask,
            "left_up": self.allside_mask,
            "left_down": self.allside_mask,
            "right_up": self.allside_mask,
            "right_down": self.allside_mask,
        }


class Disc:
    def __init__(self):
        pass
