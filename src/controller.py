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
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.background_pic = pygame.image.load('assets/Sprites/space.png')
        self.state = "BEGIN"
        self.hero_state = "RUN"
        self.width = width
        self.height = height
        self.white = (255,255,255)
        self.jump = True
        self.run = True
        self.hero = hero.Hero("Johnny", self.width / 3, self.height / 3, "assets/Sprites/run 1.png", "right", "RUN")
        self.wall = wall.Wall(self.width / 4, self.height - 240, 'assets/Sprites/stoneWall.png')
        self.coin = coin.Coin(self.width / 5, self.height - 240, 'assets/Sprites/goldCoin1.png')
        self.bullet = bullet.Bullet(self.hero.rect.centerx, self.hero.rect.centery,self.hero.direction,"assets/Sprites/bullet.png")


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
        background = pygame.image.load(self.background_pic)
        background_size = self.screen.get_size()
        background_rect = background.get_rect()
        background_screen = pygame.display.set_mode(background_size)
        background_screen.blit(background, background_rect)
        my_font = pygame.font.SysFont(None, 40)
        title_font = pygame.font.SysFont(None, 50)
        name_of_game = title_font.render('Space Run', False, self.white)
        instructions = my_font.render('Hit space to jump, Hit "z" to shoot. Press space to play.', False, self.white)
        background_screen.blit(name_of_game, ((self.width / 3) + 50, self.height / 4))
        background_screen.blit(instructions, ((self.width / 3) - 220, self.height / 1.5))
        pygame.display.flip()
        

    def gameLoop(self):
        while self.state == "GAME":
            background = pygame.image.load(self.background_pic)
            background_size = self.screen.get_size()
            background_rect = background.get_rect()
            background_screen = pygame.display.set_mode(background_size)
            background_screen.blit(background, background_rect)
            for img in self.hero.run_sprite:

            for event in pygame.event.get():
                pass
