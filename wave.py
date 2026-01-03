import pygame
from character import character
from get_font import get_font

def check_for_enemies(p1,p2,screen, game_stats):
    if len(p1.enemies) != 0 or len(p2.enemies) != 0:
        okay = False
        for enemy in p1.enemies[:]:
            if enemy.HP > 0:
                okay = True
                screen.blit(enemy.sprite, (enemy.x, enemy.y))
            else:
                p1.enemies.remove(enemy)
                game_stats.points += 20
                game_stats.enemies_destroyed += 1
        for enemy in p2.enemies[:]:
            if enemy.HP > 0:
                okay = True
                screen.blit(enemy.sprite, (enemy.x, enemy.y))
            else:
                p2.enemies.remove(enemy)
                game_stats.points += 20
                game_stats.enemies_destroyed += 1
        return okay
    else:
        return False

def mirror_x(x, w):
    return SCREEN_W - x - w

def load_enemies(wave_nr,p1,p2,screen, game_stats):
    if wave_nr == 1:
        # Enemies of player 1
        # Tier 1, Enemy 1
        t1_e1_p1 = character(10, 5, 1, 10, 90, 60, 40, 1, game_stats)
        t1_e1_p1.sprite = pygame.image.load('assets/enemies/Ship1.png').convert_alpha()
        # Tier 1, Enemy 2
        t1_e2_p1 = character(10, 5, 1, 60, 130, 60, 40, 1, game_stats)
        t1_e2_p1.sprite = pygame.image.load('assets/enemies/Ship1.png').convert_alpha()
        # Tier 1, Enemy 3
        t1_e3_p1 = character(10, 5, 1, 110, 90, 60, 40, 1, game_stats)
        t1_e3_p1.sprite = pygame.image.load('assets/enemies/Ship1.png').convert_alpha()
        # Tier 2, Enemy 1
        t2_e1_p1 = character(10, 8, 2, 160, 10, 70, 40, 2, game_stats)
        t2_e1_p1.sprite = pygame.image.load('assets/enemies/Ship2.png').convert_alpha()
        # Resize hitbox
        t2_e1_p1.rect = pygame.Rect(t2_e1_p1.x + 25, t2_e1_p1.y + 30, t2_e1_p1.width, t2_e1_p1.height)
        # Tier 3, Enemy 1
        t3_e1_p1 = character(10, 10, 3, 250, 0, 70, 40, 3, game_stats)
        t3_e1_p1.sprite = pygame.image.load('assets/enemies/Ship3.png').convert_alpha()
        # Resize hitbox
        t3_e1_p1.rect = pygame.Rect(t3_e1_p1.x + 30, t3_e1_p1.y + 30, t3_e1_p1.width, t3_e1_p1.height)
        # Tier 2, Enemy 2
        t2_e2_p1 = character(10, 8, 2, 340, 10, 70, 40, 2, game_stats)
        t2_e2_p1.sprite = pygame.image.load('assets/enemies/Ship2.png').convert_alpha()
        # Resize hitbox
        t2_e2_p1.rect = pygame.Rect(t2_e2_p1.x + 25, t2_e2_p1.y + 30, t2_e2_p1.width, t2_e2_p1.height)
        # Tier 1, Enemy 4
        t1_e4_p1 = character(10, 5, 1, 430, 90, 60, 40, 1, game_stats)
        t1_e4_p1.sprite = pygame.image.load('assets/enemies/Ship1.png').convert_alpha()
        # Tier 1, Enemy 5
        t1_e5_p1 = character(10, 5, 1, 490, 130, 60, 40, 1, game_stats)
        t1_e5_p1.sprite = pygame.image.load('assets/enemies/Ship1.png').convert_alpha()
        # Tier 1, Enemy 6
        t1_e6_p1 = character(10, 5, 1, 550, 90, 60, 40, 1, game_stats)
        t1_e6_p1.sprite = pygame.image.load('assets/enemies/Ship1.png').convert_alpha()

        #Enemies of p2
        t1_e1_p2 = character(10, 5, 1, 1280 - 10 - 60, 90, 60, 40, 1, game_stats)
        t1_e1_p2.sprite = pygame.image.load('assets/enemies/Ship1.png').convert_alpha()

        t1_e2_p2 = character(10, 5, 1, 1280 - 60 - 60, 130, 60, 40, 1, game_stats)
        t1_e2_p2.sprite = pygame.image.load('assets/enemies/Ship1.png').convert_alpha()

        t1_e3_p2 = character(10, 5, 1, 1280 - 110 - 60, 90, 60, 40, 1, game_stats)
        t1_e3_p2.sprite = pygame.image.load('assets/enemies/Ship1.png').convert_alpha()

        t2_e1_p2 = character(10, 8, 2, 1280 - 160 - 70, 10, 70, 40, 2, game_stats)
        t2_e1_p2.sprite = pygame.image.load('assets/enemies/Ship2.png').convert_alpha()
        t2_e1_p2.rect = pygame.Rect(t2_e1_p2.x + 25, t2_e1_p2.y + 30, t2_e1_p2.width, t2_e1_p2.height)

        t3_e1_p2 = character(10, 10, 3, 1280 - 250 - 70, 0, 70, 40, 3, game_stats)
        t3_e1_p2.sprite = pygame.image.load('assets/enemies/Ship3.png').convert_alpha()
        t3_e1_p2.rect = pygame.Rect(t3_e1_p2.x + 30, t3_e1_p2.y + 30, t3_e1_p2.width, t3_e1_p2.height)

        t2_e2_p2 = character(10, 8, 2, 1280 - 340 - 70, 10, 70, 40, 2, game_stats)
        t2_e2_p2.sprite = pygame.image.load('assets/enemies/Ship2.png').convert_alpha()
        t2_e2_p2.rect = pygame.Rect(t2_e2_p2.x + 25, t2_e2_p2.y + 30, t2_e2_p2.width, t2_e2_p2.height)

        t1_e4_p2 = character(10, 5, 1, 1280 - 430 - 60, 90, 60, 40, 1, game_stats)
        t1_e4_p2.sprite = pygame.image.load('assets/enemies/Ship1.png').convert_alpha()

        t1_e5_p2 = character(10, 5, 1, 1280 - 490 - 60, 130, 60, 40, 1, game_stats)
        t1_e5_p2.sprite = pygame.image.load('assets/enemies/Ship1.png').convert_alpha()

        t1_e6_p2 = character(10, 5, 1, 1280 - 550 - 60, 90, 60, 40, 1, game_stats)
        t1_e6_p2.sprite = pygame.image.load('assets/enemies/Ship1.png').convert_alpha()


        # Add enemies to list of enemies
        p1.enemies.extend([
            t1_e1_p1, t1_e2_p1, t1_e3_p1,
            t2_e1_p1, t3_e1_p1, t2_e2_p1,
            t1_e4_p1, t1_e5_p1, t1_e6_p1
        ])

        p2.enemies.extend([
            t1_e1_p2, t1_e2_p2, t1_e3_p2,
            t2_e1_p2, t3_e1_p2, t2_e2_p2,
            t1_e4_p2, t1_e5_p2, t1_e6_p2
        ])

    elif wave_nr == 2:
        # Enemies of player 1
        # Tier 2, Enemy 1
        t2_e1_p1 = character(10, 8, 2, 0, 60, 70, 40, 2, game_stats)
        t2_e1_p1.sprite = pygame.image.load('assets/enemies/Ship2.png').convert_alpha()
        # Resize hitbox
        t2_e1_p1.rect = pygame.Rect(t2_e1_p1.x + 25, t2_e1_p1.y + 30, t2_e1_p1.width, t2_e1_p1.height)
        # Tier 3, Enemy 1
        t3_e1_p1 = character(10, 10, 3, 80, 30, 70, 40, 3, game_stats)
        t3_e1_p1.sprite = pygame.image.load('assets/enemies/Ship3.png').convert_alpha()
        # Resize hitbox
        t3_e1_p1.rect = pygame.Rect(t3_e1_p1.x + 30, t3_e1_p1.y + 30, t3_e1_p1.width, t3_e1_p1.height)
        # Tier 4, Enemy 1
        t4_e1_p1 = character(10, 12, 4, 215, 0, 90, 40, 4, game_stats)
        t4_e1_p1.sprite = pygame.image.load('assets/enemies/Ship4.png').convert_alpha()
        # Resize hitbox
        t4_e1_p1.rect = pygame.Rect(t4_e1_p1.x + 20, t4_e1_p1.y + 30, t4_e1_p1.width, t4_e1_p1.height)
        # Tier 3, Enemy 2
        t3_e2_p1 = character(10, 10, 3, 345, 30, 70, 40, 3, game_stats)
        t3_e2_p1.sprite = pygame.image.load('assets/enemies/Ship3.png').convert_alpha()
        # Resize hitbox
        t3_e2_p1.rect = pygame.Rect(t3_e2_p1.x + 30, t3_e2_p1.y + 30, t3_e2_p1.width, t3_e2_p1.height)
        # Tier 2, Enemy 2
        t2_e2_p1 = character(10, 8, 2, 450, 60, 70, 40, 2, game_stats)
        t2_e2_p1.sprite = pygame.image.load('assets/enemies/Ship2.png').convert_alpha()
        # Resize hitbox
        t2_e2_p1.rect = pygame.Rect(t2_e2_p1.x + 25, t2_e2_p1.y + 30, t2_e2_p1.width, t2_e2_p1.height)


        # Enemies of player 2
        t2_e1_p2 = character(10, 8, 2, 1280 - 0   - 120, 60, 70, 40, 2, game_stats)
        t2_e1_p2.sprite = pygame.image.load('assets/enemies/Ship2.png').convert_alpha()
        t2_e1_p2.rect = pygame.Rect(t2_e1_p2.x + 25, t2_e1_p2.y + 30, t2_e1_p2.width, t2_e1_p2.height)

        t3_e1_p2 = character(10, 10, 3, 1280 - 80  - 120, 30, 70, 40, 3, game_stats)
        t3_e1_p2.sprite = pygame.image.load('assets/enemies/Ship3.png').convert_alpha()
        t3_e1_p2.rect = pygame.Rect(t3_e1_p2.x + 30, t3_e1_p2.y + 30, t3_e1_p2.width, t3_e1_p2.height)

        t4_e1_p2 = character(10, 12, 4, 1280 - 215 - 140, 0, 90, 40, 4, game_stats)
        t4_e1_p2.sprite = pygame.image.load('assets/enemies/Ship4.png').convert_alpha()
        t4_e1_p2.rect = pygame.Rect(t4_e1_p2.x + 20, t4_e1_p2.y + 30, t4_e1_p2.width, t4_e1_p2.height)

        t3_e2_p2 = character(10, 10, 3, 1280 - 345 - 120, 30, 70, 40, 3, game_stats)
        t3_e2_p2.sprite = pygame.image.load('assets/enemies/Ship3.png').convert_alpha()
        t3_e2_p2.rect = pygame.Rect(t3_e2_p2.x + 30, t3_e2_p2.y + 30, t3_e2_p2.width, t3_e2_p2.height)

        t2_e2_p2 = character(10, 8, 2, 1280 - 450 - 120, 60, 70, 40, 2, game_stats)
        t2_e2_p2.sprite = pygame.image.load('assets/enemies/Ship2.png').convert_alpha()
        t2_e2_p2.rect = pygame.Rect(t2_e2_p2.x + 25, t2_e2_p2.y + 30, t2_e2_p2.width, t2_e2_p2.height)

        # Add enemies to list of enemies
        p1.enemies.extend([
            t2_e1_p1, t3_e1_p1, t4_e1_p1, t3_e2_p1, t2_e2_p1
        ])

        p2.enemies.extend([
            t2_e1_p2, t3_e1_p2, t4_e1_p2, t3_e2_p2, t2_e2_p2
        ])

    
    elif wave_nr == 3:
        # Enemies of BOTH PLAYERS
        # Tier 1, Enemy 1
        t1_e1 = character(10, 5, 1, 60, 60, 60, 40, 1, game_stats)
        t1_e1.sprite = pygame.image.load('assets/enemies/Ship1.png').convert_alpha()
        # Tier 2, Enemy 1
        t2_e1 = character(10, 8, 2, 100, 90, 70, 40, 2, game_stats)
        t2_e1.sprite = pygame.image.load('assets/enemies/Ship2.png').convert_alpha()
        # Resize hitbox
        t2_e1.rect = pygame.Rect(t2_e1.x + 25, t2_e1.y + 30, t2_e1.width, t2_e1.height)
        # Tier 3, Enemy 1
        t3_e1 = character(10, 10, 3, 200, 100, 70, 40, 3, game_stats)
        t3_e1.sprite = pygame.image.load('assets/enemies/Ship3.png').convert_alpha()
        # Resize hitbox
        t3_e1.rect = pygame.Rect(t3_e1.x + 30, t3_e1.y + 30, t3_e1.width, t3_e1.height)
        # Tier 4, Enemy 1
        t4_e1 = character(10, 12, 4, 310, 70, 90, 40, 4, game_stats)
        t4_e1.sprite = pygame.image.load('assets/enemies/Ship4.png').convert_alpha()
        # Resize hitbox
        t4_e1.rect = pygame.Rect(t4_e1.x + 20, t4_e1.y + 30, t4_e1.width, t4_e1.height)
        # FINAL BOSS
        BOSS = character(500, 20, 5, 465, 0, 350, 150, 5, game_stats)
        # Load sprite cu alpha (transparență)
        BOSS.sprite = pygame.image.load("assets/enemies/Boss.png").convert_alpha()
        BOSS.sprite = pygame.transform.scale(BOSS.sprite, (350, 150))
        BOSS.rect = pygame.Rect(BOSS.x + 40, BOSS.y + 30, 270, 90)
        # Tier 4, Enemy 2 (mirror of t4_e1)
        t4_e2 = character(10, 12, 4, 840, 70, 90, 40, 4, game_stats)
        t4_e2.sprite = pygame.image.load('assets/enemies/Ship4.png').convert_alpha()
        t4_e2.rect = pygame.Rect(t4_e2.x + 20, t4_e2.y + 30, t4_e2.width, t4_e2.height)

        # Tier 3, Enemy 2 (mirror of t3_e1)
        t3_e2 = character(10, 10, 3, 960, 100, 70, 40, 3, game_stats)
        t3_e2.sprite = pygame.image.load('assets/enemies/Ship3.png').convert_alpha()
        t3_e2.rect = pygame.Rect(t3_e2.x + 30, t3_e2.y + 30, t3_e2.width, t3_e2.height)

        # Tier 2, Enemy 2 (mirror of t2_e1)
        t2_e2 = character(10, 8, 2, 1060, 90, 70, 40, 2, game_stats)
        t2_e2.sprite = pygame.image.load('assets/enemies/Ship2.png').convert_alpha()
        t2_e2.rect = pygame.Rect(t2_e2.x + 25, t2_e2.y + 30, t2_e2.width, t2_e2.height)

        # Tier 1, Enemy 2 (mirror of t1_e1)
        t1_e2 = character(10, 5, 1, 1160, 60, 60, 40, 1, game_stats)
        t1_e2.sprite = pygame.image.load('assets/enemies/Ship1.png').convert_alpha()

        # Add enemies to list of enemies
        p1.enemies.append(t1_e1)
        p1.enemies.append(t2_e1)
        p1.enemies.append(t3_e1)
        p1.enemies.append(t4_e1)
        p1.enemies.append(BOSS)
        p1.enemies.append(t4_e2)
        p1.enemies.append(t3_e2)
        p1.enemies.append(t2_e2)
        p1.enemies.append(t1_e2)

        p2.enemies.append(t1_e1)
        p2.enemies.append(t2_e1)
        p2.enemies.append(t3_e1)
        p2.enemies.append(t4_e1)
        p2.enemies.append(BOSS)
        p2.enemies.append(t4_e2)
        p2.enemies.append(t3_e2)
        p2.enemies.append(t2_e2)
        p2.enemies.append(t1_e2)
    
    #add p1, p2 as enemies to the enemies
    for enemy in p1.enemies:
        enemy.enemies.append(p1)
    for enemy in p2.enemies:
        enemy.enemies.append(p2)

def draw_wave_text(screen, wave_nr, wave_text_time):
    if wave_text_time>=900:
        font = get_font(100)
    else:
        font = get_font(wave_text_time * 100 //800)

    if wave_nr == 3:
        text = "FINAL BOSS"
    else:
        text = f"WAVE {wave_nr}"

    surf = font.render(text, True, (255, 80, 80))
    rect = surf.get_rect(center=(640, 320))
    screen.blit(surf, rect)