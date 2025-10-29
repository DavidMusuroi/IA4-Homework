import pygame, sys
from main_menu import main_menu
from get_font import get_font

pygame.init()

menu, img_menu = main_menu()

while True:
    menu.blit(img_menu, (0, 0))
    menu_text = get_font(120).render("MAIN MENU", True, "#5240b6")
    menu_rect = menu_text.get_rect(center = (640, 100))

    menu.blit(menu_text, menu_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()