import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.containers = None
        self.kind = None


    def update(self, dt):
        self.position += self.velocity * dt
    

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_velocity = self.velocity.rotate(random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid.velocity = new_velocity * 1.2
            new_asteroid.containers = self.containers

            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2.velocity = new_velocity * -1.2
            new_asteroid2.containers = self.containers