import pygame, sys
from get_font import get_font  
from info_button import display_info_image

def display_main_menu(screen, mouse_pos):
    global info_anim
    #backround image
    img_menu = pygame.image.load('assets/main_menu.png')
    screen.blit(img_menu, (0, 0))
    #title text
    menu_title_text = get_font(120).render("MAIN MENU", True, "#5240b6")
    menu_title_rect = menu_title_text.get_rect(center = (640, 150))
    screen.blit(menu_title_text, menu_title_rect)
    #start text
    menu_start_text = get_font(60).render("START", True, "#5240b6")
    menu_start_rect = menu_start_text.get_rect(center = (640, 450))
    if(menu_start_rect.collidepoint(mouse_pos)):
        menu_start_text = get_font(60).render("START", True, "#BA55D3")
    screen.blit(menu_start_text, menu_start_rect)
    #exit text
    menu_exit_text = get_font(60).render("EXIT", True, "#5240b6")
    menu_exit_rect = menu_exit_text.get_rect(center = (640, 550))
    if(menu_exit_rect.collidepoint(mouse_pos)):
        menu_exit_text = get_font(60).render("EXIT", True, "#BA55D3")
    screen.blit(menu_exit_text, menu_exit_rect)
    #info image
    display_info_image(screen, mouse_pos)
    #verify events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(menu_start_rect.collidepoint(mouse_pos)):  #start button pressed
                return True
            if(menu_exit_rect.collidepoint(mouse_pos)):  #exit button pressed
                pygame.quit()
                sys.exit()
    return False
            