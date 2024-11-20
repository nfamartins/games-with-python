import pygame

class Player:
    def __init__(self):
        self.position = (400, 300)
        self.speed = 5
        self.health = 100
        self.radius = 20

    def move(self):
        # Lógica de movimento
        pass

    def draw(self, screen):
        # Desenhar o jogador
        pygame.draw.circle(screen, (255,0,0),self.position,self.radius)
        # pygame.draw.line(screen,(255,0,0),self.position,
        #                  tuple(x + y for x, y in zip(self.position, (0,30))),5)

    def update(self):
        self.move()

