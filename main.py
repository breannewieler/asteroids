import pygame
import player
import circleshape
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

# setup frames per second; delta time dt
clock = pygame.time.Clock()
dt = 0

# game loop
running = True

# fill screen black
screen.fill("black")

# create player
x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2
player = player.Player(x, y)

# refresh screen
pygame.display.flip()

while running:
    log_state()

    # close when user hits X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.draw(screen)

    # defines the amount of time since last called
    # how often the loop runs; dt to seconds
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
