[&larr; voltar para início](../README.md)

Bem-vindo ao segundo módulo do nosso curso de desenvolvimento de jogos em Python! Vamos explorar os conceitos fundamentais de pixel art e como aplicá-los utilizando Python. A pixel art é uma forma de arte digital que tem sido amplamente utilizada no desenvolvimento de jogos, especialmente em títulos indie e retro.

# 1. Teoria
## 1.1 Conceitos de pixel art e como aplicá-los em Python
### Conceitos Básicos de Pixel Art
Pixel art é uma forma de arte digital onde as imagens são criadas e editadas no nível do pixel, que é a menor unidade de uma imagem digital. Este estilo de arte surgiu devido às limitações tecnológicas dos primeiros consoles de videogame, mas hoje é amplamente utilizado por seu apelo estético e nostálgico ([Produção de Jogos](https://producaodejogos.com/pixel-art/)).

**Características Principais**
1. **Pixels Visíveis**: Em pixel art, cada pixel é intencionalmente visível e contribui para a forma e textura da imagem.
2. **Paleta de Cores Limitada**: Tradicionalmente, pixel art utiliza um número limitado de cores, embora isso possa variar dependendo do estilo e da plataforma.
3. **Anti-aliasing controlado**: O uso de anti-aliasing (suavização de bordas) é cuidadosamente controlado, muitas vezes feito manualmente pixel por pixel.

### Aplicando Pixel Art em Python
Para criar pixel art em Python, podemos utilizar bibliotecas gráficas como Pygame. Vamos explorar como implementar alguns conceitos básicos:

**Veja o exemplo abaixo**
Etapas:
1. Configuração inicial: Primeiro, precisamos configurar nosso ambiente
2. Criando uma Grade de Pixels: Para trabalhar com pixel art, é útil criar uma grade de pixels
3. Desenhando Pixels: Agora podemos desenhar pixels individuais
4. Implementando uma Paleta de Cores: Uma paleta de cores limitada é essencial para pixel art
5. Loop Principal: O loop principal do jogo permite interação e atualização contínua

```python
## 1. CONFIGURAÇÃO INICIAL
import pygame 
# Inicialização 
pygame.init() 
# Definir tamanho da tela 
SCREEN_WIDTH = 640 
SCREEN_HEIGHT = 480 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
# Definir título da janela 
pygame.display.set_caption("Pixel Art em Python")

# 2. CRIANDO UMA GRADE DE PIXELS
PIXEL_SIZE = 10 
GRID_WIDTH = SCREEN_WIDTH // PIXEL_SIZE 
GRID_HEIGHT = SCREEN_HEIGHT // PIXEL_SIZE 
grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# 3. DESENHANDO PIXELS
def draw_pixel(x, y, color): 
	pygame.draw.rect(screen, color, 
	(x * PIXEL_SIZE, y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE)) 
# Exemplo de uso 
draw_pixel(5, 5, (255, 0, 0)) # Desenha um pixel vermelho na posição (5, 5)

# 4. IMPLEMENTANDO UMA PALETA DE CORES
PALETTE = [ (0, 0, 0), # Preto 
		   (255, 255, 255), # Branco 
		   (255, 0, 0), # Vermelho 
		   (0, 255, 0), # Verde 
		   (0, 0, 255), # Azul 
		   (255, 255, 0), # Amarelo 
] 
current_color = PALETTE[0]
# 5. LOOP PRINCIPAL
running = True 
while running: 
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			running = False 
		elif event.type == pygame.MOUSEBUTTONDOWN: 
			if event.button == 1: # Botão esquerdo do mouse 
				x, y = event.pos 
				grid_x, grid_y = x // PIXEL_SIZE, y // PIXEL_SIZE 
				draw_pixel(grid_x, grid_y, current_color) 
	pygame.display.flip() 
pygame.quit()
```

Adicionando um seletor de cores:
```python
import pygame

class PixelArtGame:
    def __init__(self):
        pygame.init()
        self.SCREEN_WIDTH = 640
        self.SCREEN_HEIGHT = 480
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Pixel Art em Python com Seletor de Cor")
        self.PIXEL_SIZE = 10
        self.GRID_WIDTH = self.SCREEN_WIDTH // self.PIXEL_SIZE
        self.GRID_HEIGHT = (self.SCREEN_HEIGHT - 40) // self.PIXEL_SIZE
        self.grid = [[None for _ in range(self.GRID_WIDTH)] for _ in range(self.GRID_HEIGHT)]
        self.PALETTE = [
            (0, 0, 0),       # Preto
            (255, 255, 255), # Branco
            (255, 0, 0),     # Vermelho
            (0, 255, 0),     # Verde
            (0, 0, 255),     # Azul
            (255, 255, 0),   # Amarelo
            (255, 0, 255),   # Magenta
            (0, 255, 255),   # Ciano
        ]
        self.current_color = self.PALETTE[0]
        
    def draw_pixel(self, x, y, color):
        pygame.draw.rect(self.screen, color, (x * self.PIXEL_SIZE, y * self.PIXEL_SIZE, self.PIXEL_SIZE, self.PIXEL_SIZE))

    def draw_palette(self):
        for i, color in enumerate(self.PALETTE):
            pygame.draw.rect(self.screen, color, (i * 40, self.SCREEN_HEIGHT - 40, 40, 40))
            if color == self.current_color:
                pygame.draw.rect(self.screen, (255, 255, 255), (i * 40, self.SCREEN_HEIGHT - 40, 40, 40), 2)

    def get_color_from_pos(self, pos):
        x, y = pos
        if y > self.SCREEN_HEIGHT - 40:
            index = x // 40
            if index < len(self.PALETTE):
                return self.PALETTE[index]
        return None
        
    def handle_click(self, pos):
        x, y = pos
        color = self.get_color_from_pos(pos)
        if color:
            self.current_color = color
        else:
            grid_x, grid_y = x // self.PIXEL_SIZE, y // self.PIXEL_SIZE
            if 0 <= grid_x < self.GRID_WIDTH and 0 <= grid_y < self.GRID_HEIGHT:
                self.grid[grid_y][grid_x] = self.current_color

    def draw_grid(self):
        for y in range(self.GRID_HEIGHT):
            for x in range(self.GRID_WIDTH):
                if self.grid[y][x]:
                    self.draw_pixel(x, y, self.grid[y][x])
                    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Botão esquerdo do mouse
                        self.handle_click(event.pos)
            self.screen.fill((200, 200, 200))  # Cor de fundo cinza claro
            self.draw_grid()
            self.draw_palette()
            pygame.display.flip()
		pygame.quit()

  

if __name__ == "__main__":
    game = PixelArtGame()
    game.run()
```

### Técnicas Avançadas
1. **Dithering**: Técnica para criar a ilusão de mais cores usando padrões de pixels ([Produção de jogos](https://producaodejogos.com/pixel-art/)).
2. **Spriting**: Criação de personagens e objetos animados usando sequências de imagens pixel art.
3. **Tile-based Design**: Criação de cenários usando blocos (tiles) repetitivos.
### Conclusão
A pixel art é uma forma de expressão artística poderosa no desenvolvimento de jogos. Com Python e Pygame, podemos facilmente implementar os conceitos básicos e começar a criar nossas próprias obras de pixel art. À medida que você pratica e experimenta, desenvolverá suas habilidades e seu estilo único.
Lembre-se, a chave para se tornar proficiente em pixel art é a prática constante e a experimentação com diferentes técnicas e estilos. Não tenha medo de começar com projetos simples e gradualmente aumentar a complexidade à medida que ganha confiança e habilidade.

**Mais conteúdos**
1. Vídeos
	1. "Aseprite Tutorial For Beginners (Pixel Art)" no YouTube. Este tutorial abrangente ensina as ferramentas básicas do Aseprite, dicas e fluxo de trabalho para criar pixel art.
	2. Série de tutoriais em vídeo do canal "Pixel Art Academy" no YouTube, que oferece lições detalhadas sobre várias técnicas de pixel art.
	3. "Pixel Art Masterclass" da Udemy, um curso mais extenso que cobre desde os fundamentos até técnicas avançadas de pixel art.
2. Artigos
	1. ["Pixel Art in Python" do site 101 Computing](https://www.101computing.net/pixel-art-in-python/). Este artigo explora como usar listas em Python para criar gráficos de pixel art 2D, oferecendo uma perspectiva técnica interessante.
	2. ["Pixel Art: Tudo que Você Precisa Saber para Começar" no site Produção de Jogos](https://producaodejogos.com/pixel-art/). Este artigo abrangente cobre os fundamentos da pixel art, incluindo conceitos básicos e ferramentas.
	3. ["Pixel Art | Dicas cruciais para iniciantes" do site Crie Seus Jogos](https://www.crieseusjogos.com.br/pixel-art-dicas-cruciais-para-iniciantes/). Oferece dicas práticas para iniciantes, incluindo recomendações de ferramentas e técnicas básicas.
	4. "The Ultimate Pixel Art Tutorial" no site Lospec, que fornece um guia detalhado sobre técnicas de pixel art, desde o básico até o avançado.
	5. "Pixel Art for Beginners" no site Envato Tuts+, um guia passo a passo para criar seu primeiro sprite em pixel art.
## 1.2 Mapas em 2D: criação de cenários, tilesets e mapas baseados em grade
Vamos explorar o mundo dos mapas 2D em jogos, focando na criação de cenários, tilesets e mapas baseados em grade. Este é um tópico fundamental para o desenvolvimento de jogos 2D, especialmente quando trabalhamos com pixel art.
### Conceitos Básicos
Os mapas 2D são a base de muitos jogos clássicos e modernos. Eles representam o ambiente do jogo de uma perspectiva de cima para baixo ou lateral, usando uma série de imagens (tiles) organizadas em uma grade.

**Componentes Principais**
1. **Tiles**: Pequenas imagens quadradas que, quando combinadas, formam o cenário completo.
2. **Tilesets**: Conjuntos de tiles que compartilham um tema ou estilo visual comum.
3. **Grid (Grade)**: A estrutura invisível que organiza os tiles no mapa.
4. **Layers (Camadas)**: Diferentes níveis de tiles sobrepostos para criar profundidade e complexidade.

**Criação de Cenários**
A criação de cenários envolve a concepção e design do mundo do jogo. Isso inclui:
1. **Planejamento**: Esboçar o layout geral do mapa, definindo áreas-chave e fluxo do jogo.
2. **Tematização**: Escolher um tema visual coerente (por exemplo, floresta, deserto, cidade futurista).
3. **Detalhamento**: Adicionar elementos que dão vida ao cenário, como vegetação, estruturas e objetos interativos.

 **Implementação em Python:**
```python
import pygame 

class Scenario: 
	def __init__(self, width, height, tile_size): 
		self.width = width 
		self.height = height 
		self.tile_size = tile_size 
		self.grid = [[0 for _ in range(width)] for _ in range(height)] 
	
	def set_tile(self, x, y, tile_id): 
		if 0 <= x < self.width and 0 <= y < self.height: 
			self.grid[y][x] = tile_id 
			
	def draw(self, screen, tileset): 
		for y in range(self.height): 
			for x in range(self.width): 
				tile_id = self.grid[y][x] 
				if tile_id != 0: 
					# Assumindo que 0 é um tile vazio 
					screen.blit(tileset[tile_id], 
						(x * self.tile_size, y * self.tile_size))
```

Veja um exemplo prático de um game com um cenário simples neste [script](modulos/scripts/g11_cenarios.py). Neste código, fizemos o seguinte:
1. Criamos uma classe `Game` que gerencia o jogo.
2. No método `create_tileset()`, definimos quatro tipos de tiles: grama, árvore, areia e água.
3. O método `create_scenario()` cria um cenário simples com:
    - Uma borda de areia
    - Um rio no meio
    - Grama cobrindo a maior parte do cenário
    - Árvores espalhadas aleatoriamente
    
4. O método `run()` configura o loop principal do jogo, lidando com eventos e renderizando o cenário.
5. Usamos `pygame.time.Clock()` para controlar a taxa de quadros do jogo.
### Tilesets
Tilesets são coleções de tiles individuais que podem ser combinados para criar mapas completos.

**Características Importantes**
1. **Consistência Visual**: Todos os tiles devem compartilhar um estilo artístico coerente.
2. **Variedade**: Incluir diferentes variações de terrenos, objetos e decorações.
3. **Modularidade**: Tiles devem se conectar suavemente uns aos outros.

**Tipos Comuns de Tiles**
- Terreno base (grama, areia, água)
- Bordas e transições
- Objetos (árvores, rochas, construções)
- Decorações (flores, arbustos, detalhes de ambiente)

#### Implementação de um Tileset em Python
Primeiro, podemos criar um imagens .png de ==tiles individuais==:
```python
import pygame
import random
import os

def create_grass_tile(size):
    surface = pygame.Surface((size, size))
    color = (34, 139, 34)  # Verde escuro
    surface.fill(color)
    return surface

def create_water_tile(size):
    surface = pygame.Surface((size, size))
    color = (65, 105, 225)  # Azul royal
    surface.fill(color)
    # Adicionar algumas ondas simples
    for i in range(0, size, 4):
        pygame.draw.line(surface, (100, 149, 237), (0, i), (size, i), 2)
    return surface
    
def create_tree_tile(size):
    surface = pygame.Surface((size, size), pygame.SRCALPHA)
    # Tronco
    pygame.draw.rect(surface, (139, 69, 19), (size//3, size//2, size//3, size//2))
    # Copa
    pygame.draw.circle(surface, (0, 100, 0), (size//2, size//3), size//3)
    return surface

def create_sand_tile(size):
    surface = pygame.Surface((size, size))
    color = (210, 180, 140)  # Bege
    surface.fill(color)
    # Adicionar alguns pontos para textura
    for _ in range(20):
        x = random.randint(0, size)
        y = random.randint(0, size)
        pygame.draw.circle(surface, (188, 158, 118), (x, y), 1)
    return surface

def generate_tiles():
    pygame.init()
    tile_size = 32
    if not os.path.exists('assets'):
        os.makedirs('assets')
    tiles = {
        'grass.png': create_grass_tile,
        'water.png': create_water_tile,
        'tree.png': create_tree_tile,
        'sand.png': create_sand_tile
    }

    for filename, create_func in tiles.items():
        tile = create_func(tile_size)
        pygame.image.save(tile, os.path.join('assets', filename))
    print("Tiles gerados com sucesso!")

if __name__ == "__main__":
    generate_tiles()
```

Agora, vamos criar o `tileset_generator.py` para usar esses tiles gerados e ==criar um tileset==:
```python
import pygame
import os

class Tileset:
    def __init__(self):
        self.tiles = {}

    def load_tile(self, tile_id, image_path):
        self.tiles[tile_id] = pygame.image.load(image_path).convert_alpha()
        
    def get_tile(self, tile_id):
        return self.tiles.get(tile_id)
  
    def save_tileset(self, filename):
        pygame.image.save(self.create_tileset_surface(), filename)
  
    def create_tileset_surface(self):
        tile_size = next(iter(self.tiles.values())).get_size()
        tileset_width = tile_size[0] * len(self.tiles)
        tileset_surface = pygame.Surface((tileset_width, tile_size[1]), pygame.SRCALPHA)
        for i, (tile_id, tile) in enumerate(self.tiles.items()):
            tileset_surface.blit(tile, (i * tile_size[0], 0))
        return tileset_surface

def generate_tileset():
    # Inicialize o Pygame com o modo de vídeo dummy
    pygame.init()
    pygame.display.set_mode((1, 1), pygame.NOFRAME)
    tileset = Tileset()
    # Carregando tiles individuais
    tileset.load_tile(1, 'assets/grass.png')
    tileset.load_tile(2, 'assets/water.png')
    tileset.load_tile(3, 'assets/tree.png')
    tileset.load_tile(4, 'assets/sand.png')
    # Salvando o tileset como uma única imagem
    tileset.save_tileset('assets/tileset.png')
    print("Tileset gerado com sucesso!")
    # Encerre o Pygame
    pygame.quit()

if __name__ == "__main__":
    generate_tileset()
```

E, por fim, vamos gerar um jogo que utilize o tileset gerado:
```python
import pygame
import random
  
class Tileset:
    def __init__(self, filename, tile_size):
        self.tile_size = tile_size
        self.tileset_image = pygame.image.load(filename).convert_alpha()
        self.rect = self.tileset_image.get_rect()
        self.tiles = []
        self.load_tiles()
  
    def load_tiles(self):
        x_tiles = self.rect.width // self.tile_size
        for i in range(x_tiles):
            rect = (i * self.tile_size, 0, self.tile_size, self.tile_size)
            self.tiles.append(self.tileset_image.subsurface(rect))

    def get_tile(self, tile_id):
        return self.tiles[tile_id - 1]  # tile_id começa em 1, mas o índice começa em 0
  
class Scenario:
    def __init__(self, width, height, tile_size):
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.tree_layer = [[0 for _ in range(width)] for _ in range(height)]

    def set_tile(self, x, y, tile_id):
        if 0 <= x < self.width and 0 <= y < self.height:
            if tile_id == 3:  # Se for uma árvore
                self.tree_layer[y][x] = tile_id
            else:
                self.grid[y][x] = tile_id
  
    def draw(self, screen, tileset):
        for y in range(self.height):
            for x in range(self.width):
                tile_id = self.grid[y][x]
                if tile_id != 0:
                    screen.blit(tileset.get_tile(tile_id), (x * self.tile_size, y * self.tile_size))
        # Desenhar árvores por último
        for y in range(self.height):
            for x in range(self.width):
                tile_id = self.tree_layer[y][x]
                if tile_id != 0:
                    screen.blit(tileset.get_tile(tile_id), (x * self.tile_size, y * self.tile_size))

class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Jogo com Tileset")
        self.tile_size = 32
        self.scenario_width = self.screen_width // self.tile_size
        self.scenario_height = self.screen_height // self.tile_size
        self.tileset = Tileset('assets/tileset.png', self.tile_size)
        self.scenario = Scenario(self.scenario_width, self.scenario_height, self.tile_size)
        self.create_scenario()

    def create_scenario(self):
        for y in range(self.scenario_height):
            for x in range(self.scenario_width):
                if y < 2 or y >= self.scenario_height - 2 or x < 2 or x >= self.scenario_width - 2:
                    self.scenario.set_tile(x, y, 4)  # Borda de areia
                elif 5 <= y < 8 and 5 <= x < self.scenario_width - 5:
                    self.scenario.set_tile(x, y, 2)  # Rio
                else:
                    self.scenario.set_tile(x, y, 1)  # Grama
                    if random.random() < 0.1:
                        self.scenario.set_tile(x, y, 3)  # Árvores aleatórias
                        
    def run(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill((0, 0, 0))  # Preenche a tela com preto
            self.scenario.draw(self.screen, self.tileset)
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
  
if __name__ == "__main__":
    game = Game()
    game.run()
```

Alguns pontos importantes:
1. Na classe `Scenario`, adicionamos uma camada separada para árvores (`tree_layer`).
2. Modificamos o método `set_tile` para colocar árvores na camada de árvores.
3. Alteramos o método `draw` para primeiro desenhar todos os tiles de base e depois desenhar as árvores por cima.
4. No método `create_scenario`, garantimos que a grama seja sempre colocada antes das árvores.

Essas ações garantem que:
1. As árvores sejam desenhadas por último, ficando por cima da grama.
2. A transparência das árvores seja preservada.
3. Cada tile de árvore tenha grama por baixo.

==Este processo completo cria tiles simples, gera um tileset a partir deles e usa esse tileset em um jogo básico==. Os tiles gerados são bem simples, mas servem como um bom ponto de partida. Você pode modificar as funções de geração de tiles no `tile_generator.py` para criar designs mais elaborados ou adicionar mais variedade de tiles.Lembre-se de que este é apenas um começo. A partir daqui, você pode expandir o jogo adicionando mais tipos de tiles, criando cenários mais complexos, implementando personagens jogáveis, inimigos, colisões e muito mais.
### Mapas Baseados em Grade
Mapas baseados em grade organizam os tiles em uma estrutura matricial, facilitando o posicionamento e a lógica do jogo.

**Vantagens**
1. **Simplicidade**: Fácil de implementar e entender.
2. **Eficiência**: Permite otimizações de renderização e colisão.
3. **Flexibilidade**: Suporta diferentes tipos de jogos (RPGs, estratégia, puzzle).

 **Implementação de um Mapa em Grade**
 ```python
 class TileMap: 
	 def __init__(self, width, height): 
		 self.width = width 
		 self.height = height 
		 self.map_data = [[0 for _ in range(width)] for _ in range(height)] 
		 
	 def set_tile(self, x, y, tile_id): 
		 if 0 <= x < self.width and 0 <= y < self.height: 
			 self.map_data[y][x] = tile_id 
			 
	 def get_tile(self, x, y): 
		 if 0 <= x < self.width and 0 <= y < self.height: 
			 return self.map_data[y][x] 
		 return None 
		 
	 def draw(self, screen, tileset, camera_x=0, camera_y=0): 
		 for y in range(self.height): 
			 for x in range(self.width): 
				 tile_id = self.map_data[y][x] 
				 tile = tileset.get_tile(tile_id) 
				 if tile: 
					 screen.blit(tile, (x * TILE_SIZE - camera_x, y * TILE_SIZE - camera_y))
```

Modificando o game anterior para usar um mapa baseado em grade:
```python
import pygame
import random

class Tileset:
    def __init__(self, filename, tile_size):
        self.tile_size = tile_size
        self.tileset_image = pygame.image.load(filename).convert_alpha()
        self.rect = self.tileset_image.get_rect()
        self.tiles = []
        self.load_tiles()
  
    def load_tiles(self):
        x_tiles = self.rect.width // self.tile_size
        for i in range(x_tiles):
            rect = (i * self.tile_size, 0, self.tile_size, self.tile_size)
            self.tiles.append(self.tileset_image.subsurface(rect))

    def get_tile(self, tile_id):
        if tile_id > 0 and tile_id <= len(self.tiles):
            return self.tiles[tile_id - 1]
        return None

class TileMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map_data = [[0 for _ in range(width)] for _ in range(height)]
        self.tree_layer = [[0 for _ in range(width)] for _ in range(height)]

    def set_tile(self, x, y, tile_id):
        if 0 <= x < self.width and 0 <= y < self.height:
            if tile_id == 3:  # Se for uma árvore
                self.tree_layer[y][x] = tile_id
            else:
                self.map_data[y][x] = tile_id
  
    def get_tile(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.map_data[y][x]
        return None
  
    def draw(self, screen, tileset, camera_x=0, camera_y=0):
        for y in range(self.height):
            for x in range(self.width):
                tile_id = self.map_data[y][x]
                tile = tileset.get_tile(tile_id)
                if tile:
                    screen.blit(tile, (x * tileset.tile_size - camera_x, y * tileset.tile_size - camera_y))

        # Desenhar árvores por último
        for y in range(self.height):
            for x in range(self.width):
                tile_id = self.tree_layer[y][x]
                tile = tileset.get_tile(tile_id)
                if tile:
                    screen.blit(tile, (x * tileset.tile_size - camera_x, y * tileset.tile_size - camera_y))
  
class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Jogo com TileMap")
        self.tile_size = 32
        self.map_width = self.screen_width // self.tile_size
        self.map_height = self.screen_height // self.tile_size
        self.tileset = Tileset('assets/tileset.png', self.tile_size)
        self.tile_map = TileMap(self.map_width, self.map_height)
        self.create_map()
        
    def create_map(self):
        for y in range(self.map_height):
            for x in range(self.map_width):
                if y < 2 or y >= self.map_height - 2 or x < 2 or x >= self.map_width - 2:
                    self.tile_map.set_tile(x, y, 4)  # Borda de areia
                elif 5 <= y < 8 and 5 <= x < self.map_width - 5:
                    self.tile_map.set_tile(x, y, 2)  # Rio
                else:
                    self.tile_map.set_tile(x, y, 1)  # Grama
                    if random.random() < 0.1:
                        self.tile_map.set_tile(x, y, 3)  # Árvores aleatórias

    def run(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill((0, 0, 0))  # Preenche a tela com preto
            self.tile_map.draw(self.screen, self.tileset)
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
        
if __name__ == "__main__":
    game = Game()
    game.run()
```

As principais mudanças nesta versão são:
1. Substituímos a classe `Scenario` pela classe `TileMap`, que agora gerencia tanto a camada base quanto a camada de árvores.
2. A classe `TileMap` agora inclui métodos `set_tile` e `get_tile`, tornando mais fácil manipular os dados do mapa.
3. ==O método `draw` da classe `TileMap` agora inclui parâmetros para a posição da câmera, permitindo a implementação futura de mapas maiores que a tela.==
4. A lógica de criação do mapa foi movida para o método `create_map` na classe `Game`, que agora usa os métodos da classe `TileMap`.
5. A renderização do mapa é feita chamando `tile_map.draw()` no loop principal do jogo.

Esta implementação oferece várias vantagens:
- Melhor organização do código, separando claramente a lógica do mapa da lógica do jogo.
- Maior flexibilidade para adicionar novas funcionalidades, como mapas maiores que a tela visível.
- Facilidade para implementar funcionalidades adicionais, como salvar/carregar mapas ou edição de mapas em tempo real.

Com esta estrutura, você pode facilmente expandir o jogo para incluir mapas maiores, movimentação de câmera, e até mesmo um editor de mapas. A classe `TileMap` fornece uma base sólida para o desenvolvimento futuro do seu jogo baseado em tiles.
### Técnicas Avançadas
1. **Autotiling**: Técnica que automaticamente escolhe o tile correto baseado nos tiles adjacentes.
2. **Layers Múltiplas**: Usar várias camadas para criar profundidade (chão, objetos, topo).
3. **Mapeamento Procedural**: Gerar mapas aleatoriamente usando algoritmos.
4. **Pathfinding**: Implementar algoritmos como A* para navegação de personagens.

### Ferramentas Úteis
1. **Tiled**: Editor de mapas popular e gratuito.
2. **PyTMX**: Biblioteca Python para carregar mapas criados no Tiled.
3. **Aseprite**: Excelente para criar tilesets em pixel art.

### Conclusão
A criação de mapas 2D é uma habilidade essencial no desenvolvimento de jogos. Combina aspectos técnicos de programação com criatividade artística. À medida que você pratica, experimentará com layouts mais complexos, estilos visuais variados e técnicas avançadas de design de níveis.

**Recursos Adicionais para Aprofundamento**
1. Livro: "Foundations of Game Engine Development, Volume 1: Mathematics" por Eric Lengyel
2. Curso online: "2D Game Development with libGDX" na Udacity
3. Tutorial: "Creating a Tile Map Editor" no site Game Development Envato Tuts+
4. Artigo: "The Guide to Implementing 2D Platformers" no Higher-Order Fun blog
5. Vídeo: "Make a Tile Map Editor with Python and Pygame" no canal Clear Code no YouTube

Estes recursos oferecem perspectivas diferentes e aprofundadas sobre o tema, desde conceitos teóricos até implementações práticas. Lembre-se de que a prática constante é fundamental para dominar essas técnicas. Experimente criar seus próprios mapas, tilesets e até mesmo um editor de mapas simples para solidificar seu aprendizado.
## 1.3 Introdução a ferramentas como **Tiled** para criação de mapas e como importá-los no Pygame
Tiled é classificado como um "editor de mapas de tiles" ou "level editor". É uma ferramenta de design de níveis especializada, focada na criação de mapas baseados em tiles para jogos 2D. Embora seja principalmente usado para jogos, também pode ser utilizado para outros tipos de projetos que requerem layouts baseados em grade, como planos de casas ou mapas de dungeons para RPGs de mesa.

***Uso no Desenvolvimento de Jogos***
No contexto do desenvolvimento de jogos, Tiled serve como uma ponte entre o design visual e a implementação técnica. Designers podem criar mapas visualmente atraentes e funcionais sem necessariamente entender o código subjacente, enquanto os programadores podem facilmente importar esses mapas para o motor do jogo. Tiled é amplamente compatível com várias engines de jogos e frameworks, incluindo Unity, Godot, Phaser, e pode ser usado com Pygame através de bibliotecas como PyTMX. Esta ferramenta é particularmente valiosa para equipes de desenvolvimento, pois permite que artistas e designers trabalhem nos layouts dos níveis independentemente dos programadores, melhorando assim o fluxo de trabalho e a eficiência da produção do jogo. Compreender o Tiled e sua integração com engines de jogos como Pygame é uma habilidade valiosa para qualquer desenvolvedor de jogos 2D, pois oferece um meio eficiente e flexível de criar mundos de jogo detalhados e envolventes.

 **Conceitos Principais do Tiled**
1. **Tilesets**: Coleções de tiles que podem ser usadas para criar mapas.
2. **Layers (Camadas)**: Permitem organizar diferentes elementos do mapa (chão, objetos, decorações).
3. **Objects (Objetos)**: Elementos não-tile que podem ser adicionados ao mapa (pontos de spawn, colisões).
4. **Properties (Propriedades)**: Informações adicionais que podem ser atribuídas a tiles, objetos ou camadas.
5. **Auto-tiling**: Recurso que automaticamente escolhe o tile correto baseado nos tiles adjacentes.

### Tiled vs. Criação Direta em Python/Pygame
**Criação Direta em Python/Pygame**
Vantagens:
1. Controle total sobre o processo de criação.
2. Integração direta com o código do jogo.
3. Não requer ferramentas externas.
4. Bom para projetos pequenos ou protótipos rápidos.
Desvantagens:
1. Pode ser tedioso para mapas grandes ou complexos.
2. Limitado às capacidades de desenho programático.
3. Difícil visualização em tempo real durante a criação.
4. Menos intuitivo para designers não programadores.

**Criação usando Tiled**
Vantagens:
1. Interface gráfica intuitiva para criação de mapas.
2. Suporte a camadas, objetos e propriedades personalizadas.
3. Facilita a colaboração entre programadores e designers.
4. Permite criar mapas complexos rapidamente.
5. Exporta para formatos padrão (como TMX) que podem ser importados em várias engines.
6. Oferece recursos avançados como auto-tiling e animações.
Desvantagens:
1. Requer aprendizado de uma ferramenta adicional.
2. Pode exigir código extra para importar os mapas no jogo.
3. Menos flexível para geração procedural de mapas em tempo real.

### Como Utilizar o [Tiled](https://www.mapeditor.org/)
Antes de iniciar com o Tiled, tenha em mente que você precisará criar os seus tiles e tisets em outra ferramenta para então poder importar no programa para a criação de mapas e mundos.

Algumas ferramentas fáceis e gratuitas para produzir tiles:
1. Piskel: Um editor de pixel art online e gratuito que roda diretamente no navegador. Permite criar animações, exportar PNG e GIF, e visualizar o resultado em tempo real.
2. Pixilart: Uma aplicação web gratuita com interface simples. Além de criar pixel art, você pode salvar suas criações online e compartilhá-las em redes sociais.
3. Lospec Pixel Editor: Um editor web simples, ideal para iniciantes. O site também oferece tutoriais e paletas de cores.
4. GIMP: Um software de edição de imagens gratuito e de código aberto, disponível para Windows, Mac e Linux. Embora não seja exclusivo para pixel art, possui as ferramentas necessárias para criar tiles.
5. Piq: Uma ferramenta online com interface simples, mas que oferece opções avançadas como modo isométrico e ferramenta de dithering.

**Criando mapas**
1. **Criação de um novo projeto**
2. **Criação de um Novo Mapa**:
    - Abra o Tiled e selecione "File" > "New" > "New Map".
    - Escolha o tipo de orientação (geralmente "Orthogonal" para jogos 2D).
    - Defina o tamanho do mapa e dos tiles.
3. **Importação de Tilesets**:
    - Vá em "Map" > "New Tileset".
    - Escolha uma imagem de tileset ou crie um novo.
    - Defina o tamanho dos tiles e o espaçamento.
4. **Criação de Camadas**:
    - Use o painel de camadas para adicionar novas camadas (tile layers, object layers).
    - Organize as camadas conforme necessário (ex: fundo, decorações, colisões).
5. **Desenhando o Mapa**:
    - Selecione tiles do tileset e pinte-os no mapa.
    - Use ferramentas como preenchimento, seleção retangular para trabalhar mais rápido.
6. **Adicionando Objetos**:
    - Use camadas de objetos para adicionar elementos como pontos de spawn, áreas de trigger.
7. **Exportação**:
    - Salve o mapa no formato TMX.
    - Exporte para outros formatos se necessário (JSON, CSV).

### Importando Mapas do Tiled no Pygame
Para importar mapas do Tiled no Pygame, você pode usar a biblioteca `pytmx`. Aqui está um exemplo básico:

```python
import pygame 
import pytmx 

def load_pygame(filename): 
	tmx_data = pytmx.load_pygame(filename) 
	return tmx_data 
	
def render_map(surface, tmx_data): 
	for layer in tmx_data.visible_layers: 
		if isinstance(layer, pytmx.TiledTileLayer): 
			for x, y, gid in layer: 
				tile = tmx_data.get_tile_image_by_gid(gid) 
				if tile: 
					surface.blit(tile, 
							(x * tmx_data.tilewidth, y * tmx_data.tileheight)) 

# No seu loop principal: 
tmx_data = load_pygame("seu_mapa.tmx") 
render_map(screen, tmx_data)
```

Colocando na lógica de mapas baseados em grade:
```python
import pygame
import pytmx
import sys
  
class TileMap:
    def __init__(self, filename):
        self.tmx_data = pytmx.load_pygame(filename)
        self.width = self.tmx_data.width * self.tmx_data.tilewidth
        self.height = self.tmx_data.height * self.tmx_data.tileheight
  
    def draw(self, surface):
        for layer in self.tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.tmx_data.get_tile_image_by_gid(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmx_data.tilewidth, y * self.tmx_data.tileheight))
  
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Mapa Tiled em Pygame")
        self.clock = pygame.time.Clock()
        self.tile_map = TileMap("assets/first_tiled_map.tmx")

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill((0, 0, 0))
            self.tile_map.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)
  
        pygame.quit()
        sys.exit()
  
if __name__ == "__main__":
    game = Game()
    game.run()
```

### Recursos Adicionais
1. [Documentação oficial do Tiled](https://doc.mapeditor.org/en/stable/)
2. [Getting started](https://doc.mapeditor.org/en/stable/manual/introduction/#getting-started)
3. Tutorial em vídeo: "Introduction to Tiled Map Editor" no YouTube
4. Artigo: "Using Tiled Map Editor with Pygame" no site Real Python
5. [Documentação do PyTMX](https://pytmx.readthedocs.io/en/latest/)
6. Curso Udemy: "2D Game Development with Tiled and Pygame"

Lembre-se de que, embora o Tiled ofereça muitas vantagens para a criação de mapas complexos, a escolha entre usar Tiled ou criar mapas diretamente no Pygame depende das necessidades específicas do seu projeto. Para jogos menores ou protótipos, a criação direta pode ser mais rápida, enquanto para projetos maiores ou com equipes de design, o Tiled pode oferecer um fluxo de trabalho mais eficiente e colaborativo.
# 2. Prática
## 2.1 Criar um cenário básico de cidade em pixel art
## 2.2 Implementar mapas e movimentação do jogador pelo cenário
## 2.3 Colocar barreiras e objetos para dar uma sensação de espaço e profundidade

# 3. Projeto
**Exploração Urbana**: Um cenário simples de cidade com interações mínimas. O jogador explora a área e aprende a navegar em um ambiente maior.