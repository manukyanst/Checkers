import pygame
from values import *
from board import *
from piece import *

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')
FPS = 60

def main ():
    finished = False
    clock = pygame.time.Clock()
    board = Board()
    
    while not finished:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        board.draw_squares(screen)
        pygame.display.update()

    pygame.quit()

main()
