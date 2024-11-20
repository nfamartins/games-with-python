import pygame
import random
from src03.player import Player
from src03.settings import *

class Game:
    def __init__(self):  # configuração inicial
        pygame.init() 
        pygame.display.set_caption("Game 03") 
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player()
        self.enemies = RandomEnemies()
        self.FONT_DISPLAY = pygame.font.Font(None, 36)
    
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
        # Movimento contínuo baseado nas teclas pressionadas
        keys = pygame.key.get_pressed()
        self.player.dx = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        self.player.dy = keys[pygame.K_DOWN] - keys[pygame.K_UP]

    def update(self):
        self.player.update()

    def draw_margins(self):
        pygame.draw.line(self.screen,WHITE,   # margens
                         (MARGIN,MARGIN_OVER),(SCREEN_WIDTH-MARGIN,MARGIN_OVER),MARGIN_SIZE)
        pygame.draw.line(self.screen,WHITE,
                         (MARGIN,MARGIN_OVER),(MARGIN,SCREEN_HEIGHT-MARGIN),MARGIN_SIZE)
        pygame.draw.line(self.screen,WHITE,
                         (SCREEN_WIDTH-MARGIN,MARGIN_OVER),(SCREEN_WIDTH-MARGIN,SCREEN_HEIGHT-MARGIN),MARGIN_SIZE)
        pygame.draw.line(self.screen,WHITE,
                         (MARGIN,SCREEN_HEIGHT-MARGIN),(SCREEN_WIDTH-MARGIN,SCREEN_HEIGHT-MARGIN),MARGIN_SIZE)
    
    def draw_display(self):
        # nome
        self.screen.blit(self.FONT_DISPLAY.render(GAME_NAME, False, WHITE),
                         GAME_NAME_POSITION)
        # health
        self.screen.blit(self.FONT_DISPLAY.render(f"Health: {self.player.health}", False, WHITE),
                         HEALTH_POSITION)
        
    def draw(self):                 # tela principal
        self.screen.fill(BLACK) # fundo preto
        self.draw_margins() # margens
        self.draw_display() # display
        self.player.draw(self.screen) # player
        self.enemies.draw(self.screen)


class RandomEnemies:
    def __init__(self,n=5,size=ENEMY_HEIGHT,color=ENEMY_COLOR):
        self.size = size
        self.n = n
        self.create()

    def create(self):
        self.objects = []
        for i in range(self.n):
            x = random.randint(MARGIN, SCREEN_WIDTH - MARGIN)
            y = random.randint(MARGIN_OVER, SCREEN_HEIGHT - MARGIN_OVER)
            self.objects.append(pygame.Rect(x,y,self.size,self.size))
    
    def draw(self,screen):
        for object in self.objects:
            pygame.draw.rect(screen, RED, object)
        