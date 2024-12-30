# this allows us to use code from
# the open-source pygame library
# throughout this file
# source venv/bin/activate
import pygame
from constants import *
from player import Player

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
Player.containers = (updateable, drawable)

player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    screen.fill((0, 0, 0))

    for thing in updateable:
        thing.update(dt)
    for thingie in drawable:
        thingie.draw(screen)
    # player.update(dt)
    # player.draw(screen)

    pygame.display.flip()
    # clock.tick(60)
    dt = clock.tick(60)/1000
