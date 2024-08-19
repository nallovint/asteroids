import pygame

class CircleShape(pygame.sprite.Sprite):
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
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass


    def collide(self, other):
        # sub-classes must override
        # Each CircleShape's position property is a pygame.Vector2. Use its distance_to method to calculate the distance between the two shapes.
        if self.position.distance_to(other.position) < self.radius + other.radius:
            return True
        else:
            return False