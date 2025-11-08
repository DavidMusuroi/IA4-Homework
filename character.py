import pygame
import time

class character:
    def __init__(self, HP, damage, velocity, x, y, width, height):
        self.HP = HP
        self.damage = damage
        self.velocity = velocity
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.status = 1 #Default
        self.last_time_hit = 0
        self.rect = pygame.Rect(x, y, width, height)

    def load_spritesheet(self, filename, rot_angle, scale, width, height):
        spritesheet = pygame.image.load(filename)
        rect_spritesheet = spritesheet.get_rect()
        sprites = []

        for i in range(rect_spritesheet.width // width):
            frame = pygame.Surface((width, height), pygame.SRCALPHA)
            frame.blit(spritesheet, (0, 0), (i * width, 0, width, height))
            frame = pygame.transform.rotate(frame, rot_angle)
            frame = pygame.transform.scale(frame, scale)
            sprites.append(frame)
        return sprites

    def lose_health(self, nr):
        sec = time.time()
        if sec - self.last_time_hit >= 1:
            self.HP -= nr
            self.last_time_hit = sec
    