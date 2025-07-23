import os


def clear_output():
    os.system("cls" if os.name == "nt" else "clear")


def display_board(board):
    clear_output()
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("-|-|-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-|-|-")
    print(board[1] + "|" + board[2] + "|" + board[3])


def position_choice():

    global game_board
    global acceptable_values
    choice = 0

    while choice not in acceptable_values or game_board[choice] != " ":

        print("Pick a position in between: ", acceptable_values)

        choice = int(input(" "))

        if choice not in acceptable_values:
            print("Sorry, invalid choice! ")

        elif game_board[choice] == "X" or game_board[choice] == "O":
            print("The position is already occupied")

    return choice


def place_marker(position, marker):

    global game_board
    global acceptable_values

    game_board[position] = marker
    acceptable_values[position - 1] = "N/A"


def clear_board():

    global game_board
    clear_output()
    print("Board currently looks like this: ")
    display_board(game_board)

    user_input = input("Do you really want to clear the board (Y/N): ")

    if user_input == "Y":
        for i in range(0, 10):
            game_board[i] = " "
    else:
        pass

    clear_output()
    print("Board now looks like this: ")
    display_board(game_board)


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


def check_status():
    global game_board
    global player1_marker
    global player2_marker
    player1_winner = False
    player2_winner = False
    found_a_winner = False

    if game_board[1] != " " and game_board[1] == game_board[2] == game_board[3]:
        player1_winner, player2_winner, found_a_winner = winning_player(1)
    elif game_board[4] != " " and game_board[4] == game_board[5] == game_board[6]:
        player1_winner, player2_winner, found_a_winner = winning_player(4)
    elif game_board[7] != " " and game_board[7] == game_board[8] == game_board[9]:
        player1_winner, player2_winner, found_a_winner = winning_player(7)
    elif game_board[1] != " " and game_board[1] == game_board[4] == game_board[7]:
        player1_winner, player2_winner, found_a_winner = winning_player(1)
    elif game_board[2] != " " and game_board[2] == game_board[5] == game_board[8]:
        player1_winner, player2_winner, found_a_winner = winning_player(2)
    elif game_board[3] != " " and game_board[3] == game_board[6] == game_board[9]:
        player1_winner, player2_winner, found_a_winner = winning_player(3)
    elif game_board[1] != " " and game_board[1] == game_board[5] == game_board[9]:
        player1_winner, player2_winner, found_a_winner = winning_player(9)
    elif game_board[7] != " " and game_board[7] == game_board[5] == game_board[3]:
        player1_winner, player2_winner, found_a_winner = winning_player(7)
    else:
        pass

    return (player1_winner, player2_winner, found_a_winner)


def winning_player(marker):
    global player1_marker
    global player2_marker
    global game_board
    player1_winner = False
    player2_winner = False
    found_a_winner = False

    if player1_marker == game_board[marker]:
        player1_winner = True
        found_a_winner = True
        print("\nPlayer 1 is the winner")
    else:
        player2_winner = True
        found_a_winner = True
        print("\nPlayer 2 is the winner")

    return (player1_winner, player2_winner, found_a_winner)


# Main game loop

if __name__ == "__main__":

    # Variable initialization

    acceptable_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    moves_ctr = 1
    found_a_winner = False
    player1_winner = False
    player2_winner = False
    pos_choice = 0
    game_board = [" "] * 10

    clear_output()
    player1_marker, player2_marker = marker_selection()

    while (
        player1_winner == False or player2_winner == False
    ) and found_a_winner == False:

        display_board(game_board)

        print("Now playing: Player 1 (", player1_marker, ")")
        pos_choice = int(position_choice())

        place_marker(pos_choice, player1_marker)
        moves_ctr += 1
        display_board(game_board)
        player1_winner, player2_winner, found_a_winner = check_status()

        if player1_winner and found_a_winner:
            break

        print("Now playing: Player 2 (", player2_marker, ")")
        pos_choice = int(position_choice())

        place_marker(pos_choice, player2_marker)
        moves_ctr += 1
        display_board(game_board)
        player1_winner, player2_winner, found_a_winner = check_status()

        if moves_ctr >= 9:
            print("\nThe game has tied")
            break
