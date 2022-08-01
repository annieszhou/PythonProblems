def blanks(array, index):
    indexes = []

    for i in range(len(array)):
        #print(i)
        for j in range(len(array[i])):
            #print('\t', j)

            if array[i][j] == " ":
                indexes.append([i, j])
    print(indexes)

    print(index)

    if index in indexes:
        blank = True

    else: 
        blank = False

    print(blank)

if __name__ == '__main__':
    print("Blanks")

    array_1 =   [["s", "m" ," ", "h"],
                 ["h", " ", " ", "s"],   
                 ["m", " ", "m", "m"]]

    index_1 = [0, 0]

    array_2 =    [[" ", " ", "r"],
                  [" ", " ", "p"]]
    
    index_2 = [0,0]
    
    blanks(array_1, index_1)
    blanks(array_2, index_2)

    