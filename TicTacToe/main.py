import pygame as pg
import sys
from random import randint, choice

vec2 = pg.math.Vector2
WIN_SIZE = 600
CELL_SIZE = WIN_SIZE // 3
CELL_CENTER = vec2(CELL_SIZE / 2)
INF = float("inf")


class StartScreen:
    def __init__(self, game):
        self.game = game
        self.font = pg.font.SysFont("Verdana", 50, True)
        self.play_button = pg.Rect(WIN_SIZE // 2 - 75, WIN_SIZE // 2, 150, 50)
        self.button_font = pg.font.SysFont("Verdana", 30, True)
        self.dropdown1_rect = pg.Rect(WIN_SIZE // 4 - 75, WIN_SIZE // 2 + 60, 150, 30)
        self.dropdown2_rect = pg.Rect(
            3 * WIN_SIZE // 4 - 75, WIN_SIZE // 2 + 60, 150, 30
        )
        self.dropdown1_open = False
        self.dropdown2_open = False
        self.dropdown1_options = ["Player", "Random", "Perfect"]
        self.dropdown2_options = ["Player", "Random", "Perfect"]
        self.selected_option1 = None
        self.selected_option2 = None
        self.title_image = pg.image.load("TicTacToe/resources/tic-tac-toe.png")
        self.title_image = pg.transform.scale(
            self.title_image, (100, 100)
        )  # Ajuste o tamanho conforme necessário

    def draw_background(self):
        for i in range(WIN_SIZE):
            color = (i * 255 // WIN_SIZE, 0, 255 - i * 255 // WIN_SIZE)
            pg.draw.line(self.game.screen, color, (0, i), (WIN_SIZE, i))

    def draw_title(self):
        title_surface = self.font.render("Tic Tac Toe", True, (0, 0, 0))
        title_rect = title_surface.get_rect(
            center=(WIN_SIZE // 2 + 50, WIN_SIZE // 2 - 100)
        )

        # Desenhar a imagem ao lado esquerdo do título
        image_rect = self.title_image.get_rect(
            center=(title_rect.left - 70, title_rect.centery)
        )
        self.game.screen.blit(self.title_image, image_rect)

        # Define o retângulo do título com borda preta e cantos arredondados
        title_bg_rect = pg.Rect(
            title_rect.x - 20,
            title_rect.y - 10,
            title_rect.width + 40,
            title_rect.height + 20,
        )

        # Desenha o retângulo com borda preta e cantos arredondados
        pg.draw.rect(self.game.screen, (255, 255, 255), title_bg_rect, border_radius=10)
        pg.draw.rect(self.game.screen, (0, 0, 0), title_bg_rect, 2, border_radius=10)

        # Desenha o título dentro do retângulo
        self.game.screen.blit(title_surface, title_rect)

    def draw_play_button(self):
        shadow_offset = 5
        shadow_color = (50, 50, 50)
        pg.draw.rect(
            self.game.screen,
            shadow_color,
            self.play_button.move(shadow_offset, shadow_offset),
            border_radius=5,
        )
        pg.draw.rect(
            self.game.screen, (255, 255, 255), self.play_button, border_radius=5
        )
        pg.draw.rect(self.game.screen, (0, 0, 0), self.play_button, 2, border_radius=5)

        play_surface = self.button_font.render("Play", True, (0, 0, 0))
        play_rect = play_surface.get_rect(center=self.play_button.center)
        self.game.screen.blit(play_surface, play_rect)

    def draw_dropdowns(self):

        # Dropdown 1
        pg.draw.rect(
            self.game.screen, (255, 255, 255), self.dropdown1_rect, border_radius=5
        )
        pg.draw.rect(
            self.game.screen, (0, 0, 0), self.dropdown1_rect, 2, border_radius=5
        )

        dropdown1_text = (
            "P1 O" if self.selected_option1 is None else self.selected_option1
        )
        dropdown1_surface = self.button_font.render(dropdown1_text, True, (0, 0, 0))
        dropdown1_rect = dropdown1_surface.get_rect(center=self.dropdown1_rect.center)
        self.game.screen.blit(dropdown1_surface, dropdown1_rect)

        if self.dropdown1_open:
            for i, option in enumerate(self.dropdown1_options):
                option_rect = pg.Rect(
                    self.dropdown1_rect.x, self.dropdown1_rect.y + (i + 1) * 30, 150, 30
                )
                pg.draw.rect(
                    self.game.screen, (255, 255, 255), option_rect, border_radius=5
                )
                pg.draw.rect(
                    self.game.screen, (0, 0, 0), option_rect, 2, border_radius=5
                )
                option_surface = self.button_font.render(option, True, (0, 0, 0))
                option_rect = option_surface.get_rect(center=option_rect.center)
                self.game.screen.blit(option_surface, option_rect)

        # Dropdown 2
        pg.draw.rect(
            self.game.screen, (255, 255, 255), self.dropdown2_rect, border_radius=5
        )
        pg.draw.rect(
            self.game.screen, (0, 0, 0), self.dropdown2_rect, 2, border_radius=5
        )

        dropdown2_text = (
            "P2 X" if self.selected_option2 is None else self.selected_option2
        )
        dropdown2_surface = self.button_font.render(dropdown2_text, True, (0, 0, 0))
        dropdown2_rect = dropdown2_surface.get_rect(center=self.dropdown2_rect.center)
        self.game.screen.blit(dropdown2_surface, dropdown2_rect)

        if self.dropdown2_open:
            for i, option in enumerate(self.dropdown2_options):
                option_rect = pg.Rect(
                    self.dropdown2_rect.x, self.dropdown2_rect.y + (i + 1) * 30, 150, 30
                )
                pg.draw.rect(
                    self.game.screen, (255, 255, 255), option_rect, border_radius=5
                )
                pg.draw.rect(
                    self.game.screen, (0, 0, 0), option_rect, 2, border_radius=5
                )
                option_surface = self.button_font.render(option, True, (0, 0, 0))
                option_rect = option_surface.get_rect(center=option_rect.center)
                self.game.screen.blit(option_surface, option_rect)

    def handle_dropdown_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.dropdown1_rect.collidepoint(event.pos):
                self.dropdown1_open = not self.dropdown1_open
            elif self.dropdown2_rect.collidepoint(event.pos):
                self.dropdown2_open = not self.dropdown2_open
            else:
                if self.dropdown1_open:
                    for i, option in enumerate(self.dropdown1_options):
                        option_rect = pg.Rect(
                            self.dropdown1_rect.x,
                            self.dropdown1_rect.y + (i + 1) * 30,
                            150,
                            30,
                        )
                        if option_rect.collidepoint(event.pos):
                            self.selected_option1 = option
                            self.dropdown1_open = False
                            if option == "Player":
                                self.dropdown2_options = [
                                    opt
                                    for opt in ["Player", "Random", "Perfect"]
                                    if opt != "Player"
                                ]
                            else:
                                self.dropdown2_options = ["Player", "Random", "Perfect"]
                            break
                if self.dropdown2_open:
                    for i, option in enumerate(self.dropdown2_options):
                        option_rect = pg.Rect(
                            self.dropdown2_rect.x,
                            self.dropdown2_rect.y + (i + 1) * 30,
                            150,
                            30,
                        )
                        if option_rect.collidepoint(event.pos):
                            self.selected_option2 = option
                            self.dropdown2_open = False
                            if option == "Player":
                                self.dropdown1_options = [
                                    opt
                                    for opt in ["Player", "Random", "Perfect"]
                                    if opt != "Player"
                                ]
                            else:
                                self.dropdown1_options = ["Player", "Random", "Perfect"]
                            break

    def run(self):
        while True:
            self.draw_background()
            self.draw_title()
            self.draw_play_button()
            self.draw_dropdowns()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.play_button.collidepoint(event.pos):
                        return (self.selected_option1, self.selected_option2)
                self.handle_dropdown_event(event)

            pg.display.update()
            self.game.clock.tick(60)

class BotPlayer:
    def __init__(self, game, bot_type="Perfect"):
        self.game = game
        self.bot_type = bot_type

    def move(self):
        if self.bot_type == "Random":
            self.random_move()
        elif self.bot_type == "Perfect":
            self.perfect_move()

    def random_move(self):
        empty_cells = [
            (row, col)
            for row in range(3)
            for col in range(3)
            if self.game.check_empty_cell(row, col)
        ]
        if empty_cells:
            row, col = choice(empty_cells)
            self.game.game_array[row][col] = self.game.bot

    def perfect_move(self):
        best_val = -float("inf")
        best_move = None
        if self.game.bot is 0:
            self.opp = 1
        elif self.game.bot is 1:
            self.opp = 0

        for row in range(3):
            for col in range(3):
                if self.game.check_empty_cell(row, col):
                    self.game.game_array[row][col] = self.game.bot
                    move_val = self.minimax(0, False)
                    self.game.game_array[row][col] = float("inf")
                    if move_val > best_val:
                        best_move = (row, col)
                        best_val = move_val

        if best_move:
            row, col = best_move
            self.game.game_array[row][col] = self.game.bot

    def minimax(self, depth, is_max):
        score = self.evaluate()

        if score == 10:
            return score - depth
        if score == -10:
            return score + depth
        if not self.is_moves_left():
            return 0

        if is_max:
            best = -INF
            for row in range(3):
                for col in range(3):
                    if self.game.check_empty_cell(row, col):
                        self.game.game_array[row][col] = self.game.bot
                        best = max(best, self.minimax(depth + 1, not is_max))
                        self.game.game_array[row][col] = INF
            return best
        else:
            best = INF
            for row in range(3):
                for col in range(3):
                    if self.game.check_empty_cell(row, col):
                        self.game.game_array[row][col] = self.opp
                        best = min(best, self.minimax(depth + 1, not is_max))
                        self.game.game_array[row][col] = INF
            return best

    def evaluate(self):
        for line in self.game.line_indices_array:
            if (
                self.game.game_array[line[0][0]][line[0][1]]
                == self.game.game_array[line[1][0]][line[1][1]]
                == self.game.game_array[line[2][0]][line[2][1]]
                != INF
            ):
                if self.game.game_array[line[0][0]][line[0][1]] == self.game.bot:
                    return 10
                elif self.game.game_array[line[0][0]][line[0][1]] == self.opp:
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
        self.player1, self.player2 = None, None
        self.playerExists = None
        self.turn = None

        self.field_image = self.get_scaled_image(
            path="TicTacToe/resources/field.png", res=[WIN_SIZE] * 2
        )
        self.O_image = self.get_scaled_image(
            path="TicTacToe/resources/o.png", res=[CELL_SIZE] * 2
        )
        self.X_image = self.get_scaled_image(
            path="TicTacToe/resources/x.png", res=[CELL_SIZE] * 2
        )

        self.game_array = [[INF, INF, INF], [INF, INF, INF], [INF, INF, INF]]

        self.line_indices_array = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
        ]

        self.winner = None
        self.winning_line = None
        self.game_steps = 0
        self.font = pg.font.SysFont("Verdana", CELL_SIZE // 4, True)

    def create_players(self):
        if self.player1 != None and self.player2 != None:
            if self.player1 == "Player":
                self.bot_player = BotPlayer(self, self.player2)
                self.playerExists = True
                self.player = 0
                self.bot = 1
            elif self.player2 == "Player":
                self.bot_player = BotPlayer(self, self.player1)
                self.playerExists = True
                self.player = 1
                self.bot = 0
            else:
                self.playerExists = False
                self.bot_player1 = BotPlayer(self, self.player1)
                self.bot_player2 = BotPlayer(self, self.player2)

    def get_scaled_image(self, path, res):
        img = pg.image.load(path)
        return pg.transform.scale(img, res)

    def check_empty_cell(self, row, col):
        return self.game_array[row][col] == INF

    def draw_winner_message(self):
        if self.winner is not None and self.winner != "tie":
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
            start_pos = (
                vec2(self.winning_line[0][1], self.winning_line[0][0]) * CELL_SIZE
                + CELL_CENTER
            )
            end_pos = (
                vec2(self.winning_line[2][1], self.winning_line[2][0]) * CELL_SIZE
                + CELL_CENTER
            )
            pg.draw.line(self.game.screen, (255, 0, 0), start_pos, end_pos, 10)

    def draw_objects(self):
        for row in range(3):
            for col in range(3):
                if self.game_array[row][col] == 0:
                    self.game.screen.blit(self.O_image, vec2(col, row) * CELL_SIZE)
                elif self.game_array[row][col] == 1:
                    self.game.screen.blit(self.X_image, vec2(col, row) * CELL_SIZE)

    def check_winner(self):
        if self.winner == None:
            for line in self.line_indices_array:
                if (
                    self.game_array[line[0][0]][line[0][1]]
                    == self.game_array[line[1][0]][line[1][1]]
                    == self.game_array[line[2][0]][line[2][1]]
                    != INF
                ):
                    self.winner = self.game_array[line[0][0]][line[0][1]]
                    self.winning_line = line
                    return
            # Verificar se todas as células estão preenchidas
            if all(cell != INF for row in self.game_array for cell in row):
                self.winner = "tie"

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    self.new_game()
                if event.key == pg.K_ESCAPE:
                    return True

            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = vec2(pg.mouse.get_pos()) // CELL_SIZE
                row, col = int(mouse_pos.y), int(mouse_pos.x)
                if self.check_empty_cell(row, col):
                    self.turn = 0
                    self.game_array[row][col] = self.player
        return None

    def new_game(self):
        self.game_array = [[INF, INF, INF], [INF, INF, INF], [INF, INF, INF]]
        self.winner = None
        self.winning_line = None
        self.turn = randint(0, 1)

    def check_win(self):
        self.check_winner()
        if self.winner == "tie":
            self.draw_tie_message()
        else:
            self.draw_winner_message()
        self.draw_winning_line()

    def run(self):
        self.create_players()
        self.new_game()
        if self.playerExists:
            while True:
                self.game.screen.blit(self.field_image, (0, 0))
                if self.turn and self.winner is None:
                    back_to_menu = self.check_events()
                    if back_to_menu:
                        return
                    self.draw_objects()
                    self.check_win()
                if not self.turn and self.winner is None:
                    self.turn = 1
                    self.bot_player.move()
                    self.draw_objects()
                    self.check_win()

                pg.display.update()
                self.game.clock.tick(60)

                if self.winner is not None:
                    pg.time.wait(500)  # esperar 1 segundo antes de reiniciar o jogo
                    self.new_game()
                    
        elif self.playerExists is False:
            for i in range(100):
                self.new_game()
                self.game.screen.blit(self.field_image, (0, 0))
                while True:
                    if self.turn and self.winner is None:
                        self.turn = 0
                        self.bot = 0
                        self.bot_player1.move()
                        self.draw_objects()
                        pg.display.update()
                        print("PLAYER O JOGOU")
                        pg.time.wait(500)
                        self.check_win()
                    if not self.turn and self.winner is None:
                        self.turn = 1
                        self.bot = 1
                        self.bot_player2.move()
                        self.draw_objects()
                        pg.display.update()
                        print("PLAYER X JOGOU")
                        pg.time.wait(500)
                        self.check_win()

                    pg.display.update()
                    self.game.clock.tick(60)

                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            pg.quit()
                            sys.exit()
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_ESCAPE:
                                return

                    if self.winner is not None:
                        pg.time.wait(500)  # esperar 1 segundo antes de reiniciar o jogo
                        break

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIN_SIZE, WIN_SIZE))
        self.clock = pg.time.Clock()

        pg.display.set_caption("Tic Tac Toe")
        icon = pg.image.load("TicTacToe/resources/tic-tac-toe.png")
        pg.display.set_icon(icon)

        self.start_screen = StartScreen(self)
        self.tic_tac_toe = TicTacToe(self)

    def run(self):

        while True:
            self.tic_tac_toe.player1, self.tic_tac_toe.player2 = self.start_screen.run()
            self.tic_tac_toe.run()
            pg.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.run()
