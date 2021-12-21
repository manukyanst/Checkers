import pygame
from values import *

pygame.init()
f1 = pygame.font.Font(None, 36)
f2 = pygame.font.Font(None, 100)

def draw_menu(screen):
    ''' Функция рисует меню на экране '''
    screen.blit(MENU_BACKGROUND, (0, 0))
    pygame.draw.rect(screen, (BEIGE), (WIDTH // 8, HEIGHT // 3, WIDTH * 2 // 3 + 50, HEIGHT // 8))
    text01 = f1.render('SINGLE MODE', True, BLACK)
    screen.blit(text01, (WIDTH // 8 + 200, HEIGHT // 3 + 40))
    pygame.draw.rect(screen, (GREY), (WIDTH // 8, HEIGHT // 2, WIDTH * 2 // 3 + 50, HEIGHT // 8))
    text02 = f1.render('PVP MODE', True, BLACK)
    screen.blit(text02, (WIDTH // 8 + 230, HEIGHT // 2 + 40))
    pygame.display.update()


def start_game(x, y, game_mode, screen):
    ''' Функция воспринимает нажатия на конкретный пункт меню '''
    if game_mode == 0:
        if (x > WIDTH // 8 and x < WIDTH // 8 + WIDTH * 2 // 3 + 50 and y > HEIGHT // 3 and y < HEIGHT // 3 + HEIGHT // 8):
            game_mode = 1
        if (x > WIDTH // 8 and x <  WIDTH // 8 + WIDTH * 2 // 3 + 50 and y > HEIGHT // 2 and y < HEIGHT // 2 + HEIGHT // 3 + HEIGHT // 8 + HEIGHT // 8):
            game_mode = 2
    return game_mode

def end_game(winner, screen):
    """Функция показывает на экране, кто победитель"""
    text_black = f2.render('BLACK WINS', True, WHITE)
    text_white = f2.render('WHITE WINS', True, BLACK)
    if winner == BLACK:
        screen.fill(BLACK)
        screen.blit(text_black, (200, 350))
    else:
        screen.fill(WHITE)
        screen.blit(text_white, (200, 350))
    pygame.display.update()
        
