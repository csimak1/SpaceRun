import pygame
import json


class Spikes(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.current_state = ""

    def move(self):
        self.rect.x -= 25

    def position(self):
        '''
        this method returns the positon of the sprite to a text file
        :param = None
        :returns = None
        '''
        positionref = open("position.txt","w")
        self.current_state = " Position of Spikes = "+ "("+ str(self.rect.x)+","+ str(self.rect.y)+")"
        positionref.write(self.current_state)
        positionref.close()
