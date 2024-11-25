import pygame
import random
from srcP1.player import Player
from srcP1.maze import Maze
from srcP1.settings import *

class Game:
    def __init__(self):  # configuração inicial
        pygame.init() 
        pygame.display.set_caption("Labirinto") 
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.maze = Maze()
        self.player = Player(maze=self.maze)
        self.objective_reached = False
        self.enemies = RandomEnemies()
        self.enemies_collision = False
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
        self.get_controls() # Movimento contínuo baseado nas teclas pressionadas
        self.check_collisions()
        if self.player.check_objective_reached():
            self.objective_reached = True
    
    def get_controls(self):
        # Movimento contínuo baseado nas teclas pressionadas
        keys = pygame.key.get_pressed()
        self.player.dx = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        self.player.dy = keys[pygame.K_DOWN] - keys[pygame.K_UP]
    
    def check_collisions(self):
        enemies = self.enemies.objects
        index = 0
        for enemy in enemies:
            if self.player.check_collision_enemy(enemy):
                del self.enemies.objects[index]
                self.enemies_collision = True
            index += 1

    def update(self):
        self.player.update()
        if self.enemies_collision:
            self.player.health -= 30
            self.enemies_collision = False
        

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
        
    def draw(self):                    # tela principal
        if self.objective_reached:
            self.draw_victory_screen()
        elif self.player.dead:
            self.draw_looser_screen()
        else:
            self.screen.fill(BLACK)        # fundo preto
            self.maze.draw(self.screen)    # labirinto
            self.draw_margins()            # margens
            self.draw_display()            # display
            self.player.draw(self.screen)  # player
            self.enemies.draw(self.screen) # inimigos
    
    def draw_victory_screen(self): # tela de vitória
        self.screen.fill(BLACK)
        victory_text = self.FONT_DISPLAY.render("Você venceu!", True, WHITE)
        text_rect = victory_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(victory_text, text_rect)
    
    def draw_looser_screen(self): # tela de vitória
        self.screen.fill(BLACK)
        victory_text = self.FONT_DISPLAY.render("Você perdeu! :/", True, RED)
        text_rect = victory_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(victory_text, text_rect)

class RandomEnemies:
    def __init__(self,n=ENEMY_N,size=ENEMY_HEIGHT,color=ENEMY_COLOR):
        self.size = size
        self.color = color
        self.n = n
        self.create()

    def create(self):
        self.objects = []
        for i in range(self.n):
            x = MARGIN + random.randint(1,MAZE_WIDTH-1) * MAZE_CELL_LEN + MAZE_THICKNESS
            y = MARGIN_OVER + random.randint(1,MAZE_HEIGTH-1) * MAZE_CELL_LEN + MAZE_THICKNESS
            self.objects.append(pygame.Rect(x,y,self.size,self.size))
    
    def draw(self,screen):
        for object in self.objects:
            pygame.draw.rect(screen, self.color, object)