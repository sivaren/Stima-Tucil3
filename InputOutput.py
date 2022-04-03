import numpy as np
from Dependencies import transposeToArray

# INPUT
def inputFromConsole():
    arrTemp = [] 
    print("=== MASUKKAN MATRIX 15 PUZZLE ===")
    for i in range(4):
        line = input("> ")
        for num in line.split():
            arrTemp.append(int(num))
    print()

    return arrTemp

def inputFromFile():
    arrTemp = []
    print("=== MASUKKAN NAMA FILE ===")
    namaFile = input("> ")
    with open("./testCase/" + namaFile) as f:
        lines = f.readlines()
    for line in lines:
        for num in line.split():
            arrTemp.append(int(num))
    print()

    return arrTemp

def inputRandomGenerate():
    matrix = np.arange(1, 17)
    np.random.shuffle(matrix)
    matrix = np.reshape(matrix, (4,4))
    arrTemp = transposeToArray(matrix.tolist())

    return arrTemp

# OUTPUT
def printKurangITable(array):
    for i in range(len(array)):
        if(i < 9):
            print(f"> Kurang({i+1})  = {array[i]}")
        else:
            print(f"> Kurang({i+1}) = {array[i]}")
    print()

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

def printPathSimpulFinal(pathSimpulFinal):
    for i in range(len(pathSimpulFinal)):
        printMatrix(pathSimpulFinal[i]["matrix"])
    for i in range(len(pathSimpulFinal)):
        print(pathSimpulFinal[i])
