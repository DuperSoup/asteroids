# this allows us to use code from
# the open-source pygame library
# throughout this file
# source venv/bin/activate
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    pygame.init

if __name__ == "__main__":
    main()

print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0

updateable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
Player.containers = (updateable, drawable)
Asteroid.containers = (asteroids, updateable, drawable)
AsteroidField.containers = (updateable)
Shot.containers = (shots, updateable, drawable)

player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
asteroidfield = AsteroidField()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    screen.fill((0, 0, 0))

    for thing in updateable:
        thing.update(dt)
    for thingie in drawable:
        thingie.draw(screen)
    for ast in asteroids:
        for sh in shots:
            if ast.collision(sh):
                sh.kill()
                ast.split()

        if ast.collision(player):
            print("Game over!")
            sys.exit()        


    pygame.display.flip()
    dt = clock.tick(60)/1000
