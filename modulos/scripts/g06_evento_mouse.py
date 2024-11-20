import pygame 

pygame.init() 

# Configuração da tela 
screen = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption("Testando eventos de mouse") 

# Loop principal do jogo 
running = True 
while running:     
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1: # botão esquerdo do mouse
				# ação quando botão esquerdo é pressionado
				tecla = 'botão esquerdo'
			elif event.button == 3: # botão direito
				# ação quando botão direito é pressionado
				tecla = 'botão direito'
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