import time

from InputOutput import *
from Dependencies import *
from KurangI import *

countID = 1
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

print("==== PILIH METODE INPUT 15 PUZZLE ====")
print("> 1. Input dari Console")
print("> 2. Input dari File")
print("> 3. Input dari Random Generate")
print()

print("=== MASUKKAN COMMAND ===")
inputMethod = int(input("> "))
print()

initialPuzzleArray = []
if (inputMethod == 1):
    initialPuzzleArray = inputFromConsole()
elif (inputMethod == 2):
    initialPuzzleArray = inputFromFile()
elif (inputMethod == 3):
    initialPuzzleArray = inputRandomGenerate()
else:
    print("Error message!")

# initialPuzzleArray = [
#         # solve 
#         # 1,2,3,4,5,6,16,8,9,10,7,11,13,14,15,12
#         # unsolved
#         1,3,4,15,2,16,5,12,7,6,11,14,8,9,10,13
        
#         # 
#         # 12,6,1,7,13,10,8,16,4,9,5,15,2,14,3,11    
#         # 13,2,6,11,12,1,4,10,15,7,3,16,8,14,5,9
#         # 6,5,2,4,9,1,3,8,10,16,7,15,13,14,12,11
#         # 1,6,2,4,5,16,3,8,9,7,15,11,13,14,10,12
#         # 5,1,3,4,9,2,7,8,16,6,15,11,13,10,14,12
#     ]

timeTakes = 0.0

startTime = time.time()
kurangI_table = kurang_i_table(initialPuzzleArray)
kurangI_sum =  sumOf_kurang_i(kurangI_table)
kurangI_plus_x = kurangI_plusX(initialPuzzleArray, kurangI_sum)

timeTakes += (time.time() - startTime)

print("=== INITIAL MATRIX PUZZLE ===")
printMatrix(transposeToMatrix(initialPuzzleArray))

print("=== KURANG(i) TABLE ===")
printKurangITable(kurangI_table)

print("====== KURANG(i) + X ======")
print(f"> Sum Of Kurang(i) + X = {kurangI_plus_x}\n")

if (kurangI_plus_x % 2 == 0):
    startTime = time.time()
    initialPuzzle = {
        "id"        : 1,
        "idBefore"  : 0,
        "matrix"    : transposeToMatrix(initialPuzzleArray),
        "fi"        : 0,
        "gi"        : 0,
        "cost"      : 0,
        "lastMove"  : -1
    } 
    simpulE = {}
    simpulChecked = []
    pathSimpulFinal = []
    simpulH = [initialPuzzle]
    # found = False
    
    while(len(simpulH) != 0):
        simpulE = simpulH.pop(0)
        simpulChecked.append(simpulE)
        if(isMatrixGoal(simpulE["matrix"])):
            simpulE["cost"] = simpulE["fi"]
            pathSimpulFinal = getFinalPath(simpulChecked, simpulE["id"])
            # found = True
            timeTakes += (time.time() - startTime)
            break
        risedNode = riseNode(simpulE)
        for node in risedNode:
            simpulH.append(node)
        simpulH = sortSimpulHidup(simpulH)

    print("=== PATH SIMPUL FINAL ===")
    printPathSimpulFinal(pathSimpulFinal)

    print("================== WAKTU EKSEKUSI PROGRAM ==================")
    print(f"> Program berlangsung selama {format(timeTakes, '.23f')} detik\n")

    print("=== JUMLAH SIMPUL DIBANGKITKAN ===")
    print(f"> Banyak simpul dibangkitkan = {len(simpulChecked) + len(simpulH)}")
    print()
else:
    print("===== POSSIBLE FOUND STATUS =====")
    print("> Puzzle tidak dapat dipecahkan!\n")

    print("================== WAKTU EKSEKUSI PROGRAM ===================")
    print(f"> Program berlangsung selama {format(timeTakes, '.23f')} detik\n")