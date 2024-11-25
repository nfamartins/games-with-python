import pygame
import random

class Scenario:
    def __init__(self, width, height, tile_size):
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.grid = [[0 for _ in range(width)] for _ in range(height)]

    def set_tile(self, x, y, tile_id):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = tile_id

    def draw(self, screen, tileset):
        for y in range(self.height):
            for x in range(self.width):
                tile_id = self.grid[y][x]
                if tile_id != 0:  # Assumindo que 0 é um tile vazio
                    screen.blit(tileset[tile_id], (x * self.tile_size, y * self.tile_size))

class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Cenário 2D Simples")

        self.tile_size = 40
        self.scenario_width = self.screen_width // self.tile_size
        self.scenario_height = self.screen_height // self.tile_size

        self.scenario = Scenario(self.scenario_width, self.scenario_height, self.tile_size)
        self.tileset = self.create_tileset()

        self.create_scenario()

    def create_tileset(self):
        tileset = {}
        colors = {
            1: (34, 139, 34),   # Grama (verde escuro)
            2: (0, 128, 0),     # Árvore (verde)
            3: (210, 180, 140), # Areia (bege)
            4: (65, 105, 225),  # Água (azul royal)
        }
        for tile_id, color in colors.items():
            surf = pygame.Surface((self.tile_size, self.tile_size))
            surf.fill(color)
            tileset[tile_id] = surf
        return tileset

    def create_scenario(self):
        # Criando um cenário simples
        for y in range(self.scenario_height):
            for x in range(self.scenario_width):
                if y < 3 or y >= self.scenario_height - 3 or x < 3 or x >= self.scenario_width - 3:
                    self.scenario.set_tile(x, y, 3)  # Borda de areia
                elif 5 <= y < 8 and 5 <= x < self.scenario_width - 5:
                    self.scenario.set_tile(x, y, 4)  # Rio
                else:
                    if random.random() < 0.1:
                        self.scenario.set_tile(x, y, 2)  # Árvores aleatórias
                    else:
                        self.scenario.set_tile(x, y, 1)  # Grama

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