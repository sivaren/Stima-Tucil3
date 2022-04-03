# fungsi untuk transpose dari array ke matrix
def transposeToMatrix(array):
    matrix = []
    baris = []
    for i in range(len(array)):
        baris.append(array[i])
        if ((i + 1) % 4 == 0):
            matrix.append(baris)
            baris = []

    return matrix

# fungsi untuk transpose dari matrix ke array
def transposeToArray(matrix):
    array = []
    for row in matrix:
        for col in row:
            array.append(col)

    return array

# fungsi untuk meng-copy matrix
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

# fungsi untuk mengecek apakah suatu matrix
# sudah sama dengan Goal state
def isMatrixGoal(matrix):
    finalMatrix =  [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i][j] != finalMatrix[i][j]):
                return False

    return True

# fungsi untuk mendapatkan koordinat angka 16 (kotak kosong)
# dari suatu matrix
def getEmptyPosition(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i][j] == 16):
                return [i, j]

# fungsi untuk mendapatkan arah gerakan 
# dari kotak kosong yang mungkin dilakukan
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

# fungsi untuk mendapatkan state matrix yang 
# telah melakukan gerakan tertentu dari state matrix sebelumnya
def move(node, direction, countID):
    newNode = {}
    newNode["id"] = countID
    newNode["idBefore"] = node["id"]
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

# fungsi untuk menghitung cost g(i) dari suatu state
def calculate_gi(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j] != ((i * 4) + j + 1) and matrix[i][j] != 16):
                count += 1

    return count

# fungsi untuk mengurutkan collection dari simpul hidup
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

# fungsi untuk mendapatkan node dengan ID tertentu
# dari node yang telah di cek/kunjungi
def findNode(simpulChecked, nodeID):
    for node in simpulChecked:
        if node["id"] == nodeID:
            return node

# fungsi untuk mendapatkan seluruh node 
# dari matrix awal ke matrix akhir (Goal State)
def getFinalPath(simpulChecked, finalNodeID):
    node = findNode(simpulChecked, finalNodeID)
    temp = []
    temp.append(node)

    while(node["idBefore"] != 0):
        node = findNode(simpulChecked, node["idBefore"])
        temp.append(node)
    temp.reverse()

    return temp
