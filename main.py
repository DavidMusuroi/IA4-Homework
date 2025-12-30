import pygame, sys
from menu import display_main_menu
from end_game import display_end_screen
from get_font import get_font
from force_field import force_field
from character import character
from bullet import Bullet
from wave import check_for_enemies, load_enemies

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Starfield Assault")
clock = pygame.time.Clock()

#App loop
while True:
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
    p2.HP = 12
    # Current wave
    wave_nr = 1

    # HP1 Icon
    HP1_Icon = pygame.image.load('assets/p1/HP_Icon.png')
    HP1_Icon = pygame.transform.scale(HP1_Icon, (32, 32))
    HP1_Font = pygame.font.Font(None, 32)

    # HP2 Icon
    HP2_Icon = pygame.image.load('assets/p2/HP_Icon.png')
    HP2_Icon = pygame.transform.scale(HP2_Icon, (32, 32))
    HP2_Font = pygame.font.Font(None, 32)

    # 0 -> game is not over
    # 1 -> win
    # 2 -> lose
    Game_over = 0

    #Game loop
    while not Game_over:
        img_menu = pygame.image.load('assets/main_menu.png')
        screen.blit(img_menu, (0, 0))
        field.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(p1.sprites[p1.status], (p1.x, p1.y))
        screen.blit(p2.sprites[p2.status], (p2.x, p2.y))

        #Load enemies for wave 1, 2, 3
        if not p1.enemies and not p2.enemies:
            load_enemies(wave_nr,p1,p2,screen)
        #Verify if any wave finished to move to the next one
        if wave_nr < 4:
            enemies_alive = check_for_enemies(p1, p2, screen)
            if not enemies_alive:
                wave_nr += 1
        #WIN TODO : Game WIN Screen
        elif wave_nr == 4 and not p1.enemies and not p2.enemies:
            print("GG")
            Game_over = 1

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
            print("GAME OVER - You lost")
            Game_over = 2

        clock.tick(60) #limit FPS to 60
        pygame.display.update()

    end_screen_is_over = False
    #End screen loop
    while end_screen_is_over == False:
        mouse_pos = pygame.mouse.get_pos()
        end_screen_is_over = display_end_screen(screen, mouse_pos, Game_over)
        clock.tick(60) #limit FPS to 60
        pygame.display.update()