import pygame

from circleshape import CircleShape
from constants import *



SHOT_RADIUS = 5
SHOT_VELOCITY = 500

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, -SHOT_VELOCITY)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius)