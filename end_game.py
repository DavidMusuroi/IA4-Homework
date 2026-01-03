import pygame, sys
from get_font import get_font

def display_end_screen(screen, mouse_pos, Game_over):
    #backround image
    img_menu = pygame.image.load('assets/main_menu.png')
    screen.blit(img_menu, (0, 0))
    #title image
    if Game_over == 1: #win
        img_title = pygame.image.load('assets/lose_or_win/Header_win.png').convert_alpha()
    else: #lose
        img_title = pygame.image.load('assets/lose_or_win/Header_lose.png').convert_alpha()
    
    w, h = img_title.get_size()
    img_title = pygame.transform.scale(img_title, (int(w * 2), int(h * 2)))
    title_rect = img_title.get_rect(center=(640, 250))
    screen.blit(img_title, title_rect)
    #menu text
    menu_text = get_font(60).render("MENU", True, "#5240b6")
    menu_rect = menu_text.get_rect(center = (640, 400))
    if(menu_rect.collidepoint(mouse_pos)):
        menu_text = get_font(60).render("MENU", True, "#BA55D3")
    screen.blit(menu_text, menu_rect)
    #stats text
    stats_text = get_font(60).render("STATS", True, "#5240b6")
    stats_rect = stats_text.get_rect(center = (640, 500))
    if(stats_rect.collidepoint(mouse_pos)):
        stats_text = get_font(60).render("STATS", True, "#BA55D3")
    screen.blit(stats_text, stats_rect)
    #exit text
    exit_text = get_font(60).render("EXIT", True, "#5240b6")
    exit_rect = exit_text.get_rect(center = (640, 600))
    if(exit_rect.collidepoint(mouse_pos)):
        exit_text = get_font(60).render("EXIT", True, "#BA55D3")
    screen.blit(exit_text, exit_rect)
    #verify events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(menu_rect.collidepoint(mouse_pos)):  #menu button pressed
                return 1
            if(stats_rect.collidepoint(mouse_pos)):  #stats button pressed
                return 2
            if(exit_rect.collidepoint(mouse_pos)):  #exit button pressed
                pygame.quit()
                sys.exit()
    return 0

def display_stats(screen, mouse_pos, Game_over, game_stats):
    #backround image
    img_menu = pygame.image.load('assets/main_menu.png')
    screen.blit(img_menu, (0, 0))
    #title text
    menu_title_text = get_font(120).render("GAME STATS", True, "#5240b6")
    menu_title_rect = menu_title_text.get_rect(center = (640, 150))
    screen.blit(menu_title_text, menu_title_rect)
    #Points
    _text = get_font(30).render("Points: ", True, "#BA55D3")
    screen.blit(_text, (300, 315))
    text = f"{game_stats.points}"
    text = get_font(30).render(text, True, "#FFFFFF")
    screen.blit(text, (890, 315))
    #play time
    play_time_text = get_font(30).render("Play time: ", True, "#BA55D3")
    screen.blit(play_time_text, (300, 360))
    
    total_seconds = game_stats.play_time // 1000
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    if hours > 0:
        text = f"{hours:02}:{minutes:02}:{seconds:02}"
    else:
        text = f"{minutes:02}:{seconds:02}"
    
    text = get_font(30).render(text, True, "#FFFFFF")
    screen.blit(text, (890, 360))
    #enemies destroyed
    _text = get_font(30).render("Enemies destroyed: ", True, "#BA55D3")
    screen.blit(_text, (300, 405))
    text = f"{game_stats.enemies_destroyed}"
    text = get_font(30).render(text, True, "#FFFFFF")
    screen.blit(text, (890, 405))
    #Boss Defeated
    _text = get_font(30).render("Boss Defeated: ", True, "#BA55D3")
    screen.blit(_text, (300, 450))
    text = f"{game_stats.boss_defeated}"
    text = get_font(30).render(text, True, "#FFFFFF")
    screen.blit(text, (890, 450))
    #Shots hit
    _text = get_font(30).render("Shots Hit: ", True, "#BA55D3")
    screen.blit(_text, (300, 495))
    text = f"{game_stats.shots_hit}"
    text = get_font(30).render(text, True, "#FFFFFF")
    screen.blit(text, (890, 495))
    #Accuracy
    _text = get_font(30).render("Accuracy: ", True, "#BA55D3")
    screen.blit(_text, (300, 540))
    if game_stats.shots != 0:
        text = f"{game_stats.shots_hit/game_stats.shots*100:.2f}"
    else:
        text = "0"
    text = get_font(30).render(text, True, "#FFFFFF")
    screen.blit(text, (890, 540))
    #back text
    back_text = get_font(60).render("BACK", True, "#5240b6")
    back_rect = back_text.get_rect(center = (1050, 630))
    if(back_rect.collidepoint(mouse_pos)):
        back_text = get_font(60).render("BACK", True, "#BA55D3")
    screen.blit(back_text, back_rect)
    #verify events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(back_rect.collidepoint(mouse_pos)):  #back button pressed
                return 1
    return 0