"""player class definition"""

import pygame

from circleshape import CircleShape
from constants import (PLAYER_RADIUS, PLAYER_SHOOT_COOLDOWN,
                       PLAYER_SHOOT_SPEED, PLAYER_SPEED, PLAYER_TURN_SPEED)
from shot import Shot


class Player(CircleShape):
    """player sprite"""

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.__rotation = 0
        self.__shoot_timer = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.__triangle(), 2)

    def update(self, dt):
        self.__shoot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.__rotate(-dt)
        if keys[pygame.K_d]:
            self.__rotate(dt)
        if keys[pygame.K_w]:
            self.__move(dt)
        if keys[pygame.K_s]:
            self.__move(-dt)
        if keys[pygame.K_SPACE]:
            self.__shoot()

    def __triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.__rotation)
        right = pygame.Vector2(0, 1).rotate(self.__rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def __rotate(self, dt):
        self.__rotation += PLAYER_TURN_SPEED * dt

    def __move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.__rotation)
        self.position += forward * PLAYER_SPEED * dt

    def __shoot(self):
        if self.__shoot_timer > 0:
            return
        self.__shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = (
            pygame.Vector2(0, 1).rotate(self.__rotation) * PLAYER_SHOOT_SPEED
        )
