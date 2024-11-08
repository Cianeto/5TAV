# 5TAV (Disciplina de ADS (FAETERJ-RIO)) <!-- omit in toc -->

- [Jogo da Velha Inteligente](#jogo-da-velha-inteligente)
  - [Análise de Desempenho dos Jogadores Aleatório e Campeão](#análise-de-desempenho-dos-jogadores-aleatório-e-campeão)
  - [Análise de Desempenho do Jogador Inteligente](#análise-de-desempenho-do-jogador-inteligente)

## Jogo da Velha Inteligente

- Todos os testes foram feitos com 100.000 amostras.

### Análise de Desempenho dos Jogadores Aleatório e Campeão

- **Aleatório x Aleatório**:
  - Vitórias Aleatório 1: 58.69%
  - Vitórias Aleatório 2: 28.77%
  - Empates: 12.53%

- **Aleatório x Campeão**:
  - Vitórias Aleatório: 0%
  - Vitórias Campeão: 86.36%
  - Empates: 13.64%

- **Campeão x Aleatório**:
  - Vitórias Campeão: 97.79%
  - Vitórias Aleatório: 0%
  - Empates: 2.21%

- **Campeão x Campeão**:
  - Vitórias Campeão 1: 0%
  - Vitórias Campeão 2: 0%
  - Empates: 100%

### Análise de Desempenho do Jogador Inteligente

- **Inteligente x Aleatório**:
  - Vitórias Inteligente: 85.67%
  - Vitórias Aleatório: 0.42%
  - Empates: 13.91%

  ![Gráfico Inteligente x Aleatório](TicTacToe/img/int-aleat-graph.png)

- **Aleatório x Inteligente**:
  - Vitórias Aleatório: 3.58%
  - Vitórias Inteligente: 70.61%
  - Empates: 25.81%

  ![Gráfico Aleatório x Inteligente](TicTacToe/img/aleat-int-graph.png)

- **Inteligente x Campeão**:
  - Vitórias Inteligente: 0%
  - Vitórias Campeão: 0%
  - Empates: 100%

- **Campeão x Inteligente**:
  - Vitórias Campeão: 0.02%
  - Vitórias Inteligente: 0%
  - Empates: 99.98%

- **Inteligente x Inteligente**:
  - Vitórias Inteligente 1: 0.01%
  - Vitórias Inteligente 2: 0%
  - Empates: 99.99%

  ![Gráfico ~100% Empates](TicTacToe/img/just-draws-graph.png)
