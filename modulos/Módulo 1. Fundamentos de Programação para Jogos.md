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
```python
import pygame pygame.init() 

# Configurações iniciais 
screen = pygame.display.set_mode((800, 600)) 
clock = pygame.time.Clock() 
running = True 
while running: 
	# Processamento de entrada 
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

# 2. Prática
## 2.1 Implementar um loop de jogo simples com movimentação de personagem

## 2.2. Detectar colisões básicas entre objetos

## 2.3. Trabalhar com coordenadas para movimento em um ambiente 2D


# Projeto
**Jogo de Labirinto**: O jogador navega em um labirinto simples, coletando itens para escapar. Esse projeto ajudará a consolidar a base de movimento e colisão.