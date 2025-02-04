"""asteroid class"""

import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    """Asteroid sprite"""

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        """handle shot collision"""
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        velocity_1 = self.velocity.rotate(angle) * 1.2
        velocity_2 = self.velocity.rotate(-angle) * 1.2
        radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, radius)
        asteroid_1.velocity = velocity_1
        asteroid_2.velocity = velocity_2
