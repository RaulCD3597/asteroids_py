"""player class definition"""

import pygame

from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED


class Player(CircleShape):
    """player sprite"""

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.__rotation = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.__triangle(), 2)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.__rotate(-dt)
        if keys[pygame.K_d]:
            self.__rotate(dt)

    def __triangle(self):
        """define player shape"""
        forward = pygame.Vector2(0, 1).rotate(self.__rotation)
        right = pygame.Vector2(0, 1).rotate(self.__rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def __rotate(self, dt):
        self.__rotation += PLAYER_TURN_SPEED * dt
