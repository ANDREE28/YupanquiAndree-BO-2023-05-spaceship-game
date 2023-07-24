import pygame
from game.utils.constants import SOUND_BACKGROUND, SOUND_IMAGE

class SoundManager:
    def __init__(self):
       pygame.mixer.music.load(SOUND_BACKGROUND)
       pygame.mixer.music.play(-1)

       self.volume_image = SOUND_IMAGE["sound_up"]  # Start with the volume up image

    def update(self, user_input):
        # Baja Volumen
        if user_input[pygame.K_9] and pygame.mixer.music.get_volume() > 0.0:
            self.volumen_down()
            print("baja")
        elif user_input[pygame.K_9] and pygame.mixer.music.get_volume() == 0.0:
            self.volumen_muted()
            print("m")
        
        # Sube volumen
        if user_input[pygame.K_0] and pygame.mixer.music.get_volume() < 1.0:
            self.volumen_up()
            print("sube")
        elif user_input[pygame.K_0] and pygame.mixer.music.get_volume() == 1.0:
            self.volumen_max()
            print("max")

 

    def volumen_down(self):
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01)
        self.update_volume_image()

    def volumen_up(self):
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
        self.update_volume_image()

    def volumen_muted(self):
        pygame.mixer.music.set_volume(0.0)  # Establece el volumen en 0 para desactivar el sonido.
        self.volume_image = SOUND_IMAGE["sound_mute"]

    def volumen_max(self):
        pygame.mixer.music.set_volume(1.0)  # Establece el volumen al máximo (1.0).
        self.volume_image = SOUND_IMAGE["sound_max"]

    def update_volume_image(self):
        volume = pygame.mixer.music.get_volume()
        if volume == 0.0:
            self.volume_image = SOUND_IMAGE["sound_mute"]
        elif volume == 1.0:
            self.volume_image = SOUND_IMAGE["sound_max"]
        elif volume > 0.5:
            self.volume_image = SOUND_IMAGE["sound_up"]
        else:
            self.volume_image = SOUND_IMAGE["sound_down"]
