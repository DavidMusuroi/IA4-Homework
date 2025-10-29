import pygame

def main_menu():
    menu = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Starfield Assault")
    img_menu = pygame.image.load('assets/main_menu.png')
    return menu, img_menu