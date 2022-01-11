# Snek

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Imports

import sys
import pygame
import random
from pygame.math import Vector2

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Classes

class Snake():
    def __init__(self):
        self.body = [Vector2(7, 10), Vector2(6, 10), Vector2(5, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False


class Fruit():
    def __init__(self):
        self.randomise()


class Main():
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Main Function

def main():
    pass

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Constants

pygame.init()
CLOCK = pygame.time.Clock()
CELL_SIZE = 20
CELL_NUMBER = 40
SCREEN_WIDTH = CELL_NUMBER * CELL_SIZE
SCREEN_HEIGHT = CELL_NUMBER * CELL_SIZE
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Runs Program

if __name__ == '__main__':
    main()
