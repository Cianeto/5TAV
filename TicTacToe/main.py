import pygame as pg
import sys
from random import randint, choice

WIN_SIZE = 600
CELL_SIZE = WIN_SIZE // 3
INF = float('inf')
vec2 = pg.math.Vector2
CELL_CENTER = vec2(CELL_SIZE / 2)

class StartScreen:
    def __init__(self, game):
        self.game = game
        self.font = pg.font.SysFont('Verdana', 50, True)
        self.play_button = pg.Rect(WIN_SIZE // 2 - 75, WIN_SIZE // 2, 150, 50)
        self.button_font = pg.font.SysFont('Verdana', 30, True)

    def draw_background(self):
        # Draw a gradient background
        for i in range(WIN_SIZE):
            color = (i * 255 // WIN_SIZE, 0, 255 - i * 255 // WIN_SIZE)
            pg.draw.line(self.game.screen, color, (0, i), (WIN_SIZE, i))

    def draw_title(self):
        title_surface = self.font.render("TIC TAC TOE", True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(WIN_SIZE // 2, WIN_SIZE // 2 - 100))
        self.game.screen.blit(title_surface, title_rect)

    def draw_play_button(self):
        # Draw button with shadow
        shadow_offset = 5
        shadow_color = (50, 50, 50)
        pg.draw.rect(self.game.screen, shadow_color, self.play_button.move(shadow_offset, shadow_offset))
        pg.draw.rect(self.game.screen, (255, 255, 255), self.play_button)
        
        play_surface = self.button_font.render("Play", True, (0, 0, 0))
        play_rect = play_surface.get_rect(center=self.play_button.center)
        self.game.screen.blit(play_surface, play_rect)

    def run(self):
        while True:
            self.draw_background()
            self.draw_title()
            self.draw_play_button()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.play_button.collidepoint(event.pos):
                        return

            pg.display.update()
            self.game.clock.tick(60)

class BotPlayer:
    def __init__(self, game, bot_type='perfect'):
        self.game = game
        self.bot_type = bot_type

    def move(self):
        if self.bot_type == 'random':
            self.random_move()
        elif self.bot_type == 'perfect':
            self.perfect_move()

    def random_move(self):
        empty_cells = [(row, col) for row in range(3) for col in range(3) if self.game.check_empty_cell(row, col)]
        if empty_cells:
            row, col = choice(empty_cells)
            self.game.game_array[row][col] = self.game.player
            self.game.player = 1 - self.game.player

    def perfect_move(self):
        best_val = -float('inf')
        best_move = None

        for row in range(3):
            for col in range(3):
                if self.game.check_empty_cell(row, col):
                    self.game.game_array[row][col] = self.game.player
                    move_val = self.minimax(0, False)
                    self.game.game_array[row][col] = float('inf')
                    if move_val > best_val:
                        best_move = (row, col)
                        best_val = move_val

        if best_move:
            row, col = best_move
            self.game.game_array[row][col] = self.game.player
            self.game.player = 1 - self.game.player

    def minimax(self, depth, is_max):
        score = self.evaluate()

        if score == 10:
            return score - depth
        if score == -10:
            return score + depth
        if not self.is_moves_left():
            return 0

        if is_max:
            best = -float('inf')
            for row in range(3):
                for col in range(3):
                    if self.game.check_empty_cell(row, col):
                        self.game.game_array[row][col] = self.game.player
                        best = max(best, self.minimax(depth + 1, not is_max))
                        self.game.game_array[row][col] = float('inf')
            return best
        else:
            best = float('inf')
            for row in range(3):
                for col in range(3):
                    if self.game.check_empty_cell(row, col):
                        self.game.game_array[row][col] = 1 - self.game.player
                        best = min(best, self.minimax(depth + 1, not is_max))
                        self.game.game_array[row][col] = float('inf')
            return best

    def evaluate(self):
        for line in self.game.line_indices_array:
            if self.game.game_array[line[0][0]][line[0][1]] == self.game.game_array[line[1][0]][line[1][1]] == self.game.game_array[line[2][0]][line[2][1]] != float('inf'):
                if self.game.game_array[line[0][0]][line[0][1]] == self.game.player:
                    return 10
                elif self.game.game_array[line[0][0]][line[0][1]] == 1 - self.game.player:
                    return -10
        return 0

    def is_moves_left(self):
        for row in range(3):
            for col in range(3):
                if self.game.check_empty_cell(row, col):
                    return True
        return False


class TicTacToe:
    def __init__(self, game):
        self.game = game
        self.bot_player = BotPlayer(self)
        self.field_image = self.get_scaled_image(path='TicTacToe/resources/field.png', res=[WIN_SIZE] * 2)
        self.O_image = self.get_scaled_image(path='TicTacToe/resources/o.png', res=[CELL_SIZE] * 2)
        self.X_image = self.get_scaled_image(path='TicTacToe/resources/x.png', res=[CELL_SIZE] * 2)

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

    def draw_winner_message(self):
        if self.winner is not None and self.winner != 'tie':
            winner_text = f"Player {self.winner + 1} wins!"
            text_surface = self.font.render(winner_text, True, (255, 0, 0))
            text_rect = text_surface.get_rect(center=(WIN_SIZE // 2, WIN_SIZE // 2))
            self.game.screen.blit(text_surface, text_rect)

    def draw_tie_message(self):
        tie_text = "Draw"
        text_surface = self.font.render(tie_text, True, (255, 0, 0))
        text_rect = text_surface.get_rect(center=(WIN_SIZE // 2, WIN_SIZE // 2))
        self.game.screen.blit(text_surface, text_rect)

    def draw_winning_line(self):
        if self.winning_line is not None:
            start_pos = vec2(self.winning_line[0][1], self.winning_line[0][0]) * CELL_SIZE + CELL_CENTER
            end_pos = vec2(self.winning_line[2][1], self.winning_line[2][0]) * CELL_SIZE + CELL_CENTER
            pg.draw.line(self.game.screen, (255, 0, 0), start_pos, end_pos, 10)

    def draw_objects(self):
        for row in range(3):
            for col in range(3):
                if self.game_array[row][col] == 0:
                    self.game.screen.blit(self.O_image, vec2(col, row) * CELL_SIZE)
                elif self.game_array[row][col] == 1:
                    self.game.screen.blit(self.X_image, vec2(col, row) * CELL_SIZE)

    def check_winner(self):
        if(self.winner == None):
            for line in self.line_indices_array:
                if self.game_array[line[0][0]][line[0][1]] == self.game_array[line[1][0]][line[1][1]] == self.game_array[line[2][0]][line[2][1]] != INF:
                    self.winner = self.game_array[line[0][0]][line[0][1]]
                    self.winning_line = line
                    return
            # Verificar se todas as células estão preenchidas
            if all(cell != INF for row in self.game_array for cell in row):
                self.winner = 'tie'

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.new_game()
                """ if event.key == pg.K_r: """

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

    def check_win(self):
        self.check_winner()
        if self.winner == 'tie':
            self.draw_tie_message()
        else:
            self.draw_winner_message()
        self.draw_winning_line()

    def run(self):
        while True:
            self.game.screen.blit(self.field_image, (0, 0))
            self.check_events()
            self.draw_objects()
            self.check_win()
            if self.player == 1 and self.winner is None:  # Assuming player 1 is the machine
                self.bot_player.move()
                self.draw_objects()
                pg.time.wait(1000)
                self.check_win()

            pg.display.update()
            self.game.clock.tick(60)

            if self.winner is not None:
                pg.time.wait(1000)  # esperar 1 segundo antes de reiniciar o jogo
                self.new_game()

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIN_SIZE, WIN_SIZE))
        self.clock = pg.time.Clock()

        pg.display.set_caption("Tic Tac Toe")
        icon = pg.image.load('TicTacToe/resources/tic-tac-toe.png')
        pg.display.set_icon(icon)

        self.start_screen = StartScreen(self)
        self.tic_tac_toe = TicTacToe(self)

    def run(self):
        
        while True:
            self.start_screen.run()
            self.tic_tac_toe.run()
            pg.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()
