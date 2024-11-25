import pygame
import random
from pyamaze import maze
from srcP1.settings import *

class Maze:
    def __init__(self, complexity=MAZE_COMPLEXITY):
        self.cell_len = MAZE_CELL_LEN
        self.width = MAZE_WIDTH
        self.height = MAZE_HEIGTH
        self.complexity = complexity
        self.goal = (random.randint(1,MAZE_WIDTH-1), 
                     random.randint(1,MAZE_HEIGTH-1))
        self.make()
    
    def make(self):
        self.maze = maze(self.height, self.width) 
        self.maze.CreateMaze(loopPercent=self.complexity)
    
    def draw(self,screen):
        for x in range(self.maze.cols):
            for y in range(self.maze.rows):
                cell = self.maze.maze_map[(y+1, x+1)]
                px, py = MARGIN + x * self.cell_len, MARGIN_OVER + y * self.cell_len

                if not cell['N']:
                    pygame.draw.line(screen, WHITE, (px, py), (px + self.cell_len, py), MAZE_THICKNESS)
                if not cell['W']:
                    pygame.draw.line(screen, WHITE, (px, py), (px, py + self.cell_len), MAZE_THICKNESS)
                if y == self.maze.rows - 1 and not cell['S']:
                    pygame.draw.line(screen, WHITE, (px, py + self.cell_len), 
                                     (px + self.cell_len, py + self.cell_len), MAZE_THICKNESS)
                if x == self.maze.cols - 1 and not cell['E']:
                    pygame.draw.line(screen, WHITE, (px + self.cell_len, py), 
                                     (px + self.cell_len, py + self.cell_len), MAZE_THICKNESS)
    
        # objetivo
        obj_x, obj_y = self.goal
        pygame.draw.rect(screen, WHITE, (obj_x * self.cell_len + MARGIN, 
                                         obj_y * self.cell_len + MARGIN_OVER, 
                                         self.cell_len+MAZE_THICKNESS, self.cell_len+MAZE_THICKNESS))