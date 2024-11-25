## 1. CONFIGURAÇÃO INICIAL
import pygame 
# Inicialização 
pygame.init() 
# Definir tamanho da tela 
SCREEN_WIDTH = 640 
SCREEN_HEIGHT = 480 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
# Definir título da janela 
pygame.display.set_caption("Pixel Art em Python")

# 2. CRIANDO UMA GRADE DE PIXELS
PIXEL_SIZE = 5 
GRID_WIDTH = SCREEN_WIDTH // PIXEL_SIZE 
GRID_HEIGHT = SCREEN_HEIGHT // PIXEL_SIZE 
grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# 3. DESENHANDO PIXELS
def draw_pixel(x, y, color): 
	pygame.draw.rect(screen, color, (x * PIXEL_SIZE, y * PIXEL_SIZE, 
								  PIXEL_SIZE, PIXEL_SIZE)) 
# Exemplo de uso 
draw_pixel(5, 5, (255, 0, 0)) # Desenha um pixel vermelho na posição (5, 5)

# 4. IMPLEMENTANDO UMA PALETA DE CORES
PALETTE = [ (0, 0, 0), # Preto 
		   (255, 255, 255), # Branco 
		   (255, 0, 0), # Vermelho 
		   (0, 255, 0), # Verde 
		   (0, 0, 255), # Azul 
		   (255, 255, 0), # Amarelo 
] 
current_color = PALETTE[2]

# 5. LOOP PRINCIPAL
running = True 
while running: 
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			running = False 
		elif event.type == pygame.MOUSEBUTTONDOWN: 
			if event.button == 1: # Botão esquerdo do mouse 
				x, y = event.pos 
				grid_x, grid_y = x // PIXEL_SIZE, y // PIXEL_SIZE 
				draw_pixel(grid_x, grid_y, current_color) 
	pygame.display.flip() 
pygame.quit()