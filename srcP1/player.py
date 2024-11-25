import pygame
from srcP1.settings import *

class Player:
    def __init__(self, maze,
                 x=PLAYER_X0,y=PLAYER_Y0,
                 speed=PLAYER_SPEED,health=PLAYER_HEALTH,
                 radius=PLAYER_RADIUS):
        self.x = x  # Posição do player (x)
        self.y = y  # Posição do player (y)
        self.dx = 0 # Direção do movimento x
        self.dy = 0 # Direção do movimento y
        self.speed = speed
        self.health = health
        self.dead = False
        self.radius = radius
        self.maze = maze

    def draw(self, screen):
        # Desenhar o jogador
        pygame.draw.circle(screen, PLAYER_COLOR,(self.x,self.y),self.radius)

    def move(self):
        # Lógica de movimento
        new_x = self.x + self.dx * self.speed
        new_y = self.y + self.dy * self.speed

        # Manter o player dentro dos limites da tela
        new_x = max(MARGIN + self.radius + 2, 
                     min(new_x, SCREEN_WIDTH - MARGIN - self.radius))
        new_y = max(MARGIN_OVER + self.radius + 2, 
                               min(new_y, SCREEN_HEIGHT - MARGIN - self.radius))
        if self.can_move(new_x,new_y):
            self.x, self.y = new_x, new_y

        
    def can_move(self,x, y):
        x, y = x - MARGIN, y - MARGIN_OVER
        cell_x = x // MAZE_CELL_LEN + 1
        cell_y = y // MAZE_CELL_LEN + 1
        current_cell = self.maze.maze.maze_map[(cell_y, cell_x)]

        if x % MAZE_CELL_LEN < self.radius:
            if not current_cell['W']:
                return False
        elif x % MAZE_CELL_LEN > MAZE_CELL_LEN - self.radius:
            if not current_cell['E']:
                return False

        if y % MAZE_CELL_LEN < self.radius:
            if not current_cell['N']:
                return False
        elif y % MAZE_CELL_LEN > MAZE_CELL_LEN - self.radius:
            if not current_cell['S']:
                return False
        return True

    def update(self):
        self.move()
        self.check_died()

    def check_collision_enemy(self, enemy):
        # enemy == retângulo
        expanded_enemy = enemy.inflate(self.radius * 2, self.radius * 2)
        return expanded_enemy.collidepoint(self.x, self.y)
    
    def check_objective_reached(self):
        obj_x, obj_y = self.maze.goal
        player_left = self.x - self.radius
        player_right = self.x + self.radius
        player_top = self.y - self.radius
        player_bottom = self.y + self.radius

        objective_left = obj_x * MAZE_CELL_LEN + MARGIN
        objective_right = (obj_x + 1) * MAZE_CELL_LEN + MARGIN
        objective_top = obj_y * MAZE_CELL_LEN + MARGIN_OVER
        objective_bottom = (obj_y + 1) * MAZE_CELL_LEN + MARGIN_OVER

        return (player_left >= objective_left and
                player_right <= objective_right and
                player_top >= objective_top and
                player_bottom <= objective_bottom)
    
    def check_died(self):
        if self.health < 0:
            self.dead = True