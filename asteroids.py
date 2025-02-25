import pygame
from circleshape import CircleShape
from constants import *

WHITE = (250, 250, 250)

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, width= 2)