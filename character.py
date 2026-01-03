import pygame
import time
import math
import random
from bullet import Bullet

class character:
    def __init__(self, HP, damage, velocity, x, y, width, height, tier, game_stats):
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
        self.tier = tier #type of enemy

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
                Bullet(self.x + self.width//2 + 10, self.y, -14, self.damage, color, 0, 1, None)
            )
            self.game_stats.shots += 1
            self.shoot_cooldown = 15

    def get_dir_to_player(self, player):
        dx = (player.x + player.width//2) - (self.x + self.width//2)
        dy = (player.y + player.height//2) - (self.y + self.height//2)

        dist = math.hypot(dx, dy)
        if dist == 0:
            return 0, 1

        return dx / dist, dy / dist

    def ai_shoot(self, color):
        match self.tier:
            case 1:
                if self.shoot_cooldown == 0:
                    self.bullets.append(
                        Bullet(self.x + self.width//2 + 10, self.y + self.height, 10, self.damage, color, 0, 1, None)
                    )
                    self.shoot_cooldown = 120

            case 2:
                if self.shoot_cooldown == 0:
                    self.bullets.append(
                        Bullet(self.x + self.width//2 + 20, self.y + self.height, 8, self.damage, color, 0, 1, None)
                    )
                    self.bullets.append(
                        Bullet(self.x + self.width//2, self.y + self.height, 8, self.damage, color, 0, 1, None)
                    )
                    self.shoot_cooldown = 100

            case 3: #sniper
                if self.shoot_cooldown == 0:
                    dx, dy = self.get_dir_to_player(self.enemies[0])
                    self.bullets.append(
                        Bullet(self.x + self.width//2 + 10, self.y + self.height, 14, self.damage, color, dx, dy, 'assets/laserBullet.png')
                    )
                    self.shoot_cooldown = 250

            case 4: #TODO
                if self.shoot_cooldown == 0:
                    self.bullets.append(
                        Bullet(self.x + self.width//2 + 10, self.y + self.height, 10, self.damage, color, 0, 1, None)
                    )
                    self.shoot_cooldown = 140

            case 5:   # boss
                if self.shoot_cooldown == 0:
                    target = random.choice(self.enemies)
                    dx, dy = self.get_dir_to_player(target)
                    self.bullets.append(
                        Bullet(self.x + self.width//2, self.y + self.height, 4, self.damage, color, dx, dy, "assets/rocket.png", target=target, turn_rate=0.06)
                    )
                    self.shoot_cooldown = 320
                if self.shoot_cooldown %90 == 0:
                    target = random.choice(self.enemies)
                    dx, dy = self.get_dir_to_player(target)
                    self.bullets.append(
                        Bullet(self.x + self.width//2, self.y + self.height, 4, self.damage, color, dx, dy, 'assets/laserBullet.png')
                    )

     
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
                    if self.tier == 0:
                        self.game_stats.shots_hit += 1
                        self.game_stats.points += 5
                    break