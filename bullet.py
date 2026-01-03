import pygame

class Bullet:
    def __init__(self, x, y, speed, damage, color, dx, dy, sprite_path=None):
        self.x = x
        self.y = y
        self.speed = speed
        self.damage = damage
        self.color = color
        self.width = 4
        self.height = 15
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.dx = dx
        self.dy = dy
        self.sprite = None

        # if png load it
        if sprite_path:
            self.sprite = pygame.image.load(sprite_path).convert_alpha()
            self.width = self.sprite.get_width()
            self.height = self.sprite.get_height()
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        self.y += self.speed*self.dy
        self.x += self.speed*self.dx
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        if self.sprite == None:
            pygame.draw.rect(screen, self.color, self.rect)
        else:
            screen.blit(self.sprite, (self.x, self.y))

    def off_screen(self):
        return self.y < 0 or self.y > 670