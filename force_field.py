import pygame
class force_field:
    def __init__(self, damage, colour, coords):
        self.damage = damage
        self.colour = colour
        self.coords = coords
        self.rect = pygame.Rect(coords)

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.coords)