import pygame

class Labirinto:
    def __init__(self):
        self.labirinto = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]
        ]
    
    def draw(self, screen):
        for y, row in enumerate(self.labirinto):
            for x, cell in enumerate(row):
                if cell == 1:
                    pygame.draw.rect(screen, (0, 0, 0), (x*32, y*32, 32, 32))