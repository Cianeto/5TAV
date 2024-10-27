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
    def __init__(self, player_type, player_symbol, board):
        self.player_type = player_type
        self.player_symbol = player_symbol
        self.board = board
        self.matches_won = []
        self.matches_drawn = []
        self.current_match = []
        self.moves_used = []
        self.gen_match_id = 1

    def move(self):  # <~~ DEFINE QUAL ESTRATÉGIA ESSE PLAYER APLICARÁ
        play = {1: self.random_move, 2: self.perfect_move, 3: self.intelligent_move}
        play[self.player_type](self.player_symbol)
        # Game().print_board(self.board)

    def random_move(self, p):  # <~~ ESTRATÉGIA DO PLAYER ALEATÓRIO
        self.board[0] += 1
        empty_positions = [i for i in range(1, 10) if self.board[i] == 0]
        if empty_positions:
            position = choice(empty_positions)
            self.board[position] = p

    def block(self, p, opp):  # <~~ BLOQUEAR OPONENTE (SE O PRÓXIMO MOVE DELE CONCLUIR A PARTIDA)
        b = self.board
        for combo in WINCO:
            if b[combo[0]] == b[combo[1]] == opp and b[combo[2]] == 0:
                b[combo[2]] = p
                return True
            if b[combo[1]] == b[combo[2]] == opp and b[combo[0]] == 0:
                b[combo[0]] = p
                return True
            if b[combo[0]] == b[combo[2]] == opp and b[combo[1]] == 0:
                b[combo[1]] = p
                return True
        return False

    def two_steps_block(self, p, opp):  # <~~ BLOQUEAR OPONENTE (SE OS PRÓXIMOS DOIS MOVES DELE CONCLUIR A PARTIDA)
        b = self.board

        if b[0] == 4:
            if b[6] == b[7] == opp:
                if b[8] == 0:
                    b[8] = p
                    return True
            if b[6] == b[1] == opp:
                if b[2] == 0:
                    b[2] = p
                    return True

            if b[8] == b[1] == opp:
                if b[4] == 0:
                    b[4] = p
                    return True
            if b[8] == b[3] == opp:
                if b[6] == 0:
                    b[6] = p
                    return True

            if b[4] == b[3] == opp:
                if b[1] == 0:
                    b[1] = p
                    return True
            if b[4] == b[9] == opp:
                if b[7] == 0:
                    b[7] = p
                    return True

            if b[2] == b[7] == opp:
                if b[1] == 0:
                    b[1] = p
                    return True
            if b[2] == b[9] == opp:
                if b[3] == 0:
                    b[3] = p
                    return True

            if b[6] == b[8] == opp:
                if b[9] == 0:
                    b[9] = p
                    return True

            if b[4] == b[8] == opp:
                if b[7] == 0:
                    b[7] = p
                    return True

            if b[2] == b[4] == opp:
                if b[1] == 0:
                    b[1] = p
                    return True

            if b[2] == b[6] == opp:
                if b[3] == 0:
                    b[3] = p
                    return True

            if b[1] == b[9] == opp:
                if b[2] == 0:
                    b[2] = p
                    return True

            if b[3] == b[7] == opp:
                if b[2] == 0:
                    b[2] = p
                    return True

        if b[0] == 6:
            if b[6] == b[7] == b[2] == opp:
                if b[3] == 0:
                    b[3] = p
                    return True
            if b[6] == b[1] == b[8] == opp:
                if b[9] == 0:
                    b[9] = p
                    return True
            if b[8] == b[3] == b[4] == opp:
                if b[7] == 0:
                    b[7] = p
                    return True
            if b[4] == b[9] == b[2] == opp:
                if b[1] == 0:
                    b[1] = p
                    return True
        return False

    def fill(self, p):  # <~~ OCUPAR ALGUMA POSIÇÃO ESPECÍFICA (CASO NÃO HAJA COMO BLOQUEAR OU VENCER)
        b = self.board
        # Corners
        for position in [1, 3, 7, 9]:
            if b[position] == 0:
                b[position] = p
                return True
        # Sides
        for position in [2, 4, 6, 8]:
            if b[position] == 0:
                b[position] = p
                return True

    def win(self, p):  # <~~ VENCER (CASO FALTE APENAS UMA POSIÇÃO PARA VENCER)
        b = self.board
        for combo in WINCO:
            if b[combo[0]] == b[combo[1]] == p and b[combo[2]] == 0:
                b[combo[2]] = p
                return True
            if b[combo[1]] == b[combo[2]] == p and b[combo[0]] == 0:
                b[combo[0]] = p
                return True
            if b[combo[0]] == b[combo[2]] == p and b[combo[1]] == 0:
                b[combo[1]] = p
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
            return

        if b[0] == 2:
            if b[5] == opp:
                b[1] = p
                return
            b[5] = p
            return

        if b[0] == 3:
            if b[5] == opp:
                b[9] = p
                return
            if b[9] == 0:
                b[9] = p
                return
            b[7] = p
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

    def find_next_move(self, m, match_type, p):
        aux = 0
        if match_type:
            filtered_matches = [match for match in self.matches_won if match[0] == m[0] + 1]
            for match in filtered_matches:
                if match[11] > aux:
                    aux = match[11]
                    pos = match[10]
            return pos

    def intelligent_move(self, p):  # <~~ ESTRATÉGIA DO PLAYER INTELIGENTE

        highest_score = 0
        aux = self.board.copy()
        aux.append(1)
        aux.append(self.gen_match_id)
        self.current_match.append(aux)

        b = self.board[1:10]

        filtered_won_matches = [match for match in self.matches_won if match[0] == self.board[0] + 1]
        for match in filtered_won_matches:
            match[match[10]] = 0
            if match[1:10] == b and match[11] > highest_score:
                highest_score = match[11]
                best_position = match[10]
        if highest_score != 0:
            self.board[0] += 1
            self.board[best_position] = p
            return
        
        filtered_drawn_matches = [match for match in self.matches_drawn if match[0] == self.board[0] + 1]
        for match in filtered_drawn_matches:
            match[match[10]] = 0
            if match[1:10] == b and match[11] > highest_score:
                highest_score = match[11]
                best_position = match[10]
        if highest_score != 0:
            self.board[0] += 1
            self.board[best_position] = p
            return

        self.random_move(p)


