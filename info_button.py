import pygame
from get_font import get_font  
info_anim = 0

def display_info_image(screen, mouse_pos):
    global info_anim
    img_info = pygame.image.load('assets/info.png')
    img_info = pygame.transform.scale(img_info, (img_info.get_width()*0.15, img_info.get_height()*0.15))
    info_rect = img_info.get_rect(center= (1280-img_info.get_width()/2-20, 720-img_info.get_height()/2-20))
    if(info_rect.collidepoint(mouse_pos)):
        img_info = pygame.image.load('assets/info_changed.png')
        img_info = pygame.transform.scale(img_info, (img_info.get_width()*0.15, img_info.get_height()*0.15))
        #animation
        info_anim += 0.25
        if info_anim > 1:
            info_anim = 1
    else:
        info_anim -= 0.5
        if info_anim < 0:
            info_anim = 0
    if info_anim > 0:
        base_w, base_h = 500, 250

        w = base_w * info_anim
        h = base_h * info_anim

        info_panel = pygame.Surface((base_w, base_h), pygame.SRCALPHA)
        info_panel.fill((30, 30, 30, 200))

        scaled_panel = pygame.transform.scale(info_panel, (w, h))

        # panoul iese din icon
        panel_x = info_rect.centerx - w
        panel_y = info_rect.centery - h

        screen.blit(scaled_panel, (panel_x, panel_y))

        # text doar când panoul e suficient de mare
        if info_anim > 0.8:
            font = get_font(16)
            screen.blit(font.render("Starfield Assault", True, (220,220,220)), (panel_x+125, panel_y+15))
            screen.blit(font.render("A small pygame project...", True, (220,220,220)), (panel_x+15, panel_y+50))
            screen.blit(font.render("Made by:", True, (220,220,220)), (panel_x+15, panel_y+155))
            screen.blit(font.render("Musuroi David & Tanasa Damian", True, (220,220,220)), (panel_x+15, panel_y+190))
    screen.blit(img_info, info_rect)