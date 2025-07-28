import os


def clear_output():
    os.system("cls" if os.name == "nt" else "clear")


# Using List Comprehension for better readability
def display_board(board):
    clear_output()
    board_layout = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
    board_rows = ["|".join([board[i] for i in row]) for row in board_layout]
    print("\n-|-|-\n".join(board_rows))


# Taking user input for position choice, ensuring the input is valid and the position is not already occupied
# Acceptable values are from 1 to 9, representing the positions on the board
# The function will keep prompting the user until a valid choice is made


def position_choice(game_board, acceptable_values):

    choice = 0

    while choice not in acceptable_values or game_board[choice] != " ":

        print("Pick a position in between: ", acceptable_values)

        choice = int(input(" "))

        if choice not in acceptable_values:
            print("Sorry, invalid choice! ")

        elif game_board[choice] == "X" or game_board[choice] == "O":
            print("The position is already occupied")

    return choice


def game_on():

    user_input = input("\nDo you want to continue playing (Y/N): ")

    if user_input == "Y":
        return True
    elif user_input == "N":
        print("\nThanks for playing!")
        return False
    else:
        print("Invalid input, please enter Y or N")
        return game_on()  # Recursively call until valid input is received


# Function to select markers for the players
def marker_selection():

    marker = ""
    acceptable_values = ["X", "O"]

    print("=========== Welcome to the game of Tic Tac Toe ===========\n")
    while marker not in acceptable_values:

        marker = input("Player 1, choose X or O: ").upper()

        if marker not in acceptable_values:
            print("Sorry, I dont understand, please choose X or O")

        player1 = marker

        if player1 == "X":
            player2 = "O"
        else:
            player2 = "X"

    return (player1, player2)


# Function to check the status of the game board and if either player has won.
# It checks all possible winning combinations (rows, columns, diagonals) to determine if a player has won.


def check_status(game_board, marker_tuple):

    def winning_player(marker):

        player1_winner_ = False
        player2_winner_ = False

        # Checking if player 1 is the winner
        if marker_tuple[0] == game_board[marker]:
            player1_winner_ = True
            print("\nPlayer 1 is the winner")
        else:  # Checking if player 2 is the winner
            player2_winner_ = True
            print("\nPlayer 2 is the winner")

        return (player1_winner_, player2_winner_)

    player1_winner = False
    player2_winner = False

    # Check for winning conditions, specifically if any row, column, or diagonal has the same marker
    if game_board[1] != " " and game_board[1] == game_board[2] == game_board[3]:
        player1_winner, player2_winner = winning_player(1)
    elif game_board[4] != " " and game_board[4] == game_board[5] == game_board[6]:
        player1_winner, player2_winner = winning_player(4)
    elif game_board[7] != " " and game_board[7] == game_board[8] == game_board[9]:
        player1_winner, player2_winner = winning_player(7)
    elif game_board[1] != " " and game_board[1] == game_board[4] == game_board[7]:
        player1_winner, player2_winner = winning_player(1)
    elif game_board[2] != " " and game_board[2] == game_board[5] == game_board[8]:
        player1_winner, player2_winner = winning_player(2)
    elif game_board[3] != " " and game_board[3] == game_board[6] == game_board[9]:
        player1_winner, player2_winner = winning_player(3)
    elif game_board[1] != " " and game_board[1] == game_board[5] == game_board[9]:
        player1_winner, player2_winner = winning_player(9)
    elif game_board[7] != " " and game_board[7] == game_board[5] == game_board[3]:
        player1_winner, player2_winner = winning_player(7)
    else:
        pass

    return (player1_winner, player2_winner)


# Function to initialize the game variables and settings
# It sets up the game board, acceptable values for positions, and player markers.


def initialize_game():

    clear_output()
    acceptable_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    moves_ctr = 1
    player1_winner = False
    player2_winner = False
    pos_choice = 0
    game_board = [" "] * 10
    game_is_on = True

    player1_marker, player2_marker = marker_selection()
    marker_tuple = (player1_marker, player2_marker)

    return (
        game_board,
        acceptable_values,
        moves_ctr,
        player1_winner,
        player2_winner,
        pos_choice,
        game_is_on,
        marker_tuple,
    )


# Main game loop

if __name__ == "__main__":

    # Game initialization

    (
        game_board,
        acceptable_values,
        moves_ctr,
        player1_winner,
        player2_winner,
        pos_choice,
        game_is_on,
        marker_tuple,
    ) = initialize_game()

    while (player1_winner == False or player2_winner == False) and game_is_on:

        display_board(game_board)

        print("Now playing: Player 1 (", marker_tuple[0], ")")
        pos_choice = int(position_choice(game_board, acceptable_values))

        # Placing the marker for Player 1 and re-defining the acceptable values list
        game_board[pos_choice] = marker_tuple[0]
        acceptable_values[pos_choice - 1] = "N/A"

        moves_ctr += 1
        display_board(game_board)

        player1_winner, player2_winner = check_status(game_board, marker_tuple)

        # if player1 is the winner, then break the loop
        if player1_winner:
            game_is_on = game_on()

            if not game_is_on:
                break
            else:
                (
                    game_board,
                    acceptable_values,
                    moves_ctr,
                    player1_winner,
                    player2_winner,
                    pos_choice,
                    game_is_on,
                    marker_tuple,
                ) = initialize_game()
                continue

        print("Now playing: Player 2 (", marker_tuple[1], ")")
        pos_choice = int(position_choice(game_board, acceptable_values))

        # Placing the marker for Player 2 and re-defining the acceptable values list
        game_board[pos_choice] = marker_tuple[1]
        acceptable_values[pos_choice - 1] = "N/A"

        moves_ctr += 1
        display_board(game_board)

        player1_winner, player2_winner = check_status(game_board, marker_tuple)

        # if player2 is the winner, then break the loop
        if player2_winner:
            game_is_on = game_on()

            if not game_is_on:
                break
            else:
                (
                    game_board,
                    acceptable_values,
                    moves_ctr,
                    player1_winner,
                    player2_winner,
                    pos_choice,
                    game_is_on,
                    marker_tuple,
                ) = initialize_game()
                continue

        if moves_ctr >= 9:
            print("\nThe game has tied")
            game_is_on = game_on()

            if not game_is_on:
                break
            else:
                (
                    game_board,
                    acceptable_values,
                    moves_ctr,
                    player1_winner,
                    player2_winner,
                    pos_choice,
                    game_is_on,
                    marker_tuple,
                ) = initialize_game()
                continue
