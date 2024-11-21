[&larr; voltar para início](../README.md)

# 1. Teoria
## 1.1. Conceitos básicos de jogos 2D e mecânicas de jogo

### Introdução aos jogos 2D
Os jogos 2D são caracterizados por sua representação visual em duas dimensões, geralmente exibidos em um plano X-Y. Esses jogos têm uma longa história na indústria de videogames e continuam sendo populares devido à sua simplicidade, charme nostálgico e potencial para gameplay inovador [[Fábrica de jogos](https://www.fabricadejogos.net/posts/mecanica-de-jogos-parte-1/), [iMasters](https://imasters.com.br/desenvolvimento/conhecendo-mecanica-de-jogos-parte-01)].

**Características principais dos jogos 2D:**
- Gráficos baseados em sprites ou vetores
- Movimento limitado a um plano bidimensional
- Perspectiva fixa (geralmente vista lateral ou top-down)
- Foco em gameplay e mecânicas simples, mas envolventes

**Tipos comuns de jogos 2D**
1. **Plataforma:** Jogos focados em pular entre plataformas e superar obstáculos.
    - Exemplo: Super Mario Bros., Celeste
2. **Puzzle:** Desafios baseados em lógica e resolução de problemas.
    - Exemplo: Tetris, Baba Is You
3. **Ação/Aventura:** Combinam exploração com combate e resolução de quebra-cabeças.
    - Exemplo: The Legend of Zelda (jogos 2D), Hollow Knight
4. **Shoot 'em up:** Jogos de tiro com foco em reflexos rápidos e esquiva.
    - Exemplo: Space Invaders, Gradius
5. **RPG:** Jogos com foco em narrativa, desenvolvimento de personagens e combate por turnos.
    - Exemplo: Pokémon (jogos 2D), Stardew Valley

**Elementos de design em jogos 2D**
1. **Tilesets:** Conjuntos de gráficos reutilizáveis para criar níveis e ambientes.
2. **Sprites:** Imagens ou animações 2D que representam personagens e objetos.
3. **Parallax scrolling:** Técnica que cria ilusão de profundidade movendo camadas de fundo em velocidades diferentes.
4. **HUD (Heads-Up Display):** Interface que mostra informações importantes como pontuação, vida, itens, etc.
5. **Câmera 2D:** Controle de como o jogo é visualizado, incluindo rolagem e zoom.

### Mecânicas fundamentais
As mecânicas de jogo são as regras e sistemas que formam a base da interação do jogador com o jogo. Em jogos 2D, algumas mecânicas fundamentais incluem:
1. **Movimento:** Controle do personagem ou objetos no espaço 2D.
	- Exemplo: Andar, correr, pular em plataformas
2. **Colisão:** Detecção e resposta quando objetos se tocam ou se sobrepõem.
    - Exemplo: Colidir com inimigos, coletar itens
3. **Física simplificada:** Simulação básica de gravidade, aceleração e atrito.
    - Exemplo: Queda de objetos, deslizamento em superfícies
4. **Pontuação e progressão:** Sistemas para medir o desempenho e avanço do jogador.
    - Exemplo: Coletar moedas, desbloquear níveis
5. **Condições de vitória/derrota:** Objetivos claros e estados finais do jogo.
    - Exemplo: Chegar ao fim do nível, perder todas as vidas

### Considerações de gameplay
1. **Controles responsivos:** Garantir que as ações do jogador sejam imediatas e precisas.
2. **Curva de dificuldade:** Balancear o desafio para manter o jogador engajado sem frustrá-lo.
3. **Feedback visual e sonoro:** Fornecer respostas claras às ações do jogador para melhorar a experiência.
4. **Level design:** Criar níveis que introduzam e explorem as mecânicas de forma gradual e interessante.
5. **Replayability:** Incorporar elementos que incentivem múltiplas jogadas, como segredos ou múltiplos caminhos.

### Conclusão
Entender esses conceitos básicos de jogos 2D e mecânicas de jogo é essencial para começar a desenvolver jogos. À medida que avançamos no curso, exploraremos como implementar essas ideias usando Python e Pygame, transformando conceitos em código funcional.

**Para aprofundamento, recomendo os seguintes recursos:**
- [ ] [# Artigo: Mecânica de Jogos – Parte 1](https://www.fabricadejogos.net/posts/mecanica-de-jogos-parte-1/)
- [ ] [# Conhecendo a mecânica de jogos – Parte 01](https://imasters.com.br/desenvolvimento/conhecendo-mecanica-de-jogos-parte-01)
- [ ] [Livro: "The Art of Game Design: A Book of Lenses" por Jesse Schell](https://edifes.ifes.edu.br/images/stories/ebook_jogos_digitais.pdf)
- [ ] [Vídeo: "2D Game Development in Python" por Clear Code no YouTube](https://www.youtube.com/watch?v=BNr96v9JJ08&t=1s) 
- [ ] [Artigo: "Principles of 2D Game Design" no Game Developer](https://awari.com.br/desenvolvimento-de-jogos-2d-o-que-e-e-qual-sua-importancia/)

Estes materiais fornecerão uma base sólida para entender melhor o design e desenvolvimento de jogos 2D.

## 1.2. Estrutura de um loop de jogo e como programá-lo em Python

Um loop de jogo, também conhecido como game loop, é o coração de qualquer jogo. É uma estrutura de programação que executa continuamente, atualizando o estado do jogo e renderizando gráficos a cada iteração. O loop de jogo é responsável por manter o jogo rodando, processar entradas do usuário, atualizar a lógica do jogo e renderizar os gráficos na tela.

**Principais componentes**
1. **Processamento de entrada:** Captura e processa as ações do jogador (teclado, mouse, etc.).
2. **Atualização do estado do jogo:** Atualiza a lógica do jogo, como posições de objetos, colisões, etc.
3. **Renderização:** Desenha o estado atual do jogo na tela.

### Estrutura básica de um loop de jogo em Python
Aqui está uma estrutura básica de um loop de jogo em Python:
- **inicialização**
- **loop principal**
	- **processamento de eventos**: captura e processa todos os eventos do Pygame, incluindo entradas do usuário.
	- **atualização do estado do jogo**: atualiza a lógica do jogo, como movimento de objetos, física, IA, etc.
	- **renderização**: desenha todos os elementos visuais do jogo na tela.
	- **controle de FPS**: controla a velocidade do jogo para manter uma taxa de quadros consistente.
- encerramento

```python
import pygame pygame.init() 

# Configurações iniciais 
screen = pygame.display.set_mode((800, 600)) 
clock = pygame.time.Clock() 
running = True 
while running: 
	# Processamento de eventos 
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			running = False 
			
	# Atualização do estado do jogo 
	# (Aqui você colocaria a lógica do seu jogo) 
	
	# Renderização 
	screen.fill((0, 0, 0)) # Preenche a tela com preto 
	# (Aqui você desenharia os elementos do seu jogo) 
	pygame.display.flip() # Atualiza a tela 
	
	# Controle de FPS 
	clock.tick(60) # Limita o jogo a 60 FPS 

pygame.quit()
```
#### Inicialização
Antes do loop principal, inicializamos o Pygame e configuramos a janela do jogo:
```python
pygame.init() screen = pygame.display.set_mode((800, 600)) clock = pygame.time.Clock()
```

#### Processamento de entrada
Dentro do loop, processamos os eventos do Pygame:
```python
for event in pygame.event.get():
	if event.type == pygame.QUIT:
		running = False
```

Este bloco verifica se o usuário fechou a janela do jogo. ==Em um jogo real, você adicionaria mais verificações de eventos aqui para lidar com entradas do teclado, mouse, etc.==

#### Atualização do estado do jogo
Esta é a parte onde você implementaria a lógica do seu jogo:
```python
# Exemplo de atualização de posição de um personagem 
player_x += player_speed 
if player_x > screen_width:
	player_x = 0
```

#### Renderização
Aqui, desenhamos o estado atual do jogo na tela:
```python
screen.fill((0, 0, 0))  # Limpa a tela 
# Desenhe seus elementos de jogo aqui 
pygame.display.flip()  # Atualiza a tela
```

#### Controle de FPS
O controle de FPS (==Frames Per Second==) é importante para manter a velocidade do jogo consistente:

```python
clock.tick(60)  # Limita o jogo a 60 FPS
```

##### Considerações importantes
1. **Delta time:** Para jogos mais complexos, é importante usar o conceito de "delta time" para garantir que o jogo rode na mesma velocidade em diferentes máquinas.
2. **Fixed timestep:** Em alguns casos, pode ser benéfico usar um loop de jogo com timestep fixo para simulações mais precisas.
3. ==**Separação de preocupações:** À medida que seu jogo cresce, é uma boa prática separar a lógica de atualização e renderização em funções ou classes diferentes.==
4. **Otimização:** Para jogos mais complexos, você pode precisar otimizar seu loop de jogo para melhor performance.

#### Outros elementos mais avançados
**Gerenciamento de Estado do Jogo**
Gerencia diferentes estados do jogo (menu principal, jogando, pausado, etc.).
```python
if game_over:     
	show_game_over_screen() 
elif paused:
	show_pause_menu()
```

**Atualização de Elementos da Interface do Usuário**
Atualiza elementos da UI como pontuação, barra de vida, etc
```python
update_score_display() 
update_health_bar()
```

 **Gerenciamento de Áudio:**
 Controla a música de fundo e efeitos sonoros.
```python
update_background_music() 
play_sound_effects()
```

**Cálculos de Tempo Delta:**
Usado para fazer atualizações independentes da taxa de quadros.
```python
delta_time = clock.get_time() / 1000.0  # Tempo desde o último frame em segundos
```
### Exemplo prático: Movendo um retângulo
Vamos ver um exemplo simples de um loop de jogo que move um retângulo pela tela:
```python
import pygame 

pygame.init() 

# Configurações 
WIDTH, HEIGHT = 800, 600 
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
clock = pygame.time.Clock() 

# Propriedades do retângulo 
rect_x, rect_y = 400, 300 
rect_speed = 5 

running = True 
while running: 
	# Processamento de entrada 
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			running = False 
	
	# Atualização 
	keys = pygame.key.get_pressed() 
	if keys[pygame.K_LEFT]: 
		rect_x -= rect_speed 
	if keys[pygame.K_RIGHT]: 
		rect_x += rect_speed 
	if keys[pygame.K_UP]: 
		rect_y -= rect_speed 
	if keys[pygame.K_DOWN]: 
		rect_y += rect_speed 
	
	# Renderização 
	screen.fill((0, 0, 0))  # preenche a tela de preto
	pygame.draw.rect(screen, (255, 0, 0), (rect_x, rect_y, 50, 50)) 
	pygame.display.flip() 
	
	clock.tick(60) 

pygame.quit()
```
Este exemplo demonstra um loop de jogo básico que permite mover um retângulo vermelho usando as teclas de seta. Arquivo disponível em [g01_rectangle.py](scripts/g01_rectangle.py)

Alguns pontos: 
- `screen.fill((0, 0, 0))`: preenche toda a tela com a cor preta. O método `fill()` aceita uma tupla RGB (Red, Green, Blue). Neste caso, (0, 0, 0) representa preto. Isso essencialmente limpa a tela, removendo qualquer coisa desenhada no frame anterior.
- `pygame.draw.rect(screen, (255, 0, 0), (rect_x, rect_y, 50, 50))`: desenha um retângulo vermelho na tela. Vamos decompor os argumentos:
	- `screen`: é a superfície onde o retângulo será desenhado.
	- `(255, 0, 0)`: é a cor do retângulo em RGB. (255, 0, 0) representa vermelho puro.
	- `(rect_x, rect_y, 50, 50)`: é uma tupla que define a posição e o tamanho do retângulo:
	    - `rect_x` e `rect_y` são as coordenadas do canto superior esquerdo do retângulo.
	    - `50, 50` são a largura e altura do retângulo em pixels.
- `pygame.display.flip()`: atualiza toda a tela. Depois de desenhar todos os elementos, usamos `flip()` para "virar" o display, mostrando tudo o que foi desenhado desde o último `flip()`. ==Isso é crucial para evitar flickering e garantir que todas as mudanças sejam exibidas simultaneamente.==
- Essas três linhas trabalham juntas para criar a ilusão de movimento:
	1. Limpar a tela (removendo o retângulo do frame anterior)
	2. Desenhar o retângulo em sua nova posição
	3. Atualizar a tela para mostrar as mudanças
- Este processo, repetido muitas vezes por segundo, cria a animação suave do retângulo se movendo pela tela.

### Conclusão
Entender e implementar corretamente o loop de jogo é crucial para o desenvolvimento de jogos. À medida que você avança no desenvolvimento, você irá expandir e refinar esta estrutura básica para acomodar mecânicas de jogo mais complexas.

Para aprofundamento, recomendo os seguintes recursos:
- [ ] Livro: "Game Programming Patterns" por Robert Nystrom (especialmente o capítulo sobre Game Loop)
- [ ] Vídeo: "Pygame Tutorial - Creating a Game Loop" por Tech With Tim no YouTube
- [ ] Artigo: "Fix Your Timestep!" por Glenn Fiedler (para uma discussão avançada sobre loops de jogo)
Estes recursos fornecerão uma compreensão mais profunda dos loops de jogo e como implementá-los eficientemente em diferentes cenários.
## 1.3. Introdução à biblioteca **Pygame** para controle de gráficos e eventos

### O que é Pygame?
Pygame é uma biblioteca de código aberto para Python, especialmente projetada para o desenvolvimento de jogos e aplicações multimídia. Construída sobre a biblioteca SDL (Simple DirectMedia Layer), Pygame oferece uma interface Python amigável para muitas das funcionalidades do SDL, facilitando a criação de jogos 2D.

**Principais características do Pygame:**
1. **Multiplataforma:** Funciona em Windows, macOS, Linux e outras plataformas.
2. **Gráficos 2D:** Oferece ferramentas robustas para desenhar formas, imagens e animações.
3. **Controle de eventos:** Gerencia entradas de teclado, mouse e outros dispositivos de forma eficiente.
4. **Som:** Suporta reprodução e mixagem de áudio para efeitos sonoros e música.
5. **Colisão:** Fornece funções para detecção de colisões entre objetos.
6. **Sprites:** Facilita o trabalho com sprites, elementos gráficos fundamentais em jogos 2D.

**Instalação do Pygame**
Para instalar o Pygame, use o seguinte comando no terminal ou prompt de comando (preferencialmente em um ambiente virtual dedicado para o projeto):

```CMD
pip install pygame
```

**Estrutura básica de um programa Pygame**
Já vimos anteriormente a estrutura básica do jogo. Basicamente consiste em configurar a tela, e dentro do loop de jogo definir a lógica e atualizar os frames:

```python
	import pygame 
	
	pygame.init() 
	
	# Configuração da tela 
	screen = pygame.display.set_mode((800, 600)) 
	pygame.display.set_caption("Meu Primeiro Jogo Pygame") 
	# Loop principal do jogo 
	running = True 
	while running:     
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False     
		# Lógica do jogo aqui   
		  
		# Renderização    
		screen.fill((0, 0, 0))  # Preenche a tela com preto    
		
		pygame.display.flip() 
	pygame.quit()
```

### Controle de Gráficos

Pygame oferece diversas formas de desenhar e manipular gráficos na tela:

1. **Desenho de formas básicas:** [g02_formas_basicas.py](modulos/scripts/g02_formas_basicas.py)
```python
# Desenha um retângulo vermelho
# (screen, cor, posicao(cantosuperioresquerdo)/tamanho)
# == (scren, (reg,green,blue), (x,y,largura,altura))
pygame.draw.rect(screen, (255,0,0), (50,50,100,100))

# desenha um círculo verde
# (screen, cor, posicao(centro),raio) == (screen, (R,G,B), (x,y), raio)
pygame.draw.circle(screen, (0,255,0), (200,200), 50)

# desenha uma linha
# (screen, cor, posicao inicial, posicao final, espessura)
# (screen, (R,G,B), (x0,y0),(xf,yf), espessura)
pygame.draw.line(screen, (0,0,255), (300,300),(500,400), 5)
```
	
2. **Carregamento e exibição de imagens:** [g03_carregamento_imagens.py](modulos/scripts/g03_carregamento_imagens.py)
```python
# carrega a imagem
image = pygame.image.load('images/teste_mario.png')
# transforma a imagem
# (image, novo tamanho em pixel) == (image, (largura,altura))
image = pygame.transform.scale(image, (100, 100))

# mostra na tela
# (image, posicao) == (image, (x,y))
screen.blit(image,(200,500))
```

Para transformação de imagens mantendo a proporção original:
```python
# Obtém as dimensões originais da imagem 
original_width, original_height = original_image.get_size() 
# Calcula o fator de escala (por exemplo, reduzir pela metade) 
scale_factor = 0.5 
# Redimensiona a imagem mantendo a proporção 
new_width = int(original_width * scale_factor) 
new_height = int(original_height * scale_factor) 
image = pygame.transform.smoothscale(original_image, (new_width, new_height)) 
# Desenha a imagem redimensionada na tela 
screen.blit(image, (300, 300))
```

3. **Renderização de texto:** [g04_renderizando_texto.py](modulos/scripts/g04_renderizando_texto.py)
```python
	# definindo a fonte (nome da fonte, tamanho)
	# (path da fonte, tamanho)
	font = pygame.font.Font(None,36)
	
	# renderizando a fonte
	# (texto, anti-aliasing, cor)
	text = font.render("Olá, novo dev!", True, (255,255,255))
	
	# desenha/blita o texto renderizado na tela
	# (texto, posicao)
	screen.blit(text, (400,400))
```

- O parâmetro `True` ativa o anti-aliasing, que suaviza as bordas do texto.
- É possível colocar fontes personalizadas e informar o caminho relativo

Exemplo de uso com sombra:
```python
import pygame pygame.init() 
screen = pygame.display.set_mode((800, 600)) 
# Carregando uma fonte específica (se disponível no sistema) 
try: 
	font = pygame.font.Font("Arial.ttf", 36) 
except: 
	font = pygame.font.Font(None, 36) # Usa a fonte padrão se Arial não estiver disponível 

# Renderizando texto com sombra 
shadow_color = (100, 100, 100) # Cor cinza para a sombra 
text_color = (255, 255, 0) # Cor amarela para o texto 
shadow = font.render("Hello, Pygame!", True, shadow_color) 
text = font.render("Hello, Pygame!", True, text_color) 

# Desenhando o texto com sombra 
screen.blit(shadow, (402, 402)) # Sombra ligeiramente deslocada 
screen.blit(text, (400, 400)) # Texto principal 

pygame.display.flip() 

# Mantém a janela aberta 
running = True 
while running: 
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			running = False 
			
pygame.quit()
```
### Controle de Eventos
Pygame captura eventos do sistema e os disponibiliza para o seu programa. Estrutura básica do ==loop de processamento de eventos==:
```python
for event in pygame.event.get(): 
	if event.type == pygame.QUIT: 
		running = False
```

Este loop é fundamental para lidar com eventos em um jogo Pygame. Vamos analisar cada parte:
1. `pygame.event.get()`:
    - Esta função retorna uma lista de todos os eventos Pygame que ocorreram desde a última vez que foi chamada.
    - Eventos incluem ações do usuário (como cliques do mouse, pressionamentos de teclas) e eventos do sistema (como o fechamento da janela).
2. `for event in ...`:
    - Este loop itera sobre cada evento na lista retornada por `pygame.event.get()`.
3. `if event.type == pygame.QUIT`:
    - Verifica se o evento atual é do tipo `pygame.QUIT`, que ocorre quando o usuário tenta fechar a janela do jogo.

**Importância**
- **Responsividade**: Permite que o jogo responda imediatamente às ações do usuário.
- **Controle de Fluxo**: Oferece um ponto centralizado para gerenciar todas as entradas do usuário e eventos do sistema.
- **Prevenção de Travamentos**: Ao processar todos os eventos, evita que o sistema operacional considere o programa como não responsivo.

#### Tipos de eventos
Esses eventos devem ser indicados no loop de processamento de eventos. 
1. **Eventos de teclado:** [g05_evento_teclado.py](modulos/scripts/g05_evento_teclado.py)
```python
# processamento de entrada
for event in pygame.event.get():
	if event.type == pygame.QUIT:
		running = False
	# eventos de teclado
	elif event.type == pygame.KEYDOWN:
		if event.key == pygame.K_SPACE:
			# ação quando espaço é pressionado
			tecla = 'espaço'
		elif event.key == pygame.K_LEFT:
			# ação quando seta para esquerda é pressionada
			tecla = 'para esquerda'
```
Neste caso, os eventos poderiam ser visualizados como texto, por exemplo:
```python
# Renderização
    screen.fill((0,0,0)) # preenche a tela com preto
    font = pygame.font.Font(None,36)
    try:
        text = font.render(f"Você pressionou: {tecla}", False, (255,255,255))
    except:
        text = font.render("Você pressionou: nada", False, (255,255,255))

    screen.blit(text, (400,400))
    pygame.display.flip()
```

2. **Eventos de mouse:** [g06_evento_mouse.py](modulos/scripts/g06_evento_mouse.py)
```python
for event in pygame.event.get():
	if event.type == pygame.QUIT:
		running = False
	elif event.type == pygame.MOUSEBUTTONDOWN:
		if event.button == 1: # botão esquerdo do mouse
			# ação quando botão esquerdo é pressionado
			tecla = 'botão esquerdo'
		elif event.button == 3: # botão direito
			# ação quando botão direito é pressionado
			tecla = 'botão direito'
```
Os eventos podem ser visualizados da mesma maneira do exemplo anterior

3. **Evento de fechamento da janela:**
Este trecho de código é crucial para o funcionamento adequado de qualquer aplicação Pygame, pois ele lida com o evento de fechamento da janela do jogo.
```python
if event.type == pygame.QUIT:     
	running = False
```
- É possível adicionar lógica adicional antes de definir `running = False`, como salvar o progresso do jogo, exibir uma mensagem de confirmação, etc.

4. Evento de Joystick/Gamepad
	```python
	if event.type == pygame.JOYBUTTONDOWN: 
		# Ação quando um botão do joystick é pressionado
	```
1. Eventos Personalizados
	```python
	if event.type == pygame.USEREVENT: 
		# Lidar com eventos personalizados
	```

#### Considerações Importantes
1. **Ordem de Processamento**: A ordem em que você verifica os eventos pode ser importante, especialmente para eventos que podem ocorrer simultaneamente.
2. **Eficiência**: Processar eventos é geralmente rápido, mas em jogos com muitos eventos, pode ser necessário otimizar este loop.
3. ==**Estado do Teclado**: Para ações contínuas (como movimento), às vezes é melhor usar `pygame.key.get_pressed()` fora deste loop.==
4. **Eventos Personalizados**: Você pode criar e disparar seus próprios eventos usando `pygame.event.post()`.
5. **Limpeza de Eventos**: Em alguns casos, pode ser útil limpar a fila de eventos com `pygame.event.clear()` para evitar atrasos.

Em resumo, o loop de processamento de eventos é crucial para criar jogos interativos e responsivos em Pygame. Ele permite que você capture e responda a uma ampla gama de entradas do usuário e eventos do sistema, formando a base para a interatividade do seu jogo.
### Exemplo prático: Jogo simples de clique

Vamos criar um exemplo simples que demonstra o controle de gráficos e eventos:

```python
import pygame
import random

pygame.init()

# Configuração da tela
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jogo de Clique")

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

# Loop principal
running = True
clock = pygame.time.Clock()
while running:
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
            else:
                score -= 1
                target_pos = [random.randint(0, width), random.randint(0, height)]

    # Renderização
    screen.fill(BLACK)
    pygame.draw.circle(screen, RED, target_pos, target_radius)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

Este exemplo cria um jogo simples onde o jogador deve clicar em círculos vermelhos que aparecem aleatoriamente na tela. Cada clique bem-sucedido aumenta a pontuação.

#### Temporizado
Para modificar o jogo de clique de modo que o círculo permaneça por um tempo determinado (por exemplo, 1 segundo) e depois desapareça, precisamos introduzir um sistema de temporização. Se o usuário não clicar no círculo dentro desse tempo ou clicar fora dele, ele perderá um ponto. Aqui está uma versão modificada:

```python
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
target_duration = 1500  # 1000 milissegundos = 1 segundo
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
```


### Conclusão

Pygame oferece uma ampla gama de funcionalidades para criar jogos e aplicações multimídia em Python. Esta introdução cobre os conceitos básicos de gráficos e eventos, fornecendo uma base sólida para começar a desenvolver jogos simples.

Para aprofundamento, recomendo:
- A documentação oficial do Pygame: [https://www.pygame.org/docs/](https://www.pygame.org/docs/)
- O livro "Python Crash Course" por Eric Matthes (que inclui um projeto de jogo usando Pygame)
- Tutoriais em vídeo no canal "Clear Code" no YouTube, que oferece excelentes tutoriais de Pygame

Estes recursos ajudarão a explorar recursos mais avançados do Pygame, como animações complexas, física de jogos, som e muito mais. À medida que você avança, poderá criar jogos cada vez mais sofisticados e interativos.

# 2. Prática
## 2.1 Implementar uma tela de jogo (com score, tempo, vida) e um player. 
Uma boa prática da programação orientada a objetos é a criação desses objetos (classes, no python). Assim, iniciaremos a construção e desenvolvimento com a construção de classes.

Neste exemplo simples, teremos o arquivo principal (main.py), que irá chamar rodar uma classe Game (que conterá a lógica do jogo). Ainda, a classe Game utilizará um outra classe, Player, para renderizar o player na tela.

[main.py](game01.py):
```python
from src01.game import Game

if __name__ == "__main__":
    game = Game()
    game.run()
```

[game.py](src01/game.py):
```python
import pygame
from src01.player import Player

class Game:
    def __init__(self):  # configuração inicial
        pygame.init()
        pygame.display.set_caption("Game 01")
        self.screen = pygame.display.set_mode((960, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player()

    def run(self):
        while self.running:      # loop principal
            self.handle_events() # loop de tratamento de eventos
            self.draw()          # renderização
            pygame.display.flip()
            self.clock.tick(60)

    def handle_events(self):     # loop de tratamento de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
    def draw(self):                 # tela principal
        self.screen.fill((0, 0, 0)) # fundo preto
        pygame.draw.line(self.screen,(255,255,255),   # margens
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
        
        health_text = font.render(f"Health: {self.player.health}",
                                  False, (255,255,255))
        self.screen.blit(health_text,(800,15))
  
        # player
        self.player.draw(self.screen)
```

[player.py](src01/player):
```python
import pygame

class Player:
    def __init__(self):
        self.position = (400, 300)
        self.speed = 5
        self.health = 100
        self.radius = 20
  
    def draw(self, screen):
        # Desenhar o jogador
        pygame.draw.circle(screen, (255,0,0),self.position,self.radius)
```


## 2.2 Implementar um loop de jogo simples com movimentação de personagem
Agora, iremos implementar o movimento do player no jogo anterior. 

Alterando o [player.py](scr02/player.py):
- Adicionar o atributo `self.direction = [0, 0]  # Direção do movimento [x, y]`
- Criar os métodos `move` e `update`:
```python
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
```

E, alterar o [game.py](src02/game.py)
- Criar o método `update`:
```python
 def update(self):
        self.player.update()
```
- Alterar o `handle_events`:
```python
def handle_events(self):     # loop de tratamento de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        # Movimento contínuo baseado nas teclas pressionadas
        keys = pygame.key.get_pressed()
        self.player.direction[0] = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        self.player.direction[1] = keys[pygame.K_DOWN] - keys[pygame.K_UP]
```
- E, adicionar o `update` no `run`:
```python
def run(self):
        while self.running:      
            self.handle_events() 
            self.update() # atualiza a posição do player
            self.draw()        
            pygame.display.flip()
            self.clock.tick(60)
```
## 2.3. Detectar colisões básicas entre objetos
A detecção de colisões é fundamental para a interação entre objetos em um jogo. Existem diferentes métodos para detectar colisões, dependendo da forma dos objetos envolvidos. Vamos focar em dois tipos principais:
- Colisão entre retângulos
- Colisão entre círculos

### Colisão entre retângulos
Para detectar colisões entre retângulos, usaremos o método `colliderect()` do Pygame. Este método é eficiente e fácil de usar para objetos retangulares.
```python
# Criando retângulos 
rect1 = pygame.Rect(100, 100, 50, 50) 
rect2 = pygame.Rect(200, 200, 60, 60) 

# Verificando colisão 
if rect1.colliderect(rect2): 
	print("Colisão detectada!")
```

### Colisão entre círculos
Para círculos, implementaremos nossa própria função de detecção de colisão usando a distância entre os centros dos círculos.

```python
def check_circle_collision(circle1, circle2): 
	distance = math.sqrt((circle1.x - circle2.x)**2 + (circle1.y - circle2.y)**2)
	return distance <= (circle1.radius + circle2.radius) 
	
# Exemplo de uso 
class Circle: 
	def __init__(self, x, y, radius): 
		self.x = x 
		self.y = y 
		self.radius = radius 
		
circle1 = Circle(100, 100, 30) 
circle2 = Circle(150, 150, 40) 

if check_circle_collision(circle1, circle2): 
	print("Colisão entre círculos detectada!")
```

### Aplicando ao jogo
Neste momento, já iremos reorganizar nosso código. Alterações:
- Criação do arquivo [setings.py](src03/settings.py) com os parâmetros do jogo
- Criação da classe de inimigos (em posições aleatórias):
	```python
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
	```
- Chamar o RandomEneminies.draw() no método .draw() da classe Game(), no [game.py](src03/game.py)
- Adicionar uma função para verificar a colisão do player com "inimigos" na classe Player:
```python
def check_collision_enemy(self, enemy):
        # enemy == retângulo
        expanded_enemy = enemy.inflate(self.radius * 2, self.radius * 2)
        return expanded_enemy.collidepoint(self.x, self.y)
```
- Adicionar método para chegar se houve colisões na classe Game:
```python
def check_collisions(self):
        enemies = self.enemies.objects
        index = 0
        for enemy in enemies:
            if self.player.check_collision_enemy(enemy):
                del self.enemies.objects[index]
                self.enemies_collision = True
            index += 1
```
- Criar parâmetro e atualizar a colisão no método update também da classe Game:
```python
def update(self):
        self.player.update()
        if self.enemies_collision:
            self.enemies_collision = False
```

Jogo final: [main.py](game03.py), [player.py](src03/player.py), [game.py](src02/game.py)

# Projeto
**Jogo de Labirinto**: O jogador navega em um labirinto simples, coletando itens para escapar. Esse projeto ajudará a consolidar a base de movimento e colisão.