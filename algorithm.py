from copy import deepcopy
import pygame
from values import *


def minimax(board, depth, max_player, game):
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
        for move in get_all_moves(board, WHITE, game):
            evaluation = minimax(move, depth - 1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        
        return maxEval, best_move
    else:
        minEval = float('+inf')
        best_move = None
        for move in get_all_moves(board, BLACK, game):
            evaluation = minimax(move, depth - 1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        
        return minEval, best_move


def simulate_move(piece, move, board, game, skip):
    """Функция создает и возвращает версию доски с предполагаемым ходом"""
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def get_all_moves(board, color, game):
    """Функция возвращает все возможные варианты ходов(доски) с данной позиции"""
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    
    return moves

def draw_moves(game, board, piece):
    """Функция отрисовывает выбранный ход и доску"""
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.screen)
    pygame.draw.circle(game.screen, GREEN, (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
