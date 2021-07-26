import sys
import pygame
import random
import time
from src import hero
from src import bullet
from src import spikes
from src import wall
from src import coin
from src import hs_data


class Controller:
    def __init__(self, width=800, height=400):
        self.screen = pygame.display.set_mode((width, height))
        self.obj_layer = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.background= pygame.image.load('assets/Sprites/space.png').convert_alpha()
        self.background2 = pygame.image.load("assets/background2.jpg").convert_alpha()
        self.game_state = "BEGIN"
        self.hero_state = "RUN"
        self.width = width
        self.height = height
        self.white = (255,255,255)
        self.alive = True
        self.hero = hero.Hero("Johnny", 50, 265, "assets/Sprites/run 1.png")
        self.wall = wall.Wall(random.randrange(400,801,255), 255, 'assets/Sprites/stoneWall.png')
        self.coin = coin.Coin(random.randrange(400,801,265), 255, 'assets/Sprites/goldCoin1.png')
        self.spikes = spikes.Spikes(random.randrange(300,701,275), 255,'assets/Sprites/spike.png' )
        self.bullet = None
        self.x = 0
        self.all_sprites = pygame.sprite.Group((self.hero),)
        self.clock = pygame.time.Clock()
        self.game_speed = 10
        self.obj_list = []
        self.obj_sprites = pygame.sprite.Group()
        self.collect = pygame.sprite.Group()
        self.t0 = time.time()
        self.score_count = 0
        self.music_state = None
        self.space_sound = pygame.mixer.Sound("assets/game_sound.mp3")
        self.coin_sound = pygame.mixer.Sound("assets/coin_sound.wav")


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
        my_font = pygame.font.SysFont("impact", 30)
        title_font = pygame.font.SysFont("impact", 30)
        name_of_game = title_font.render('Space Run', False, self.white)
        instructions = my_font.render('Hit space to jump  Hit "z" to shoot  Press space to play.', False, self.white)
        background_screen.blit(name_of_game, ((self.width / 3) + 50, self.height / 4))
        background_screen.blit(instructions, ((self.width / 3) - 200, self.height / 1.5))
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
        self.x -= 4

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()



    def draw_obstacles(self):
        t1 = time.time()

        if (((int(t1) - int(self.t0)) % 7 ) == 0) and (not self.wall.alive()) and (not self.spikes.alive()) and (not self.coin.alive()) :
            self.wall = wall.Wall(random.randrange(400,2500), 255, 'assets/Sprites/stoneWall.png')
            self.coin = coin.Coin(random.randrange(400,2500), 265, 'assets/Sprites/goldCoin1.png')
            self.spikes = spikes.Spikes(random.randrange(400,2500), 275,'assets/Sprites/spike.png' )
            self.obj_sprites.add(self.wall, self.spikes)
            self.collect.add(self.coin)

    def sound(self):
        if self.music_state == None:
            self.space_sound.play(-1)
            self.music_state = 1


    def gameLoop(self):
        while self.alive:
            # set up music
            pygame.mixer.init()
            pygame.mixer.music.set_volume(0.25)
            self.sound()
            score = time.time()
            # Set the score multiplyer
            if (int(score) - int(self.t0)) % 2 == 0:
                mult = random.randrange(0,3)
                self.score_count += mult
            myfont = pygame.font.SysFont('impact', 40)
            message = myfont.render('Score: '+ str(self.score_count), False, (255,255,255))
            self.screen.blit(message,[600, 30])
            pygame.display.flip()
            self.clock.tick(self.game_speed)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_SPACE):
                            self.hero.state = "JUMP"
                    elif(event.key == pygame.K_z and self.hero.state != "JUMP" ):
                        self.hero.state = "R_SHOOT"
                        if self.bullet is not None:
                            self.bullet.kill()
                        self.bullet = bullet.Bullet(self.hero.rect.centerx, self.hero.rect.centery + -15,"assets/Sprites/bullet.png")
                        self.all_sprites.add(self.bullet)
                    elif event.type == pygame.QUIT:
                        sys.exit()
            #collisions
            if self.bullet is not None:
                hits = pygame.sprite.spritecollide(self.bullet, self.obj_sprites, True)

            else:
                hits = False
            if (hits):
                for obj in hits:
                    print(obj)
                    obj.kill()
                    self.obj_sprites.update()
            self.draw_background()
            self.draw_obstacles()
            if self.hero.state == "RUN":
                self.hero.run()
            if self.hero.state == "JUMP":
                self.hero.jump()
            if self.hero.state == "R_SHOOT":
                self.hero.run_shoot()
                self.bullet.update()
                if self.bullet.rect.x > 800:
                    self.hero.state = "RUN"

            self.wall.move()
            self.coin.move()
            self.spikes.move()


            if self.wall.rect.x < 0:
                self.wall.kill()
            if self.spikes.rect.x < 0:
                self.spikes.kill()
            if self.coin.rect.x < 0:
                self.coin.kill()

            if self.hero.col_check(self.hero,self.collect):
                self.score_count += 1
                self.coin_sound.play()

            if self.hero.crash_check(self.hero, self.obj_sprites):
                self.game_state = "LOSE"
                hs_data.enter_score(self.score_count)
                self.mainLoop()




            #update screen
            self.obj_sprites.update()
            self.obj_sprites.draw(self.obj_layer)
            self.all_sprites.update()
            self.all_sprites.draw(self.screen)
            self.collect.update()
            self.collect.draw(self.screen)
            pygame.display.flip()

    def gameOverScreen(self):
        background_size = self.screen.get_size()
        background_rect = self.background2.get_rect()
        background_screen = pygame.display.set_mode(background_size)
        background_screen.blit(self.background2, background_rect)
        top_five = hs_data.top_five()
        data_font = pygame.font.SysFont("impact", 30)
        title_font = pygame.font.SysFont("impact", 50)
        game_over = title_font.render('GAME OVER!', False, (255,0,0))
        your_score = data_font.render('Your Score: '+ str(self.score_count), False, self.white)
        leaders = title_font.render('LEADERBOARD' , False, self.white)
        first = data_font.render('1: '+ str(top_five[0]), False, self.white)
        second = data_font.render('2: '+ str(top_five[1]), False, self.white)
        third = data_font.render('3: '+ str(top_five[2]), False, self.white)
        fourth = data_font.render('4: '+ str(top_five[3]), False, self.white)
        fifth = data_font.render('5: '+ str(top_five[4]), False, self.white)
        background_screen.blit(game_over, (75, 20))
        background_screen.blit(your_score, (75, 100))
        background_screen.blit(leaders, (350, 20))
        background_screen.blit(first, (350, 100))
        background_screen.blit(second, (350, 150))
        background_screen.blit(third, (350, 200))
        background_screen.blit(fourth, (350, 250))
        background_screen.blit(fifth, (350, 300))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                sys.exit()


