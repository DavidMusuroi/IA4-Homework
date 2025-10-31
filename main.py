import pygame, sys
from main_menu import display_main_menu
from get_font import get_font

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Starfield Assault")
clock = pygame.time.Clock()
menu_is_over = False

#Menu loop
while menu_is_over == False:
    mouse_pos = pygame.mouse.get_pos()
    display_main_menu(screen, mouse_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            menu_is_over = True
            
    clock.tick(60) #limit FPS to 60
    pygame.display.update()

#Game loop
while True:
    img_menu = pygame.image.load('assets/main_menu.png')
    screen.blit(img_menu, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    clock.tick(60) #limit FPS to 60
    pygame.display.update()