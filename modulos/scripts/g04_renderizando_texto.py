import pygame 

pygame.init() 

# Configuração da tela 
screen = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption("Testando formas") 

# Loop principal do jogo 
running = True 
while running:     
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
    # Lógica do jogo
	# Renderização
	screen.fill((0,0,0)) # preenche a tela com preto
	
    # definindo a fonte (nome da fonte, tamanho)
	# (path da fonte, tamanho)
	font = pygame.font.Font(None,36)
	
    # renderizando a fonte
	# (texto, anti-aliasing, cor)
	text = font.render("Olá, novo dev!", True, (255,255,255))
	text2 = font.render("Olá, novo dev!", False, (255,255,255))
	
    # desenha/blita o texto renderizado na tela
	# (texto, posicao)
	screen.blit(text, (400,400))
	screen.blit(text2, (400,200))

	pygame.display.flip() 
pygame.quit()