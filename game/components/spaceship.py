from typing import Any
import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH,SCREEN_HEIGHT
from game.components.bullets.bullet import Bullet
from game.utils.constants import SOUND
class Spaceship(Sprite):
    SPACESHIP_WIDTH = 40
    SPACESHIP_HEIGHT = 60
    SPACESHIP_POS_X = SCREEN_WIDTH /2
    SPACESHIP_POS_Y = 500


    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image,(self.SPACESHIP_WIDTH ,self.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect(midbottom = (self.SPACESHIP_POS_X,self.SPACESHIP_POS_Y))
        self.type = 'player'
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def update(self, user_input,game):
        if user_input[pygame.K_LEFT] and user_input[pygame.K_SPACE] :
            self.move_left()
            self.shoot(game)
        elif user_input[pygame.K_RIGHT] and user_input[pygame.K_SPACE] :
            self.move_right()
            self.shoot(game)
        elif user_input[pygame.K_SPACE]:
            self.shoot(game)
        elif user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP] and self.rect.top > 300:
            self.rect.y -=10
        elif user_input[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT :
            self.rect.y +=10


    def move_left(self):
        self.rect.x -=10
        if self.rect.x<0:
            self.rect.x = SCREEN_WIDTH

    def move_right(self):
        self.rect.x +=10
        if self.rect.right > SCREEN_WIDTH:
            self.rect.x = 0

    def shoot(self,game):
        bullet = Bullet(self)
        game.bullet_manager.add_bullet(bullet)
        SOUND["Shoothing"].set_volume(0.02)
        SOUND["Shoothing"].play()

    def reset(self):
        self.rect.x = self.SPACESHIP_POS_X
        self.rect.y = self.SPACESHIP_POS_Y





