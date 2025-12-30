import pygame
from get_font import get_font

def display_timer(screen, start_time):
    #display box for time
    timer_height = 50
    timer_weight = 100
    timer_surface = pygame.Surface((timer_weight, timer_height), pygame.SRCALPHA)
    timer_surface.fill((200, 200, 200, 170))
    screen.blit(timer_surface, (1280-timer_weight-20, 20))
    #display time
    elapsed_seconds = (pygame.time.get_ticks() - start_time)//1000
    minutes = elapsed_seconds // 60
    seconds = elapsed_seconds % 60
    time_text = f"{minutes:02}:{seconds:02}"
    time_render = get_font(16).render(time_text, True, "#5240b6")
    text_rect = time_render.get_rect(center=(1280 - timer_weight + 32, timer_height-2))
    screen.blit(time_render, text_rect)
