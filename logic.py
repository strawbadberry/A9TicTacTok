import random

class TicTacToe:
    def __init__(self, single_player=False):
        self.game_board = self.initialize_empty_board()
        self.current_player = 'X'
        self.single_player_mode = single_player
        self.bot_player = Bot() if single_player else None
        self.winner = None
        self.move_count = 0

    def initialize_empty_board(self):
        return [[None, None, None] for _ in range(3)]

    def display_board(self):
        for row in self.game_board:
            print(' | '.join([cell if cell is not None else ' ' for cell in row]))

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def get_player_input(self):
        if self.current_player == 'O' and self.single_player_mode:
            return self.bot_player.make_move(self.game_board)
        else:
            prompt = f"Player {self.current_player}, enter your move (row,col): "
            player_input = input(prompt)
            row_col_list = player_input.split(',')
            return [int(x) for x in row_col_list]

    def increment_move_count(self):
        self.move_count += 1
        
    def check_winner(self):
        # Check rows for a winner
        for row in self.game_board:
            if row[0] == row[1] == row[2] and row[0] is not None:
                self.winner = row[0]
                return row[0]

        # Check columns for a winner
        for col in range(3):
            if self.game_board[0][col] == self.game_board[1][col] == self.game_board[2][col] and self.game_board[0][col] is not None:
                self.winner = self.game_board[0][col]
                return self.game_board[0][col]

        # Check diagonals for a winner
        if self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] and self.game_board[0][0] is not None:
            self.winner = self.game_board[0][0]
            return self.game_board[0][0]
        if self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0] and self.game_board[0][2] is not None:
            self.winner = self.game_board[0][2]
            return self.game_board[0][2]

        # Check for a draw
        if all(all(row) for row in self.game_board):
            self.winner = "draw"
            return "draw"

        return None

    def play_game(self):
        winner = None
        while winner is None:
            self.display_board()
            try:
                row, col = self.get_player_input()
                if self.game_board[row][col] is not None:
                    print("Spot taken, try again.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input, try again.")
                continue

            self.game_board[row][col] = self.current_player
            winner = self.check_winner()
            self.switch_player()

        self.display_board()
        if winner == "draw":
            print("It's a draw!")
        else:
            print(f"Player {winner} wins!")

class Bot:
    def make_move(self, board):
        empty_positions = [(i, j) for i in range(3) for j in range(3) if board[i][j] is None]
        return random.choice(empty_positions)



