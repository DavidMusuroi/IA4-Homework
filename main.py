import pygame, sys
from menu import display_main_menu, display_records
from end_game import display_end_screen, display_stats
from timer import display_timer
from get_font import get_font
from force_field import force_field
from character import character
from bullet import Bullet
from stats import stats
from wave import check_for_enemies, load_enemies, draw_wave_text

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Starfield Assault")
clock = pygame.time.Clock()

#App loop
while True:
    #load best stats
    best_stats = stats()
    best_stats.load_best_stats()
    
    menu_is_over = 0
    #Menu loop
    while menu_is_over != 1:
        mouse_pos = pygame.mouse.get_pos()
        if menu_is_over == 0:
            menu_is_over = display_main_menu(screen, mouse_pos)
        else:
            records_is_over = False
            #Records loop
            while records_is_over == False:
                mouse_pos = pygame.mouse.get_pos()
                records_is_over = display_records(screen, mouse_pos, best_stats)
                clock.tick(60) #limit FPS to 60
                pygame.display.update()
            menu_is_over = 0
        clock.tick(60) #limit FPS to 60
        pygame.display.update()

    #game_stats
    game_stats = stats()

    #Force Field
    field = force_field(4, (178, 34, 34), (640, 0, 10, 670))

    # P1's ship
    p1 = character(100, 10, 7, 280, 610, 40, 40, game_stats)
    p1.sprites = p1.load_spritesheet('assets/p1/Move.png', 90, (64, 64), 192, 192)

    # P2's ship
    p2 = character(100, 10, 7, 950, 610, 40, 40, game_stats)
    p2.sprites = p2.load_spritesheet('assets/p2/Move.png', 90, (64, 64), 192, 192)

    # Current wave
    wave_nr = 2

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
    start_time = pygame.time.get_ticks()
    wave_text_start = pygame.time.get_ticks()
    show_wave_text = True
    #Game loop
    while not Game_over:
        img_menu = pygame.image.load('assets/main_menu.png')
        screen.blit(img_menu, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(p1.sprites[p1.status], (p1.x, p1.y))
        screen.blit(p2.sprites[p2.status], (p2.x, p2.y))

        if show_wave_text:
            wave_text_time = pygame.time.get_ticks() - wave_text_start
            draw_wave_text(screen, wave_nr, wave_text_time)
            if wave_text_time >= 2400:
                show_wave_text = False
        else:
            #Load enemies for wave 1, 2, 3
            if not p1.enemies and not p2.enemies:
                load_enemies(wave_nr,p1,p2,screen, game_stats)
            #Verify if any wave finished to move to the next one
            if wave_nr < 4:
                enemies_alive = check_for_enemies(p1, p2, screen, game_stats)
                if not enemies_alive:
                    wave_nr += 1
                    if wave_nr != 4:
                        show_wave_text = True
                        wave_text_start = pygame.time.get_ticks()
                    #points for clear wave
                    if wave_nr < 4:
                        game_stats.points += 200
                    else:
                        game_stats.points += 500 #for final boss 
            #WIN
            elif wave_nr == 4 and not p1.enemies and not p2.enemies:
                game_stats.boss_defeated = 1
                game_stats.play_time = pygame.time.get_ticks() - start_time
                Game_over = 1
        
        #LOSE
        if ((p1.HP <= 0 or p2.HP <= 0) and wave_nr < 3) or (p1.HP <= 0 and p2.HP <= 0 and wave_nr == 3):
            Game_over = 2
            game_stats = start_time - pygame.time.get_ticks()

        keys_p1 = pygame.key.get_pressed()
        keys_p2 = pygame.key.get_pressed()
        # KEYS P1
        if keys_p1[pygame.K_w] and p1.y > 0:
            p1.y -= p1.velocity
            p1.status = 2
        if keys_p1[pygame.K_a] and p1.x > 0:
            p1.x -= p1.velocity
            p1.status = 3
        if keys_p1[pygame.K_s] and p1.y < 650 - p1.height:
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
        if keys_p2[pygame.K_DOWN] and p2.y < 650 - p2.height:
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

        if wave_nr < 3:
            field.draw(screen)
            #colision with the field
            if p1.rect.colliderect(field.rect):
                p1.lose_health_by_field(field.damage)
            if p2.rect.colliderect(field.rect):
                p2.lose_health_by_field(field.damage)
        
        #display info bar  
        HUD_HEIGHT = 50
        hud_surface = pygame.Surface((1280, HUD_HEIGHT), pygame.SRCALPHA)
        hud_surface.fill((82, 64, 182, 200))   # mov cu alpha (0–255)
        screen.blit(hud_surface, (0, 720 - HUD_HEIGHT))
        HUD_HEIGHT2 = 10
        hud_surface2 = pygame.Surface((1280, HUD_HEIGHT2), pygame.SRCALPHA)
        hud_surface2.fill((255, 255, 255, 200))   # mov cu alpha (0–255)
        screen.blit(hud_surface2, (0, 720 - 40 - HUD_HEIGHT2))

        #display hp for p1
        HP1_Text = get_font(16).render(str(p1.HP), True, (0, 180, 0))
        HP1_Text_rect = HP1_Text.get_rect(center = (55, 700))
        screen.blit(HP1_Icon, (3, 685))
        screen.blit(HP1_Text, HP1_Text_rect)
        
        #display hp for p2
        HP2_Text = get_font(16).render(str(p2.HP), True, (0, 180, 0))
        HP2_Text_rect = HP2_Text.get_rect(center = (1220, 700))
        screen.blit(HP2_Icon, (1280 - 35, 685))
        screen.blit(HP2_Text, HP2_Text_rect)

        #display game time
        display_timer(screen, start_time)
        
        clock.tick(60) #limit FPS to 60
        pygame.display.update()

    #compare to best game
    if game_stats.points > best_stats.points:
        best_stats.copy_from(game_stats)
    else:
        if game_stats.points == best_stats.points:
            if game_stats.play_time < best_stats.play_time:
                best_stats.copy_from(game_stats)
            else:
                if game_stats.play_time == best_stats.play_time:
                    if best_stats.shots == 0:
                        best_stats.copy_from(game_stats)
                    elif game_stats.shots_hit/game_stats.shots*100 > best_stats.shots_hit/best_stats.shot*100:
                        best_stats.copy_from(game_stats)
    best_stats.save_best()

    end_screen_is_over = 0
    #End screen loop
    while end_screen_is_over != 1:
        mouse_pos = pygame.mouse.get_pos()
        if end_screen_is_over == 0:
            end_screen_is_over = display_end_screen(screen, mouse_pos, Game_over)
        else:
            stats_is_over = 0
            #Stats loop
            while stats_is_over != 1:
                mouse_pos = pygame.mouse.get_pos()
                stats_is_over = display_stats(screen, mouse_pos, Game_over, game_stats)
                clock.tick(60) #limit FPS to 60
                pygame.display.update()
            end_screen_is_over = 0
        clock.tick(60) #limit FPS to 60
        pygame.display.update()