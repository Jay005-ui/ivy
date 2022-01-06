print("-=" * 50)
print("WELCOME TO GAME 'TIC - TAC - TOE'")
print("-=" * 50)

table = [["", "", ""], ["", "", ""], ["", "", "_"]]

game_on = True
winner = None

player1 = input("player1 name = ")
symbol1 = input("select 'one' symbol of your choice = ")
print()
player2 = input("player2 name = ")
symbol2 = input("select 'one' symbol of your choice = ")

def display_table():
    print(table[0][0] + " | " + table[0][1] + " | " + table[0][2])
    print(table[1][0] + " | " + table[1][1] + " | " + table[1][2])
    print(table[2][0] + " | " + table[2][1] + " | " + table[2][2])

def start_game():
    print()
    display_table()
    print()

    print("-*" * 50)
    print("Game is set Start playing................")
    print("-*" * 50)

    while game_on:

        play_game()

        game_over()

    if winner == symbol1 or winner == symbol2:
        if winner == symbol1:
            print(f"{player1} won... the GAME ")
        if winner == symbol2:
            print(f"{player2} won... the Game")
    else:
        print("Tie...")

def players(player):
    print()
    print(f"{player} play your game.")

def positions(symbols):
    row = int(input(f"enter row position = "))
    column = int(input(f"enter column position = "))
    if [row, column] not in [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]:
        print()
        print("invalid input try again")
        positions(symbols)

    else:
        if table[row][column] == "_":
            table[row][column] = symbols
            print()
            display_table()
        else:
            print()
            print("invalid position please enter correct position")
            positions(symbols)


def play_game():
    players(player1)
    print()
    positions(symbol1)

    players(player2)
    print()
    positions(symbol2)

def game_over():
    check_winner()
    check_tie()

def check_winner():
    global winner
    row_winner = check_rows()

    column_winner = check_columns()

    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

    return

def check_tie():
    if "_" not in table:
        return False
    return

def check_rows():
    global game_on
    row_1 = table[0][0] == table[0][1] == table[0][2] != "_"
    row_2 = table[1][0] == table[1][1] == table[1][2] != "_"
    row_3 = table[2][0] == table[2][1] == table[2][2] != "_"

    if row_1 or row_2 or row_3:
        game_on = False
    if row_1:
        return table[0][0]
    elif row_2:
        return table[1][0]
    elif row_3:
        return table[2][0]

    return


def check_columns():
    global game_on
    column_1 = table[0][0] == table[1][0] == table[2][0] != "_"
    column_2 = table[0][1] == table[1][1] == table[2][1] != "_"
    column_3 = table[0][2] == table[1][2] == table[2][2] != "_"

    if column_1 or column_2 or column_3:
        game_on = False
    if column_1:
        return table[0][0]
    elif column_2:
        return table[1][0]
    elif column_3:
        return table[2][0]

    return

def check_diagonals():
    global game_on
    diagonal_1 = table[0][0] == table[1][1] == table[2][2] != "_"
    diagonal_2 = table[2][0] == table[1][1] == table[0][2] != "_"

    if diagonal_1 or diagonal_2:
        game_on = False
    if diagonal_1:
        return table[0][0]
    elif diagonal_2:
        return table[2][0]

    return


start_game()