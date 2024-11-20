import pygame 
import random 

pygame.init() 

# Configuração da tela 
width, height = 800, 600 
screen = pygame.display.set_mode((width, height)) 
pygame.display.set_caption("Jogo de Clique") 

# Cores 
BLACK = (0, 0, 0) 
RED = (255, 0, 0) 
WHITE = (255, 255, 255) 

# Alvo 
target_pos = [random.randint(0, width), random.randint(0, height)] 
target_radius = 20 

# Pontuação 
score = 0 
font = pygame.font.Font(None, 36) 

# Loop principal 
running = True 
clock = pygame.time.Clock() 
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_pos = pygame.mouse.get_pos()
			distance = ((mouse_pos[0] - target_pos[0]) ** 2 + 
			   (mouse_pos[1] - target_pos[1]) ** 2) ** 0.5
			if distance <= target_radius:
				score += 1
				target_pos = [random.randint(0, width), random.randint(0, height)]
			else:
				score -= 1
				target_pos = [random.randint(0, width), random.randint(0, height)]
	# Renderização
	screen.fill(BLACK)
	pygame.draw.circle(screen, RED, target_pos, target_radius)
	score_text = font.render(f"Score: {score}", True, WHITE)
	screen.blit(score_text, (10, 10))
	pygame.display.flip()
	clock.tick(60) 
pygame.quit()