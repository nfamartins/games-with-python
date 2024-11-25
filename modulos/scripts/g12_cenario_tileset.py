# main_game.py
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
        return self.tiles[tile_id - 1]  # tile_id começa em 1, mas o índice começa em 0

class Scenario:
    def __init__(self, width, height, tile_size):
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.tree_layer = [[0 for _ in range(width)] for _ in range(height)]

    def set_tile(self, x, y, tile_id):
        if 0 <= x < self.width and 0 <= y < self.height:
            if tile_id == 3:  # Se for uma árvore
                self.tree_layer[y][x] = tile_id
            else:
                self.grid[y][x] = tile_id

    def draw(self, screen, tileset):
        for y in range(self.height):
            for x in range(self.width):
                tile_id = self.grid[y][x]
                if tile_id != 0:
                    screen.blit(tileset.get_tile(tile_id), (x * self.tile_size, y * self.tile_size))
        
        # Desenhar árvores por último
        for y in range(self.height):
            for x in range(self.width):
                tile_id = self.tree_layer[y][x]
                if tile_id != 0:
                    screen.blit(tileset.get_tile(tile_id), (x * self.tile_size, y * self.tile_size))

class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Jogo com Tileset")

        self.tile_size = 32
        self.scenario_width = self.screen_width // self.tile_size
        self.scenario_height = self.screen_height // self.tile_size

        self.tileset = Tileset('assets/tileset.png', self.tile_size)
        self.scenario = Scenario(self.scenario_width, self.scenario_height, self.tile_size)

        self.create_scenario()

    def create_scenario(self):
        for y in range(self.scenario_height):
            for x in range(self.scenario_width):
                if y < 2 or y >= self.scenario_height - 2 or x < 2 or x >= self.scenario_width - 2:
                    self.scenario.set_tile(x, y, 4)  # Borda de areia
                elif 5 <= y < 8 and 5 <= x < self.scenario_width - 5:
                    self.scenario.set_tile(x, y, 2)  # Rio
                else:
                    self.scenario.set_tile(x, y, 1)  # Grama
                    if random.random() < 0.1:
                        self.scenario.set_tile(x, y, 3)  # Árvores aleatórias

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((0, 0, 0))  # Preenche a tela com preto
            self.scenario.draw(self.screen, self.tileset)
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()