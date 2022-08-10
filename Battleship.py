def print_board(board):
    extra_line = "     |     |     |     |"
    new_line = "-----|-----|-----|-----|-----"
    
    print(extra_line)

    for i in range(5):
        print(" ", board[i][0], " | ", board[i][1], " | ", board[i][2], " | ", board[i][3], " | ", board[i][4])
        print(new_line)

    print(extra_line)



def place_ship(board, i, character):
    print("placing ship ...")


    if "R" == character and i//5 < 4:
        board[i//5][i%5]="S"
        board[i//5][i%5-1]="S"
        board[i//5][i%5-2]="S"

    elif "L" == character and i//5 > 2:
        board[i//5][i%5]="S" 
        board[i//5][i%5+1]="S" 
        board[i//5][i%5+2]="S" 

    elif "U" == character and i%5 < 4:
        board[i//5][i%5]="S" 
        board[i//5-1][i%5]="S" 
        board[i//5-2][i%5]="S" 

    elif "D" == character and i%5 > 2:
        board [i//5][i%5]="S" 
        board[i//5+1][i%5]="S" 
        board[i//5+2][i%5]="S"

    else:
        print( "not valid move")



    
    


if __name__ == '__main__':
    print("Battleship")



    array_1 = [["S", " ", " ", " ", " "],
               ["S", " ", " ", " ", " "],
               [" ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " "]]

    array_2 = [[" ", " ", " ", " ", " "],
               [" ", " ", " ", "S", "S"],
               [" ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " "]]

    print_board(array_1)

    place_ship(array_1, 3, "D")

    print_board(array_1)
