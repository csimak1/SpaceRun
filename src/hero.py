import pygame
from src import controller


class Hero(pygame.sprite.Sprite):
    def __init__(self, name, x, y, image,direction):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = direction
        self.obj = controller.Controller()
        self.state = self.obj.hero_state
        self.screen = self.obj.screen
        self.run_sprite = ["assets/Sprites/run 1.png", "assets/Sprites/run 2.png", "assets/Sprites/run 3.png",
                           "assets/Sprites/run 4.png", "assets/Sprites/run 5.png", "assets/Sprites/run 6.png"]
        self.run_index = 0

        self.jump_sprite = ["assets/Sprites/jump1.png"*10,"assets/Sprites/jump2.png"*10]


        self.jump_sprite = ["assets/Sprites/jump1.png", "assets/Sprites/jump2.png"]

        self.jump_index = 0
        self.run_shoot_sprite = ["assets/Sprites/runshoot1.png", "assets/Sprites/runshoot2.png",
                                 "assets/Sprites/runshoot3.png", "assets/Sprites/runshoot4.png",
                                 "assets/Sprites/runshoot5.png", "assets/Sprites/runshoot6.png"]
        self.run_shoot_index = 0


    def run(self):
        '''
        this method cycles through images that make the hero look like it is running.
        :param = None
        :returns = None
        '''
        x = self.rect.x
        y = self.rect.y
        while self.state == "RUN":
            self.image = pygame.image.load(self.run_sprite[self.run_index]).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.run_index = (self.run_index+1) % len(self.run_sprite)





    def jump(self):
        '''
        this method cycles through images that make the hero look like the hero is jumping.
        :param = None
        :returns = None
        '''
        x = self.rect.x
        y = self.rect.y
        while self.state == "JUMP":
            self.image = pygame.image.load(self.jump_sprite[self.jump_index]).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.jump_index = (self.jump_index+1) % len(self.jump_sprite)
            if self.jump_index < 10:
                self.rect.y -= 10
            elif self.jump_index > 10:
                self.rect.y += 10
            else:
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
