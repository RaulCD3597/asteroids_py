"""module to represent a circle"""

import pygame


class CircleShape(pygame.sprite.Sprite):
    """Base class for game objects"""

    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        """draw shape in screen"""
        # sub-classes must override
        pass

    def update(self, dt):
        """update circle in screen"""
        # sub-classes must override
        pass

    def collides_with(self, other):
        """check if is collisioning with another circle"""
        return self.position.distance_to(other.position) <= self.radius + other.radius
