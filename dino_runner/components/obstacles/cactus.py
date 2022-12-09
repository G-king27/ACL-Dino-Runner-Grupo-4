from pygame import Surface
from random import randint

from dino_runner.components.obstacles.obstacle import Obstacle


class Cactus(Obstacle):
    Y_POS_LARGE_CACTUS = 300

    def __init__(self, images: list[Surface], type):
        super(). __init__(images, randint(0, 2))
        self.rect.y = self.Y_POS_LARGE_CACTUS


class SmallCactus(Obstacle):
    Y_POS_SMALL_CACTUS = 325
    
    def __init__(self, images: list[Surface], type):
        super(). __init__(images, randint(0, 2))
        self.rect.y = self.Y_POS_SMALL_CACTUS