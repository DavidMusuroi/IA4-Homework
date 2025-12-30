import pygame

class Bullet:
    def __init__(self, x, y, speed, damage, color):
        self.x = x
        self.y = y
        self.speed = speed
        self.damage = damage
        self.color = color
        self.width = 4
        self.height = 15
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        self.y += self.speed
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def off_screen(self):
        return self.y < 0 or self.y > 670