import pygame
import math

class Bullet:
    def __init__(self, x, y, speed, damage, color, dx, dy, sprite_path=None, target=None, turn_rate=None):
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
        self.sprite_original = None
        self.target = target
        self.turn_rate = turn_rate

        # if png load it
        if sprite_path:
            self.sprite = pygame.image.load(sprite_path).convert_alpha()
            self.sprite = pygame.transform.scale(self.sprite, (24, 48))
            self.sprite_original = pygame.image.load(sprite_path).convert_alpha()
            self.sprite_original = pygame.transform.scale(self.sprite, (24, 48))
            self.width = self.sprite.get_width()
            self.height = self.sprite.get_height()
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        if self.target:
            tx = self.target.x + self.target.width//2
            ty = self.target.y + self.target.height//2

            desired_dx, desired_dy = self.get_dir_to_point(tx, ty)

            self.dx += (desired_dx - self.dx) * self.turn_rate
            self.dy += (desired_dy - self.dy) * self.turn_rate

            length = (self.dx*self.dx + self.dy*self.dy) ** 0.5
            if length != 0:
                self.dx /= length
                self.dy /= length

        self.y += self.speed*self.dy
        self.x += self.speed*self.dx
        if self.target:
            # Recalculează unghiul
            angle = math.degrees(math.atan2(self.dy, self.dx)) - 90

            # Rotește sprite
            self.sprite = pygame.transform.rotate(self.sprite_original, -angle)
            self.rect = self.sprite.get_rect(center=(self.x, self.y))
        else:
            self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        if self.sprite == None:
            pygame.draw.rect(screen, self.color, self.rect)
        else:
            screen.blit(self.sprite, (self.x, self.y))

    def off_screen(self):
        return self.y < 0 or self.y > 670

    
    def get_dir_to_point(self, tx, ty):
        dx = tx - self.x
        dy = ty - self.y
        length = (dx*dx + dy*dy) ** 0.5
        if length == 0:
            return self.dx, self.dy
        return dx/length, dy/length
