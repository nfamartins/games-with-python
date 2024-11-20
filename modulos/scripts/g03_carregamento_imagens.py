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
	
    # carrega a imagem
	image = pygame.image.load('images/teste_mario.png')
	# transforma a imagem
	# (image, novo tamanho em pixel) == (image, (largura,altura))
	image = pygame.transform.scale(image, (100, 100))
	# mostra na tela
	# (image, posicao) == (image, (x,y))
	screen.blit(image,(200,500))

	pygame.display.flip() 
pygame.quit()