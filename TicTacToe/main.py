from random import randint, choice

ALEATORIO = 0
PERFEITO = 1
INTELIGENTE = 2


class Player:
    def __init__(self, player_type, player_symbol, board):
        self.player_type = player_type
        self.player_symbol = player_symbol
        self.board = board

    def move(self):
        self.board[0] += 1
        play = {
            0: self.random_move,
            1: self.perfect_move,
        }
        play[self.player_type](self.player_symbol)

    def random_move(self, p):
        """ """

    def perfect_move(self, p):
        """ """


class Game:
    def __init__(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # posição 0 é o número de passos
        """ 1 | 2 | 3
            4 | 5 | 6
            7 | 8 | 9 """
        self.p1 = Player(ALEATORIO, 1, self.board)
        self.p2 = Player(ALEATORIO, -1, self.board)
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

    def reset_board(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def check_win(self):
        for combo in self.win_combinations:
            total = self.board[combo[0]] + self.board[combo[1]] + self.board[combo[2]]
            if total == 3:
                self.p1_wins += 1
                return 1
            elif total == -3:
                self.p2_wins += 1
                return 1
        return 0

    def run(self):
        for i in range(100):
            for j in range(5):
                self.p1.move()
                if self.board[0] >= 5:
                    if self.check_win():
                        break

                if j == 5:
                    self.draws += 1
                    break

                self.p2.move()
                if self.board[0] >= 5:
                    if self.check_win():
                        break
                    
            self.reset_board()
        print(f"P1 -> {self.p1_wins}\nP2 -> {self.p2_wins}\nEMPATES -> {self.draws}")


if __name__ == "__main__":
    game = Game()
    game.run()
