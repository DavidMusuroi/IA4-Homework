import pygame
import time
from bullet import Bullet

class character:
    def __init__(self, HP, damage, velocity, x, y, width, height, game_stats):
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
        self.bullets = [] #bullet list
        self.shoot_cooldown = 0
        self.enemies = [] #list of enemies
        self.game_stats = game_stats

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

    def lose_health_by_field(self, nr):
        sec = time.time()
        if sec - self.last_time_hit >= 1:
            self.HP -= nr
            self.last_time_hit = sec

    def lose_health(self, nr):
        self.HP -= nr

    def shoot(self, color):
        if self.shoot_cooldown == 0:
            self.bullets.append(
                Bullet(self.x + self.width//2 + 10, self.y, -14, self.damage, color)
            )
            self.game_stats.shots += 1
            self.shoot_cooldown = 15
    
    def update_bullets(self, screen):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

        for bullet in self.bullets[:]:
            bullet.update()
            bullet.draw(screen)

            if bullet.off_screen():
                self.bullets.remove(bullet)

    def check_hits(self):
        for bullet in self.bullets[:]:
            for enemy in self.enemies:
                if bullet.rect.colliderect(enemy.rect):
                    enemy.lose_health(bullet.damage)
                    self.bullets.remove(bullet)
                    self.game_stats.shots_hit += 1
                    self.game_stats.points += 5
                    break