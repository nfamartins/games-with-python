import pygame
import random

# Inicialização
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Jogador
player = pygame.Rect(400, 300, 50, 50)
player_speed = 5

# Obstáculos
obstacles = [pygame.Rect(random.randint(0, 750), random.randint(0, 550), 50, 50) for _ in range(5)]

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimento do jogador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed

    # Manter o jogador na tela
    player.clamp_ip(screen.get_rect())

    # Verificar colisões
    for obstacle in obstacles:
        if player.colliderect(obstacle):
            print("Colisão!")

    # Desenhar
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player)
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()