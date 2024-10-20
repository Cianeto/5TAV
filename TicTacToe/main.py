from random import choice

ALEATORIO = 0
PERFEITO = 1
INTELIGENTE = 2


class Player:
    def __init__(self, player_type, player_symbol, board):
        self.player_type = player_type
        self.player_symbol = player_symbol
        self.board = board

    def check_empty(self, position):
        if self.board[position] != 0:
            return 1
        return 0

    def move(self):
        self.board[0] += 1
        play = {
            0: self.random_move,
            1: self.perfect_move,
        }
        play[self.player_type](self.player_symbol)
        # Game().print_board(self.board)

    def random_move(self, p):
        empty_positions = [i for i in range(1, 10) if self.board[i] == 0]
        if empty_positions:
            position = choice(empty_positions)
            self.board[position] = p

    def perfect_move(self, p):
        opp = -1 if p == 1 else 1
        b = self.board
        if b[0] == 1:
            b[1] = p
        elif b[0] == 2:
            """  """
        elif b[0] == 3:
            """  """
        elif b[0] == 4:
            """  """
        elif b[0] == 5:
            """  """
        elif b[0] == 6:
            """  """
        elif b[0] == 7:
            """  """
        elif b[0] == 8:
            """  """
        elif b[0] == 9:
            """  """

class Game:
    def __init__(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # posição 0 é o número de passos
        """ 1 | 2 | 3
            4 | 5 | 6
            7 | 8 | 9 """
        self.p1 = Player(ALEATORIO, 1, self.board)
        self.p2 = Player(PERFEITO, -1, self.board)
        self.p1_wins = 0
        self.p2_wins = 0
        self.draws = 0
        self.win_combinations = [
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

    def print_board(self, b):
        formatted_board = f"""
        {b[1]} | {b[2]} | {b[3]}
        -----------
        {b[4]} | {b[5]} | {b[6]}
        -----------
        {b[7]} | {b[8]} | {b[9]}
        """
        print(formatted_board)

    def reset_board(self):
        self.board.clear()
        self.board.extend([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def check_win(self):
        for combo in self.win_combinations:
            total = self.board[combo[0]] + self.board[combo[1]] + self.board[combo[2]]
            if total == 3:
                self.p1_wins += 1
                # self.print_board(self.board)
                # print("WINNER: P1\n")
                return 1
            elif total == -3:
                self.p2_wins += 1
                # self.print_board(self.board)
                # print("WINNER: P2\n")
                return 1
        return 0

    def run(self):
        for i in range(5000):

            # SEM ALTERNÂNCIA
            for j in range(5):
                self.p1.move()
                if self.board[0] >= 5 and self.check_win():
                    break

                if j == 4:
                    self.draws += 1
                    # self.print_board(self.board)
                    # print("DRAW\n")
                    break

                self.p2.move()
                if self.board[0] >= 5 and self.check_win():
                    break

            # COM ALTERNÂNCIA
            """ starting_player = i % 2
            for j in range(5):
                if starting_player == 0:
                    self.p1.move()
                    if self.board[0] >= 5 and self.check_win():
                        break
                    if j == 4:
                        self.draws += 1
                        # self.print_board(self.board)
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
                        self.draws += 1
                        # self.print_board(self.board)
                        # print("DRAW\n")
                        break
                    self.p1.move()
                    if self.board[0] >= 5 and self.check_win():
                        break """

            self.reset_board()
        print(f"P1 -> {self.p1_wins}\nP2 -> {self.p2_wins}\nEMPATES -> {self.draws}")


if __name__ == "__main__":
    game = Game()
    game.run()
