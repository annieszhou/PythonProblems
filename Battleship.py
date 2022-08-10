


def place_ship(array, integer, character, board):
    print("placing ship ...")

    if "R" is character:
        board[i//5][i%5]="S"
        board[i//5][i%5-1]="S"
        board[i//5][i%5-2]="S"

    if "L" is character:
        board[i//5][i%5]="S" 
        board[i//5][i%5+1]="S" 
        board[i//5][i%5+2]="S" 

    if "U" is character:
        board[i//5][i%5]="S" 
        board[i//5-1][i%5]="S" 
        board[i//5-2][i%5]="S" 

    if "D" is character:
        board [i//5][i%5]="S" 
        board[i//5+1][i%5]="S" 
        board[i//5+2][i%5]="S"



    
    


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

    place_ship(array_1, 15, "R")

    print("array_1")
