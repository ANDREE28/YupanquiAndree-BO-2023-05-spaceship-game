import pygame,random
from game.components.enemies.enemy import Enemy

class EnemyManager:
    def __init__(self):
        self.enemies = []
    
    def update(self, game):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies,game)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        enemy_type = random.randint(1,2)
        if enemy_type == 1:
            enemy = Enemy()
        else:
            x_speed=10
            y_speed =1
            moves_before_change = [20,500]
            enemy = Enemy(enemy_type,x_speed,y_speed,moves_before_change)
        
        if len(self.enemies)<2:
            self.enemies.append(enemy)

