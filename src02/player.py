import pygame

class Player:
    def __init__(self):
        self.position = [400, 300]
        self.direction = [0, 0]  # Direção do movimento [x, y]
        self.speed = 5
        self.health = 100
        self.radius = 20

    def draw(self, screen):
        # Desenhar o jogador
        pygame.draw.circle(screen, (255,0,0),self.position,self.radius)
        # pygame.draw.line(screen,(255,0,0),self.position,
        #                  tuple(x + y for x, y in zip(self.position, (0,30))),5)

    def move(self):
        # Lógica de movimento
        self.position[0] += self.direction[0] * self.speed
        self.position[1] += self.direction[1] * self.speed

        # Manter o player dentro dos limites da tela
        self.position[0] = max(10 + self.radius, 
                               min(self.position[0], 950 - self.radius))
        self.position[1] = max(50 + self.radius, 
                               min(self.position[1], 710 - self.radius))

    def update(self):
        self.move()


