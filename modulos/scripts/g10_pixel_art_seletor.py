import pygame

class PixelArtGame:
    def __init__(self):
        pygame.init()
        self.SCREEN_WIDTH = 640
        self.SCREEN_HEIGHT = 480
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Pixel Art em Python com Seletor de Cor")

        self.PIXEL_SIZE = 10
        self.GRID_WIDTH = self.SCREEN_WIDTH // self.PIXEL_SIZE
        self.GRID_HEIGHT = (self.SCREEN_HEIGHT - 40) // self.PIXEL_SIZE

        self.grid = [[None for _ in range(self.GRID_WIDTH)] for _ in range(self.GRID_HEIGHT)]

        self.PALETTE = [
            (0, 0, 0),       # Preto
            (255, 255, 255), # Branco
            (255, 0, 0),     # Vermelho
            (0, 255, 0),     # Verde
            (0, 0, 255),     # Azul
            (255, 255, 0),   # Amarelo
            (255, 0, 255),   # Magenta
            (0, 255, 255),   # Ciano
        ]
        self.current_color = self.PALETTE[0]

    def draw_pixel(self, x, y, color):
        pygame.draw.rect(self.screen, color, (x * self.PIXEL_SIZE, y * self.PIXEL_SIZE, self.PIXEL_SIZE, self.PIXEL_SIZE))

    def draw_palette(self):
        for i, color in enumerate(self.PALETTE):
            pygame.draw.rect(self.screen, color, (i * 40, self.SCREEN_HEIGHT - 40, 40, 40))
            if color == self.current_color:
                pygame.draw.rect(self.screen, (255, 255, 255), (i * 40, self.SCREEN_HEIGHT - 40, 40, 40), 2)

    def get_color_from_pos(self, pos):
        x, y = pos
        if y > self.SCREEN_HEIGHT - 40:
            index = x // 40
            if index < len(self.PALETTE):
                return self.PALETTE[index]
        return None

    def handle_click(self, pos):
        x, y = pos
        color = self.get_color_from_pos(pos)
        if color:
            self.current_color = color
        else:
            grid_x, grid_y = x // self.PIXEL_SIZE, y // self.PIXEL_SIZE
            if 0 <= grid_x < self.GRID_WIDTH and 0 <= grid_y < self.GRID_HEIGHT:
                self.grid[grid_y][grid_x] = self.current_color

    def draw_grid(self):
        for y in range(self.GRID_HEIGHT):
            for x in range(self.GRID_WIDTH):
                if self.grid[y][x]:
                    self.draw_pixel(x, y, self.grid[y][x])

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Botão esquerdo do mouse
                        self.handle_click(event.pos)

            self.screen.fill((200, 200, 200))  # Cor de fundo cinza claro
            self.draw_grid()
            self.draw_palette()
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    game = PixelArtGame()
    game.run()