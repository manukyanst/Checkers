import pygame
from values import *

" В этом модуле описывается класс Шашки и функции, связанные с шашками "

class Piece:
    BOARDER = 2
    def __init__(self,  row, col, color):
        """ Конструктор класса Piece - шашка

        Arguments:
        row - строка положения шашки
        col - столбец положения шашки
        color - цвет шашки
        king - значение говорит, является ли шашка королем или нет
        direction - значение показывает,может ли двигаться шашка вверх или вниз
        в зависимости от цвета шашки
        x, y - координаты шашки
        
        """
        self.row = row
        self.col = col
        self.color = color
        self.line_color = GREY
        self.king = False

        if self.color == BLACK:
            self.direction = -1
        else:
            self.direction = 1

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        """ Функция определяет координаты центра шашки исходя из значений строки и столбца """
        
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE//2 
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE//2

    def make_king(self):
        """ Функция делает шашку королем """
        self.king = True

    def draw(self, screen):
        """ Функция отрисовывает шашку в нужном положении """
        r = SQUARE_SIZE//2 - 5 * BOARDER
        pygame.draw.circle(screen, self.line_color, (self.x, self.y), r + LINE)
        pygame.draw.circle(screen, self.color, (self.x, self.y), r)
        
        


