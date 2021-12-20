import pygame

pygame.init()
f1 = pygame.font.Font(None, 36)

def draw_menu(screen):
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 0, 255), (100, 100, 600, 100))
    text01 = f1.render('SINGLE MODE', True, (0, 0, 0))
    screen.blit(text01, (300, 140))
    pygame.draw.rect(screen, (0, 255, 0), (100, 400, 600, 100))
    text02 = f1.render('PVP MODE', True, (0, 0, 0))
    screen.blit(text02, (330, 440))
    pygame.display.update()


def start_game(x, y, game_mode, screen):

    if game_mode == 0:
        
        if (x > 100 and x < 700 and y > 100 and y < 200):
            game_mode = 1

        if (x > 100 and x < 700 and y > 400 and y < 500):
            game_mode = 2

    return game_mode

        


    
    

