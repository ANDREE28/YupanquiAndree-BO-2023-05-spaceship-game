import pygame

from game.utils.constants import SOUND

class BulletManager:
    def __init__(self):
        self.player_bullets = []
        self.enemy_bullets = []
    
    def update(self, game):
        for bullet in self.player_bullets:
            bullet.update(self.player_bullets)

            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner =='player':
                    game.enemy_manager.enemies.remove(enemy)
                    self.player_bullets.remove(bullet)
                    game.increase_score()
                    SOUND["Burst"].set_volume(0.02)
                    SOUND["Burst"].play()

        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                self.enemy_bullets.remove(bullet)
                game.increase_death_counter()
                game.playing = False
                pygame.time.delay(500)
                break

    def draw(self, screen):
        for bullet in self.player_bullets:
            bullet.draw(screen)

        for bullet in self.enemy_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == 'player' and len(self.player_bullets) < 5:
            self.player_bullets.append(bullet)
        elif bullet.owner =='enemy' and len(self.enemy_bullets)<2:
            self.enemy_bullets.append(bullet)

    
    def reset(self):
        self.player_bullets = []
        self.enemy_bullets = []