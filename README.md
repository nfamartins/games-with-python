# games-with-python

---
### [Módulo 1. Fundamentos do desenvolvimento de jogos em python](modulos/Módulo%2001.%20Fundamentos%20do%20desenvolvimento%20de%20jogos%20em%20python.md)

1. **Teoria**
	1. Conceitos básicos de jogos 2D e mecânicas de jogo
	2. Estrutura de um loop de jogo e como programá-lo em Python
	3. Introdução à biblioteca **Pygame** para controle de gráficos e eventos
2. **Prática**
	1. Implementar um loop de jogo simples com movimentação de personagem
	2. Detectar colisões básicas entre objetos
	3. Trabalhar com coordenadas para movimento em um ambiente 2D
3. **Projeto**
	1. *Jogo de Labirinto*: o jogador navega em um labirinto simples, coletando itens para escapar. Esse projeto ajudará a consolidar a base de movimento e colisão.

---

### [Módulo 02. Construção de Cenários e Pixel Art](modulos\Módulo%2002.%20Construção%20de%20Cenários%20e%20Pixel%20Art.md)

1. Teoria
	1. Conceitos de pixel art e como aplicá-los em Python
	2. Mapas em 2D: criação de cenários, tilesets e mapas baseados em grade
	3. Introdução a ferramentas como **Tiled** para criação de mapas e como importá-los no Pygame
2. Prática
	1. Criar um cenário básico de cidade em pixel art
	2. Implementar mapas e movimentação do jogador pelo cenário
	3. Colocar barreiras e objetos para dar uma sensação de espaço e profundidade
3. Projeto
	1. **Exploração Urbana**: Um cenário simples de cidade com interações mínimas. O jogador explora a área e aprende a navegar em um ambiente maior.

---

### **Módulo 3: Interações com Personagens e Diálogos**

#### Teoria

- Sistemas de diálogo e como gerenciá-los em Python
- Estruturas de dados para armazenar diálogos e opções de escolhas (ex.: dicionários, JSON)
- Criação de personagens e narrativa com impacto nas escolhas do jogador

#### Prática

- Implementar interações com personagens usando menus de diálogo
- Criar diálogos que variam conforme as decisões anteriores do jogador
- Aprimorar o mapa da cidade para adicionar NPCs interativos

#### Projeto

**História com Escolhas**: Uma pequena aventura interativa onde o jogador conversa com diferentes personagens que dão pistas para resolver um mini-mistério.

---

### **Módulo 4: Inventário e Sistema de Itens**

#### Teoria

- Sistema de inventário: como criar, gerenciar e exibir itens coletados
- Programação de objetos interativos e coleta de itens em um jogo
- Variáveis e objetos persistentes (itens que afetam o jogo conforme coletados)

#### Prática

- Implementar um inventário básico e interface visual para exibir itens
- Criar itens colecionáveis que o jogador usa para resolver pequenos puzzles
- Expandir o cenário para incluir áreas bloqueadas que exigem itens específicos para desbloqueio

#### Projeto

**Aventura com Coleta de Itens**: O jogador explora um ambiente onde coleta itens e resolve pequenos desafios para avançar.

---

### **Módulo 5: Puzzles e Desafios Interativos**

#### Teoria

- Tipos de puzzles em jogos e técnicas para desenvolver lógica de quebra-cabeças
- Design de puzzles que integram a narrativa e aumentam em dificuldade
- Controle de estado e progresso do jogo baseado na resolução de puzzles

#### Prática

- Implementar diferentes tipos de puzzles que dependem do inventário ou interações com o cenário
- Criar mecanismos de aumento de dificuldade nos puzzles
- Testar lógica de combinação e resolução dos desafios

#### Projeto

**Exploração com Puzzles**: O jogador explora uma série de locais com puzzles que devem ser resolvidos para avançar e encontrar itens ou pistas adicionais.

---

### **Módulo 6: Efeitos Visuais e Simulação de Física**

#### Teoria

- Fundamentos de simulação de física (como gravidade e movimento realista) em jogos
- Efeitos visuais básicos em Pygame para melhorar a estética do jogo (como partículas e animações)
- Sons e efeitos sonoros para aumentar a imersão

#### Prática

- Implementar efeitos como gravidade e interação física leve com o cenário
- Criar animações simples para o movimento dos personagens e partículas
- Integrar sons e efeitos sonoros nos eventos importantes do jogo

#### Projeto

**Simulação e Puzzle com Física**: Um ambiente onde o jogador resolve desafios que envolvem lógica de física (como mover objetos pesados ou calcular trajetórias).

---

### **Módulo Final: Desenvolvimento do Projeto Final**

#### Teoria

- Integração de todos os módulos para criar um jogo completo e imersivo
- Elementos de narrativa ramificada e design de escolhas com impacto
- Técnicas de balanceamento de dificuldade e desenvolvimento de puzzles complexos
- Testes de usabilidade e refinamento do jogo

#### Prática

- Criar a narrativa completa com uma São Paulo futurista, usando pixel art detalhado para o ambiente urbano
- Implementar diálogos dinâmicos que respondem às escolhas do jogador
- Desenvolver puzzles complexos que exigem itens específicos e exploração de áreas para resolução
- Criar reviravoltas e eventos climáticos para aumentar o suspense

#### Projeto Final

**Jogo de Mistério Distópico: "São Paulo 2099"**: Neste jogo, o jogador assume o papel de um investigador que percorre os bairros distópicos de São Paulo, conversando com personagens e coletando pistas para resolver um grande mistério. A narrativa é cheia de reviravoltas, e as decisões do jogador influenciam o rumo da história, que explora temas de reflexão sobre sociedade, tecnologia e identidade. Esse projeto final integra mecânicas de exploração, coleta de itens, narrativa interativa e puzzles complexos, finalizando com um mistério resolvido que deixa uma mensagem para o jogador.