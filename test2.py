from Kurang_i import *
from test import *

countID = 1
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
finalPuzzle = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]

def riseNode(node):
    global countID

    moveAvail = availableMove(node)
    simpulHidup = []
    for direction in moveAvail:
        countID = countID + 1
        temp = move(node, direction, countID)
        temp["gi"] = calculate_gi(temp["matrix"])
        temp["cost"] = temp["fi"] + temp["gi"]
        simpulHidup.append(temp)
        # print(move)
    return simpulHidup

def sortSimpulHidup(simpulHidup):
    temp = simpulHidup
    

simpulE = initialPuzzle
simpulH = riseNode(initialPuzzle)
simpulFinal = [initialPuzzle]
printMatrix(simpulE["matrix"])

for i in range(len(simpulH)):
    printMatrix(simpulH[i]["matrix"])
    print(simpulH[i])
    print()
