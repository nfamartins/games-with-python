import pygame
from src02.player import Player

class Game:
    def __init__(self):  # configuração inicial
        pygame.init() 
        pygame.display.set_caption("Game 01") 
        self.screen = pygame.display.set_mode((960, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player()
    
    def run(self): 
        while self.running:      # loop principal
            self.handle_events() # loop de tratamento de eventos
            self.update()        # atualiza a posição do player
            self.draw()          # renderização
            pygame.display.flip()
            self.clock.tick(60)

    def handle_events(self):     # loop de tratamento de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        # Movimento contínuo baseado nas teclas pressionadas
        keys = pygame.key.get_pressed()
        self.player.direction[0] = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        self.player.direction[1] = keys[pygame.K_DOWN] - keys[pygame.K_UP]

    def update(self):
        self.player.update()
        
    def draw(self):                 # tela principal
        self.screen.fill((0, 0, 0)) # fundo preto
        pygame.draw.line(self.screen,(255,255,255),   # margens
                         (10,50),(950,50),2)
        pygame.draw.line(self.screen,(255,255,255),
                         (10,50),(10,710),2)
        pygame.draw.line(self.screen,(255,255,255),
                         (950,50),(950,710),2)
        pygame.draw.line(self.screen,(255,255,255),
                         (10,710),(950,710),2)
        
        font = pygame.font.Font(None, 36)
        name_text = font.render(f"GAME 01", False, (255,255,255))
        self.screen.blit(name_text,(10,15))

        # score_text = font.render(f"Score: --", False, (255,255,255))
        # self.screen.blit(score_text,(850,15))

        health_text = font.render(f"Health: {self.player.health}", 
                                  False, (255,255,255))
        self.screen.blit(health_text,(800,15))

        # player
        self.player.draw(self.screen)


