import matplotlib.pyplot as plt
import csv
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
        if self.player_type == 3:
            if self.player_symbol == 1:
                self.win_pos = 12
            else:
                self.win_pos = 13
            self.ranked_moves = []
            self.random_moves = []
            self.move_database = []
            self.win_flag = 0
            self.draw_flag = 0

    def move(self):  # <~~ DEFINE QUAL ESTRATÉGIA ESSE PLAYER APLICARÁ
        play = {1: self.random_move, 2: self.perfect_move, 3: self.intelligent_move}
        play[self.player_type](self.player_symbol)
        # self.game.print_board()

    def random_move(self, p):  # <~~ ESTRATÉGIA DO PLAYER ALEATÓRIO
        self.board[0] += 1
        empty_positions = [i for i in range(1, 10) if self.board[i] == 0]
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
        # [11] = núm. de jogos
        # [12] = P1 vitórias
        # [13] = P2 vitórias
        # [14] = empates
        # [15] = pontuação

        self.board[0] += 1
        b = self.board[1:10]

        if self.board[0] == 1 or self.board[0] == 2:  # <~~ NOVO ROUND
            if self.win_flag < self.board[self.win_pos]:  # <~~ PLAYER VENCEU A PARTIDA
                self.win_flag += 1
                for move in self.random_moves:
                    self.move_database.append(move)  # <~~ JOGADA ALEATÓRIA ADICIONADA À BASE DE DADOS
                for move_pos in self.ranked_moves:
                    self.move_database[move_pos][15] += 1  # <~~ RECOMPENSA

            elif self.draw_flag == self.board[14]:  # <~~ PLAYER PERDEU A PARTIDA
                self.ranked_moves.sort(reverse=True)
                for move_pos in self.ranked_moves:
                    self.move_database[move_pos][15] -= 10  # <~~ PUNIÇÃO POR PERDER
                    if self.move_database[move_pos][15] < 0:  # <~~ PONTUAÇÃO NEGATIVA -> RETIRA JOGADA DA BASE DE DADOS
                        del self.move_database[move_pos]

            else:  # <~~ PARTIDA TERMINOU EM EMPATE
                self.draw_flag += 1
                for move in self.ranked_moves:
                    self.move_database[move][15] -= 1  # <~~ PUNIÇÃO POR EMPATAR
                for move_pos in self.random_moves:
                    self.move_database.append(move_pos)  # <~~ JOGADA ALEATÓRIA ADICIONADA À BASE DE DADOS

            self.move_database.sort(key=lambda sub_arr: sub_arr[15], reverse=True)
            self.random_moves = []
            self.ranked_moves = []

        possible_move_exists = [
            move + [index]
            for index, move in enumerate(self.move_database)
            if move[0] == self.board[0] and move[1:10] == b
        ]
        if possible_move_exists:
            aux = [possible_move_exists[0]]
            for move in possible_move_exists[1:]:
                if move[15] < aux[0][15]:
                    break
                aux.append(move)

            aux = choice(aux)
            self.ranked_moves.append(aux[16])
            self.board[aux[10]] = p
            self.board[10] = aux[10]
            return

        # JOGADA ALEATÓRIA CASO NÃO ENCONTRE JOGADA COM PONTUAÇÃO SUFICIENTE NA BASE DE DADOS
        empty_positions = [i for i in range(1, 10) if self.board[i] == 0]
        pos = choice(empty_positions)
        self.board[pos] = p
        self.board[10] = pos
        aux = self.board.copy()
        aux[aux[10]] = 0
        self.random_moves.append(aux)


