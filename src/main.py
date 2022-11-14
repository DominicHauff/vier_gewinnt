import player_class
import vier_gewinnt_board_class
import pymatrix

class Game:
    def __init__(self):
        self.board = vier_gewinnt_board_class.VierGewinntBoard()
        self.player1 = player_class.Player(number_1=True)
        self.player2 = player_class.Player(number_1=False)

    def game_loop(self):
        won = False
        who_won = 0
        while not won:
            print(pymatrix.matrix(self.board.board))
            valid_input = False
            while not valid_input:
                input_file = int(input("Player 1, enter file to play (1-7):"))
                if self.board.board[0][input_file] == 0:
                    self.board.add_chip(self.player1, input_file)
                    valid_input = True
                else:
                    print("File is full.")
            won = self.board.check_winner(self.board.last_played_position)
            if won:
                who_won = 1
                break
            print(pymatrix.matrix(self.board.board))
            valid_input = False
            while not valid_input:
                input_file = int(input("Player 2, enter file to play (1-7):"))
                if self.board.board[0][input_file] == 0:
                    self.board.add_chip(self.player1, input_file)
                    valid_input = True
                else:
                    print("File is full.")
            won = self.board.check_winner(self.board.last_played_position)
            if won:
                who_won = 2

        print(f'Congratulations player {who_won}, you won the game!!')


if __name__ == '__main__':
    game = Game()
    game.game_loop()






