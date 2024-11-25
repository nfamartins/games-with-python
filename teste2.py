import pygame
from pyamaze import maze

# Configurações
CELL_SIZE = 40
WALL_THICKNESS = 2
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Gerar o labirinto
m = maze(10, 10)
m.CreateMaze(loopPercent=20)

# Inicializar Pygame
pygame.init()
width = m.cols * CELL_SIZE
height = m.rows * CELL_SIZE
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Labirinto PyMaze no Pygame")

# Jogador
player_size = CELL_SIZE // 2
player_x = CELL_SIZE // 2
player_y = CELL_SIZE // 2
player_speed = 5

# Objetivo (saída do labirinto)
OBJECTIVE_POSITION = (8, 8)  # posição em células (coluna, linha)

def draw_maze():
    screen.fill(WHITE)
    for x in range(m.cols):
        for y in range(m.rows):
            cell = m.maze_map[(y+1, x+1)]
            px, py = x * CELL_SIZE, y * CELL_SIZE

            if not cell['N']:
                pygame.draw.line(screen, BLACK, (px, py), (px + CELL_SIZE, py), WALL_THICKNESS)
            if not cell['W']:
                pygame.draw.line(screen, BLACK, (px, py), (px, py + CELL_SIZE), WALL_THICKNESS)
            if y == m.rows - 1 and not cell['S']:
                pygame.draw.line(screen, BLACK, (px, py + CELL_SIZE), (px + CELL_SIZE, py + CELL_SIZE), WALL_THICKNESS)
            if x == m.cols - 1 and not cell['E']:
                pygame.draw.line(screen, BLACK, (px + CELL_SIZE, py), (px + CELL_SIZE, py + CELL_SIZE), WALL_THICKNESS)
    
    # Desenhar o objetivo
    obj_x, obj_y = OBJECTIVE_POSITION
    pygame.draw.rect(screen, GREEN, (obj_x * CELL_SIZE, obj_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_player():
    pygame.draw.rect(screen, RED, (player_x - player_size // 2, player_y - player_size // 2, player_size, player_size))

def can_move(x, y):
    cell_x = x // CELL_SIZE + 1
    cell_y = y // CELL_SIZE + 1
    current_cell = m.maze_map[(cell_y, cell_x)]

    if x % CELL_SIZE < player_size // 2:
        if not current_cell['W']:
            return False
    elif x % CELL_SIZE > CELL_SIZE - player_size // 2:
        if not current_cell['E']:
            return False

    if y % CELL_SIZE < player_size // 2:
        if not current_cell['N']:
            return False
    elif y % CELL_SIZE > CELL_SIZE - player_size // 2:
        if not current_cell['S']:
            return False

    return True

def check_objective_reached(player_x, player_y):
    obj_x, obj_y = OBJECTIVE_POSITION
    player_left = player_x - player_size // 2
    player_right = player_x + player_size // 2
    player_top = player_y - player_size // 2
    player_bottom = player_y + player_size // 2

    objective_left = obj_x * CELL_SIZE
    objective_right = (obj_x + 1) * CELL_SIZE
    objective_top = obj_y * CELL_SIZE
    objective_bottom = (obj_y + 1) * CELL_SIZE

    return (player_left >= objective_left and
            player_right <= objective_right and
            player_top >= objective_top and
            player_bottom <= objective_bottom)

# Loop principal
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    new_x, new_y = player_x, player_y

    if keys[pygame.K_LEFT]:
        new_x -= player_speed
    if keys[pygame.K_RIGHT]:
        new_x += player_speed
    if keys[pygame.K_UP]:
        new_y -= player_speed
    if keys[pygame.K_DOWN]:
        new_y += player_speed

    if can_move(new_x, new_y):
        player_x, player_y = new_x, new_y

    draw_maze()
    draw_player()
    pygame.display.flip()

    if check_objective_reached(player_x, player_y):
        print("Objetivo alcançado! Você venceu!")
        running = False

    clock.tick(60)

pygame.quit()