class Game:
    def __init__(self):
        self.board = [0] * 16  # [0] = passos, [10] = última posição jogada
        # [11] = núm. de jogos, [12] = P1 vitórias, [13] = P2 vitórias, [14] = empates, [15] = pontuação
        """ 1 | 2 | 3
            4 | 5 | 6
            7 | 8 | 9 """
        self.p1 = None
        self.p2 = None
        self.tictactoe_debug = []

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
        for i in range(11):
            self.board[i] = 0
        self.board[11] += 1

    def reset_all(self):  # <~~ ZERAR VITÓRIAS E EMPATES
        self.board.clear()
        self.board.extend([0] * 16)

    def store_board_to_debug(self):
        b = self.board
        formatted_board = f"""
        {b[1]} | {b[2]} | {b[3]}
        -----------
        {b[4]} | {b[5]} | {b[6]}
        -----------
        {b[7]} | {b[8]} | {b[9]}
        """
        self.tictactoe_debug.append(formatted_board)

    def print_stored_boards(self):
        for board in self.tictactoe_debug:
            print(board + "\n")

    def write_log(self):
        with open("TicTacToe/log.csv", "a") as log_file:
            elements = self.board[11:15]
            csv_line = ",".join(map(str, elements))
            log_file.write(f"{csv_line}\n")

    def reset_log(self):
        with open("TicTacToe/log.csv", "w") as log_file:
            log_file.write("rounds,p1,p2,draws\n")

    def draw_graph(self):
        rounds = []
        p1 = []
        p2 = []
        draws = []

        with open("TicTacToe/log.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                rounds.append(int(row["rounds"]))
                p1.append(int(row["p1"]))
                p2.append(int(row["p2"]))
                draws.append(int(row["draws"]))

        # Plot the data
        plt.plot(rounds, p1, label="P1 Wins")
        plt.plot(rounds, p2, label="P2 Wins")
        plt.plot(rounds, draws, label="Draws")

        # Add labels and title
        plt.xlabel("Rounds")
        plt.ylabel("Scores")
        plt.title("Game Scores Over Rounds")
        plt.legend()

        # Show the plot
        plt.show()

    def check_win(self):  # <~~ PERCORRER TABULEIRO PARA VERIFICAR SE ALGUÉM VENCEU
        for combo in WINCO:
            total = self.board[combo[0]] + self.board[combo[1]] + self.board[combo[2]]
            if total == 3:
                self.board[12] += 1
                # print("WINNER: P1\n")
                # if self.i > 10000:
                #    print("NAOOOOOO")
                self.write_log()
                return 1
            if total == -3:
                self.board[13] += 1
                # print("WINNER: P2\n")
                # if self.i > 10000:
                #    print("NAOOOOOO")
                self.write_log()
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

            self.reset_log()

            if alternating == False:  # SEM ALTERNÂNCIA
                for self.i in range(self.total_rounds):  # <~~ QUANTIDADE DE PARTIDAS
                    for j in range(5):
                        self.p1.move()  # <~~ MOVIMENTO DO JOGADOR 1
                        if self.board[0] >= 5 and self.check_win():
                            break

                        if j == 4:
                            self.board[14] += 1
                            self.write_log()
                            # print("DRAW\n")
                            break

                        self.p2.move()  # <~~ MOVIMENTO DO JOGADOR 2
                        if self.board[0] >= 5 and self.check_win():
                            break
                    self.reset_board()
                    self.print_progress()
                    # self.tictactoe_debug = []

            else:  # COM ALTERNÂNCIA
                for self.i in range(self.total_rounds):
                    starting_player = self.i % 2
                    for j in range(5):
                        if starting_player == 0:
                            self.p1.move()
                            if self.board[0] >= 5 and self.check_win():
                                break
                            if j == 4:
                                self.board[14] += 1
                                self.write_log()
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
                                self.board[14] += 1
                                self.write_log()
                                # print("DRAW\n")
                                break
                            self.p1.move()
                            if self.board[0] >= 5 and self.check_win():
                                break
                    self.reset_board()
                    self.print_progress()

            print(
                f"\nP1 -> {self.board[12]} ({self.board[12]/self.total_rounds*100:.2f}%)\nP2 -> {self.board[13]} ({self.board[13]/self.total_rounds*100:.2f}%)\nEMPATES -> {self.board[14]} ({self.board[14]/self.total_rounds*100:.2f}%)\n"
            )

            self.reset_all()
            self.draw_graph()


if __name__ == "__main__":
    game = Game()
    game.run()
