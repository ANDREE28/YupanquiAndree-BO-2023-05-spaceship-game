from typing import Any
import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH,SCREEN_HEIGHT

#la clase Spaceship va a heredar de la clase Sprite
class Spaceship(Sprite):
    SPACESHIP_WIDTH = 40
    SPACESHIP_HEIGHT = 60
    SPACESHIP_POS_X = SCREEN_WIDTH /2
    SPACESHIP_POS_Y = 500

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image,(self.SPACESHIP_WIDTH ,self.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect(midbottom = (self.SPACESHIP_POS_X,self.SPACESHIP_POS_Y))
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def update(self, user_input):
        if user_input[pygame.K_LEFT] :
            self.left()
        elif user_input[pygame.K_RIGHT] :
            self.right()
            
        elif user_input[pygame.K_UP] and self.rect.top > 300:
            self.rect.y -=10
        elif user_input[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT :
            self.rect.y +=10



    def left(self):
        self.rect.x -=10
        if self.rect.x<0:
            self.rect.x = SCREEN_WIDTH

    def right(self):
        self.rect.x +=10
        if self.rect.right > SCREEN_WIDTH:
            self.rect.x = 0




