####	Tic-Tac-Toe with AI    ####

# Functions
def default():
    # Display welcome message
    print("\nWelcome! Let's play▶ TIC-TAC-TOE\n")


def rules():
    print("The 3 x 3 board will look like below: ⤵\n")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    # print("The positions of this 3 x 3 board is same as the right side of your key board.\n")
    print("\nYou just have to Enter↩ the position(1-9).")


def play():
    # Asking if the user is ready
    return input("\nAre you ready to play▶ the game? Enter↩ [Y]es or [N]o: ").upper().startswith('Y')


def names():
    # Input players names
    p1_name = input("\nEnter↩ NAME of 👱: ").capitalize()
    p2_name = input("Enter↩ NAME of 👱‍♀️: ").capitalize()
    return (p1_name, p2_name)


def choice():
    # Input players choice
    p1_choice = " "
    p2_choice = " "

    # while loop: if the entered value isn't X or O
    while p1_choice != "X" or p1_choice != "O":
        # while loop body begins
        p1_choice = input(f"\n{p1_name}, Do you want to be ❌ or ⭕?: ")[0].upper()
        # The input above has [0].upper() in the end,
        # So even if user enters x, X, xxxx or XXX the input will always be taken as X.
        # Hence, increasing the user input window.

        if p1_choice == "X" or p1_choice == "O":
            # if entered value is X or O, end the loop.
            break
        print("INVALID🚫 INPUT! Please Try Again!")
        # if the entered value isn't X or O, restart the while loop.
        # while loop body begins

    # Assigning the value to p2 and then diplaying the values
    if p1_choice == "X":
        p2_choice = "O"
    elif p1_choice == "O":
        p2_choice = "X"
    return (p1_choice, p2_choice)


def first_player():
    # This function will randomly decide who will play first
    import random
    return random.choice((0, 1))


def display_board(board, avail):
    print("    " + " {} | {} | {} ".format(board[1], board[2], board[3]) + "            " + " {} | {} | {} ".format(
        avail[1], avail[2], avail[3]))
    print("    " + "-----------" + "            " + "-----------")
    print("    " + " {} | {} | {} ".format(board[4], board[5], board[6]) + "            " + " {} | {} | {} ".format(
        avail[4], avail[5], avail[6]))
    print("    " + "-----------" + "            " + "-----------")
    print("    " + " {} | {} | {} ".format(board[7], board[8], board[9]) + "            " + " {} | {} | {} ".format(
        avail[7], avail[8], avail[9]))


def player_choice(board, name, choice):
    position = 0
    # Initialising position as 0^, so it passes through the while loop
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input(f"\n{name} ({choice}), Choose your next position: (1-9): "))

        if position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position) or position == "":
            # To check whether the given position is in the set [1-9] or whether it is empty or occupied
            print(f"INVALID🚫 INPUT. Please Try Again!\n")
    print("\n")
    return position


#####################################

# Functions to add AI to game
def CompAI(board, name, choice):
    position = 0
    possibilities = [x for x, letter in enumerate(board) if letter == " " and x != 0]

    # Including both X and O, since if AI will win, it will place a choice there,
    # but if the component will win ➡ we have to block that move
    for let in ["O", "X"]:
        for i in possibilities:
            # Creating a copy of the board everytime, placing the move and checking if it wins
            # Creating a copy like this and not this boardCopy = board, since changes to
            #  boardCopy changes the original board
            boardCopy = board[:]
            boardCopy[i] = let
            if (win_check(boardCopy, let)):
                position = i
                return position

    openCorners = [x for x in possibilities if x in [1, 3, 7, 9]]

    if len(openCorners) > 0:
        position = selectRandom(openCorners)
        return position

    if 5 in possibilities:
        position = 5
        return position

    openEdges = [x for x in possibilities if x in [2, 4, 6, 8]]

    if len(openEdges) > 0:
        position = selectRandom(openEdges)
        return position


def selectRandom(board):
    import random
    ln = len(board)
    r = random.randrange(0, ln)
    return board[r]


def place_marker(board, avail, choice, position):
    # To mark/replace the position on the board list
    board[position] = choice
    avail[position] = " "


def space_check(board, position):
    # To check whether the given position is empty or occupied
    return board[position] == " "


def full_board_check(board):
    # To check if the board is full, then the game is a draw
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def win_check(board, choice):
    # To check if one of the following patterns are true and then the respective player has won!;

    # Horizontal Check
    return (
            (board[1] == choice and board[2] == choice and board[3] == choice)
            or (board[4] == choice and board[5] == choice and board[6] == choice)
            or (board[7] == choice and board[8] == choice and board[9] == choice)
            # Vertical Check
            or (board[1] == choice and board[4] == choice and board[7] == choice)
            or (board[2] == choice and board[5] == choice and board[8] == choice)
            or (board[3] == choice and board[6] == choice and board[9] == choice)
            # Diagonal Check
            or (board[1] == choice and board[5] == choice and board[9] == choice)
            or (board[3] == choice and board[5] == choice and board[7] == choice)
    )


