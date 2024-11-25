# tileset_generator.py
import pygame
import os

class Tileset:
    def __init__(self):
        self.tiles = {}

    def load_tile(self, tile_id, image_path):
        self.tiles[tile_id] = pygame.image.load(image_path).convert_alpha()

    def get_tile(self, tile_id):
        return self.tiles.get(tile_id)

    def save_tileset(self, filename):
        pygame.image.save(self.create_tileset_surface(), filename)

    def create_tileset_surface(self):
        tile_size = next(iter(self.tiles.values())).get_size()
        tileset_width = tile_size[0] * len(self.tiles)
        tileset_surface = pygame.Surface((tileset_width, tile_size[1]), pygame.SRCALPHA)
        
        for i, (tile_id, tile) in enumerate(self.tiles.items()):
            tileset_surface.blit(tile, (i * tile_size[0], 0))
        
        return tileset_surface

def generate_tileset():
    # Inicialize o Pygame com o modo de vídeo dummy
    pygame.init()
    pygame.display.set_mode((1, 1), pygame.NOFRAME)

    tileset = Tileset()

    # Carregando tiles individuais
    tileset.load_tile(1, 'assets/grass.png')
    tileset.load_tile(2, 'assets/water.png')
    tileset.load_tile(3, 'assets/tree.png')
    tileset.load_tile(4, 'assets/sand.png')

    # Salvando o tileset como uma única imagem
    tileset.save_tileset('assets/tileset.png')
    print("Tileset gerado com sucesso!")

    # Encerre o Pygame
    pygame.quit()

if __name__ == "__main__":
    generate_tileset()