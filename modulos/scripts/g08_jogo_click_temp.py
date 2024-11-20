import pygame
import random
import time

pygame.init()

# Configuração da tela
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jogo de Clique Temporizado")

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

# Tempo
target_duration = 1500  # 1000 milissegundos = 1 segundo
target_spawn_time = pygame.time.get_ticks() # retorna a quantidade de tempo desde a inicialização do aplicativo

# Loop principal
running = True
clock = pygame.time.Clock()
while running:
    current_time = pygame.time.get_ticks()
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
                target_spawn_time = current_time
            else:
                score -= 1
                target_pos = [random.randint(0, width), random.randint(0, height)]
                target_spawn_time = current_time

    # Verifica se o tempo do alvo expirou
    if current_time - target_spawn_time > target_duration:
        score -= 1
        target_pos = [random.randint(0, width), random.randint(0, height)]
        target_spawn_time = current_time

    # Renderização
    screen.fill(BLACK)
    
    # Desenha o alvo 
    pygame.draw.circle(screen, RED, target_pos, target_radius)

    # visualização do score
    score_text = font.render(f"Score: {score}", False, WHITE)
    screen.blit(score_text, (10, 35))

    # visualização do tempo
    temp_text = font.render(f"Tempo: {pygame.time.get_ticks()/1000}", False, WHITE)
    screen.blit(temp_text, (10, 10))

    pygame.display.flip()
    clock.tick(60) # limita o jogo a 60 FPS

pygame.quit()