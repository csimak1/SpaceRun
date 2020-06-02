import pygame


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = "SPIN"
        self.spin_sprite = ["assets/Sprites/goldCoin1.png", "assets/Sprites/goldCoin2.png",
        "assets/Sprites/goldCoin3.png", "assets/Sprites/goldCoin4.png", "assets/Sprites/goldCoin5.png",
        "assets/Sprites/goldCoin6.png", "assets/Sprites/goldCoin7.png", "assets/Sprites/goldCoin8.png",
        "assets/Sprites/goldCoin9.png"]
        self.spin_index = 0
    def spin(self):
        '''
        this method spins the coin
        :param = None
        :returns = None
        '''
        x = self.rect.x
        y = self.rect.y
        self.image = pygame.image.load(self.spin_sprite[self.spin_index]).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # where im getting the error
        self.spin_index = (self.spin_index+1) % len(self.spin_sprite)
    def update(self):
        '''
        this method checks the state of the coin and updates it/spins it.
        :param = None
        :returns = None
        '''
        if self.state == "SPIN":
            self.spin()
    def position(self):
        '''
        this method returns the positon of the sprite to a text file
        :param = None
        :returns = None
        '''
        positionref = open("position.txt","w")
        self.current_state = " Position of Coin (x,y) = "+ "("+ str(self.rect.x)+","+ str(self.rect.y)+")"
        positionref.write(self.current_state)
        positionref.close()
