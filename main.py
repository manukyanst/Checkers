import pygame
from values import *
from game import Game


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')
FPS = 60


def get_row_col_from_mouse(pos):
    """ Функция возвращает номер строки и столбца по положению мыши """

    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    finished = False
    clock = pygame.time.Clock()
    game = Game(screen)

    while not finished:
        clock.tick(FPS)

        if game.winner() is not None:
            print(game.winner())
            finished = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()


main()
