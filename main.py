import pygame
from constants import *
from logger import log_state

def main():
    print("Starting Asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

# note: fails silently
pygame.init()

# get GUI window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# fill screen black
screen.fill("black")
pygame.display.flip()

while True:
    log_state()

    # close when user hits X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return


if __name__ == "__main__":
    main()
