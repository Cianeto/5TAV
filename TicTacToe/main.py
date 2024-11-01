from random import choice

WINCO = [  # Combinações vencedoras
    # Linhas
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    # Colunas
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    # Diagonais
    [1, 5, 9],
    [3, 5, 7],
]


class Player:
    def __init__(self, player_type, player_symbol, game):
        self.game = game
        self.board = self.game.board
        self.player_type = player_type
        self.player_symbol = player_symbol
        self.win_count = 0
        if self.player_type == 3:
            self.random_moves = []
            self.winning_moves = []
            self.database = []
            self.moves_used = []
            self.win_flag = 0
            self.draw_flag = 0

    def move(self):  # <~~ DEFINE QUAL ESTRATÉGIA ESSE PLAYER APLICARÁ
        play = {1: self.random_move, 2: self.perfect_move, 3: self.intelligent_move}
        play[self.player_type](self.player_symbol)
        # self.game.print_board()

    def random_move(self, p):  # <~~ ESTRATÉGIA DO PLAYER ALEATÓRIO
        self.board[0] += 1
        empty_positions = [i for i in range(1, 10) if self.board[i] == 0]
        if empty_positions:
            pos = choice(empty_positions)
            self.board[pos] = p
            self.board[10] = pos

    def block(self, p, opp):  # <~~ BLOQUEAR OPONENTE (SE O PRÓXIMO MOVE DELE CONCLUIR A PARTIDA)
        b = self.board
        for combo in WINCO:
            if b[combo[0]] == b[combo[1]] == opp and b[combo[2]] == 0:
                b[combo[2]] = p
                b[10] = combo[2]
                return True
            if b[combo[1]] == b[combo[2]] == opp and b[combo[0]] == 0:
                b[combo[0]] = p
                b[10] = combo[0]
                return True
            if b[combo[0]] == b[combo[2]] == opp and b[combo[1]] == 0:
                b[combo[1]] = p
                b[10] = combo[1]
                return True
        return False

    def two_steps_block(self, p, opp):  # <~~ BLOQUEAR OPONENTE (SE OS PRÓXIMOS DOIS MOVES DELE CONCLUIR A PARTIDA)
        b = self.board

        if b[0] == 4:
            if b[6] == b[7] == opp:
                if b[8] == 0:
                    b[8] = p
                    b[10] = 8
                    return True
            if b[6] == b[1] == opp:
                if b[2] == 0:
                    b[2] = p
                    b[10] = 2
                    return True

            if b[8] == b[1] == opp:
                if b[4] == 0:
                    b[4] = p
                    b[10] = 4
                    return True
            if b[8] == b[3] == opp:
                if b[6] == 0:
                    b[6] = p
                    b[10] = 6
                    return True

            if b[4] == b[3] == opp:
                if b[1] == 0:
                    b[1] = p
                    b[10] = 1
                    return True
            if b[4] == b[9] == opp:
                if b[7] == 0:
                    b[7] = p
                    b[10] = 7
                    return True

            if b[2] == b[7] == opp:
                if b[1] == 0:
                    b[1] = p
                    b[10] = 1
                    return True
            if b[2] == b[9] == opp:
                if b[3] == 0:
                    b[3] = p
                    b[10] = 3
                    return True

            if b[6] == b[8] == opp:
                if b[9] == 0:
                    b[9] = p
                    b[10] = 9
                    return True

            if b[4] == b[8] == opp:
                if b[7] == 0:
                    b[7] = p
                    b[10] = 7
                    return True

            if b[2] == b[4] == opp:
                if b[1] == 0:
                    b[1] = p
                    b[10] = 1
                    return True

            if b[2] == b[6] == opp:
                if b[3] == 0:
                    b[3] = p
                    b[10] = 3
                    return True

            if b[1] == b[9] == opp:
                if b[2] == 0:
                    b[2] = p
                    b[10] = 2
                    return True

            if b[3] == b[7] == opp:
                if b[2] == 0:
                    b[2] = p
                    b[10] = 2
                    return True

        if b[0] == 6:
            if b[6] == b[7] == b[2] == opp:
                if b[3] == 0:
                    b[3] = p
                    b[10] = 3
                    return True
            if b[6] == b[1] == b[8] == opp:
                if b[9] == 0:
                    b[9] = p
                    b[10] = 9
                    return True
            if b[8] == b[3] == b[4] == opp:
                if b[7] == 0:
                    b[7] = p
                    b[10] = 7
                    return True
            if b[4] == b[9] == b[2] == opp:
                if b[1] == 0:
                    b[1] = p
                    b[10] = 1
                    return True
        return False

    def fill(self, p):  # <~~ OCUPAR ALGUMA POSIÇÃO ESPECÍFICA (CASO NÃO HAJA COMO BLOQUEAR OU VENCER)
        b = self.board
        # Corners
        for position in [1, 3, 7, 9]:
            if b[position] == 0:
                b[position] = p
                b[10] = position
                return True
        # Sides
        for position in [2, 4, 6, 8]:
            if b[position] == 0:
                b[position] = p
                b[10] = position
                return True

    def win(self, p):  # <~~ VENCER (CASO FALTE APENAS UMA POSIÇÃO PARA VENCER)
        b = self.board
        for combo in WINCO:
            if b[combo[0]] == b[combo[1]] == p and b[combo[2]] == 0:
                b[combo[2]] = p
                b[10] = combo[2]
                return True
            if b[combo[1]] == b[combo[2]] == p and b[combo[0]] == 0:
                b[combo[0]] = p
                b[10] = combo[0]
                return True
            if b[combo[0]] == b[combo[2]] == p and b[combo[1]] == 0:
                b[combo[1]] = p
                b[10] = combo[1]
                return True
        return False

    def perfect_move(self, p):  # <~~ ESTRATÉGIA DO PLAYER PERFEITO
        self.board[0] += 1
        opp = -1 if p == 1 else 1
        b = self.board
        block = self.block
        two_steps_block = self.two_steps_block
        fill = self.fill
        win = self.win

        if b[0] == 1:
            b[1] = p
            b[10] = 1
            return

        if b[0] == 2:
            if b[5] == opp:
                b[1] = p
                b[10] = 1
                return
            b[5] = p
            b[10] = 5
            return

        if b[0] == 3:
            if b[9] == 0:
                b[9] = p
                b[10] = 9
                return
            b[7] = p
            b[10] = 7
            return

        if b[0] == 4:
            if block(p, opp):
                return
            if two_steps_block(p, opp):
                return
            fill(p)
            return

        if b[0] == 5:
            if win(p):
                return
            if block(p, opp):
                return
            fill(p)
            return

        if b[0] == 6:
            if win(p):
                return
            if block(p, opp):
                return
            if two_steps_block(p, opp):
                return
            fill(p)
            return

        if b[0] == 7:
            if win(p):
                return
            if block(p, opp):
                return
            fill(p)
            return

        if b[0] == 8:
            if win(p):
                return
            if block(p, opp):
                return
            fill(p)
            return

        if b[0] == 9:
            fill(p)

    def intelligent_move(self, p):  # <~~ ESTRATÉGIA DO PLAYER INTELIGENTE
        # [10] = última posição jogada
        # [11] = raiz da árvore de jogadas
        # [12] = pontuação
        # [13+] = jogadas ainda não feitas

        self.board[0] += 1
        b = self.board[1:10]

        if self.board[0] == 1 or self.board[0] == 2:  # <~~ NOVO ROUND
            self.moves_flag = None
            if self.win_flag < self.win_count:  # <~~ PLAYER VENCEU A PARTIDA
                self.win_flag += 1
                for move in self.random_moves:
                    move.append(1)  # PONTUAÇÃO
                    self.winning_moves.append(move)
                    unused_moves = [i for i in range(1, 10) if move[i] == 0 and i != move[10]]
                    for unused_move in unused_moves:
                        move.append(unused_move)
                    move[12] == None
                    self.database.append(move)
                for move in self.moves_used:
                    if move[1]:
                        self.winning_moves[move[0]][12] += 1
                    else:
                        aux = self.database[move[0]][0:13]
                        aux[12] = 1
                        self.winning_moves.append(aux)

            elif self.draw_flag == self.game.draw_count and self.moves_used:  # <~~ PLAYER PERDEU A PARTIDA
                for move in self.moves_used:
                    if move[1]:
                        del self.winning_moves[move[0]]

            else:  # <~~ PARTIDA TERMINOU EM EMPATE
                self.draw_flag += 1

            self.random_moves = []
            self.moves_used = []

        for pattern in self.database:
            if pattern[0] == self.board[0] and pattern[1:10] == b and len(pattern) > 13:
                self.board[pattern[13]] = p
                self.board[10] = pattern[13]
                del pattern[13]
                self.moves_used.append((self.database.index(pattern), 0))
                return

        win_moves = [move for move in self.winning_moves if move[0] == self.board[0] and move[1:10] == b]
        if win_moves:
            for move in win_moves:
                if move[12] >= 100:
                    self.board[move[10]] = p
                    self.board[10] = move[10]
                    self.moves_used.append((self.winning_moves.index(move), 1))

            win_move = choice(win_moves)
            self.board[win_move[10]] = p
            self.board[10] = win_move[10]
            self.moves_used.append((self.winning_moves.index(win_move), 1))
            return

        empty_positions = [i for i in range(1, 10) if self.board[i] == 0]
        pos = choice(empty_positions)
        self.board[pos] = p
        self.board[10] = pos
        aux = self.board.copy()
        aux[aux[10]] = 0
        self.random_moves.append(aux)


