import pygame
from src03.settings import *

class Player:
    def __init__(self,x=300,y=400,speed=5,health=100,radius=20):
        self.x = x  # Posição do player (x)
        self.y = y  # Posição do player (y)
        self.dx = 0 # Direção do movimento x
        self.dy = 0 # Direção do movimento y
        self.speed = speed
        self.health = health
        self.radius = radius

    def draw(self, screen):
        # Desenhar o jogador
        pygame.draw.circle(screen, PLAYER_COLOR,(self.x,self.y),self.radius)

    def move(self):
        # Lógica de movimento
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

        # Manter o player dentro dos limites da tela
        self.x = max(MARGIN + self.radius + 2, 
                     min(self.x, SCREEN_WIDTH - MARGIN - self.radius))
        self.y = max(MARGIN_OVER + self.radius + 2, 
                               min(self.y, SCREEN_HEIGHT - MARGIN - self.radius))

    def update(self):
        self.move()

    def check_collision_enemy(self, enemy):
        # enemy == retângulo
        expanded_enemy = enemy.inflate(self.radius * 2, self.radius * 2)
        return expanded_enemy.collidepoint(self.x, self.y)
    
