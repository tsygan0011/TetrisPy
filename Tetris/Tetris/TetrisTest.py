

# import
import random
import pygame
import sys
import os
from time import sleep
from pygame.locals import *

colors = [(19, 232, 232),  # Cyan  (0, 128, 0),  # Green
          (236, 14, 14),  # Red
          (30, 30, 201),  # Blue
          (240, 110, 2),  # Orange
          (236, 236, 14),  # Yellow
          (126, 5, 126)]  # Purple

white = (255, 255, 255)
grey = (128, 128, 128)
black = (0, 0, 0)



class Tetris:
    cleared_lines = 0
    score = 0
    state = "start"
    field = []
    HEIGHT = 0
    WIDTH = 0
    startX = 100
    startY = 50
    zoom = 20
    figure = None

    def __init__(self, height, width):
        self.field = []
        self.figure = None
        self.height = height
        self.width = width
        for i in range(height):
            new_line = []
            for x in range(width):
                new_line.append(0)
            self.field.append(new_line)

    def create_figure(self):
        self.figure = Figures(3, 0)

    def intersect(self):
        intersect = False
        for i in range(4):
            for x in range(4):
                if (i * 4) + x in self.figure.get_image():
                    if ((i + self.figure.y) > (self.height - 1)) or ((x + self.figure.x) > (self.width - 1)) or (
                            (x + self.figure.x) < 0) or (self.field[i + self.figure.y][x + self.figure.x] > 0):
                        intersect = True
        return intersect

    def freeze_figure(self):
        for i in range(4):
            for x in range(4):
                if i * 4 + x in self.figure.get_image():
                    self.field[i + self.figure.y][x + self.figure.x] = self.figure.color
        self.break_lines()
        self.create_figure()
        if self.intersect():
            self.state = "gameover"

    def break_lines(self):
        line = 0
        for i in range(1, self.height):
            zero = 0
            for x in range(0, self.width):
                if self.field[i][x] == 0:
                    zero += 1

            if zero == 0:
                line += 1
                for n in range(i, 1, -1):
                    for x in range(self.width):
                        self.field[n][x] = self.field[n - 1][x]
        self.score += line ** 2
        self.cleared_lines += line

    def space(self):
        while not self.intersect():
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze_figure()

    def down(self):
        self.figure.y += 1
        if self.intersect():
            self.figure.y -= 1
            self.freeze_figure()

    def sideways(self, dx):
        previous_x = self.figure.x
        self.figure.x += dx
        if self.intersect():
            self.figure.x = previous_x

    def rotate(self):
        previous_rotation = self.figure.rotation
        self.figure.rotate()
        if self.intersect():
            self.figure.rotation = previous_rotation


class Figures:
    figures = [
        [[4, 5, 6, 7], [1, 5, 9, 13]],  # Straight Line
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],  # pyramid
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 8, 9], [4, 5, 6, 10]],  # Left L
        [[1, 2, 6, 10], [3, 5, 6, 7], [2, 6, 10, 11], [5, 6, 7, 9]],  # Right L
        [[5, 6, 9, 10]],  # Square
        [[1, 2, 4, 5], [0, 4, 5, 9], [5, 6, 8, 9], [1, 5, 6, 10]],  # zig zag L
        [[1, 2, 6, 7], [3, 6, 7, 10], [5, 6, 10, 11], [2, 5, 6, 9]]  # zig zag right
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, (len(self.figures) - 1))
        self.color = random.randint(1, (len(colors) - 1))
        self.rotation = 0

    def get_image(self):
        return self.figures[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % (len(self.figures[self.type]))


def main():
    boardHeight = 400
    boardWidth = 500
    gameHeight = 20
    gameWidth = 10
    pressingDown = False
    gameover = False
    counter = 0
    fps = 30

    pygame.init()
    window = pygame.display.set_mode((boardHeight, boardWidth))
    clock = pygame.time.Clock()
    game = Tetris(gameHeight, gameWidth)

    while not gameover:
        if game.figure is None:
            game.create_figure()
        counter += 1
        if counter > 100000:
            counter = 0
        if counter % (fps // 2) == 0 or pressingDown:
            if game.state == "start":
                game.down()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    game.sideways(1)
                if event.key == pygame.K_LEFT:
                    game.sideways(-1)
                if event.key == pygame.K_UP:
                    game.rotate()
                if event.key == pygame.K_DOWN:
                    pressingDown = True
                if event.key == pygame.K_SPACE:
                    game.space()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pressingDown = False

        window.fill(white)

        for i in range(gameHeight):
            for x in range(gameWidth):
                pygame.draw.rect(window, grey,
                                 [game.startX + game.zoom * x, game.startY + game.zoom * i, game.zoom, game.zoom], 1)
                if game.field[i][x] > 0:
                    pygame.draw.rect(window, colors[game.field[i][x]],
                                     [game.startX + game.zoom * x, game.startY + game.zoom * i, game.zoom - 2,
                                      game.zoom - 1])

        if game.figure is not None:
            for i in range(4):
                for x in range(4):
                    p = i * 4 + x
                    if p in game.figure.get_image():
                        pygame.draw.rect(window, colors[game.figure.color], [
                            game.startX + game.zoom * (x + game.figure.x) + 1,
                            game.startY + game.zoom * (i + game.figure.y) + 1,
                            game.zoom - 1,
                            game.zoom - 1
                        ])

        font1 = pygame.font.SysFont('Arial', 11, bold=True)
        text_score = font1.render("Score: " + str(game.score), True, black)
        text_gameOver = font1.render("Game Over", True, black)
        text_exit = font1.render("Press ESC", True, black)

        window.blit(text_score, [100, 20])
        if game.state == "gameover":
            window.blit(text_gameOver, [20, 220])
            window.blit(text_exit, [20, 275])
        pygame.display.flip()
        clock.tick(fps)


if __name__ == "__main__":
    main()
