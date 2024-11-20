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
	
    # Desenha um retângulo vermelho 
	# (screen, cor, posicao(cantosuperioresquerdo)/tamanho) 
    # == (scren, (reg,green,blue), (x,y,largura,altura))
	pygame.draw.rect(screen, (255,0,0), (50,50,100,100)) 
	
    # desenha um círculo verde
	# (screen, cor, posicao(centro),raio) == (screen, (red,green,blue), (x,y), raio)
	pygame.draw.circle(screen, (0,255,0), (200,200), 50)
	
    # desenha uma linha
	# (screen, cor, posicao inicial, posicao final, espessura)
	# (screen, (red,green,blue), (x0,y0),(xf,yf), espessura)
	pygame.draw.line(screen, (0,0,255), (300,300),(500,400), 5)
	

	pygame.display.flip() 
pygame.quit()
