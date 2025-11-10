import sys
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *
from logger import log_state, log_event

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

# create groups
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

# create containers
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)
Shot.containers = (updatable, drawable, shots)

# create asteroid field
field = AsteroidField()

# create player
x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2
ship = Player(x, y)

# game loop
running = True

while running:
    log_state()

    # close when user hits X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill screen black
    screen.fill("black")

    # update position
    updatable.update(dt)

    for asteroid in asteroids:
        if asteroid.collides_with(ship):
            log_event("player_hit")
            print("Game over!")
            sys.exit()
        for shot in shots:
            if shot.collides_with(asteroid):
                log_event("asteroid_shot")
                shot.kill()
                asteroid.split()

    
    # draw player
    for item in drawable:
        item.draw(screen)

    # refresh screen
    pygame.display.flip()

    # defines the amount of time since last called
    # how often the loop runs; dt to seconds
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
