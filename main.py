import pygame
from labyrinth import Labyrinth
from maze import Game

# globals 
SIZE = 20 
def main() :
    
    pygame.display.init()
    game = Game(SIZE)
    game.run()
    pygame.display.quit()

if __name__ == "__main__" :
    main()