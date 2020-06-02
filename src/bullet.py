import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, img_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = direction
        self.current_state = ""

    def update(self):
        '''
        this method updates the bullet and moves it across the screen when the hero fires.
        :param = None
        :returns = None
        '''
        if self.direction == "right":
            self.rect.x += 15
    def position(self):
        '''
        this method returns the positon of the sprite to a text file
        :param = None
        :returns = None
        '''
        positionref = open("position.txt","w")
        self.current_state = " Position of Bullet = "+ "("+ str(self.rect.x)+","+ str(self.rect.y)+")"
        positionref.write(self.current_state)
        positionref.close()
