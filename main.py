import pygame, sys
from menu import display_main_menu
from get_font import get_font
from force_field import force_field
from character import character
from bullet import Bullet

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Starfield Assault")
clock = pygame.time.Clock()
menu_is_over = False
#Menu loop
while menu_is_over == False:
    mouse_pos = pygame.mouse.get_pos()
    menu_is_over = display_main_menu(screen, mouse_pos)
    clock.tick(60) #limit FPS to 60
    pygame.display.update()

#Force Field
field = force_field(4, (178, 34, 34), (640, 0, 10, 720))

# P1's ship
p1 = character(100, 10, 7, 280, 665, 40, 40)
p1.sprites = p1.load_spritesheet('assets/p1/Move.png', 90, (64, 64), 192, 192)

# P2's ship
p2 = character(100, 10, 7, 950, 665, 40, 40)
p2.sprites = p2.load_spritesheet('assets/p2/Move.png', 90, (64, 64), 192, 192)

# Current wave
wave_nr = 1

# Enemies 1 and 2 of player 1
e1_p1 = character(30, 5, 1, 400, 400, 60, 40)
e1_p1.sprite = pygame.image.load('assets/enemies/Ship1.png').convert_alpha()
e2_p1 = character(55, 8, 2, 500, 500, 70, 55)
e2_p1.sprite = pygame.image.load('assets/enemies/Ship2.png').convert_alpha()
# Resize hitbox
e2_p1.rect = pygame.Rect(e2_p1.x + 25, e2_p1.y, e2_p1.width, e2_p1.height)
# Enemies 1 and 2 of player 2
e1_p2 = character(30, 2, 1, 1000, 500, 60, 45)
e1_p2.sprite = pygame.image.load('assets/enemies/Ship1.png').convert_alpha()
e2_p2 = character(55, 8, 2, 1000, 600, 70, 55)
e2_p2.sprite = pygame.image.load('assets/enemies/Ship2.png').convert_alpha()
# Resize hitbox
e2_p2.rect = pygame.Rect(e2_p2.x + 25, e2_p2.y, e2_p2.width, e2_p2.height)

# HP1 Icon
HP1_Icon = pygame.image.load('assets/p1/HP_Icon.png')
HP1_Icon = pygame.transform.scale(HP1_Icon, (32, 32))
HP1_Font = pygame.font.Font(None, 32)

# HP2 Icon
HP2_Icon = pygame.image.load('assets/p2/HP_Icon.png')
HP2_Icon = pygame.transform.scale(HP2_Icon, (32, 32))
HP2_Font = pygame.font.Font(None, 32)

#Game loop
while True:
    img_menu = pygame.image.load('assets/main_menu.png')
    screen.blit(img_menu, (0, 0))
    field.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(p1.sprites[p1.status], (p1.x, p1.y))
    screen.blit(p2.sprites[p2.status], (p2.x, p2.y))
    # Start Wave 1
    if wave_nr == 1 and not p1.enemies and not p2.enemies:
        p1.enemies.append(e1_p1)
        p2.enemies.append(e1_p2)
        p1.enemies.append(e2_p1)
        p2.enemies.append(e2_p2)
        screen.blit(e1_p1.sprite, (e1_p1.x, e1_p1.y))
        screen.blit(e1_p2.sprite, (e1_p2.x, e1_p2.y))
        screen.blit(e2_p1.sprite, (e2_p1.x, e2_p1.y))
        screen.blit(e2_p2.sprite, (e2_p2.x, e2_p2.y))
    # Check if we have enemies remaining
    elif len(p1.enemies) != 0 or len(p2.enemies) != 0:
        okay = False
        for enemy in p1.enemies[:]:
            if enemy.HP > 0:
                okay = True
                screen.blit(enemy.sprite, (enemy.x, enemy.y))
            else:
                p1.enemies.remove(enemy)
        for enemy in p2.enemies[:]:
            if enemy.HP > 0:
                okay = True
                screen.blit(enemy.sprite, (enemy.x, enemy.y))
            else:
                p2.enemies.remove(enemy)
        if okay == False:
            wave_nr += 1
    # Advance to wave 2 if no enemies remain
    elif wave_nr == 2 and not p1.enemies and not p2.enemies:
        wave_nr += 1
        # TODO : insert enemies
    # Advance to wave 3 if no enemies remain
    elif wave_nr == 3 and not p1.enemies and not p2.enemies:
        wave_nr += 1
        # TODO : insert enemies
    # You win!
    elif wave_nr == 4 and not p1.enemies and not p2.enemies:
        k = "GG"
        # TODO : Win Screen
    

    keys_p1 = pygame.key.get_pressed()
    keys_p2 = pygame.key.get_pressed()
    # KEYS P1
    if keys_p1[pygame.K_w] and p1.y > 0:
        p1.y -= p1.velocity
        p1.status = 2
    if keys_p1[pygame.K_a] and p1.x > 0:
        p1.x -= p1.velocity
        p1.status = 3
    if keys_p1[pygame.K_s] and p1.y < 700 - p1.height:
        p1.y += p1.velocity
        p1.status = 4
    if keys_p1[pygame.K_d] and p1.x < 605:
        p1.x += p1.velocity
        p1.status = 5
    
    # KEYS P2
    if keys_p2[pygame.K_UP] and p2.y > 0:
        p2.y -= p2.velocity
        p2.status = 2
    if keys_p2[pygame.K_LEFT] and p2.x > 615:
        p2.x -= p1.velocity
        p2.status = 3
    if keys_p2[pygame.K_DOWN] and p2.y < 700 - p2.height:
        p2.y += p1.velocity
        p2.status = 4
    if keys_p2[pygame.K_RIGHT] and p2.x < 1270 - p2.width:
        p2.x += p2.velocity
        p2.status = 5

    #check for shoot
    if keys_p1[pygame.K_f]:
        p1.shoot((47,249,36))

    if keys_p2[pygame.K_SPACE]:
        p2.shoot((0,255,255))

    #update rect for p1 & p2
    p1.rect.topleft = (p1.x, p1.y)
    p2.rect.topleft = (p2.x, p2.y)

    #TODO -> ADD ENEMIES IN p1.enemies and p2.enemies if the list is empty
    #if(not p1.enemies):
        #...
        #create enemy as a new instance of character (maybe at random coords)
        #add it to the list
        
    #if(not p2.enemies):
        #...

    #display bullets and check for hits
    p1.check_hits()
    p2.check_hits()
    p1.update_bullets(screen)
    p2.update_bullets(screen)

    #colision with the field
    if p1.rect.colliderect(field.rect):
        p1.lose_health_by_field(field.damage)
    if p2.rect.colliderect(field.rect):
        p2.lose_health_by_field(field.damage)
    
    #display hp for p1
    HP1_Text = HP1_Font.render(str(p1.HP), True, (75, 0, 130))
    HP1_Text_rect = HP1_Text.get_rect(center = (16, 680))
    screen.blit(HP1_Icon, (0, 690))
    screen.blit(HP1_Text, HP1_Text_rect)
    
    #display hp for p2
    HP2_Text = HP2_Font.render(str(p2.HP), True, (75, 0, 130))
    HP2_Text_rect = HP2_Text.get_rect(center = (1262, 680))
    screen.blit(HP2_Icon, (1280 - 32, 690))
    screen.blit(HP2_Text, HP2_Text_rect)

    # TODO : Game Over Screen
    if p1.HP <= 0 or p2.HP <= 0:
        pygame.quit()
        sys.exit()
        print("GAME OVER")

    clock.tick(60) #limit FPS to 60
    pygame.display.update()