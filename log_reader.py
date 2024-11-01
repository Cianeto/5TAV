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


class LogReader:
    def __init__(self):
        self.p1_wins = 0
        self.p2_wins = 0

    def check_win(self, arr):
        for combo in WINCO:
            total = arr[combo[0]] + arr[combo[1]] + arr[combo[2]]
            if total == 3:
                self.p1_wins += 1
                return 1
            if total == -3:
                self.p2_wins += 1
                return 1

    def reset_stats(self):
        self.p1_wins = 0
        self.p2_wins = 0

    def run(self):
        with open("log.txt", "r") as log_file:
            for line in log_file:
                array = eval(line.strip())
                if array[11] < 500:
                    self.check_win(array)
                elif array[11] == 500:
                    if array[0] == 1:
                        print(f"~~> Primeiro Corte\n~~> P1: ", self.p1_wins, "\n~~> P2: ", self.p2_wins)
                        self.reset_stats()
                    self.check_win(array)
                else:
                    self.check_win(array)
        print(f"~~> Segunda Corte\n~~> P1: ", self.p1_wins, "\n~~> P2: ", self.p2_wins)


if __name__ == "__main__":
    log_reader = LogReader()
    log_reader.run()
