import pygame, random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        velo1 = self.velocity.rotate(angle)
        velo2 = self.velocity.rotate(-angle)
        Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS).velocity = velo1 * 1.2
        Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS).velocity = velo2 * 1.2