def delay(mode):
    if mode == 2:
        import time
        time.sleep(2)


def replay():
    # If the users want to play the game again?
    return input("\nDo you want to play again? 🔁 Enter↩ [Y]es or [N]o: ").lower().startswith("y")


# Main Program begins
input("Press ENTER↩ to start▶")
default()
rules()

#####################################

while True:

    # Creating the board as a list to be kept replacing it with user input
    theBoard = [" "] * 10

    # Creating the available options on the board
    available = [str(num) for num in range(0, 10)]  # a List Comprehension
    # available ➡ "0 1 2 3 4 5 6 7 8 9"

    print("\n0️⃣➡ 👱 🆚 🤖")
    print("1️⃣➡ 👱 🆚 👱‍♀️")
    print("2️⃣➡ 🤖 🆚 🤖")
    mode = int(input("\nSelect↩ an option 0, 1, or 2: "))

    # Mode for 👱 🆚 🤖
    if mode == 0:
        p1_name = input("\nEnter↩ NAME of 👱 who will go against the 🤖: ").capitalize()
        p2_name = "🤖"
        # Asking Choices Printing choices➡ X or O
        p1_choice, p2_choice = choice()
        print(f"\n👱{p1_name}:", p1_choice)
        print(f"{p2_name}:", p2_choice)

    # Mode for 👱 🆚 👱‍♀️
    elif mode == 1:
        # Asking Names
        p1_name, p2_name = names()
        # Asking Choices Printing choices➡ X or O
        p1_choice, p2_choice = choice()
        print(f"\n👱{p1_name}:", p1_choice)
        print(f"👱‍♀️{p2_name}:", p2_choice)

    # Mode for 🤖 🆚 🤖
    else:
        p1_name = "🤖1️⃣"
        p2_name = "🤖2️⃣"
        p1_choice, p2_choice = "X", "O"
        print(f"\n{p1_name}:", p1_choice)
        print(f"\n{p2_name}:", p2_choice)

    # Printing randomly who will go first
    if first_player():
        turn = p2_name
    else:
        turn = p1_name
    print(f"\n{turn} will go first!☝️")

    #  The user, if ready to play the game, output will be True or False
    if (mode == 2):
        ent = input("\nThis is going to be fast!⚡ Press Enter↩ for the battle⚔ to begin!\n")
        play_game = 1
    else:
        play_game = play()

    while play_game:

        #####################################
        # Player_1
        if turn == p1_name:

            # Displaying the board
            display_board(theBoard, available)

            # Position of the input
            if mode != 2:
                position = player_choice(theBoard, p1_name, p1_choice)
            else:
                position = CompAI(theBoard, p1_name, p1_choice)
                print(f"\n{p1_name} ({p1_choice}) have chosen position: {position}\n")

            # Replacing the " " at *position* to *p1_choice* in *theBoard* list
            place_marker(theBoard, available, p1_choice, position)

            # To check if Player_1 has won after the current input
            if win_check(theBoard, p1_choice):
                display_board(theBoard, available)
                print("\n************************************************")
                if (mode >= 0):
                    print(f"\nCONGRATULATIONS {p1_name}! You've won the Game! 🏆\n")
                play_game = False

            else:
                # To check if the board is full, if yes, the game is a draw
                if full_board_check(theBoard):
                    display_board(theBoard, available)
                    print("******************")
                    print("\nThe game is a DRAW ⚖!\n")
                    print("******************")
                    break
                # If none of the above is possible, next turn of Player_2
                else:
                    turn = p2_name

        #####################################
        # Player_2
        elif turn == p2_name:

            # Displaying the board
            display_board(theBoard, available)

            # Position of the input
            if (mode == 1):
                position = player_choice(theBoard, p2_name, p2_choice)
            else:
                position = CompAI(theBoard, p2_name, p2_choice)
                print(f"\n{p2_name} ({p2_choice}) have chosen position: {position}\n")

            # Replacing the " " at *position* to *p2_choice* in *theBoard* list
            place_marker(theBoard, available, p2_choice, position)

            # To check if Player_2 has won after the current input
            if win_check(theBoard, p2_choice):
                display_board(theBoard, available)
                print("\n************************************************")
                if (mode):
                    print(f"\nCONGRATULATIONS {p2_name}! You've won the Game! 🏆\n")
                else:
                    print("\nTHE 🤖 has won the Game! 🏆\n")
                print("************************************************")
                play_game = False

            else:
                # To check if the board is full, if yes, the game is a draw
                if full_board_check(theBoard):
                    display_board(theBoard, available)
                    print("******************")
                    print("\nThe game is a DRAW ⚖! 😑\n")
                    print("******************")
                    break
                # If none of the above is possible, next turn of Player_2
                else:
                    turn = p1_name

                    # If the users want to play the game again?
    if replay():
        # if Yes
        continue
    else:
        # if No
        break

    # Ending message
print("\n\n\t\t\t🏵THE END🏵")
