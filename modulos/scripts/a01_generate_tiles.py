import pygame
import random
import os

def create_grass_tile(size):
    surface = pygame.Surface((size, size))
    color = (34, 139, 34)  # Verde escuro
    surface.fill(color)
    return surface

def create_water_tile(size):
    surface = pygame.Surface((size, size))
    color = (65, 105, 225)  # Azul royal
    surface.fill(color)
    # Adicionar algumas ondas simples
    for i in range(0, size, 4):
        pygame.draw.line(surface, (100, 149, 237), (0, i), (size, i), 2)
    return surface

def create_tree_tile(size):
    surface = pygame.Surface((size, size), pygame.SRCALPHA)
    # Tronco
    pygame.draw.rect(surface, (139, 69, 19), (size//3, size//2, size//3, size//2))
    # Copa
    pygame.draw.circle(surface, (0, 100, 0), (size//2, size//3), size//3)
    return surface

def create_sand_tile(size):
    surface = pygame.Surface((size, size))
    color = (210, 180, 140)  # Bege
    surface.fill(color)
    # Adicionar alguns pontos para textura
    for _ in range(20):
        x = random.randint(0, size)
        y = random.randint(0, size)
        pygame.draw.circle(surface, (188, 158, 118), (x, y), 1)
    return surface

def generate_tiles():
    pygame.init()
    tile_size = 32
    
    if not os.path.exists('assets'):
        os.makedirs('assets')

    tiles = {
        'grass.png': create_grass_tile,
        'water.png': create_water_tile,
        'tree.png': create_tree_tile,
        'sand.png': create_sand_tile
    }

    for filename, create_func in tiles.items():
        tile = create_func(tile_size)
        pygame.image.save(tile, os.path.join('assets', filename))

    print("Tiles gerados com sucesso!")

if __name__ == "__main__":
    generate_tiles()