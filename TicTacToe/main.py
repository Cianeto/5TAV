from random import randint, choice

ALEATORIO = 0
PERFEITO = 1
INTELIGENTE = 2

class Player:
    def __init__(self, playerType):
        self.playerType = playerType

    def move(self):
        players = {
            0: self.random_move,
            1: self.perfect_move,
        }

    def random_move(self):
        """ do this """

class Game:
    def __init__(self):
        self.p1 = Player(ALEATORIO)
        self.p2 = Player(PERFEITO)
        

if __name__ == "__main__":
    game = Game()
    game.run()
