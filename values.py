import pygame

" В этом файле хранятся все константы - значения размеров поля, картинки и т.д."

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
LINE = 1
BOARDER = 2
# rgb
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (100, 67, 33)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
BEIGE = (255, 230, 180)

CROWN = pygame.transform.scale(pygame.image.load('graphics/crown.png'), (44, 25))

