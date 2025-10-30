import pygame, sys
from main_menu import display_main_menu
from get_font import get_font

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Starfield Assault")

while True:
    mouse_pos = pygame.mouse.get_pos()
    display_main_menu(screen, mouse_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()