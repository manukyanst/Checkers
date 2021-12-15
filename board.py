import pygame
from values import *
from piece import *

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
        create_board - создание массива данных доски (строки и столбцы)

        """
        self.board = []
        self.selected_square = None
        self.black_pieces = 12
        self.white_pieces = 12
        self.white_kings = 0
        self.black_kings = 0
        self.create_board()

    def draw_squares(self, screen):
        
        """ Функция рисует квадраты доски """
        
        screen.fill(BROWN)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(screen, BEIGE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def move(self, piece, row, col):

        """ Функция меняет позицию шашки """
        
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        #меняем местами начальные "координаты" шашки с конечными в списке
        piece.move(row, col)

        #если шашка дошла до конца доски, она становимся королем
        if row == ROWS or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.black_kings += 1
        
    
    def get_piece(self, row, col):
        
        """ Функция возвращает объект по номеру строки и столбца """
        
        return self.board[row][col]
    
    def create_board(self):
        
        """ Функция рисует шашки на доске в начале игры """
        
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, BLACK))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
               
    def draw(self, screen):
        
        """ Функция рисует квадраты и шашки на экране """
        
        self.draw_squares(screen)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(screen)
