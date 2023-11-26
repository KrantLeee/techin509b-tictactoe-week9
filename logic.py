import random

class GameBoard:
    def __init__(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.winner = None

    def make_move(self, x, y, player):
        if self.is_valid_move(x, y):
            self.board[x][y] = player
            self.update_winner(player)
            return True
        return False

    def is_valid_move(self, x, y):
        return 0 <= x < 3 and 0 <= y < 3 and self.board[x][y] is None

    def update_winner(self, player):
        # Implement the logic to update the winner
        for i in range(3):
            if (self.board[i][0] == self.board[i][1] == self.board[i][2] == player or
                self.board[0][i] == self.board[1][i] == self.board[2][i] == player):
                self.winner = player
                return

        if (self.board[0][0] == self.board[1][1] == self.board[2][2] == player or
            self.board[0][2] == self.board[1][1] == self.board[2][0] == player):
            self.winner = player

    def get_winner(self):
        return self.winner

    def check_draw(self):
        return all(cell is not None for row in self.board for cell in row)

class Player:
    def __init__(self, symbol, board):
        self.symbol = symbol
        self.board = board

    def make_move(self):
        raise NotImplementedError


class HumanPlayer(Player):
    def make_move(self):
        while True:
            user_input = input('Please make your movement by typing x,y (e.g., 1,2):').strip().split(',')
            if len(user_input) == 2 and user_input[0].strip().isdigit() and user_input[1].strip().isdigit():
                x, y = int(user_input[0].strip()), int(user_input[1].strip())
                if 0 <= x < 3 and 0 <= y < 3:
                    return x, y
                else:
                    print("Invalid coordinates. Please enter values between 0 and 2.")
            else:
                print("Invalid input. Please enter in the format x,y.")


class ComputerPlayer(Player):
    def make_move(self):
        empty_cells = [(a, b) for a in range(3) for b in range(3) if self.board.board[a][b] is None]
        return random.choice(empty_cells)
