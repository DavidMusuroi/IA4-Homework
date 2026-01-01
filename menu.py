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
    menu_start_rect = menu_start_text.get_rect(center = (640, 400))
    if(menu_start_rect.collidepoint(mouse_pos)):
        menu_start_text = get_font(60).render("START", True, "#BA55D3")
    screen.blit(menu_start_text, menu_start_rect)
    #records text
    menu_records_text = get_font(60).render("RECORDS", True, "#5240b6")
    menu_records_rect = menu_records_text.get_rect(center = (640, 500))
    if(menu_records_rect.collidepoint(mouse_pos)):
        menu_records_text = get_font(60).render("RECORDS", True, "#BA55D3")
    screen.blit(menu_records_text, menu_records_rect)
    #exit text
    menu_exit_text = get_font(60).render("EXIT", True, "#5240b6")
    menu_exit_rect = menu_exit_text.get_rect(center = (640, 600))
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
                return 1
            if(menu_records_rect.collidepoint(mouse_pos)):  #records button pressed
                return 2
            if(menu_exit_rect.collidepoint(mouse_pos)):  #exit button pressed
                pygame.quit()
                sys.exit()
    return 0

def display_records(screen, mouse_pos):
    #backround image
    img_menu = pygame.image.load('assets/main_menu.png')
    screen.blit(img_menu, (0, 0))
    #title text
    menu_title_text = get_font(120).render("RECORDS", True, "#5240b6")
    menu_title_rect = menu_title_text.get_rect(center = (640, 150))
    screen.blit(menu_title_text, menu_title_rect)
    #back text
    back_text = get_font(60).render("BACK", True, "#5240b6")
    back_rect = back_text.get_rect(center = (1050, 630))
    if(back_rect.collidepoint(mouse_pos)):
        back_text = get_font(60).render("BACK", True, "#BA55D3")
    screen.blit(back_text, back_rect)
    #general
    _text = get_font(35).render("General ", True, "#FFFFFF")
    screen.blit(_text, (180, 270))
    #Total Points
    _text = get_font(20).render("Total Points:", True, "#BA55D3")
    screen.blit(_text, (160, 330))
    #total play time
    total_play_time_text = get_font(20).render("Total play time: ", True, "#BA55D3")
    screen.blit(total_play_time_text, (160, 360))
    #total games
    _text = get_font(20).render("Total games: ", True, "#BA55D3")
    screen.blit(_text, (160, 390))
    #win rate
    _text = get_font(20).render("Win rate: ", True, "#BA55D3")
    screen.blit(_text, (160, 420))
    #Total Enemies Destroyed
    _text = get_font(20).render("Total enemies destroyed: ", True, "#BA55D3")
    screen.blit(_text, (160, 450))
    #Bosses Defeated
    _text = get_font(20).render("Bosses Defeated: ", True, "#BA55D3")
    screen.blit(_text, (160, 480))
    #Shots Hit
    _text = get_font(20).render("Shots Hit: ", True, "#BA55D3")
    screen.blit(_text, (160, 510))
    #Average Accuracy
    _text = get_font(20).render("Average Accuracy: ", True, "#BA55D3")
    screen.blit(_text, (160, 540))

    #best
    _text = get_font(35).render("Best game ", True, "#FFFFFF")
    screen.blit(_text, (790, 270))
    #Points
    _text = get_font(20).render("Points:", True, "#BA55D3")
    screen.blit(_text, (770, 330))
    #play time
    play_time_text = get_font(20).render("Play time: ", True, "#BA55D3")
    screen.blit(play_time_text, (770, 360))
    #enemies destroyed
    _text = get_font(20).render("Enemies destroyed: ", True, "#BA55D3")
    screen.blit(_text, (770, 390))
    #Boss Defeated
    _text = get_font(20).render("Boss Defeated: ", True, "#BA55D3")
    screen.blit(_text, (770, 420))
    #Shots hit
    _text = get_font(20).render("Shots Hit: ", True, "#BA55D3")
    screen.blit(_text, (770, 450))
    #Accuracy
    _text = get_font(20).render("Accuracy: ", True, "#BA55D3")
    screen.blit(_text, (770, 480))
    #verify events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(back_rect.collidepoint(mouse_pos)):  #back button pressed
                return 1
    return 0

            