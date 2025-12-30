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
    menu_rect = menu_text.get_rect(center = (500, 450))
    if(menu_rect.collidepoint(mouse_pos)):
        menu_text = get_font(60).render("MENU", True, "#BA55D3")
    screen.blit(menu_text, menu_rect)
    #exit text
    exit_text = get_font(60).render("EXIT", True, "#5240b6")
    exit_rect = exit_text.get_rect(center = (800, 450))
    if(exit_rect.collidepoint(mouse_pos)):
        exit_text = get_font(60).render("EXIT", True, "#BA55D3")
    screen.blit(exit_text, exit_rect)
    #verify events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(menu_rect.collidepoint(mouse_pos)):  #start button pressed
                return True
            if(exit_rect.collidepoint(mouse_pos)):  #exit button pressed
                pygame.quit()
                sys.exit()
    return False