import numpy as np
from Kurang_i import printMatrix

# dict = {
#     "id" : 1,
#     "matrix" : [
#         [1,2,3,4],
#         [4,5,6,1],
#         [4,5,6,1],
#         [4,5,6,1],
#     ],
#     "cost" : 100,
#     "lastMove" : 12
# }

dict = [
    1,
    [
        [1,2,3,4],
        [4,5,6,1],
        [4,5,6,1],
        [4,5,6,1],
    ],
    100,
    12
]

temp = [
        [1,2,3],
        [4,5,16],
    ]

# print(dict)
# print(dict["id"])
# print(dict["matrix"])
# print(dict["cost"])
# print(dict["lastMove"])

# if (dict["cost"]==100):
#     print("hello")

# if (dict["matrix"]==temp):
#     print("matrix sama")

initialPuzzle = {
    "id" : 1,
    "matrix" : [
        [1,2,3,4],
        [5,6,16,8],
        [9,10,7,11],
        [13,14,15,12]
    ],
    "fi" : 0,
    "gi" : 0,
    "cost" : 0,
    "lastMove" : -1
}

# initialPuzzle = [
#     1,
#     [
#         [4,2,6,3],
#         [5,16,7,8],
#         [9,10,11,12],
#         [1,14,15,13]
#     ],
#     0,
#     0,
#     0,
#     -1
# ]

def getEmptyPosition(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i][j] == 16):
                return [i, j]

def availableMove(node):
    emptyPosition = getEmptyPosition(node["matrix"])
    availMove = []
    # cek move up
    if ((emptyPosition[0] - 1 >= 0) and node["lastMove"] != 2):
        availMove.append(0)
    # cek move right
    if ((emptyPosition[1] + 1 <= 3) and node["lastMove"] != 3):
        availMove.append(1)
    # cek move down
    if ((emptyPosition[0] + 1 <= 3) and node["lastMove"] != 0):
        availMove.append(2)
    # cek move left
    if ((emptyPosition[1] - 1 >= 0) and node["lastMove"] != 1):
        availMove.append(3)
    return availMove

def copyMatrix(matrix):
    temp = []
    baris = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            baris.append(matrix[i][j])
            if (j == len(matrix[i]) - 1):
                temp.append(baris)
                baris = []
    return temp

def move(node, direction, countID):
    newNode = {}
    newNode["id"] = countID
    newNode["matrix"] = []
    newNode["fi"] = node["fi"] + 1
    newNode["gi"] = 0
    newNode["cost"] = node["fi"] + 1
    newMatrix = copyMatrix(node["matrix"])
    emptyPosition = getEmptyPosition(node["matrix"])
    if (direction == 0):
        newMatrix[emptyPosition[0]][emptyPosition[1]] = node["matrix"][emptyPosition[0] - 1][emptyPosition[1]] 
        newMatrix[emptyPosition[0] - 1][emptyPosition[1]] = 16
        newNode["lastMove"] = 0
    elif (direction == 1):
        newMatrix[emptyPosition[0]][emptyPosition[1]] = node["matrix"][emptyPosition[0]][emptyPosition[1] + 1] 
        newMatrix[emptyPosition[0]][emptyPosition[1] + 1] = 16
        newNode["lastMove"] = 1
    elif (direction == 2):
        newMatrix[emptyPosition[0]][emptyPosition[1]] = node["matrix"][emptyPosition[0] + 1][emptyPosition[1]] 
        newMatrix[emptyPosition[0] + 1][emptyPosition[1]] = 16
        newNode["lastMove"] = 2
    else:
        newMatrix[emptyPosition[0]][emptyPosition[1]] = node["matrix"][emptyPosition[0]][emptyPosition[1] - 1] 
        newMatrix[emptyPosition[0]][emptyPosition[1] - 1] = 16
        newNode["lastMove"] = 3
    newNode["matrix"] = newMatrix
    return newNode

def calculate_gi(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j] != ((i * 4) + j + 1) and matrix[i][j] != 16):
                count += 1
    return count

# def move(node, direction, countID):
#     temp = []
#     temp.append(countID)
#     temp.append([])
#     temp.append(node[2] + 1)
#     temp.append(0)
#     temp.append(node[2] + 1)
#     temp[1] = copyMatrix(node[1])
#     emptyPosition = getEmptyPosition(temp[1])
#     if (direction == 0):
#         temp[1][emptyPosition[0]][emptyPosition[1]] = 6
#         temp[1][emptyPosition[0] - 1][emptyPosition[1]] = 16
#         temp.append(0)
#     # newNode[1] = newMatrix
#     return temp

# print(initialPuzzle["matrix"])
# print(copyMatrix(initialPuzzle["matrix"]))

printMatrix(initialPuzzle["matrix"])
# print(initialPuzzle)
newNodeUp = move(initialPuzzle, 0, 2)
newNodeUp["gi"] = calculate_gi(newNodeUp["matrix"])
newNodeUp["cost"] = newNodeUp["fi"] + newNodeUp["gi"]
newNodeRight = move(initialPuzzle, 1, 2)
newNodeRight["gi"] = calculate_gi(newNodeRight["matrix"])
newNodeRight["cost"] = newNodeRight["fi"] + newNodeRight["gi"]
newNodeDown = move(initialPuzzle, 2, 2)
newNodeDown["gi"] = calculate_gi(newNodeDown["matrix"])
newNodeDown["cost"] = newNodeDown["fi"] + newNodeDown["gi"]
newNodeLeft = move(initialPuzzle, 3, 2)
newNodeLeft["gi"] = calculate_gi(newNodeLeft["matrix"])
newNodeLeft["cost"] = newNodeLeft["fi"] + newNodeLeft["gi"]
printMatrix(newNodeUp["matrix"])
print(newNodeUp)
printMatrix(newNodeRight["matrix"])
print(newNodeRight)
printMatrix(newNodeDown["matrix"])
print(newNodeDown)
printMatrix(newNodeLeft["matrix"])
print(newNodeLeft)

# print(getEmptyPosition(initialPuzzle["matrix"]))
# availMove = availableMove(initialPuzzle)
# print(availMove)
# print(initialPuzzle)
