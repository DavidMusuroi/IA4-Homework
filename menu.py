import pygame
from get_font import get_font  

def display_main_menu(screen, mouse_pos):
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
    img_info = pygame.image.load('assets/info.png')
    img_info = pygame.transform.scale(img_info, (img_info.get_width()*0.15, img_info.get_height()*0.15))
    info_rect = img_info.get_rect(center= (1280-img_info.get_width()/2-20, 720-img_info.get_height()/2-20))
    if(info_rect.collidepoint(mouse_pos)):
        img_info = pygame.image.load('assets/info_changed.png')
        img_info = pygame.transform.scale(img_info, (img_info.get_width()*0.15, img_info.get_height()*0.15))
    screen.blit(img_info, info_rect)