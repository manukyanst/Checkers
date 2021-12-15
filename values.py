import pygame

" В этом файле хранятся все константы - значения размеров поля, картинки и т.д."

WIDTH = 800 #ширина доски
HEIGHT = 800 #высота доски

ROWS = 8 #число строк
COLS = 8 #число столбцов

SQUARE_SIZE = WIDTH//ROWS #размер квадрата
BOARDER = 2  #отступ шашки от квадрата
LINE = 1     #толщиа контура

#цвета rgb
BROWN = (100, 67, 33)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BEIGE = (255, 230, 180)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREY = (146, 150, 177)

CROWN = pygame.transform.scale(pygame.image.load('graphics/crown.png'), (45, 25))
