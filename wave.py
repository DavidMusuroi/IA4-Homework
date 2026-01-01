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
        # Enemies 1 and 2 of player 1
        e1_p1 = character(30, 5, 1, 400, 400, 60, 40, game_stats)
        e1_p1.sprite = pygame.image.load('assets/enemies/Ship1.png').convert_alpha()
        e1_p1.sprite = pygame.transform.rotate(e1_p1.sprite, -90)
        e2_p1 = character(55, 8, 2, 500, 500, 70, 55, game_stats)
        e2_p1.sprite = pygame.image.load('assets/enemies/Ship2.png').convert_alpha()
        e2_p1.sprite = pygame.transform.rotate(e2_p1.sprite, -90)
        # Resize hitbox
        e2_p1.rect = pygame.Rect(e2_p1.x + 25, e2_p1.y, e2_p1.width, e2_p1.height)
        # Enemies 1 and 2 of player 2
        e1_p2 = character(30, 2, 1, 1000, 500, 60, 45, game_stats)
        e1_p2.sprite = pygame.image.load('assets/enemies/Ship1.png').convert_alpha()
        e2_p2 = character(55, 8, 2, 1000, 400, 70, 55, game_stats)
        e2_p2.sprite = pygame.image.load('assets/enemies/Ship2.png').convert_alpha()
        # Resize hitbox
        e2_p2.rect = pygame.Rect(e2_p2.x + 25, e2_p2.y, e2_p2.width, e2_p2.height)
        p1.enemies.append(e1_p1)
        p1.enemies.append(e2_p1)
        p2.enemies.append(e1_p2)
        p2.enemies.append(e2_p2)
    
    elif wave_nr == 2:
        e1_p1 = character(30, 5, 1, 400, 400, 60, 40, game_stats)
        e1_p1.sprite = pygame.image.load('assets/enemies/Ship1.png').convert_alpha()
        p1.enemies.append(e1_p1)
        # TODO ...
    
    elif wave_nr == 3:
        e2_p2 = character(55, 8, 2, 1000, 600, 70, 55, game_stats)
        e2_p2.sprite = pygame.image.load('assets/enemies/Ship2.png').convert_alpha()
        p2.enemies.append(e2_p2)
        # TODO ...

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