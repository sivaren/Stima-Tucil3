# fungsi untuk menghitung hasil dari kurang(i)
def kurang_i(i, puzzle):
    i_position = puzzle.index(i)
    sum = 0
    for pos in range(i_position + 1, len(puzzle)):
        if(puzzle[pos] < i):
            sum += 1
    
    return sum

# fungsi untuk menampung seluruh hasil dari fungsi kurang(i)
def kurang_i_table(puzzle):
    tempArr = [0 for i in range(len(puzzle))]
    for i in range(len(puzzle)):
        kurangIResult = kurang_i(puzzle[i], puzzle)
        tempArr[puzzle[i]-1] = kurangIResult

    return tempArr

# fungsi untuk mendapatkan jumlah dari seluruh hasil fungsi kurang(i)
def sumOf_kurang_i(table):
    sum = 0
    for i in range(len(table)):
        sum += table[i]
    
    return sum

# fungsi untuk mendapatkan nilai Sigma Kurang(i) + X
def kurangI_plusX(puzzle, kurang_i_sum):
    blankPos = puzzle.index(16) + 1
    tempVal = kurang_i_sum
    tempArr = [2,4,5,7,10,12,13,15]
    if (blankPos in tempArr):
        tempVal += 1
    
    return tempVal
