from random import choice

ALEATORIO = 0
PERFEITO = 1
INTELIGENTE = 2


class Player:
    def __init__(self, player_type, player_symbol, board, winco):
        self.player_type = player_type
        self.player_symbol = player_symbol
        self.board = board
        self.win_combinations = winco

    def move(self):
        self.board[0] += 1
        play = {
            0: self.random_move,
            1: self.perfect_move,
        }
        play[self.player_type](self.player_symbol)
        Game().print_board(self.board)

    def random_move(self, p):
        empty_positions = [i for i in range(1, 10) if self.board[i] == 0]
        if empty_positions:
            position = choice(empty_positions)
            self.board[position] = p

    def block(self, p, opp):
        b = self.board
        for combo in self.win_combinations:
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

    def two_steps_block(self, p, opp):
        b = self.board

        if b[6] == b[7] == opp:
            if b[8] == 0:
                b[8] = p
                return True
            """ if b[9] == 0:
                b[9] = p
                return True """
        if b[6] == b[1] == opp:
            if b[2] == 0:
                b[2] = p
                return True
            """ if b[3] == 0:
                b[3] = p
                return True """
            
        if b[8] == b[1] == opp:
            if b[4] == 0:
                b[4] = p
                return True
            """ if b[7] == 0:
                b[7] = p
                return True """
        if b[8] == b[3] == opp:
            if b[6] == 0:
                b[6] = p
                return True
            """ if b[9] == 0:
                b[9] = p
                return True """

        if b[4] == b[3] == opp:
            if b[1] == 0:
                b[1] = p
                return True
            """ if b[2] == 0:
                b[2] = p
                return True """
        if b[4] == b[9] == opp:
            if b[7] == 0:
                b[7] = p
                return True
            """ if b[8] == 0:
                b[8] = p
                return True """
            
        if b[2] == b[7] == opp:
            if b[1] == 0:
                b[1] = p
                return True
            """ if b[4] == 0:
                b[4] = p
                return True """
        if b[2] == b[9] == opp:
            if b[3] == 0:
                b[3] = p
                return True
            """ if b[6] == 0:
                b[6] = p
                return True """
            
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

        return False

    def fill(self, p):
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

    def win(self, p):
        b = self.board
        for combo in self.win_combinations:
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

    def perfect_move(self, p):
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


class Game:
    def __init__(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # posição 0 é o número de passos
        """ 1 | 2 | 3
            4 | 5 | 6
            7 | 8 | 9 """
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
        self.p1 = Player(ALEATORIO, 1, self.board, self.win_combinations)
        self.p2 = Player(PERFEITO, -1, self.board, self.win_combinations)
        self.p1_wins = 0
        self.p2_wins = 0
        self.draws = 0

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
                print("WINNER: P1\n")
                return 1
            elif total == -3:
                self.p2_wins += 1
                # self.print_board(self.board)
                # print("WINNER: P2\n")
                return 1
        return 0

    def run(self):
        for i in range(20):

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
