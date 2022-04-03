import numpy as np
from Kurang_i import *

def generateRandomMatrix():
    matrix = np.arange(1, 17)
    np.random.shuffle(matrix)

    matrix = np.reshape(matrix, (4,4))
    return matrix.tolist()
    
matrixTemp = generateRandomMatrix()
arrTemp = transposeToArray(matrixTemp)
print(matrixTemp)
print(arrTemp)
printMatrix(matrixTemp)