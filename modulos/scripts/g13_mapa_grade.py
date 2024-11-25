import pygame
import random

class Tileset:
    def __init__(self, filename, tile_size):
        self.tile_size = tile_size
        self.tileset_image = pygame.image.load(filename).convert_alpha()
        self.rect = self.tileset_image.get_rect()
        self.tiles = []
        self.load_tiles()

    def load_tiles(self):
        x_tiles = self.rect.width // self.tile_size
        for i in range(x_tiles):
            rect = (i * self.tile_size, 0, self.tile_size, self.tile_size)
            self.tiles.append(self.tileset_image.subsurface(rect))

    def get_tile(self, tile_id):
        if tile_id > 0 and tile_id <= len(self.tiles):
            return self.tiles[tile_id - 1]
        return None

class TileMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map_data = [[0 for _ in range(width)] for _ in range(height)]
        self.tree_layer = [[0 for _ in range(width)] for _ in range(height)]

    def set_tile(self, x, y, tile_id):
        if 0 <= x < self.width and 0 <= y < self.height:
            if tile_id == 3:  # Se for uma árvore
                self.tree_layer[y][x] = tile_id
            else:
                self.map_data[y][x] = tile_id

    def get_tile(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.map_data[y][x]
        return None

    def draw(self, screen, tileset, camera_x=0, camera_y=0):
        for y in range(self.height):
            for x in range(self.width):
                tile_id = self.map_data[y][x]
                tile = tileset.get_tile(tile_id)
                if tile:
                    screen.blit(tile, (x * tileset.tile_size - camera_x, y * tileset.tile_size - camera_y))
        
        # Desenhar árvores por último
        for y in range(self.height):
            for x in range(self.width):
                tile_id = self.tree_layer[y][x]
                tile = tileset.get_tile(tile_id)
                if tile:
                    screen.blit(tile, (x * tileset.tile_size - camera_x, y * tileset.tile_size - camera_y))

class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Jogo com TileMap")

        self.tile_size = 32
        self.map_width = self.screen_width // self.tile_size
        self.map_height = self.screen_height // self.tile_size

        self.tileset = Tileset('assets/tileset.png', self.tile_size)
        self.tile_map = TileMap(self.map_width, self.map_height)

        self.create_map()

    def create_map(self):
        for y in range(self.map_height):
            for x in range(self.map_width):
                if y < 2 or y >= self.map_height - 2 or x < 2 or x >= self.map_width - 2:
                    self.tile_map.set_tile(x, y, 4)  # Borda de areia
                elif 5 <= y < 8 and 5 <= x < self.map_width - 5:
                    self.tile_map.set_tile(x, y, 2)  # Rio
                else:
                    self.tile_map.set_tile(x, y, 1)  # Grama
                    if random.random() < 0.1:
                        self.tile_map.set_tile(x, y, 3)  # Árvores aleatórias

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((0, 0, 0))  # Preenche a tela com preto
            self.tile_map.draw(self.screen, self.tileset)
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()