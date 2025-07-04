import pygame
from constants import *
from circleshape import CircleShape

class Shoot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 0)  

    def update(self, dt):
        self.position += self.velocity * dt
    