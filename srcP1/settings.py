# nomes
GAME_NAME = 'JOGO DO LABIRINTO'

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# screen
SCREEN_WIDTH = 780
SCREEN_HEIGHT = 620
MARGIN = 10
MARGIN_OVER = 50
MARGIN_SIZE = 2
FPS = 60

# player
PLAYER_COLOR = BLUE
PLAYER_RADIUS = 10
PLAYER_SPEED = 4
PLAYER_HEALTH = 100
PLAYER_X0 = MARGIN + PLAYER_RADIUS
PLAYER_Y0 = MARGIN_OVER + PLAYER_RADIUS

# maze
MAZE_CELL_LEN = 4*PLAYER_RADIUS
MAZE_COMPLEXITY = 10
MAZE_THICKNESS = 2
MAZE_WIDTH = (SCREEN_WIDTH - 2 * MARGIN) // MAZE_CELL_LEN
MAZE_HEIGTH = (SCREEN_HEIGHT - MARGIN - MARGIN_OVER) // MAZE_CELL_LEN

# design
GAME_NAME_POSITION = (10,15)
HEALTH_POSITION = (SCREEN_WIDTH-150,15)

# enemies
ENEMY_HEIGHT = 20
ENEMY_COLOR = RED
ENEMY_N = 10
