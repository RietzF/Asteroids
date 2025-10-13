from circleshape import *
from player import *
from constants import SHOT_RADIUS
import pygame
class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, width=2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

