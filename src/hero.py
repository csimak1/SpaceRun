import pygame
import sys
from src import controller


class Hero(pygame.sprite.Sprite):
    def __init__(self, name, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = "RUN"
        self.run_sprite = ["assets/Sprites/run 1.png", "assets/Sprites/run 2.png", "assets/Sprites/run 3.png",
                           "assets/Sprites/run 4.png", "assets/Sprites/run 5.png", "assets/Sprites/run 6.png"]
        self.run_index = 0

        self.jump_up_sprite = "assets/Sprites/jump1.png"
        self.jump_down_sprite = "assets/Sprites/jump2.png"
        self.jump_index = 0
        self.run_shoot_sprite = ["assets/Sprites/runshoot1.png", "assets/Sprites/runshoot2.png",
                                 "assets/Sprites/runshoot3.png", "assets/Sprites/runshoot4.png",
                                 "assets/Sprites/runshoot5.png", "assets/Sprites/runshoot6.png"]
        self.run_shoot_index = 0
        self.run_speed = 6
        self.jump_speed = 6
        self.clock = pygame.time.Clock()
        self.jump_up = True
        self.jump_down = False

    def quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def getCoords(self):
        return str(self.rect.x) + ", " + str(self.rect.y)


    def run(self):
        '''
        this method cycles through images that make the hero look like it is running.
        :param = None
        :returns = None
        '''
        x = self.rect.x
        y = self.rect.y
        self.image = pygame.image.load(self.run_sprite[self.run_index]).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.run_index = (self.run_index+1) % len(self.run_sprite)
        self.quit()

    def col_check(self, hero , collect_list):
         return pygame.sprite.spritecollide(hero, collect_list, True, pygame.sprite.collide_rect_ratio(0.5))

    def crash_check(self, hero, obj_list):
        return pygame.sprite.spritecollide(hero, obj_list, False, pygame.sprite.collide_rect_ratio(0.5))




    def jump(self):
        '''
        this method cycles through images that make the hero look like the hero is jumping.
        :param = None
        :returns = None
        '''
        done = False
        x = self.rect.x
        y = self.rect.y
        self.image = pygame.image.load(self.jump_up_sprite).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.quit()

        if(self.jump_up):
            if(self.rect.y <= 75):
                self.jump_up = False
                self.jump_down = True
            if(self.rect.y > 75):
                self.rect.y += -35



        if(self.jump_down):
            self.image = pygame.image.load(self.jump_down_sprite).convert_alpha()
            if(self.rect.y >= 265):
                self.rect.y = 265
                self.jump_down = False
                done = True
            if(self.rect.y < 265):
                self.rect.y += 55

        if (done == True):
            self.jump_up = True
            self.state = "RUN"





    def run_shoot(self):
        '''
        this method cycles through images that make the hero look like its running and shooting.
        :param = None
        :returns = None
        '''
        x = self.rect.x
        y = self.rect.y
        self.image = pygame.image.load(self.run_shoot_sprite[self.run_shoot_index]).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.run_shoot_index = (self.run_shoot_index+1) % len(self.run_shoot_sprite)


    def position(self):
        '''
        this method returns the positon of the sprite to a text file
        :param = None
        :returns = None
        '''
        positionref = open("position.txt","w")
        self.current_state = " Position of Hero = "+ "("+ str(self.rect.x)+","+ str(self.rect.y)+")"
        positionref.write(self.current_state)
        positionref.close()
