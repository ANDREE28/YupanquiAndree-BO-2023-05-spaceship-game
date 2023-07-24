import pygame

from game.utils.constants import SOUND,SHIELD_TYPE,BURST
 

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
                    game.score.update()
                    self.perform_enemy_explosion(enemy.rect.center, game.screen)
                    SOUND["Burst"].set_volume(0.02)
                    SOUND["Burst"].play()
                    
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                if game.player.power_up_type != SHIELD_TYPE:
                    game.player.life -=1
                    SOUND["Burst_player"].set_volume(0.1)
                    SOUND["Burst_player"].play()
                    if game.player.life <=0:
                        self.enemy_bullets.remove(bullet)
                        self.perform_player_explosion(game.player.rect.center, game.screen)
                        game.playing = False
                        pygame.time.delay(500)
                        break
                    else:
                        self.enemy_bullets.remove(bullet)
                else:
                    self.enemy_bullets.remove(bullet)
                

    def draw(self, screen):
        for bullet in self.player_bullets:
            bullet.draw(screen)

        for bullet in self.enemy_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == 'player' and len(self.player_bullets) < 5:
            self.player_bullets.append(bullet)
        elif bullet.owner =='enemy' and len(self.enemy_bullets)<4:
            self.enemy_bullets.append(bullet)

    
    def reset(self):
        self.player_bullets = []
        self.enemy_bullets = []

    def perform_enemy_explosion(self, explosion_center, screen):
        screen.blit(BURST, BURST.get_rect(center=explosion_center))
        pygame.display.update()

    def perform_player_explosion(self, explosion_center, screen):
        screen.blit(BURST,BURST.get_rect(center=explosion_center))
        pygame.display.update()
