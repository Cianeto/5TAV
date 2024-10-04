import pygame as pg
import sys
import os
from random import randint, choice

WIN_SIZE = 600
CELL_SIZE = WIN_SIZE // 3
INF = float('inf')
vec2 = pg.math.Vector2
CELL_CENTER = vec2(CELL_SIZE / 2)

class TicTacToe:
    def __init__(self, game):
        self.game = game
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.field_image = self.get_scaled_image(path=os.path.join(base_dir, 'resources', 'field.png'), res=[WIN_SIZE] * 2)
        self.O_image = self.get_scaled_image(path=os.path.join(base_dir, 'resources', 'o.png'), res=[CELL_SIZE] * 2)
        self.X_image = self.get_scaled_image(path=os.path.join(base_dir, 'resources', 'x.png'), res=[CELL_SIZE] * 2)

        self.game_array = [[INF, INF, INF],
                           [INF, INF, INF],
                           [INF, INF, INF]]
        self.player = randint(0, 1)

        self.line_indices_array = [[(0, 0), (0, 1), (0, 2)],
                                   [(1, 0), (1, 1), (1, 2)],
                                   [(2, 0), (2, 1), (2, 2)],
                                   [(0, 0), (1, 0), (2, 0)],
                                   [(0, 1), (1, 1), (2, 1)],
                                   [(0, 2), (1, 2), (2, 2)],
                                   [(0, 0), (1, 1), (2, 2)],
                                   [(0, 2), (1, 1), (2, 0)]]

        self.winner = None
        self.winning_line = None
        self.game_steps = 0
        self.font = pg.font.SysFont('Verdana', CELL_SIZE // 4, True)

    def get_scaled_image(self, path, res):
        img = pg.image.load(path)
        return pg.transform.scale(img, res)

    def check_empty_cell(self, row, col):
        return self.game_array[row][col] == INF

    def make_random_move(self):
        empty_cells = [(row, col) for row in range(3) for col in range(3) if self.check_empty_cell(row, col)]
        if empty_cells:
            row, col = choice(empty_cells)
            self.game_array[row][col] = self.player
            self.player = 1 - self.player

    def draw_winner_message(self):
        if self.winner is not None:
            winner_text = f"Player {self.winner + 1} wins!"
            text_surface = self.font.render(winner_text, True, (255, 0, 0))
            text_rect = text_surface.get_rect(center=(WIN_SIZE // 2, WIN_SIZE // 2))
            self.game.screen.blit(text_surface, text_rect)

    def draw_winning_line(self):
        if self.winning_line is not None:
            start_pos = vec2(self.winning_line[0][1], self.winning_line[0][0]) * CELL_SIZE + CELL_CENTER
            end_pos = vec2(self.winning_line[2][1], self.winning_line[2][0]) * CELL_SIZE + CELL_CENTER
            pg.draw.line(self.game.screen, (255, 0, 0), start_pos, end_pos, 10)

    def run(self):
        while True:
            self.game.screen.blit(self.field_image, (0, 0))
            self.draw_objects()
            self.check_winner()
            self.draw_winner_message()
            self.draw_winning_line()
            self.check_events()
            if self.player == 1 and self.winner is None:  # Assuming player 1 is the machine
                self.make_random_move()
            pg.display.update()
            self.game.clock.tick(60)

    def draw_objects(self):
        for row in range(3):
            for col in range(3):
                if self.game_array[row][col] == 0:
                    self.game.screen.blit(self.O_image, vec2(col, row) * CELL_SIZE)
                elif self.game_array[row][col] == 1:
                    self.game.screen.blit(self.X_image, vec2(col, row) * CELL_SIZE)

    def check_winner(self):
        for line in self.line_indices_array:
            if self.game_array[line[0][0]][line[0][1]] == self.game_array[line[1][0]][line[1][1]] == self.game_array[line[2][0]][line[2][1]] != INF:
                self.winner = self.game_array[line[0][0]][line[0][1]]
                self.winning_line = line
                break

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.new_game()
            if event.type == pg.MOUSEBUTTONDOWN and self.player == 0:  # Assuming player 0 is the human
                mouse_pos = vec2(pg.mouse.get_pos()) // CELL_SIZE
                row, col = int(mouse_pos.y), int(mouse_pos.x)
                if self.check_empty_cell(row, col):
                    self.game_array[row][col] = self.player
                    self.player = 1 - self.player

    def new_game(self):
        self.game_array = [[INF, INF, INF],
                           [INF, INF, INF],
                           [INF, INF, INF]]
        self.player = randint(0, 1)
        self.winner = None
        self.winning_line = None
        self.game_steps = 0

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIN_SIZE, WIN_SIZE))
        self.clock = pg.time.Clock()
        self.tic_tac_toe = TicTacToe(self)

    def run(self):
        while True:
            self.tic_tac_toe.run()
            pg.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.run()
