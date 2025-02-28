import pygame

# imports variables from constants file
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x,y)

    while True:
        # quits game if windows closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # sets screen to black
        black = (0,0,0)
        screen.fill(black)
        player.draw(screen)

        pygame.display.flip()

        # limits frame rate
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()

