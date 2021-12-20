import pygame
pygame.init()
" В этом файле хранятся все константы - значения размеров поля, картинки и т.д."

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8 #количество строк и столбцов
SQUARE_SIZE = WIDTH // COLS #размер квадрата доски
LINE = 1 #ширина границы шашки
BOARDER = 2 #отступ 

# цвета rgb
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (100, 67, 33)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
BEIGE = (255, 230, 180)
GREEN = (0, 255, 0)

CROWN = pygame.transform.scale(pygame.image.load('graphics/crown.png'), (44, 25))
MENU_BACKGROUND = pygame.image.load('graphics/background.WebP')

MOVE_SOUND = pygame.mixer.Sound('sounds/move_sound.mp3')
