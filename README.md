# 5TAV (Disciplina de ADS (FAETERJ-RIO))

## Jogo da Velha

### StartScreen

Esta classe é responsável pela tela inicial do jogo, onde os jogadores podem selecionar suas opções e iniciar o jogo.

Métodos Principais:
draw_background(): Desenha o fundo da tela.
draw_title(): Desenha o título do jogo.
draw_play_button(): Desenha o botão de "Play".
draw_dropdowns(): Desenha os dropdowns para seleção de jogadores.
handle_dropdown_event(event): Lida com eventos de clique nos dropdowns.
run(): Executa o loop principal da tela inicial.

### BotPlayer

Esta classe representa o jogador bot, que pode ter diferentes níveis de dificuldade.

Métodos Principais:
move(): Decide o movimento do bot com base no tipo (Random ou Perfect).
random_move(): Realiza um movimento aleatório.
perfect_move(): Realiza o movimento perfeito usando o algoritmo Minimax.

### Algoritmo Minimax

O algoritmo Minimax é usado para determinar o movimento perfeito do bot. Ele é um algoritmo recursivo que simula todos os movimentos possíveis no jogo e escolhe o melhor movimento para o bot, assumindo que o oponente também joga de forma ótima.

#### Funcionamento do Minimax

Simulação de Movimentos: O algoritmo simula todos os movimentos possíveis para o bot e para o oponente.
Avaliação de Movimentos: Cada movimento é avaliado com base em uma função de pontuação.
Recursão: O algoritmo chama a si mesmo recursivamente para simular os movimentos subsequentes.
Escolha do Melhor Movimento: O movimento que maximiza a pontuação do bot (ou minimiza a pontuação do oponente) é escolhido.

### TicTacToe

A classe TicTacToe é a classe principal que gerencia o jogo da velha.

#### Inicialização da Classe (__init__)

self.board inicializa o tabuleiro como uma lista de 9 espaços vazios.
self.current_player define o jogador atual como 'X'.

#### Exibir o Tabuleiro (display_board)

O método imprime o tabuleiro em uma grade 3x3.

#### Fazer uma Jogada (make_move)

- Verifica se a posição está livre.
- Atualiza o tabuleiro com o símbolo do jogador atual.
- Verifica se há um vencedor ou empate.
- Alterna para o próximo jogador se o jogo continuar.

#### Verificar Vitória (check_winner)

- Verifica todas as combinações possíveis de vitória (linhas, colunas e diagonais).

#### Verificar Empate (check_draw)

- Verifica se todas as posições do tabuleiro estão preenchidas.

#### Reiniciar o Jogo (reset_game)

- Redefine o tabuleiro e o jogador atual para o estado inicial.

### Game

A classe Game é responsável por inicializar e gerenciar o loop principal do jogo Tic Tac Toe. Aqui está uma explicação detalhada dos componentes e métodos da classe:

#### Atributos

screen: A superfície onde todos os elementos do jogo são desenhados. É inicializada com uma dimensão definida por WIN_SIZE.
clock: Um objeto de relógio para controlar a taxa de atualização do jogo.
start_screen: Uma instância da classe StartScreen, que provavelmente gerencia a tela inicial do jogo.
tic_tac_toe: Uma instância da classe TicTacToe, que gerencia a lógica principal do jogo Tic Tac Toe.

#### Métodos

__init__: O método construtor que inicializa o Pygame, configura a tela do jogo, define o ícone e o título da janela, e cria instâncias das classes StartScreen e TicTacToe.
run: O método principal que contém o loop do jogo. Ele alterna entre a tela inicial e o jogo principal, atualizando a tela e controlando a taxa de quadros por segundo.

### Autor

Desenvolvido por Gabriel Melo Dias.