class Game:
    def __init__(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # [0] = núm. de passos, [10] = última posição preenchida
        """ 1 | 2 | 3
            4 | 5 | 6
            7 | 8 | 9 """
        self.p1_wins = 0
        self.p2_wins = 0
        self.draws = 0
        # self.games_history = []

    def print_board(self, b):  # <~~ PRINTAR ESTADO ATUAL DO TABULEIRO
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

    def print_progress(self, i, t):  # <~~ PRINTAR PROGRESSO DA EXECUÇÃO DO PROGRAMA
        if i == 0:
            print(f"\n[--------------------------------------------------] 0%", end="\r")
            return
        if i == t - 1:
            print(f"\033[K[\033[92m##################################################\033[0m] \033[92m100%\033[0m")
            return

        if t >= 100:
            percentage = int((i / t) * 100)
            if i % (t // 100) == 0:
                print(f"\033[K[{self.progress_bar(percentage)}] {percentage}%", end="\r")

    def reset_board(self):  # <~~ ZERAR TABULEIRO
        self.board.clear()
        self.board.extend([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def reset_stats(self):  # <~~ ZERAR VITÓRIAS E EMPATES
        self.p1_wins = 0
        self.p2_wins = 0
        self.draws = 0

    def check_win(self):  # <~~ PERCORRER TABULEIRO PARA VERIFICAR SE ALGUÉM VENCEU
        for combo in WINCO:
            total = self.board[combo[0]] + self.board[combo[1]] + self.board[combo[2]]
            if total == 3:
                self.p1_wins += 1
                # self.print_board(self.board)
                # print("WINNER: P1\n")
                return 1
            if total == -3:
                self.p2_wins += 1
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

                total_rounds = int(input("\nNúmero de partidas: "))
                if not total_rounds > 0:
                    print("\n\033[91mEntrada inválida para número de partidas. Tente novamente.\033[0m\n")
                    continue

                alternating = int(input("\nSem alternância (0) OU Com alternância (1): "))
                if alternating not in [0, 1]:
                    print("\n\033[91mEntrada inválida para alternância. Tente novamente.\033[0m\n")
                    continue
            except ValueError:  # <~~ SE O INPUT LER ALGO QUE NÃO SEJA UM NÚMERO
                print("\n\033[91mEntrada não numérica. Tente novamente.\033[0m\n")
                continue

            p1 = Player(p1, 1, self.board)
            p2 = Player(p2, -1, self.board)

            if alternating == False:  # SEM ALTERNÂNCIA
                for i in range(total_rounds):  # <~~ QUANTIDADE DE PARTIDAS
                    for j in range(5):
                        p1.move()  # <~~ MOVIMENTO DO JOGADOR 1
                        if self.board[0] >= 5 and self.check_win():
                            break

                        if j == 4:
                            self.draws += 1
                            # self.print_board(self.board)
                            # print("DRAW\n")
                            break

                        p2.move()  # <~~ MOVIMENTO DO JOGADOR 2
                        if self.board[0] >= 5 and self.check_win():
                            break
                    self.reset_board()
                    self.print_progress(i, total_rounds)

            else:  # COM ALTERNÂNCIA
                for i in range(total_rounds):
                    starting_player = i % 2
                    for j in range(5):
                        if starting_player == 0:
                            p1.move()
                            if self.board[0] >= 5 and self.check_win():
                                break
                            if j == 4:
                                self.draws += 1
                                # self.print_board(self.board)
                                # print("DRAW\n")
                                break
                            p2.move()
                            if self.board[0] >= 5 and self.check_win():
                                break
                        else:
                            p2.move()
                            if self.board[0] >= 5 and self.check_win():
                                break
                            if j == 4:
                                self.draws += 1
                                # self.print_board(self.board)
                                # print("DRAW\n")
                                break
                            p1.move()
                            if self.board[0] >= 5 and self.check_win():
                                break
                    self.reset_board()
                    self.print_progress(i, total_rounds)

            print(f"\nP1 -> {self.p1_wins}\nP2 -> {self.p2_wins}\nEMPATES -> {self.draws}\n")
            self.reset_stats()


if __name__ == "__main__":
    game = Game()
    game.run()
