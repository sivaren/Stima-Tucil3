import numpy as np
from Dependencies import transposeToArray

# INPUT
# input puzzle dari console
def inputFromConsole():
    print("======= CONTOH MASUKKAN ======")
    print("> 1 2 3 4")
    print("> 5 6 7 8")
    print("> 9 10 11 12")
    print("> 13 14 15 16\n")
    print("> Angka 16 untuk kotak kosong")
    print("==============================\n")
    print("=== MASUKKAN MATRIX PUZZLE ===")
    
    arrTemp = [] 
    for i in range(4):
        line = input("> ")
        for num in line.split():
            arrTemp.append(int(num))
    print("===============================\n")

    return arrTemp

# input puzzle dari file
def inputFromFile():
    print("======= CONTOH MASUKKAN ======")
    print("> solve1.txt")
    print("==============================\n")
    print("=== MASUKKAN NAMA FILE ===")
    namaFile = input("> ")

    arrTemp = []
    with open("./testCase/" + namaFile) as f:
        lines = f.readlines()
    for line in lines:
        for num in line.split():
            arrTemp.append(int(num))
    print("==========================\n")

    return arrTemp

# input puzzle dari random generation
def inputRandomGenerate():
    print("===== RANDOM GENERATE =====")
    print("> Generate your 15 Puzzle")
    print("===========================\n")

    matrix = np.arange(1, 17)
    np.random.shuffle(matrix)
    matrix = np.reshape(matrix, (4,4))
    arrTemp = transposeToArray(matrix.tolist())

    return arrTemp

# OUTPUT
# menampilkan seluruh hasil fungsi kurang(i)
def printKurangITable(array):
    for i in range(len(array)):
        if(i < 9):
            print(f"> Kurang({i+1})  = {array[i]}")
        else:
            print(f"> Kurang({i+1}) = {array[i]}")

# menampilkan matrix
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

# menampilkan seluruh node dari matrix awal ke matrix akhir (Goal State)
def printPathSimpulFinal(pathSimpulFinal):
    for i in range(len(pathSimpulFinal)):
        print(f"> Step-{i}")
        printMatrix(pathSimpulFinal[i]["matrix"])
        
        if(i + 1 != len(pathSimpulFinal)):
            print()
