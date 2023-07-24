import pygame

from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH, BACKGROUND

class Menu:
    SCREEN_HALF_HEIGHT = SCREEN_HEIGHT / 2
    SCREEN_HALF_WIDTH = SCREEN_WIDTH / 2

    def __init__(self):
        self.background_image = BACKGROUND
        self.font = pygame.font.Font(FONT_STYLE, 30)
    
    def update(self, game):
        pygame.display.update()
        self.handle_events(game)

    def draw(self, screen):
        screen.blit(self.text, self.rect)
    
    def handle_events(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            if event.type == pygame.KEYDOWN:
                game.run()
    
    def reset_screen(self, screen):
        screen.blit(pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
    
    def draw(self,screen, message,x=SCREEN_HALF_WIDTH,y=SCREEN_HALF_HEIGHT,color = (255,255,255)):
        text = self.font.render(message,True,color)
        text_rect = text.get_rect()
        text_rect.center = (x,y)
        screen.blit(text, text_rect)