# finalPuzzle = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

# puzzle = [1,3,4,15,2,16,5,12,7,6,11,14,8,9,10,13]
# puzzle = [1,2,3,4,5,6,16,8,9,10,7,11,13,14,15,12]

def kurang_i(i, puzzle):
    i_position = puzzle.index(i)
    sum = 0
    for pos in range(i_position + 1, len(puzzle)):
        if(puzzle[pos] < i):
            sum += 1
    return sum

def kurang_i_table(puzzle):
    tempArr = [0 for i in range(len(puzzle))]
    for i in range(len(puzzle)):
        kurangIResult = kurang_i(puzzle[i], puzzle)
        tempArr[puzzle[i]-1] = kurangIResult
    return tempArr

def sumOf_kurang_i(table):
    sum = 0
    for i in range(len(table)):
        sum += table[i]
    return sum

def kurangI_plusX(puzzle, kurang_i_sum):
    blankPos = puzzle.index(16) + 1
    tempVal = kurang_i_sum
    tempArr = [2,4,5,7,10,12,13,15]
    if (blankPos in tempArr):
        tempVal += 1
    return tempVal

def printKurangITable(array):
    # print("=== KURANG(i) TABLE ===")
    for i in range(len(array)):
        if(i < 9):
            print(f"> Kurang({i+1})  = {array[i]}")
        else:
            print(f"> Kurang({i+1}) = {array[i]}")

    print()

def transposeToMatrix(array):
    matrix = []
    baris = []
    for i in range(len(array)):
        baris.append(array[i])
        if ((i + 1) % 4 == 0):
            matrix.append(baris)
            baris = []
    return matrix

def printMatrix(matrix):
    for i in range(len(matrix)):
        print("> ", end="")
        for j in range(len(matrix[i])):
            if(matrix[i][j] / 10 < 1):
                print(f"{matrix[i][j]} ", end=" ")
            else:
                if(matrix[i][j] == 16):
                    print("  ", end=" ")
                else:
                    print(f"{matrix[i][j]}", end=" ")
        print()
    print()

# kurangI_table = kurang_i_table(puzzle)
# kurang_i_sum = sumOf_kurang_i(kurangI_table)

# print(f"Sum of Kurang(i): {kurang_i_sum}\n")
# printKurangITable(kurangI_table)

# isSolved = possibleToSolve(puzzle, kurang_i_sum)
# matrix1 = transposeToMatrix(finalPuzzle)
# matrix2 = transposeToMatrix(puzzle)

# printMatrix(matrix1)
# printMatrix(matrix2)

# if(isSolved):
#     print("Bisa di solved!")
# else:
#     print("Gabisa di solved!")
