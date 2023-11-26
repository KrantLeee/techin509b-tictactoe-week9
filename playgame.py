import logging
import csv
import os
from datetime import datetime
from logic import GameBoard, HumanPlayer, ComputerPlayer
from cli import GameCLI

#Basic configuration
logging.basicConfig(filename='logs/game_results.log', level=logging.INFO, 
                    format='%(asctime)s,%(message)s', datefmt='%Y-%m-%d %H:%M:%S')

logs_dir = 'logs'
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

class GameController:
    def __init__(self, game_mode):
        self.board = GameBoard()
        self.game_mode = game_mode
        self.players = self.create_players(game_mode)
        self.current_player_index = 0

    def create_players(self, game_mode):
        if game_mode == '1':
            return [HumanPlayer('X', self.board), ComputerPlayer('O', self.board)]
        elif game_mode == '2':
            return [HumanPlayer('X', self.board), HumanPlayer('O', self.board)]
        elif game_mode == '3':
            return [ComputerPlayer('X', self.board), ComputerPlayer('O', self.board)]

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def play(self):
        while not self.board.winner and not self.board.check_draw():
            current_player = self.players[self.current_player_index]
            move_made = False
            while not move_made:
                x, y = current_player.make_move()
                move_made = self.board.make_move(x, y, current_player.symbol)
                if not move_made and self.game_mode != '3':
                    print("Invalid move. Try again.")

            GameCLI.display_board(self.board.board)
            if self.board.get_winner() == current_player.symbol:
                print(f"{current_player.symbol} wins!")
                break

            if self.board.check_draw():
                print("It's a draw!")
                break

            self.switch_player()
    
        self.log_game_result()
    
    def log_game_result(self):
        winner = self.board.get_winner()
        is_draw = self.board.check_draw()
        result = 'Draw' if is_draw else ('Winner:' + winner if winner else 'No Result')

        logging.info(result) # Log to file using logging
        self.save_to_csv(winner, is_draw) #Save to CSV
    
    def save_to_csv(self, winner, is_draw):
        filename = 'logs/database.csv'
        
        #Check if file exists, if not create with header
        file_exists = os.path.isfile(filename)
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(['Date', 'Winner', 'Is_Draw'])
            
            writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), winner if winner else '', is_draw])





if __name__ == '__main__':
    game_mode = GameCLI.get_game_mode()
    game = GameController(game_mode)
    game.play()
