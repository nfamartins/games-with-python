import pygame 

pygame.init() 

# Configuração da tela 
screen = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption("Testando eventos de teclado") 

# Loop principal do jogo 
running = True 
while running:     
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				# ação quando espaço é pressionado
				tecla = 'espaço'
			elif event.key == pygame.K_LEFT:
				# ação quando seta para esquerda é pressionada
				tecla = 'para esquerda'
    # Lógica do jogo
	# Renderização
	screen.fill((0,0,0)) # preenche a tela com preto
	font = pygame.font.Font(None,36)
	try:
		text = font.render(f"Você pressionou: {tecla}", False, (255,255,255))
	except:
		text = font.render("Você pressionou: nada", False, (255,255,255))
	
	screen.blit(text, (400,400))
	
	pygame.display.flip() 
pygame.quit()
