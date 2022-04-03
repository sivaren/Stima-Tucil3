import time

from InputOutput import *
from Dependencies import *
from KurangI import *

# countID untuk menghitung jumlah node yang telah di bangkitkan
countID = 1
# fungsi untuk membangkitkan simpul
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

# input angka untuk memilih metode input 15 puzzle
print("\n==== PILIH METODE INPUT 15 PUZZLE ====")
print("> 1. Input dari Console")
print("> 2. Input dari File")
print("> 3. Input dari Random Generate")
print("======================================\n")

print("=== MASUKKAN COMMAND ===")
inputMethod = input("> ")
print("========================\n")

# validasi input
while(inputMethod not in [1,2,3,'1','2','3']):
    print("=== MASUKKAN TIDAK VALID! ===")
    print("> PILIH ANGKA 1/2/3!")
    print("=============================\n")

    print("=== MASUKKAN COMMAND ===")
    inputMethod = input("> ")
    print("========================\n")

# inisialisasi puzzle sebagai array
initialPuzzleArray = []
if (int(inputMethod) == 1):
    initialPuzzleArray = inputFromConsole()
elif (int(inputMethod) == 2):
    initialPuzzleArray = inputFromFile()
elif (int(inputMethod) == 3):
    initialPuzzleArray = inputRandomGenerate()

timeTakes = 0.0         # inisialisasi waktu eksekusi
startTime = time.time() # waktu dimulai

# beberapa operasi terkait fungsi Kurang(i)
kurangI_table = kurang_i_table(initialPuzzleArray)
kurangI_sum =  sumOf_kurang_i(kurangI_table)
kurangI_plus_x = kurangI_plusX(initialPuzzleArray, kurangI_sum)

timeTakes += (time.time() - startTime)  # menambahkan waktu eksekusi program

print("=== INITIAL MATRIX PUZZLE ===")
printMatrix(transposeToMatrix(initialPuzzleArray))
print("=============================\n")

print("=== KURANG(i) TABLE ===")
printKurangITable(kurangI_table)
print("=======================\n")

print("=== SIGMA KURANG(i) + X ===")
print(f"> Sigma Kurang(i) + X = {kurangI_plus_x}")
print("===========================\n")

if (kurangI_plus_x % 2 == 0):
    startTime = time.time()     # waktu kembali dimulai

    # inisialisasi node awal puzzle
    initialPuzzle = {
        "id"        : 1,
        "idBefore"  : 0,
        "matrix"    : transposeToMatrix(initialPuzzleArray),
        "fi"        : 0,
        "gi"        : 0,
        "cost"      : 0,
        "lastMove"  : -1
    } 

    # inisialisasi simpulExpand, simpulChecked, pathSimpulFinal, dan simpulHidup
    simpulE = {}
    simpulChecked = []
    pathSimpulFinal = []
    simpulH = [initialPuzzle]
    
    while(len(simpulH) != 0):
        simpulE = simpulH.pop(0)
        simpulChecked.append(simpulE)

        # jika matrix sudah sesuai dengan goal, maka keluar dari loop
        if(isMatrixGoal(simpulE["matrix"])):
            simpulE["cost"] = simpulE["fi"]
            pathSimpulFinal = getFinalPath(simpulChecked, simpulE["id"])
            timeTakes += (time.time() - startTime)  # menambahkan waktu eksekusi program
            break

        # membangkitkan simpul dari simpul terkini
        risedNode = riseNode(simpulE)
        for node in risedNode:
            simpulH.append(node)
        # mengurutkan simpulHidup berdasarkan cost
        simpulH = sortSimpulHidup(simpulH)

    print("=== PATH SIMPUL FINAL ===")
    printPathSimpulFinal(pathSimpulFinal)
    print("=========================\n")

    print("================== WAKTU EKSEKUSI PROGRAM ==================")
    print(f"> Program berlangsung selama {format(timeTakes, '.23f')} detik")
    print("============================================================\n")

    print("==== JUMLAH SIMPUL DIBANGKITKAN ====")
    print(f"> Banyak simpul dibangkitkan = {len(simpulChecked) + len(simpulH)}")
    print("====================================\n")
else:
    print("============== POSSIBLE FOUND STATUS =============")
    print("> Puzzle tidak dapat dipecahkan!")
    print("> Dikarenakan Sigma Kurang(i) + X bernilai GANJIL")
    print("==================================================\n")

    print("================== WAKTU EKSEKUSI PROGRAM ===================")
    print(f"> Program berlangsung selama {format(timeTakes, '.23f')} detik")
    print("=============================================================\n")
