import pygame
import random
from pygame.sprite import Sprite

from game.utils.constants import ENEMY_1,ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH

class Enemy(Sprite):
    ENEMY_WIDTH = 40
    ENEMY_HEIGHT = 60
    Y_POS = 0
    X_POS_RANGE = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    SPEED_ON_Y = 1
    SPEED_ON_X = 10
    MOVES = { 0: 'left', 1: 'right' }
    IMAGE = {1:ENEMY_1, 2:ENEMY_2}

    def __init__(self,image = 1,speed_x = SPEED_ON_X , speed_y = SPEED_ON_Y , moves_before_change = [20,50]):
        self.image = self.IMAGE[image]
        self.image = pygame.transform.scale(self.image, (self.ENEMY_WIDTH, self.ENEMY_HEIGHT))
        self.rect = self.image.get_rect(midtop = (random.choice(self.X_POS_RANGE), self.Y_POS))
        self.direction = self.MOVES[random.randint(0, 1)]
        self.movement_count = 0
        self.SPEED_ON_X =speed_x
        self.SPEED_ON_Y = speed_y
        self.moves_before_change = random.randint(moves_before_change[0],moves_before_change[1])

    def update(self, enemies):
        self.rect.y += self.SPEED_ON_Y

        if self.direction == self.MOVES[0]:
            self.rect.x -= self.SPEED_ON_X
        elif self.direction == self.MOVES[1]:
            self.rect.x += self.SPEED_ON_X

        self.handle_direction()

        if self.rect.top > SCREEN_HEIGHT:
            enemies.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def handle_direction(self):
        self.movement_count += 1

        if (self.movement_count >= self.moves_before_change and self.direction == self.MOVES[1]) or self.rect.right >= SCREEN_WIDTH:
            self.direction = self.MOVES[0]
        elif self.movement_count >= self.moves_before_change and self.direction == self.MOVES[0] or self.rect.left <= 0:
            self.direction = self.MOVES[1]
        
        if (self.movement_count >= self.moves_before_change):
            self.movement_count = 0