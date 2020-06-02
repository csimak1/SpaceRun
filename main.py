import pygame
from src import controller

def main():
    '''
    this function runs the game
    :param = None
    :returns = None
    '''
    pygame.init()
    main_window = controller.Controller()
    main_window.mainLoop()


main()
