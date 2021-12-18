from copy import deepcopy
import pygame
from values import *


def minimax(board, depth, max_player):
    """Функция осуществляет выбор наилучшего хода для ии
        board - позиция (вариант доски)
        depth - глубина (на сколько ходов вперед просчитывается)
        max_player - логическая переменная, которая показывает
        надо ли максимизировать (T) или минимизировать (F) чсило очков - evalaute
    """
    if depth == 0 or board.winner() != None:
        return board.evaluate(), board
    
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(board, WHITE):
            evaluation = minimax(move, depth - 1, False)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        
        return maxEval, best_move
    else:
        minEval = float('+inf')
        best_move = None
        for move in get_all_moves(board, BLACK):
            evaluation = minimax(move, depth - 1, True)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        
        return minEval, best_move


def simulate_move(piece, move, board, skip):
    """Функция создает и возвращает версию доски с предполагаемым ходом"""
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def get_all_moves(board, color):
    """Функция возвращает все возможные варианты ходов(доски) с данной позиции"""
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, skip)
            moves.append(new_board)
    
    return moves


