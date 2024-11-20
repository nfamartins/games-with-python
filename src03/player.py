import pygame
from src03.settings import *

class Player:
    def __init__(self,x=300,y=400,speed=5,health=100,radius=20):
        self.x = x # Posição do player (x)
        self.y = y # Posição do player (y)
        self.dx = 0 # Direção do movimento x
        self.dy = 0 # Direção do movimento y
        self.speed = speed
        self.health = health
        self.radius = radius

    def draw(self, screen):
        # Desenhar o jogador
        pygame.draw.circle(screen, PLAYER_COLOR,(self.x,self.y),self.radius)
        # pygame.draw.line(screen,(255,0,0),self.position,
        #                  tuple(x + y for x, y in zip(self.position, (0,30))),5)

    def move(self):
        # Lógica de movimento
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

        # Manter o player dentro dos limites da tela
        self.x = max(10 + self.radius, 
                     min(self.x, 950 - self.radius))
        self.y = max(50 + self.radius, 
                               min(self.y, 710 - self.radius))

    def update(self):
        self.move()


