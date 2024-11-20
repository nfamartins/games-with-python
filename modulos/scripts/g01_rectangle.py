import pygame 

pygame.init() 

# Configurações 
WIDTH, HEIGHT = 800, 600 
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
clock = pygame.time.Clock() 
pygame.display.set_caption("Meu Primeiro Jogo Pygame") 

# Propriedades do retângulo 
rect_x, rect_y = 400, 300 
rect_speed = 5 

running = True 
while running: 
	# Processamento de entrada 
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			running = False 
	
	# Atualização 
	keys = pygame.key.get_pressed() 
	if keys[pygame.K_LEFT]: 
		rect_x -= rect_speed 
	if keys[pygame.K_RIGHT]: 
		rect_x += rect_speed 
	if keys[pygame.K_UP]: 
		rect_y -= rect_speed 
	if keys[pygame.K_DOWN]: 
		rect_y += rect_speed 
	
	# Renderização 
	screen.fill((0, 0, 0)) 
	pygame.draw.rect(screen, (255, 0, 0), (rect_x, rect_y, 50, 50)) 
	pygame.display.flip() 
	
	clock.tick(60) 

pygame.quit()