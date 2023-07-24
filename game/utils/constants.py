import pygame
import os
pygame.mixer.init()
# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
HEART_TYPE = 'heart'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
ENEMY_3 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_3.png"))
BURST = pygame.image.load(os.path.join(IMG_DIR, "Enemy/burst.png"))

SOUND_BACKGROUND =os.path.join(IMG_DIR,"Sound/Sound_background.mp3")
SOUND = {
   "Shoothing" : pygame.mixer.Sound(os.path.join(IMG_DIR, "Sound/shooting.wav")),
   "Burst": pygame.mixer.Sound(os.path.join(IMG_DIR, "Sound/burst.wav")),
   "shield": pygame.mixer.Sound(os.path.join(IMG_DIR,"Sound/shield.wav")),
   "heart":pygame.mixer.Sound(os.path.join(IMG_DIR,"Sound/heart.wav")),
   "Burst_player": pygame.mixer.Sound(os.path.join(IMG_DIR, "Sound/burst_player.wav")),
}

SOUND_IMAGE = {
    "sound_up":pygame.image.load(os.path.join(IMG_DIR,"Sound_image/volume_up.png")),
    "sound_down":pygame.image.load(os.path.join(IMG_DIR,"Sound_image/volume_down.png")),
    "sound_mute":pygame.image.load(os.path.join(IMG_DIR,"Sound_image/volume_muted.png")),
    "sound_max":pygame.image.load(os.path.join(IMG_DIR,"Sound_image/volume_max.png"))
}
BACKGROUND = pygame.image.load(os.path.join(IMG_DIR, "Other/background.png"))


FONT_STYLE = os.path.join(IMG_DIR, "text/Amuro.otf")
FONT_SIZE = 24