class Game:
    def __init__(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # [0] = núm. de passos, [10] = última posição preenchida
        """ 1 | 2 | 3
            4 | 5 | 6
            7 | 8 | 9 """
        self.draw_count = 0
        self.p1 = None
        self.p2 = None
        # self.games_history = []

    def print_board(self):  # <~~ PRINTAR ESTADO ATUAL DO TABULEIRO
        b = self.board
        formatted_board = f"""
        {b[1]} | {b[2]} | {b[3]}
        -----------
        {b[4]} | {b[5]} | {b[6]}
        -----------
        {b[7]} | {b[8]} | {b[9]}
        """
        print(formatted_board)

    def progress_bar(self, percentage):  # <~~ FUNÇÃO AUXILIAR DO print_progress()
        progress = percentage // 2
        remaining = 50 - progress
        return "\033[92m" + "#" * progress + "\033[0m" + "-" * remaining

    def print_progress(self):  # <~~ PRINTAR PROGRESSO DA EXECUÇÃO DO PROGRAMA
        if self.i == 0:
            print(f"\n[--------------------------------------------------] 0%", end="\r")
            return
        if self.i == self.total_rounds - 1:
            print(f"\033[K[\033[92m##################################################\033[0m] \033[92m100%\033[0m")
            return

        if self.total_rounds >= 100:
            percentage = int((self.i / self.total_rounds) * 100)
            if self.i % (self.total_rounds // 100) == 0:
                print(f"\033[K[{self.progress_bar(percentage)}] {percentage}%", end="\r")

    def reset_board(self):  # <~~ ZERAR TABULEIRO
        self.board.clear()
        self.board.extend([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, self.i])

    def reset_stats(self):  # <~~ ZERAR VITÓRIAS E EMPATES
        self.p1.win_count = 0
        self.p2.win_count = 0
        self.draw_count = 0

    def check_win(self):  # <~~ PERCORRER TABULEIRO PARA VERIFICAR SE ALGUÉM VENCEU
        for combo in WINCO:
            total = self.board[combo[0]] + self.board[combo[1]] + self.board[combo[2]]
            if total == 3:
                self.p1.win_count += 1
                # self.print_board(self.board)
                # print("WINNER: P1\n")
                return 1
            if total == -3:
                self.p2.win_count += 1
                # self.print_board(self.board)
                # print("WINNER: P2\n")
                return 1
        return 0

    def run(self):  # <~~ EXECUÇÃO DO PROGRAMA
        while True:
            try:  # <~~ VALIDAR INPUT
                p1 = int(input("\033[1mP1\033[0m Aleatório (1) OU Perfeito (2) OU Inteligente (3): "))
                if p1 not in [1, 2, 3]:
                    print("\n\033[91mEntrada inválida para P1. Tente novamente.\033[0m\n")
                    continue

                p2 = int(input("\n\033[1mP2\033[0m Aleatório (1) OU Perfeito (2) OU Inteligente (3): "))
                if p2 not in [1, 2, 3]:
                    print("\n\033[91mEntrada inválida para P2. Tente novamente.\033[0m\n")
                    continue

                self.total_rounds = int(input("\nNúmero de partidas: "))
                if not self.total_rounds > 0:
                    print("\n\033[91mEntrada inválida para número de partidas. Tente novamente.\033[0m\n")
                    continue

                alternating = int(input("\nSem alternância (0) OU Com alternância (1): "))
                if alternating not in [0, 1]:
                    print("\n\033[91mEntrada inválida para alternância. Tente novamente.\033[0m\n")
                    continue
            except ValueError:  # <~~ SE O INPUT LER ALGO QUE NÃO SEJA UM NÚMERO
                print("\n\033[91mEntrada não numérica. Tente novamente.\033[0m\n")
                continue

            self.p1 = Player(p1, 1, self)
            self.p2 = Player(p2, -1, self)

            if alternating == False:  # SEM ALTERNÂNCIA
                for self.i in range(self.total_rounds):  # <~~ QUANTIDADE DE PARTIDAS
                    for j in range(5):
                        self.p1.move()  # <~~ MOVIMENTO DO JOGADOR 1
                        if self.board[0] >= 5 and self.check_win():
                            break

                        if j == 4:
                            self.draw_count += 1
                            # self.print_board()
                            # print("DRAW\n")
                            break

                        self.p2.move()  # <~~ MOVIMENTO DO JOGADOR 2
                        if self.board[0] >= 5 and self.check_win():
                            break
                    self.reset_board()
                    self.print_progress()

            else:  # COM ALTERNÂNCIA
                for self.i in range(self.total_rounds):
                    starting_player = self.i % 2
                    for j in range(5):
                        if starting_player == 0:
                            self.p1.move()
                            if self.board[0] >= 5 and self.check_win():
                                break
                            if j == 4:
                                self.draw_count += 1
                                # self.print_board()
                                # print("DRAW\n")
                                break
                            self.p2.move()
                            if self.board[0] >= 5 and self.check_win():
                                break
                        else:
                            self.p2.move()
                            if self.board[0] >= 5 and self.check_win():
                                break
                            if j == 4:
                                self.draw_count += 1
                                # self.print_board()
                                # print("DRAW\n")
                                break
                            self.p1.move()
                            if self.board[0] >= 5 and self.check_win():
                                break
                    self.reset_board()
                    self.print_progress()

            print(f"\nP1 -> {self.p1.win_count}\nP2 -> {self.p2.win_count}\nEMPATES -> {self.draw_count}\n")
            self.reset_stats()


if __name__ == "__main__":
    game = Game()
    game.run()
