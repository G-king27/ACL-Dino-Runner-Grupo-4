import pygame
from random import randint

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS


class ObstacleManager:
    def __init__(self):
        self.obstacles: list[Obstacle] = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus("SMALL" if randint(0, 1) else "LARGE"))

            for obstacle in self.obstacles:
                obstacle.update(game.game_speed, self.obstacles)
                if not game.player.shield:
                    if game.player.dino_rect.colliderect(obstacle.rect()):
                        game.player_heart_manager.reduce_heart_count
                        if game.player_heart_manager.heart_count > 0:
                            self.obstacles.pop()
                        else:
                            pygame.time.delay(1000)
                            game.playing = False
                            game.death_count += 1

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []