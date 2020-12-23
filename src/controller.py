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
        self.FPS = 30
        self.background= pygame.image.load('assets/Sprites/space.png').convert_alpha()
        self.game_state = "BEGIN"
        self.hero_state = "RUN"
        self.width = width
        self.height = height
        self.white = (255,255,255)
        self.alive = True
        self.hero = hero.Hero("Johnny", 100, 265, "assets/Sprites/run 1.png")
        self.wall = wall.Wall(self.width / 4, self.height - 240, 'assets/Sprites/stoneWall.png')
        self.coin = coin.Coin(self.width / 5, self.height - 240, 'assets/Sprites/goldCoin1.png')
        self.bullet = None
        self.x = 0
        self.all_sprites = pygame.sprite.Group((self.hero),)
        self.clock = pygame.time.Clock()
        self.game_speed = 10


    def mainLoop(self):
        '''
        this method checks the state of the game and runs either the game, the game intro screen, or the game over screen.
        :param = None
        :returns = None
        '''
        while self.alive:
            if self.game_state == "BEGIN":
                self.gameIntroScreen()
            elif self.game_state == "GAME":
                self.gameLoop()
            elif self.game_state == "LOSE":
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
                    self.game_state = "GAME"
                    self.mainLoop()
    def draw_background(self):
        rect_w = self.background.get_rect().width
        x_end = self.x % rect_w
        self.screen.blit(self.background,(x_end - rect_w , 0))
        if x_end < self.width:
            self.screen.blit(self.background,(x_end , 0))
        self.x -= 20

    def gameLoop(self):
        while self.alive:
            self.clock.tick(self.game_speed)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_SPACE):
                            self.hero.state = "JUMP"
                    elif(event.key == pygame.K_z and self.hero.state != "JUMP" ):
                        self.hero.state = "R_SHOOT"
                        if self.bullet is not None:
                            self.bullet.kill()
                        self.bullet = bullet.Bullet(self.hero.rect.centerx, self.hero.rect.centery,"assets/Sprites/bullet.png")
                        self.all_sprites.add(self.bullet)
                    elif event.type == pygame.QUIT:
                        sys.exit()
            self.draw_background()
            if self.hero.state == "RUN":
                self.hero.run()
            if self.hero.state == "JUMP":
                self.hero.jump()
            if self.hero.state == "R_SHOOT":
                self.hero.run_shoot()
                self.bullet.update()
                if self.bullet.rect.x > 800:
                    self.hero.state = "RUN"
            self.all_sprites.update()
            self.all_sprites.draw(self.screen)
            pygame.display.flip()
