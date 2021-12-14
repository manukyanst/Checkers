import pygame
from values import *

" в этом модуле описывается класс Доска и функции, связанные с ней"

class Board:
    def __init__(self):
        """ Конструктор класса Board

        Arguments:
        board - двумерный массив, в котором хранится информация
        о положении шашек на доске
        selected_square - значение, показывающее, выбран ли квадрат на доске для хода
        black/white pieces - количество белых или черных шашек
        black/white kings - количество белых или черных королей
        

        """
        self.board = []
        self.selected_square = None
        self.black_pieces = 12
        self.white_pieces = 12
        self.white_kings = 0
        self.black_kings = 0

    def draw_squares(self, screen):
        
        """ Функция рисует квадраты доски """
        
        screen.fill(BROWN)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(screen, BEIGE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                
    def new_board(self):
        
        """ Функция рисует шашки на доске в начале игры """

        
