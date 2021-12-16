import pygame
from values import *

" В этом модуле описывается класс Шашки и функции, связанные с шашками "


class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        """ Конструктор класса Piece - шашка
        Arguments:
        row - строка положения шашки
        col - столбец положения шашки
        color - цвет шашки
        king - значение говорит, является ли шашка королем или нет
        x, y - координаты шашки

        """
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        """ Функция определяет координаты центра шашки исходя из значений строки и столбца """

        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        """ Функция делает шашку королем """

        self.king = True

    def move(self, row, col):
        """ Фунцкия двигает шашку и пересчитывает координаты её левого перхнего угла """

        self.row = row
        self.col = col
        self.calc_pos()

    def draw(self, screen):
        """ Функция отрисовывает шашку в нужном положении """

        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(screen, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(screen, self.color, (self.x, self.y), radius)
        if self.king:
            screen.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))
        


