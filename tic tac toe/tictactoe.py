import random
from colorama import init, Fore, Style
init(autoreset=True)

def display_board(board):
    print()
    def colored(cell):
        if cell == 'X':
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == '0':
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL
    
    print(' ' + colored(board[0]) + ' | ' + colored(board[1]) + ' | ' + colored(board[2]))
    print('---' + '---' + '---')
    print(' ' + colored(board[3]) + ' | ' + colored(board[4]) + ' | ' + colored(board[5]))
    print('---' + '---' + '---')
    print(' ' + colored(board[6]) + ' | ' + colored(board[7]) + ' | ' + colored(board[8]))
    print()

def player_choice():
    symbol = ''
    while symbol not in ['X', '0']:
        symbol = input(Fore.GREEN + "Do you want to be X or 0? " + Style.RESET_ALL).upper()
    if symbol == 'X':
        return ('X', '0')
    else:
        return ('0', 'X')

def player_move(board, symbol):
    move = -1
    while move not in range(1, 10) or not board[move - 1].isdigit():
        try:
            move = int(input("Enter your move (1-9): "))
            if move not in range(1, 10) or not board[move - 1].isdigit():
                print("Invalid move. Please try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")
    board[move - 1] = symbol

def ai_move(board, ai_symbol, player_symbol):
    # Check for winning move
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = ai_symbol
            if check_win(board_copy, ai_symbol):
                board[i] = ai_symbol
                return
    
    # Block player's winning move
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = player_symbol
            if check_win(board_copy, player_symbol):
                board[i] = ai_symbol
                return
    
    # Random move if no winning or blocking move
    possible_moves = [i for i in range(9) if board[i].isdigit()]
    move = random.choice(possible_moves)
    board[move] = ai_symbol

def check_win(board, symbol):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == symbol:
            return True
    
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == symbol:
            return True
    
    # Check diagonals
    if board[0] == board[4] == board[8] == symbol:
        return True
    if board[2] == board[4] == board[6] == symbol:
        return True
    
    return False

def check_tie(board):
    for cell in board:
        if cell.isdigit():
            return False
    return True

def play_game():
    board = [str(i) for i in range(1, 10)]
    player_symbol, ai_symbol = player_choice()
    
    print(Fore.CYAN + "\nGame starts! You are " + player_symbol)
    display_board(board)
    
    # Determine who goes first
    current_turn = 'X' if player_symbol == 'X' else '0'
    
    while True:
        if current_turn == player_symbol:
            player_move(board, player_symbol)
            display_board(board)
            
            if check_win(board, player_symbol):
                print(Fore.GREEN + "Congratulations! You win!")
                break
            elif check_tie(board):
                print(Fore.YELLOW + "It's a tie!")
                break
            else:
                current_turn = ai_symbol
        else:
            print(Fore.MAGENTA + "AI's turn...")
            ai_move(board, ai_symbol, player_symbol)
            display_board(board)
            
            if check_win(board, ai_symbol):
                print(Fore.RED + "AI wins!")
                break
            elif check_tie(board):
                print(Fore.YELLOW + "It's a tie!")
                break
            else:
                current_turn = player_symbol

# Run the game
if __name__ == "__main__":
    play_game()