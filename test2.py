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

    return (simpulHidup)

def sortSimpulHidup(simpulHidup):
    tempSimpulHidup = simpulHidup
    for i in range(0, len(tempSimpulHidup)-1):
        minIdx = i
        for j in range (i+1, len(tempSimpulHidup)):
            if(tempSimpulHidup[j]["cost"] < tempSimpulHidup[minIdx]["cost"]):
                minIdx = j
        tempVal = tempSimpulHidup[minIdx]
        tempSimpulHidup[minIdx] = tempSimpulHidup[i]
        tempSimpulHidup[i] = tempVal

    return tempSimpulHidup

simpulE = {}
simpulFinal = []
simpulH = [initialPuzzle]
found = False
printMatrix(initialPuzzle["matrix"])

# for i in range(len(simpulH)):
#     printMatrix(simpulH[i]["matrix"])
#     print(simpulH[i])
#     print()

while(len(simpulH) != 0 and not found):
    simpulE = simpulH.pop(0)
    simpulFinal.append(simpulE)
    if(simpulE["matrix"] == finalPuzzle):
        simpulE["cost"] = simpulE["fi"]
        found = True
        break
    risedNode = riseNode(simpulE)
    for node in risedNode:
        simpulH.append(node)
    simpulH = sortSimpulHidup(simpulH)

print("== PATH SIMPUL FINAL ==")
for i in range(len(simpulFinal)):
    print(simpulFinal[i])
    print()
    printMatrix(simpulFinal[i]["matrix"])

print("== SIMPUL HIDUP ==")
for i in range(len(simpulH)):
    print(simpulH[i])
    print()
    printMatrix(simpulH[i]["matrix"])

print("== STATUS FOUND ==")
print(found)

