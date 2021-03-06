import pygame
from values import *
from board import Board


class Game:
    def __init__(self, screen):
        self._init()
        self.screen = screen

    def update(self):
        
        """Функция обновляет положение игры"""
        
        self.board.draw(self.screen)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        
        """Функция определяет начальные настройки"""
        
        self.selected = None
        self.board = Board()
        self.turn = BLACK
        self.valid_moves = {}

    def winner(self):
        return self.board.winner()

    def reset(self):
        
        """Функция возвращает к начальным настройкам"""
        
        self._init()

    def select(self, row, col):
        
        """Выбор шашки и ее перемещения"""
        
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        
        """Отрисовка возможных ходов"""
        
        for move in moves:
            row, col = move
            pygame.draw.circle(self.screen, BLUE,
                               (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    def change_turn(self):
        
        """Передает ход"""
        
        self.valid_moves = {}
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK

        MOVE_SOUND.play(0)
        

    def get_board(self):
        """Функция возвращает состояние доски"""
        return self.board
    
    def ai_move(self, board):
        """Функция "движения" шашки со стороны ии
            (по сути происходит не ход, а обновление доски)"""
        self.board = board
        self.change_turn()    
        
        






        

    
