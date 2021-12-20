import pygame
from values import *
from game import Game
from algorithm import minimax
from menu import *


pygame.init()
f1 = pygame.font.Font(None, 36)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')
FPS = 60
game_mode = 0



def get_row_col_from_mouse(pos):
    """ Функция возвращает номер строки и столбца по положению мыши """

    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main(game_mode):
    finished = False
    clock = pygame.time.Clock()
    game = Game(screen)

    while not finished:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                game_mode = start_game(event.pos[0], event.pos[1], game_mode, screen)

        if game_mode == 0:
            draw_menu(screen)
            
        if game_mode == 1:

            if game.turn == WHITE:
                value, new_board = minimax(game.get_board(), 4, WHITE, game)
                game.ai_move(new_board)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
            game.update()

        if game_mode == 2:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
            game.update()

        if game.winner() is not None:
            print(game.winner())
            finished = True
     
    pygame.quit()

main(game_mode)
