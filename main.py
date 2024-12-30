# this allows us to use code from
# the open-source pygame library
# throughout this file
# source venv/bin/activate
import pygame
from constants import *

def main():
    print("Starting asteroids!")
    pygame.init

if __name__ == "__main__":
    main()

print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
    screen.fill((0, 0, 0))
    pygame.display.flip()