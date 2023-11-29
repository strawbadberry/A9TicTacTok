import unittest
from unittest.mock import patch
from logic import HumanPlayer, BotPlayer, TicTacToe

class TestHumanPlayer(unittest.TestCase):
    @patch('builtins.input', return_value='1,1')
    def test_get_move(self, mock_input):
        player = HumanPlayer('X')
        move = tuple(player.get_move(None))
        self.assertEqual(move, (1, 1))

class TestBotPlayer(unittest.TestCase):
    def test_get_move(self):
        board = [[None, None, None], [None, None, None], [None, None, None]]
        player = BotPlayer('O')
        x, y = player.get_move(board)
        self.assertIn((x, y), [(i, j) for i in range(3) for j in range(3)])

class TestTicTacToe(unittest.TestCase):
    def test_initial_board(self):
        game = TicTacToe(HumanPlayer('X'), BotPlayer('O'))
        self.assertEqual(game.board, [[None] * 3 for _ in range(3)])

    @patch('builtins.input', return_value='1,1')
    def test_play_turn(self, mock_input):
        game = TicTacToe(HumanPlayer('X'), BotPlayer('O'))
        game.play_turn()
        self.assertEqual(game.board[1][1], 'X')

    def test_winner_row(self):
        game = TicTacToe(HumanPlayer('X'), BotPlayer('O'))
        game.board = [['X', 'X', 'X'], [None, None, None], [None, None, None]]
        self.assertEqual(game.get_winner(), 'X')

    def test_winner_column(self):
        game = TicTacToe(HumanPlayer('X'), BotPlayer('O'))
        game.board = [['O', None, 'X'], ['O', 'X', None], ['O', None, 'X']]
        self.assertEqual(game.get_winner(), 'O')

    def test_winner_diagonal(self):
        game = TicTacToe(HumanPlayer('X'), BotPlayer('O'))
        game.board = [['X', None, 'O'], [None, 'X', None], ['O', None, 'X']]
        self.assertEqual(game.get_winner(), 'X')

    def test_draw(self):
        game = TicTacToe(HumanPlayer('X'), BotPlayer('O'))
        game.board = [['X', 'O', 'X'], ['X', 'X', 'O'], ['O', 'X', 'O']]
        self.assertTrue(game.is_draw())

if __name__ == '__main__':
    unittest.main()
