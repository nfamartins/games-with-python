import pygame
import os
import random

# Inicializar Pygame
pygame.init()

# Definir cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)
BROWN = (139, 69, 19)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Criar diretório de assets se não existir
if not os.path.exists('assets/tiles'):
    os.makedirs('assets/tiles')

def create_tile(size, color, details=None):
    surface = pygame.Surface(size)
    surface.fill(color)
    if details:
        details(surface)
    return surface

def add_cracks(surface):
    for _ in range(5):
        start = (random.randint(0, surface.get_width()), random.randint(0, surface.get_height()))
        end = (random.randint(0, surface.get_width()), random.randint(0, surface.get_height()))
        pygame.draw.line(surface, DARK_GRAY, start, end, 1)

def add_windows(surface):
    for i in range(2):
        for j in range(3):
            rect = pygame.Rect(i*16 + 4, j*10 + 2, 8, 6)
            pygame.draw.rect(surface, RED, rect)

def create_tileset(name, tiles):
    tileset_width = len(tiles) * 32
    tileset_height = 32
    tileset = pygame.Surface((tileset_width, tileset_height))
    for i, tile in enumerate(tiles):
        tileset.blit(tile, (i * 32, 0))
    pygame.image.save(tileset, f'assets/tiles/{name}_tileset.png')

# Gerar tiles
tiles = {
    'distopico': [
        create_tile((32, 32), GRAY, add_cracks),
        create_tile((32, 32), DARK_GRAY),
        create_tile((32, 32), BROWN),
    ],
    'atual': [
        create_tile((32, 32), GRAY),
        create_tile((32, 32), WHITE, add_windows),
        create_tile((32, 32), BLACK),  # Asfalto
    ],
    'antigo': [
        create_tile((32, 32), GREEN),
        create_tile((32, 32), BLUE),
        create_tile((32, 32), BROWN),
    ],
    'personagem': [
        create_tile((16, 32), RED),  # Placeholder para personagem
    ],
    'mapa_cidade': [
        create_tile((64, 64), GREEN),
        create_tile((64, 64), GRAY),
        create_tile((64, 64), BLUE),
    ],
    'edificios': [
        create_tile((64, 64), WHITE, add_windows),
        create_tile((64, 64), BROWN),
        create_tile((64, 64), GRAY),
    ],
}

# Criar tilesets
for name, tile_list in tiles.items():
    create_tileset(name, tile_list)

print("Tiles e tilesets gerados com sucesso em 'assets/tiles/'")