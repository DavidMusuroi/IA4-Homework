import pygame, sys
from menu import display_main_menu
from get_font import get_font
from force_field import force_field
from character import character

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

#Force Field and P1's ship
field = force_field(1, (178, 34, 34), (640, 0, 10, 720))
p1 = character(100, 10, 7, 400, 300, 40, 40)
p1.sprites = p1.load_spritesheet('assets/p1/Move.png', 90, (64, 64), 192, 192)

HP_Icon = pygame.image.load('assets/p1/HP_Icon.png')
HP_Icon = pygame.transform.scale(HP_Icon, (32, 32))
HP_Font = pygame.font.Font(None, 32)

#Game loop
while True:
    img_menu = pygame.image.load('assets/main_menu.png')
    screen.blit(img_menu, (0, 0))
    field.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(p1.sprites[p1.status], (p1.x, p1.y))
    keys_p1 = pygame.key.get_pressed()
    if keys_p1[pygame.K_w] and p1.y > 0:
        p1.y -= p1.velocity
        p1.status = 2
    if keys_p1[pygame.K_a] and p1.x > 0:
        p1.x -= p1.velocity
        p1.status = 3
    if keys_p1[pygame.K_s] and p1.y < 670:
        p1.y += p1.velocity
        p1.status = 4
    if keys_p1[pygame.K_d] and p1.x < 610:
        p1.x += p1.velocity
        p1.status = 5
    
    p1.rect.topleft = (p1.x, p1.y)
    if p1.rect.colliderect(field.rect):
        p1.lose_health(field.damage)
    
    HP_Text = HP_Font.render(str(p1.HP), True, (75, 0, 130))
    HP_Text_rect = HP_Text.get_rect(center = (HP_Icon.get_width() // 2, (HP_Icon.get_height() + 680)))
    screen.blit(HP_Icon, (0, 680))
    screen.blit(HP_Text, HP_Text_rect)
    clock.tick(60) #limit FPS to 60
    pygame.display.update()