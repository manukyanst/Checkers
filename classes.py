import pygame




class Board:
    def __init__(self):
        self.board = []


        #двумерный массив, который хранит данные о положении фигур на доске
        
        self.choosen_square = None
        self.black_left = self.white
        self.screen = screen
        
    def draw_board(self):
        self.screen.blit(BOARD_IMAGE, (0,0))

    def start_postion(self):
        self.board[
