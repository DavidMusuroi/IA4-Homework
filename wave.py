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

def load_enemies(wave_nr,p1,p2,screen, game_stats):
    if wave_nr == 1:
        # Enemies of player 1
        # Tier 1, Enemy 1
        t1_e1_p1 = character(10, 5, 1, 10, 0, 60, 40, game_stats)
        t1_e1_p1.sprite = pygame.image.load('assets/enemies/Ship1.png').convert_alpha()
        # Tier 2, Enemy 1
        t2_e1_p1 = character(10, 8, 2, 60, -30, 70, 40, game_stats)
        t2_e1_p1.sprite = pygame.image.load('assets/enemies/Ship2.png').convert_alpha()
        # Resize hitbox
        t2_e1_p1.rect = pygame.Rect(t2_e1_p1.x + 25, t2_e1_p1.y + 30, t2_e1_p1.width, t2_e1_p1.height)
        # Tier 3, Enemy 1
        t3_e1_p1 = character(10, 10, 3, 150, -30, 70, 40, game_stats)
        t3_e1_p1.sprite = pygame.image.load('assets/enemies/Ship3.png').convert_alpha()
        # Resize hitbox
        t3_e1_p1.rect = pygame.Rect(t3_e1_p1.x + 30, t3_e1_p1.y + 30, t3_e1_p1.width, t3_e1_p1.height)
        # Tier 2, Enemy 2
        t2_e2_p1 = character(10, 8, 2, 240, -30, 70, 40, game_stats)
        t2_e2_p1.sprite = pygame.image.load('assets/enemies/Ship2.png').convert_alpha()
        # Resize hitbox
        t2_e2_p1.rect = pygame.Rect(t2_e2_p1.x + 25, t2_e2_p1.y + 30, t2_e2_p1.width, t2_e2_p1.height)
        # Tier 1, Enemey 2
        t1_e2_p1 = character(10, 5, 1, 350, 0, 60, 40, game_stats)
        t1_e2_p1.sprite = pygame.image.load('assets/enemies/Ship1.png').convert_alpha()


        # Enemies of player 2
        t1_e1_p2 = character(10, 5, 1, 660, 0, 60, 40, game_stats)
        t1_e1_p2.sprite = pygame.image.load('assets/enemies/Ship1.png').convert_alpha()
        # Tier 2, Enemy 1
        t2_e1_p2 = character(10, 8, 2, 710, -30, 70, 40, game_stats)
        t2_e1_p2.sprite = pygame.image.load('assets/enemies/Ship2.png').convert_alpha()
        # Resize hitbox
        t2_e1_p2.rect = pygame.Rect(t2_e1_p2.x + 25, t2_e1_p2.y + 30, t2_e1_p2.width, t2_e1_p2.height)
        # Tier 3, Enemy 1
        t3_e1_p2 = character(10, 10, 3, 800, -30, 60, 40, game_stats)
        t3_e1_p2.sprite = pygame.image.load('assets/enemies/Ship3.png').convert_alpha()
        # Resize hitbox
        t3_e1_p2.rect = pygame.Rect(t3_e1_p2.x + 40, t3_e1_p2.y + 30, t3_e1_p2.width, t3_e1_p2.height)
        # Tier 2, Enemy 2
        t2_e2_p2 = character(10, 8, 2, 890, -30, 70, 40, game_stats)
        t2_e2_p2.sprite = pygame.image.load('assets/enemies/Ship2.png').convert_alpha()
        # Resize hitbox
        t2_e2_p2.rect = pygame.Rect(t2_e2_p2.x + 25, t2_e2_p2.y + 30, t2_e2_p2.width, t2_e2_p2.height)
        # Tier 1, Enemey 2
        t1_e2_p2 = character(10, 5, 1, 1000, 0, 60, 40, game_stats)
        t1_e2_p2.sprite = pygame.image.load('assets/enemies/Ship1.png').convert_alpha()


        # Add enemies to list of enemies
        p1.enemies.append(t1_e1_p1)
        p1.enemies.append(t2_e1_p1)
        p1.enemies.append(t3_e1_p1)
        p1.enemies.append(t2_e2_p1)
        p1.enemies.append(t1_e2_p1)

        p2.enemies.append(t1_e1_p2)
        p2.enemies.append(t2_e1_p2)
        p2.enemies.append(t3_e1_p2)
        p2.enemies.append(t2_e2_p2)
        p2.enemies.append(t1_e2_p2)

    elif wave_nr == 2:
        # Enemies of player 1
        # Tier 2, Enemy 1
        t2_e1_p1 = character(10, 8, 2, -10, -30, 70, 40, game_stats)
        t2_e1_p1.sprite = pygame.image.load('assets/enemies/Ship2.png').convert_alpha()
        # Resize hitbox
        t2_e1_p1.rect = pygame.Rect(t2_e1_p1.x + 25, t2_e1_p1.y + 30, t2_e1_p1.width, t2_e1_p1.height)
        # Tier 3, Enemy 1
        t3_e1_p1 = character(10, 10, 3, 80, -30, 70, 40, game_stats)
        t3_e1_p1.sprite = pygame.image.load('assets/enemies/Ship3.png').convert_alpha()
        # Resize hitbox
        t3_e1_p1.rect = pygame.Rect(t3_e1_p1.x + 30, t3_e1_p1.y + 30, t3_e1_p1.width, t3_e1_p1.height)
        # Tier 4, Enemy 1
        t4_e1_p1 = character(10, 12, 4, 185, -30, 90, 40, game_stats)
        t4_e1_p1.sprite = pygame.image.load('assets/enemies/Ship4.png').convert_alpha()
        # Resize hitbox
        t4_e1_p1.rect = pygame.Rect(t4_e1_p1.x + 20, t4_e1_p1.y + 30, t4_e1_p1.width, t4_e1_p1.height)
        # Tier 3, Enemy 2
        t3_e2_p1 = character(10, 10, 3, 290, -30, 70, 40, game_stats)
        t3_e2_p1.sprite = pygame.image.load('assets/enemies/Ship3.png').convert_alpha()
        # Resize hitbox
        t3_e2_p1.rect = pygame.Rect(t3_e2_p1.x + 30, t3_e2_p1.y + 30, t3_e2_p1.width, t3_e2_p1.height)
        # Tier 2, Enemy 2
        t2_e2_p1 = character(10, 8, 2, 390, -30, 70, 40, game_stats)
        t2_e2_p1.sprite = pygame.image.load('assets/enemies/Ship2.png').convert_alpha()
        # Resize hitbox
        t2_e2_p1.rect = pygame.Rect(t2_e2_p1.x + 25, t2_e2_p1.y + 30, t2_e2_p1.width, t2_e2_p1.height)


        # Enemies of player 2
        # Tier 2, Enemy 1
        t2_e1_p2 = character(10, 8, 2, 660, -30, 70, 40, game_stats)
        t2_e1_p2.sprite = pygame.image.load('assets/enemies/Ship2.png').convert_alpha()
        # Resize hitbox
        t2_e1_p2.rect = pygame.Rect(t2_e1_p2.x + 25, t2_e1_p2.y + 30, t2_e1_p2.width, t2_e1_p2.height)
        # Tier 3, Enemy 1
        t3_e1_p2 = character(10, 10, 3, 750, -30, 70, 40, game_stats)
        t3_e1_p2.sprite = pygame.image.load('assets/enemies/Ship3.png').convert_alpha()
        # Resize hitbox
        t3_e1_p2.rect = pygame.Rect(t3_e1_p2.x + 30, t3_e1_p2.y + 30, t3_e1_p2.width, t3_e1_p2.height)
        # Tier 4, Enemy 1
        t4_e1_p2 = character(10, 12, 4, 855, -30, 90, 40, game_stats)
        t4_e1_p2.sprite = pygame.image.load('assets/enemies/Ship4.png').convert_alpha()
        # Resize hitbox
        t4_e1_p2.rect = pygame.Rect(t4_e1_p2.x + 20, t4_e1_p2.y + 30, t4_e1_p2.width, t4_e1_p2.height)
        # Tier 3, Enemy 2
        t3_e2_p2 = character(10, 10, 3, 960, -30, 70, 40, game_stats)
        t3_e2_p2.sprite = pygame.image.load('assets/enemies/Ship3.png').convert_alpha()
        # Resize hitbox
        t3_e2_p2.rect = pygame.Rect(t3_e2_p2.x + 30, t3_e2_p2.y + 30, t3_e2_p2.width, t3_e2_p2.height)
        # Tier 2, Enemy 2
        t2_e2_p2 = character(10, 8, 2, 1060, -30, 70, 40, game_stats)
        t2_e2_p2.sprite = pygame.image.load('assets/enemies/Ship2.png').convert_alpha()
        # Resize hitbox
        t2_e2_p2.rect = pygame.Rect(t2_e2_p2.x + 25, t2_e2_p2.y + 30, t2_e2_p2.width, t2_e2_p2.height)

        # Add enemies to list of enemies
        p1.enemies.append(t2_e1_p1)
        p1.enemies.append(t3_e1_p1)
        p1.enemies.append(t4_e1_p1)
        p1.enemies.append(t3_e2_p1)
        p1.enemies.append(t2_e2_p1)

        p2.enemies.append(t2_e1_p2)
        p2.enemies.append(t3_e1_p2)
        p2.enemies.append(t4_e1_p2)
        p2.enemies.append(t3_e2_p2)
        p2.enemies.append(t2_e2_p2)
    
    elif wave_nr == 3:
        # Enemies of BOTH PLAYERS
        # Tier 1, Enemy 1
        t1_e1 = character(10, 5, 1, 10, 0, 60, 40, game_stats)
        t1_e1.sprite = pygame.image.load('assets/enemies/Ship1.png').convert_alpha()
        # Tier 2, Enemy 1
        t2_e1 = character(10, 8, 2, 60, -30, 70, 40, game_stats)
        t2_e1.sprite = pygame.image.load('assets/enemies/Ship2.png').convert_alpha()
        # Resize hitbox
        t2_e1.rect = pygame.Rect(t2_e1.x + 25, t2_e1.y + 30, t2_e1.width, t2_e1.height)
        # Tier 3, Enemy 1
        t3_e1 = character(10, 10, 3, 150, -30, 70, 40, game_stats)
        t3_e1.sprite = pygame.image.load('assets/enemies/Ship3.png').convert_alpha()
        # Resize hitbox
        t3_e1.rect = pygame.Rect(t3_e1.x + 30, t3_e1.y + 30, t3_e1.width, t3_e1.height)
        # Tier 4, Enemy 1
        t4_e1 = character(10, 12, 4, 255, -30, 90, 40, game_stats)
        t4_e1.sprite = pygame.image.load('assets/enemies/Ship4.png').convert_alpha()
        # Resize hitbox
        t4_e1.rect = pygame.Rect(t4_e1.x + 20, t4_e1.y + 30, t4_e1.width, t4_e1.height)
        # Tier 5, Enemy 1
        t5_e1 = character(100, 15, 5, 370, -30, 100, 40, game_stats)
        t5_e1.sprite = pygame.image.load('assets/enemies/Ship5.png').convert_alpha()
        # Resize hitbox
        t5_e1.rect = pygame.Rect(t5_e1.x + 10, t5_e1.y + 30, t5_e1.width, t5_e1.height)
        BOSS = character(100, 20, 1, 490, -20, 105, 40, game_stats)
        BOSS.sprite = pygame.image.load('assets/enemies/Ship6.png').convert_alpha()
        # Resize hitbox
        BOSS.rect = pygame.Rect(BOSS.x + 10, BOSS.y + 30, BOSS.width, BOSS.height)
        # Tier 5, Enemy 1
        t5_e2 = character(100, 15, 5, 620, -30, 100, 40, game_stats)
        t5_e2.sprite = pygame.image.load('assets/enemies/Ship5.png').convert_alpha()
        # Resize hitbox
        t5_e2.rect = pygame.Rect(t5_e2.x + 10, t5_e2.y + 30, t5_e2.width, t5_e2.height)
        # Tier 4, Enemy 1
        t4_e2 = character(10, 12, 4, 735, -30, 90, 40, game_stats)
        t4_e2.sprite = pygame.image.load('assets/enemies/Ship4.png').convert_alpha()
        # Resize hitbox
        t4_e2.rect = pygame.Rect(t4_e2.x + 20, t4_e2.y + 30, t4_e2.width, t4_e2.height)
        # Tier 3, Enemy 1
        t3_e2 = character(10, 10, 3, 840, -30, 70, 40, game_stats)
        t3_e2.sprite = pygame.image.load('assets/enemies/Ship3.png').convert_alpha()
        # Resize hitbox
        t3_e2.rect = pygame.Rect(t3_e2.x + 30, t3_e2.y + 30, t3_e2.width, t3_e2.height)
        # Tier 2, Enemy 1
        t2_e2 = character(10, 8, 2, 940, -30, 70, 40, game_stats)
        t2_e2.sprite = pygame.image.load('assets/enemies/Ship2.png').convert_alpha()
        # Resize hitbox
        t2_e2.rect = pygame.Rect(t2_e2.x + 25, t2_e2.y + 30, t2_e2.width, t2_e2.height)
        # Tier 1, Enemy 1
        t1_e2 = character(10, 5, 1, 1050, 0, 60, 40, game_stats)
        t1_e2.sprite = pygame.image.load('assets/enemies/Ship1.png').convert_alpha()

        # Add enemies to list of enemies
        p1.enemies.append(t1_e1)
        p1.enemies.append(t2_e1)
        p1.enemies.append(t3_e1)
        p1.enemies.append(t4_e1)
        p1.enemies.append(t5_e1)
        p1.enemies.append(BOSS)
        p1.enemies.append(t5_e2)
        p1.enemies.append(t4_e2)
        p1.enemies.append(t3_e2)
        p1.enemies.append(t2_e2)
        p1.enemies.append(t1_e2)

        p2.enemies.append(t1_e1)
        p2.enemies.append(t2_e1)
        p2.enemies.append(t3_e1)
        p2.enemies.append(t4_e1)
        p2.enemies.append(t5_e1)
        p2.enemies.append(BOSS)
        p2.enemies.append(t5_e2)
        p2.enemies.append(t4_e2)
        p2.enemies.append(t3_e2)
        p2.enemies.append(t2_e2)
        p2.enemies.append(t1_e2)

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