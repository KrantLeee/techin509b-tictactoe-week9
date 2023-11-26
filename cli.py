class GameCLI:
    @staticmethod
    def display_board(board):
        for i, row in enumerate(board):
            display_row = [' ' if cell is None else cell for cell in row]
            print(' | '.join(display_row))
            if i < 2:
                print('——' * 5)

    @staticmethod
    def get_user_input(prompt):
        return input(prompt)

    @staticmethod
    def get_game_mode():
        while True:
            mode = input("Choose a mode (1 for single-player, 2 for double-player, 3 for computer-vs-computer): ").strip()
            if mode in ['1', '2', '3']:
                return mode
            print("Invalid input. Please choose 1, 2 or 3.")
