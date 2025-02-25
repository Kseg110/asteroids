import pygame
from circleshape import CircleShape
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def draw(self, screen):
        color = (250, 250, 250)
        pygame.draw.polygon(screen, color, self.triangle(), width= 0)
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt): # player rotation method
        self.rotation += PLAYER_TURN_SPEED * dt
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_SPACE]:
            self.shoot()
            
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        # create velocity vector 
        velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        velocity *= PLAYER_SHOT_SPEED
        #create a new shot at the player position
        Shot(self.position.x, self.position.y, SHOT_RADIUS, velocity)

RED = (240, 0, 0)
class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity #stores the velocity for movement 
    def draw(self, screen):
        pygame.draw.circle(screen, RED, self.position, SHOT_RADIUS, width= 1)
    def update(self, dt):
        self.position += self.velocity * dt