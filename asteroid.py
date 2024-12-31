import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS

# from main import screen

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            angle = random.uniform(20,50)
            newangle1 = pygame.math.Vector2.rotate(self.velocity, angle)
            newangle2 = pygame.math.Vector2.rotate(self.velocity, -angle)
            newradius = self.radius - ASTEROID_MIN_RADIUS
            newast1 = Asteroid(self.position[0], self.position[1], newradius)
            newast2 = Asteroid(self.position[0], self.position[1], newradius)
            newast1.velocity = newangle1 * 1.2
            newast2.velocity = newangle2 * 1.2
            self.kill()
        