import sys
import pygame
import random
from src import hero
from src import bullet
from src import spikes
from src import wall
from src import coin


class Controller:
    def __init__(self, width=800, height=400):
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.background= pygame.image.load('assets/Sprites/space.png').convert_alpha()
        self.state = "BEGIN"
        self.width = width
        self.height = height
        self.white = (255,255,255)
        self.jump = True
        self.run = True
        self.hero = hero.Hero("Johnny", 100, 265, "assets/Sprites/run 1.png")
        self.wall = wall.Wall(self.width / 4, self.height - 240, 'assets/Sprites/stoneWall.png')
        self.coin = coin.Coin(self.width / 5, self.height - 240, 'assets/Sprites/goldCoin1.png')
        self.bullet = bullet.Bullet(self.hero.rect.centerx, self.hero.rect.centery,"assets/Sprites/bullet.png")
        self.all_sprites = pygame.sprite.Group()
    def quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


    def mainLoop(self):
        '''
        this method checks the state of the game and runs either the game, the game intro screen, or the game over screen.
        :param = None
        :returns = None
        '''
        while self.run:
            if self.state == "BEGIN":
                self.gameIntroScreen()
            elif self.state == "GAME":
                self.gameLoop()
            elif self.state == "LOSE":
                self.gameOverScreen()

    def gameIntroScreen(self):
        '''
        this method creates a game intro screen
        :param = None
        :returns = None
        '''
        background_size = self.screen.get_size()
        background_rect = self.background.get_rect()
        background_screen = pygame.display.set_mode(background_size)
        background_screen.blit(self.background, background_rect)
        my_font = pygame.font.SysFont(None, 40)
        title_font = pygame.font.SysFont(None, 50)
        name_of_game = title_font.render('Space Run', False, self.white)
        instructions = my_font.render('Hit space to jump, Hit "z" to shoot. Press space to play.', False, self.white)
        background_screen.blit(name_of_game, ((self.width / 3) + 50, self.height / 4))
        background_screen.blit(instructions, ((self.width / 3) - 220, self.height / 1.5))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_SPACE):
                    self.state = "GAME"
                    self.mainLoop()

    def gameLoop(self):
        x = 0
        rect_w = self.background.get_rect().width
        while self.run:
            x_end = x % rect_w
            self.screen.blit(self.background,(x_end - rect_w , 0))
            if x_end < self.width:
                self.screen.blit(self.background,(x_end , 0))
            x -= 15
            self.hero.run(self.run,self.hero,self.all_sprites,self.screen)
            pygame.display.update()
            self.clock.tick(self.FPS)
            self.quit()
